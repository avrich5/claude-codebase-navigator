# base-states

**Категория:** 🔮 [Predictors & Models](../categories/predictors_models.md)
**Статус:** 🟢 active
**Путь:** `/Users/andriy/VisualStudio/base-states`

## 📊 Git

- **Branch:** `aa_local`
- **Коммитов:** 57
- **Последний:** 2026-03-05
- **Сообщение:** ignore docs/Mechanism_Signal_Mapper_TZ.md
- **За 30 дней:** 57 коммитов

### Последние коммиты

- `2026-03-05` ignore docs/Mechanism_Signal_Mapper_TZ.md
- `2026-03-02` fix: update nginx conf to use IPV4
- `2026-03-02` update ingress annotations
- `2026-03-02` fix: nginx container file
- `2026-03-02` fix: nginx permissions

## 🛠 Tech Stack

- **Tools:** Docker Compose

## 📁 Files (130 indexed)

### Docs (19 files, 4.7 MB)

| File | Size | Modified |
|------|------|----------|
| `requirements_realtime.txt` | 133 B | 2026-03-05 |
| `requirements_pipeline.txt` | 97 B | 2026-03-05 |
| `docs/state-detection.md` | 15 KB | 2026-03-05 |
| `docs/running-the-app.md` | 2 KB | 2026-03-05 |
| `docs/regime_logic.html` | 29 KB | 2026-03-05 |
| `docs/project-structure.md` | 5 KB | 2026-03-05 |
| `docs/features-and-flows.md` | 7 KB | 2026-03-05 |
| `docs/devops-reference.md` | 5 KB | 2026-03-05 |
| `docs/database.md` | 6 KB | 2026-03-05 |
| `docs/base-states-overview.md` | 16 KB | 2026-03-05 |
| `docs/api-reference.md` | 7 KB | 2026-03-05 |
| `app/realtime_dashboard.html` | 22 KB | 2026-03-05 |
| `README.md` | 11 KB | 2026-03-05 |
| `CLAUDE.md` | 18 KB | 2026-03-05 |
| `docs/Mechanism_Signal_Mapper_TZ.md` | 31 KB | 2026-03-02 |

### Config (36 files, 0.8 MB)

| File | Size | Modified |
|------|------|----------|
| `helm/base-states/templates/configmap.yaml` | 263 B | 2026-03-05 |
| `docker-compose.yml` | 845 B | 2026-03-05 |
| `.gitlab-ci.yml` | 6 KB | 2026-03-05 |
| `output/composite_summary.json` | 1 KB | 2026-02-28 |
| `output/regime_summary.json` | 20 KB | 2026-02-28 |
| `realtime_output/live_state.json` | 4 KB | 2026-02-26 |
| `realtime_output/narrative_cache.json` | 1 KB | 2026-02-26 |

### Code (43 files, 0.3 MB)

| File | Size | Modified |
|------|------|----------|
| `tests/test_uncertainty.py` | 11 KB | 2026-03-05 |
| `pipeline/uncertainty.py` | 12 KB | 2026-03-05 |
| `tests/test_validation.py` | 8 KB | 2026-03-05 |
| `tests/test_transition_probs.py` | 12 KB | 2026-03-05 |
| `tests/test_rules.py` | 14 KB | 2026-03-05 |
| `tests/test_proximity.py` | 12 KB | 2026-03-05 |
| `tests/test_live_fetcher.py` | 13 KB | 2026-03-05 |
| `tests/test_features.py` | 5 KB | 2026-03-05 |
| `tests/test_composite.py` | 13 KB | 2026-03-05 |
| `pipeline/validation.py` | 5 KB | 2026-03-05 |
| `pipeline/state_rules.py` | 11 KB | 2026-03-05 |
| `pipeline/output.py` | 3 KB | 2026-03-05 |
| `pipeline/main.py` | 6 KB | 2026-03-05 |
| `pipeline/logger.py` | 2 KB | 2026-03-05 |
| `pipeline/features.py` | 6 KB | 2026-03-05 |

### Data (32 files, 13.1 MB)

| File | Size | Modified |
|------|------|----------|
| `output/composite_market_state.csv` | 184 KB | 2026-02-28 |
| `output/all_regimes.parquet` | 2.1 MB | 2026-02-28 |
| `output/XRPUSDT_regimes.csv` | 499 KB | 2026-02-28 |
| `output/SOLUSDT_regimes.csv` | 506 KB | 2026-02-28 |
| `output/ETHUSDT_regimes.csv` | 514 KB | 2026-02-28 |
| `output/DOGEUSDT_regimes.csv` | 501 KB | 2026-02-28 |
| `output/BTCUSDT_regimes.csv` | 520 KB | 2026-02-28 |
| `output/BNBUSDT_regimes.csv` | 507 KB | 2026-02-28 |
| `output/ADAUSDT_regimes.csv` | 499 KB | 2026-02-28 |
| `data/XRPUSDT_1d.parquet` | 119 KB | 2026-02-28 |
| `data/SOLUSDT_1d.parquet` | 106 KB | 2026-02-28 |
| `data/ETHUSDT_1d.parquet` | 111 KB | 2026-02-28 |
| `data/DOGEUSDT_1d.parquet` | 127 KB | 2026-02-28 |
| `data/BTCUSDT_1d.parquet` | 115 KB | 2026-02-28 |
| `data/BNBUSDT_1d.parquet` | 102 KB | 2026-02-28 |

## 📝 README

```
# Base-States — Market Regime Classifier

A deterministic crypto market regime classification system. Labels every trading day for 7 assets with one of 12 macro market states (R1–R12) based on percentile-normalized technical features. Runs as a one-shot batch pipeline for historical output and as a persistent real-time API server for live monitoring.

---

## What It Does

The classifier answers one question: *what kind of market is this?*

Every trading day for BTCUSDT, ETHUSDT, BNBUSDT, SOLUSDT, XRPUSDT, ADAUSDT, and DOGEUSDT is assigned one of 12 regimes derived from ~20 rolling features (trend strength, volatility, volume behavior, price structure). These labels are the foundation for downstream trading systems that need to adapt their behavior to current market conditions.

**Two independent modes:**

| | Batch Pipeline | Real-Time Server |
|---|---|---|
| Purpose | Classify 5 years of historical data | Monitor current market state live |
| Entry point | `python pipeline/main.py` | `uvicorn app.server:app` |
| Output | CSV/Parquet/JSON + static HTML dashboard | JSON API + live-updating browser UI |
| Binance | Fetches on run, then caches | Polls every 5 minutes |
| OpenAI | Not used | Optional — narrative generation |
| Container | One-shot, exits on completion | Persistent, `restart: unless-stopped` |

Both modes share the same classification engine (`pipeline/state_rules.py`, `pipeline/features.py`, `pipeline/config.py`).

---

## The 12 Regimes

Classification is a pr
```
