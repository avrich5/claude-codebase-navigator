# llm-council

**Категория:** 🧠 [LLM & AI Training](../categories/llm_ai_training.md)
**Статус:** 🟠 dormant
**Путь:** `/Users/andriy/VisualStudio/llm-council`

## 📊 Git

- **Branch:** `master`
- **Коммитов:** 5
- **Последний:** 2025-11-22
- **Сообщение:** readme tweaks
- **За 30 дней:** 0 коммитов

### Последние коммиты

- `2025-11-22` readme tweaks
- `2025-11-22` add vibe code warning
- `2025-11-22` a bit more progressive update and single turn
- `2025-11-22` Label maker add
- `2025-11-22` v0

## 🛠 Tech Stack

- **Languages:** Python

## 📁 Files (38 indexed)

### Config (16 files, 0.2 MB)

| File | Size | Modified |
|------|------|----------|
| `frontend/package-lock.json` | 133 KB | 2025-11-25 |
| `.vscode/tasks.json` | 3 KB | 2025-11-25 |
| `pyrightconfig.json` | 432 B | 2025-11-25 |
| `.vscode/extensions.json` | 615 B | 2025-11-25 |
| `.vscode/launch.json` | 2 KB | 2025-11-25 |
| `.vscode/settings.json` | 1 KB | 2025-11-25 |
| `pyproject.toml` | 278 B | 2025-11-25 |
| `frontend/package.json` | 637 B | 2025-11-25 |

### Docs (4 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `frontend/index.html` | 357 B | 2025-11-25 |
| `frontend/README.md` | 1 KB | 2025-11-25 |
| `README.md` | 3 KB | 2025-11-25 |
| `CLAUDE.md` | 7 KB | 2025-11-25 |

### Code (18 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `backend/config.py` | 688 B | 2025-11-25 |
| `backend/openrouter.py` | 3 KB | 2025-11-25 |
| `backend/council.py` | 10 KB | 2025-11-25 |
| `start.sh` | 625 B | 2025-11-25 |
| `main.py` | 89 B | 2025-11-25 |
| `frontend/vite.config.js` | 161 B | 2025-11-25 |
| `frontend/src/main.jsx` | 229 B | 2025-11-25 |
| `frontend/src/App.jsx` | 6 KB | 2025-11-25 |
| `frontend/eslint.config.js` | 758 B | 2025-11-25 |
| `backend/storage.py` | 4 KB | 2025-11-25 |
| `backend/main.py` | 7 KB | 2025-11-25 |
| `backend/__init__.py` | 35 B | 2025-11-25 |

## 📝 README

```
# LLM Council

![llmcouncil](header.jpg)

The idea of this repo is that instead of asking a question to your favorite LLM provider (e.g. OpenAI GPT 5.1, Google Gemini 3.0 Pro, Anthropic Claude Sonnet 4.5, xAI Grok 4, eg.c), you can group them into your "LLM Council". This repo is a simple, local web app that essentially looks like ChatGPT except it uses OpenRouter to send your query to multiple LLMs, it then asks them to review and rank each other's work, and finally a Chairman LLM produces the final response.

In a bit more detail, here is what happens when you submit a query:

1. **Stage 1: First opinions**. The user query is given to all LLMs individually, and the responses are collected. The individual responses are shown in a "tab view", so that the user can inspect them all one by one.
2. **Stage 2: Review**. Each individual LLM is given the responses of the other LLMs. Under the hood, the LLM identities are anonymized so that the LLM can't play favorites when judging their outputs. The LLM is asked to rank them in accuracy and insight.
3. **Stage 3: Final response**. The designated Chairman of the LLM Council takes all of the model's responses and compiles them into a single final answer that is presented to the user.

## Vibe Code Alert

This project was 99% vibe coded as a fun Saturday hack because I wanted to explore and evaluate a number of LLMs side by side in the process of [reading books together with LLMs](https://x.com/karpathy/status/1990577951671509438). It'
```
