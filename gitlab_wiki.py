#!/usr/bin/env python3
"""
GitLab Production Wiki Generator
==================================
Сканує /Users/andriy/gitlab-prod, будує wiki з картою зв'язків між проектами.
Збагачує даними з catalog_state.json (cataloger.py): файли, стек, git-історія.
Підтримує LOCAL_ONLY_PROJECTS — проекти які ще не в gitlab але треба в карті.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CLI КОМАНДИ
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  python3 gitlab_wiki.py
      Повне сканування всіх gitlab-prod проектів + генерація wiki.
      Результат: /Users/andriy/gitlab-prod/wiki/

  python3 gitlab_wiki.py --map PROJECT [PROJECT ...]
      Генерує компактну карту вказаних проектів для вставки в промпт.
      Шукає в gitlab-prod І в LOCAL_ONLY_PROJECTS (напр. best-strat-pipeline).
      Результат: виводить в stdout + зберігає в wiki/_prompt_map.md

      Приклади:
        python3 gitlab_wiki.py --map ai-trading-strategy-advisor best-strat-pipeline
        python3 gitlab_wiki.py --map base-states pattern-recognition llm-training-data-miner

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
USER GUIDE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ФЛОУ 1 — Скласти ефективний промпт для Claude Code / Opus
──────────────────────────────────────────────────────────
Мета: замість того щоб Claude витрачав токени на дослідження проектів
через MCP, ти готуєш карту заздалегідь і вставляєш її в промпт.

  Крок 1: Сформулюй задачу (1-2 речення)
      "Інтегрувати best-strat-pipeline як постачальник даних в
       ai-trading-strategy-advisor. Pipeline видає tiered JSON-бенчмарки,
       advisor має використовувати їх паралельно з training_data_unified_v2.2"

  Крок 2: Згенеруй карту проектів
      python3 gitlab_wiki.py --map ai-trading-strategy-advisor best-strat-pipeline

  Крок 3: Відправ локальній LLM (Скуф / llama3.2 на Mac Mini)
      Промпт = задача + вміст wiki/_prompt_map.md
      Скуф поверне: які файли змінити, план по кроках, уточнюючі питання

  Крок 4: Перевір план (2 хв) → відправ до Claude Code
      Промпт = задача + карта + план від Скуфа
      Економія: ~40-60% токенів Opus бо Claude Code не витрачає час
      на дослідження — одразу отримує структурований контекст

ФЛОУ 2 — Підняти проекти локально для тестування інтеграції
─────────────────────────────────────────────────────────────
Мета: перевірити інтеграцію між проектами (напр. best-strat-pipeline +
ai-trading-strategy-advisor) без того щоб Claude витрачав токени
на з'ясування як що запускати, де env змінні, які порти, доступи до БД.

  Крок 1: Згенеруй карту з усіма залежними проектами
      python3 gitlab_wiki.py --map ai-trading-strategy-advisor best-strat-pipeline llm-training-data-miner

      Карта покаже: порти, docker-compose сервіси, .env змінні,
      URL зв'язки між проектами (хто до кого звертається)

  Крок 2: Відправ Скуфу з конкретним запитом
      "На основі цієї карти — напиши покроковий план як підняти
       ai-trading-strategy-advisor локально включно з Postgres
       (llm-training-data-miner). Які .env треба заповнити,
       який порядок запуску docker-compose, як перевірити що все працює"

  Крок 3: Скуф генерує runbook (конкретні команди)
      Ти перевіряєш → виконуєш → якщо щось не так, вставляєш
      помилку + карту до Claude Code для точкового фіксу

  Примітка: llm-training-data-miner має Postgres — треба додати
  його в LOCAL_ONLY_PROJECTS або переконатись що він є в gitlab-prod.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
КОНФІГ
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  LOCAL_ONLY_PROJECTS — додай сюди проекти які не в gitlab-prod
  GITLAB_TO_LOCAL     — маппінг якщо ім'я в gitlab ≠ ім'я в VisualStudio
"""

import os
import re
import json
import subprocess
import argparse
from datetime import datetime, timezone
from pathlib import Path
from collections import defaultdict
from typing import Optional

# ═══════════════════════════════════════════════════════════════
# CONFIG
# ═══════════════════════════════════════════════════════════════

GITLAB_DIR    = Path("/Users/andriy/gitlab-prod")
GITHUB_DIR    = Path("/Users/andriy/github-prod")
WIKI_DIR      = GITLAB_DIR / "wiki"
GITLAB_URL    = "https://git.forvest.software/frv"
CATALOG_STATE = Path("/Users/andriy/VisualStudio/project_cataloger/catalog_state.json")
VISUALSTUDIO_DIR  = Path("/Users/andriy/VisualStudio")
CATALOGER_DIR     = Path("/Users/andriy/VisualStudio/project_cataloger")
INTEGRATION_GRAPH = CATALOGER_DIR / "wiki" / "integration_graph.json"

# Локальні проекти які ще не в gitlab-prod але треба включати в --map
LOCAL_ONLY_PROJECTS = {
    "best-strat-pipeline": "/Users/andriy/VisualStudio/best-strat-pipeline",
    "check_strategies":    "/Users/andriy/VisualStudio/check_strategies",
    "bruteforce-analytics": "/Users/andriy/VisualStudio/bruteforce-analytics",
    "volatility": "/Users/andriy/VisualStudio/volatility",
    "docvault": "/Users/andriy/docvault",
    "adi-token-health": "/Users/andriy/github-prod/adi-token-health",
    "aviator": "/Users/andriy/github-prod/aviator",
    "belief-trajectory-demo": "/Users/andriy/github-prod/belief-trajectory-demo",
    "buyers_insite_Investigation": "/Users/andriy/github-prod/buyers_insite_Investigation",
    "claude-codebase-navigator": "/Users/andriy/github-prod/claude-codebase-navigator",
    "corporate-data": "/Users/andriy/github-prod/corporate-data",
    "FamilyTranslator": "/Users/andriy/github-prod/FamilyTranslator",
    "live-predictor": "/Users/andriy/github-prod/live-predictor",
    "live-predictor-system": "/Users/andriy/github-prod/live-predictor-system",
    "markov-predictor": "/Users/andriy/github-prod/markov-predictor",
    "markov_quantile_predictor": "/Users/andriy/github-prod/markov_quantile_predictor",
    "predictor_mq": "/Users/andriy/github-prod/predictor_mq",
    "predictor_mq_3.0": "/Users/andriy/github-prod/predictor_mq_3.0",
    "profit-radar-ai": "/Users/andriy/github-prod/profit-radar-ai",
    "profitradar.io": "/Users/andriy/github-prod/profitradar.io",
    "smart_sales": "/Users/andriy/github-prod/smart_sales",
    "strategy-market": "/Users/andriy/github-prod/strategy-market",
    "verdict": "/Users/andriy/github-prod/verdict",
    "VoiceVocab-Trainer": "/Users/andriy/github-prod/VoiceVocab-Trainer",
    "rox": "/Users/andriy/VisualStudio/rox",
}

