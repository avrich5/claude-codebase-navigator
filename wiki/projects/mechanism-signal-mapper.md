# mechanism-signal-mapper

**Категория:** 📦 [Uncategorized](../categories/uncategorized.md)
**Статус:** 📁 no-git
**Путь:** `/Users/andriy/VisualStudio/mechanism-signal-mapper`

## 🛠 Tech Stack

- **Languages:** Python
- **Frameworks:** NumPy, Pandas
- **Tools:** pip

## 📁 Files (27 indexed)

### Code (19 files, 0.1 MB)

| File | Size | Modified |
|------|------|----------|
| `main.py` | 7 KB | 2026-03-03 |
| `data/aggregator.py` | 2 KB | 2026-03-03 |
| `data/states_loader.py` | 4 KB | 2026-03-03 |
| `data/clickhouse_loader.py` | 2 KB | 2026-03-03 |
| `config.py` | 1 KB | 2026-03-03 |
| `analysis/candidates.py` | 2 KB | 2026-03-03 |
| `output/writer.py` | 2 KB | 2026-03-03 |
| `analysis/stability.py` | 3 KB | 2026-03-03 |
| `analysis/aggregation.py` | 3 KB | 2026-03-03 |
| `analysis/transition_typer.py` | 3 KB | 2026-03-03 |
| `analysis/state_overlay.py` | 926 B | 2026-03-03 |
| `signals/matrix_builder.py` | 2 KB | 2026-03-03 |
| `signals/evaluator.py` | 4 KB | 2026-03-03 |
| `indicators/calculator.py` | 7 KB | 2026-03-03 |
| `indicators/warmup.py` | 2 KB | 2026-03-03 |

### Docs (4 files, 0.1 MB)

| File | Size | Modified |
|------|------|----------|
| `README.md` | 4 KB | 2026-03-03 |
| `docs/Mechanism_Signal_Mapper_TZ.md` | 46 KB | 2026-03-03 |
| `docs/CONTRACTS.md` | 2 KB | 2026-03-03 |
| `requirements.txt` | 218 B | 2026-03-03 |

### Data (3 files, 0.3 MB)

| File | Size | Modified |
|------|------|----------|
| `test_output/settings_to_signal_configs.csv` | 5 KB | 2026-03-03 |
| `test_output/activity_by_state.csv` | 48 KB | 2026-03-03 |
| `test_output/signal_matrix.parquet` | 228 KB | 2026-03-03 |

### Config (1 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `test_output/mechanism_candidates.json` | 365 B | 2026-03-03 |

## 📝 README

```
# Mechanism Signal Mapper

## Overview
The Mechanism Signal Mapper is a standalone analytical service designed to evaluate the performance and parametric stability of trading signal configurations across different market states and transitions between them. 
It takes bruteforce optimization results (`settings.tsv`), applies the extracted technical indicator conditions against historical minute-level market data from ClickHouse, and overlays daily market regime classifications (Base-States) to identify stable \"Mechanism Candidates\" during transitional states (R12).

## Key Features
- **Multi-timeframe Indicator Evaluation**: Parses logic strings (e.g., `RSI(30M,10)[0] < 25`) and computes all necessary technical indicators using TALib and pandas_ta.
- **State Overlaying**: Maps minute-by-minute signal occurrences to daily macroeconomic state labels (R1-R11 for stable states, R12 for transitions).
- **Transition Typing**: Automatically categorizes contiguous R12 periods by observing the stable states immediately before and after the transition (e.g., `R6→R2`).
- **Parametric Stability Analysis**: Groups similar indicator kernels to determine if a signal's activity in a specific transition type is robust against minor parameter variations.
- **Candidate Generation**: Outputs high-confidence Mechanism Candidates mapped back to their original optimization settings.

## Architecture & Integration
This project is architecturally separated from the `base-states` classifier to mainta
```
