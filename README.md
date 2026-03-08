# claude-codebase-navigator

> **Turn your project directories into token-efficient context maps for Claude, ChatGPT, and any LLM.**

When you ask an LLM to help across multiple repos, it burns hundreds of tokens exploring your codebase file-by-file before it can even start helping. Claude Codebase Navigator pre-generates a **compact, structured context map** you paste directly into your prompt — so the LLM understands your architecture instantly.

**Typical savings: 40–70% tokens vs live MCP file exploration.**

---

## What it does

| Feature | Description |
|---------|-------------|
| 🗺 **Prompt maps** | One command generates a compact map of selected projects (tech stack, ports, integrations, key files, README) — ready to paste into any LLM prompt |
| 📚 **Markdown wiki** | Auto-generated wiki with index, per-project pages, status dashboard, timeline, and tech matrix |
| 🔍 **Auto-detection** | Tech stack, integrations via `.env` / `docker-compose.yml`, git status |
| ⚙️ **Zero lock-in** | Pure Python, one YAML config, works with any git host (GitHub, GitLab, Bitbucket, self-hosted) |
| 📦 **Minimal deps** | Only requires `pyyaml`. Everything else is stdlib. |

---

## Quick start

```bash
git clone https://github.com/yourname/claude-codebase-navigator
cd claude-codebase-navigator
pip install -r requirements.txt

cp config.example.yaml config.yaml
# Edit config.yaml → set sources.local_dev to your projects directory

python navigate.py          # Scan everything + build wiki
```

The wiki is generated in `./wiki/INDEX.md`.

---

## The killer feature: `--map`

When you need LLM help across multiple services, run:

```bash
python navigate.py --map auth-service frontend-app postgres-migrations
```

This prints (and saves) a structured map like:

```
## 🟢 active  auth-service
**Git:** branch `main` · last commit 2026-03-01 — feat: add refresh tokens
**Stack:** Python, FastAPI, PostgreSQL, Redis
**Docker services:**
  - `api` ports: 8001→8001 · env: DB_NAME=auth_db | PORT=8001
  - `redis` ports: 6379→6379
**Key files:** app/main.py, app/routers/auth.py, app/models/user.py
**Files:** 34 code / 8 docs / 2 data
**README:** JWT-based authentication service with refresh token rotation…
```

Paste this into your prompt. The LLM immediately understands the architecture — no file exploration needed.

### Recommended workflow

```
1. Identify the projects involved in your task
2. Run: python navigate.py --map project-a project-b project-c
3. Copy the output (or contents of wiki/_prompt_map_N.md)
4. Paste into your Claude / ChatGPT prompt along with your question
```

---

## Configuration

Copy `config.example.yaml` → `config.yaml` and edit:

```yaml
sources:
  local_dev: ~/Projects           # your main dev directory
  production: ~/cloned-repos      # optional: cloned production repos

git_remote:
  base_url: https://github.com/myorg   # for deep links in the wiki

categories:
  backend:
    icon: "⚙️"
    title: "Backend Services"
    keywords: [api, service, server, backend]
  frontend:
    icon: "🎨"
    title: "Frontend Apps"
    keywords: [ui, frontend, web, app, dashboard]
  # ... add your own
```

That's it. No hardcoded paths. No personal data.

---

## CLI reference

```
python navigate.py                         # Full scan + wiki
python navigate.py --map svc-a svc-b       # Prompt map for named projects
python navigate.py --diff                  # Show what changed since last scan
python navigate.py --wiki-only             # Rebuild wiki without re-scanning
python navigate.py --watch --interval 10   # Auto-rescan every 10 minutes
python navigate.py --category backend      # Scan only matching projects
python navigate.py --config ~/my.yaml      # Use a custom config file
python navigate.py --map svc-a --output prompt.md  # Save map to file
```

---

## Wiki structure

```
wiki/
├── INDEX.md          # master index by category
├── STATUS.md         # all projects by git activity status
├── TIMELINE.md       # recent commits across all repos
├── TECH_MATRIX.md    # technology usage per project
├── categories/       # one page per category
├── projects/         # one page per project
└── _prompt_map_*.md  # auto-saved prompt maps
```

---

## Project page example

Each project gets a full page with:
- Git status, branch, recent commit history
- Tech stack (auto-detected from `requirements.txt`, `package.json`, `Dockerfile`)
- Docker services with ports and key env vars
- Auto-detected integrations from `.env` files (URL references)
- Key code files
- README excerpt

---

## Use cases

**Multi-repo debugging**
> "Why are `payment-service` and `order-service` out of sync?"
> → `--map payment-service order-service` → paste map → ask Claude

**Onboarding**
> New team member needs to understand which services exist and how they connect
> → share the generated `wiki/INDEX.md`

**Architecture review**
> Need to document all services and their integrations
> → run scan → share `wiki/INTEGRATION_MAP.md` *(if integrations are configured)*

**Code review context**
> Reviewing a PR that touches 3 services
> → `--map` those 3 services → paste into your review prompt

---

## Requirements

- Python 3.10+
- `pyyaml` (one pip install)
- `git` on PATH (for git metadata; optional — projects without `.git` are still scanned)

---

## Contributing

PRs welcome. The codebase is intentionally simple:

```
navigate.py          # CLI entry point
src/
  config.py          # config loading & validation
  scanner.py         # single-project metadata extraction
  catalog.py         # multi-project scan orchestration & state
  wiki.py            # Markdown wiki generation
  mapper.py          # prompt map generation (the killer feature)
config.example.yaml  # annotated config template
```

---

## License

MIT
