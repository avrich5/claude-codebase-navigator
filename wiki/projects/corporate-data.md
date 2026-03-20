# corporate-data

**Категория:** 📦 [Uncategorized](../categories/uncategorized.md)
**Статус:** 🟢 active
**Путь:** `/Users/andriy/VisualStudio/corporate-data`

## 📊 Git

- **Branch:** `main`
- **Коммитов:** 17
- **Последний:** 2026-03-11
- **Сообщение:** feat(matrix): add Stage 06c BCG×ABC matrix with quarterly dynamics and transition tracker
- **За 30 дней:** 17 коммитов

### Последние коммиты

- `2026-03-11` feat(matrix): add Stage 06c BCG×ABC matrix with quarterly dynamics and transition tracker
- `2026-03-11` fix(advisor): switch to OpenAI gpt-4o — resolves output truncation (finish=stop, 15 recs)
- `2026-03-11` style(advisor): remove emoji from UI — violates cursorrules English-only rule
- `2026-03-11` fix(advisor): add LLM recs cache + model_lines cache; fix aggregate_model_lines signature
- `2026-03-11` feat(advisor): add Stage 06a aggregator, Stage 06b advisor, Advisor tab in UI

## 🛠 Tech Stack

- **Languages:** Python
- **Frameworks:** NumPy, OpenAI API, Pandas, Plotly, Streamlit
- **Tools:** pip

## 📁 Files (149 indexed)

### Code (33 files, 0.2 MB)

| File | Size | Modified |
|------|------|----------|
| `app/query_ui.py` | 24 KB | 2026-03-11 |
| `pipeline/stage_06c_matrix.py` | 5 KB | 2026-03-11 |
| `pipeline/stage_06b_advisor.py` | 9 KB | 2026-03-11 |
| `pipeline/stage_06a_aggregate.py` | 9 KB | 2026-03-11 |
| `pipeline/stage_05e_chart.py` | 11 KB | 2026-03-11 |
| `pipeline/stage_05d_execute.py` | 11 KB | 2026-03-11 |
| `pipeline/stage_05c_generate.py` | 4 KB | 2026-03-11 |
| `pipeline/stage_05b_retrieve.py` | 7 KB | 2026-03-11 |
| `pipeline/stage_02_analyze.py` | 16 KB | 2026-03-11 |
| `utils/prompt_builder.py` | 6 KB | 2026-03-11 |
| `utils/llm_client.py` | 4 KB | 2026-03-11 |
| `config.py` | 6 KB | 2026-03-11 |
| `pipeline/stage_05a_embed.py` | 7 KB | 2026-03-11 |
| `parse_docx.py` | 564 B | 2026-03-11 |
| `pipeline/stage_04_assemble.py` | 7 KB | 2026-03-11 |

### Docs (10 files, 0.1 MB)

| File | Size | Modified |
|------|------|----------|
| `NEXT_ASSISTANT_PROMPT.md` | 16 KB | 2026-03-11 |
| `TODO.md` | 15 KB | 2026-03-11 |
| `requirements.txt` | 2 KB | 2026-03-11 |
| `ARCHITECTURE.md` | 7 KB | 2026-03-11 |
| `README.md` | 7 KB | 2026-03-11 |
| `specs/SPEC_stage_04_assemble.md` | 2 KB | 2026-03-11 |
| `specs/SPEC_stage_03_review.md` | 8 KB | 2026-03-11 |
| `specs/SPEC_stage_02_analyze.md` | 3 KB | 2026-03-11 |
| `specs/SPEC_stage_01_extract.md` | 3 KB | 2026-03-11 |
| `STAGE1_FINDINGS.md` | 3 KB | 2026-03-11 |

### Config (104 files, 4.7 MB)

| File | Size | Modified |
|------|------|----------|
| `outputs/structural_2026-03-11T21-26-27.json` | 114 KB | 2026-03-11 |
| `outputs/navigation_2026-03-11T21-26-09.json` | 4 KB | 2026-03-11 |
| `outputs/advisor_recs_categories_b0cc12a83498.json` | 8 KB | 2026-03-11 |
| `outputs/advisor_recs_categories_7d06e55c5716.json` | 14 KB | 2026-03-11 |
| `outputs/advisor_recs_categories_ef26f2f037d0.json` | 8 KB | 2026-03-11 |
| `outputs/advisor_recs_categories_3f275291bd74.json` | 13 KB | 2026-03-11 |
| `outputs/advisor_recs_categories_1e397f903bfe.json` | 13 KB | 2026-03-11 |
| `outputs/advisor_recs_categories_7167258a183e.json` | 13 KB | 2026-03-11 |
| `outputs/advisor_recs_categories_46ef9863fdb3.json` | 7 KB | 2026-03-11 |
| `outputs/advisor_lines_cache_42598000.json` | 108 KB | 2026-03-11 |
| `outputs/advisor_recs_categories_fe63be5d294a.json` | 7 KB | 2026-03-11 |
| `outputs/advisor_cache_42598000.json` | 24 KB | 2026-03-11 |
| `outputs/final_schema_2026-03-11T17-00-10.json` | 43 KB | 2026-03-11 |
| `outputs/semantic_2026-03-11T17-00-10.json` | 88 KB | 2026-03-11 |
| `outputs/structural_2026-03-11T16-55-26.json` | 113 KB | 2026-03-11 |

### Data (2 files, 1.8 MB)

| File | Size | Modified |
|------|------|----------|
| `sources/Анализ BCG ДУ 2025_4 кв. NEW.xlsx` | 914 KB | 2026-03-11 |

## 📝 README

```
# corporate-data

**Excel Analytics Pipeline** — автоматична побудова структурованої схеми даних з корпоративних Excel-файлів із використанням LLM.

Демонструє, як перетворити сотні Excel-таблиць, накопичених роками, на машиночитану базу знань — основу для корпоративного data agent.

---

## Задача

Організації накопичують сотні Excel-файлів побудованих фахівцями предметної галузі. Файли кодують критичну бізнес-логіку (пайплайни, ієрархії, порогові значення), яка існує лише в структурі файлів та в головах авторів.

**Мета:** автоматично витягнути цю структуру у `final_schema.json` — семантичний шар (data catalog) для майбутнього query agent.

---

## Архітектура

```
Excel
  │
  ▼
Stage 01b — LLM Navigation     ← визначає header_row, data_start, period blocks
  │
  ▼
Stage 01  — Structural Extractor  ← механічні факти (типи, null rate, sentinels)
  │
  ▼
Stage 02  — Semantic Analyzer (LLM) ← класифікує поля, виявляє зв'язки
  │
  ├── resolved[]        confidence > 0.85  → автоматично
  ├── confirm_queue[]   confidence 0.5–0.85 → human review
  └── escalate_queue[]  confidence < 0.5   → людина відповідає
  │
  ▼
Stage 03  — Human Review (CLI)
  │
  ▼
Stage 04  — Schema Assembler
  │
  ├── final_schema_<timestamp>.json   ← data catalog
  └── report_<timestamp>.docx         ← звіт для стейкхолдерів
```

Кожен stage — окремий модуль, комунікує через файли (ADR-001). Джерелний Excel ніколи не модифікується (ADR-003).

---

## Швидкий старт

### 1. Клонувати і налаштувати

```bash

```