# Name mapping: gitlab project name → VisualStudio local name (if different)
GITLAB_TO_LOCAL = {
    "ai-trading-strategy-advisor": "ai-trading-strategy-advisor",
    "base-states": "base-states",
    "bottom-model": "bottom-model",
    "llm-training-data-miner": "llm-training-data-miner",
    "scalping-pnl": "scalping-pnl",
    "profitradar": "profitradar_ui",  # different local name
    "profitradar-api": "profit-radar-io",
    "profitradar-landing": "profitradar-landings",
    "indicators-basic": "indicators-basic",
    "shark-bot": "shark-bot",
    "candle-miner": "candle-miner",
    "funding-rate-miner": "funding-rate-miner-master 2",
    "adi-token-dashboard": "adi-token-dashboard",
    "ai-trading-strategy-advisor": "ai-trading-strategy-advisor",
    "simple-evaluation-framework": "simple-evaluation-framework",
    "scalping-pnl-info": "scalping-pnl-info",
    "signal-emulator": "signal-emulator"
}

# ═══════════════════════════════════════════════════════════════
# PROJECT METADATA (вручную дополняется)
# ═══════════════════════════════════════════════════════════════

CATEGORIES = {
    "core_platform": {
        "icon": "🚀",
        "title": "Core Platform",
        "projects": ["profitradar", "profitradar-api", "profitradar-landing", "admin-dashboard", "scalping-ui"],
    },
    "ai_advisor": {
        "icon": "🧠",
        "title": "AI & LLM",
        "projects": ["ai-trading-strategy-advisor", "llm-training-data-miner", "simple-evaluation-framework", "base-states"],
    },
    "trading_engine": {
        "icon": "📊",
        "title": "Trading Engine",
        "projects": ["scalping-pnl", "scalping-pnl-info", "shark-bot", "shark-monitoring", "bottom-model"],
    },
    "data_infrastructure": {
        "icon": "🗄",
        "title": "Data Infrastructure",
        "projects": ["candle-miner", "indicators-basic", "indicator-tests", "funding-rate-miner",
                     "forex-data-miners", "stock-data-miners", "slippage-analytics"],
    },
    "tools": {
        "icon": "🛠",
        "title": "Tools & Utils",
        "projects": ["telegram-bot", "wizard-backend", "darvin", "inc-analytics", "profit-radar"],
    },
}

# Ручное описание связей (откуда → куда, что передаётся)
KNOWN_INTEGRATIONS = {
    "profitradar": [
        {"target": "profitradar-api", "type": "HTTP", "url": "http://localhost:8005 (VITE_API_BASE_URL)", "data": "Trading signals, strategies"},
        {"target": "ai-trading-strategy-advisor", "type": "HTTP", "url": "port 8005", "data": "AI advisor queries"},
    ],
    "profitradar-api": [
        {"target": "ai-trading-strategy-advisor", "type": "HTTP", "url": "AI_ORCHESTRATOR_URL=http://localhost:8001", "data": "Strategy queries → AI synthesis"},
        {"target": "scalping-pnl", "type": "HTTP", "url": "BACKTESTING_URL=http://localhost:8002", "data": "Backtest requests"},
        {"target": "indicators-basic", "type": "ClickHouse", "url": "db_candles_binance_futures", "data": "Market data (OHLCV)"},
    ],
    "ai-trading-strategy-advisor": [
        {"target": "llm-training-data-miner", "type": "data", "url": "brute_* catalog files", "data": "Strategy catalog for semantic search"},
        {"target": "base-states", "type": "DB", "url": "postgresql (shared DB)", "data": "Market regime states R1-R12"},
    ],
    "llm-training-data-miner": [
        {"target": "scalping-pnl", "type": "HTTP/K8S", "url": "K8S_SERVICE_URL=https://info.lab.mmi.ai / port 8080", "data": "Bruteforce backtest results"},
        {"target": "indicators-basic", "type": "ClickHouse", "url": "db_candles_binance_futures", "data": "OHLCV candles for training data"},
        {"target": "scalping-pnl", "type": "ClickHouse", "url": "db_scalping_backtests", "data": "Backtest results DB"},
    ],
    "base-states": [
        {"target": "ai-trading-strategy-advisor", "type": "DB", "url": "postgresql (shared DB)", "data": "Provides R1-R12 regime labels"},
        {"target": "indicators-basic", "type": "ClickHouse", "url": "db_candles_binance_futures", "data": "Raw candles for regime classification"},
    ],
    "scalping-pnl": [
        {"target": "indicators-basic", "type": "internal", "url": "port 5000 (features container)", "data": "Indicator features"},
        {"target": "scalping-pnl-info", "type": "HTTP", "url": "http://backtest:10080", "data": "Backtest calculation results"},
    ],
    "simple-evaluation-framework": [
        {"target": "ai-trading-strategy-advisor", "type": "HTTP", "url": "ADVISER_URL=http://localhost:8005", "data": "Eval queries to advisor"},
    ],
    "shark-bot": [
        {"target": "telegram-bot", "type": "HTTP", "url": "WEBHOOK", "data": "Trade notifications → Telegram"},
        {"target": "shark-monitoring", "type": "DB", "url": "shared DB", "data": "Account status monitoring"},
        {"target": "wizard-backend", "type": "HTTP", "url": "PORT env", "data": "Manual trade commands"},
    ],
    "shark-monitoring": [
        {"target": "telegram-bot", "type": "HTTP", "url": "WEBHOOK/WEBHOOK2", "data": "Monitoring alerts"},
    ],
    "candle-miner": [
        {"target": "indicators-basic", "type": "ClickHouse", "url": "db_candles_{market}", "data": "Writes OHLCV candles"},
    ],
    "indicators-basic": [
        {"target": "scalping-pnl", "type": "HTTP", "url": "port 5000", "data": "RSI, BBE indicators"},
        {"target": "indicator-tests", "type": "HTTP", "url": "realtime API", "data": "Indicator values for verification"},
    ],
    "forex-data-miners": [
        {"target": "indicators-basic", "type": "ClickHouse", "url": "db_candles_forex", "data": "Forex OHLCV data"},
    ],
    "stock-data-miners": [
        {"target": "indicators-basic", "type": "ClickHouse", "url": "db_candles_stocks", "data": "NASDAQ OHLCV data"},
    ],
    "scalping-ui": [
        {"target": "scalping-pnl",  "type": "HTTP", "url": "backtesting_api.js", "data": "Backtesting requests, experiment management"},
        {"target": "scalping-pnl-info", "type": "HTTP", "url": "connectors/", "data": "PnL info, brute results"},
        {"target": "shark-bot",     "type": "HTTP", "url": "bot_api.js",      "data": "Trading commands, account management"},
        {"target": "shark-monitoring", "type": "DB", "url": "shared DB",      "data": "Account monitoring data"},
    ],
    "profitradar": [
        {"target": "scalping-ui",   "type": "HTTP", "url": "SCALPING_UI_URL", "data": "UI proxy — admin panel"},
        {"target": "scalping-pnl",  "type": "HTTP", "url": "BACKTESTING_URL", "data": "Backtesting results"},
        {"target": "shark-bot",     "type": "HTTP", "url": "SHARK_BOT_URL",   "data": "Bot controls"},
        {"target": "ai-trading-strategy-advisor", "type": "HTTP", "url": "AI_ORCHESTRATOR_URL", "data": "AI advisor queries"},
    ],
}

# ═══════════════════════════════════════════════════════════════
# LOCAL CATALOG LOADER
# ═══════════════════════════════════════════════════════════════

