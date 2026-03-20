# shark-monitoring

**Категория:** 📦 [Uncategorized](../categories/uncategorized.md)
**Статус:** 🟡 recent
**Путь:** `/Users/andriy/gitlab-prod/shark-monitoring`

## 📊 Git

- **Branch:** `master`
- **Коммитов:** 134
- **Последний:** 2025-12-28
- **Сообщение:** added autocorrection for new binance algoorder placing error:'Send status unknown; execution status unknown'
- **За 30 дней:** 0 коммитов

### Последние коммиты

- `2025-12-28` added autocorrection for new binance algoorder placing error:'Send status unknown; execution status unknown'
- `2025-04-09` fix balance check
- `2025-04-08` fix eu acc balance
- `2025-03-14` fixed eu mode account pnl and balance calculation
- `2024-10-30` fixed some errors

## 🛠 Tech Stack

- **Languages:** JavaScript/TypeScript
- **Tools:** Docker, npm

## 📁 Files (20 indexed)

### Config (7 files, 0.1 MB)

| File | Size | Modified |
|------|------|----------|
| `package.json` | 414 B | 2026-02-28 |
| `package-lock.json` | 43 KB | 2026-02-28 |
| `default_presicion_OKX_FUTURES.json` | 26 KB | 2026-02-28 |
| `default_presicion_KRAKEN_FUTURES.json` | 13 KB | 2026-02-28 |
| `default_presicion_BINANCE_FUTURES.json` | 57 KB | 2026-02-28 |
| `.gitlab-ci.yml` | 3 KB | 2026-02-28 |
| `.eslintrc.json` | 299 B | 2026-02-28 |

### Code (12 files, 0.3 MB)

| File | Size | Modified |
|------|------|----------|
| `run.js` | 651 B | 2026-02-28 |
| `logger.js` | 490 B | 2026-02-28 |
| `deploy.sh` | 1 KB | 2026-02-28 |

### Docs (1 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `readme.md` | 1 KB | 2026-02-28 |

## 📝 README

```
## SharkBot - Monitoring

For start monitoring instance: `node run.js`<br />

## ENVIRONMENTAL VARIABLES
| PARAM | DB_USER | DB_PORT | DB_HOST | DB_PASSWORD | MARKET | WEBHOOK | WEBHOOK2 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | 
| Required | yes | yes | yes | yes | yes | yes | yes | 
| NOTE | DB user name | DB port | DB url | DB password | Market name to check accounts | webhook to channel1 | webhook to channel2 |

## Project code structure 
1) File `run.js` is main file to start project.
2) Folder `markets` with needed code to make all robots check.
3) Eaсh market from `markets` has few files
    - `db.js` for working with database
    - `index.js` main logic 
    - `{market}.js` for connecting to market-api/bot-api


## Main functions 
1) Check if bot’s api is available for queries.
2) Check if market’s rest-api is available for queries.
3) Check if current negative PNL on market is less than 50% of account balance.
4) Check db-saved errors for last 5 minutes.
5) Check if asset - websockets have no delays in data receiving from market.
6) Compare all market position parameters (amount of poses, sizes, average prices, sides) with internal trading-bot information about these positions.
7) Compare all market orders parameters (amount of orders, sizes, prices) with internal trading-bot information about these orders.
8) Check api keys validity (if 7 days left to their disable) than signal slack.


```
