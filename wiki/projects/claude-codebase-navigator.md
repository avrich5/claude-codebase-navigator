# claude-codebase-navigator

**Категория:** 📦 [Uncategorized](../categories/uncategorized.md)
**Статус:** 🟢 active
**Путь:** `/Users/andriy/VisualStudio/claude-codebase-navigator`

## 📊 Git

- **Branch:** `main`
- **Коммитов:** 5
- **Последний:** 2026-03-19
- **Сообщение:** feat: global config at ~/.config/navigate/config.yaml — works from any directory
- **За 30 дней:** 5 коммитов

### Последние коммиты

- `2026-03-19` feat: global config at ~/.config/navigate/config.yaml — works from any directory
- `2026-03-19` feat: add --add-project CLI to scan projects from any directory
- `2026-03-08` docs: add killer feature 2 — single-project deep review for LLM
- `2026-03-08` fix: noisy dirs filtered from listings, key files ranked by size, readme expanded to 4000 chars
- `2026-03-08` Initial release: project wiki & LLM context maps

## 🛠 Tech Stack

- **Languages:** Python
- **Tools:** pip

## 📁 Files (118 indexed)

### Docs (101 files, 0.3 MB)

| File | Size | Modified |
|------|------|----------|
| `wiki/TECH_MATRIX.md` | 5 KB | 2026-03-19 |
| `wiki/TIMELINE.md` | 11 KB | 2026-03-19 |
| `wiki/STATUS.md` | 7 KB | 2026-03-19 |
| `wiki/projects/pattern_config_gen.md` | 4 KB | 2026-03-19 |
| `wiki/projects/mechanism-signal-mapper.md` | 4 KB | 2026-03-19 |
| `wiki/projects/development plans.md` | 536 B | 2026-03-19 |
| `wiki/projects/c2-strategy-longtrend-lowvol-main.md` | 1 KB | 2026-03-19 |
| `wiki/projects/c2-strategy-gapfill-main.md` | 1 KB | 2026-03-19 |
| `wiki/projects/ProfitRadar_main.md` | 6 KB | 2026-03-19 |
| `wiki/INDEX.md` | 9 KB | 2026-03-19 |
| `README.md` | 8 KB | 2026-03-08 |
| `wiki/_prompt_map_3.md` | 763 B | 2026-03-08 |
| `wiki/_prompt_map_2.md` | 2 KB | 2026-03-08 |
| `wiki/_prompt_map_1.md` | 376 B | 2026-03-08 |
| `requirements.txt` | 125 B | 2026-03-08 |

### Config (10 files, 28.4 MB)

| File | Size | Modified |
|------|------|----------|
| `history/catalog_20260319_153212.json` | 4.5 MB | 2026-03-19 |
| `catalog_state.json` | 4.5 MB | 2026-03-19 |
| `history/catalog_20260319_133035.json` | 4.5 MB | 2026-03-19 |
| `history/catalog_20260319_132622.json` | 4.5 MB | 2026-03-19 |
| `history/catalog_20260319_132607.json` | 3.2 MB | 2026-03-19 |
| `history/catalog_20260308_095555.json` | 3.2 MB | 2026-03-08 |
| `history/catalog_20260308_094530.json` | 4.0 MB | 2026-03-08 |
| `config.yaml` | 2 KB | 2026-03-08 |
| `history/catalog_20260308_094423.json` | 2 B | 2026-03-08 |
| `config.example.yaml` | 3 KB | 2026-03-08 |

### Code (7 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `src/config.py` | 7 KB | 2026-03-19 |
| `navigate.py` | 7 KB | 2026-03-19 |
| `src/catalog.py` | 6 KB | 2026-03-19 |
| `src/mapper.py` | 7 KB | 2026-03-08 |
| `src/scanner.py` | 13 KB | 2026-03-08 |
| `src/wiki.py` | 10 KB | 2026-03-08 |
| `src/__init__.py` | 28 B | 2026-03-08 |

## 📝 README

```
# claude-codebase-navigator

> **Turn your project directories into token-efficient context maps for Claude, ChatGPT, and any LLM.**

When you ask an LLM to help across multiple repos, it burns hundreds of tokens exploring your codebase file-by-file before it can even start helping. Claude Codebase Navigator pre-generates a **compact, structured context map** you paste directly into your prompt — so the LLM understands your architecture instantly.

**Typical savings: 40–70% tokens vs live MCP file exploration.**

---

## What it does

| Feature | Description |
|---------|-------------|
| 🗺 **Prompt maps** | One command generates a compact map of selected projects (tech stack, ports, integrations, key files, README) — ready to paste into any LLM prompt |
| 🔬 **Single-project deep review** | Full wiki page per project — git history, all key files ranked by size, tech stack, integrations — structured for LLM code review |
| 📚 **Markdown wiki** | Auto-generated wiki with index, per-project pages, status dashboard, timeline, and tech matrix |
| 🔍 **Auto-detection** | Tech stack, integrations via `.env` / `docker-compose.yml`, git status |
| ⚙️ **Zero lock-in** | Pure Python, one YAML config, works with any git host (GitHub, GitLab, Bitbucket, self-hosted) |
| 📦 **Minimal deps** | Only requires `pyyaml`. Everything else is stdlib. |

---

## Quick start

```bash
git clone https://github.com/yourname/claude-codebase-navigator
cd claude-codebase-navigator
pip install -r requirements.
```
