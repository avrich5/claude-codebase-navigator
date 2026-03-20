# smart_sales

**Категория:** 📦 [Uncategorized](../categories/uncategorized.md)
**Статус:** 🟢 active
**Путь:** `/Users/andriy/VisualStudio/smart_sales`

## 📊 Git

- **Branch:** `main`
- **Коммитов:** 42
- **Последний:** 2026-03-19
- **Сообщение:** docs: rewrite README — current state, all UI features, chat, templates, API
- **За 30 дней:** 42 коммитов

### Последние коммиты

- `2026-03-19` docs: rewrite README — current state, all UI features, chat, templates, API
- `2026-03-19` fix: chat race condition + markdown rendering
- `2026-03-19` fix: suggestion chips copy to input only, don't auto-send
- `2026-03-19` fix: chat hang — sync OpenAI stream was blocking async event loop
- `2026-03-19` fix: chat hang + events not visible to model

## 🛠 Tech Stack

- **Languages:** Python
- **Frameworks:** FastAPI, NumPy, OpenAI API, Pandas
- **Tools:** pip

## 📁 Files (49 indexed)

### Docs (34 files, 3.2 MB)

| File | Size | Modified |
|------|------|----------|
| `README.md` | 11 KB | 2026-03-19 |
| `docs/MASTER_PLAN.md` | 8 KB | 2026-03-19 |
| `docs/claude_code_brief.md` | 21 KB | 2026-03-19 |
| `prompts/prompt_chat.md` | 6 KB | 2026-03-19 |
| `docs/chat_spec.md` | 7 KB | 2026-03-19 |
| `prompts/prompt_llm_agents_en.md` | 5 KB | 2026-03-19 |
| `docs/pitch_deck.html` | 321 KB | 2026-03-18 |
| `docs/demo_guide_final.html` | 604 KB | 2026-03-18 |
| `docs/presentation.html` | 493 KB | 2026-03-18 |
| `docs/one_pager.html` | 113 KB | 2026-03-18 |
| `docs/next_chat_brief.md` | 3 KB | 2026-03-17 |
| `docs/demo_guide.html` | 845 KB | 2026-03-17 |
| `docs/deploy.md` | 5 KB | 2026-03-17 |
| `docs/data_pipeline.md` | 6 KB | 2026-03-17 |
| `docs/ROX -> Smart Sales.txt` | 185 KB | 2026-03-17 |

### Code (11 files, 0.1 MB)

| File | Size | Modified |
|------|------|----------|
| `app/main.py` | 32 KB | 2026-03-19 |
| `deploy.sh` | 2 KB | 2026-03-19 |
| `src/llm_pipeline.py` | 26 KB | 2026-03-19 |
| `src/generate_v2.py` | 18 KB | 2026-03-17 |
| `src/data_guard.py` | 12 KB | 2026-03-17 |
| `src/upsert_h2.py` | 2 KB | 2026-03-17 |
| `app/__init__.py` | 14 B | 2026-03-17 |
| `src/pattern_library.py` | 16 KB | 2026-03-17 |
| `src/parser_en.py` | 22 KB | 2026-03-17 |
| `src/generate_experts.py` | 4 KB | 2026-03-16 |
| `src/causal_rules.py` | 14 KB | 2026-03-16 |

### Data (2 files, 0.3 MB)

| File | Size | Modified |
|------|------|----------|
| `data/dataset3_canonical.db` | 252 KB | 2026-03-17 |

### Config (2 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `data/.data_guard.json` | 587 B | 2026-03-19 |
| `data/run_manifest.json` | 12 KB | 2026-03-17 |

## 📝 README

```
# Smart Sales — B2B Account Intelligence

> Predicts CHURN / RENEWAL / EXPANSION using only events before the `cut_date`.
> The model never sees the future. Every decision has an audit trail.

**Live demo:** https://smart-sales.dataintelligencelab.com
**Local dev:** `uvicorn app.main:app --port 8765` → http://localhost:8765

---

## What it does

Three sales advisors (Sceptic, Analyst, Contextualist) each analyse the same account data through their own cognitive lens. Smart Sales reads everything simultaneously, corrects each advisor with specific evidence, and recommends a concrete action.

```
CRM events → deterministic facts → causal rules → State Vector (6 FSM axes)
           → pattern_library (14 historical patterns, no LLM)
           → LLM: Sceptic + Analyst + Contextualist + Smart Sales synthesis
```

- LLM only **interprets** structured context — it never generates facts
- Same data always produces the same State Vector
- Every claim cites a specific CRM event (audit trail)

---

## Results

| Metric | Value |
|--------|-------|
| Companies | 15 (6 CHURN · 1 RENEWAL · 8 EXPANSION) |
| Advisors per company | 3 (Sceptic, Analyst, Contextualist) |
| Historical patterns | 14 unique |
| Smart Sales accuracy | **73.3%** (11/15) |
| API cost (full rebuild) | ~$1.64 |

---

## Three advisors

| Advisor | Role | Mental model | Blind spot |
|---------|------|-------------|------------|
| **Viktor · Sceptic** | Risk detector | Worst outcome first, look for counter-evidence | C
```
