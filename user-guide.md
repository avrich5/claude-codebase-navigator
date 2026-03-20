# Project Cataloger and Wiki Generator: User Guide

This guide explains how to use the Project Cataloger and GitLab Wiki Generator tools located in `/Users/andriy/VisualStudio/project_cataloger`. These scripts help manage dependencies, track metadata across multiple codebases, and automatically generate a Markdown Wiki.

## 1. Quick Start

If you just want to update the Wiki with the latest files and projects from GitLab, here are the easiest ways to do so:

### A. Add a Specific New Project by URL
If you have a new Git repository URL and want to add it immediately (it will be cloned to `~/gitlab-prod` and the wiki will be rebuilt):

```bash
python3 gitlab_wiki.py --add-url https://git.forvest.software/frv/your-new-project.git
```

### B. Fetch All Updated/New Projects from GitLab
If you want to sync your entire `gitlab-prod` directory against the GitLab group API (which clones all missing projects and updates existing ones), and then rebuild the wiki:

```bash
# 1. Fetch missing/new projects
bash /Users/andriy/gitlab-prod/git-pull-frv.sh

# 2. Rebuild the Wiki
python3 gitlab_wiki.py
```

---

## 2. Core Scripts

### `cataloger.py`
**Purpose:** Scans local development projects in `/Users/andriy/VisualStudio`.
- Extracts file statistics, Git commit history, tech stack details, and README files.
- Generates a `catalog_state.json` file which is later used to enrich the centralized GitLab Wiki.
- Can run continuously (`--watch`) or scan specific categories (`--category`).

**Example Usage:**
```bash
python3 cataloger.py           # Full scan and rebuild local wiki
python3 cataloger.py --diff    # Show changes since last scan
```

### `gitlab_wiki.py`
**Purpose:** Scans cloned projects in `/Users/andriy/gitlab-prod` and merges the data with the local `catalog_state.json` (to include local file and full README details). It then generates the comprehensive **GitLab Production Wiki** with integration maps.

**Key Flags:**
- `--map PROJECT1 PROJECT2`: Generates a compact markdown map detailing the tech stack, ports, environment variables, and connections between the given projects. Highly useful for generating context to paste into Claude/LLM prompts.
  - _Example:_ `python3 gitlab_wiki.py --map ai-trading-strategy-advisor profitradar`
- `--add-url URL`: Automatically `git clone` (or `git pull` if it exists) a specific repository URL into `~/gitlab-prod` and immediately regenerates the wiki.
- `--add-local NAME_OR_PATH`: Adds a local-only project path to the wiki scanning scope (useful for local-only pipelines not yet pushed to GitLab).

---

## 3. Workflow for Writing LLM Prompts

1. Find the names of the projects you need to integrate or debug.
2. Run `gitlab_wiki.py --map` targeted at those projects to automatically generate a dependency map:
   ```bash
   python3 gitlab_wiki.py --map signal-emulator indicators-basic
   ```
3. Copy the output generated in `/Users/andriy/gitlab-prod/wiki/_prompt_map_<N>.md`.
4. Paste the output into your prompt for Claude Code or Opus to provide immediate, token-efficient context about project structures and integrations.

---

## 4. Where is Everything?

- **Wiki Location:** `/Users/andriy/gitlab-prod/wiki/INDEX.md`
- **Catalog State:** `/Users/andriy/VisualStudio/project_cataloger/catalog_state.json`
- **GitLab Clones:** `/Users/andriy/gitlab-prod/`
- **Local Dev Clones:** `/Users/andriy/VisualStudio/`
