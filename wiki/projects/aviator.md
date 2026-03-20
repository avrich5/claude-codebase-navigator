# aviator

**Категория:** 💰 [DeFi & Crypto Tools](../categories/defi_crypto.md)
**Статус:** 🟠 dormant
**Путь:** `/Users/andriy/VisualStudio/aviator`

## 📊 Git

- **Branch:** `main`
- **Коммитов:** 2
- **Последний:** 2025-04-06
- **Сообщение:** Перед созданием live-predictor
- **За 30 дней:** 0 коммитов

### Последние коммиты

- `2025-04-06` Перед созданием live-predictor
- `2025-03-31` Initial commit

## 📁 Files (109 indexed)

### Code (17 files, 0.4 MB)

| File | Size | Modified |
|------|------|----------|
| `data_validation.py` | 32 KB | 2025-04-16 |
| `api_test_synthetic.py` | 22 KB | 2025-04-16 |
| `prepare_and_calibrate.py` | 20 KB | 2025-04-16 |
| `trading_bot.py` | 12 KB | 2025-04-16 |
| `simple_api_test.py` | 4 KB | 2025-04-16 |
| `api_client.py` | 7 KB | 2025-04-16 |
| `high_performance_test.py` | 43 KB | 2025-04-16 |
| `main.py` | 11 KB | 2025-04-06 |
| `economics/risk_analysis.py` | 30 KB | 2025-04-01 |
| `economics/kelly_position_sizing.py` | 26 KB | 2025-04-01 |
| `economics/simulator.py` | 39 KB | 2025-04-01 |
| `results_analyzer.py` | 58 KB | 2025-03-31 |
| `clean_large_csv.py` | 6 KB | 2025-03-31 |
| `nan-fix-script.py` | 3 KB | 2025-03-31 |
| `data_explorer.py` | 29 KB | 2025-03-31 |

### Data (70 files, 194.3 MB)

| File | Size | Modified |
|------|------|----------|
| `processed_eth_base.csv` | 2.6 MB | 2025-03-31 |

### Docs (7 files, 2.0 MB)

| File | Size | Modified |
|------|------|----------|
| `README.md` | 15 KB | 2025-04-16 |
| `api_logs_20250416_193623.txt` | 1.4 MB | 2025-04-16 |
| `api_logs_20250406_111150.txt` | 209 KB | 2025-04-06 |
| `aviator_files.txt` | 5 KB | 2025-04-02 |
| `economics/REARME.md` | 9 KB | 2025-04-01 |
| `api_logs_20250401_095305.txt` | 348 KB | 2025-04-01 |
| `run_scripts.txt` | 4 KB | 2025-03-31 |

### Config (15 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `config.ini` | 2 KB | 2025-07-16 |

## 📝 README

```
# Торговый бот с использованием API Analysator

Этот проект представляет собой торгового бота, который использует API Analysator для получения торговых сигналов и принятия решений о покупке/продаже активов.

## Компоненты проекта

1. **TradingBot** - основной класс бота, который управляет торговыми решениями
2. **AnalysatorClient** - клиент для работы с API Analysator
3. **TradingAnalyzer** - инструмент для анализа результатов торговли и генерации отчетов
4. **Main** - главный скрипт для запуска различных компонентов системы

## Установка и запуск

### Зависимости

Для работы проекта необходимы следующие библиотеки:
- requests
- pandas
- matplotlib
- numpy

Установите зависимости с помощью pip:

```bash
pip install requests pandas matplotlib numpy
```

### Структура проекта

```
trading-bot/
├── main.py              # Главный скрипт для запуска бота
├── trading_bot.py       # Класс торгового бота
├── api_client.py        # Клиент API для получения предсказаний
├── data_analyzer.py     # Анализатор данных и генератор отчетов
├── config.ini           # Файл конфигурации
├── trade_log.json       # Лог сделок
├── logs/                # Директория с логами
└── reports/             # Директория с отчетами
```

## Использование

### Запуск торгового бота

```bash
python main.py bot [--config CONFIG_FILE]
```

Параметры:
- `--config` или `-c` - путь к файлу конфигурации (необязательный)

### Анализ результатов торговли

```bash
python main.py analyze [--log LOG_FILE] [--report]
```


```
