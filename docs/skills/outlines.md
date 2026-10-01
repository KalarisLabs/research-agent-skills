---
title: "outlines — AI agent skill for llm applications"
description: "Generates guaranteed-valid structured output from LLMs with Outlines (dottxt.ai), constraining token sampling via finite state machines for JSON schemas,…"
---

# `outlines`

> Generates guaranteed-valid structured output from LLMs with Outlines (dottxt.ai), constraining token sampling via finite state machines for JSON schemas, Pydantic models, regex, choice lists, and integer/float types, on Transformers, llama.cpp, vLLM, and limited OpenAI backends. Use when you need output that always parses as valid JSON or matches a regex. Use when extracting typed data into Pydantic models from a local model. Use when classifying text into a fixed set of categories. Use when running batch structured generation on vLLM or Transformers. Use when controlling token sampling at the grammar level. Not for API models needing automatic retries (use Instructor).

**Category:** [llm-applications](/skills#llm-applications) · **License:** MIT · **Version:** 1.0.0

## Install

```bash
npx skills add KalarisLabs/research-agent-skills --skill outlines
```

## When to use it

Generates guaranteed-valid structured output from LLMs with Outlines (dottxt.ai), constraining token sampling via finite state machines for JSON schemas, Pydantic models, regex, choice lists, and integer/float types, on Transformers, llama.cpp, vLLM, and limited OpenAI backends. Use when you need output that always parses as valid JSON or matches a regex. Use when extracting typed data into Pydantic models from a local model. Use when classifying text into a fixed set of categories. Use when running batch structured generation on vLLM or Transformers. Use when controlling token sampling at the grammar level. Not for API models needing automatic retries (use Instructor).

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/outlines/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
