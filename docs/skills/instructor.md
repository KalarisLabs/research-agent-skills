---
title: "instructor — AI agent skill for llm applications"
description: "Extracts structured, validated data from LLM responses using the Instructor Python library with Pydantic response models, including nested models, enums,…"
---

# `instructor`

> Extracts structured, validated data from LLM responses using the Instructor Python library with Pydantic response models, including nested models, enums, custom validators, automatic retries with validation error feedback, and streaming of partial objects or iterables. Works with Anthropic, OpenAI, and local Ollama models. Use when pulling typed fields or entities out of free text, when classifying text into fixed categories, when an LLM must return JSON that passes schema validation, when failed extractions need automatic retry, or when streaming partial structured results. Not for prompt optimization (use DSPy) or building multi-step chains (use LangChain).

**Category:** [llm-applications](/skills#llm-applications) · **License:** MIT · **Version:** 1.0.0

## Install

```bash
npx skills add KalarisLabs/research-agent-skills --skill instructor
```

## When to use it

Extracts structured, validated data from LLM responses using the Instructor Python library with Pydantic response models, including nested models, enums, custom validators, automatic retries with validation error feedback, and streaming of partial objects or iterables. Works with Anthropic, OpenAI, and local Ollama models. Use when pulling typed fields or entities out of free text, when classifying text into fixed categories, when an LLM must return JSON that passes schema validation, when failed extractions need automatic retry, or when streaming partial structured results. Not for prompt optimization (use DSPy) or building multi-step chains (use LangChain).

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/instructor/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
