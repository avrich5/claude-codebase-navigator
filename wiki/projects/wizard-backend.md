# wizard-backend

**Категория:** 📦 [Uncategorized](../categories/uncategorized.md)
**Статус:** 🔴 archived
**Путь:** `/Users/andriy/gitlab-prod/wizard-backend`

## 📊 Git

- **Branch:** `master`
- **Коммитов:** 41
- **Последний:** 2024-04-09
- **Сообщение:** FS-65 (3 new commands)
- **За 30 дней:** 0 коммитов

### Последние коммиты

- `2024-04-09` FS-65 (3 new commands)
- `2024-02-08` pivot filter change command
- `2024-01-09` Merge branch 'master' of ssh://git.forvest.software/frv/wizard-backend
- `2024-01-09` changed replace pause trigger command logic
- `2024-01-08` fix sa name

## 🛠 Tech Stack

- **Languages:** JavaScript/TypeScript
- **Tools:** Docker, npm

## 📁 Files (9 indexed)

### Code (5 files, 0.1 MB)

| File | Size | Modified |
|------|------|----------|
| `queries/wizard_operations.sql` | 426 B | 2026-02-28 |
| `queries/wizard_logs.sql` | 303 B | 2026-02-28 |
| `index.js` | 71 KB | 2026-02-28 |
| `deploy.sh` | 996 B | 2026-02-28 |
| `connectors/DB.js` | 9 KB | 2026-02-28 |

### Docs (1 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `readme.md` | 1 KB | 2026-02-28 |

### Config (3 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `package.json` | 343 B | 2026-02-28 |
| `package-lock.json` | 45 KB | 2026-02-28 |
| `.gitlab-ci.yml` | 2 KB | 2026-02-28 |

## 📝 README

```
# Backend Wizard

### ENVS
###### PORT=
###### DB_USER=
###### DB_PORT=
###### DB_HOST=
###### DB_PASSWORD=
###### IS_DEV=


### To start running comand send POST request to /set_commands with JSON body
###
### Command examples:

##### Close only
```javascript
This command will set close-only false (unpause) for binance_dev account EOS,APE assets. And set close-only true (pause) for binance_dev_2 account XRP asset.
[
    {
        "account" : "binance_dev",
        "symbols" : ["EOS","APE"],
        "changes" : [["close_only",false]]
    },
    {
        "account" : "binance_dev_2",
        "symbols" : ["XRP"],
        "changes" : [["close_only",true]]
    }
]
```

##### Start orders 

```javascript
This command will set start order long 100$ for binance_dev account EOS,APE assets. And set start order short 20$ for binance_dev_2 account XRP asset.
[
    {
        "account" : "binance_dev",
        "symbols" : ["EOS","APE"],
        "changes" : [["start_order_usd_long",100]]
    },
    {
        "account" : "binance_dev_2",
        "symbols" : ["XRP"],
        "changes" : [["start_order_usd_short",20]]
    }
]
```


```
