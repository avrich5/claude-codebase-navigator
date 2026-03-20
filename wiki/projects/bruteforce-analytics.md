# bruteforce-analytics

**Категория:** 📈 [Data & Analytics](../categories/data_analytics.md)
**Статус:** 📁 no-git
**Путь:** `/Users/andriy/VisualStudio/bruteforce-analytics`

## 🛠 Tech Stack

- **Languages:** Python

## 📁 Files (17 indexed)

### Config (2 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `pyproject.toml` | 621 B | 2026-01-29 |
| `configs/paths.yaml` | 767 B | 2026-01-29 |

### Docs (4 files, 0.1 MB)

| File | Size | Modified |
|------|------|----------|
| `docs/IMPLEMENTATION_PLAN_FULL_ML_PIPELINE.md` | 130 KB | 2026-01-29 |
| `docs/IMPLEMENTATION_PLAN_v2.md` | 9 KB | 2026-01-29 |
| `docs/unified_json_schema.md` | 9 KB | 2026-01-29 |
| `README.md` | 1 KB | 2026-01-29 |

### Code (11 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `tests/__init__.py` | 21 B | 2026-01-29 |
| `tests/test_parsers.py` | 2 KB | 2026-01-29 |
| `src/shared/config.py` | 3 KB | 2026-01-29 |
| `src/__init__.py` | 43 B | 2026-01-29 |

## 📝 README

```
# Bruteforce Analytics Service

Аналітичний сервіс для обробки результатів bruteforce оптимізації торгових стратегій.

## Архітектура

```
bruteforce-analytics/
├── src/
│   ├── shared/           # Спільні модулі (parsers, quality, loaders)
│   ├── generator/        # Training data generation (offline batch)
│   ├── analytics/        # Plateau finder, regime analysis (offline batch)
│   └── api/              # FastAPI endpoints (future microservice)
├── tests/
├── configs/
└── data/                 # Локальні дані для розробки (gitignore)
```

## Сервіси (planned)

| Service | Type | Purpose |
|---------|------|---------|
| generator | Batch | LLM training data з bruteforce results |
| analytics | Batch | Plateau/regime analysis |
| api | REST | Query interface (Phase 2) |

## Data Flow

```
External: /Users/andriy/VisualStudio/llm-training-data-miner/test_data/
    ↓
[shared/loaders] → Raw KPI, Settings
    ↓
[shared/parsers] → Parsed indicators
    ↓
[generator] OR [analytics]
    ↓
Output: training_data/ OR analysis_results/
```

## Конфігурація

Всі зовнішні шляхи в `configs/paths.yaml`:
- Не hardcode paths в коді
- Environment-specific overrides

```
