# simple-evaluation-framework

**Категория:** 🧠 [LLM & AI Training](../categories/llm_ai_training.md)
**Статус:** 🟢 active
**Путь:** `/Users/andriy/gitlab-prod/simple-evaluation-framework`

## 📊 Git

- **Branch:** `main`
- **Коммитов:** 2
- **Последний:** 2026-02-19
- **Сообщение:** first results added
- **За 30 дней:** 2 коммитов

### Последние коммиты

- `2026-02-19` first results added
- `2026-02-19` initial commit

## 🛠 Tech Stack

- **Languages:** Python
- **Tools:** pip

## 📁 Files (9 indexed)

### Docs (3 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `requirements.txt` | 50 B | 2026-02-28 |
| `docs/deepval-lib.md` | 5 KB | 2026-02-28 |
| `README.md` | 4 KB | 2026-02-28 |

### Code (1 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `evaluate.py` | 18 KB | 2026-02-28 |

### Config (3 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `questions/eval_questions.json` | 8 KB | 2026-02-28 |

### Data (2 files, 0.0 MB)

## 📝 README

```
# Adviser Model Evaluation Framework

Evaluates generation quality of trading strategy adviser models by sending fixed questions through the REST API and scoring text responses with **DeepEval** (LLM-as-judge via GPT-4o).

RAG, semantic search, and retrieval are identical across runs — only the generation model differs.

## Metrics

| Metric | Type | What it measures |
|--------|------|-----------------|
| Answer Relevancy | DeepEval built-in | Does the response actually address the question? |
| Reasoning Quality | GEval | Does it explain WHY, not just WHAT? |
| Correctness | GEval | Are numbers and facts plausible, no hallucinations? |
| Actionability | GEval | Can a trader act on this response? |
| Domain Specificity | GEval | Uses system terms (fitness, tier, Grid Trap, mechanism...)? |

**Final score** = average of all 5 metric scores (0.0 – 1.0)

**Cost**: ~$0.35–0.40 per full run (27 questions × 5 metrics via GPT-4o)

## Setup

```bash
# 1. Create virtualenv
python -m venv venv
source venv/bin/activate        # Linux/Mac
# venv\Scripts\activate         # Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment
cp .env.example .env
# Edit .env — set ADVISER_URL and OPENAI_API_KEY
```

Get your OpenAI API key at: https://platform.openai.com/api-keys

## Environment variables

```env
ADVISER_URL=http://localhost:8000   # your adviser API
OPENAI_API_KEY=sk-...               # used by DeepEval judge
JUDGE_MODEL=gpt-4o                  #
```
