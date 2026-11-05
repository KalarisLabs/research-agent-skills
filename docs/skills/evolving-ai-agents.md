---
title: "evolving-ai-agents — AI agent skill for llm applications"
description: "Provides guidance for automatically evolving and optimizing AI agents across any domain using LLM-driven evolution algorithms."
keywords: ["Agent Evolution", "Self-Improving Agents", "Prompt Optimization", "LLM", "Benchmark Evaluation", "Skill Discovery", "Agentic AI"]
---

# `evolving-ai-agents`

**Category:** [llm-applications](/skills#llm-applications) · **License:** MIT · **Version:** 1.0.0

**Tags:** Agent Evolution, Self-Improving Agents, Prompt Optimization, LLM, Benchmark Evaluation, Skill Discovery, Agentic AI

## When to use it

Provides guidance for automatically evolving and optimizing AI agents across any domain using LLM-driven evolution algorithms. Use when building self-improving agents, optimizing agent prompts and skills against benchmarks, or implementing automated agent evaluation loops.

## Example requests

Ask your agent in plain language, for example:

- *"Can I automatically evolve my agent's prompts and skills against a benchmark?"*
- *"I have a custom agent in ./my_agent with a BaseAgent subclass and a 200-task internal QA dataset scored 0-1. I ran 3 evolution cycles and it reported converged=True, but the agent doesn't seem to use the evolved prompts/system.md. How do I fix both problems?"*
- *"I want my coding assistant to get better at fixing GitHub issues over time without me hand-tuning anything. It should try tasks, look at where it failed, rewrite its own instructions and reusable procedures, and roll back changes that make things worse. How do I set that up?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill evolving-ai-agents

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills evolving-ai-agents
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `llm-applications` category with `/plugin install llm-applications@research-agent-skills`.

## Related

- [`autogpt-agents`](/skills/autogpt-agents)
- [`research-skill-creator`](/skills/research-skill-creator)
- [Skills for AI research](/fields/artificial-intelligence)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/evolving-ai-agents/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
