#!/usr/bin/env python3
"""
Project Cataloger & Wiki Generator
===================================
Scans ~/VisualStudio projects, categorizes them, extracts metadata,
tracks changes over time, and generates a Markdown wiki.

Usage:
    python3 cataloger.py                    # Full scan + wiki generation
    python3 cataloger.py --diff             # Show changes since last scan
    python3 cataloger.py --category trading # Scan only one category
    python3 cataloger.py --watch            # Watch mode (rescan every 5 min)
"""

import os
import sys
import json
import hashlib
import subprocess
import re
import argparse
import time
from datetime import datetime, timezone
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Optional, Tuple

# ═══════════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════════

BASE_DIR = Path("/Users/andriy/VisualStudio")
CATALOG_DIR = BASE_DIR / "project_cataloger"
WIKI_DIR = CATALOG_DIR / "wiki"
STATE_FILE = CATALOG_DIR / "catalog_state.json"
HISTORY_DIR = CATALOG_DIR / "history"

CODE_EXTENSIONS = {".py", ".ipynb", ".js", ".ts", ".jsx", ".tsx", ".sh", ".sql"}
DOC_EXTENSIONS = {".md", ".txt", ".rst", ".html"}
CONFIG_EXTENSIONS = {".json", ".yaml", ".yml", ".toml", ".cfg", ".ini", ".env"}
DATA_EXTENSIONS = {".csv", ".parquet", ".xlsx", ".db", ".sqlite"}
ALL_EXTENSIONS = CODE_EXTENSIONS | DOC_EXTENSIONS | CONFIG_EXTENSIONS | DATA_EXTENSIONS

SKIP_DIRS = {
    "node_modules", ".git", "__pycache__", ".venv", "venv", "env",
    ".tox", ".mypy_cache", ".pytest_cache", "dist", "build",
    ".next", ".nuxt", "coverage", ".cache", ".eggs",
}

# ═══════════════════════════════════════════════════════════════
# PROJECT CATEGORIES — auto-detection rules
# ═══════════════════════════════════════════════════════════════

CATEGORIES = {
    "predictors_models": {
        "icon": "🔮",
        "title": "Predictors & Models",
        "description": "ML модели предсказания цен, Markov chains, pattern recognition",
        "keywords": ["predictor", "markov", "pattern", "bottom-model", "base-states", "meta-labeling"],
    },
    "trading_strategies": {
        "icon": "📊",
        "title": "Trading Strategies",
        "description": "Торговые стратегии, бэктесты, оптимизация параметров",
        "keywords": ["strategy", "strat", "trading_service", "freqtrade", "adaptive_exit",
                     "trailing", "c2-strategy", "check_strategies", "volatility", "signal-emulator"],
    },
    "profitradar_platform": {
        "icon": "🚀",
        "title": "ProfitRadar Platform",
        "description": "Платформа ProfitRadar — UI, backend, API, landing pages",
        "keywords": ["profitradar", "profit-radar", "ProfitRadar", "indicators-basic", "scalping"],
    },
    "llm_ai_training": {
        "icon": "🧠",
        "title": "LLM & AI Training",
        "description": "LLM обучение, синтетические датасеты, RAG, AI советники",
        "keywords": ["llm", "synds", "synthetic", "ai-trading", "claude-server", "Framework"],
    },
    "data_analytics": {
        "icon": "📈",
        "title": "Data & Analytics",
        "description": "Сбор данных, пайплайны, аналитика, визуализация",
        "keywords": ["data_collection", "pipeline", "best-strat-pipeline", "bruteforce",
                     "polars", "predictor-visualization", "predictor-analysis",
                     "financial-data", "funding-rate", "dashboard"],
    },
    "defi_crypto": {
        "icon": "💰",
        "title": "DeFi & Crypto Tools",
        "description": "DeFi инструменты, арбитраж, Polymarket, токен-аналитика",
        "keywords": ["polymarket", "adi-token", "ff_arbitrage", "ff", "antigravity",
                     "aviator", "trade-fun"],
    },
    "portfolio_risk": {
        "icon": "📐",
        "title": "Portfolio & Risk",
        "description": "Портфельная оптимизация, риск-менеджмент, ребалансировка",
        "keywords": ["portfolio", "prtf", "sharp", "shares", "stress",
                     "ai powered", "pair trading", "statical arb"],
    },
    "infrastructure": {
        "icon": "🛠",
        "title": "Infrastructure & Tools",
        "description": "Инфраструктура, MCP серверы, деплой, мониторинг",
        "keywords": ["claude-server", "financial-data-mcp", "llm-cost-tracker",
                     "live-predictor-system", "hybrid_model", "docker",
                     "development plans", "dataintelligence"],
    },
    "business_pitch": {
        "icon": "🎯",
        "title": "Business & Pitch",
        "description": "Бизнес-планы, презентации, оценки, pitch materials",
        "keywords": ["pitch", "biounity", "cases", "buyers_insite",
                     "strategy-market", "music", "resorts"],
    },
}


