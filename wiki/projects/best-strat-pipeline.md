# best-strat-pipeline

**Категория:** 📊 [Trading Strategies](../categories/trading_strategies.md)
**Статус:** 🟢 active
**Путь:** `/Users/andriy/VisualStudio/best-strat-pipeline`

## 📊 Git

- **Branch:** `claude/wizardly-curran`
- **Коммитов:** 3
- **Последний:** 2026-03-01
- **Сообщение:** before how-to-bekieve
- **За 30 дней:** 2 коммитов

### Последние коммиты

- `2026-03-01` before how-to-bekieve
- `2026-02-28` before backtest implementing
- `2026-02-06` Initial commit: Best Strat Pipeline setup with interactive Streamlit app

## 🛠 Tech Stack

- **Languages:** Python
- **Frameworks:** NumPy, Pandas, Plotly, Streamlit
- **Tools:** pip

## 📁 Files (15336 indexed)

### Docs (40 files, 0.5 MB)

| File | Size | Modified |
|------|------|----------|
| `docs/Mechanism_Signal_Mapper_TZ.md` | 46 KB | 2026-03-03 |
| `docs/INCREMENTAL_UPDATER_GUIDE.md` | 15 KB | 2026-03-01 |
| `docs/INCREMENTAL_UPDATER/README.md` | 7 KB | 2026-03-01 |
| `docs/WORKBENCH_API_SPEC.md` | 11 KB | 2026-03-01 |
| `docs/OPERATOR_WORKBENCH_SPEC.md` | 19 KB | 2026-03-01 |
| `requirements.txt` | 69 B | 2026-03-01 |
| `docs/EXPERIMENT_RESULT_PROTOCOL.md` | 7 KB | 2026-03-01 |
| `docs/ENRICHED_BENCHMARK_SCHEMA.md` | 7 KB | 2026-03-01 |
| `docs/Best-Strat Pipeline — Complete Documentation.md` | 41 KB | 2026-03-01 |
| `docs/metrics_audit.md` | 13 KB | 2026-03-01 |
| `.claude/worktrees/wizardly-curran/requirements.txt` | 55 B | 2026-03-01 |
| `.claude/worktrees/wizardly-curran/README.md` | 24 KB | 2026-03-01 |
| `docs/TASK_backtest_confidence.md` | 32 KB | 2026-03-01 |
| `README.md` | 24 KB | 2026-03-01 |
| `docs/TASK_strategy_analyzer.md` | 26 KB | 2026-02-28 |

### Config (9425 files, 35.9 MB)

| File | Size | Modified |
|------|------|----------|
| `benchmarks/bruteforce_775_benchmark.json` | 11 KB | 2026-03-01 |
| `benchmarks/bruteforce_581_benchmark.json` | 9 KB | 2026-03-01 |
| `benchmarks/bruteforce_11480_benchmark.json` | 9 KB | 2026-03-01 |
| `benchmarks/bruteforce_11636_benchmark.json` | 13 KB | 2026-03-01 |
| `benchmarks/bruteforce_12101_benchmark.json` | 11 KB | 2026-03-01 |
| `benchmarks/bruteforce_565_benchmark.json` | 8 KB | 2026-03-01 |
| `benchmarks/bruteforce_1443_benchmark.json` | 9 KB | 2026-03-01 |
| `benchmarks/bruteforce_11432_benchmark.json` | 9 KB | 2026-03-01 |
| `benchmarks/bruteforce_1190_benchmark.json` | 13 KB | 2026-03-01 |
| `benchmarks/bruteforce_11873_benchmark.json` | 13 KB | 2026-03-01 |
| `benchmarks/bruteforce_11471_benchmark.json` | 10 KB | 2026-03-01 |
| `benchmarks/bruteforce_10983_benchmark.json` | 13 KB | 2026-03-01 |
| `benchmarks/bruteforce_11629_benchmark.json` | 9 KB | 2026-03-01 |
| `benchmarks/bruteforce_1449_benchmark.json` | 11 KB | 2026-03-01 |
| `benchmarks/bruteforce_11921_benchmark.json` | 8 KB | 2026-03-01 |

