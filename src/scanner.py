"""
scanner.py — scans a single project directory and extracts metadata.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from .config import Config

CODE_EXTENSIONS  = {".py", ".ipynb", ".js", ".ts", ".jsx", ".tsx", ".sh", ".sql", ".go", ".rs", ".rb"}
DOC_EXTENSIONS   = {".md", ".txt", ".rst", ".html"}
CONFIG_EXTENSIONS = {".json", ".yaml", ".yml", ".toml", ".cfg", ".ini", ".env"}
DATA_EXTENSIONS  = {".csv", ".parquet", ".xlsx", ".db", ".sqlite"}
ALL_EXTENSIONS   = CODE_EXTENSIONS | DOC_EXTENSIONS | CONFIG_EXTENSIONS | DATA_EXTENSIONS

_IMPORTANT_NAMES = {
    "readme", "main", "app", "config", "setup", "requirements",
    "dockerfile", "docker-compose", "makefile", "changelog", "todo", "plan",
    "orchestrator", "router", "server", "index", "cli",
}

_FRAMEWORK_HINTS = {
    "fastapi": "FastAPI", "flask": "Flask", "django": "Django",
    "streamlit": "Streamlit", "gradio": "Gradio",
    "pandas": "Pandas", "numpy": "NumPy", "torch": "PyTorch",
    "tensorflow": "TensorFlow", "sklearn": "scikit-learn",
    "langchain": "LangChain", "openai": "OpenAI", "anthropic": "Anthropic",
    "ccxt": "CCXT", "polars": "Polars", "plotly": "Plotly",
    "sqlalchemy": "SQLAlchemy", "asyncpg": "PostgreSQL", "clickhouse": "ClickHouse",
    "celery": "Celery", "redis": "Redis",
    "react": "React", "next": "Next.js", "vue": "Vue.js", "nuxt": "Nuxt.js",
    "svelte": "Svelte", "tailwindcss": "Tailwind CSS",
    "typescript": "TypeScript", "vite": "Vite", "webpack": "Webpack",
    "express": "Express", "fastify": "Fastify", "nestjs": "NestJS",
}


class ProjectScanner:
    def __init__(self, project_path: Path, cfg: Config):
        self.path = project_path
        self.name = project_path.name
        self.cfg = cfg

    def scan(self) -> dict:
        meta: dict = {
            "name": self.name,
            "path": str(self.path),
            "scanned_at": datetime.now(timezone.utc).isoformat(),
            "category": self._detect_category(),
            "git": self._git_info(),
            "files": self._scan_files(),
            "readme": self._extract_readme(),
            "tech_stack": self._detect_tech_stack(),
            "integrations": self._detect_integrations(),
            "status": "unknown",
        }
        meta["status"] = self._infer_status(meta)
        meta["summary"] = self._build_summary(meta)
        return meta

    def _detect_category(self) -> str:
        name_lower = self.name.lower()
        for cat_id, cat_info in self.cfg.categories.items():
            for kw in cat_info.get("keywords", []):
                if kw.lower() in name_lower:
                    return cat_id
        return "uncategorized"

    def _git_info(self) -> Optional[dict]:
        if not (self.path / ".git").exists():
            return None
        try:
            def run(args: list[str]) -> Optional[str]:
                r = subprocess.run(
                    ["git"] + args, cwd=self.path,
                    capture_output=True, text=True, timeout=10
                )
                return r.stdout.strip() if r.returncode == 0 else None

            latest_ref = run(["for-each-ref", "--sort=-committerdate",
                               "refs/heads/", "refs/remotes/",
                               "--format=%(refname:short)", "--count=1"])
            if latest_ref and latest_ref.startswith("origin/"):
                latest_ref = latest_ref[7:]
            branch = latest_ref or run(["rev-parse", "--abbrev-ref", "HEAD"])
            last_date = run(["log", "-1", "--all", "--format=%aI"])
            last_msg  = run(["log", "-1", "--all", "--format=%s"])
            count     = run(["rev-list", "--count", "--all"])
            recent_raw = run(["log", "--all", "--since=30 days ago", "--oneline"])
            recent_count = len(recent_raw.split("\n")) if recent_raw else 0
            last5_raw = run(["log", "-5", "--all", "--format=%aI|||%s"])
            timeline = []
            if last5_raw:
                for line in last5_raw.split("\n"):
                    if "|||" in line:
                        d, m = line.split("|||", 1)
                        timeline.append({"date": d[:10], "msg": m})
            return {
                "branch": branch,
                "last_commit_date": last_date,
                "last_commit_msg": last_msg,
                "commit_count": int(count) if count else 0,
                "recent_commits_30d": recent_count,
                "timeline": timeline,
            }
        except Exception as exc:
            return {"error": str(exc)}


    def _scan_files(self) -> dict:
        stats: dict = defaultdict(lambda: {"count": 0, "total_size": 0, "files": []})
        total = 0
        for root, dirs, files in os.walk(self.path):
            dirs[:] = [d for d in dirs if d not in self.cfg.skip_dirs]
            for fname in files:
                ext = Path(fname).suffix.lower()
                if ext not in ALL_EXTENSIONS:
                    continue
                fpath = Path(root) / fname
                try:
                    size = fpath.stat().st_size
                    mtime = datetime.fromtimestamp(fpath.stat().st_mtime, tz=timezone.utc).isoformat()
                except OSError:
                    continue
                rel = str(fpath.relative_to(self.path))
                total += 1
                if ext in CODE_EXTENSIONS:       ftype = "code"
                elif ext in DOC_EXTENSIONS:      ftype = "docs"
                elif ext in CONFIG_EXTENSIONS:   ftype = "config"
                else:                            ftype = "data"
                stats[ftype]["count"] += 1
                stats[ftype]["total_size"] += size
                depth = len(Path(rel).parts)
                important = any(k in fname.lower() for k in _IMPORTANT_NAMES)
                if depth <= 2 or important:
                    stats[ftype]["files"].append({"path": rel, "size": size, "modified": mtime})
        return {"total_indexed": total, "by_type": {k: dict(v) for k, v in stats.items()}}

    def _extract_readme(self) -> Optional[str]:
        for name in ["README.md", "readme.md", "README.txt", "README"]:
            p = self.path / name
            if p.exists():
                try:
                    return p.read_text(errors="ignore")[:3000]
                except Exception:
                    pass
        return None

    def _detect_tech_stack(self) -> dict:
        stack: dict[str, set] = {"languages": set(), "frameworks": set(), "tools": set()}
        indicator_files = {
            "requirements.txt": ("Python", "pip"),
            "setup.py":         ("Python", None),
            "pyproject.toml":   ("Python", None),
            "go.mod":           ("Go", None),
            "Cargo.toml":       ("Rust", None),
            "Gemfile":          ("Ruby", None),
            "package.json":     ("JavaScript/TypeScript", "npm"),
            "Dockerfile":       (None, "Docker"),
            "docker-compose.yml": (None, "Docker Compose"),
            "Makefile":         (None, "Make"),
            ".github":          (None, "GitHub Actions"),
            ".gitlab-ci.yml":   (None, "GitLab CI"),
        }
        for fname, (lang, tool) in indicator_files.items():
            if (self.path / fname).exists():
                if lang: stack["languages"].add(lang)
                if tool: stack["tools"].add(tool)
        req = self.path / "requirements.txt"
        if req.exists():
            txt = req.read_text(errors="ignore").lower()
            for key, label in _FRAMEWORK_HINTS.items():
                if key in txt:
                    stack["frameworks"].add(label)
        pkg = self.path / "package.json"
        if pkg.exists():
            try:
                data = json.loads(pkg.read_text(errors="ignore"))
                deps = {**data.get("dependencies", {}), **data.get("devDependencies", {})}
                for key, label in _FRAMEWORK_HINTS.items():
                    if key in deps:
                        stack["frameworks"].add(label)
            except Exception:
                pass
        return {k: sorted(v) for k, v in stack.items()}

    def _detect_integrations(self) -> list[dict]:
        found: list[dict] = []
        for entry in self.cfg.integrations.get(self.name, []):
            found.append({**entry, "source": "manual"})
        for env_file in [".env", ".env.example", ".env.template", ".env.sample"]:
            p = self.path / env_file
            if not p.exists():
                continue
            try:
                for line in p.read_text(errors="ignore").splitlines():
                    line = line.strip()
                    if line.startswith("#") or "=" not in line:
                        continue
                    key, _, val = line.partition("=")
                    key = key.strip().upper()
                    val = val.strip().strip('"').strip("'")
                    if not val or val.startswith("$"):
                        continue
                    m = re.search(r'https?://[^/\s]+(?:/[^\s]*)?', val)
                    if m and (key.endswith("_URL") or key.endswith("_HOST") or "API" in key):
                        found.append({
                            "target": key, "type": "HTTP",
                            "url": m.group(0), "data": f"via env {key}", "source": "auto",
                        })
            except Exception:
                pass
        return found

    def _infer_status(self, meta: dict) -> str:
        git = meta.get("git")
        if not git or "error" in (git or {}):
            return "📁 no-git"
        if git.get("recent_commits_30d", 0) > 0:
            return "🟢 active"
        try:
            last = datetime.fromisoformat(git["last_commit_date"])
            if last.tzinfo is None:
                last = last.replace(tzinfo=timezone.utc)
            days = (datetime.now(timezone.utc) - last).days
            if days < 90:  return "🟡 recent"
            if days < 365: return "🟠 dormant"
            return "🔴 archived"
        except Exception:
            return "⚪ unknown"

    def _build_summary(self, meta: dict) -> str:
        by_type = meta["files"]["by_type"]
        code = by_type.get("code", {}).get("count", 0)
        docs = by_type.get("docs", {}).get("count", 0)
        parts = [f"{code} code, {docs} docs"]
        s = meta["tech_stack"]
        if s["languages"]:  parts.append(", ".join(s["languages"]))
        if s["frameworks"]: parts.append(", ".join(s["frameworks"][:4]))
        return " | ".join(parts)
