---
title: "pi-agent — AI agent skill for research automation"
description: "Build with and use Pi, the minimal terminal coding harness."
keywords: ["coding agents", "terminal agents", "AI agents", "developer tools"]
---

# `pi-agent`

**Category:** [research-automation](/skills#research-automation) · **License:** MIT · **Version:** 1.4

**Tags:** coding agents, terminal agents, AI agents, developer tools

## When to use it

Build with and use Pi, the minimal terminal coding harness. Use for installing Pi, configuring providers/models/settings/environment variables, creating Pi skills/extensions/packages/themes/prompt templates, embedding Pi through the SDK, integrating over RPC or JSON event streams, parsing sessions, running local models through the llama.cpp router, developing custom Pi providers and TUI components, or using ecosystem packages such as pi-subagents (delegation/orchestration), pi-mcp-adapter (MCP servers), pi-interview (interactive forms), and pi-web-access (web search, fetching, video understanding).

## Example requests

Ask your agent in plain language, for example:

- *"How do I install Pi and hook it up to my Anthropic key?"*
- *"I'm writing a Python harness that drives the Pi coding agent for a benchmark over 200 repos. I tried parsing its stdout with line-by-line splitting in a Node script and sometimes get broken JSON on messages with unusual unicode characters. Which integration mode should I use, and how do I run it so each task is stateless? Please also tell me how to read events correctly."*
- *"I want my terminal AI coding assistant to be able to call out to several of my lab's existing tool servers over the Model Context Protocol, and also hand off sub-tasks to helper agents running in parallel. Can I do both without writing my own plumbing?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill pi-agent

# Kalaris Labs installer with checksum verification
npx research-agent-skills install pi-agent
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `research-automation` category with `/plugin install research-automation@research-agent-skills`.

## Related

- [`qiskit`](/skills/qiskit)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/pi-agent/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
