# freqtrade-develop

**Категория:** 📊 [Trading Strategies](../categories/trading_strategies.md)
**Статус:** 📁 no-git
**Путь:** `/Users/andriy/VisualStudio/freqtrade-develop`

## 🛠 Tech Stack

- **Languages:** Python
- **Frameworks:** CCXT, FastAPI, NumPy, Pandas
- **Tools:** Docker, Docker Compose, pip

## 📁 Files (633 indexed)

### Code (472 files, 4.7 MB)

| File | Size | Modified |
|------|------|----------|
| `setup.sh` | 9 KB | 2026-01-22 |
| `tests/pytest.sh` | 110 B | 2026-01-22 |
| `tests/conftest.py` | 104 KB | 2026-01-22 |
| `tests/conftest_hyperopt.py` | 38 KB | 2026-01-22 |
| `tests/test_plotting.py` | 20 KB | 2026-01-22 |
| `tests/test_misc.py` | 8 KB | 2026-01-22 |
| `tests/conftest_trades_usdt.py` | 10 KB | 2026-01-22 |
| `tests/test_configuration.py` | 53 KB | 2026-01-22 |
| `tests/conftest_trades.py` | 14 KB | 2026-01-22 |
| `tests/test_talib.py` | 443 B | 2026-01-22 |
| `tests/test_wallets.py` | 22 KB | 2026-01-22 |
| `tests/__init__.py` | 0 B | 2026-01-22 |
| `tests/test_directory_operations.py` | 4 KB | 2026-01-22 |
| `tests/test_strategy_updater.py` | 7 KB | 2026-01-22 |
| `tests/test_timerange.py` | 3 KB | 2026-01-22 |

### Docs (109 files, 0.9 MB)

| File | Size | Modified |
|------|------|----------|
| `requirements-plot.txt` | 78 B | 2026-01-22 |
| `requirements.txt` | 1 KB | 2026-01-22 |
| `README.md` | 12 KB | 2026-01-22 |
| `requirements-freqai.txt` | 213 B | 2026-01-22 |
| `requirements-dev.txt` | 788 B | 2026-01-22 |
| `CONTRIBUTING.md` | 6 KB | 2026-01-22 |
| `requirements-hyperopt.txt` | 167 B | 2026-01-22 |
| `requirements-freqai-rl.txt` | 492 B | 2026-01-22 |
| `ft_client/requirements.txt` | 84 B | 2026-01-22 |
| `ft_client/README.md` | 304 B | 2026-01-22 |
| `docs/windows_installation.md` | 2 KB | 2026-01-22 |
| `docs/advanced-hyperopt.md` | 10 KB | 2026-01-22 |
| `docs/docker_quickstart.md` | 11 KB | 2026-01-22 |
| `docs/freqai-configuration.md` | 29 KB | 2026-01-22 |
| `docs/strategy-callbacks.md` | 67 KB | 2026-01-22 |

### Config (47 files, 3.8 MB)

| File | Size | Modified |
|------|------|----------|
| `mkdocs.yml` | 4 KB | 2026-01-22 |
| `.pre-commit-config.yaml` | 2 KB | 2026-01-22 |
| `pyproject.toml` | 8 KB | 2026-01-22 |
| `.readthedocs.yml` | 191 B | 2026-01-22 |
| `docker-compose.yml` | 1 KB | 2026-01-22 |
| `ft_client/pyproject.toml` | 1 KB | 2026-01-22 |
| `docker/docker-compose-jupyter.yml` | 393 B | 2026-01-22 |
| `docker/docker-compose-freqai.yml` | 1 KB | 2026-01-22 |
| `tests/config_test_comments.json` | 3 KB | 2026-01-22 |
| `tests/testdata/config.tests.usdt.json` | 2 KB | 2026-01-22 |
| `tests/testdata/config.tests.json` | 2 KB | 2026-01-22 |
| `tests/testdata/testconfigs/test_base_config.json` | 208 B | 2026-01-22 |
| `tests/testdata/testconfigs/testconfig.json` | 102 B | 2026-01-22 |
| `tests/testdata/testconfigs/main_test_config.json` | 2 KB | 2026-01-22 |
| `.devcontainer/devcontainer.json` | 2 KB | 2026-01-22 |

### Data (5 files, 0.4 MB)

## 📝 README

```
# ![freqtrade](https://raw.githubusercontent.com/freqtrade/freqtrade/develop/docs/assets/freqtrade_poweredby.svg)

[![Freqtrade CI](https://github.com/freqtrade/freqtrade/actions/workflows/ci.yml/badge.svg?branch=develop)](https://github.com/freqtrade/freqtrade/actions/workflows/ci.yml)
[![DOI](https://joss.theoj.org/papers/10.21105/joss.04864/status.svg)](https://doi.org/10.21105/joss.04864)
[![Coverage Status](https://coveralls.io/repos/github/freqtrade/freqtrade/badge.svg?branch=develop&service=github)](https://coveralls.io/github/freqtrade/freqtrade?branch=develop)
[![Documentation](https://readthedocs.org/projects/freqtrade/badge/)](https://www.freqtrade.io)

Freqtrade is a free and open source crypto trading bot written in Python. It is designed to support all major exchanges and be controlled via Telegram or webUI. It contains backtesting, plotting and money management tools as well as strategy optimization by machine learning.

![freqtrade](https://raw.githubusercontent.com/freqtrade/freqtrade/develop/docs/assets/freqtrade-screenshot.png)

## Disclaimer

This software is for educational purposes only. Do not risk money which
you are afraid to lose. USE THE SOFTWARE AT YOUR OWN RISK. THE AUTHORS
AND ALL AFFILIATES ASSUME NO RESPONSIBILITY FOR YOUR TRADING RESULTS.

Always start by running a trading bot in Dry-Run and do not engage money
before you understand how it works and what profit/loss you should
expect.

We strongly recommend you to have coding and Python knowle
```
