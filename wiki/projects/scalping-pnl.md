# scalping-pnl

**Категория:** 🚀 [ProfitRadar Platform](../categories/profitradar_platform.md)
**Статус:** 🟡 recent
**Путь:** `/Users/andriy/gitlab-prod/scalping-pnl`

## 📊 Git

- **Branch:** `master`
- **Коммитов:** 853
- **Последний:** 2026-02-06
- **Сообщение:** fixed wrong indicator file passes after using all cpus
- **За 30 дней:** 0 коммитов

### Последние коммиты

- `2026-02-06` fixed wrong indicator file passes after using all cpus
- `2026-02-06` full cpu utilisation. logs optimisation
- `2026-02-06` Calc indicators before btuteforce
- `2026-02-03` added sharpe ratio for bruteforces
- `2026-02-02` fixed brutes calcculation without indicators. speed improvements without indicators x2. added sharp ratio to brute results.

## 🛠 Tech Stack

- **Languages:** JavaScript/TypeScript
- **Tools:** Docker, npm

## 📁 Files (82 indexed)

### Config (21 files, 0.3 MB)

| File | Size | Modified |
|------|------|----------|
| `package.json` | 569 B | 2026-02-28 |
| `package-lock.json` | 118 KB | 2026-02-28 |
| `indicators_strat/package.json` | 409 B | 2026-02-28 |
| `indicators_strat/package-lock.json` | 36 KB | 2026-02-28 |
| `docker-compose.yaml` | 1 KB | 2026-02-28 |
| `default_presicion.json` | 117 KB | 2026-02-28 |
| `darvin/config/config.json` | 821 B | 2026-02-28 |
| `config_examples/portfolio.json` | 399 B | 2026-02-28 |
| `config_examples/multi_configs.json` | 2 KB | 2026-02-28 |
| `config_examples/default.json` | 1 KB | 2026-02-28 |
| `config_examples/brute_inds_fitness.json` | 2 KB | 2026-02-28 |
| `config_examples/brute_indicators_volatility.json` | 2 KB | 2026-02-28 |
| `config_examples/brute_indicators_sync_tf.json` | 2 KB | 2026-02-28 |
| `config_examples/brute_indicators_16ksettings_4assets.json` | 3 KB | 2026-02-28 |
| `config_examples/brute_generate_munations.json` | 2 KB | 2026-02-28 |

### Code (55 files, 2.4 MB)

| File | Size | Modified |
|------|------|----------|
| `sanbox.js` | 9 KB | 2026-02-28 |
| `queries/get_dtb4wk.sql` | 179 B | 2026-02-28 |
| `queries/get_daily_gap.sql` | 3 KB | 2026-02-28 |
| `queries/get_configs_debug.sql` | 250 B | 2026-02-28 |
| `queries/get_configs.sql` | 108 B | 2026-02-28 |
| `indicators_strat/indicators.js` | 1 KB | 2026-02-28 |
| `indicators_strat/index.js` | 65 KB | 2026-02-28 |
| `indicators_strat/db.js` | 2 KB | 2026-02-28 |
| `index.js` | 175 KB | 2026-02-28 |
| `extract_folders.js` | 703 B | 2026-02-28 |
| `deploy.sh` | 49 B | 2026-02-28 |
| `darvin/queries/save_accounts_main_table_raw.sql` | 7 KB | 2026-02-28 |
| `darvin/queries/save_accounts_main_table_all.sql` | 2 KB | 2026-02-28 |
| `darvin/queries/save_accounts_main_table.sql` | 709 B | 2026-02-28 |
| `darvin/queries/save_accounts_configs_raw.sql` | 1 KB | 2026-02-28 |

### Docs (5 files, 0.1 MB)

| File | Size | Modified |
|------|------|----------|
| `readme.md` | 12 KB | 2026-02-28 |
| `darvin/readme_old.md` | 12 KB | 2026-02-28 |
| `darvin/readme_new.md` | 7 KB | 2026-02-28 |
| `darvin/readme.md` | 21 KB | 2026-02-28 |
| `darvin/r.md` | 1 KB | 2026-02-28 |

### Data (1 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `totals-report.csv` | 873 B | 2026-02-28 |

## 📝 README

```
# Scalping Back Testing

##### Результаты пишутся в папку results и тоталы с конфигами дополнительно в таблицах БД.


## Режимы работы :
- default. Классический режим работы, который считает пнл для каждого из заданных ассетов и режимов работы (0,1,2). Тотал результаты записываются в таблицу БД db_scalping_backtests.tbl_run_results. На файловой системе результат имеет папку логов (сделки), pnl (поминутный пнл) , take_profits (статистика по тейкпрофитам) total.csv (агрегированные результаты) и config.json (изначальные настройки). Файлы логов и пнл имеют такие названия CRVUSDT_2_0.csv это означает что это прогон монеты CRVUSDT в 2 режиме работы на 0 интервале (если их несколько то будут файлы CRVUSDT_2_0, CRVUSDT_2_1, CRVUSDT_2_2 .... )
- portfolio. Режим просчетов пнл портфеля (несколько монет одновременно играют). На файловой системе всё тоже самое как и в default режиме, только добавляется файл balance с общим пнл и в total.csv записывается 1 строчка - общий результат. 
- multi_configs. Такой же режим как и дефолтный, только на вход ему подаются n готовых сеток. Тоталы в бд таблице db_scalping_backtests.tbl_multiconfig_run_results. В results/id появятся папки 1 2 3 ... это номер сетки в каждой из них структура как в дефолтном конфиге. Доступна возможность задать монету для каждой сетки (в секцию парамс добавляем "symbol" : "XRPUSDT").
##### Примеры конфигов лежат в папке config_examples.


## API

1) `POST http://localhost:8080/set_config`
Cохраняет конфиг в системме и присв
```
