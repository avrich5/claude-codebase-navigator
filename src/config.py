"""
config.py — loads and validates config.yaml
"""
from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Any

# ── try to import yaml (optional dep, fallback to built-in) ──
try:
    import yaml as _yaml
    def _load_yaml(text: str) -> dict:
        return _yaml.safe_load(text) or {}
except ImportError:
    def _load_yaml(text: str) -> dict:  # type: ignore[misc]
        raise SystemExit(
            "❌  PyYAML is required: pip install pyyaml\n"
            "    Or install all deps: pip install -r requirements.txt"
        )


# ── Defaults ────────────────────────────────────────────────
_DEFAULTS: dict[str, Any] = {
    "sources": {
        "local_dev": "~/Projects",
        "production": None,
    },
    "output": {
        "catalog_state": "./catalog_state.json",
        "wiki_dir": "./wiki",
        "history_dir": "./history",
    },
    "git_remote": {
        "base_url": None,
    },
    "categories": {
        "backend":  {"icon": "⚙️",  "title": "Backend Services",   "keywords": ["api", "service", "server", "backend", "worker", "daemon"]},
        "frontend": {"icon": "🎨",  "title": "Frontend Apps",      "keywords": ["ui", "frontend", "web", "app", "dashboard", "landing"]},
        "data":     {"icon": "📊",  "title": "Data & Analytics",   "keywords": ["data", "pipeline", "etl", "analytics", "miner", "scraper"]},
        "ml":       {"icon": "🧠",  "title": "ML & AI",            "keywords": ["model", "predict", "train", "llm", "ai", "ml", "neural"]},
        "infra":    {"icon": "🛠",  "title": "Infrastructure",     "keywords": ["infra", "deploy", "docker", "k8s", "terraform", "monitoring"]},
        "libs":     {"icon": "📦",  "title": "Libraries & SDKs",   "keywords": ["lib", "sdk", "client", "utils", "helpers", "common", "shared"]},
    },
    "local_only": {},
    "aliases": {},
    "integrations": {},
}

_SKIP_DIRS = {
    "node_modules", ".git", "__pycache__", ".venv", "venv", "env",
    ".tox", ".mypy_cache", ".pytest_cache", "dist", "build",
    ".next", ".nuxt", "coverage", ".cache", ".eggs", ".ruff_cache",
}


def _expand(path_str: str | None) -> Path | None:
    if not path_str:
        return None
    return Path(os.path.expandvars(os.path.expanduser(str(path_str)))).resolve()


def _deep_merge(base: dict, override: dict) -> dict:
    result = dict(base)
    for k, v in override.items():
        if isinstance(v, dict) and isinstance(result.get(k), dict):
            result[k] = _deep_merge(result[k], v)
        else:
            result[k] = v
    return result


class Config:
    """Parsed, validated configuration."""

    def __init__(self, raw: dict):
        merged = _deep_merge(_DEFAULTS, raw)

        src = merged.get("sources", {})
        self.local_dev: Path | None = _expand(src.get("local_dev"))
        self.production: Path | None = _expand(src.get("production"))

        out = merged.get("output", {})
        self.catalog_state = _expand(out.get("catalog_state")) or Path("./catalog_state.json")
        self.wiki_dir = _expand(out.get("wiki_dir")) or Path("./wiki")
        self.history_dir = _expand(out.get("history_dir")) or Path("./history")

        gr = merged.get("git_remote", {})
        base = (gr.get("base_url") or "").rstrip("/")
        self.git_remote_base: str | None = base or None

        self.categories: dict[str, dict] = merged.get("categories", _DEFAULTS["categories"])

        self.local_only: dict[str, Path] = {
            name: _expand(p) for name, p in (merged.get("local_only") or {}).items()
            if p and _expand(p) and _expand(p).exists()
        }
        self.aliases: dict[str, str] = merged.get("aliases") or {}
        self.reverse_aliases: dict[str, str] = {v: k for k, v in self.aliases.items()}
        self.integrations: dict[str, list] = merged.get("integrations") or {}
        self.skip_dirs: set[str] = _SKIP_DIRS

    def gitlab_url(self, project_name: str) -> str | None:
        if not self.git_remote_base:
            return None
        return f"{self.git_remote_base}/{project_name}"

    def resolve_local_path(self, project_name: str) -> Path | None:
        """Given a (possibly aliased) project name, find the local directory."""
        local_name = self.reverse_aliases.get(project_name, project_name)
        for base in filter(None, [self.local_dev, self.production]):
            candidate = base / local_name
            if candidate.exists():
                return candidate
        if project_name in self.local_only:
            return self.local_only[project_name]
        return None


def load(config_path: str | Path = "config.yaml") -> Config:
    """
    Load config using the following search order:

    1. Explicit --config path (if provided by user)
    2. ./config.yaml              — current working directory
    3. ~/.config/navigate/config.yaml  — global user config
    4. <script_dir>/config.yaml   — next to navigate.py
    5. Built-in defaults          — with a warning
    """
    _GLOBAL_CONFIG = Path.home() / ".config" / "navigate" / "config.yaml"

    # If the user explicitly passed --config, use only that path
    if str(config_path) != "config.yaml":
        p = Path(config_path)
        if p.exists():
            return Config(_load_yaml(p.read_text(encoding="utf-8")) or {})
        print(f"❌  Config file not found: {p}")
        sys.exit(1)

    # Auto-search order
    candidates = [
        Path.cwd() / "config.yaml",                         # 1. cwd (project-local)
        _GLOBAL_CONFIG,                                      # 2. global user config
        Path(sys.argv[0]).resolve().parent / "config.yaml",  # 3. next to script (fallback)
    ]

    for candidate in candidates:
        if candidate.exists():
            raw = _load_yaml(candidate.read_text(encoding="utf-8")) or {}
            # For global config: always resolve output paths to ~/.config/navigate/
            # Override relative paths (./...) so output lands next to the config,
            # not in whatever cwd the user happens to be in
            if candidate == _GLOBAL_CONFIG:
                base = str(_GLOBAL_CONFIG.parent)
                out = raw.setdefault("output", {})
                for key, default in [
                    ("catalog_state", f"{base}/catalog_state.json"),
                    ("wiki_dir",      f"{base}/wiki"),
                    ("history_dir",   f"{base}/history"),
                ]:
                    val = out.get(key, "")
                    # Replace relative paths like ./something with absolute
                    if not val or str(val).startswith("."):
                        out[key] = default
            return Config(raw)

    # Nothing found — print helpful message
    print("⚠️  No config.yaml found. Search order:")
    for c in candidates:
        print(f"     {c}")
    print()
    print("   To create a global config (recommended for global 'navigate' command):")
    script_dir = Path(sys.argv[0]).resolve().parent
    print(f"   mkdir -p ~/.config/navigate")
    print(f"   cp {script_dir}/config.example.yaml ~/.config/navigate/config.yaml")
    print(f"   # then edit ~/.config/navigate/config.yaml")
    print()
    print("   Using built-in defaults for now.")
    return Config({})
