# llm-training-data-miner

**Категория:** 🧠 [LLM & AI Training](../categories/llm_ai_training.md)
**Статус:** 🟢 active
**Путь:** `/Users/andriy/VisualStudio/llm-training-data-miner`

## 📊 Git

- **Branch:** `strat-factory`
- **Коммитов:** 314
- **Последний:** 2026-03-09
- **Сообщение:** fix(factory): make bruteforce config compatible with engine strategy expansion
- **За 30 дней:** 28 коммитов

### Последние коммиты

- `2026-03-09` fix(factory): make bruteforce config compatible with engine strategy expansion
- `2026-03-06` feat(factory): implement Phase 4 quality filter
- `2026-03-05` feat(factory): implement Phase 3 bruteforce submission
- `2026-03-04` feat(factory): implement Phase 2 config generation
- `2026-03-04` feat(factory): add Phase 1 pattern discovery based on .ideas/pattern-recognition

## 📁 Files (13683 indexed)

### Docs (279 files, 4.2 MB)

| File | Size | Modified |
|------|------|----------|
| `temporary/States.txt` | 2 KB | 2026-02-21 |
| `DOCUMENTATION/task3_adviser_navigation_architecture.md` | 13 KB | 2026-02-19 |
| `DOCUMENTATION/task1_context_expansion_report.md` | 30 KB | 2026-02-19 |
| `DOCUMENTATION/task2_tier_validity_report.md` | 17 KB | 2026-02-19 |
| `DOCUMENTATION/task3_schema_assembly.md` | 7 KB | 2026-02-19 |
| `temporary/task3_schema_assembly.md` | 7 KB | 2026-02-19 |
| `DOCUMENTATION/task2_tier_validity.md` | 5 KB | 2026-02-19 |
| `temporary/task2_tier_validity.md` | 5 KB | 2026-02-19 |
| `DOCUMENTATION/task1_context_expansion.md` | 5 KB | 2026-02-19 |
| `temporary/task1_context_expansion.md` | 5 KB | 2026-02-19 |
| `docs/session_log_2026_02_18.md` | 3 KB | 2026-02-18 |
| `bruteforce_analysis/DATA_TRACING_COMPLETE.md` | 17 KB | 2026-02-03 |
| `bruteforce_analysis/DATA_TRACING_CHECKPOINT_2.md` | 1 KB | 2026-02-03 |
| `bruteforce_analysis/DATA_TRACING_CHECKPOINT_1.md` | 1 KB | 2026-02-03 |
| `trading_ai_dashboard.html` | 45 KB | 2026-02-02 |

### Code (319 files, 2.8 MB)

| File | Size | Modified |
|------|------|----------|
| `orchestrator/semantic_search.py` | 4 KB | 2026-02-14 |
| `orchestrator/orchestrator.py` | 51 KB | 2026-02-14 |
| `model-testing-app/backend/main.py` | 11 KB | 2026-02-14 |
| `model-testing-app/frontend/vite.config.ts` | 194 B | 2026-02-14 |
| `filter_by_intervals.py` | 6 KB | 2026-02-05 |
| `analyze_unique_experiments.py` | 9 KB | 2026-02-05 |
| `bruteforce_analysis/scripts/config.py` | 4 KB | 2026-02-03 |
| `bruteforce_analysis/run_bruteforce_analysis.py` | 2 KB | 2026-02-03 |
| `verify_model_v5_accuracy.py` | 5 KB | 2026-02-02 |
| `validate_indicators_dataset.py` | 11 KB | 2026-02-02 |
| `unified_generator_production_v7_3.py` | 62 KB | 2026-02-02 |
| `trading_logic_parser.py` | 30 KB | 2026-02-02 |
| `test_settings_extraction.py` | 488 B | 2026-02-02 |
| `test_selection_logic.py` | 4 KB | 2026-02-02 |
| `test_quality_scorer.py` | 7 KB | 2026-02-02 |

### Config (8088 files, 75.4 MB)

| File | Size | Modified |
|------|------|----------|
| `test_data/summary.json` | 115 KB | 2026-02-23 |
| `test_data/bruteforce_12278/config.json` | 2 KB | 2026-02-23 |
| `test_data/bruteforce_12247/config.json` | 1 KB | 2026-02-23 |
| `test_data/bruteforce_12276/config.json` | 1 KB | 2026-02-23 |
| `test_data/bruteforce_12271/config.json` | 1 KB | 2026-02-23 |
| `test_data/bruteforce_12270/config.json` | 1 KB | 2026-02-23 |
| `test_data/bruteforce_12248/config.json` | 1 KB | 2026-02-23 |
| `test_data/bruteforce_12277/config.json` | 1 KB | 2026-02-23 |
| `test_data/bruteforce_12279/config.json` | 2 KB | 2026-02-23 |
| `test_data/bruteforce_12246/config.json` | 1 KB | 2026-02-23 |
| `test_data/bruteforce_12267/config.json` | 1 KB | 2026-02-23 |
| `test_data/bruteforce_12269/config.json` | 1 KB | 2026-02-23 |
| `test_data/bruteforce_12268/config.json` | 1 KB | 2026-02-23 |
| `test_data/bruteforce_12272/config.json` | 1 KB | 2026-02-23 |
| `test_data/bruteforce_12281/config.json` | 2 KB | 2026-02-23 |

### Data (4997 files, 840.3 MB)

## 📝 README

```
# LLM Training Data Miner

Generate training data for AI trading advisor from bruteforce backtesting results.

## Quick Start

```bash
cd /Users/andriy/VisualStudio/llm-training-data-miner
python run_pipeline.py
```

## Manual Commands

```bash
# Bruteforce API
cd bruteforce_api
python bruteforce_api_client.py --list              # List all bruteforces
python bruteforce_api_client.py --status 787        # Check status
python bruteforce_api_client.py --download 787      # Download results
python bruteforce_api_client.py --config configs/01_RSI_period_sensitivity_BTC.json  # Run config

# Analyzer Bot
cd analyzer_bot
python main.py --brute-id 787                       # Analyze single
python main.py --brute-ids 783,785,786              # Analyze multiple
python main.py --brute-id 787 --dry-run             # Validate only
```

## Directory Structure

```
llm-training-data-miner/
├── run_pipeline.py              # 🚀 Main entry point
├── bruteforce_api/
│   ├── configs/                 # Bruteforce configurations
│   └── bruteforce_api_client.py # API client
├── analyzer_bot/                # Data processing pipeline
├── test_data/                   # Downloaded bruteforce results
├── training_data/               # Generated training examples
│   ├── tier_1/                  # Best quality (weight 1.0)
│   ├── tier_2/                  # Good quality (weight 0.7)
│   ├── tier_3/                  # Educational (weight 0.3)
│   └── tier_4/                  # Excluded (weight 0.0)
└──
```
