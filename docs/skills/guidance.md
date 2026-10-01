---
title: "guidance — AI agent skill for llm applications"
description: "Constrains LLM output during generation with Guidance (Microsoft Research), using regex, select() choices, context-free grammars, token healing, and @guid…"
---

# `guidance`

> Constrains LLM output during generation with Guidance (Microsoft Research), using regex, select() choices, context-free grammars, token healing, and @guidance functions, with Anthropic, OpenAI, Transformers, and llama.cpp backends. Use when you need generated text to match a regex or fixed format such as dates, emails, or IDs. Use when you need guaranteed valid JSON, XML, or code from a model. Use when building multi-step generation workflows or ReAct-style agents with Python control flow. Use when classifying text into fixed categories with select(). Use when running local models and wanting grammar constraints. Not for Pydantic validation with automatic retries; use Instructor for that.

**Category:** [llm-applications](/skills#llm-applications) · **License:** MIT · **Version:** 1.0.0

## Install

```bash
npx skills add KalarisLabs/research-agent-skills --skill guidance
```

## When to use it

Constrains LLM output during generation with Guidance (Microsoft Research), using regex, select() choices, context-free grammars, token healing, and @guidance functions, with Anthropic, OpenAI, Transformers, and llama.cpp backends. Use when you need generated text to match a regex or fixed format such as dates, emails, or IDs. Use when you need guaranteed valid JSON, XML, or code from a model. Use when building multi-step generation workflows or ReAct-style agents with Python control flow. Use when classifying text into fixed categories with select(). Use when running local models and wanting grammar constraints. Not for Pydantic validation with automatic retries; use Instructor for that.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/guidance/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
