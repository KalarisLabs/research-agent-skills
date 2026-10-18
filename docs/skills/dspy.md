---
title: "dspy — AI agent skill for llm applications"
description: "Builds and optimizes language model programs with DSPy (Stanford NLP), using Signatures, modules (Predict, ChainOfThought, ReAct, ProgramOfThought) and…"
keywords: ["Prompt Engineering", "DSPy", "Declarative Programming", "RAG", "Agents", "Prompt Optimization", "LM Programming", "Stanford NLP", "Automatic Optimization", "Modular AI"]
---

# `dspy`

**Category:** [llm-applications](/skills#llm-applications) · **License:** MIT · **Version:** 1.0.0 · **Includes scripts**

**Tags:** Prompt Engineering, DSPy, Declarative Programming, RAG, Agents, Prompt Optimization, LM Programming, Stanford NLP, Automatic Optimization, Modular AI

## When to use it

Builds and optimizes language model programs with DSPy (Stanford NLP), using Signatures, modules (Predict, ChainOfThought, ReAct, ProgramOfThought) and optimizers (BootstrapFewShot, MIPRO, BootstrapFinetune). Use when replacing hand-written prompts with declarative signatures, when automatically tuning prompts against training data and a metric, when building multi-stage RAG pipelines or ReAct agents, when building classifiers or structured-output programs, or when saving and evaluating optimized LM programs across providers such as Anthropic, OpenAI, or Ollama. Not for quick prototypes or simple chains; use manual prompting or LangChain instead.

## Example requests

Ask your agent in plain language, for example:

- *"How do I turn a dspy Signature into an optimized program?"*
- *"I have a hand-written few-shot prompt in prompts/triage.txt that classifies 2,000 clinical notes in notes_labeled.csv into 6 urgency classes with claude-sonnet. Accuracy is stuck around 71%. I'd like to port it to DSPy and use MIPROv2 to tune it, and I keep getting 'AttributeError: module dspy has no attribute OpenAI' when I configure the LM. Can you help?"*
- *"I'm building a question-answering system over our lab's 5,000 protocol PDFs. The retrieval step then answer generation needs to be tuned automatically against about 150 question/answer pairs I wrote, so I don't have to keep rewriting prompts by hand every time we swap the underlying model. What's a good approach?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill dspy

# Kalaris Labs installer with checksum verification
npx research-agent-skills install dspy
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `llm-applications` category with `/plugin install llm-applications@research-agent-skills`.

## Related

- [Skills for AI research](/fields/artificial-intelligence)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/dspy/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