def load_local_catalog() -> dict:
    """Load catalog_state.json produced by cataloger.py"""
    if not CATALOG_STATE.exists():
        print("⚠️  catalog_state.json not found — skipping local enrichment")
        return {}
    with open(CATALOG_STATE) as f:
        return json.load(f)


def enrich_with_local(project: dict, local_catalog: dict) -> dict:
    """
    Merge gitlab project data with local VisualStudio catalog data.
    Local catalog has: files stats, full README, tech_stack, git history, status.
    """
    gitlab_name = project["name"]
    local_name = GITLAB_TO_LOCAL.get(gitlab_name, gitlab_name)
    local = local_catalog.get(local_name)

    if not local:
        return project  # no local match, return as-is

    project["local_name"] = local_name
    project["local_path"] = local.get("path", "")

    # Enrich README from local if not found in gitlab clone
    if not project.get("readme") and local.get("readme"):
        project["readme"] = local["readme"]

    # Enrich tech stack: merge local frameworks into gitlab tech
    local_stack = local.get("tech_stack", {})
    for fw in local_stack.get("frameworks", []):
        if fw not in project["tech"]["frameworks"]:
            project["tech"]["frameworks"].append(fw)
    for lang in local_stack.get("languages", []):
        if lang not in project["tech"]["lang"]:
            project["tech"]["lang"].append(lang)

    # Add local file stats
    local_files = local.get("files", {})
    by_type = local_files.get("by_type", {})
    project["local_files"] = {
        "total": local_files.get("total_indexed", 0),
        "code": by_type.get("code", {}).get("count", 0),
        "docs": by_type.get("docs", {}).get("count", 0),
        "data": by_type.get("data", {}).get("count", 0),
        "key_files": sorted(
            [f["path"] for f in by_type.get("code", {}).get("files", [])
             if not f["path"].endswith((".txt", ".log", ".md"))],
            key=lambda p: (
                0 if any(k in Path(p).name for k in ["orchestrator","semantic","app","main","config","models","pipeline","cli"]) else 1,
                len(p.split("/"))
            )
        )[:8],
    }

    # Use local git history (may be richer — local has actual work history)
    local_git = local.get("git")
    if local_git and local_git.get("commit_count", 0) > project["git"].get("commit_count", 0):
        project["git_local"] = local_git  # keep both, show local as primary history

    # Use local status if more informative
    local_status = local.get("status", "")
    if "active" in local_status and "active" not in project["status"]:
        project["status"] = local_status  # local has fresher uncommitted changes

    project["local_summary"] = local.get("summary", "")

    return project


# ═══════════════════════════════════════════════════════════════
# SCANNER
# ═══════════════════════════════════════════════════════════════

def find_key_files(project_path: Path, limit: int = 10) -> list:
    """Find key code files by scanning disk directly — more accurate than catalog_state."""
    PRIORITY_NAMES = {"orchestrator", "semantic", "app", "main", "config", "models",
                      "pipeline", "cli", "router", "search", "knowledge", "advisor"}
    SKIP_DIRS = {"node_modules", ".git", "__pycache__", ".venv", "venv", "dist", "build",
                 ".next", "coverage", ".cache"}
    CODE_EXT = {".py", ".ts", ".js", ".tsx", ".jsx", ".sh"}

    found = []
    for root, dirs, files in os.walk(project_path):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            if Path(f).suffix.lower() not in CODE_EXT:
                continue
            rel = str(Path(root).relative_to(project_path) / f)
            priority = 0 if any(k in f.lower() for k in PRIORITY_NAMES) else 1
            depth = len(Path(rel).parts)
            found.append((priority, depth, rel))

    found.sort()
    return [r for _, _, r in found[:limit]]


def parse_docker_compose(path: Path) -> dict:
    """
    Parse docker-compose.yml: витягує сервіси, порти та env змінні з дефолтами.
    Повертає:
      {
        "services": {
          "postgres": {
            "ports": [{"host": "15432", "container": "5432"}],
            "env": {"POSTGRES_USER": "llm_training", "DB_PORT": "15432", ...}
          },
          ...
        }
      }
    """
    result = {"services": {}}
    for fname in ["docker-compose.yml", "docker-compose.yaml"]:
        dc = path / fname
        if not dc.exists():
            continue
        text = dc.read_text(errors="ignore")

        # Знаходимо блоки сервісів через простий парсинг (без yaml-залежності)
        current_service = None
        in_ports = False
        in_environment = False
        indent_service = 2  # типово services: indent 2, service name indent 2

        for line in text.splitlines():
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue

            indent = len(line) - len(line.lstrip())

            # Детект імені сервісу (рівень 2 відступу під services:)
            if indent == 2 and stripped.endswith(":") and not stripped.startswith("-"):
                svc_name = stripped[:-1]
                # Пропускаємо top-level keys та суфікси _data / _network / _volume
                skip = ("version", "services", "volumes", "networks", "configs", "secrets")
                skip_suffix = ("_data", "_network", "_volume", "_db", "_cache", "-network", "-data")
                if svc_name not in skip and not any(svc_name.endswith(s) for s in skip_suffix):
                    current_service = svc_name
                    result["services"].setdefault(current_service, {"ports": [], "env": {}})
                else:
                    current_service = None  # скидаємо щоб не збирати в цей блок
                in_ports = False
                in_environment = False
                continue

            if current_service is None:
                continue

            svc = result["services"][current_service]

            # Детект секцій ports / environment
            if indent == 4:
                in_ports = stripped == "ports:"
                in_environment = stripped in ("environment:", "env:")
                continue

            # Парсинг портів
            if in_ports and indent == 6:
                raw = stripped.lstrip("- ").strip().strip("\"'")
                # Витягуємо числові значення з будь-якого формату:
                # "8005:8005", "${PORT:-8005}:${PORT:-8005}", "15432:5432"
                nums = re.findall(r'(?<!\d)(\d{2,5})(?!\d)', raw)
                if len(nums) >= 2:
                    svc["ports"].append({"host": nums[0], "container": nums[-1]})
                elif len(nums) == 1:
                    svc["ports"].append({"host": nums[0], "container": nums[0]})
                continue

            # Парсинг environment
            if in_environment and indent == 6:
                raw = stripped.lstrip("- ").strip()
                # KEY=VALUE першим (щоб KEY=${VAR:-default} не розбивалось по ":")
                eq_match = re.match(r'^([A-Za-z_][A-Za-z0-9_]*)=(.*)$', raw)
                colon_match = re.match(r'^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$', raw)
                if eq_match:
                    k, v = eq_match.group(1), eq_match.group(2).strip().strip("\"'")
                    dm = re.search(r'\$\{[A-Za-z_]+(?::?[-=])([^}]+)\}', v)
                    if dm:
                        v = dm.group(1).strip()
                    svc["env"][k] = v
                elif colon_match:
                    k, v = colon_match.group(1), colon_match.group(2).strip().strip("\"'")
                    dm = re.search(r'\$\{[A-Za-z_]+(?::?[-=])([^}]+)\}', v)
                    if dm:
                        v = dm.group(1).strip()
                    svc["env"][k] = v
        break  # читаємо тільки перший знайдений файл
    return result


