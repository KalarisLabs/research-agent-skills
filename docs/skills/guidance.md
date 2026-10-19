---
title: "guidance — AI agent skill for llm applications"
description: "Constrains LLM output during generation with Guidance (Microsoft Research), using regex, select() choices, context-free grammars, token healing, and @guidance…"
keywords: ["Prompt Engineering", "Guidance", "Constrained Generation", "Structured Output", "JSON Validation", "Grammar", "Microsoft Research", "Format Enforcement", "Multi-Step Workflows"]
---

# `guidance`

**Category:** [llm-applications](/skills#llm-applications) · **License:** MIT · **Version:** 1.0.0 · **Includes scripts**

**Tags:** Prompt Engineering, Guidance, Constrained Generation, Structured Output, JSON Validation, Grammar, Microsoft Research, Format Enforcement, Multi-Step Workflows

## When to use it

Constrains LLM output during generation with Guidance (Microsoft Research), using regex, select() choices, context-free grammars, token healing, and @guidance functions, with Anthropic, OpenAI, Transformers, and llama.cpp backends. Use when you need generated text to match a regex or fixed format such as dates, emails, or IDs. Use when you need guaranteed valid JSON, XML, or code from a model. Use when building multi-step generation workflows or ReAct-style agents with Python control flow. Use when classifying text into fixed categories with select(). Use when running local models and wanting grammar constraints. Not for Pydantic validation with automatic retries; use Instructor for that.

## Example requests

Ask your agent in plain language, for example:

- *"How do I force a local Llama model to only output a date like 2024-03-15? Regex-constrained decoding please."*
- *"I'm labeling clinical trial abstracts in abstracts.csv into exactly four categories (RCT, cohort, case report, review) using a llama.cpp GGUF model on my workstation. Sometimes the model returns 'Randomized study' or adds explanations and my pandas parsing breaks. How can I make it only ever emit one of the four labels?"*
- *"I want a model to produce SQL-like queries for my lab's sample database, and the output must always parse under a specific grammar, no syntax errors ever. I also want it to first think of the table to use, then fill in the query, in several steps with Python if-statements in between. How should I build this?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill guidance

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills guidance
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `llm-applications` category with `/plugin install llm-applications@research-agent-skills`.

## Related

- [Skills for AI research](/fields/artificial-intelligence)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/guidance/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
