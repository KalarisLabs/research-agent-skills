---
title: "dhdna-profiler — AI agent skill for research writing"
description: "Extract cognitive patterns and thinking fingerprints from any text."
keywords: ["text analysis", "cognitive style", "writing analysis", "profiling"]
---

# `dhdna-profiler`

**Category:** [research-writing](/skills#research-writing) · **License:** MIT · **Version:** 1.1

**Tags:** text analysis, cognitive style, writing analysis, profiling

## When to use it

Extract cognitive patterns and thinking fingerprints from any text. Use this skill when the user wants to analyze how someone thinks, understand cognitive style, profile writing or speech patterns, compare thinking styles between people, asks "what's my thinking style", "analyze how this person reasons", "cognitive profile", "thinking pattern", "DHDNA", "digital DNA", or wants to understand the mind behind any text. Also trigger when the user provides text and wants deeper insight into the author's reasoning patterns, decision-making style, or cognitive signature.

## Example requests

Ask your agent in plain language, for example:

- *"what's the thinking style of the person who wrote this? "I keep going back and forth on this. On one hand the data says ship it, but I remember what happened with the 2019 launch, and honestly I'm not sure my read on the team is right.""*
- *"I've saved two op-ed pieces as op_ed_senator_A.txt and op_ed_senator_B.txt (about 900 words each, both on the 2024 carbon tax debate). Can you profile each author's reasoning patterns and then tell me how their minds differ and where they'd clash in a debate? It's for a discourse-analysis seminar paper."*
- *"I'm writing a memoir chapter and want to understand what my own writing reveals about how my mind works: whether I lean on logic or gut, how I handle emotion, that kind of thing. Could you look at how I've been talking to you in this session?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill dhdna-profiler

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills dhdna-profiler
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `research-writing` category with `/plugin install research-writing@research-agent-skills`.

## Related

- [`consciousness-council`](/skills/consciousness-council)
- [`creative-thinking-for-research`](/skills/creative-thinking-for-research)
- [`citation-verification`](/skills/citation-verification)
- [Write a research paper with AI](/guides/write-a-research-paper)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/dhdna-profiler/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