def detect_ports(path: Path) -> list:
    """Extract exposed ports (flat list) — використовує parse_docker_compose."""
    dc = parse_docker_compose(path)
    ports = []
    for svc in dc["services"].values():
        ports.extend(svc["ports"])
    return ports

def git_info(path: Path) -> dict:
    """Quick git metadata for a local repo."""
    def run(args):
        r = subprocess.run(["git"] + args, cwd=path, capture_output=True, text=True, timeout=8)
        return r.stdout.strip() if r.returncode == 0 else None
    try:
        latest_ref = run(["for-each-ref", "--sort=-committerdate", "refs/heads/", "refs/remotes/", "--format=%(refname:short)", "--count=1"])
        if latest_ref and latest_ref.startswith("origin/"):
            latest_ref = latest_ref[7:]
        branch = latest_ref or run(["rev-parse", "--abbrev-ref", "HEAD"])
        return {
            "branch": branch,
            "last_commit_date": run(["log", "-1", "--all", "--format=%aI"]),
            "last_commit_msg": run(["log", "-1", "--all", "--format=%s"]),
            "commit_count": int(run(["rev-list", "--count", "--all"]) or 0),
        }
    except Exception:
        return {}


def detect_tech(path: Path) -> dict:
    stack = {"lang": [], "frameworks": [], "tools": []}
    if (path / "requirements.txt").exists() or (path / "pyproject.toml").exists():
        stack["lang"].append("Python")
    if (path / "package.json").exists():
        try:
            pkg = json.loads((path / "package.json").read_text(errors="ignore"))
            deps = {**pkg.get("dependencies", {}), **pkg.get("devDependencies", {})}
            if "react" in deps: stack["frameworks"].append("React")
            if "next" in deps: stack["frameworks"].append("Next.js")
            if "typescript" in deps: stack["frameworks"].append("TypeScript")
            if "vite" in deps: stack["frameworks"].append("Vite")
            stack["lang"].append("Node.js/TypeScript")
        except Exception:
            stack["lang"].append("Node.js")
    if (path / "Dockerfile").exists() or list(path.glob("Dockerfile.*")):
        stack["tools"].append("Docker")

    req = path / "requirements.txt"
    if req.exists():
        txt = req.read_text(errors="ignore").lower()
        for k, v in {"fastapi": "FastAPI", "flask": "Flask", "uvicorn": "uvicorn",
                     "pandas": "Pandas", "numpy": "NumPy", "clickhouse": "ClickHouse",
                     "openai": "OpenAI", "langchain": "LangChain", "pgvector": "pgvector",
                     "deepeval": "DeepEval", "asyncpg": "PostgreSQL"}.items():
            if k in txt and v not in stack["frameworks"]:
                stack["frameworks"].append(v)
    return stack


def infer_status(git: dict) -> str:
    if not git.get("last_commit_date"):
        return "⚪ unknown"
    if git.get("recent_commits_30d", 0) > 0:
        return "🟢 active"
    try:
        from datetime import datetime, timezone
        last = datetime.fromisoformat(git["last_commit_date"])
        if last.tzinfo is None:
            last = last.replace(tzinfo=timezone.utc)
        days = (datetime.now(timezone.utc) - last).days
        if days < 90: return "🟡 recent"
        elif days < 365: return "🟠 dormant"
        else: return "🔴 archived"
    except Exception:
        return "⚪ unknown"


def get_readme(path: Path) -> Optional[str]:
    for name in ["README.md", "readme.md", "README.txt"]:
        p = path / name
        if p.exists():
            try:
                return p.read_text(errors="ignore")[:2000]
            except Exception:
                pass
    return None


def detect_category(name: str) -> str:
    for cat_id, cat in CATEGORIES.items():
        if name in cat["projects"]:
            return cat_id
    return "tools"


def scan_project(path: Path, local_catalog: dict = None) -> dict:
    name = path.name
    git = git_info(path)
    docker = parse_docker_compose(path)
    ports = []
    for svc in docker["services"].values():
        ports.extend(svc["ports"])
    tech = detect_tech(path)
    readme = get_readme(path)
    status = infer_status(git)
    category = detect_category(name)
    integrations = KNOWN_INTEGRATIONS.get(name, [])
    consumed_by = []
    for src, links in KNOWN_INTEGRATIONS.items():
        for link in links:
            if link["target"] == name:
                consumed_by.append({"source": src, "type": link["type"], "data": link["data"]})

    project = {
        "name": name,
        "path": str(path),
        "gitlab_url": f"{GITLAB_URL}/{name}",
        "status": status,
        "category": category,
        "git": git,
        "ports": ports,
        "docker": docker,
        "tech": tech,
        "readme": readme,
        "integrations": integrations,
        "consumed_by": consumed_by,
        "local_files": None,
        "local_name": None,
        "local_path": None,
        "local_summary": "",
        "git_local": None,
    }

    if local_catalog:
        project = enrich_with_local(project, local_catalog)

    return project


# ═══════════════════════════════════════════════════════════════
# WIKI GENERATOR
# ═══════════════════════════════════════════════════════════════

