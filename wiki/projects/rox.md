# rox

**Категория:** 📦 [Uncategorized](../categories/uncategorized.md)
**Статус:** 📁 no-git
**Путь:** `/Users/andriy/VisualStudio/rox`

## 🛠 Tech Stack

- **Languages:** Python
- **Frameworks:** NumPy, OpenAI API, Pandas
- **Tools:** pip

## 📁 Files (72 indexed)

### Docs (26 files, 0.9 MB)

| File | Size | Modified |
|------|------|----------|
| `analyst_en.txt` | 57 KB | 2026-03-16 |
| `contextualist_en.txt` | 64 KB | 2026-03-16 |
| `sceptic_en.txt` | 79 KB | 2026-03-16 |
| `v2/README.md` | 3 KB | 2026-03-16 |
| `docs/ARCHITECTURE_v2.md` | 1 KB | 2026-03-16 |
| `_analyst_en.txt` | 55 KB | 2026-03-16 |
| `_contextualist_en.txt` | 59 KB | 2026-03-16 |
| `_sceptic_en.txt` | 65 KB | 2026-03-16 |
| `dashboard_wireframe.html` | 21 KB | 2026-03-16 |
| `docs/бизнес хочет.txt` | 18 KB | 2026-03-16 |
| `app/backend/requirements.txt` | 78 B | 2026-03-16 |
| `app/README.md` | 2 KB | 2026-03-15 |
| `.cursorrules.txt` | 2 KB | 2026-03-15 |
| `docs/comparison_results2.txt` | 4 KB | 2026-03-15 |
| `docs/optimist.md` | 115 KB | 2026-03-15 |

### Data (11 files, 1.0 MB)

| File | Size | Modified |
|------|------|----------|
| `v2/dataset3_canonical.db` | 276 KB | 2026-03-16 |
| `comparison_results3.csv` | 20 KB | 2026-03-15 |
| `ml_predictions2.csv` | 2 KB | 2026-03-15 |
| `docs/comparison_results2.csv` | 14 KB | 2026-03-15 |
| `docs/ml_predictions2.csv` | 2 KB | 2026-03-15 |
| `dataset2_dirty.db` | 392 KB | 2026-03-15 |
| `docs/comparison_results_openai.csv` | 8 KB | 2026-03-15 |
| `docs/comparison_results.csv` | 18 KB | 2026-03-15 |
| `docs/ml_predictions.csv` | 1 KB | 2026-03-15 |
| `docs/ml_predictions 2.csv` | 1 KB | 2026-03-15 |
| `dataset.db` | 340 KB | 2026-03-15 |

### Code (32 files, 0.3 MB)

| File | Size | Modified |
|------|------|----------|
| `v2/causal_rules.py` | 14 KB | 2026-03-16 |
| `v2/ml_pipeline3.py` | 985 B | 2026-03-16 |
| `patch_cases_17_20.py` | 7 KB | 2026-03-16 |
| `v2/parser_en.py` | 25 KB | 2026-03-16 |
| `generate_experts.py` | 4 KB | 2026-03-16 |
| `app/frontend/src/App.jsx` | 2 KB | 2026-03-16 |
| `app/frontend/src/main.jsx` | 221 B | 2026-03-16 |
| `app/frontend/postcss.config.js` | 66 B | 2026-03-16 |
| `app/frontend/tailwind.config.js` | 310 B | 2026-03-16 |
| `app/frontend/vite.config.js` | 213 B | 2026-03-16 |
| `main.py` | 1 KB | 2026-03-16 |
| `data.py` | 12 KB | 2026-03-16 |
| `app/backend/main.py` | 1 KB | 2026-03-16 |
| `setup_app_v2.sh` | 63 KB | 2026-03-16 |
| `setup_app.sh` | 7 KB | 2026-03-15 |

### Config (3 files, 0.1 MB)

| File | Size | Modified |
|------|------|----------|
| `run_manifest_p6.json` | 420 B | 2026-03-15 |

## 📝 README

```
# MVP: ML vs LLM — Customer Health Classification

## Файлы
| Файл | Назначение |
|------|-----------|
| `dataset.db`          | SQLite база: profiles, events, facts, ground_truth |
| `parser.py`           | Парсер исходных кейсов → база |
| `ml_pipeline.py`      | ML: Random Forest + XGBoost, split by company |
| `llm_pipeline.py`     | LLM: GPT-4o с Pydantic валидацией |
| `ml_predictions.csv`  | Предсказания ML на 18 тестовых кейсах |
| `comparison_results.csv` | Финальное сравнение ML vs LLM (после запуска LLM) |

## Быстрый старт

```bash
pip install -r requirements.txt

# Шаг 1 — пересобрать базу (если нужно)
python parser.py

# Шаг 2 — запустить ML pipeline
python ml_pipeline.py

# Шаг 3 — запустить LLM pipeline
python llm_pipeline.py --key sk-proj-YOUR_OPENAI_KEY
# или
export OPENAI_API_KEY=sk-proj-YOUR_OPENAI_KEY
python llm_pipeline.py
```

## Что делает LLM pipeline

- Берёт те же 18 тестовых кейсов что и ML
- Для каждого кейса строит структурированный промпт:
  - Company Profile
  - 19 вычисленных фактов (facts table)
  - Полный Event Timeline
- Вызывает GPT-4o с temperature=0, JSON mode
- Валидирует ответ через Pydantic
- Сравнивает с ML предсказаниями и ground truth

## Метрики сравнения

- Accuracy
- F1 macro (основная метрика — сбалансированные классы)
- Churn recall (критическая — сколько churns поймано)
- Disagreement analysis: где ML и LLM расходятся
- Hard cases: кейсы с expert confidence ≤ 2

## Важные замечания

### Про тест-сет
18 строк = 6 компаний × 3 
```
