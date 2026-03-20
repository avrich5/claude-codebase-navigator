# llm-cost-tracker

**Категория:** 🧠 [LLM & AI Training](../categories/llm_ai_training.md)
**Статус:** 📁 no-git
**Путь:** `/Users/andriy/VisualStudio/llm-cost-tracker`

## 🛠 Tech Stack

- **Languages:** Python
- **Frameworks:** FastAPI
- **Tools:** pip

## 📁 Files (22 indexed)

### Docs (3 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `README.md` | 1 KB | 2026-02-13 |
| `requirements.txt` | 85 B | 2026-02-13 |

### Config (5 files, 0.1 MB)

| File | Size | Modified |
|------|------|----------|
| `recent_requests.json` | 2 KB | 2026-02-14 |
| `billing_data/anthropic_usage_2026.json` | 11 KB | 2026-02-14 |
| `billing_data/anthropic_costs_2026.json` | 9 KB | 2026-02-14 |
| `billing_data/openai_usage_2026.json` | 45 KB | 2026-02-14 |
| `billing_data/openai_costs_2026.json` | 84 KB | 2026-02-14 |

### Code (10 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `app/proxy.py` | 6 KB | 2026-02-14 |
| `app/database.py` | 7 KB | 2026-02-14 |
| `fetch_billing_2026.py` | 3 KB | 2026-02-14 |
| `app/billing.py` | 6 KB | 2026-02-14 |
| `seed_demo.py` | 2 KB | 2026-02-13 |
| `run.sh` | 156 B | 2026-02-13 |
| `app/main.py` | 607 B | 2026-02-13 |
| `app/dashboard.py` | 2 KB | 2026-02-13 |
| `app/pricing.py` | 2 KB | 2026-02-13 |
| `app/__init__.py` | 0 B | 2026-02-13 |

### Data (4 files, 0.1 MB)

| File | Size | Modified |
|------|------|----------|
| `llm_tracker.db` | 40 KB | 2026-02-14 |
| `data/cost_2026-01-01_2026-01-31.csv` | 5 KB | 2026-02-13 |
| `data/cost_2026-02-01_2026-02-13.csv` | 2 KB | 2026-02-13 |
| `data/completions_usage_2026-01-14_2026-02-13.csv` | 9 KB | 2026-02-13 |

## 📝 README

```
# LLM Cost Tracker

Internal microservice for tracking OpenAI / Anthropic API usage across company projects.

## Quick Start

```bash
cp .env.example .env
# fill in your API keys
pip install -r requirements.txt
chmod +x run.sh
./run.sh
```

Dashboard: http://localhost:8100/dashboard/

## How it works

Your projects send requests through this proxy instead of directly to OpenAI/Anthropic.
The proxy forwards requests transparently, logs token usage + cost, and shows it on the dashboard.

## Usage from projects

Instead of `https://api.openai.com/v1/chat/completions`, use:

```
POST http://localhost:8100/api/v1/openai/v1/chat/completions
Header: x-api-key: lt_<your_project_key>
```

For Anthropic:
```
POST http://localhost:8100/api/v1/anthropic/v1/messages
Header: x-api-key: lt_<your_project_key>
```

Request body stays exactly the same as the native API.

## Create a project

```bash
curl -X POST "http://localhost:8100/dashboard/api/projects?name=profit-radar"
```

Returns an API key — save it.

## API Endpoints

- `GET /dashboard/` — HTML dashboard
- `GET /dashboard/api/summary?days=30` — KPI summary
- `GET /dashboard/api/by-project?days=30` — cost breakdown by project
- `GET /dashboard/api/by-model?days=30` — cost breakdown by model
- `GET /dashboard/api/daily?days=30` — daily cost timeseries
- `GET /dashboard/api/recent?limit=50` — recent requests log

```