def gen_project_page(p: dict, wiki_dir: Path):
    lines = []
    cat = next((c for c in CATEGORIES.values() if p["category"] == next(
        (k for k, v in CATEGORIES.items() if v == c), None)), None)
    cat_info = CATEGORIES.get(p["category"], {"icon": "📦", "title": p["category"]})

    lines += [
        f"# {p['name']}",
        "",
        f"**Статус:** {p['status']}  ",
        f"**Категория:** {cat_info['icon']} {cat_info['title']}  ",
        f"**GitLab:** [{p['name']}]({p['gitlab_url']})  ",
        "",
    ]

    # Docker services
    docker = p.get("docker", {})
    if docker.get("services"):
        lines.append("## 🐳 Docker Services")
        lines.append("")
        lines.append("| Сервіс | Host port → Container | Ключові env |")
        lines.append("|--------|----------------------|-------------|")
        KEY_ENV = {"POSTGRES_USER", "POSTGRES_DB", "DB_PORT", "DB_NAME", "API_PORT",
                   "CLICKHOUSE_PORT", "CLICKHOUSE_DATABASE", "MINIO_API_PORT"}
        for svc_name, svc in docker["services"].items():
            port_str = "<br>".join(f"`{p['host']}→{p['container']}`" for p in svc["ports"]) or "—"
            shown = {k: v for k, v in svc["env"].items()
                     if k in KEY_ENV or not v.startswith("${")}
            env_str = "<br>".join(f"`{k}={v}`" for k, v in list(shown.items())[:6]) or "—"
            lines.append(f"| `{svc_name}` | {port_str} | {env_str} |")
        lines.append("")

    # Tech
    tech = p["tech"]
    if any(tech.values()):
        lines.append("## 🛠 Tech Stack")
        lines.append("")
        if tech["lang"]: lines.append(f"- **Lang:** {', '.join(tech['lang'])}")
        if tech["frameworks"]: lines.append(f"- **Frameworks:** {', '.join(tech['frameworks'])}")
        if tech["tools"]: lines.append(f"- **Tools:** {', '.join(tech['tools'])}")
        lines.append("")

    # Outgoing integrations
    if p["integrations"]:
        lines.append("## 📤 Отправляет данные в")
        lines.append("")
        lines.append("| Сервис | Тип | URL / Channel | Данные |")
        lines.append("|--------|-----|---------------|--------|")
        for i in p["integrations"]:
            lines.append(f"| [{i['target']}]({i['target']}.md) | `{i['type']}` | `{i['url']}` | {i['data']} |")
        lines.append("")

    # Incoming integrations
    if p["consumed_by"]:
        lines.append("## 📥 Потребляется из")
        lines.append("")
        lines.append("| Источник | Тип | Данные |")
        lines.append("|----------|-----|--------|")
        for c in p["consumed_by"]:
            lines.append(f"| [{c['source']}]({c['source']}.md) | `{c['type']}` | {c['data']} |")
        lines.append("")

    # Git
    git = p["git"]
    lines += [
        "## 📊 Git",
        "",
        f"- **Branch:** `{git.get('branch', '—')}`",
        f"- **Коммитов:** {git.get('commit_count', 0)}",
        f"- **Последний:** {git.get('last_commit_date', '—')}",
        f"- **Сообщение:** {git.get('last_commit_msg', '—')}",
        f"- **За 30 дней:** {git.get('recent_commits_30d', 0)} коммитов",
        "",
    ]
    if git.get("timeline"):
        lines.append("### Последние коммиты")
        lines.append("")
        for t in git["timeline"]:
            lines.append(f"- `{t['date']}` {t['msg']}")
        lines.append("")

    # Local VisualStudio files
    lf = p.get("local_files")
    if lf and lf.get("total", 0) > 0:
        lines.append("## 📁 Local Files (VisualStudio)")
        lines.append("")
        local_name = p.get("local_name") or p["name"]
        local_path = p.get("local_path") or ""
        lines.append(f"**Local path:** `{local_path}`  ")
        lines.append(f"**Summary:** {lf['code']} code, {lf['docs']} docs, {lf['data']} data files ({lf['total']} total)")
        if lf.get("key_files"):
            lines.append("")
            lines.append("**Key files:**")
            for f in lf["key_files"][:10]:
                lines.append(f"- `{f}`")
        lines.append("")

    # Local git history (if richer than gitlab)
    git_local = p.get("git_local")
    if git_local:
        lines.append("## 📊 Local Git History (VisualStudio)")
        lines.append("")
        lines.append(f"- **Коммитов:** {git_local.get('commit_count', 0)} (vs {p['git'].get('commit_count', 0)} в gitlab clone)")
        lines.append(f"- **Последний:** {git_local.get('last_commit_date', '—')}")
        lines.append(f"- **Сообщение:** {git_local.get('last_commit_msg', '—')}")
        lines.append(f"- **За 30 дней:** {git_local.get('recent_commits_30d', 0)} коммитов")
        if git_local.get("timeline"):
            lines.append("")
            for t in git_local["timeline"]:
                lines.append(f"  - `{t['date']}` {t['msg']}")
        lines.append("")

    # README
    if p.get("readme"):
        lines += ["## 📝 README", "", "```", p["readme"][:1500], "```", ""]

    (wiki_dir / f"{p['name']}.md").write_text("\n".join(lines))


def gen_index(projects: dict, wiki_dir: Path):
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        "# 🏭 GitLab Production Wiki — frv group",
        "",
        f"*Автосгенерировано: {now}*  ",
        f"*Проектов: {len(projects)}*",
        "",
        "## 📋 Навигация",
        "",
        "| Страница | Описание |",
        "|----------|----------|",
        "| [Integration Map](INTEGRATION_MAP.md) | 🗺 Карта связей между сервисами |",
        "| [Status Dashboard](STATUS.md) | 🚦 Статус всех проектов |",
        "",
    ]

    for cat_id, cat in CATEGORIES.items():
        cat_projects = [p for p in projects.values() if p["category"] == cat_id]
        if not cat_projects:
            continue
        lines.append(f"## {cat['icon']} {cat['title']}")
        lines.append("")
        for p in sorted(cat_projects, key=lambda x: x["name"]):
            ports_str = ""
            if p["ports"]:
                seen = list(dict.fromkeys(port["host"] for port in p["ports"]))[:3]
                ports_str = f" | ports: {', '.join(seen)}"
            links_count = len(p["integrations"]) + len(p["consumed_by"])
            links_str = f" | 🔗 {links_count} links" if links_count else ""
            lines.append(f"- {p['status']} [{p['name']}](projects/{p['name']}.md){ports_str}{links_str}")
        lines.append("")

    (wiki_dir / "INDEX.md").write_text("\n".join(lines))


def gen_integration_map(projects: dict, wiki_dir: Path):
    lines = [
        "# 🗺 Integration Map — связи между сервисами",
        "",
        "*Карта того кто с кем общается, по каким портам и что передаёт*",
        "",
        "## Граф зависимостей (text)",
        "",
        "```",
    ]

    # Build text graph
    for name, p in sorted(projects.items()):
        if not p["integrations"]:
            continue
        for i in p["integrations"]:
            lines.append(f"  {name} ──[{i['type']} {i['url']}]──► {i['target']}")
            lines.append(f"         data: {i['data']}")
            lines.append("")
    lines.append("```")
    lines.append("")

    # Shared infrastructure
    lines += [
        "## 🗄 Общая инфраструктура",
        "",
        "| Ресурс | Используется в |",
        "|--------|----------------|",
    ]
    ch_users = [n for n, p in projects.items()
                if any("ClickHouse" in str(i) for i in p["integrations"])]
    pg_users = [n for n, p in projects.items()
                if any("postgresql" in str(i).lower() or "PostgreSQL" in str(i) for i in p["integrations"])
                or "PostgreSQL" in p["tech"].get("frameworks", [])]
    if ch_users:
        lines.append(f"| **ClickHouse** `49.12.17.251:8123` | {', '.join(ch_users)} |")
    if pg_users:
        lines.append(f"| **PostgreSQL** | {', '.join(pg_users)} |")
    lines.append(f"| **MinIO** `port 9000/9001` | llm-training-data-miner |")
    lines.append("")

    # Full table
    lines += [
        "## 📋 Полная таблица связей",
        "",
        "| Источник | → Цель | Тип | URL / Channel | Данные |",
        "|----------|--------|-----|---------------|--------|",
    ]
    for name, p in sorted(projects.items()):
        for i in p["integrations"]:
            lines.append(
                f"| [{name}](projects/{name}.md) | [{i['target']}](projects/{i['target']}.md) "
                f"| `{i['type']}` | `{i['url']}` | {i['data']} |"
            )
    lines.append("")

    (wiki_dir / "INTEGRATION_MAP.md").write_text("\n".join(lines))


def gen_status(projects: dict, wiki_dir: Path):
    lines = [
        "# 🚦 Status Dashboard",
        "",
        f"*Обновлено: {datetime.now().strftime('%Y-%m-%d %H:%M')}*",
        "",
        "| Проект | Статус | Ветка | Последний коммит | Дней назад |",
        "|--------|--------|-------|-----------------|------------|",
    ]
    for name, p in sorted(projects.items(), key=lambda x: x[1]["git"].get("last_commit_date") or "", reverse=True):
        git = p["git"]
        days = ""
        if git.get("last_commit_date"):
            try:
                last = datetime.fromisoformat(git["last_commit_date"])
                if last.tzinfo is None:
                    last = last.replace(tzinfo=timezone.utc)
                days = str((datetime.now(timezone.utc) - last).days)
            except Exception:
                pass
        lines.append(
            f"| [{name}](projects/{name}.md) | {p['status']} "
            f"| `{git.get('branch', '—')}` "
            f"| {git.get('last_commit_date', '—')} "
            f"| {days} |"
        )
    lines.append("")
    (wiki_dir / "STATUS.md").write_text("\n".join(lines))


