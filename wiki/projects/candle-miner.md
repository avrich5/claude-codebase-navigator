# candle-miner

**Категория:** 📦 [Uncategorized](../categories/uncategorized.md)
**Статус:** 🟠 dormant
**Путь:** `/Users/andriy/gitlab-prod/candle-miner`

## 📊 Git

- **Branch:** `master`
- **Коммитов:** 25
- **Последний:** 2025-10-28
- **Сообщение:** Add backticks to ClickHouse table names for special character support
- **За 30 дней:** 0 коммитов

### Последние коммиты

- `2025-10-28` Add backticks to ClickHouse table names for special character support
- `2024-06-27` added symbols list update every hour (binance futures)
- `2024-05-03` fix spot minner due to binance config change
- `2024-05-03` update creds
- `2024-05-03` update cd

## 🛠 Tech Stack

- **Languages:** JavaScript/TypeScript
- **Tools:** Docker, npm

## 📁 Files (22 indexed)

### Code (15 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `run.js` | 618 B | 2026-02-28 |
| `logger.js` | 490 B | 2026-02-28 |
| `kraken_futures/kraken.js` | 743 B | 2026-02-28 |
| `kraken_futures/index.js` | 5 KB | 2026-02-28 |
| `kraken_futures/db.js` | 3 KB | 2026-02-28 |
| `ftx_futures/index.js` | 5 KB | 2026-02-28 |
| `ftx_futures/ftx.js` | 818 B | 2026-02-28 |
| `ftx_futures/db.js` | 3 KB | 2026-02-28 |
| `deploy.sh` | 1 KB | 2026-02-28 |
| `binance_spot/index.js` | 4 KB | 2026-02-28 |
| `binance_spot/db.js` | 3 KB | 2026-02-28 |
| `binance_spot/binance.js` | 662 B | 2026-02-28 |
| `binance_futures/index.js` | 4 KB | 2026-02-28 |
| `binance_futures/db.js` | 3 KB | 2026-02-28 |
| `binance_futures/binance.js` | 625 B | 2026-02-28 |

### Docs (1 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `readme.md` | 804 B | 2026-02-28 |

### Config (6 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `package.json` | 360 B | 2026-02-28 |
| `package-lock.json` | 9 KB | 2026-02-28 |
| `kraken_futures/assets.json` | 530 B | 2026-02-28 |
| `ftx_futures/assets.json` | 530 B | 2026-02-28 |
| `binance_spot/assets.json` | 1 KB | 2026-02-28 |
| `.gitlab-ci.yml` | 1001 B | 2026-02-28 |

## 📝 README

```
## One minute candles miner (FTX + BINANCE) futures.


For start miner instance: `node run.js`<br />
Data will be saving into tables like: `db_candles_{market}.tbl_{symbol}`


## ENVIRONMENTAL VARIABLES
| PARAM | CH_USER | CH_PORT | CH_HOST | CH_PASSWORD | MARKET |
| :---: | :---: | :---: | :---: | :---: | :---: | 
| Required | yes | yes | yes | yes | yes |
| NOTE | DB user name | DB port | DB url | DB password | Market name to save candles (FTX_FUTURES / BINANCE_FUTURES / BINANCE_SPOT) |

## Project code structure 
1) File `run.js` is main file to start project.
2) Folder `markets` with needed code to make all robots check.
3) Eaxh market from `markets` has few files
    - `db.js` for working with database
    - `index.js` main logic 
    - `{market}.js` for connecting to market-api/bot-api


```
