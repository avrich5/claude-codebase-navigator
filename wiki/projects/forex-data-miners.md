# forex-data-miners

**Категория:** 📦 [Uncategorized](../categories/uncategorized.md)
**Статус:** 🟡 recent
**Путь:** `/Users/andriy/gitlab-prod/forex-data-miners`

## 📊 Git

- **Branch:** `main`
- **Коммитов:** 1
- **Последний:** 2026-01-13
- **Сообщение:** Initial commit: Forex data miners
- **За 30 дней:** 0 коммитов

### Последние коммиты

- `2026-01-13` Initial commit: Forex data miners

## 🛠 Tech Stack

- **Languages:** JavaScript/TypeScript
- **Tools:** npm

## 📁 Files (7 indexed)

### Docs (3 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `secret/README.md` | 1 KB | 2026-02-28 |
| `README.md` | 7 KB | 2026-02-28 |

### Config (1 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `package.json` | 543 B | 2026-02-28 |

### Code (3 files, 0.1 MB)

| File | Size | Modified |
|------|------|----------|
| `tools/sse_miner_v2.js` | 32 KB | 2026-02-28 |
| `tools/dukascopy_downloader.js` | 24 KB | 2026-02-28 |
| `secret/index.js` | 499 B | 2026-02-28 |

## 📝 README

```
# Forex Data Miners

Real-time and historical forex data collection system with dual-source architecture:
- **Dukascopy** - historical tick data (from 2020+, free API)
- **Exante SSE** - real-time streaming data (~100-200ms lag)

Unified ClickHouse views automatically merge both sources for seamless querying.

## Quick Start

### 1. Install Dependencies
```bash
npm install
```

### 2. Configure Environment
```bash
cp .env.example .env
# Edit .env - add your credentials:
# - ClickHouse connection (CLICKHOUSE_HOST, CLICKHOUSE_USER, etc.)
# - Exante API keys (EXANTE_CLIENT_ID, EXANTE_APPLICATION_ID, EXANTE_SHARED_SECRET)
# - Symbol lists (SYMBOLS for SSE, DUKA_SYMBOLS for historical)
```

See [.env.example](.env.example) for full configuration options.

### 3. Run Data Miners

#### Option A: Production Setup (Recommended)

**1. Start SSE Miner** (real-time data, runs continuously):
```bash
# In terminal 1 or screen session
node tools/sse_miner_v2.js
```

**2. Start Dukascopy in Daemon Mode** (hourly checks):
```bash
# In terminal 2 or screen session
DAEMON=1 node tools/dukascopy_downloader.js
```

Both processes will:
- Create required ClickHouse tables
- Download missing historical data
- Keep data up-to-date automatically

#### Option B: Manual Backfill

**Download historical data once** (for new symbols or gaps):
```bash
# Downloads all missing data and exits
node tools/dukascopy_downloader.js
```

Then start SSE miner for real-time updates.

### 4. Verify Data

Check that da
```
