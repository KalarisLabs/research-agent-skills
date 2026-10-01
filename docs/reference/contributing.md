---
title: Contributing a skill | Research Agent Skills
description: How to write, test and contribute a new research agent skill.
---

Contributions should improve a researcher's work and document claims that can change. Every new skill needs
`skills/<name>/SKILL.md` with valid frontmatter, a clear "Use when" description, and
`evals/<name>/evals.json` with realistic prompts and a near miss.

Run these checks before opening a pull request:

```bash
uv run tools/validate.py
uv run tools/lint_injection.py
uv run tools/brand_guard.py
uv run tools/build_catalog.py --docs
uv run tools/skill_quality.py
uv run tools/trigger_bench.py
```

Read the [full contribution guide](https://github.com/KalarisLabs/research-agent-skills/blob/main/CONTRIBUTING.md)
for script rules, evaluation guidance and review requirements.
