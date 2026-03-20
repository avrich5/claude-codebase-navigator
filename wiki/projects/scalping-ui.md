# scalping-ui

**Категория:** 🚀 [ProfitRadar Platform](../categories/profitradar_platform.md)
**Статус:** 🟡 recent
**Путь:** `/Users/andriy/gitlab-prod/scalping-ui`

## 📊 Git

- **Branch:** `development`
- **Коммитов:** 2084
- **Последний:** 2026-01-15
- **Сообщение:** MINOR FIX; optima. symbol
- **За 30 дней:** 0 коммитов

### Последние коммиты

- `2026-01-15` MINOR FIX; optima. symbol
- `2025-12-26` Minor Fix. get assets from system.tables
- `2025-12-22` run_compare
- `2025-12-10` Exante Aliases
- `2025-12-08` config.market in run()

## 🛠 Tech Stack

- **Languages:** JavaScript/TypeScript
- **Tools:** Docker, npm

## 📁 Files (277 indexed)

### Code (131 files, 3.9 MB)

| File | Size | Modified |
|------|------|----------|
| `www/js/app.js` | 7 KB | 2026-02-28 |
| `utilities/run.sh` | 235 B | 2026-02-28 |
| `utilities/crawler.js` | 3 KB | 2026-02-28 |
| `routes/index.js` | 9 KB | 2026-02-28 |
| `queries/set_monitoring_logs.sql` | 322 B | 2026-02-28 |
| `queries/set_admin_comment.sql` | 250 B | 2026-02-28 |
| `queries/insert_shark_index.sql` | 47 B | 2026-02-28 |
| `queries/insert_kpi_res.sql` | 46 B | 2026-02-28 |
| `queries/insert_crypto30.sql` | 67 B | 2026-02-28 |
| `queries/insert_admin_comment.sql` | 50 B | 2026-02-28 |
| `queries/info_un_pnl.sql` | 828 B | 2026-02-28 |
| `queries/info_total.sql` | 792 B | 2026-02-28 |
| `queries/info_profit24_net_profit.sql` | 750 B | 2026-02-28 |
| `queries/info_pnl_by_assets.sql` | 484 B | 2026-02-28 |
| `queries/info_dfk_components.sql` | 255 B | 2026-02-28 |

### Docs (136 files, 7.6 MB)

| File | Size | Modified |
|------|------|----------|
| `www/setings-test.html` | 141 KB | 2026-02-28 |
| `www/index.html` | 122 KB | 2026-02-28 |
| `www/admin-wizard-popups.html` | 1 KB | 2026-02-28 |
| `www/admin-wizard-panel1.html` | 6 KB | 2026-02-28 |
| `www/admin-wizard-inner_old.html` | 2 KB | 2026-02-28 |
| `www/admin-wizard-inner.html` | 7 KB | 2026-02-28 |
| `www/admin-transaction-history.html` | 87 KB | 2026-02-28 |
| `www/admin-transaction-history-inner.html` | 2 KB | 2026-02-28 |
| `www/admin-shark_index-inner.html` | 4 KB | 2026-02-28 |
| `www/admin-risk-overview-panel1.html` | 6 KB | 2026-02-28 |
| `www/admin-risk-overview-inner.html` | 2 KB | 2026-02-28 |
| `www/admin-position-overview-popups.html` | 885 B | 2026-02-28 |
| `www/admin-position-overview-inner.html` | 2 KB | 2026-02-28 |
| `www/admin-position-inner.html` | 2 KB | 2026-02-28 |
| `www/admin-portfolios-inner.html` | 23 KB | 2026-02-28 |

### Config (7 files, 2.7 MB)

| File | Size | Modified |
|------|------|----------|
| `wizzard_commands_descriptions.json` | 8 KB | 2026-02-28 |
| `package.json` | 895 B | 2026-02-28 |
| `package-lock.json` | 142 KB | 2026-02-28 |
| `.vscode/launch.json` | 510 B | 2026-02-28 |
| `.gitlab-ci.yml` | 19 KB | 2026-02-28 |
| `.eslintrc.json` | 0 B | 2026-02-28 |

### Data (3 files, 0.1 MB)

## 📝 README

```
## admin panel v2

### Aпрувы балк изменений
1) self-approve accounts. Владельцы аккаунтов, которые могут апиувить изменения на своем аккаунте сами. Эти аккаунты прописываются пользователю в таблице db_config.tbl_admin_users колонка - self_approve_accounts. На момент 07.07.2023 Andriy & Evgen могут сами апрувить [dc1, t1, t2, f1], Dima - [d1]
2) Если это не пункт 1 то остальные юзеры делятся на группы, эти настройки прописаны в таблице db_config.tbl_bulk_approve_settings. У каждой группы есть имя, id юзеров, которые в ней состоят. А также approve_group_name  имя группы, юзер из которой должен подписать запрос. Такая система достаточно гибкая и позволяет добавлять любые группы и юзеров и контролировать их пермишены. В группе mmi - Andriy & Evgen , в группе dfk - Valera & Dima , * - все остальные, кого нету ни в какой группе. 
```` javascript
Данные из таблицы апрувов на 07.07.2023
id      name            users                   approve_group_name

1	    mmi	            ['3','4']	            dfk
2	    dfk	            ['6','7']	            mmi
3	    subadmins	    ['2','5','8','9']	    dfk
4	    other	        ['*']	                mmi
````
Алгоритм проверяет есть ли человек, который подтверждает запрос в группе которая имеет право подтверждать запросы человека, который создал запрос на балк изменения.
```
