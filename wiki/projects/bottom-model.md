# bottom-model

**Категория:** 🔮 [Predictors & Models](../categories/predictors_models.md)
**Статус:** 🟠 dormant
**Путь:** `/Users/andriy/VisualStudio/bottom-model`

## 📊 Git

- **Branch:** `both-models`
- **Коммитов:** 151
- **Последний:** 2025-06-27
- **Сообщение:** before clean up
- **За 30 дней:** 0 коммитов

### Последние коммиты

- `2025-06-27` before clean up
- `2025-06-22` feat: add dual threshold system documentation
- `2025-06-21` extremum detector & series_analysis & logNATR research
- `2025-06-18` feat: Add support for top model detection
- `2025-06-16` feat: expand parameter limits, add metadata versioning and research tools

## 🛠 Tech Stack

- **Languages:** Python
- **Frameworks:** Flask, NumPy, Pandas
- **Tools:** Docker, pip

## 📁 Files (196 indexed)

### Code (50 files, 1.3 MB)

| File | Size | Modified |
|------|------|----------|
| `calculate_historical_volatility.py` | 12 KB | 2025-10-13 |
| `crypto_clustering_final.py` | 26 KB | 2025-10-13 |
| `crypto_clustering.py` | 11 KB | 2025-10-13 |
| `app.py` | 6 KB | 2025-10-13 |
| `start-script-bottom-model.sh` | 7 KB | 2025-07-16 |
| `cleanup_project.py` | 10 KB | 2025-07-01 |
| `research/market_regime_analysis.py` | 25 KB | 2025-06-25 |
| `extremum_detector/api/app.py` | 65 KB | 2025-06-24 |
| `final_mcp_server.py` | 7 KB | 2025-06-23 |
| `install_mcp.sh` | 6 KB | 2025-06-22 |
| `train.py` | 8 KB | 2025-06-21 |
| `extremum_detector/core/config.py` | 5 KB | 2025-06-21 |
| `update_model_paths.py` | 4 KB | 2025-06-21 |
| `research/btc_regression_analysis.py` | 9 KB | 2025-06-21 |
| `research/btc_cross_validation.py` | 13 KB | 2025-06-21 |

### Docs (22 files, 0.1 MB)

| File | Size | Modified |
|------|------|----------|
| `CLEANUP_SUMMARY.md` | 1 KB | 2025-06-27 |
| `SUCCESSOR_INSTRUCTIONS.md` | 63 KB | 2025-06-27 |
| `README.md` | 14 KB | 2025-06-21 |
| `README-0.md` | 9 KB | 2025-06-20 |
| `requirements.txt` | 374 B | 2025-06-15 |
| `temp_cleanup/archived_20250627_073517/current_requirements.txt` | 5 KB | 2025-05-12 |
| `Description.md` | 5 KB | 2025-05-12 |

### Config (41 files, 2.0 MB)

| File | Size | Modified |
|------|------|----------|
| `.gitlab-ci.yml` | 3 KB | 2025-05-26 |
| `unittest.cfg` | 278 B | 2025-01-23 |
| `.codeclimate.yml` | 63 B | 2025-01-23 |

### Data (83 files, 184.5 MB)

| File | Size | Modified |
|------|------|----------|
| `research/portfolio_allocation_with_volatility.csv` | 2 KB | 2025-10-13 |
| `research/portfolio_with_drawdowns.csv` | 3 KB | 2025-10-13 |
| `research/portfolio_allocation.csv` | 2 KB | 2025-10-13 |
| `research/portfolio_summary.csv` | 1 KB | 2025-10-13 |
| `research/precision_data.csv` | 3 KB | 2025-06-15 |
| `fixtures/btc_features.csv` | 712 KB | 2025-05-12 |
| `fixtures/btc_candles.csv` | 43 KB | 2025-01-23 |

## 📝 README

```
# Bottom Model Trading System

## 🎯 Project Overview

Advanced machine learning system for cryptocurrency market extremum detection with dynamic martingale trading strategies. The system detects market bottoms and tops using ensemble models and applies LogNATR-based risk management for optimal position sizing.

## 🏗️ System Architecture

### Core Components

1. **ML Models**
   - XGBoost classifiers for pattern recognition
   - Conditional ECDF for probability estimation
   - Support for both BOTTOM and TOP detection
   - Cross-asset validation framework

2. **Dynamic Trading System**
   - LogNATR-based series analysis
   - Dynamic martingale coefficient selection (1.3x, 1.5x, 2.0x)
   - ETH/SOL rules validated on BTC data
   - No look-ahead bias protection

3. **Data Pipeline**
   - ClickHouse integration for time series data
   - Real-time and historical processing
   - 80+ technical indicators
   - Automated gap detection and filling

4. **Backtesting Framework**
   - Multiple strategy comparison
   - Risk-adjusted performance metrics
   - Cross-asset validation
   - Research mode for detailed analysis

## 📁 Project Structure

```
bottom-model/
├── extremum_detector/          # Core ML package
│   ├── core/                   # Configuration & features
│   ├── models/                 # Model training & inference
│   ├── api/                    # Flask web interface
│   └── utils/                  # Validation utilities
├── pkl/                        # Model storage (versio
```
