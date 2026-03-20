# pattern_config_gen

**Категория:** 🔮 [Predictors & Models](../categories/predictors_models.md)
**Статус:** 📁 no-git
**Путь:** `/Users/andriy/VisualStudio/pattern_config_gen`

## 🛠 Tech Stack

- **Languages:** Python
- **Tools:** pip

## 📁 Files (46 indexed)

### Docs (13 files, 0.1 MB)

| File | Size | Modified |
|------|------|----------|
| `docs/INDEX.md` | 6 KB | 2026-01-28 |
| `docs/QUICKSTART.md` | 7 KB | 2026-01-28 |
| `docs/CHANGELOG.md` | 5 KB | 2026-01-28 |
| `README.md` | 7 KB | 2026-01-28 |
| `docs/API.md` | 14 KB | 2026-01-28 |
| `docs/ARCHITECTURE.md` | 14 KB | 2026-01-28 |
| `docs/GUIDE.md` | 10 KB | 2026-01-28 |
| `step2_dsl_to_bruteforce/prompts/hypothesis_to_config.txt` | 1 KB | 2026-01-28 |
| `requirements.txt` | 223 B | 2026-01-28 |

### Config (6 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `bruteforce_cookie.json` | 89 B | 2026-01-28 |

### Code (27 files, 0.1 MB)

| File | Size | Modified |
|------|------|----------|
| `tests/debug_api.py` | 798 B | 2026-01-28 |
| `common/bruteforce_client.py` | 14 KB | 2026-01-28 |
| `tests/test_phase_d.py` | 668 B | 2026-01-28 |
| `common/anthropic_client.py` | 4 KB | 2026-01-28 |
| `step2_dsl_to_bruteforce/hypothesis_agent.py` | 2 KB | 2026-01-28 |
| `step3_failed_analysis/analyze_failures.py` | 11 KB | 2026-01-28 |
| `step2_dsl_to_bruteforce/testing_workflow.py` | 7 KB | 2026-01-28 |
| `step2_dsl_to_bruteforce/generate_configs.py` | 9 KB | 2026-01-28 |
| `step1_hypothesis_to_dsl/curate_dsl_corpus.py` | 7 KB | 2026-01-28 |
| `step3_failed_analysis/display_utils.py` | 9 KB | 2026-01-28 |
| `step3_failed_analysis/failure_analyzer.py` | 4 KB | 2026-01-28 |
| `step3_failed_analysis/failed_loader.py` | 5 KB | 2026-01-28 |
| `step2_dsl_to_bruteforce/hypothesis_manager.py` | 3 KB | 2026-01-28 |
| `step2_dsl_to_bruteforce/display_utils.py` | 7 KB | 2026-01-28 |
| `step2_dsl_to_bruteforce/config_builder.py` | 2 KB | 2026-01-28 |

## 📝 README

```
# Pattern Config Generator - Project Structure

Automated pipeline for generating and testing algorithmic trading strategies.

## Architecture

```
pattern_config_gen/
├── common/                          # Shared utilities
│   ├── path_config.py              # Interactive path setup
│   ├── anthropic_client.py         # Claude API client
│   └── bruteforce_client.py        # ProfitRadar API client
│
├── step1_hypothesis_to_dsl/        # Classification
│   ├── dsl_patterns.py             # Pattern detection
│   ├── dsl_classifier.py           # Classification logic
│   └── curate_dsl_corpus.py        # Main classifier script
│
├── step2_dsl_to_bruteforce/        # Config generation
│   ├── prompts/
│   │   └── hypothesis_to_config.txt
│   ├── config_builder.py           # Bruteforce config builder
│   ├── hypothesis_agent.py         # AI transformation
│   ├── hypothesis_manager.py       # File operations
│   ├── testing_workflow.py         # Test execution
│   ├── display_utils.py            # UI functions
│   └── generate_configs.py         # Main generator script
│
└── step3_failed_analysis/          # Failure analysis
    ├── prompts/
    │   └── failure_analysis.txt
    ├── failed_loader.py            # Failed hypothesis loader
    ├── failure_analyzer.py         # AI failure analysis
    ├── display_utils.py            # UI functions
    └── analyze_failures.py         # Main analyzer script
```

## Pipeline Flow

### Step 1: Hypothesis Classification
```bash
python ste
```
