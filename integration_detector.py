#!/usr/bin/env python3
"""
integration_detector.py
========================
Автоматичний детектор інтеграцій між проектами.

Метод 1 (PRIMARY): Endpoint matching
  - Збирає всі API endpoints з кожного проекту (FastAPI, Express, Flask)
  - Шукає виклики цих endpoints в коді інших проектів
  - Найнадійніший метод — конкретні шляхи важко переплутати

Метод 2 (SECONDARY): Hostname matching
  - Шукає ім'я проекту в URL які викликаються
  - Надійний для kubernetes/docker named services

Метод 3 (DISABLED): Port matching
  - Ненадійний — всі проекти використовують 3000, 8000, 8001

USAGE:
    from integration_detector import IntegrationDetector
    detector = IntegrationDetector(all_project_paths)
    graph = detector.build_graph()
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict
from typing import Optional

SKIP_DIRS = {
    "node_modules", ".git", "__pycache__", ".venv", "venv",
    "dist", "build", ".next", "coverage", ".cache", "target",
}
CODE_EXT = {".py", ".ts", ".js", ".tsx", ".jsx", ".sh"}

# Known infra hosts — skip these
INFRA_HOSTS = {
    "localhost", "127.0.0.1", "0.0.0.0", "host.docker.internal",
    "db", "redis", "postgres", "clickhouse", "minio",
}

# Route definition patterns (server side — what a project PROVIDES)
ROUTE_DEF_PATTERNS = [
    re.compile(r'@(?:app|router)\.(get|post|put|delete|patch)\s*\(\s*["\']([^"\']+)["\']'),
    re.compile(r'(?:app|router)\.(get|post|put|delete|patch)\s*\(\s*["\']([^"\']+)["\']'),
    re.compile(r'web\.(get|post|put|delete)\s*\(\s*["\']([^"\']+)["\']'),
]

# HTTP call patterns (client side — what a project CALLS)
CALL_PATTERNS = [
    # requests.get("/api/foo"), fetch("/api/foo")
    re.compile(r'''(?:requests\.\w+|fetch)\s*\([^)]*["\']([/][a-zA-Z][a-zA-Z0-9_/{}:.-]{2,})["\']'''),
    # axios.get("/api/foo"), axios.post(...)
    re.compile(r'''axios\.\w+\s*\(\s*["\`]([/][a-zA-Z][a-zA-Z0-9_/{}:.-]{2,})["\`]'''),
    # url = f"...{base_url}/api/foo"  or  url = base + "/api/foo"
    re.compile(r'''[+,\s]["\`]([/](?:api|v\d)[/][a-zA-Z][a-zA-Z0-9_/{}:.-]*)["\`]'''),
    # hardcoded path strings that look like API paths
    re.compile(r'''["\`](/(?:api|v\d)/[a-zA-Z][a-zA-Z0-9_/{}:.-]{2,})["\`]'''),
]

# Generic paths that appear everywhere — skip them
GENERIC_PATHS = {
    "/health", "/status", "/ping", "/favicon.ico",
    "/login", "/logout", "/dashboard", "/api/data",
    "/api/health", "/", "/docs", "/openapi.json",
}


class ProjectScanner:
    def __init__(self, path: Path, name: str):
        self.path = path
        self.name = name

    def scan(self) -> dict:
        endpoints  = set()   # paths this project PROVIDES
        calls_made = set()   # (path, context) this project CALLS
        env_vars   = {}

        for dirpath, dirs, files in os.walk(self.path):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
            for fname in files:
                ext = Path(fname).suffix.lower()
                if ext not in CODE_EXT:
                    continue
                fpath = Path(dirpath) / fname
                rel   = str(fpath.relative_to(self.path))
                try:
                    text = fpath.read_text(errors="ignore")
                    # Collect endpoints defined in THIS file (per-file to avoid self-filtering)
                    file_endpoints = set()
                    for pat in ROUTE_DEF_PATTERNS:
                        for m in pat.finditer(text):
                            raw_path = m.group(2) if len(m.groups()) == 2 else m.group(1)
                            if raw_path and len(raw_path) > 1 and not raw_path.startswith("http"):
                                norm = re.sub(r'\{[^}]+\}|:[a-zA-Z_]+', '*', raw_path)
                                file_endpoints.add(norm)
                                endpoints.add(norm)

                    # Collect HTTP calls this file MAKES (including self-calls — valid test/internal calls)
                    for pat in CALL_PATTERNS:
                        for m in pat.finditer(text):
                            raw_path = m.group(1)
                            norm = re.sub(r'\{[^}]+\}|:[a-zA-Z_]+', '*', raw_path)
                            if norm not in GENERIC_PATHS and len(norm) > 4:
                                calls_made.add((norm, f"{rel}"))
                except Exception:
                    pass

        # Also parse .env for hostname-based service references
        for fname in [".env", ".env.example", ".env.sample"]:
            fpath = self.path / fname
            if fpath.exists():
                try:
                    for line in fpath.read_text(errors="ignore").splitlines():
                        if "=" in line and not line.strip().startswith("#"):
                            k, _, v = line.partition("=")
                            env_vars[k.strip()] = v.strip().strip('"\'')
                except Exception:
                    pass

        return {
            "name": self.name,
            "path": str(self.path),
            "endpoints": sorted(endpoints),
            "calls_made": [{"path": p, "ctx": c} for p, c in calls_made],
            "env_vars": env_vars,
        }


class IntegrationDetector:
    def __init__(self, project_paths: list):
        self.projects = {}
        for p in project_paths:
            p = Path(p)
            if p.is_dir():
                s = ProjectScanner(p, p.name)
                self.projects[p.name] = s.scan()

    def build_graph(self) -> dict:
        graph = {n: {"calls": [], "called_by": []} for n in self.projects}

        # Build endpoint index: normalized_path → [project_names]
        endpoint_index = defaultdict(list)
        for name, data in self.projects.items():
            for ep in data["endpoints"]:
                endpoint_index[ep].append(name)

        # Build hostname variants → project name
        host_to_project = {}
        for name in self.projects:
            for variant in [name, name.replace("-","_"), name.replace("_","-"), name.replace("-","")]:
                host_to_project[variant.lower()] = name

        seen = set()

        for caller, data in self.projects.items():
            for call in data["calls_made"]:
                path = call["path"]
                ctx  = call["ctx"]

                # Method 1: endpoint match
                owners = [o for o in endpoint_index.get(path, []) if o != caller]

                # If ambiguous (>1 owner), try to narrow by hostname in env or context
                if len(owners) > 1:
                    # Try to find a hint in env vars
                    env_vals = " ".join(data["env_vars"].values()).lower()
                    narrowed = [o for o in owners if o.lower().replace("-","_") in env_vals
                                or o.lower().replace("_","-") in env_vals]
                    if len(narrowed) == 1:
                        owners = narrowed
                    else:
                        owners = []  # Too ambiguous — skip

                # Method 2: hostname match from env (for non-/api paths)
                if not owners:
                    for env_val in data["env_vars"].values():
                        m = re.search(r'https?://([a-z0-9._-]+)', env_val.lower())
                        if not m:
                            continue
                        host = m.group(1)
                        if host in INFRA_HOSTS:
                            continue
                        for h, proj in host_to_project.items():
                            if proj != caller and len(h) >= 5 and h in host:
                                owners = [proj]
                                break
                        if owners:
                            break

                for target in owners:
                    key = (caller, target, path)
                    if key in seen:
                        continue
                    seen.add(key)
                    graph[caller]["calls"].append({
                        "target": target,
                        "endpoint": path,
                        "via": ctx,
                    })
                    graph[target]["called_by"].append({
                        "source": caller,
                        "endpoint": path,
                        "via": ctx,
                    })

        return graph

    def save_graph(self, output_path: Path) -> dict:
        graph = self.build_graph()
        Path(output_path).write_text(json.dumps(graph, indent=2))
        return graph

    def get_integrations_for(self, project_name: str) -> dict:
        return self.build_graph().get(project_name, {"calls": [], "called_by": []})

    def print_summary(self):
        graph = self.build_graph()
        print("\n🔗 AUTO-DETECTED INTEGRATIONS (endpoint-based)")
        print("=" * 60)
        found = 0
        for name, data in sorted(graph.items()):
            calls = data["calls"]
            if not calls:
                continue
            found += 1
            # Group by target
            by_target = defaultdict(list)
            for c in calls:
                by_target[c["target"]].append(c["endpoint"])
            print(f"\n  {name}")
            for target, eps in sorted(by_target.items()):
                print(f"    → {target}  [{len(eps)} endpoints]")
                for ep in sorted(set(eps))[:4]:
                    print(f"        {ep}")
                if len(eps) > 4:
                    print(f"        ... +{len(eps)-4} more")
        print(f"\n  Projects with outgoing calls: {found}/{len(graph)}")


if __name__ == "__main__":
    import sys, argparse

    parser = argparse.ArgumentParser(description="Detect integrations via API endpoints")
    parser.add_argument("--project", metavar="NAME", help="Show integrations for one project")
    parser.add_argument("--save",    metavar="FILE", help="Save graph JSON")
    parser.add_argument("--all",     action="store_true", help="Full JSON output")
    args = parser.parse_args()

    roots = [
        Path("/Users/andriy/gitlab-prod"),
        Path("/Users/andriy/github-prod"),
        Path("/Users/andriy/VisualStudio"),
    ]
    project_paths = []
    for root in roots:
        if root.exists():
            for d in sorted(root.iterdir()):
                if d.is_dir() and not d.name.startswith(".") and d.name != "wiki":
                    project_paths.append(d)

    print(f"🔍 Scanning {len(project_paths)} projects...")
    detector = IntegrationDetector(project_paths)

    if args.save:
        detector.save_graph(Path(args.save))
        print(f"✅ Saved: {args.save}")

    if args.project:
        graph = detector.build_graph()
        data = graph.get(args.project)
        if not data:
            print(f"❌ '{args.project}' not found")
            sys.exit(1)
        by_target = defaultdict(list)
        for c in data["calls"]:
            by_target[c["target"]].append(c["endpoint"])
        by_source = defaultdict(list)
        for c in data["called_by"]:
            by_source[c["source"]].append(c["endpoint"])

        print(f"\n🔗 {args.project}")
        print(f"  Calls ({len(data['calls'])}):")
        for target, eps in sorted(by_target.items()):
            print(f"    → {target}  [{len(eps)} endpoints]")
            for ep in sorted(set(eps))[:5]:
                print(f"        {ep}")
        print(f"  Called by ({len(data['called_by'])}):")
        for src, eps in sorted(by_source.items()):
            print(f"    ← {src}  [{len(eps)} endpoints]")
            for ep in sorted(set(eps))[:5]:
                print(f"        {ep}")
    elif args.all:
        print(json.dumps(detector.build_graph(), indent=2))
    else:
        detector.print_summary()
