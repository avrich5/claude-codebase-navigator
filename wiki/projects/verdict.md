# verdict

**Категория:** 📦 [Uncategorized](../categories/uncategorized.md)
**Статус:** 🟢 active
**Путь:** `/Users/andriy/VisualStudio/verdict`

## 📊 Git

- **Branch:** `shi_group`
- **Коммитов:** 22
- **Последний:** 2026-03-13
- **Сообщение:** feat: bundle SemanticSearcher + embeddings into repo, fix import path + config
- **За 30 дней:** 22 коммитов

### Последние коммиты

- `2026-03-13` feat: bundle SemanticSearcher + embeddings into repo, fix import path + config
- `2026-03-13` fix: restore FileHandler in run_bot.py; suppress SemanticSearcher WARNING → DEBUG
- `2026-03-13` feat: run_bot.py — PID-file lock + hostname guard (skufs-mac-mini only)
- `2026-03-13` chore: add BACKLOG.md — import assets from unified.json
- `2026-03-13` feat: unsupported instrument reply 'coming soon' + RULES_TEXT fixes

## 🛠 Tech Stack

- **Languages:** Python
- **Frameworks:** Pandas
- **Tools:** pip

## 📁 Files (138 indexed)

### Docs (20 files, 0.2 MB)

| File | Size | Modified |
|------|------|----------|
| `BACKLOG.md` | 408 B | 2026-03-13 |
| `requirements.txt` | 437 B | 2026-03-13 |
| `.claude/worktrees/inspiring-davinci/requirements.txt` | 437 B | 2026-03-13 |
| `.claude/worktrees/inspiring-davinci/docs/implementation_plan.md` | 5 KB | 2026-03-13 |
| `.claude/worktrees/inspiring-davinci/README.md` | 10 KB | 2026-03-13 |
| `docs/AGENT_TASK_verdict_bot_phase1.md` | 18 KB | 2026-03-13 |
| `USER_GUIDE.md` | 13 KB | 2026-03-12 |
| `README.md` | 10 KB | 2026-03-10 |
| `CONTRIBUTING.md` | 3 KB | 2026-03-10 |
| `docs/task.md` | 6 KB | 2026-03-10 |
| `docs/implementation_plan.md` | 5 KB | 2026-03-10 |
| `docs/verdict_signal_import_tz_clarifications.md` | 7 KB | 2026-03-10 |
| `docs/verdict_contextual_signal_detector_architecture.md` | 37 KB | 2026-03-10 |
| `reports/corpus_report.html` | 12 KB | 2026-03-10 |

### Config (5 files, 11.3 MB)

| File | Size | Modified |
|------|------|----------|
| `data/strategy_embeddings.json` | 11.3 MB | 2026-03-13 |
| `config.yaml` | 6 KB | 2026-03-13 |
| `.claude/worktrees/inspiring-davinci/config.yaml` | 5 KB | 2026-03-13 |
| `data/signal_keywords.yaml` | 1 KB | 2026-03-10 |

### Data (4 files, 10.3 MB)

| File | Size | Modified |
|------|------|----------|
| `data/corpus.db` | 9.4 MB | 2026-03-15 |
| `reports/corpus_data.csv` | 849 KB | 2026-03-10 |
| `data/twscrape_accounts.db` | 12 KB | 2026-03-09 |
| `accounts.db` | 12 KB | 2026-03-09 |

### Code (109 files, 0.4 MB)

| File | Size | Modified |
|------|------|----------|
| `scripts/run_bot.py` | 3 KB | 2026-03-13 |
| `migrations/005_bot_members.sql` | 164 B | 2026-03-13 |
| `scripts/group_log.py` | 3 KB | 2026-03-13 |
| `migrations/004_group_messages.sql` | 659 B | 2026-03-13 |
| `.claude/worktrees/inspiring-davinci/src/verdict/verdict_config.py` | 2 KB | 2026-03-13 |
| `.claude/worktrees/inspiring-davinci/src/config_loader.py` | 366 B | 2026-03-13 |
| `scripts/import.py` | 3 KB | 2026-03-10 |
| `tests/test_importer.py` | 4 KB | 2026-03-10 |
| `tests/__init__.py` | 0 B | 2026-03-10 |
| `scripts/verdict.py` | 10 KB | 2026-03-10 |
| `src/verdict/verdict_config.py` | 2 KB | 2026-03-10 |
| `migrations/003_verdict_results.sql` | 1 KB | 2026-03-10 |
| `scripts/manage_channels.py` | 8 KB | 2026-03-10 |
| `scripts/analyze.py` | 3 KB | 2026-03-09 |
| `scripts/manage_twitter_accounts.py` | 4 KB | 2026-03-09 |

## 📝 README

```
# Verdict — Trading Signal Analyzer

> Receives raw trading signals (text or screenshot), reconstructs the market context at the moment of publication, matches against known statistical patterns, and delivers a structured verdict with confidence score and actionable strategy.

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![Claude API](https://img.shields.io/badge/LLM-Claude%20Sonnet%204.6-orange.svg)](https://anthropic.com)
[![SQLite](https://img.shields.io/badge/storage-SQLite-green.svg)](https://sqlite.org/)

---

## What it does

A typical signal arrives as a Telegram message like:

```
BTC SHORT
Entry: 68700
SL: 70400  TP: 67500
```

Verdict answers:
- **What was happening on the market at that moment?** (RSI, Bollinger, MACD, Stochastic — 46 binary signals from real OHLCV)
- **Is this a known pattern?** (matched against pattern DB with lift, win rate, drawdown)
- **Is the author consistent?** (corpus statistics per source)
- **What's the verdict?** — one of: `validated_strategy` / `potential_strategy` / `random_entry` / `red_flags` / `insufficient_data`

---

## Architecture

```
Signal Input (text / screenshot)
        │
        ▼
┌─────────────────────┐
│   Signal Parser     │  regex + Claude Haiku fallback
│   (Layer 1)         │  → instrument, direction, entry, SL, TP
└──────────┬──────────┘
           │
    ┌──────┴───────┬──────────────┐
    ▼              ▼              ▼
┌─────────┐  ┌──────────┐  ┌──────────────
```