# ═══════════════════════════════════════════════════════════════
# PROJECT SCANNER
# ═══════════════════════════════════════════════════════════════

class ProjectScanner:
    def __init__(self, project_path: Path):
        self.path = project_path
        self.name = project_path.name

    def scan(self) -> dict:
        meta = {
            "name": self.name,
            "path": str(self.path),
            "scanned_at": datetime.now(timezone.utc).isoformat(),
            "category": self._detect_category(),
            "git": self._git_info(),
            "files": self._scan_files(),
            "readme": self._extract_readme(),
            "tech_stack": self._detect_tech_stack(),
            "status": "unknown",
        }
        meta["status"] = self._infer_status(meta)
        meta["summary"] = self._build_summary(meta)
        return meta

    def _detect_category(self) -> str:
        name_lower = self.name.lower()
        for cat_id, cat_info in CATEGORIES.items():
            for kw in cat_info["keywords"]:
                if kw.lower() in name_lower or name_lower in kw.lower():
                    return cat_id
        return "uncategorized"

    def _git_info(self) -> Optional[dict]:
        git_dir = self.path / ".git"
        if not git_dir.exists():
            return None
        try:
            def git_cmd(args):
                r = subprocess.run(
                    ["git"] + args, cwd=self.path,
                    capture_output=True, text=True, timeout=10
                )
                return r.stdout.strip() if r.returncode == 0 else None

            last_date = git_cmd(["log", "-1", "--all", "--format=%aI"])
            last_msg = git_cmd(["log", "-1", "--all", "--format=%s"])
            
            latest_ref = git_cmd(["for-each-ref", "--sort=-committerdate", "refs/heads/", "refs/remotes/", "--format=%(refname:short)", "--count=1"])
            if latest_ref and latest_ref.startswith("origin/"):
                latest_ref = latest_ref[7:]
            branch = latest_ref or git_cmd(["rev-parse", "--abbrev-ref", "HEAD"])
            
            count = git_cmd(["rev-list", "--count", "--all"])
            recent = git_cmd(["log", "--all", "--since=30 days ago", "--oneline"])
            recent_count = len(recent.split("\n")) if recent else 0

            # Get last 5 commits for timeline
            last5 = git_cmd(["log", "-5", "--all", "--format=%aI|||%s"])
            timeline = []
            if last5:
                for line in last5.split("\n"):
                    if "|||" in line:
                        d, m = line.split("|||", 1)
                        timeline.append({"date": d, "msg": m})

            return {
                "branch": branch,
                "last_commit_date": last_date,
                "last_commit_msg": last_msg,
                "commit_count": int(count) if count else 0,
                "recent_commits_30d": recent_count,
                "timeline": timeline,
            }
        except Exception as e:
            return {"error": str(e)}

    def _scan_files(self) -> dict:
        stats = defaultdict(lambda: {"count": 0, "total_size": 0, "files": []})
        total = 0
        for root, dirs, files in os.walk(self.path):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
            for f in files:
                ext = Path(f).suffix.lower()
                if ext not in ALL_EXTENSIONS:
                    continue
                fpath = Path(root) / f
                try:
                    size = fpath.stat().st_size
                    mtime = datetime.fromtimestamp(
                        fpath.stat().st_mtime, tz=timezone.utc
                    ).isoformat()
                except OSError:
                    continue
                rel = str(fpath.relative_to(self.path))
                total += 1
                if ext in CODE_EXTENSIONS:
                    ftype = "code"
                elif ext in DOC_EXTENSIONS:
                    ftype = "docs"
                elif ext in CONFIG_EXTENSIONS:
                    ftype = "config"
                else:
                    ftype = "data"
                stats[ftype]["count"] += 1
                stats[ftype]["total_size"] += size
                depth = len(Path(rel).parts)
                important = any(k in f.lower() for k in [
                    "readme", "main", "app", "config", "setup",
                    "requirements", "dockerfile", "docker-compose",
                    "makefile", "changelog", "todo", "plan"
                ])
                if depth <= 2 or important:
                    stats[ftype]["files"].append({
                        "path": rel, "size": size, "modified": mtime,
                    })
        return {"total_indexed": total, "by_type": {k: dict(v) for k, v in stats.items()}}

    def _extract_readme(self) -> Optional[str]:
        for name in ["README.md", "readme.md", "README.txt", "README"]:
            p = self.path / name
            if p.exists():
                try:
                    return p.read_text(errors="ignore")[:2000]
                except Exception:
                    pass
        return None

    def _detect_tech_stack(self) -> dict:
        stack = {"languages": set(), "frameworks": set(), "tools": set()}
        checks = {
            "requirements.txt": ("Python", "pip"),
            "setup.py": ("Python", None),
            "pyproject.toml": ("Python", None),
            "package.json": ("JavaScript/TypeScript", "npm"),
            "Dockerfile": (None, "Docker"),
            "docker-compose.yml": (None, "Docker Compose"),
            "Makefile": (None, "Make"),
        }
        for fname, (lang, tool) in checks.items():
            if (self.path / fname).exists():
                if lang: stack["languages"].add(lang)
                if tool: stack["tools"].add(tool)
        # Parse requirements.txt
        req = self.path / "requirements.txt"
        if req.exists():
            try:
                txt = req.read_text(errors="ignore").lower()
                fw = {"fastapi":"FastAPI","flask":"Flask","streamlit":"Streamlit",
                      "pandas":"Pandas","numpy":"NumPy","torch":"PyTorch",
                      "sklearn":"scikit-learn","freqtrade":"Freqtrade","ccxt":"CCXT",
                      "polars":"Polars","plotly":"Plotly","langchain":"LangChain",
                      "openai":"OpenAI API","gradio":"Gradio"}
                for k,v in fw.items():
                    if k in txt: stack["frameworks"].add(v)
            except Exception: pass
        # Parse package.json
        pkg = self.path / "package.json"
        if pkg.exists():
            try:
                p = json.loads(pkg.read_text(errors="ignore"))
                deps = {**p.get("dependencies",{}), **p.get("devDependencies",{})}
                js = {"react":"React","next":"Next.js","vue":"Vue.js",
                      "tailwindcss":"Tailwind CSS","typescript":"TypeScript","vite":"Vite"}
                for k,v in js.items():
                    if k in deps: stack["frameworks"].add(v)
            except Exception: pass
        return {k: sorted(v) for k, v in stack.items()}

    def _infer_status(self, meta: dict) -> str:
        git = meta.get("git")
        if not git or "error" in (git or {}):
            return "📁 no-git"
        if git.get("recent_commits_30d", 0) > 0:
            return "🟢 active"
        try:
            last = datetime.fromisoformat(git["last_commit_date"])
            days = (datetime.now(timezone.utc) - last).days
            if days < 90: return "🟡 recent"
            elif days < 365: return "🟠 dormant"
            else: return "🔴 archived"
        except Exception:
            return "⚪ unknown"

    def _build_summary(self, meta: dict) -> str:
        f = meta["files"]
        code = f["by_type"].get("code", {}).get("count", 0)
        docs = f["by_type"].get("docs", {}).get("count", 0)
        parts = [f"{code} code, {docs} docs"]
        s = meta["tech_stack"]
        if s["languages"]: parts.append(", ".join(s["languages"]))
        if s["frameworks"]: parts.append(", ".join(s["frameworks"][:4]))
        return " | ".join(parts)


