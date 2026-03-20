# markov_quantile_predictor

**Категория:** 🔮 [Predictors & Models](../categories/predictors_models.md)
**Статус:** 🟠 dormant
**Путь:** `/Users/andriy/VisualStudio/markov_quantile_predictor`

## 📊 Git

- **Branch:** `main`
- **Коммитов:** 19
- **Последний:** 2025-03-27
- **Сообщение:** depence on base config decrease confidence_threshold=0.005 Success Rate=54.29%
- **За 30 дней:** 0 коммитов

### Последние коммиты

- `2025-03-27` depence on base config decrease confidence_threshold=0.005 Success Rate=54.29%
- `2025-03-25` base and improved configs works properly
- `2025-03-24` 57.81%
- `2025-03-24` before project refactoring
- `2025-03-23` Сохраняю локальные изменения перед переключением

## 🛠 Tech Stack

- **Languages:** Python
- **Frameworks:** NumPy, Pandas
- **Tools:** pip

## 📁 Files (108 indexed)

### Docs (58 files, 0.1 MB)

| File | Size | Modified |
|------|------|----------|
| `reports/custom_report_20250327_175534.md` | 2 KB | 2025-03-27 |
| `reports/baseline_report_20250327_175534.md` | 2 KB | 2025-03-27 |
| `markov_quantile_predictor_files.txt` | 8 KB | 2025-03-27 |
| `reports/custom_report_20250325_171825.md` | 1 KB | 2025-03-25 |
| `reports/baseline_report_20250325_171825.md` | 2 KB | 2025-03-25 |
| `validation_results_v3/btc_uptrend_ws750_cov5_report.md` | 1 KB | 2025-03-25 |
| `validation_results_v3/btc_downtrend_ws750_cov5_report.md` | 1 KB | 2025-03-25 |
| `file_list.txt` | 6 KB | 2025-03-25 |
| `README.md` | 15 KB | 2025-03-25 |
| `reports/custom_report_20250325_163304.md` | 1 KB | 2025-03-25 |
| `reports/baseline_report_20250325_163304.md` | 1 KB | 2025-03-25 |
| `reports/custom_report_20250325_162644.md` | 1 KB | 2025-03-25 |
| `reports/baseline_report_20250325_162644.md` | 1 KB | 2025-03-25 |
| `reports/custom_report_20250325_160322.md` | 1 KB | 2025-03-25 |
| `reports/baseline_report_20250325_160322.md` | 1 KB | 2025-03-25 |

### Code (28 files, 0.3 MB)

| File | Size | Modified |
|------|------|----------|
| `examples/base_config.py` | 19 KB | 2025-03-27 |
| `examples/improved_config.py` | 17 KB | 2025-03-27 |
| `temp_comparison/test_enhanced_hybrid_old.py` | 4 KB | 2025-03-25 |
| `temp_comparison/test_enhanced_hybrid_new.py` | 4 KB | 2025-03-25 |
| `examples/validate_enhanced_hybrid.py` | 27 KB | 2025-03-25 |
| `examples/simple_example.py` | 6 KB | 2025-03-25 |
| `examples/new_config_usage.py` | 21 KB | 2025-03-25 |
| `examples/compare_models.py` | 8 KB | 2025-03-25 |
| `reports/improved_config_20250325_144520.py` | 673 B | 2025-03-25 |
| `examples/early_stopping_enhancement.py` | 9 KB | 2025-03-25 |
| `markov_quantile_predictor/predictor_config.py` | 6 KB | 2025-03-25 |
| `examples/test_enhanced_hybrid.py` | 12 KB | 2025-03-24 |
| `markov_quantile_predictor/factory.py` | 2 KB | 2025-03-23 |
| `markov_quantile_predictor/__init__.py` | 951 B | 2025-03-23 |
| `temp_comparison/quantile_regression_new.py` | 9 KB | 2025-03-23 |

### Data (22 files, 21.2 MB)

| File | Size | Modified |
|------|------|----------|
| `reports/config_comparison_20250325_101537.csv` | 207 B | 2025-03-25 |
| `validation_results_v3/validation_summary_20250323_131804.csv` | 1 B | 2025-03-23 |
| `validation_data/predictor_btc_uptrend.csv` | 136 KB | 2025-03-23 |
| `validation_data/predictor_btc_low_volatility.csv` | 399 KB | 2025-03-23 |
| `validation_data/predictor_btc_last_month.csv` | 399 KB | 2025-03-23 |
| `validation_data/predictor_btc_high_volatility.csv` | 32 KB | 2025-03-23 |
| `validation_data/predictor_btc_downtrend.csv` | 282 KB | 2025-03-23 |
| `validation_data/predictor_btc_base.csv` | 399 KB | 2025-03-23 |
| `validation_data/predictor_btc_5min.csv` | 399 KB | 2025-03-23 |
| `validation_data/eth_base.csv` | 2.3 MB | 2025-03-23 |
| `validation_data/btc_uptrend.csv` | 2.2 MB | 2025-03-23 |
| `validation_data/btc_sideways.csv` | 112 KB | 2025-03-23 |
| `validation_data/btc_low_volatility.csv` | 2.2 MB | 2025-03-23 |
| `validation_data/btc_last_month.csv` | 2.3 MB | 2025-03-23 |
| `validation_data/btc_high_volatility.csv` | 203 KB | 2025-03-23 |

## 📝 README

```
# Markov Quantile Predictor

Гибридная модель для предсказания временных рядов, объединяющая марковские цепи и квантильную регрессию.

## Описание проекта

Markov Quantile Predictor представляет собой гибридный подход к прогнозированию временных рядов. Проект включает три основные модели:

1. **MarkovPredictor** - базовая модель на основе марковских цепей
2. **MarkovQuantilePredictor** - простая гибридная модель, объединяющая марковские цепи и квантильную регрессию
3. **EnhancedHybridPredictor** - улучшенная гибридная модель с расширенными характеристиками состояний

Такой подход позволяет не только предсказывать направление движения цены, но и оценивать вероятностные интервалы будущих значений.

## Структура проекта

```
markov_quantile_predictor/
├── __init__.py
├── predictor_config.py
├── factory.py
├── utils.py
├── config/
│   ├── __init__.py
│   ├── defaults.py
│   └── presets.py
├── models/
│   ├── __init__.py
│   ├── markov_predictor.py       # Базовая марковская модель
│   ├── hybrid_predictor.py       # Гибридные модели (MarkovQuantilePredictor и EnhancedHybridPredictor)
│   ├── quantile_regression.py    # Модуль квантильной регрессии
│   └── early_stopping.py         # Функциональность раннего останова
└── examples/
    ├── simple_example.py             # Простой пример использования
    ├── new_config_usage.py           # Пример работы с конфигурациями
    ├── validate_enhanced_hybrid.py   # Валидация улучшенной гибридной модели
    ├── test_enhanced_hybrid.py     
```
