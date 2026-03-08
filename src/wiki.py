"""
wiki.py — generates a Markdown wiki from the project catalog.
"""
from __future__ import annotations

from collections import defaultdict
from datetime import datetime
from pathlib import Path

from .config import Config


class WikiGenerator:
    def __init__(self, projects: dict, cfg: Config):
        self.projects = projects
        self.cfg = cfg
        self.wiki_dir = cfg.wiki_dir

    def generate(self):
        self.wiki_dir.mkdir(parents=True, exist_ok=True)
        (self.wiki_dir / "projects").mkdir(exist_ok=True)
        (self.wiki_dir / "categories").mkdir(exist_ok=True)
        self._gen_index()
        self._gen_category_pages()
        self._gen_project_pages()
        self._gen_status_dashboard()
        self._gen_timeline()
        self._gen_tech_matrix()
        print(f"✅  Wiki → {self.wiki_dir / 'INDEX.md'}")

    def _gen_index(self):
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        lines = [
            "# 🗂 Codebase Navigator — Project Wiki", "",
            f"*Generated: {now} · {len(self.projects)} projects*", "",
            "## Navigation", "",
            "| Page | Description |", "|------|-------------|",
            "| [Status Dashboard](STATUS.md) | Live status of all projects |",
            "| [Timeline](TIMELINE.md) | Recent commits across all repos |",
            "| [Tech Matrix](TECH_MATRIX.md) | Technology usage per project |",
            "", "## Categories", "",
        ]
        by_cat: dict = defaultdict(list)
        for p in self.projects.values():
            by_cat[p["category"]].append(p)

        for cat_id, cat_info in self.cfg.categories.items():
            projs = by_cat.get(cat_id, [])
            if not projs:
                continue
            lines.append(f"### {cat_info['icon']} [{cat_info['title']}](categories/{cat_id}.md)")
            lines.append("")
            for p in sorted(projs, key=lambda x: x["name"]):
                status_icon = p["status"].split()[0]
                lines.append(f"- {status_icon} [{p['name']}](projects/{p['name']}.md) — {p['summary']}")
            lines.append("")

        uncat = by_cat.get("uncategorized", [])
        if uncat:
            lines.append("### 📦 Uncategorized")
            lines.append("")
            for p in sorted(uncat, key=lambda x: x["name"]):
                lines.append(f"- {p['status'].split()[0]} [{p['name']}](projects/{p['name']}.md) — {p['summary']}")
            lines.append("")
        (self.wiki_dir / "INDEX.md").write_text("\n".join(lines))

    def _gen_category_pages(self):
        by_cat: dict = defaultdict(list)
        for p in self.projects.values():
            by_cat[p["category"]].append(p)
        for cat_id, cat_info in self.cfg.categories.items():
            projs = by_cat.get(cat_id, [])
            if not projs:
                continue
            lines = [
                f"# {cat_info['icon']} {cat_info['title']}", "",
                f"**{len(projs)} projects**", "",
                "| Project | Status | Code files | Stack | Last commit |",
                "|---------|--------|-----------|-------|-------------|",
            ]
            for p in sorted(projs, key=lambda x: (x.get("git") or {}).get("last_commit_date", "") or "", reverse=True):
                git = p.get("git") or {}
                last = (git.get("last_commit_date") or "—")[:10]
                code = p["files"]["by_type"].get("code", {}).get("count", 0)
                fw   = ", ".join(p["tech_stack"].get("frameworks", [])[:3]) or "—"
                lines.append(f"| [{p['name']}](../projects/{p['name']}.md) | {p['status']} | {code} | {fw} | {last} |")
            lines.append("")
            (self.wiki_dir / "categories" / f"{cat_id}.md").write_text("\n".join(lines))


    def _gen_project_pages(self):
        proj_dir = self.wiki_dir / "projects"
        for p in self.projects.values():
            cat_info = self.cfg.categories.get(p["category"], {"icon": "📦", "title": "Uncategorized"})
            lines = [
                f"# {p['name']}", "",
                f"**Category:** {cat_info['icon']} [{cat_info['title']}](../categories/{p['category']}.md)  ",
                f"**Status:** {p['status']}  ",
                f"**Path:** `{p['path']}`  ",
            ]
            url = self.cfg.gitlab_url(p["name"])
            if url:
                lines.append(f"**Remote:** [{p['name']}]({url})  ")
            lines.append("")
            git = p.get("git")
            if git and "error" not in git:
                lines += [
                    "## Git", "",
                    f"- **Branch:** `{git.get('branch', '—')}`",
                    f"- **Commits:** {git.get('commit_count', 0)}",
                    f"- **Last commit:** {(git.get('last_commit_date') or '—')[:10]}",
                    f"- **Message:** {git.get('last_commit_msg', '—')}",
                    f"- **Last 30 days:** {git.get('recent_commits_30d', 0)} commits", "",
                ]
                if git.get("timeline"):
                    lines.append("### Recent commits")
                    lines.append("")
                    for t in git["timeline"]:
                        lines.append(f"- `{t['date']}` {t['msg']}")
                    lines.append("")
            s = p["tech_stack"]
            if any(s.values()):
                lines.append("## Tech Stack")
                lines.append("")
                if s.get("languages"):  lines.append(f"- **Languages:** {', '.join(s['languages'])}")
                if s.get("frameworks"): lines.append(f"- **Frameworks:** {', '.join(s['frameworks'])}")
                if s.get("tools"):      lines.append(f"- **Tools:** {', '.join(s['tools'])}")
                lines.append("")
            integrations = p.get("integrations", [])
            if integrations:
                lines += ["## Integrations", "", "| Target | Type | URL | Data | Source |", "|--------|------|-----|------|--------|"]
                for i in integrations:
                    lines.append(f"| `{i.get('target','')}` | `{i.get('type','')}` | `{i.get('url','')}` | {i.get('data','')} | {i.get('source','manual')} |")
                lines.append("")
            files = p["files"]
            lines.append(f"## Files ({files['total_indexed']} indexed)")
            lines.append("")
            for ftype, info in files["by_type"].items():
                size_mb = info["total_size"] / (1024 * 1024)
                lines.append(f"### {ftype.title()} ({info['count']} files, {size_mb:.1f} MB)")
                lines.append("")
                shown = sorted(info["files"], key=lambda x: x["modified"], reverse=True)[:12]
                if shown:
                    lines.append("| File | Size | Modified |")
                    lines.append("|------|------|----------|")
                    for f in shown:
                        sz = f["size"]
                        sz_str = (f"{sz/(1024*1024):.1f} MB" if sz > 1_048_576 else f"{sz/1024:.0f} KB" if sz > 1024 else f"{sz} B")
                        lines.append(f"| `{f['path']}` | {sz_str} | {f['modified'][:10]} |")
                    lines.append("")
            if p.get("readme"):
                lines += ["## README", "", "```", p["readme"][:2000], "```", ""]
            (proj_dir / f"{p['name']}.md").write_text("\n".join(lines))

    def _gen_status_dashboard(self):
        lines = ["# 🚦 Status Dashboard", "", f"*Updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*", ""]
        by_status: dict = defaultdict(list)
        for p in self.projects.values():
            by_status[p["status"]].append(p)
        for status in ["🟢 active", "🟡 recent", "🟠 dormant", "🔴 archived", "📁 no-git", "⚪ unknown"]:
            projs = by_status.get(status, [])
            if not projs:
                continue
            lines += [f"## {status} ({len(projs)})", "", "| Project | Category | Last commit | Message |", "|---------|----------|-------------|---------|"]
            for p in sorted(projs, key=lambda x: (x.get("git") or {}).get("last_commit_date", "") or "", reverse=True):
                git = p.get("git") or {}
                cat = self.cfg.categories.get(p["category"], {"icon": "📦"})
                lines.append(f"| [{p['name']}](projects/{p['name']}.md) | {cat['icon']} | {(git.get('last_commit_date') or '—')[:10]} | {(git.get('last_commit_msg') or '—')[:50]} |")
            lines.append("")
        (self.wiki_dir / "STATUS.md").write_text("\n".join(lines))

    def _gen_timeline(self):
        events = []
        for p in self.projects.values():
            git = p.get("git")
            if not git or "error" in git:
                continue
            for t in git.get("timeline", []):
                events.append({"date": t["date"], "project": p["name"], "msg": t["msg"], "category": p["category"]})
        events.sort(key=lambda x: x["date"], reverse=True)
        lines = ["# 📅 Timeline", "", f"*{len(events)} recent commits across all projects*", "",
                 "| Date | Project | Category | Commit |", "|------|---------|----------|--------|"]
        for e in events[:200]:
            cat = self.cfg.categories.get(e["category"], {"icon": "📦"})
            lines.append(f"| {e['date']} | [{e['project']}](projects/{e['project']}.md) | {cat['icon']} | {e['msg'][:70]} |")
        lines.append("")
        (self.wiki_dir / "TIMELINE.md").write_text("\n".join(lines))

    def _gen_tech_matrix(self):
        tech_usage: dict = defaultdict(list)
        for p in self.projects.values():
            for fw in p["tech_stack"].get("frameworks", []):
                tech_usage[fw].append(p["name"])
            for lang in p["tech_stack"].get("languages", []):
                tech_usage[lang].append(p["name"])
        lines = ["# 🛠 Tech Matrix", "", "Technology usage across all projects.", "",
                 "| Technology | Count | Projects |", "|-----------|-------|----------|"]
        for tech, projs in sorted(tech_usage.items(), key=lambda x: -len(x[1])):
            links = ", ".join(f"[{n}](projects/{n}.md)" for n in sorted(projs)[:6])
            if len(projs) > 6:
                links += f" +{len(projs)-6} more"
            lines.append(f"| **{tech}** | {len(projs)} | {links} |")
        lines.append("")
        (self.wiki_dir / "TECH_MATRIX.md").write_text("\n".join(lines))
