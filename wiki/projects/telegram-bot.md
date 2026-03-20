# telegram-bot

**Категория:** 📦 [Uncategorized](../categories/uncategorized.md)
**Статус:** 🔴 archived
**Путь:** `/Users/andriy/gitlab-prod/telegram-bot`

## 📊 Git

- **Branch:** `master`
- **Коммитов:** 40
- **Последний:** 2024-01-14
- **Сообщение:** update dev release name
- **За 30 дней:** 0 коммитов

### Последние коммиты

- `2024-01-14` update dev release name
- `2024-01-14` turn back deploy
- `2024-01-13` rm empty string from msg and del msg with no pnl change
- `2023-12-22` some msg changes
- `2023-12-22` Merge branch 'master' of ssh://gita.forvest.software/frv/telegram-bot

## 🛠 Tech Stack

- **Languages:** JavaScript/TypeScript
- **Tools:** Docker, npm

## 📁 Files (7 indexed)

### Code (3 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `logger.js` | 489 B | 2026-02-28 |
| `index.js` | 10 KB | 2026-02-28 |
| `DB.js` | 8 KB | 2026-02-28 |

### Docs (1 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `readme.md` | 1 KB | 2026-02-28 |

### Config (3 files, 0.1 MB)

| File | Size | Modified |
|------|------|----------|
| `package.json` | 393 B | 2026-02-28 |
| `package-lock.json` | 60 KB | 2026-02-28 |
| `.gitlab-ci.yml` | 3 KB | 2026-02-28 |

## 📝 README

```
## Telegram bot for sending notifications for SHARK users
For start bot: `node index.js`<br />

This bot can authenticate user by phone number and send shark-bot notifications to them.
### 1) Start command
![Alt text](/src/start.png?raw=true "Start command")
### 2) Sending phone number
![Alt text](/src/phone_number.jpg?raw=true "Phone number")
### 3) Click on stop notifications button
![Alt text](/src/stop.png?raw=true "Stop")


## Endpoints
### 1) Send message to user.
`POST /send_message`
Body format :
`
    { 
        "msg" : "test123",
        "marketAccount" : 1
    }   
`

## ENVIRONMENTAL VARIABLES
| PARAM | DB_USER | DB_PORT | DB_HOST | DB_PASSWORD | TG_BOT_TOKEN | PORT |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | 
| Required | yes | yes | yes | yes | yes | no | 
| NOTE | DB user name | DB port | DB url | DB password | Telegram bot token | Rest-Api Port (8080 default) |

## Project code structure 
1) File `index.js` is main file to start project. Also it has main bot logic
2) File `DB.js` for working with Database


```
