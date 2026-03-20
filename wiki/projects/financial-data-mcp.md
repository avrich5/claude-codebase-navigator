# financial-data-mcp

**Категория:** 📈 [Data & Analytics](../categories/data_analytics.md)
**Статус:** 📁 no-git
**Путь:** `/Users/andriy/VisualStudio/financial-data-mcp`

## 📁 Files (6 indexed)

### Code (4 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `start_server.sh` | 89 B | 2025-06-20 |
| `financial_mcp_server.py` | 25 KB | 2025-06-20 |

### Docs (1 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `README.md` | 3 KB | 2025-06-20 |

### Data (1 files, 0.0 MB)

## 📝 README

```
# Financial Data MCP Server

## 🏦 Что это?

Безопасный MCP сервер для работы с финансовыми данными, Python кодом и Jupyter ноутбуками в Claude Desktop. Автоматически фильтрует чувствительную информацию.

## 🔐 Безопасность

### Автоматически скрывает:
- API ключи и токены
- Номера счетов и ID клиентов  
- Персональные данные
- Финансовые балансы
- Пароли и секреты

### Поддерживаемые форматы:
- Python (.py) - анализ кода и функций
- Jupyter (.ipynb) - анализ ячеек
- CSV файлы - умная фильтрация
- Excel (.xlsx, .xls)
- JSON, YAML, SQL

## 🚀 Быстрый старт

1. **Размещение данных:**
   ```bash
   # Скопируйте ваши файлы в папку financial_data/
   cp -r ~/your_trading_data/* financial_data/
   ```

2. **Перезапуск Claude Desktop:**
   - Полностью закройте Claude Desktop
   - Запустите снова

3. **Тестирование в Claude:**
   ```
   Покажи структуру моих финансовых проектов
   ```

## 💡 Примеры команд

- "Проанализируй CSV файл sample_trading_data.csv"
- "Извлеки функции из example_strategy.py"  
- "Покажи структуру ноутбука market_analysis.ipynb"
- "Найди код связанный с 'backtest'"

## 📂 Структура

```
financial-data-mcp/
├── venv/                    # Python окружение
├── financial_mcp_server.py  # MCP сервер
├── financial_data/          # 👈 ВАШИ ДАННЫЕ
│   ├── strategies/          # Python стратегии
│   ├── notebooks/           # Jupyter ноутбуки
│   ├── data/               # CSV, Excel файлы
│   └── config/             # Конфигурации
└── README.md
```

## 🔧 Устранение неполадок
```
