# indicator-tests

**Категория:** 📦 [Uncategorized](../categories/uncategorized.md)
**Статус:** 🟢 active
**Путь:** `/Users/andriy/gitlab-prod/indicator-tests`

## 📊 Git

- **Branch:** `main`
- **Коммитов:** 2
- **Последний:** 2026-03-02
- **Сообщение:** feat(testing): add realtime load test and update README
- **За 30 дней:** 2 коммитов

### Последние коммиты

- `2026-03-02` feat(testing): add realtime load test and update README
- `2026-02-24` initial commit

## 🛠 Tech Stack

- **Languages:** Python
- **Tools:** pip

## 📁 Files (20 indexed)

### Code (14 files, 0.2 MB)

| File | Size | Modified |
|------|------|----------|
| `load_test_realtime.py` | 10 KB | 2026-03-03 |
| `ind_sync_check.py` | 22 KB | 2026-03-03 |
| `verify_taapi_history_stability.py` | 13 KB | 2026-02-28 |
| `verify_realtime_vs_taapi.py` | 33 KB | 2026-02-28 |
| `verify_realtime_vs_backtest.py` | 25 KB | 2026-02-28 |
| `verify_hypothesis2_candles.py` | 13 KB | 2026-02-28 |
| `verify_hypothesis1_transitions.py` | 19 KB | 2026-02-28 |
| `stoch_timing_window.py` | 12 KB | 2026-02-28 |
| `stoch_sync_check.py` | 11 KB | 2026-02-28 |
| `raw_stoch.py` | 1 KB | 2026-02-28 |
| `raw_ichimoku.py` | 810 B | 2026-02-28 |
| `raw_cdlengulfing.py` | 818 B | 2026-02-28 |
| `indicators_loader.py` | 2 KB | 2026-02-28 |
| `debug_stoch_candles.py` | 8 KB | 2026-02-28 |

### Docs (2 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `README.md` | 26 KB | 2026-03-03 |
| `requirements.txt` | 12 B | 2026-02-28 |

### Config (4 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `taapi_indicators.json` | 8 KB | 2026-03-03 |
| `strategies/test_rsi_ema_diff.json` | 200 B | 2026-02-28 |
| `strategies/test_rsi_70.json` | 199 B | 2026-02-28 |
| `strategies/default_rsi_ema.json` | 206 B | 2026-02-28 |

## 📝 README

```
# INDICATOR_TESTING.md

Верификация индикаторного сервиса: сравнение реалтайм-значений с эталонами TAAPI.IO.

---

## Оглавление

1. [Философия тестирования](#1-философия-тестирования)
2. [Тест реалтайм vs бэктест](#2-тест-реалтайм-vs-бэктест-verify_realtime_vs_backtestpy)
3. [Архитектура: тест vs TAAPI](#3-архитектура-тест-vs-taapi-ind_sync_checkpy)
4. [Критерии вердикта](#4-критерии-вердикта)
5. [Статус индикаторов](#5-статус-индикаторов)
6. [Запуск тестов](#6-запуск-тестов)
7. [Добавление нового индикатора](#7-добавление-нового-индикатора)
8. [Известные особенности](#8-известные-особенности)
9. [Нагрузочное тестирование](#9-нагрузочное-тестирование-load_test_realtimepy)
10. [Файлы проекта](#10-файлы-проекта)

---

## 1. Философия тестирования

### Что мы проверяем

Наш сервис и TAAPI.IO — два независимых источника, оба используют TA-Lib под капотом.
Цель не добиться идеального совпадения, а убедиться, что:

- **тайминг совпадает** — оба обновляют значение на одной и той же границе TF
- **алгоритм совпадает** — числовые значения близки в штатном режиме

### Почему не может быть идеального совпадения

**Разный warmup.** Наш сервис накапливает 8 дней × TF исторических данных для прогрева.
TAAPI использует существенно меньше. Из-за этого в первые фреймы после запуска TAAPI,
и в экстремумах стохастика (~0 или ~100), значения расходятся — это не баг, это артефакт
прогрева.

**TAAPI latency.** Сразу после закрытия свечи TAAPI ещё не пересчитал значение.
Именно поэтому мы использу
```
