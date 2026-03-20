# signal-emulator

**Категория:** 📊 [Trading Strategies](../categories/trading_strategies.md)
**Статус:** 🟢 active
**Путь:** `/Users/andriy/gitlab-prod/signal-emulator`

## 📊 Git

- **Branch:** `dev`
- **Коммитов:** 4
- **Последний:** 2026-03-02
- **Сообщение:** chore: stop tracking local Cursor rules
- **За 30 дней:** 4 коммитов

### Последние коммиты

- `2026-03-02` chore: stop tracking local Cursor rules
- `2026-03-02` chore: stop tracking local Cursor rules
- `2026-03-02` feat: integrate indicators service and improve monitoring logs
- `2026-03-02` feat: scaffold signals emulator service with monitoring loop, migrations and docker

## 🛠 Tech Stack

- **Languages:** JavaScript/TypeScript
- **Tools:** Docker, npm

## 📁 Files (24 indexed)

### Config (5 files, 0.1 MB)

| File | Size | Modified |
|------|------|----------|
| `tsconfig.base.json` | 265 B | 2026-03-03 |
| `services/signal-emulator/tsconfig.json` | 138 B | 2026-03-03 |
| `package.json` | 288 B | 2026-03-03 |
| `package-lock.json` | 66 KB | 2026-03-03 |

### Docs (4 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `docs/running.md` | 2 KB | 2026-03-03 |
| `docs/architecture.md` | 910 B | 2026-03-03 |
| `docs/api-signals.md` | 774 B | 2026-03-03 |
| `README.md` | 655 B | 2026-03-03 |

### Code (15 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `services/signal-emulator/src/core/strategies/strategy-config.ts` | 72 B | 2026-03-03 |
| `services/signal-emulator/src/api/config.ts` | 41 B | 2026-03-03 |

## 📝 README

```
Signals Emulator
================

Backend service for real-time strategy monitoring and virtual signal generation.

This repo is **backend-only**. Another service is responsible for exposing generated signals to the frontend.

High-level components:
- Node.js + TypeScript + Express HTTP API
- Strategy monitoring loop (every 1 minute)
- Integrations with ClickHouse (candles) and Indicators Service (TA entries/exits)
- PostgreSQL storage for signals, positions, and P&L

Environment:
- `DATABASE_URL` (preferred, e.g. `postgresql+asyncpg://...`) or `POSTGRES_URL` – the service will normalize this to a `pg`-compatible `postgres://` URL internally.


```
