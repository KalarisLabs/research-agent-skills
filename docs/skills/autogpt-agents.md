---
title: "autogpt-agents — AI agent skill for llm applications"
description: "Autonomous AI agent platform for building and deploying continuous agents."
keywords: ["Agents", "AutoGPT", "Autonomous Agents", "Workflow Automation", "Visual Builder", "AI Platform"]
---

# `autogpt-agents`

**Category:** [llm-applications](/skills#llm-applications) · **License:** MIT · **Version:** 1.0.0

**Tags:** Agents, AutoGPT, Autonomous Agents, Workflow Automation, Visual Builder, AI Platform

## When to use it

Autonomous AI agent platform for building and deploying continuous agents. Use when creating visual workflow agents, deploying persistent autonomous agents, or building complex multi-step AI automation systems.

## Example requests

Ask your agent in plain language, for example:

- *"How do I set up AutoGPT locally with Docker?"*
- *"I'm running the AutoGPT platform in Docker for my lab's literature-monitoring agent. I built a graph in the builder with a webhook block feeding an AITextGeneratorBlock and then an OUTPUT block, but when GitHub fires the webhook the execution just hangs in 'running' and never finishes. Services show as up. How do I debug this?"*
- *"I want something that watches a set of preprint servers every morning, summarizes new papers that match my topics, and posts the summaries to our lab Discord without me touching anything. I'd like to build it by dragging boxes together instead of writing code. What are my options?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill autogpt-agents

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills autogpt-agents
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `llm-applications` category with `/plugin install llm-applications@research-agent-skills`.

## Related

- [`crewai-multi-agent`](/skills/crewai-multi-agent)
- [`evolving-ai-agents`](/skills/evolving-ai-agents)
- [`autoresearch`](/skills/autoresearch)
- [`langchain`](/skills/langchain)
- [Skills for AI research](/fields/artificial-intelligence)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/autogpt-agents/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
