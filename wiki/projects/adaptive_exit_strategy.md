# adaptive_exit_strategy

**Категория:** 📊 [Trading Strategies](../categories/trading_strategies.md)
**Статус:** 📁 no-git
**Путь:** `/Users/andriy/VisualStudio/adaptive_exit_strategy`

## 🛠 Tech Stack

- **Languages:** Python
- **Frameworks:** CCXT, Flask, NumPy, Pandas, Plotly, Polars
- **Tools:** pip

## 📁 Files (237 indexed)

### Docs (34 files, 0.1 MB)

| File | Size | Modified |
|------|------|----------|
| `data/adaptive_exit_strategy_data_files.txt` | 3 KB | 2025-05-04 |
| `results/summary_report.txt` | 3 KB | 2025-05-04 |
| `adaptive_exit_strateg_files.txt` | 2 KB | 2025-05-03 |
| `README.md` | 29 KB | 2025-05-03 |
| `talib.txt` | 185 B | 2025-05-03 |
| `requirements.txt` | 5 KB | 2025-05-03 |
| `plan.md` | 11 KB | 2025-05-03 |

### Code (28 files, 0.7 MB)

| File | Size | Modified |
|------|------|----------|
| `analyze_all_predictions.py` | 61 KB | 2025-05-04 |
| `convert_inform_to_predictions.py` | 16 KB | 2025-05-04 |
| `exit_point_analysis.py` | 53 KB | 2025-05-04 |
| `adaptive_analysis.py` | 52 KB | 2025-05-04 |
| `adaptive_exit_strategy/main.py` | 16 KB | 2025-05-03 |
| `tests/test_clickhouse.py` | 11 KB | 2025-05-03 |
| `load_env.py` | 648 B | 2025-05-03 |
| `simple_test.py` | 5 KB | 2025-05-03 |
| `adaptive_exit_strategy/__init__.py` | 0 B | 2025-05-03 |

### Config (8 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `config/config.json` | 2 KB | 2025-05-03 |
| `config/logging_config.json` | 0 B | 2025-05-03 |

### Data (167 files, 446.6 MB)

| File | Size | Modified |
|------|------|----------|
| `results/conditional_probabilities.csv` | 2 KB | 2025-05-04 |
| `results/minute_stats.csv` | 3 KB | 2025-05-04 |
| `results/signal_results.csv` | 40 KB | 2025-05-04 |
| `results/reason_summary.csv` | 448 B | 2025-05-03 |
| `results/model_summary.csv` | 156 B | 2025-05-03 |
| `results/market_summary.csv` | 799 B | 2025-05-03 |
| `results/trades_detailed_report.csv` | 278 KB | 2025-05-03 |

## 📝 README

```
# Документация моделей и настроек адаптивной стратегии выхода

## Содержание
1. [Архитектура системы](#архитектура-системы)
2. [Модели и компоненты](#модели-и-компоненты)
   - [MarketAnalyzer](#marketanalyzer)
   - [DecisionMaker](#decisionmaker)
   - [PositionManager](#positionmanager)
   - [BacktestEngine](#backtestengine)
3. [Настройки](#настройки)
   - [Настройки стратегии выхода](#настройки-стратегии-выхода)
   - [Настройки управления позициями](#настройки-управления-позициями)
   - [Настройки бэктестинга](#настройки-бэктестинга)
   - [Настройки технических индикаторов](#настройки-технических-индикаторов)
4. [Методология бэктестинга](#методология-бэктестинга)
5. [Метрики эффективности](#метрики-эффективности)

## Архитектура системы

Система адаптивной стратегии выхода состоит из четырех основных компонентов:

1. **MarketAnalyzer** - анализ состояния рынка и построение прогнозных моделей
2. **DecisionMaker** - принятие решений о точке выхода на основе анализа рынка
3. **PositionManager** - управление открытыми позициями и их параметрами
4. **BacktestEngine** - движок для симуляции торговли на исторических данных

Взаимодействие между компонентами:
- **MarketAnalyzer** получает исторические данные и анализирует состояние рынка
- **DecisionMaker** использует результаты анализа для определения оптимальной точки выхода
- **PositionManager** управляет размером позиций и их закрытием
- **BacktestEngine** координирует работу всех компонентов и моделирует выполнение стратегии

#
```
