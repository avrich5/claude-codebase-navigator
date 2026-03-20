# llm-training-data-miner-strat-factory

**Категория:** 📊 [Trading Strategies](../categories/trading_strategies.md)
**Статус:** 🟢 active
**Путь:** `/Users/andriy/VisualStudio/llm-training-data-miner-strat-factory`

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

## 🛠 Tech Stack

- **Languages:** Python
- **Frameworks:** FastAPI, NumPy, OpenAI API, Pandas
- **Tools:** Docker Compose, Make, pip

## 📁 Files (692 indexed)

### Docs (123 files, 1.5 MB)

| File | Size | Modified |
|------|------|----------|
| `training_data/README.md` | 10 KB | 2026-03-05 |
| `src/llm_training_data_miner/analyzers/v7/README.md` | 2 KB | 2026-03-05 |
| `requirements.txt` | 3 KB | 2026-03-05 |
| `requirements-dev.txt` | 1 KB | 2026-03-05 |
| `profit-radar-guide/visual_constructor_guide.html` | 35 KB | 2026-03-05 |
| `profit-radar-guide/ta_only_guide.html` | 18 KB | 2026-03-05 |
| `profit-radar-guide/quick_start_main.html` | 15 KB | 2026-03-05 |
| `profit-radar-guide/platform_navigation_guide.html` | 16 KB | 2026-03-05 |
| `profit-radar-guide/interface_pages_guide.html` | 27 KB | 2026-03-05 |
| `profit-radar-guide/index.html` | 19 KB | 2026-03-05 |
| `profit-radar-guide/guide-params.html` | 43 KB | 2026-03-05 |
| `profit-radar-guide/guide-optima.html` | 40 KB | 2026-03-05 |
| `profit-radar-guide/grid_only_guide.html` | 16 KB | 2026-03-05 |
| `profit-radar-guide/grid_configuration_guide.html` | 30 KB | 2026-03-05 |
| `profit-radar-guide/from_settings_guide.html` | 20 KB | 2026-03-05 |

### Config (195 files, 2.7 MB)

| File | Size | Modified |
|------|------|----------|
| `postman/LLM_Training_Data_Miner_API.postman_collection.json` | 93 KB | 2026-03-10 |
| `training_data/metadata_index.json` | 31 KB | 2026-03-05 |
| `pytest.ini` | 676 B | 2026-03-05 |
| `pyproject.toml` | 1 KB | 2026-03-05 |
| `pattern_94.json` | 0 B | 2026-03-05 |
| `pattern_1.json` | 0 B | 2026-03-05 |
| `helm/llm-training-data-miner/templates/scripts-configmap.yaml` | 3 KB | 2026-03-05 |
| `helm/llm-training-data-miner/templates/patterns-configmap.yaml` | 426 B | 2026-03-05 |
| `helm/llm-training-data-miner/templates/migrations-configmap.yaml` | 605 B | 2026-03-05 |
| `helm/llm-training-data-miner/templates/init-scripts-configmap.yaml` | 3 KB | 2026-03-05 |
| `helm/llm-training-data-miner/templates/configmap.yaml` | 6 KB | 2026-03-05 |
| `frontend/tsconfig.node.json` | 214 B | 2026-03-05 |
| `frontend/tsconfig.json` | 732 B | 2026-03-05 |
| `frontend/package.json` | 1 KB | 2026-03-05 |
| `frontend/package-lock.json` | 145 KB | 2026-03-05 |

### Code (374 files, 3.0 MB)

| File | Size | Modified |
|------|------|----------|
| `src/llm_training_data_miner/factory/config_generation/signal_mapping.py` | 8 KB | 2026-03-10 |
| `src/llm_training_data_miner/factory/config_generation/config_builder.py` | 6 KB | 2026-03-10 |
| `tests/unit/test_recommended_config_extractor.py` | 3 KB | 2026-03-05 |
| `tests/unit/test_config_hash.py` | 5 KB | 2026-03-05 |
| `tests/unit/test_config_generation.py` | 4 KB | 2026-03-05 |
| `tests/conftest.py` | 2 KB | 2026-03-05 |
| `tests/__init__.py` | 48 B | 2026-03-05 |
| `src/llm_training_data_miner/utils/config_hash.py` | 2 KB | 2026-03-05 |
| `src/llm_training_data_miner/oos_backtest/config_builder.py` | 4 KB | 2026-03-05 |
| `src/llm_training_data_miner/migrations/025_factory_generated_configs.sql` | 1 KB | 2026-03-05 |
| `src/llm_training_data_miner/migrations/009_asset_interval_configs.sql` | 4 KB | 2026-03-05 |
| `src/llm_training_data_miner/factory/pattern_discovery/config.py` | 2 KB | 2026-03-05 |
| `src/llm_training_data_miner/factory/config_generation/config_validator.py` | 2 KB | 2026-03-05 |
| `src/llm_training_data_miner/export/recommended_config_extractor.py` | 6 KB | 2026-03-05 |
| `src/llm_training_data_miner/core/metrics_wrapper.py` | 11 KB | 2026-03-05 |

## 📝 README

```
# LLM Training Data Miner

Generate training data for AI trading advisor from bruteforce backtesting results.

## Quick Start

### Prerequisites

- Python 3.13 or higher
- Virtual environment (recommended)
- For K8S mode: Kubernetes cluster access and `kubectl` configured

### Setup

```bash
# Clone repository
cd llm-training-data-miner

# Create virtual environment
python3.13 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your configuration (see Environment Configuration below)

# For K8S mode (local dev): Start port-forward in separate terminal
# kubectl port-forward service/backtest 8080:8080 -n trading

# Run pipeline
python run_pipeline.py
```

### Environment Setup

**K8S Mode (Local Development):**

```bash
# 1. Start port-forward (keep running in separate terminal)
kubectl port-forward service/backtest 8080:8080 -n trading

# 2. Configure .env
API_ACCESS_MODE=k8s
K8S_PORT_FORWARD_PORT=8080
```

**Cookie Mode:**

```bash
# Configure .env
API_ACCESS_MODE=cookie
PROFITRADAR_COOKIE=shark=your-cookie-value
```

## Manual Commands

```bash
# Bruteforce API
cd bruteforce_api
python bruteforce_api_client.py --list              # List all bruteforces
python bruteforce_api_client.py --status 787        # Check status
python bruteforce_api_client.py --download 787      # Download results
python bruteforce_api_client.py --config config
```
