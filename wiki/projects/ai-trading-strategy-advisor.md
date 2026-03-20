# ai-trading-strategy-advisor

**Категория:** 📊 [Trading Strategies](../categories/trading_strategies.md)
**Статус:** 🟡 recent
**Путь:** `/Users/andriy/VisualStudio/ai-trading-strategy-advisor`

## 📊 Git

- **Branch:** `chyrva_home`
- **Коммитов:** 78
- **Последний:** 2026-02-12
- **Сообщение:** check new pipeline
- **За 30 дней:** 0 коммитов

### Последние коммиты

- `2026-02-12` check new pipeline
- `2026-02-11` fix secret path correct configuration
- `2026-02-11` fix secret path
- `2026-02-11` refactor: migrate session management from files to PostgreSQL with caching
- `2026-02-10` few docs added

## 🛠 Tech Stack

- **Tools:** Docker Compose

## 📁 Files (2897 indexed)

### Docs (27 files, 0.1 MB)

| File | Size | Modified |
|------|------|----------|
| `frontend/index.html` | 538 B | 2026-02-14 |
| `backend/requirements.txt` | 277 B | 2026-02-14 |
| `final_output_v2.txt` | 5 KB | 2026-02-14 |
| `final_output.txt` | 8 KB | 2026-02-14 |
| `orchestrator_output.txt` | 6 KB | 2026-02-14 |
| `helm/ai-trading-strategy-advisor/README.md` | 4 KB | 2026-01-20 |
| `docs/GITLAB_CI.md` | 7 KB | 2026-01-20 |
| `backend/docs/claude/SETUP.md` | 6 KB | 2026-01-20 |
| `docs/LOCAL_DEVELOPMENT.md` | 2 KB | 2026-01-18 |
| `frontend/README.md` | 7 KB | 2026-01-18 |
| `docs/TESTING_GUIDE.md` | 8 KB | 2026-01-18 |
| `docs/README.md` | 1 KB | 2026-01-18 |
| `docs/DOCKER_SETUP_SUMMARY.md` | 10 KB | 2026-01-18 |
| `docs/DOCKER_COMMANDS.md` | 4 KB | 2026-01-18 |
| `backend/docs/LOCAL_SETUP.md` | 4 KB | 2026-01-18 |

### Code (27 files, 0.2 MB)

| File | Size | Modified |
|------|------|----------|
| `backend/app/main.py` | 13 KB | 2026-02-14 |
| `frontend/src/config.ts` | 779 B | 2026-02-14 |
| `frontend/vite.config.ts` | 326 B | 2026-02-14 |
| `run_backend_with_proxy.sh` | 833 B | 2026-02-14 |
| `run_with_proxy.sh` | 325 B | 2026-02-14 |
| `recommended_backtests_data/fetch_templates.py` | 4 KB | 2026-01-21 |
| `recommended_backtests_data/backtest_manager.py` | 21 KB | 2026-01-21 |
| `recommended_backtests_data/run_backtests.py` | 4 KB | 2026-01-20 |
| `recommended_backtests_data/generate_backtest_configs.py` | 7 KB | 2026-01-20 |
| `recommended_backtests_data/fetch_results.py` | 4 KB | 2026-01-20 |
| `frontend/docker-entrypoint.sh` | 720 B | 2026-01-20 |
| `frontend/src/main.tsx` | 230 B | 2026-01-18 |
| `frontend/src/App.tsx` | 2 KB | 2026-01-18 |
| `frontend/eslint.config.js` | 616 B | 2026-01-18 |

### Config (2212 files, 39.3 MB)

| File | Size | Modified |
|------|------|----------|
| `backend/test_data/brute_990/config.json` | 2 KB | 2026-02-14 |
| `backend/test_data/brute_989/config.json` | 2 KB | 2026-02-14 |
| `backend/test_data/brute_987/config.json` | 2 KB | 2026-02-14 |
| `backend/test_data/brute_985/config.json` | 2 KB | 2026-02-14 |
| `backend/test_data/brute_983/config.json` | 2 KB | 2026-02-14 |
| `backend/test_data/brute_978/config.json` | 2 KB | 2026-02-14 |
| `backend/test_data/brute_976/config.json` | 2 KB | 2026-02-14 |
| `backend/test_data/brute_973/config.json` | 2 KB | 2026-02-14 |
| `backend/test_data/brute_972/config.json` | 2 KB | 2026-02-14 |
| `backend/test_data/brute_970/config.json` | 2 KB | 2026-02-14 |
| `backend/test_data/brute_969/config.json` | 2 KB | 2026-02-14 |
| `backend/test_data/brute_968/config.json` | 2 KB | 2026-02-14 |
| `backend/test_data/brute_958/config.json` | 2 KB | 2026-02-14 |
| `backend/test_data/brute_957/config.json` | 2 KB | 2026-02-14 |
| `backend/test_data/brute_956/config.json` | 2 KB | 2026-02-14 |

### Data (631 files, 211.0 MB)

| File | Size | Modified |
|------|------|----------|
| `recommended_backtests_data/remaining_configs.csv` | 22 KB | 2026-01-20 |
| `recommended_backtests_data/recommended_configs - 2.csv` | 26 KB | 2026-01-20 |
| `recommended_backtests_data/check_recommended_configs.csv` | 4 KB | 2026-01-20 |

## 📝 README

```
# AI Orchestrator Full Stack

Complete application for ProfitRadar.io AI Trading Advisor - combines semantic search, RAG retrieval, and GPT synthesis with a modern React frontend.

> **New to the project?** Start here:
> - 🚀 **Run with Docker**: Follow [Quick Start with Docker](#-quick-start-with-docker) below
> - 💻 **Run locally**: See [Local Development Guide](docs/LOCAL_DEVELOPMENT.md)
> - 📚 **Browse all docs**: Check [Documentation Index](docs/README.md)

## 🎯 Overview

This project consists of:
- **Backend**: FastAPI service with semantic search and GPT-4o-mini synthesis
- **Frontend**: React + TypeScript interface with real-time chat

## 🚀 Quick Start with Docker

### Prerequisites
- Docker and Docker Compose installed
- OpenAI API key

### 1. Clone and Configure

```bash
# Copy environment template
cp .env.example .env

# Edit .env and add your OpenAI API key
nano .env  # or use your preferred editor
```

### 2. Start All Services

```bash
# Build and start both frontend and backend
docker-compose up --build

# Or run in detached mode
docker-compose up -d --build
```

### 3. Access the Application

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8005
- **API Documentation**: http://localhost:8005/docs

### 4. Stop Services

```bash
# Stop all services
docker-compose down

# Stop and remove volumes
docker-compose down -v
```

## 📁 Project Structure

```
ai-orchestrator/
├── backend/                     # FastAPI backend service
│   ├── app/
│  
```
