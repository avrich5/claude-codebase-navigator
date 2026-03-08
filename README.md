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
pip install -r requirements.txt

cp config.example.yaml config.yaml
# Edit config.yaml → set sources.local_dev to your projects directory

python navigate.py          # Scan everything + build wiki
```

The wiki is generated in `./wiki/INDEX.md`.

---

## Killer feature 1: `--map` for multi-project context

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

## Killer feature 2: wiki pages for single-project deep review

When you need an LLM to review, refactor, or deeply understand one large project, the `--map` compact format isn't enough — you need the full structured picture.

Every project gets a rich wiki page at `wiki/projects/<name>.md` containing:

```
# payment-service

**Status:** 🟢 active  ·  **Branch:** main  ·  **Commits:** 847

### Recent commits
- 2026-03-05  feat: add idempotency keys to charge endpoint
- 2026-03-04  fix: retry logic on Stripe timeout
- 2026-03-02  refactor: extract PaymentIntent factory

## Tech Stack
- Languages: Python
- Frameworks: FastAPI, SQLAlchemy, Redis, Celery
- Tools: Docker Compose, GitLab CI

## Integrations
| Target         | Type  | URL                      |
|----------------|-------|--------------------------|
| NOTIFICATION_URL | HTTP | http://notify-svc:9000  |
| ANALYTICS_URL  | HTTP  | http://analytics:8080    |

## Files (148 code / 42 docs / 11 data)
### Code — top files by size
| File                          | Size  | Modified   |
|-------------------------------|-------|------------|
| app/services/charge.py        | 48 KB | 2026-03-05 |
| app/routers/payments.py       | 31 KB | 2026-03-04 |
| app/models/transaction.py     | 22 KB | 2026-03-02 |
...

## README
[full README excerpt up to 4000 chars]
```

### Why this beats asking the LLM to explore the repo itself

| Approach | Tokens spent on orientation | Tokens left for actual work |
|---|---|---|
| LLM explores via MCP | ~3,000–8,000 | what's left |
| Paste `wiki/projects/<name>.md` | ~800–1,500 | almost everything |

The wiki page is pre-computed, noise-free (data artifact dirs filtered out), and ranked by importance — so the LLM starts with the most relevant files, not alphabetical order or random directory traversal.

### Recommended workflow for code review

```
1. Run: python navigate.py   (or --wiki-only if already scanned)
2. Open: wiki/projects/<your-project>.md
3. Copy the full contents
4. Paste into your LLM prompt:
   "Here is the project structure: [paste wiki page]
    Now review the charge.py service and suggest improvements."
```

This works especially well for:
- **Refactoring sessions** — LLM sees all files ranked by size, knows the full tech stack
- **Bug investigation** — recent commit history shows exactly what changed and when
- **Onboarding new LLM context** — after hitting token limits mid-conversation, paste the wiki page to restore full project awareness instantly
- **Code review of a PR** — combine wiki page + diff for complete context

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
├── projects/         # one page per project  ← killer feature 2
└── _prompt_map_*.md  # auto-saved prompt maps  ← killer feature 1
```

---

## Use cases

**Multi-repo debugging**
> "Why are `payment-service` and `order-service` out of sync?"
> → `--map payment-service order-service` → paste map → ask Claude

**Deep single-project review**
> "Refactor the charge service — suggest improvements"
> → paste `wiki/projects/payment-service.md` → ask Claude

**Onboarding**
> New team member needs to understand which services exist and how they connect
> → share the generated `wiki/INDEX.md`

**Restoring LLM context mid-conversation**
> Hit token limit, need to continue in a new chat
> → paste the relevant `wiki/projects/<n>.md` to instantly restore full project awareness

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
  mapper.py          # prompt map generation (killer feature 1)
config.example.yaml  # annotated config template
```

---

## License

MIT
