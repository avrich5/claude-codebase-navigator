# stock-data-miners

**Категория:** 📦 [Uncategorized](../categories/uncategorized.md)
**Статус:** 🟡 recent
**Путь:** `/Users/andriy/gitlab-prod/stock-data-miners`

## 📊 Git

- **Branch:** `main`
- **Коммитов:** 3
- **Последний:** 2026-01-09
- **Сообщение:** Merge remote README
- **За 30 дней:** 0 коммитов

### Последние коммиты

- `2026-01-09` Merge remote README
- `2026-01-09` Initial commit
- `2026-01-09` Initial commit: Stock data miners with dual-source architecture

## 🛠 Tech Stack

- **Languages:** JavaScript/TypeScript
- **Tools:** npm

## 📁 Files (7 indexed)

### Docs (3 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `secret/README.md` | 1 KB | 2026-02-28 |
| `README.md` | 3 KB | 2026-02-28 |

### Config (1 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `package.json` | 343 B | 2026-02-28 |

### Code (3 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `tools/sse_trades_miner_stocks.js` | 21 KB | 2026-02-28 |
| `tools/polygon_daemon.js` | 29 KB | 2026-02-28 |
| `secret/index.js` | 499 B | 2026-02-28 |

## 📝 README

```
# Stock Data Miners

Система сбора и агрегации данных фондового рынка NASDAQ с двухуровневой архитектурой:
- **Polygon.io** - исторические данные (2 года, консолидированные объёмы)
- **Exante SSE** - реалтайм данные (лаг ~100 секунд)

## Быстрый старт

### 1. Установка зависимостей
```bash
npm install
```

### 2. Настройка окружения
```bash
cp .env.example .env
# Отредактируйте .env - добавьте свои ключи API
```

### 3. Запуск майнеров

**Polygon Daemon (исторические данные):**
```bash
# Первичная загрузка
node tools/polygon_daemon.js

# Production (scheduled mode)
SCHEDULED=1 node tools/polygon_daemon.js
```

**SSE Miner (реалтайм данные):**
```bash
node tools/sse_trades_miner_stocks.js
```

## Документация

- **[Архитектура системы](tools/docs/ARCHITECTURE.md)** - подробное описание, настройка, troubleshooting

## Структура проекта
```
stock-data-miners/
├── tools/
│   ├── polygon_daemon.js          # Загрузка данных из Polygon.io
│   ├── sse_trades_miner_stocks.js # Сбор реалтайм данных из Exante SSE
│   └── docs/
│       └── ARCHITECTURE.md         # Полная документация
├── secret/
│   ├── index.js                    # Модуль шифрования/дешифровки (RSA)
│   └── mmi_rsa                     # RSA приватный ключ (НЕ в git!)
├── .env.example                    # Шаблон переменных окружения
├── .gitignore
├── package.json
└── README.md
```

**⚠️ Безопасность:**
- `secret/mmi_rsa` - приватный ключ, **НЕ коммитится в git**
- Локально: файл должен существовать для дешифровки
- На
```
