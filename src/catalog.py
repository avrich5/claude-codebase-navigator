"""
catalog.py — orchestrates project scanning, state persistence, and diffing.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from .config import Config
from .scanner import ProjectScanner


class CatalogEngine:
    def __init__(self, cfg: Config):
        self.cfg = cfg
        self.projects: dict = {}
        self.previous_state: dict = self._load_state()

    def _load_state(self) -> dict:
        p = self.cfg.catalog_state
        if p and p.exists():
            try:
                return json.loads(p.read_text())
            except Exception:
                pass
        return {}

    def save_state(self):
        self.cfg.catalog_state.parent.mkdir(parents=True, exist_ok=True)
        self.cfg.catalog_state.write_text(
            json.dumps(self.projects, indent=2, default=str)
        )
        self.cfg.history_dir.mkdir(parents=True, exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        snap = self.cfg.history_dir / f"catalog_{ts}.json"
        snap.write_text(json.dumps(self.projects, indent=2, default=str))

    def scan_all(self, category_filter: Optional[str] = None) -> dict:
        cfg = self.cfg
        dirs_map: dict[str, Path] = {}

        if cfg.production and cfg.production.exists():
            for entry in sorted(cfg.production.iterdir()):
                if entry.is_dir() and not entry.name.startswith(".") and entry.name != "wiki":
                    dirs_map[entry.name] = entry

        if cfg.local_dev and cfg.local_dev.exists():
            for entry in sorted(cfg.local_dev.iterdir()):
                if entry.is_dir() and not entry.name.startswith(".") \
                        and entry.name not in cfg.skip_dirs:
                    canonical = cfg.aliases.get(entry.name, entry.name)
                    dirs_map[canonical] = entry

        for name, path in cfg.local_only.items():
            if path and path.exists():
                dirs_map[name] = path

        all_dirs = sorted(dirs_map.items(), key=lambda x: x[0])
        total = len(all_dirs)

        print(f"\n{'═'*60}")
        print(f"  claude-codebase-navigator")
        print(f"  Scanning {total} projects — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'═'*60}\n")

        for i, (name, path) in enumerate(all_dirs, 1):
            scanner = ProjectScanner(path, cfg)
            scanner.name = name

            if category_filter:
                cat = scanner._detect_category()
                if category_filter.lower() not in cat.lower():
                    continue

            print(f"  [{i:3d}/{total}] {name:<40}", end="", flush=True)
            meta = scanner.scan()
            meta["name"] = name
            self.projects[name] = meta
            cat_info = cfg.categories.get(meta["category"], {"icon": "📦", "title": "Uncategorized"})
            print(f"  {meta['status']}  {cat_info['icon']} {cat_info['title']}")

        self.save_state()
        print(f"\n✅  Scanned {len(self.projects)} projects → {cfg.catalog_state}")
        return self.projects

    def diff(self) -> list[str]:
        changes: list[str] = []
        prev = self.previous_state
        curr = self.projects

        for name in sorted(set(curr) - set(prev)):
            changes.append(f"➕ NEW       {name}")
        for name in sorted(set(prev) - set(curr)):
            changes.append(f"➖ REMOVED   {name}")
        for name in sorted(set(curr) & set(prev)):
            old_git = (prev[name].get("git") or {})
            new_git = (curr[name].get("git") or {})
            if old_git.get("last_commit_date") != new_git.get("last_commit_date"):
                changes.append(
                    f"🔄 UPDATED   {name:<35} {new_git.get('last_commit_msg', '')[:50]}"
                )
            old_n = prev[name].get("files", {}).get("total_indexed", 0)
            new_n = curr[name].get("files", {}).get("total_indexed", 0)
            if old_n != new_n:
                sign = "+" if new_n > old_n else ""
                changes.append(f"📝 FILES     {name:<35} {sign}{new_n - old_n} files")
        return changes
