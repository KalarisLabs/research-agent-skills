---
title: "crewai-multi-agent — AI agent skill for llm applications"
description: "Multi-agent orchestration framework for autonomous AI collaboration."
keywords: ["Agents", "CrewAI", "Multi-Agent", "Orchestration", "Collaboration", "Role-Based", "Autonomous", "Workflows", "Memory", "Production"]
---

# `crewai-multi-agent`

**Category:** [llm-applications](/skills#llm-applications) · **License:** MIT · **Version:** 1.0.0 · **Includes scripts**

**Tags:** Agents, CrewAI, Multi-Agent, Orchestration, Collaboration, Role-Based, Autonomous, Workflows, Memory, Production

## When to use it

Multi-agent orchestration framework for autonomous AI collaboration. Use when building teams of specialized agents working together on complex tasks, when you need role-based agent collaboration with memory, or for production workflows requiring sequential/hierarchical execution. Built without LangChain dependencies for lean, fast execution.

## Example requests

Ask your agent in plain language, for example:

- *"Set up a crew with a researcher and a writer agent that hand work off to each other for a lit summary."*
- *"I'm on crewai 1.2 and my agents.yaml / tasks.yaml crew for screening ~200 abstracts from abstracts.csv keeps looping on the 'screener' agent until it hits a rate limit error (429 from OpenAI). How do I fix this?"*
- *"I want a few specialized AI workers for a systematic review pipeline: one finds papers, one extracts effect sizes, one checks the extracted numbers, and a coordinator that assigns the work and remembers earlier findings between runs. How should I build that?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill crewai-multi-agent

# Kalaris Labs installer with checksum verification
npx research-agent-skills install crewai-multi-agent
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `llm-applications` category with `/plugin install llm-applications@research-agent-skills`.

## Related

- [`aeon`](/skills/aeon)
- [`autogpt-agents`](/skills/autogpt-agents)
- [Skills for AI research](/fields/artificial-intelligence)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/crewai-multi-agent/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
