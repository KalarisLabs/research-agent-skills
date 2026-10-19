---
title: "instructor — AI agent skill for llm applications"
description: "Extracts structured, validated data from LLM responses using the Instructor Python library with Pydantic response models, including nested models, enums…"
keywords: ["Prompt Engineering", "Instructor", "Structured Output", "Pydantic", "Data Extraction", "JSON Parsing", "Type Safety", "Validation", "Streaming", "OpenAI", "Anthropic"]
---

# `instructor`

**Category:** [llm-applications](/skills#llm-applications) · **License:** MIT · **Version:** 1.0.0

**Tags:** Prompt Engineering, Instructor, Structured Output, Pydantic, Data Extraction, JSON Parsing, Type Safety, Validation, Streaming, OpenAI, Anthropic

## When to use it

Extracts structured, validated data from LLM responses using the Instructor Python library with Pydantic response models, including nested models, enums, custom validators, automatic retries with validation error feedback, and streaming of partial objects or iterables. Works with Anthropic, OpenAI, and local Ollama models. Use when pulling typed fields or entities out of free text, when classifying text into fixed categories, when an LLM must return JSON that passes schema validation, when failed extractions need automatic retry, or when streaming partial structured results. Not for prompt optimization (use DSPy) or building multi-step chains (use LangChain).

## Example requests

Ask your agent in plain language, for example:

- *"I have 300 free-text clinical trial abstracts. How do I get a typed Python object out of each one with sample size, intervention, and primary endpoint?"*
- *"pydantic ValidationError: 1 validation error for PaperMeta, year: Input should be less than or equal to 2026 [input_value=2206]. My extraction from Claude keeps failing on this. Can I make it fix itself instead of crashing?"*
- *"I'm labeling 5,000 patient forum posts as one of: symptom report, medication question, side effect, or other. The model's replies are sloppy and I need every answer to be exactly one of those labels as a Python value, running locally through Ollama. Best approach?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill instructor

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills instructor
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `llm-applications` category with `/plugin install llm-applications@research-agent-skills`.

## Related

- [Skills for AI research](/fields/artificial-intelligence)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/instructor/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