# ═══════════════════════════════════════════════════════════════
# CATALOG ENGINE — orchestrates scanning & state
# ═══════════════════════════════════════════════════════════════

class CatalogEngine:
    def __init__(self):
        self.projects = {}
        self.previous_state = self._load_state()

    def _load_state(self) -> dict:
        if STATE_FILE.exists():
            try:
                return json.loads(STATE_FILE.read_text())
            except Exception:
                pass
        return {}

    def _save_state(self):
        STATE_FILE.write_text(json.dumps(self.projects, indent=2, default=str))
        # Also save timestamped snapshot
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        hist = HISTORY_DIR / f"catalog_{ts}.json"
        hist.write_text(json.dumps(self.projects, indent=2, default=str))

    def scan_all(self, category_filter=None):
        GITLAB_DIR = Path("/Users/andriy/gitlab-prod")
        print(f"\n{'='*60}")
        print(f"  PROJECT CATALOGER — Scanning {BASE_DIR} and {GITLAB_DIR}")
        print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*60}\n")

        # Collect directories from both paths
        dir_map = {}
        
        # 1. First add gitlab-prod projects
        if GITLAB_DIR.exists():
            for e in sorted(GITLAB_DIR.iterdir()):
                if e.is_dir() and e.name not in SKIP_DIRS and not e.name.startswith("."):
                    dir_map[e.name] = e
                    
        # 2. Add VisualStudio projects (overwriting gitlab-prod if same name)
        if BASE_DIR.exists():
            # Apply some well-known mappings from gitlab to local
            GITLAB_TO_LOCAL = {
                "profitradar_ui": "profitradar",
                "profit-radar-io": "profitradar-api",
                "profitradar-landings": "profitradar-landing",
                "funding-rate-miner-master 2": "funding-rate-miner"
            }
            
            for e in sorted(BASE_DIR.iterdir()):
                if e.is_dir() and e.name not in SKIP_DIRS and e.name != "project_cataloger":
                    # If this local name maps to a specific gitlab name, use the gitlab name as key
                    mapped_name = GITLAB_TO_LOCAL.get(e.name, e.name)
                    dir_map[mapped_name] = e

        dirs = sorted(dir_map.values(), key=lambda d: d.name)

        print(f"Found {len(dirs)} project directories\n")

        for i, d in enumerate(dirs, 1):
            scanner = ProjectScanner(d)
            cat = scanner._detect_category()

            if category_filter:
                if category_filter.lower() not in cat.lower():
                    continue

            print(f"  [{i:2d}/{len(dirs)}] Scanning: {d.name}...", end="", flush=True)
            meta = scanner.scan()
            self.projects[d.name] = meta
            cat_info = CATEGORIES.get(cat, {"icon": "📦", "title": "Uncategorized"})
            print(f" {meta['status']} {cat_info['icon']} {cat_info['title']}")

        self._save_state()
        print(f"\n✅ Scanned {len(self.projects)} projects. State saved.")
        return self.projects

    def diff(self) -> List[str]:
        changes = []
        prev_names = set(self.previous_state.keys())
        curr_names = set(self.projects.keys())

        for name in curr_names - prev_names:
            changes.append(f"➕ NEW: {name}")
        for name in prev_names - curr_names:
            changes.append(f"➖ REMOVED: {name}")
        for name in curr_names & prev_names:
            old = self.previous_state[name]
            new = self.projects[name]
            # Check git changes
            old_git = old.get("git") or {}
            new_git = new.get("git") or {}
            if old_git.get("last_commit_date") != new_git.get("last_commit_date"):
                changes.append(
                    f"🔄 UPDATED: {name} — "
                    f"{new_git.get('last_commit_msg', '?')}"
                )
            # Check file count changes
            old_files = old.get("files", {}).get("total_indexed", 0)
            new_files = new.get("files", {}).get("total_indexed", 0)
            if old_files != new_files:
                diff = new_files - old_files
                sign = "+" if diff > 0 else ""
                changes.append(f"📝 FILES: {name} ({sign}{diff} files)")
        return changes


