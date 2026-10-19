---
title: "research-skill-creator — AI agent skill for research automation"
description: "Create, improve and test agent skills for research workflows (paper writing, lab protocols, analysis pipelines, domain databases) that meet the Agent Skills…"
keywords: ["skill authoring", "agent skills", "SKILL.md", "evals", "contributing"]
---

# `research-skill-creator`

**Category:** [research-automation](/skills#research-automation) · **License:** MIT · **Version:** 1.0 · **Includes scripts**

**Tags:** skill authoring, agent skills, SKILL.md, evals, contributing

## When to use it

Create, improve and test agent skills for research workflows (paper writing, lab protocols, analysis pipelines, domain databases) that meet the Agent Skills specification and this repository's quality and security bar. Use when turning a repeated research task into a reusable skill, contributing a new skill to Research Agent Skills, rewriting an existing skill, writing trigger-accurate descriptions, or adding evals. Works alongside Anthropic's official skill-creator.

## Example requests

Ask your agent in plain language, for example:

- *"Turn our lab's qPCR analysis workflow into a reusable agent skill and contribute it."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill research-skill-creator

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills research-skill-creator
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `research-automation` category with `/plugin install research-automation@research-agent-skills`.

## Related

- [`arbor`](/skills/arbor)
- [`autoresearch`](/skills/autoresearch)
- [`autoskill`](/skills/autoskill)
- [`evolving-ai-agents`](/skills/evolving-ai-agents)
- [`research-agent-skills`](/skills/research-agent-skills)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/research-skill-creator/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
