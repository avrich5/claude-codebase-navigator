# pattern-recognition

**Категория:** 🔮 [Predictors & Models](../categories/predictors_models.md)
**Статус:** 📁 no-git
**Путь:** `/Users/andriy/VisualStudio/pattern-recognition`

## 📁 Files (59 indexed)

### Code (8 files, 0.1 MB)

| File | Size | Modified |
|------|------|----------|
| `signals.py` | 12 KB | 2026-03-13 |
| `pattern_discovery.py` | 9 KB | 2026-02-18 |
| `summarize.py` | 36 KB | 2026-02-18 |
| `config.py` | 3 KB | 2026-02-18 |
| `main.py` | 2 KB | 2026-02-18 |
| `ohlcv.py` | 4 KB | 2026-02-18 |
| `features.py` | 12 KB | 2026-02-18 |
| `db.py` | 1 KB | 2026-02-18 |

### Docs (10 files, 0.6 MB)

| File | Size | Modified |
|------|------|----------|
| `docs/patern_recognition_concept_en.txt` | 4 KB | 2026-02-18 |
| `docs/patern_recognition_concept_ru.txt` | 6 KB | 2026-02-18 |
| `output/summary_20260218_132546.md` | 172 KB | 2026-02-18 |
| `development_plan.md` | 9 KB | 2026-02-18 |
| `README.md` | 12 KB | 2026-02-18 |
| `output/summary_20260218_130014.md` | 172 KB | 2026-02-18 |
| `SIGNALS.md` | 11 KB | 2026-02-18 |
| `output/summary_20260218_124107.md` | 132 KB | 2026-02-18 |
| `output/summary_20260218_123127.md` | 86 KB | 2026-02-18 |
| `output/summary_20260218_121851.md` | 40 KB | 2026-02-18 |

### Config (41 files, 9.3 MB)

| File | Size | Modified |
|------|------|----------|
| `output/signal_dictionary_BTCUSDT_1h.json` | 5 KB | 2026-03-13 |
| `output/signal_dictionary_BTC_USDT_1h.json` | 5 KB | 2026-03-10 |
| `output/signal_dictionary_ETHUSDT_1h.json` | 5 KB | 2026-03-10 |
| `output/signal_dictionary_SOLUSDT_1h.json` | 5 KB | 2026-03-10 |
| `output/signal_dictionary_XAUUSD_1h.json` | 5 KB | 2026-03-10 |
| `output/signal_dictionary_EURUSD_1h.json` | 5 KB | 2026-03-10 |
| `output/signal_dictionary_XAG_USDT_1h.json` | 5 KB | 2026-03-10 |
| `output/signal_dictionary_GBPUSD_1h.json` | 5 KB | 2026-03-10 |
| `output/cross_asset_timeframe_20260218_132546.json` | 1.2 MB | 2026-02-18 |
| `output/cross_asset_patterns_20260218_132546.json` | 1.5 MB | 2026-02-18 |
| `output/cross_asset_timeframe_20260218_130014.json` | 1.2 MB | 2026-02-18 |
| `output/cross_asset_patterns_20260218_130014.json` | 1.5 MB | 2026-02-18 |
| `output/cross_asset_patterns_20260218_124107.json` | 1.5 MB | 2026-02-18 |
| `output/pattern_dictionary_SOLUSDT_4h.json` | 78 KB | 2026-02-18 |
| `output/signal_dictionary_SOLUSDT_4h.json` | 5 KB | 2026-02-18 |

## 📝 README

```
# Pattern Recognition

Статистичний пошук структурно стійких комбінацій технічних сигналів у OHLCV-даних криптовалютних ф'ючерсів (Binance Futures).

**Ключова ідея:** знайти сигнальні комбінації, які виникають разом значно частіше ніж очікується при незалежності (high lift), стабільно рік-за-роком (low CV), і підтверджені на кількох асетах (cross-asset universality).

> Проект не робить прогнозів і не торгує. Виходи — словники паттернів для подальшого використання в стратегіях.

---

## Результати

### Паттерни по асетах (стабільні, lift > threshold)

| Asset | 5m | 15m | 30m | 1h | 4h |
|-------|-----|-----|-----|-----|-----|
| BTCUSDT | 145 | 200 | 262 | 310 | 242 |
| ETHUSDT | 156 | 217 | 290 | 389 | 360 |
| SOLUSDT | 154 | 236 | 305 | 297 | 190 |

### Cross-asset universal patterns (BTC + ETH + SOL)

| TF | 🌍 All-3 assets | 🔗 Partial (2/3) | Total |
|----|----------------|-----------------|-------|
| 5m  | 100 | 46  | 146 |
| 15m | 104 | 88  | 192 |
| 30m | 126 | 150 | 276 |
| 1h  | 109 | 189 | 298 |
| 4h  |  31 | 158 | 189 |

### Cross-asset × Cross-Timeframe (найнадійніші паттерни)

Паттерни що пройшли cross-asset фільтр **на кількох таймфреймах одночасно**. Оцінюються за `combined_score = tf_coverage × asset_coverage`.

| TF coverage | Кількість паттернів |
|-------------|---------------------|
| 2/5 TF | 144 |
| 3/5 TF | 83 |
| 4/5 TF | 56 |
| **5/5 TF (всі)** | **15** |

**Абсолютний чемпіон** — `BB_LOWER_TOUCH + MACD_HIST_SHRINK + STOCH_OVERSOLD`:
- `combined_score
```
