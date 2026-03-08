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
    """Load config from YAML file. Falls back to defaults if file not found."""
    path = Path(config_path)
    if not path.exists():
        script_dir = Path(sys.argv[0]).parent if sys.argv[0] else Path(".")
        alt = script_dir / config_path
        if alt.exists():
            path = alt

    if path.exists():
        raw = _load_yaml(path.read_text(encoding="utf-8"))
    else:
        print(f"⚠️  Config file not found: {config_path}")
        print("   Using built-in defaults. Copy config.example.yaml → config.yaml to customise.")
        raw = {}

    return Config(raw or {})