# ═══════════════════════════════════════════════════════════════
# WIKI GENERATOR — creates Markdown wiki from catalog
# ═══════════════════════════════════════════════════════════════

class WikiGenerator:
    def __init__(self, projects: dict):
        self.projects = projects

    def generate(self):
        print(f"\n📚 Generating Wiki in {WIKI_DIR}...")
        WIKI_DIR.mkdir(parents=True, exist_ok=True)

        self._gen_index()
        self._gen_category_pages()
        self._gen_project_pages()
        self._gen_timeline()
        self._gen_tech_matrix()
        self._gen_status_dashboard()

        print(f"✅ Wiki generated! Open: {WIKI_DIR / 'INDEX.md'}")

    def _gen_index(self):
        lines = [
            "# 🏠 Project Wiki — VisualStudio Catalog",
            "",
            f"*Автосгенерировано: {datetime.now().strftime('%Y-%m-%d %H:%M')}*",
            f"*Всего проектов: {len(self.projects)}*",
            "",
            "## 📋 Навигация",
            "",
            "| Страница | Описание |",
            "|----------|----------|",
            "| [Status Dashboard](STATUS.md) | Статус всех проектов |",
            "| [Timeline](TIMELINE.md) | Хронология изменений |",
            "| [Tech Matrix](TECH_MATRIX.md) | Технологии по проектам |",
            "",
            "## 📁 Категории",
            "",
        ]
        # Group by category
        by_cat = defaultdict(list)
        for p in self.projects.values():
            by_cat[p["category"]].append(p)

        for cat_id, cat_info in CATEGORIES.items():
            projs = by_cat.get(cat_id, [])
            if not projs:
                continue
            icon = cat_info["icon"]
            title = cat_info["title"]
            lines.append(f"### {icon} [{title}](categories/{cat_id}.md)")
            lines.append(f"*{cat_info['description']}*")
            lines.append("")
            for p in sorted(projs, key=lambda x: x["name"]):
                status = p["status"].split()[0]
                lines.append(f"- {status} [{p['name']}](projects/{p['name']}.md) — {p['summary']}")
            lines.append("")

        # Uncategorized
        uncat = by_cat.get("uncategorized", [])
        if uncat:
            lines.append("### 📦 Uncategorized")
            lines.append("")
            for p in sorted(uncat, key=lambda x: x["name"]):
                status = p["status"].split()[0]
                lines.append(f"- {status} [{p['name']}](projects/{p['name']}.md) — {p['summary']}")
            lines.append("")

        (WIKI_DIR / "INDEX.md").write_text("\n".join(lines))

    def _gen_category_pages(self):
        cat_dir = WIKI_DIR / "categories"
        cat_dir.mkdir(exist_ok=True)

        by_cat = defaultdict(list)
        for p in self.projects.values():
            by_cat[p["category"]].append(p)

        for cat_id, cat_info in CATEGORIES.items():
            projs = by_cat.get(cat_id, [])
            if not projs:
                continue
            lines = [
                f"# {cat_info['icon']} {cat_info['title']}",
                "",
                f"*{cat_info['description']}*",
                "",
                f"**Проектов: {len(projs)}**",
                "",
                "| Проект | Статус | Файлы | Стек | Последний коммит |",
                "|--------|--------|-------|------|-----------------|",
            ]
            for p in sorted(projs, key=lambda x: (x.get("git") or {}).get("last_commit_date", "") or "", reverse=True):
                git = p.get("git") or {}
                last_raw = git.get("last_commit_date") or "—"
                last = last_raw[:10] if last_raw else "—"
                code = p["files"]["by_type"].get("code", {}).get("count", 0)
                fw = ", ".join(p["tech_stack"].get("frameworks", [])[:3]) or "—"
                lines.append(
                    f"| [{p['name']}](../projects/{p['name']}.md) "
                    f"| {p['status']} | {code} | {fw} | {last} |"
                )
            lines.append("")
            (cat_dir / f"{cat_id}.md").write_text("\n".join(lines))

    def _gen_project_pages(self):
        proj_dir = WIKI_DIR / "projects"
        proj_dir.mkdir(exist_ok=True)

        for p in self.projects.values():
            cat_info = CATEGORIES.get(p["category"], {"icon": "📦", "title": "Uncategorized"})
            lines = [
                f"# {p['name']}",
                "",
                f"**Категория:** {cat_info['icon']} [{cat_info['title']}](../categories/{p['category']}.md)",
                f"**Статус:** {p['status']}",
                f"**Путь:** `{p['path']}`",
                "",
            ]
            # Git info
            git = p.get("git")
            if git and "error" not in git:
                lines.extend([
                    "## 📊 Git",
                    "",
                    f"- **Branch:** `{git.get('branch', '?')}`",
                    f"- **Коммитов:** {git.get('commit_count', '?')}",
                    f"- **Последний:** {(git.get('last_commit_date') or '?')[:10]}",
                    f"- **Сообщение:** {git.get('last_commit_msg', '?')}",
                    f"- **За 30 дней:** {git.get('recent_commits_30d', 0)} коммитов",
                    "",
                ])
                if git.get("timeline"):
                    lines.append("### Последние коммиты")
                    lines.append("")
                    for t in git["timeline"]:
                        lines.append(f"- `{t['date'][:10]}` {t['msg']}")
                    lines.append("")

            # Tech stack
            s = p["tech_stack"]
            if any(s.values()):
                lines.extend(["## 🛠 Tech Stack", ""])
                if s["languages"]: lines.append(f"- **Languages:** {', '.join(s['languages'])}")
                if s["frameworks"]: lines.append(f"- **Frameworks:** {', '.join(s['frameworks'])}")
                if s["tools"]: lines.append(f"- **Tools:** {', '.join(s['tools'])}")
                lines.append("")

            # Files
            files = p["files"]
            lines.extend([
                f"## 📁 Files ({files['total_indexed']} indexed)",
                "",
            ])
            for ftype, info in files["by_type"].items():
                size_mb = info["total_size"] / (1024*1024)
                lines.append(f"### {ftype.title()} ({info['count']} files, {size_mb:.1f} MB)")
                lines.append("")
                # Show important files
                shown = sorted(info["files"], key=lambda x: x["modified"], reverse=True)[:15]
                if shown:
                    lines.append("| File | Size | Modified |")
                    lines.append("|------|------|----------|")
                    for f in shown:
                        sz = f["size"]
                        if sz > 1024*1024:
                            sz_str = f"{sz/(1024*1024):.1f} MB"
                        elif sz > 1024:
                            sz_str = f"{sz/1024:.0f} KB"
                        else:
                            sz_str = f"{sz} B"
                        lines.append(f"| `{f['path']}` | {sz_str} | {f['modified'][:10]} |")
                    lines.append("")

            # README
            if p.get("readme"):
                lines.extend([
                    "## 📝 README",
                    "",
                    "```",
                    p["readme"][:1500],
                    "```",
                    "",
                ])

            (proj_dir / f"{p['name']}.md").write_text("\n".join(lines))

    def _gen_timeline(self):
        events = []
        for p in self.projects.values():
            git = p.get("git")
            if not git or "error" in git:
                continue
            if git.get("timeline"):
                for t in git["timeline"]:
                    events.append({
                        "date": t["date"][:10],
                        "project": p["name"],
                        "msg": t["msg"],
                        "category": p["category"],
                    })
        events.sort(key=lambda x: x["date"], reverse=True)

        lines = [
            "# 📅 Timeline — все изменения",
            "",
            f"*{len(events)} последних коммитов по всем проектам*",
            "",
            "| Дата | Проект | Категория | Коммит |",
            "|------|--------|-----------|--------|",
        ]
        for e in events[:100]:
            cat = CATEGORIES.get(e["category"], {"icon": "📦"})
            lines.append(
                f"| {e['date']} | [{e['project']}](projects/{e['project']}.md) "
                f"| {cat.get('icon','')} | {e['msg'][:60]} |"
            )
        lines.append("")
        (WIKI_DIR / "TIMELINE.md").write_text("\n".join(lines))

    def _gen_tech_matrix(self):
        lines = [
            "# 🛠 Tech Matrix",
            "",
            "Какие технологии используются в каких проектах.",
            "",
        ]
        # Collect all techs
        tech_usage = defaultdict(list)
        for p in self.projects.values():
            for fw in p["tech_stack"].get("frameworks", []):
                tech_usage[fw].append(p["name"])
            for lang in p["tech_stack"].get("languages", []):
                tech_usage[lang].append(p["name"])

        lines.append("| Технология | Проекты | Кол-во |")
        lines.append("|-----------|---------|--------|")
        for tech, projs in sorted(tech_usage.items(), key=lambda x: -len(x[1])):
            proj_links = ", ".join(f"[{n}](projects/{n}.md)" for n in sorted(projs)[:5])
            if len(projs) > 5:
                proj_links += f" +{len(projs)-5}"
            lines.append(f"| **{tech}** | {proj_links} | {len(projs)} |")
        lines.append("")
        (WIKI_DIR / "TECH_MATRIX.md").write_text("\n".join(lines))

    def _gen_status_dashboard(self):
        lines = [
            "# 🚦 Status Dashboard",
            "",
            f"*Обновлено: {datetime.now().strftime('%Y-%m-%d %H:%M')}*",
            "",
        ]
        # Group by status
        by_status = defaultdict(list)
        for p in self.projects.values():
            by_status[p["status"]].append(p)

        status_order = ["🟢 active", "🟡 recent", "🟠 dormant", "🔴 archived", "📁 no-git", "⚪ unknown"]
        for status in status_order:
            projs = by_status.get(status, [])
            if not projs:
                continue
            lines.append(f"## {status} ({len(projs)})")
            lines.append("")
            lines.append("| Проект | Категория | Последний коммит | Коммит |")
            lines.append("|--------|-----------|-----------------|--------|")
            for p in sorted(projs, key=lambda x: (x.get("git") or {}).get("last_commit_date", "") or "", reverse=True):
                git = p.get("git") or {}
                cat = CATEGORIES.get(p["category"], {"icon": "📦", "title": "?"})
                lines.append(
                    f"| [{p['name']}](projects/{p['name']}.md) "
                    f"| {cat['icon']} {cat['title']} "
                    f"| {(git.get('last_commit_date') or '—')[:10]} "
                    f"| {(git.get('last_commit_msg') or '—')[:40]} |"
                )
            lines.append("")
        (WIKI_DIR / "STATUS.md").write_text("\n".join(lines))


