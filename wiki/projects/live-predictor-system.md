# live-predictor-system

**Категория:** 🔮 [Predictors & Models](../categories/predictors_models.md)
**Статус:** 🟠 dormant
**Путь:** `/Users/andriy/VisualStudio/live-predictor-system`

## 📊 Git

- **Branch:** `main`
- **Коммитов:** 1
- **Последний:** 2025-04-09
- **Сообщение:** Initial commit
- **За 30 дней:** 0 коммитов

### Последние коммиты

- `2025-04-09` Initial commit

## 🛠 Tech Stack

- **Languages:** Python
- **Frameworks:** NumPy, Pandas
- **Tools:** pip

## 📁 Files (44 indexed)

### Docs (20 files, 0.1 MB)

| File | Size | Modified |
|------|------|----------|
| `reports/latest_report.html` | 4 KB | 2025-04-12 |
| `reports/report_20250412_170518.html` | 4 KB | 2025-04-12 |
| `reports/report_20250412_105013.html` | 4 KB | 2025-04-12 |
| `reports/report_20250412_042508.html` | 4 KB | 2025-04-12 |
| `reports/report_20250411_134610.html` | 4 KB | 2025-04-11 |
| `data/comparison_report.md` | 274 B | 2025-04-11 |
| `reports/report_20250411_074553.html` | 4 KB | 2025-04-11 |
| `reports/report_20250411_014538.html` | 4 KB | 2025-04-10 |
| `reports/report_20250410_194519.html` | 4 KB | 2025-04-10 |
| `reports/report_20250410_134511.html` | 4 KB | 2025-04-10 |
| `reports/report_20250410_074425.html` | 4 KB | 2025-04-10 |
| `reports/report_20250410_014330.html` | 4 KB | 2025-04-09 |
| `reports/report_20250409_194246.html` | 4 KB | 2025-04-09 |
| `README.md` | 8 KB | 2025-04-09 |
| `reports/report_20250409_132654.html` | 3 KB | 2025-04-09 |

### Code (15 files, 0.2 MB)

| File | Size | Modified |
|------|------|----------|
| `fix_calibration.py` | 14 KB | 2025-04-09 |
| `src/binance_client.py` | 10 KB | 2025-04-09 |
| `src/service.py` | 24 KB | 2025-04-09 |
| `src/predictor_client.py` | 21 KB | 2025-04-09 |
| `main_service_control.py` | 7 KB | 2025-04-09 |
| `fix_csv_structure.py` | 2 KB | 2025-04-09 |
| `src/data_manager.py` | 29 KB | 2025-04-09 |
| `query_hybrid_predictor.py` | 4 KB | 2025-04-09 |
| `src/compare_predictors.py` | 9 KB | 2025-04-09 |
| `switch_predictor.py` | 7 KB | 2025-04-09 |
| `src/utils.py` | 13 KB | 2025-04-07 |
| `src/chart_generator.py` | 19 KB | 2025-04-07 |
| `src/performance_tracker.py` | 13 KB | 2025-04-06 |
| `run_monitor.py` | 4 KB | 2025-04-06 |
| `main.py` | 7 KB | 2025-04-06 |

### Config (6 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `config.json` | 514 B | 2025-04-11 |
| `data/metrics.json` | 393 B | 2025-04-11 |
| `data/hybrid_metrics.json` | 320 B | 2025-04-09 |

### Data (3 files, 0.5 MB)

| File | Size | Modified |
|------|------|----------|
| `data/predictions.csv` | 70 KB | 2025-04-12 |
| `data/predictions 10-11 april.csv` | 212 KB | 2025-04-11 |
| `data/hybrid_predictions.csv` | 263 KB | 2025-04-11 |

## 📝 README

```
# Live Predictor System

Система для работы с API предикторов криптовалютных рынков в режиме реального времени. Получает данные с Binance, отправляет их предикторам и анализирует точность предсказаний.

## Возможности

- Получение данных с публичного API Binance
- Поддержка нескольких предикторов (оригинальный и гибридный)
- Калибровка предикторов на исторических данных
- Получение и валидация предсказаний в режиме реального времени
- Визуализация результатов и метрик точности
- Сравнение эффективности предикторов
- Отказоустойчивость и автоматическое восстановление

## Установка

```bash
# Клонируем репозиторий
git clone https://github.com/yourusername/live-predictor-system.git
cd live-predictor-system

# Создаем виртуальное окружение
python -m venv venv
source venv/bin/activate  # для Linux/Mac
# или
venv\Scripts\activate  # для Windows

# Устанавливаем зависимости
pip install -r requirements.txt
```

## Конфигурация

Настройки хранятся в файле `config.json`. Пример конфигурации:

```json
{
  "binance": {
    "pairs": ["BTC/USDC"],
    "interval": "1m",
    "historical_points": 120
  },
  "predictor": {
    "api_url": "http://194.32.79.48",
    "recalibration_hours": 24
  },
  "hybrid_predictor": {
    "api_url": "http://localhost:8000",
    "enabled": true,
    "model_name": "btc_optimal_base"
  },
  "service": {
    "check_interval": 60,
    "chart_update_interval": 300,
    "data_retention_days": 7
  },
  "log": {
    "level": "INFO",
    "file": "logs/live-predictor.log
```
