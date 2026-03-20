# profit-radar-io

**Категория:** 🚀 [ProfitRadar Platform](../categories/profitradar_platform.md)
**Статус:** 🟡 recent
**Путь:** `/Users/andriy/VisualStudio/profit-radar-io`

## 📊 Git

- **Branch:** `baas`
- **Коммитов:** 84
- **Последний:** 2026-01-09
- **Сообщение:** fix status before add model test window
- **За 30 дней:** 0 коммитов

### Последние коммиты

- `2026-01-09` fix status before add model test window
- `2025-12-22` Strategy Description + Conditions & Filters
- `2025-12-22` Strategy Descriptiond
- `2025-12-22` backtest result title fixed
- `2025-12-22` Fixed Style Strategy Description

## 🛠 Tech Stack

- **Languages:** JavaScript/TypeScript
- **Tools:** Docker, npm

## 📁 Files (344 indexed)

### Docs (89 files, 1.0 MB)

| File | Size | Modified |
|------|------|----------|
| `www/update-cookies.html` | 9 KB | 2026-01-09 |
| `www/strategy.html` | 13 KB | 2026-01-09 |
| `www/strategy-optimization.html` | 7 KB | 2026-01-09 |
| `www/strategy-generation.html` | 5 KB | 2026-01-09 |
| `www/strategy-builder.html` | 46 KB | 2026-01-09 |
| `www/main.html` | 5 KB | 2026-01-09 |
| `www/login.html` | 3 KB | 2026-01-09 |
| `www/data/README-configs.md` | 9 KB | 2026-01-09 |
| `www/dashboard.html` | 21 KB | 2026-01-09 |
| `www/balances_carousel.html` | 2 KB | 2026-01-09 |
| `profitradar BAAS_IDEOLOGY.md` | 57 KB | 2026-01-09 |
| `experiments/_service/README.md` | 4 KB | 2026-01-09 |
| `experiments/README-AI-KNOWLEDGE-BASE.md` | 7 KB | 2026-01-09 |
| `experiments/AI_CHAT_PROMPTS.md` | 15 KB | 2026-01-09 |
| `chat_ai_foundation.md` | 32 KB | 2026-01-09 |

### Code (82 files, 0.6 MB)

| File | Size | Modified |
|------|------|----------|
| `utils/knowledge-base.js` | 13 KB | 2026-01-09 |
| `update-ai-prompt.py` | 4 KB | 2026-01-09 |
| `test-knowledge-base.js` | 4 KB | 2026-01-09 |
| `services/backtest/configMapper.js` | 6 KB | 2026-01-09 |
| `scripts/update-cookies.js` | 2 KB | 2026-01-09 |
| `routes/index.js` | 4 KB | 2026-01-09 |
| `quick-fix.sh` | 3 KB | 2026-01-09 |
| `master-integrate.py` | 2 KB | 2026-01-09 |
| `integrate-ai-chat.py` | 7 KB | 2026-01-09 |
| `index.js` | 966 B | 2026-01-09 |
| `experiments/load-test-config.js` | 1 KB | 2026-01-09 |
| `experiments/generate-strategy-catalog.js` | 12 KB | 2026-01-09 |
| `experiments/generate-single-configs.js` | 6 KB | 2026-01-09 |
| `experiments/debug-trading-report.js` | 2 KB | 2026-01-09 |
| `experiments/build-analytics-matrix.js` | 13 KB | 2026-01-09 |

### Data (35 files, 45.1 MB)

| File | Size | Modified |
|------|------|----------|
| `total.csv` | 63 B | 2026-01-09 |
| `report.csv` | 63 B | 2026-01-09 |
| `archive/pnls.csv` | 63 B | 2025-11-06 |
| `archive/report.csv` | 63 B | 2025-11-05 |
| `archive/total.csv` | 63 B | 2025-11-05 |

### Config (138 files, 0.7 MB)

| File | Size | Modified |
|------|------|----------|
| `.auth-cookies.json` | 240 B | 2026-01-16 |
| `www/data/generation-curves-config.json` | 12 KB | 2026-01-09 |
| `www/data/generation-curves-config-very-aggressive.json` | 12 KB | 2026-01-09 |
| `www/data/generation-curves-config-realistic-mix.json` | 12 KB | 2026-01-09 |
| `www/data/generation-curves-config-conservative.json` | 12 KB | 2026-01-09 |
| `www/data/generation-curves-config-base.json` | 12 KB | 2026-01-09 |
| `www/data/generation-curves-config-balanced.json` | 12 KB | 2026-01-09 |
| `www/data/generation-curves-config-aggressive.json` | 12 KB | 2026-01-09 |
| `package.json` | 670 B | 2026-01-09 |
| `package-lock.json` | 96 KB | 2026-01-09 |
| `experiments/test-config.json` | 2 KB | 2026-01-09 |
| `experiments/test-config-0.json` | 2 KB | 2026-01-09 |
| `experiments/strategy-catalog.json` | 26 KB | 2026-01-09 |
| `experiments/experiment-16581/config.json` | 2 KB | 2026-01-09 |
| `experiments/experiment-16576/config.json` | 2 KB | 2026-01-09 |

## 📝 README

```
# 🚀 Profit Radar IO - Backtest-as-a-Service

Retail-friendly платформа для створення і тестування торгових стратегій з реальним backtest движком ProfitRadar.

---

## 📖 Швидкий старт

```bash
npm install
npm start
# Server: http://localhost:3000
```

**Документація:**
- 📘 [Quick Start Guide](QUICK_START.md) - швидкий старт
- 📋 [Config JSON Rules](CONFIG_JSON_RULES.md) - правила config
- 🎯 [BAAS Ideology](BAAS_IDEOLOGY.md) - повна ідеологія
- 🔧 [Developer Guide](DEVELOPER.md) - для розробників

---

## ✅ Що працює зараз

### Backend
- ✅ Auth Service (cookie-based)
- ✅ Backtest Controller (run-config, status, results)
- ✅ Config Mapper (UI → scalping-pnl format)
- ✅ Integration з admin-dev API

### Протестовано
- Multi-asset mode (16539, 16542) ✅
- SAME ASSET mode (16546) ✅

---

## 📋 Структура проекту

```
profit-radar-io/
├── controllers/        # API контролери
│   └── backtest.js    # Backtest orchestration
├── services/          # Бізнес логіка
│   ├── auth/         # Авторизація
│   └── backtest/     # Config mapping
├── routes/           # Express routes
├── www/              # Frontend
│   ├── css/
│   ├── js/
│   └── index.html
└── docs/             # Додаткова документація
```

---

## 🎯 Roadmap

### Phase 1: Simple Backtest ✅
- [x] Backend API
- [x] Config mapper
- [x] Auth integration
- [ ] UI integration

### Phase 2: Random Search (TODO)
- [ ] Batch backtest endpoint
- [ ] Strategy variations
- [ ] Results ranking

### Phase 3: Genetic Algorithm (TODO)
- [ ] Darvi
```
