---
title: "langsmith-observability — AI agent skill for ml inference and ops"
description: "LLM observability platform for tracing, evaluation, and monitoring."
keywords: ["Observability", "LangSmith", "Tracing", "Evaluation", "Monitoring", "Debugging", "Testing", "LLM Ops", "Production"]
---

# `langsmith-observability`

**Category:** [ml-inference-and-ops](/skills#ml-inference-and-ops) · **License:** MIT · **Version:** 1.0.0

**Tags:** Observability, LangSmith, Tracing, Evaluation, Monitoring, Debugging, Testing, LLM Ops, Production

## When to use it

LLM observability platform for tracing, evaluation, and monitoring. Use when debugging LLM applications, evaluating model outputs against datasets, monitoring production systems, or building systematic testing pipelines for AI applications.

## Example requests

Ask your agent in plain language, for example:

- *"How do I get LangSmith tracing working on my OpenAI calls?"*
- *"My RAG pipeline in rag_pipeline.py uses Claude through the Anthropic SDK. I have 200 question/answer pairs in qa_gold.csv and I want to run them all through it, score each answer for correctness, and compare two prompt versions in LangSmith. I'm getting 'Traces not appearing' in my project, and the runs show up under 'default'. Can you help?"*
- *"Our lab's literature-summarization assistant is going to be used by about 50 grad students next month. I need to find out why some responses take 30 seconds, how much each query costs in tokens, and set it up so a failing summary gets caught before we ship a new prompt version. I'd also like to collect thumbs up/down from users. What should I set up?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill langsmith-observability

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills langsmith-observability
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-inference-and-ops` category with `/plugin install ml-inference-and-ops@research-agent-skills`.

## Related

- [`phoenix-observability`](/skills/phoenix-observability)
- [`llamaindex`](/skills/llamaindex)
- [`nemo-guardrails`](/skills/nemo-guardrails)
- [`pyvene-interventions`](/skills/pyvene-interventions)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/langsmith-observability/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