def _fmt_size(size_bytes: int) -> str:
    if size_bytes >= 1024 * 1024:
        return f"{size_bytes / 1024 / 1024:.0f}MB"
    if size_bytes >= 1024:
        return f"{size_bytes / 1024:.0f}KB"
    return f"{size_bytes}B"


def _render_project_block(name, git, tech, readme, status, path, gitlab_url,
                           docker, integrations, consumed_by,
                           local_files, project_names, catalog_local) -> list:
    """Render one project block for --map output. Maximally informative for Claude."""
    lines = []

    # Header
    header = f"## {status} {name}"
    if gitlab_url:
        header += f"  |  GitLab: {gitlab_url}"
    lines.append(header)
    lines.append("")

    # Path & Git
    if path:
        lines.append(f"**Path:** `{path}`")
    branch   = git.get("branch", "—")
    last_date = git.get("last_commit_date", "—")
    last_msg  = git.get("last_commit_msg", "—")
    commits   = git.get("commit_count", 0)
    recent    = git.get("recent_commits_30d", 0)
    lines.append(f"**Git:** branch `{branch}` | {commits} commits | {recent} in last 30d")
    lines.append(f"**Last commit:** {last_date} — {last_msg}")
    if git.get("timeline"):
        items = [f"`{t['date'][:10]}` {t['msg']}" for t in git["timeline"][:3]]
        lines.append("**Recent commits:** " + " → ".join(items))
    lines.append("")

    # Tech Stack
    lang  = tech.get("lang", [])
    fw    = tech.get("frameworks", [])
    tools = tech.get("tools", [])
    parts = []
    if lang:  parts.append("Lang: " + ", ".join(lang))
    if fw:    parts.append("Frameworks: " + ", ".join(fw))
    if tools: parts.append("Tools: " + ", ".join(tools))
    if parts:
        lines.append("**Stack:** " + " | ".join(parts))
        lines.append("")

    # Docker services
    if docker and docker.get("services"):
        lines.append("**Docker services:**")
        dc_path = Path(path) if path else None
        for svc_name, svc in docker["services"].items():
            port_str = ", ".join(
                f"{pr['host']}→{pr['container']}" for pr in svc["ports"]
            ) if svc["ports"] else "no ports"
            lines.append(f"  - `{svc_name}`: ports {port_str}")
            KEY_ENV = {"POSTGRES_USER", "POSTGRES_PASSWORD", "POSTGRES_DB",
                       "DB_PORT", "DB_NAME", "DB_HOST", "DB_PASSWORD",
                       "API_PORT", "CLICKHOUSE_PORT", "CLICKHOUSE_DATABASE",
                       "MINIO_API_PORT", "OPENAI_API_KEY", "REDIS_URL"}
            shown = {k: v for k, v in svc["env"].items()
                     if k in KEY_ENV or (v and not v.startswith("${"))}
            if shown:
                env_parts = ", ".join(f"{k}={v}" for k, v in list(shown.items())[:8])
                lines.append(f"    env: {env_parts}")
        if dc_path and (dc_path / "docker-compose.yml").exists():
            lines.append(f"  → Start: `docker-compose up -d` in `{path}`")
        lines.append("")

    # Key files from catalog_state
    by_type = catalog_local.get("files", {}).get("by_type", {}) if catalog_local else {}
    code_files = by_type.get("code", {}).get("files", [])
    doc_files  = by_type.get("docs", {}).get("files", [])
    data_files = by_type.get("data", {}).get("files", [])

    # Fallback: scan directly if no catalog
    if not code_files and path and Path(path).exists():
        raw = find_key_files(Path(path), limit=10)
        code_files = [{"path": f, "size": 0} for f in raw]

    if code_files:
        lines.append("**Key source files:**")
        for f in code_files[:10]:
            sz = f" ({_fmt_size(f['size'])})" if f.get("size") else ""
            lines.append(f"  - `{f['path']}`{sz}")
        lines.append("")

    if doc_files:
        lines.append("**Docs:**")
        for f in doc_files[:6]:
            sz = f" ({_fmt_size(f['size'])})" if f.get("size") else ""
            lines.append(f"  - `{f['path']}`{sz}")
        lines.append("")

    code_cnt = by_type.get("code", {}).get("count", 0)
    docs_cnt = by_type.get("docs", {}).get("count", 0)
    data_cnt = by_type.get("data", {}).get("count", 0)
    if code_cnt or docs_cnt:
        lines.append(f"**File counts:** {code_cnt} code, {docs_cnt} docs, {data_cnt} data")
        lines.append("")

    # ── Integrations ─────────────────────────────────────────────────────────
    int_graph = _load_integration_graph()
    g = int_graph.get(name, {})

    # Auto-detected: group by target/source with endpoints + source file
    auto_by_target = defaultdict(list)  # target → [(endpoint, via_file)]
    for c in g.get("calls", []):
        auto_by_target[c["target"]].append((c.get("endpoint",""), c.get("via","")))

    auto_by_source = defaultdict(list)  # source → [(endpoint, via_file)]
    for c in g.get("called_by", []):
        auto_by_source[c["source"]].append((c.get("endpoint",""), c.get("via","")))

    # Manual KNOWN_INTEGRATIONS (kept for non-auto cases)
    manual_out = [i for i in integrations if i["target"] not in auto_by_target]
    manual_in  = [i for i in consumed_by  if i["source"] not in auto_by_source]

    # Render outgoing
    if auto_by_target or manual_out:
        lines.append("**Calls →**")
        for target, items in sorted(auto_by_target.items()):
            in_map = "🗺" if target in project_names else "🌐"
            eps = sorted(set(ep for ep, _ in items if ep))
            via_files = sorted(set(v for _, v in items if v))
            eps_str = ", ".join(eps[:5])
            if len(eps) > 5:
                eps_str += f" +{len(eps)-5} more"
            via_str = f"  _(in `{via_files[0]}`)" if via_files else ""
            lines.append(f"  - {in_map} `{target}`: {eps_str}{via_str}")
        for i in manual_out:
            lines.append(f"  - 🌐 `{i['target']}` via {i['type']} `{i.get('url','')}` → {i['data']}")
        lines.append("")
    if auto_by_source or manual_in:
        lines.append("**Called by ←**")
        for source, items in sorted(auto_by_source.items()):
            in_map = "🗺" if source in project_names else "🌐"
            eps = sorted(set(ep for ep, _ in items if ep))
            via_files = sorted(set(v for _, v in items if v))
            eps_str = ", ".join(eps[:5])
            if len(eps) > 5:
                eps_str += f" +{len(eps)-5} more"
            via_str = f"  _(in `{via_files[0]}`)" if via_files else ""
            lines.append(f"  - {in_map} `{source}`: {eps_str}{via_str}")
        for i in manual_in:
            lines.append(f"  - 🌐 `{i['source']}` via {i['type']} → {i['data']}")
        lines.append("")

    # README — first 2 meaningful paragraphs
    if readme:
        paragraphs = []
        for para in readme.split("\n\n"):
            clean = para.strip()
            if not clean or clean.startswith("!["):
                continue
            if clean.startswith("#"):
                clean = clean.lstrip("#").strip()
            paragraphs.append(clean.replace("\n", " "))
            if len(paragraphs) >= 2:
                break
        if paragraphs:
            lines.append("**What this project does:**")
            for para in paragraphs:
                lines.append(f"  {para[:500]}")
            lines.append("")

    # Concept / Spec docs — include excerpt
    CONCEPT_NAMES = {"CONCEPT", "SPEC", "ARCHITECTURE", "DESIGN", "OVERVIEW",
                     "PLAN", "CLAUDE", "SUCCESSOR"}
    if path and Path(path).exists() and doc_files:
        for f in doc_files[:20]:
            if any(kw in Path(f["path"]).stem.upper() for kw in CONCEPT_NAMES):
                fpath = Path(path) / f["path"]
                if fpath.exists():
                    try:
                        content = fpath.read_text(errors="ignore")[:800]
                        lines.append(f"**{Path(f['path']).name}** (excerpt):")
                        lines.append("```")
                        lines.append(content)
                        lines.append("```")
                        lines.append("")
                    except Exception:
                        pass
                    break

    lines.append("---")
    lines.append("")
    return lines


