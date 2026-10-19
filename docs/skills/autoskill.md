---
title: "autoskill — AI agent skill for research automation"
description: "Observe the user's screen via screenpipe, detect repeated research workflows, match them against existing research-agent-skills, and draft new skills (or…"
keywords: ["skill authoring", "workflow automation", "research automation", "AI agents"]
---

# `autoskill`

**Category:** [research-automation](/skills#research-automation) · **License:** MIT · **Version:** 1.4 · **Includes scripts**

**Tags:** skill authoring, workflow automation, research automation, AI agents

## When to use it

Observe the user's screen via screenpipe, detect repeated research workflows, match them against existing research-agent-skills, and draft new skills (or composition recipes that chain existing ones) for the patterns not yet covered. Use when the user asks to analyze their recent work and propose skills based on what they actually do. Requires the screenpipe daemon (https://github.com/screenpipe/screenpipe) running locally on port 3030 — the skill has no other data source and will refuse to run if screenpipe is unreachable. All detection runs locally; only redacted cluster summaries reach the LLM.

## Example requests

Ask your agent in plain language, for example:

- *"Can you look at what I did this afternoon and suggest skills I should make from it?"*
- *"I've spent the past week bouncing between Zotero, RStudio, and Overleaf for my meta-analysis, over and over. Run autoskill on the last 7 days, but use --plan first so I can see what gets analyzed before anything goes to Claude. Screenpipe is on port 3030 and my token is in SCREENPIPE_TOKEN."*
- *"I keep doing the same dance every day: pull new papers, skim them, copy notes into my lab notebook, then format the references. Can you watch how I actually work over the last few days and work out which of those steps my existing skills already handle and which still need something new?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill autoskill

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills autoskill
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `research-automation` category with `/plugin install research-automation@research-agent-skills`.

## Related

- [`citation-management`](/skills/citation-management)
- [`generate-image`](/skills/generate-image)
- [`literature-review`](/skills/literature-review)
- [`research-skill-creator`](/skills/research-skill-creator)
- [`scientific-schematics`](/skills/scientific-schematics)
- [`scientific-slides`](/skills/scientific-slides)
- [`scientific-writing`](/skills/scientific-writing)
- [`sentence-transformers`](/skills/sentence-transformers)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/autoskill/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
