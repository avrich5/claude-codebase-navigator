# markov_predictor

**Категория:** 🔮 [Predictors & Models](../categories/predictors_models.md)
**Статус:** 🟠 dormant
**Путь:** `/Users/andriy/VisualStudio/markov_predictor`

## 📊 Git

- **Branch:** `main`
- **Коммитов:** 1
- **Последний:** 2025-05-09
- **Сообщение:** Новая версия проекта с LSTM-предиктором
- **За 30 дней:** 0 коммитов

### Последние коммиты

- `2025-05-09` Новая версия проекта с LSTM-предиктором

## 🛠 Tech Stack

- **Languages:** Python
- **Frameworks:** CCXT, Flask, NumPy, Pandas, Plotly, Polars, PyTorch
- **Tools:** pip

## 📁 Files (266 indexed)

### Docs (4 files, 0.1 MB)

| File | Size | Modified |
|------|------|----------|
| `markov_predictor_files.txt` | 24 KB | 2025-05-10 |
| `requirements.txt` | 5 KB | 2025-05-09 |
| `files.txt` | 6 KB | 2025-05-09 |
| `README.md` | 17 KB | 2025-05-09 |

### Code (28 files, 0.6 MB)

| File | Size | Modified |
|------|------|----------|
| `examples/lstm_experiment.py` | 54 KB | 2025-05-10 |
| `examples/test_significant_movement.py` | 24 KB | 2025-05-10 |
| `examples/diagnostic_test_significant_movement.py` | 4 KB | 2025-05-10 |
| `markov_predictor_api/__init__.py` | 115 B | 2025-05-10 |
| `markov_predictor/__init__.py` | 542 B | 2025-05-10 |
| `markov_predictor/significant_movement_predictor.py` | 39 KB | 2025-05-10 |
| `examples/test_market_modes.py` | 14 KB | 2025-05-10 |
| `evaluation/__init__.py` | 326 B | 2025-05-10 |
| `file_describer.ipynb` | 7 KB | 2025-05-10 |
| `markov_predictor/lstm_predictor.py` | 38 KB | 2025-05-09 |
| `market_optimizer.py` | 29 KB | 2025-04-13 |
| `evaluation/log_based_evaluator.py` | 36 KB | 2025-04-13 |
| `restore_balance.py` | 2 KB | 2025-04-13 |
| `examples/example_usage.py` | 15 KB | 2025-04-13 |
| `evaluation/experiment_runner.py` | 47 KB | 2025-04-13 |

### Config (87 files, 8.6 MB)

| File | Size | Modified |
|------|------|----------|
| `results/significant_movement_20250510_164012/config.json` | 1016 B | 2025-05-10 |
| `configs/adjusted_config.json` | 989 B | 2025-05-10 |
| `results/significant_movement_20250510_163816/config.json` | 1016 B | 2025-05-10 |
| `results/significant_movement_20250510_163532/config.json` | 1018 B | 2025-05-10 |
| `results/significant_movement_20250510_163331/config.json` | 1017 B | 2025-05-10 |
| `results/significant_movement_20250510_163058/config.json` | 1016 B | 2025-05-10 |
| `results/significant_movement_20250510_162640/config.json` | 1016 B | 2025-05-10 |
| `results/significant_movement_20250510_162415/config.json` | 1014 B | 2025-05-10 |
| `results/significant_movement_20250510_155434/config.json` | 1014 B | 2025-05-10 |
| `results/significant_movement_20250510_155000/config.json` | 1014 B | 2025-05-10 |
| `configs/high_accuracy.json` | 643 B | 2025-05-10 |
| `results/significant_movement_20250510_154457/config.json` | 1018 B | 2025-05-10 |
| `results/significant_movement_20250510_153255/config.json` | 1018 B | 2025-05-10 |
| `configs/high_frequency.json` | 642 B | 2025-05-10 |
| `configs/balanced.json` | 642 B | 2025-05-10 |

### Data (147 files, 858.3 MB)

| File | Size | Modified |
|------|------|----------|
| `data/btc_sample.csv` | 18 KB | 2025-04-11 |

## 📝 README

```
# Запуск одиночного эксперимента
python examples/lstm_experiment.py --mode single --data data/train/BTC_price_data.csv

# Запуск серии экспериментов с изменением порога нейтрального класса
python examples/lstm_experiment.py --mode multi --param neutral_confidence_threshold --values 0.99,0.95,0.9,0.85,0.8

# Запуск серии экспериментов с изменением минимальной уверенности для направления
python examples/lstm_experiment.py --mode multi --param min_direction_confidence --values 0.05,0.1,0.2,0.3,0.4

# Инструкция по организации проекта MarkovPredictor

Вижу, что вы уже почистили структуру проекта. На основе разработанной архитектуры и существующих файлов, предлагаю следующую организацию:

## 1. Структура каталогов

```
markov_predictor/                      # Корневая директория проекта
├── markov_predictor/                  # Основной пакет
│   ├── __init__.py                    # Инициализация пакета
│   ├── base_predictor.py              # Базовый класс для предикторов
│   ├── markov_predictor.py            # Основная реализация предиктора
│   ├── config.py                      # Общая конфигурация проекта
│   ├── predictor_configs.py           # Реестр конфигураций предикторов
│   ├── dataset_manager.py             # Работа с данными
│   ├── predictor_evaluator.py         # Оценка предикторов
│   └── utils/                         # Вспомогательные модули
│       ├── __init__.py
│       ├── data_loader.py             # Загрузка данных
│       └── visualization.py           # В
```