def _load_integration_graph() -> dict:
    """Load auto-detected integration graph if exists."""
    if INTEGRATION_GRAPH.exists():
        try:
            return json.loads(INTEGRATION_GRAPH.read_text())
        except Exception:
            pass
    return {}


def expand_project_names(seed_names: list, int_graph: dict) -> list:
    """Expand seed projects to all connected via integration graph AND KNOWN_INTEGRATIONS."""
    result = list(seed_names)
    seen = set(seed_names)

    queue = list(seed_names)
    while queue:
        name = queue.pop(0)
        # From auto-detected graph
        g = int_graph.get(name, {})
        neighbors = (
            [c["target"] for c in g.get("calls", [])] +
            [c["source"] for c in g.get("called_by", [])]
        )
        # From manual KNOWN_INTEGRATIONS
        for link in KNOWN_INTEGRATIONS.get(name, []):
            neighbors.append(link["target"])
        # Reverse: who calls this project manually
        for src, links in KNOWN_INTEGRATIONS.items():
            if any(l["target"] == name for l in links):
                neighbors.append(src)

        for neighbor in neighbors:
            if neighbor not in seen:
                seen.add(neighbor)
                result.append(neighbor)
                queue.append(neighbor)

    return result


def gen_map_for_prompt(project_names: list, projects: dict, local_catalog: dict = None) -> str:
    """Generate rich context map for Claude prompt — maximally informative."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    int_graph = _load_integration_graph()

    # Auto-expand: find all connected projects from integration graph
    expanded = expand_project_names(project_names, int_graph)
    added = [n for n in expanded if n not in project_names]

    lines = [
        "# 🗺 Project Map (контекст для Claude)",
        f"*Згенеровано: {now}*",
        f"*Seed: {', '.join(project_names)}*",
    ]
    if added:
        lines.append(f"*Auto-expanded: {', '.join(added)}*")
    lines += ["", "> Вставляй цей файл на початок промпту — Claude одразу отримає повний контекст.", ""]

    # Use expanded list for everything below
    project_names = expanded

    # ── Integration Map ───────────────────────────────────────────────────────
    # Collect all connections: within map + external
    by_pair_internal = defaultdict(list)   # (src, tgt) → [eps]  both in project_names
    by_pair_external = defaultdict(list)   # (src, tgt) → [eps]  tgt outside project_names

    for name in project_names:
        g = int_graph.get(name, {})
        for c in g.get("calls", []):
            ep = c.get("endpoint", "")
            tgt = c["target"]
            if tgt in project_names:
                by_pair_internal[(name, tgt)].append(ep)
            else:
                by_pair_external[(name, tgt)].append(ep)
        for c in g.get("called_by", []):
            src = c["source"]
            if src not in project_names:
                by_pair_external[(src, name)].append(c.get("endpoint", ""))
        # KNOWN_INTEGRATIONS (manual)
        for link in KNOWN_INTEGRATIONS.get(name, []):
            tgt = link["target"]
            label = link.get("data", link.get("type", ""))
            if tgt in project_names:
                by_pair_internal[(name, tgt)].append(label)
            else:
                by_pair_external[(name, tgt)].append(label)
        # Reverse manual links
        for src, links in KNOWN_INTEGRATIONS.items():
            for link in links:
                if link["target"] == name:
                    label = link.get("data", link.get("type", ""))
                    if src in project_names:
                        by_pair_internal[(src, name)].append(label)
                    else:
                        by_pair_external[(src, name)].append(label)

    lines.append("## 🔗 Integration Map")
    lines.append("")

    if by_pair_internal or by_pair_external:
        lines.append("```")
        for name in project_names:
            out_int = [(tgt, eps) for (src, tgt), eps in by_pair_internal.items() if src == name]
            inc_int = [(src, eps) for (src, tgt), eps in by_pair_internal.items() if tgt == name]
            out_ext = [(tgt, eps) for (src, tgt), eps in by_pair_external.items() if src == name]
            inc_ext = [(src, eps) for (src, tgt), eps in by_pair_external.items() if tgt == name]
            if not any([out_int, inc_int, out_ext, inc_ext]):
                lines.append(f"  {name}  (no auto-detected connections)")
                continue
            lines.append(f"  {name}")
            for tgt, eps in sorted(out_int):
                unique = sorted(set(e for e in eps if e))
                eps_str = (", ".join(unique[:3]) + (f" +{len(unique)-3}" if len(unique) > 3 else "")) or "?"
                lines.append(f"    ──[{eps_str}]──► {tgt}")
            for src, eps in sorted(inc_int):
                unique = sorted(set(e for e in eps if e))
                eps_str = (", ".join(unique[:3]) + (f" +{len(unique)-3}" if len(unique) > 3 else "")) or "?"
                lines.append(f"    ◄──[{eps_str}]── {src}")
            for tgt, eps in sorted(out_ext):
                unique = sorted(set(e for e in eps if e))
                eps_str = (", ".join(unique[:2]) + (f" +{len(unique)-2}" if len(unique) > 2 else "")) or "?"
                lines.append(f"    ──[{eps_str}]──► 🌐 {tgt}")
            for src, eps in sorted(inc_ext):
                unique = sorted(set(e for e in eps if e))
                eps_str = (", ".join(unique[:2]) + (f" +{len(unique)-2}" if len(unique) > 2 else "")) or "?"
                lines.append(f"    ◄──[{eps_str}]── 🌐 {src}")
        lines.append("```")
    else:
        lines.append("*Auto-detection found no connections for these projects.*")
        lines.append("*Run `cataloger --detect-integrations` to rebuild the graph,*")
        lines.append("*or add manual links to `KNOWN_INTEGRATIONS` in `gitlab_wiki.py`.*")

    lines.append("")


    for name in project_names:
        p = projects.get(name)
        catalog_local = (local_catalog or {}).get(name, {})

        # LOCAL ONLY
        if not p and name in LOCAL_ONLY_PROJECTS:
            local_path = Path(LOCAL_ONLY_PROJECTS[name])
            git    = git_info(local_path) if (local_path / ".git").exists() else {}
            tech   = detect_tech(local_path)
            readme = get_readme(local_path)
            docker = parse_docker_compose(local_path)
            status = infer_status(git) if git else "📁 local-only"
            lines += _render_project_block(
                name=name, git=git, tech=tech, readme=readme,
                status=f"{status} (local)", path=str(local_path),
                gitlab_url="", docker=docker,
                integrations=[], consumed_by=[],
                local_files={}, project_names=project_names,
                catalog_local=catalog_local,
            )
            continue

        # NOT FOUND
        if not p:
            lines.append(f"## ❌ {name}")
            lines.append(f"Не знайдений. Додай: `python3 gitlab_wiki.py --add-local {name}`")
            lines.append("")
            continue

        # GITLAB PROJECT
        lines += _render_project_block(
            name=name, git=p["git"], tech=p["tech"],
            readme=p.get("readme"), status=p["status"],
            path=p.get("local_path", ""), gitlab_url=p.get("gitlab_url", ""),
            docker=p.get("docker", {}),
            integrations=p.get("integrations", []),
            consumed_by=p.get("consumed_by", []),
            local_files=p.get("local_files", {}),
            project_names=project_names,
            catalog_local=catalog_local,
        )

    return "\n".join(lines)


# ═══════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(description="GitLab Production Wiki Generator")
    parser.add_argument("--map", nargs="+", metavar="PROJECT", help="Generate compact map for Claude prompt")
    parser.add_argument("--add-local", nargs="+", metavar="NAME_OR_PATH",
                        help="Add local-only project(s) to LOCAL_ONLY_PROJECTS. "
                             "Accepts project name (searches in ~/VisualStudio) or full path.")
    parser.add_argument("--add-url", type=str, metavar="URL",
                        help="Clone a new project by Git URL into gitlab-prod and generate wiki")
    parser.add_argument("--detect-integrations", action="store_true",
                        help="Scan ALL projects and rebuild integration_graph.json")
    args = parser.parse_args()

    # --add-local: додаємо проекти в LOCAL_ONLY_PROJECTS прямо у файл
    if args.add_local:
        script_path = Path(__file__)
        script_text = script_path.read_text()

        added, skipped = [], []
        for entry in args.add_local:
            p = Path(entry)
            if not p.is_absolute():
                p = VISUALSTUDIO_DIR / entry
            name = p.name
            if not p.exists():
                print(f"  ⚠️  {name}: path не існує ({p}), пропускаємо")
                skipped.append(name)
                continue
            if f'"{name}"' in script_text:
                print(f"  ℹ️  {name}: вже є в LOCAL_ONLY_PROJECTS")
                skipped.append(name)
                continue
            # Вставляємо перед закриваючою дужкою блоку LOCAL_ONLY_PROJECTS
            new_line = f'    "{name}": "{p}",\n'
            script_text = re.sub(
                r'(LOCAL_ONLY_PROJECTS\s*=\s*\{[^}]*?)(\})',
                lambda m: m.group(1) + new_line + m.group(2),
                script_text, count=1, flags=re.DOTALL
            )
            added.append(name)

        if added:
            script_path.write_text(script_text)
            print(f"✅ Додано до LOCAL_ONLY_PROJECTS: {', '.join(added)}")
        if not added and not skipped:
            print("Нічого не додано.")
        return

    # --detect-integrations: rebuild integration graph across ALL projects
    if args.detect_integrations:
        import subprocess, sys
        detector_script = CATALOGER_DIR / "integration_detector.py"
        out = INTEGRATION_GRAPH
        out.parent.mkdir(parents=True, exist_ok=True)
        print("🔍 Scanning all projects for integrations...")
        r = subprocess.run(
            [sys.executable, str(detector_script), "--save", str(out)],
            capture_output=False
        )
        if r.returncode == 0:
            print(f"✅ Integration graph saved: {out}")
        return

    if args.add_url:
        url = args.add_url
        print(f"🔗 Adding project by URL: {url}")
        
        project_name = url.split("/")[-1]
        if project_name.endswith(".git"):
            project_name = project_name[:-4]
            
        target_dir = GITLAB_DIR / project_name
        
        if target_dir.exists():
            print(f"⚠️  Directory {target_dir} already exists. Attempting git pull instead.")
            subprocess.run(["git", "-C", str(target_dir), "pull"])
        else:
            print(f"⬇️  Cloning {project_name} into {GITLAB_DIR}...")
            res = subprocess.run(["git", "clone", url, str(target_dir)])
            if res.returncode != 0:
                print(f"❌ Failed to clone {url}")
                return
        print(f"✅ Successfully added {project_name}. Proceeding to update wiki...\n")

    # Load local VisualStudio catalog
    local_catalog = load_local_catalog()
    matched = sum(1 for d in GITLAB_DIR.iterdir()
                  if d.is_dir() and GITLAB_TO_LOCAL.get(d.name, d.name) in local_catalog)
    print(f"📚 Local catalog: {len(local_catalog)} projects, {matched} will be enriched")

    # Scan all gitlab projects
    projects = {}
    project_dirs = [d for d in GITLAB_DIR.iterdir()
                    if d.is_dir() and not d.name.startswith(".") and d.name != "wiki"]

    print(f"🔍 Scanning {len(project_dirs)} gitlab projects...")
    for d in sorted(project_dirs):
        if not (d / ".git").exists():
            continue
        local_name = GITLAB_TO_LOCAL.get(d.name, d.name)
        has_local = "➕ local" if local_name in local_catalog else ""
        print(f"  → {d.name} {has_local}")
        projects[d.name] = scan_project(d, local_catalog)

    if args.map:
        result = gen_map_for_prompt(args.map, projects, local_catalog)
        # Зберігаємо в project_cataloger/wiki/ — єдине місце для всіх карт
        map_dir = Path("/Users/andriy/VisualStudio/project_cataloger/wiki")
        map_dir.mkdir(parents=True, exist_ok=True)
        n = 1
        while (map_dir / f"_prompt_map_{n}.md").exists():
            n += 1
        map_file = map_dir / f"_prompt_map_{n}.md"
        map_file.write_text(result)
        print(result)
        print(f"\n✅ Saved to: {map_file}")
        return

    # Generate full wiki
    WIKI_DIR.mkdir(exist_ok=True)
    proj_dir = WIKI_DIR / "projects"
    proj_dir.mkdir(exist_ok=True)

    print("\n📝 Generating wiki...")
    for name, p in projects.items():
        gen_project_page(p, proj_dir)

    gen_index(projects, WIKI_DIR)
    gen_integration_map(projects, WIKI_DIR)
    gen_status(projects, WIKI_DIR)

    print(f"\n✅ Wiki generated: {WIKI_DIR}/INDEX.md")
    print(f"   Projects: {len(projects)}")
    print(f"   Integration Map: {WIKI_DIR}/INTEGRATION_MAP.md")
    print(f"\n💡 Tip: python3 gitlab_wiki.py --map ai-trading-strategy-advisor base-states profitradar-api")


if __name__ == "__main__":
    main()
