---
title: "outlines — AI agent skill for llm applications"
description: "Generates guaranteed-valid structured output from LLMs with Outlines (dottxt.ai), constraining token sampling via finite state machines for JSON schemas…"
keywords: ["Prompt Engineering", "Outlines", "Structured Generation", "JSON Schema", "Pydantic", "Local Models", "Grammar-Based Generation", "vLLM", "Transformers", "Type Safety"]
---

# `outlines`

**Category:** [llm-applications](/skills#llm-applications) · **License:** MIT · **Version:** 1.0.0

**Tags:** Prompt Engineering, Outlines, Structured Generation, JSON Schema, Pydantic, Local Models, Grammar-Based Generation, vLLM, Transformers, Type Safety

## When to use it

Generates guaranteed-valid structured output from LLMs with Outlines (dottxt.ai), constraining token sampling via finite state machines for JSON schemas, Pydantic models, regex, choice lists, and integer/float types, on Transformers, llama.cpp, vLLM, and limited OpenAI backends. Use when you need output that always parses as valid JSON or matches a regex. Use when extracting typed data into Pydantic models from a local model. Use when classifying text into a fixed set of categories. Use when running batch structured generation on vLLM or Transformers. Use when controlling token sampling at the grammar level. Not for API models needing automatic retries (use Instructor).

## Example requests

Ask your agent in plain language, for example:

- *"How do I force a local Llama model to only output one of 'positive', 'negative', or 'neutral' for my tweets?"*
- *"I'm running Qwen2.5-7B-Instruct via vLLM on our lab GPU box and need to extract patient-free trial metadata from 2,000 abstracts in abstracts.jsonl into a Pydantic model (fields: sample_size int, design enum, primary_endpoint str, funding Optional[str]). My json.loads keeps failing on about 8% of outputs with 'Expecting , delimiter'. How do I make this always parse?"*
- *"I have a small local model and need every generated sample ID to look like 'SMP-2024-0001' (three letters, year, four digits), with no malformed IDs ever coming out. Can I enforce this at decoding time instead of filtering afterward?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill outlines

# Kalaris Labs installer with checksum verification
npx research-agent-skills install outlines
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `llm-applications` category with `/plugin install llm-applications@research-agent-skills`.

## Related

- [Skills for AI research](/fields/artificial-intelligence)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/outlines/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