# ═══════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(description="Project Cataloger & Wiki")
    parser.add_argument("--diff", action="store_true", help="Show changes since last scan")
    parser.add_argument("--category", type=str, help="Scan only this category")
    parser.add_argument("--watch", action="store_true", help="Watch mode (rescan every 5 min)")
    parser.add_argument("--wiki-only", action="store_true", help="Regenerate wiki from last state")
    args = parser.parse_args()

    engine = CatalogEngine()

    if args.wiki_only:
        if engine.previous_state:
            engine.projects = engine.previous_state
            wiki = WikiGenerator(engine.projects)
            wiki.generate()
        else:
            print("❌ No previous state found. Run a full scan first.")
        return

    if args.watch:
        print("👁 Watch mode — scanning every 5 minutes. Ctrl+C to stop.")
        while True:
            engine = CatalogEngine()
            engine.scan_all(args.category)
            wiki = WikiGenerator(engine.projects)
            wiki.generate()
            if engine.previous_state:
                changes = engine.diff()
                if changes:
                    print(f"\n📋 Changes since last scan:")
                    for c in changes:
                        print(f"  {c}")
            print(f"\n⏰ Next scan in 5 minutes...")
            time.sleep(300)
    else:
        engine.scan_all(args.category)
        wiki = WikiGenerator(engine.projects)
        wiki.generate()

        if args.diff and engine.previous_state:
            changes = engine.diff()
            if changes:
                print(f"\n📋 Changes since last scan:")
                for c in changes:
                    print(f"  {c}")
            else:
                print("\n✅ No changes since last scan.")

    print(f"\n🌐 Wiki: {WIKI_DIR / 'INDEX.md'}")
    print(f"📊 State: {STATE_FILE}")


if __name__ == "__main__":
    main()