### Code (94 files, 1.2 MB)

| File | Size | Modified |
|------|------|----------|
| `src/incremental_updater.py` | 29 KB | 2026-03-01 |
| `scripts/demo_incremental_updater.py` | 5 KB | 2026-03-01 |
| `scripts/migrate_metadata_csv.py` | 4 KB | 2026-03-01 |
| `tests/test_incremental_updater.py` | 12 KB | 2026-03-01 |
| `src/models_v2.py` | 9 KB | 2026-03-01 |
| `scripts/backtest_confidence.py` | 19 KB | 2026-03-01 |
| `scripts/regime_analyzer.py` | 11 KB | 2026-03-01 |
| `scripts/strategy_analyzer.py` | 55 KB | 2026-03-01 |
| `.claude/worktrees/wizardly-curran/scripts/generate_backtest_configs.py` | 9 KB | 2026-03-01 |
| `scripts/run_backtests.py` | 8 KB | 2026-02-28 |
| `scripts/run_backtests_parallel.py` | 13 KB | 2026-02-28 |
| `scripts/tier_s_backtest_prep.py` | 29 KB | 2026-02-28 |
| `.claude/worktrees/competent-yonath/src/ui/pages/2_Generate_Configs.py` | 2 KB | 2026-02-28 |
| `.claude/worktrees/competent-yonath/src/ui/app.py` | 848 B | 2026-02-28 |
| `.claude/worktrees/competent-yonath/src/core/analysis/scripts/config.py` | 4 KB | 2026-02-28 |

### Data (5777 files, 312.4 MB)

| File | Size | Modified |
|------|------|----------|
| `data/templates_metadata_incremental.csv` | 513 KB | 2026-03-01 |
| `data/templates_metadata.csv` | 484 KB | 2026-03-01 |
| `data/templates_metadata_1.csv` | 370 KB | 2026-03-01 |
| `data/templates_metadata_recent_727.csv` | 286 KB | 2026-03-01 |

## 📝 README

```
# Best Strat Pipeline

> **Цель проекта**: из десятков тысяч вариантов grid-стратегий отобрать те, которые стабильно работают на реальных рыночных условиях, а не только на исторических данных, которые использовались при оптимизации.

---

## Содержание

1. [Концептуальная основа](#1-концептуальная-основа)
   - Что такое bruteforce-эксперимент
   - Что такое KPI и fitness
   - In-Sample vs Out-of-Sample (OOS)
   - Проблема overfitting
2. [Тиринг стратегий (Tier S/A/B)](#2-тиринг-стратегий)
3. [Backtest-валидация](#3-backtest-валидация)
   - Что такое `recent` и `oos2023`
   - Почему количество конфигов не совпадает с количеством стратегий
4. [Composite Score](#4-composite-score)
5. [Архитектура пайплайна](#5-архитектура-пайплайна)
6. [Скрипты и CLI](#6-скрипты-и-cli)
7. [Структура данных](#7-структура-данных)
8. [Текущий статус проекта](#8-текущий-статус-проекта)
9. [Дорожная карта](#9-дорожная-карта)

---

## 1. Концептуальная основа

### Что такое bruteforce-эксперимент

Bruteforce-эксперимент — это полный перебор параметров grid-стратегии на заданных
временных интервалах и ассете. Один эксперимент — это папка вида
`data/bruteforces/bruteforce_1239/`, содержащая:

- `config.json` — описание пространства параметров (индикаторы, сетка, стоп-лоссы и т.д.)
- `kpi.csv` — результаты каждой комбинации параметров (`settings_id`) на каждом интервале
- `settings.tsv` — конкретные значения параметров для каждого `settings_id`

В одном эксперименте может быть сотни или тысячи `settings_
```
