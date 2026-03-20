# shark-bot

**Категория:** 📦 [Uncategorized](../categories/uncategorized.md)
**Статус:** 🟡 recent
**Путь:** `/Users/andriy/gitlab-prod/shark-bot`

## 📊 Git

- **Branch:** `binance-algo-orders`
- **Коммитов:** 803
- **Последний:** 2025-12-23
- **Сообщение:** temporary fix to query openAlgoOrders endpoint (problem is on binance side)
- **За 30 дней:** 0 коммитов

### Последние коммиты

- `2025-12-23` temporary fix to query openAlgoOrders endpoint (problem is on binance side)
- `2025-12-22` fixed sl limit mode with ta strategy combination orders placing. reduced logs.
- `2025-12-14` binance algoorders: fixes after tests, error handling added
- `2025-12-14` feat: migrate conditional orders to Binance Algo Order API
- `2025-11-04` OHLC-loader and SSE-miner tools

## 🛠 Tech Stack

- **Languages:** JavaScript/TypeScript
- **Tools:** Docker, npm

## 📁 Files (105 indexed)

### Code (94 files, 1.5 MB)

| File | Size | Modified |
|------|------|----------|
| `upgrade.sh` | 3 KB | 2026-02-28 |
| `u.sh` | 2 KB | 2026-02-28 |
| `secret/index.js` | 499 B | 2026-02-28 |
| `scripts/get_conf.py` | 6 KB | 2026-02-28 |
| `run.js` | 731 B | 2026-02-28 |
| `remove-test.sh` | 359 B | 2026-02-28 |
| `queries/update.sql` | 64 B | 2026-02-28 |
| `queries/save_tbl_incomes.sql` | 280 B | 2026-02-28 |
| `queries/insert_tbl_incomes_tmp.sql` | 133 B | 2026-02-28 |
| `queries/insert_tbl_incomes.sql` | 129 B | 2026-02-28 |
| `queries/insert_tbl_correct_by_incomes.sql` | 111 B | 2026-02-28 |
| `queries/get_incomes_tss_last_load.sql` | 100 B | 2026-02-28 |
| `queries/get_incomes_ts_start.sql` | 158 B | 2026-02-28 |
| `queries/get_incomes_logs_by_days.sql` | 633 B | 2026-02-28 |
| `queries/get_futures_last_price.sql` | 114 B | 2026-02-28 |

### Docs (2 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `readme.md` | 27 KB | 2026-02-28 |
| `__tests__/readme.md` | 992 B | 2026-02-28 |

### Config (9 files, 0.5 MB)

| File | Size | Modified |
|------|------|----------|
| `package.json` | 1 KB | 2026-02-28 |
| `package-lock.json` | 409 KB | 2026-02-28 |
| `deploy-values/pool-1.yaml` | 334 B | 2026-02-28 |
| `deploy-values/pool-0.yaml` | 307 B | 2026-02-28 |
| `default_presicion.json` | 72 KB | 2026-02-28 |
| `.gitlab/agents/k3shetzner/config.yaml` | 34 B | 2026-02-28 |
| `.gitlab-ci.yml` | 7 KB | 2026-02-28 |
| `.eslintrc.json` | 299 B | 2026-02-28 |

## 📝 README

```
# Scalping v1.0
-----
-----
## To start project "$node run.js"
-----
-----
## ENVIRONMENTAL VARIABLES
| PARAM | DB_USER | DB_PORT | DB_HOST | DB_PASSWORD | ACCOUNT_ID | WEBHOOK  | TG_PRO_NOTIFICATIONS | PROFIT_PART_TO_SPOT | IS_DEV |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Required | yes | yes | yes | yes | yes | yes | no | no | no |
| NOTE | DB user name | DB port | DB url | DB password | Market-Account-Id | Webhook for sending msg to slack | tg notifications format (1/2) | part of profit to save (0-1) | Must be 1 or 0. If 1 than bot will work with dev DB |


## Project code structure 
1) File `run.js` is main file to start project, it starts all process.
2) Directory `controllers` has 3 modules 
  - `info_endpoints.js` - controller for all get-info rest-api endpoints (for admin panel/postman etc)
  - `settings_endpoints.js` - controller for all settings-change rest-api endpoints (for admin panel/postman etc)
  - `terminal_endpoints.js` - controller for all "hand" changes on market (placing orders/transfers etc)
3) Directory connectors has 6 modules  
  - `data_converter.js` - has functions for convert orders/api responces to binance (default for bot) formats
  - `DB.js` - has all functions for DB working
  - `errors_handler.js` - has error handler functions
  - `math_functions.js` - has functions for mathematical operations or grids changes
  - `RSI.js` - has functions for calculating indicators (deprecated)
  - `slack.js` - has f
```
