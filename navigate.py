#!/usr/bin/env python3
"""
claude-codebase-navigator
─────────────────────────
Scans your project directories, builds a Markdown wiki, and generates
compact context maps you can paste directly into Claude / ChatGPT prompts —
saving 40-70% tokens vs live MCP file exploration.

Usage:
  navigate.py                                   Full scan + wiki generation
  navigate.py --map svc-a svc-b                 Generate a prompt map for named projects
  navigate.py --add-project /path/to/project    Add a project from any directory
  navigate.py --diff                            Show what changed since last scan
  navigate.py --wiki-only                       Regenerate wiki without re-scanning
  navigate.py --watch                           Auto-rescan every N minutes
  navigate.py --config path/to/cfg              Use a specific config file
  navigate.py --category backend                Scan only projects in this category
"""

import argparse
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from src.config import load
from src.catalog import CatalogEngine
from src.wiki import WikiGenerator
from src.mapper import generate_map


def main():
    parser = argparse.ArgumentParser(
        prog="navigate.py",
        description="Claude Codebase Navigator — project wiki & LLM context maps",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python navigate.py
  python navigate.py --map auth-service frontend db-migrations
  python navigate.py --add-project /Users/andriy/docvault
  python navigate.py --add-project /Users/andriy/docvault --name my-vault
  python navigate.py --diff
  python navigate.py --watch --interval 10
        """,
    )
    parser.add_argument("--config", default="config.yaml",
                        help="Path to config file (default: config.yaml)")
    parser.add_argument("--map", nargs="+", metavar="PROJECT",
                        help="Generate a compact prompt map for the given project names")
    parser.add_argument("--add-project", metavar="PATH",
                        help="Scan and add a project from any directory into the catalog")
    parser.add_argument("--name", metavar="NAME",
                        help="(with --add-project) Override the project name (default: directory name)")
    parser.add_argument("--diff", action="store_true",
                        help="Show changes since the last scan")
    parser.add_argument("--wiki-only", action="store_true",
                        help="Regenerate wiki from the last saved catalog state (no re-scan)")
    parser.add_argument("--watch", action="store_true",
                        help="Continuously re-scan at a fixed interval")
    parser.add_argument("--interval", type=int, default=5,
                        help="Watch mode interval in minutes (default: 5)")
    parser.add_argument("--category", type=str,
                        help="Limit scan to projects matching this category keyword")
    parser.add_argument("--output", type=str,
                        help="(with --map) Write map to this file instead of stdout")
    args = parser.parse_args()

    cfg = load(args.config)

    # ── --add-project: scan a project from any path ─────────
    if args.add_project:
        engine = CatalogEngine(cfg)
        try:
            meta = engine.add_project(args.add_project, name=args.name)
        except (FileNotFoundError, NotADirectoryError) as e:
            print(f"❌  {e}")
            sys.exit(1)

        # Rebuild wiki page for the added project only
        engine.projects = engine._load_state()  # reload full catalog
        WikiGenerator(engine.projects, cfg).generate()

        # Offer to immediately show a map
        project_name = args.name or Path(args.add_project).name
        print(f"\n💡  To generate a prompt map: python navigate.py --map {project_name}")
        return

    # ── --map: generate a prompt map ────────────────────────
    if args.map:
        engine = CatalogEngine(cfg)
        catalog = engine.previous_state or {}

        if not catalog:
            print("⚠️  No catalog state found. Running a quick scan first…")
            catalog = engine.scan_all()

        result = generate_map(args.map, catalog, cfg)

        if args.output:
            out_path = Path(args.output)
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(result)
            print(f"✅  Map saved → {out_path}")
        else:
            print(result)

        wiki_dir = cfg.wiki_dir
        wiki_dir.mkdir(parents=True, exist_ok=True)
        n = 1
        while (wiki_dir / f"_prompt_map_{n}.md").exists():
            n += 1
        (wiki_dir / f"_prompt_map_{n}.md").write_text(result)
        if not args.output:
            print(f"\n📄  Also saved → {wiki_dir / f'_prompt_map_{n}.md'}")
        return

    # ── --wiki-only: rebuild wiki without scanning ───────────
    if args.wiki_only:
        engine = CatalogEngine(cfg)
        if not engine.previous_state:
            print("❌  No saved catalog state found. Run a full scan first.")
            sys.exit(1)
        engine.projects = engine.previous_state
        WikiGenerator(engine.projects, cfg).generate()
        return

    # ── --watch: continuous mode ─────────────────────────────
    if args.watch:
        interval_sec = args.interval * 60
        print(f"👁  Watch mode — scanning every {args.interval} min. Ctrl+C to stop.")
        while True:
            _run_scan(cfg, args.category, show_diff=True)
            print(f"\n⏳  Next scan in {args.interval} min…\n")
            try:
                time.sleep(interval_sec)
            except KeyboardInterrupt:
                print("\n👋  Watch mode stopped.")
                break
        return

    # ── default: full scan + wiki ────────────────────────────
    _run_scan(cfg, args.category, show_diff=args.diff)


def _run_scan(cfg, category_filter=None, show_diff=False):
    engine = CatalogEngine(cfg)
    engine.scan_all(category_filter)
    WikiGenerator(engine.projects, cfg).generate()

    if show_diff:
        changes = engine.diff()
        if changes:
            print("\n📋  Changes since last scan:")
            for c in changes:
                print(f"  {c}")
        else:
            print("\n✅  No changes since last scan.")

    return engine


if __name__ == "__main__":
    main()
