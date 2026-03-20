# indicators-basic

**Категория:** 🚀 [ProfitRadar Platform](../categories/profitradar_platform.md)
**Статус:** 🟢 active
**Путь:** `/Users/andriy/gitlab-prod/indicators-basic`

## 📊 Git

- **Branch:** `exante_symbols`
- **Коммитов:** 133
- **Последний:** 2026-03-02
- **Сообщение:** feat(indicators): add SAR, PIVOT, ICHIMOKU indicators
- **За 30 дней:** 2 коммитов

### Последние коммиты

- `2026-03-02` feat(indicators): add SAR, PIVOT, ICHIMOKU indicators
- `2025-12-12` Hide clickhouse_driver logging
- `2026-02-02` Fix Issue #5: Remove excessive DataFrame copying
- `2026-02-02` Optimize resample_to_timeframes to prevent redundant resampling
- `2026-02-02` Fix GIL-bound threading: Replace ThreadPoolExecutor with ProcessPoolExecutor

## 🛠 Tech Stack

- **Languages:** Python
- **Frameworks:** Flask, Pandas
- **Tools:** Docker, pip

## 📁 Files (11 indexed)

### Docs (3 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `requirements.txt` | 104 B | 2026-03-03 |
| `Readme.md` | 545 B | 2026-03-03 |
| `Blueprint.md` | 374 B | 2026-03-03 |

### Config (1 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `.gitlab-ci.yml` | 3 KB | 2026-03-03 |

### Code (7 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `app/utils.py` | 5 KB | 2026-03-03 |
| `app/app.py` | 2 KB | 2026-03-03 |

## 📝 README

```
# Create basic market indicators (RSI, BBE) from close price data

environment variables

database credentials

```bash
CH_HOST=
CH_PORT=
CH_USER=
CH_PASS=
```

common flask envs

```bash
FLASK_APP=app
FLASK_ENV=production
```

- quote for FTX = PERP, FOR BINANCE = USDT
- INDICATORS now supported only bbe, rsi and macd /n
- TFS - candles timeframes in minutes
- TIMEPERIOD - qty of candles used for indicator calculation, for macd now cardcoded values

```bash
QUOTE=PERP
INDICATORS=["bbe", "rsi", "macd"]
TFS=["15m", "30m"]
TIMEPERIOD=14
```

```
