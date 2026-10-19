---
title: "phoenix-observability — AI agent skill for ml inference and ops"
description: "Open-source AI observability platform for LLM tracing, evaluation, and monitoring."
keywords: ["Observability", "Phoenix", "Arize", "Tracing", "Evaluation", "Monitoring", "LLM Ops", "OpenTelemetry"]
---

# `phoenix-observability`

**Category:** [ml-inference-and-ops](/skills#ml-inference-and-ops) · **License:** MIT · **Version:** 1.0.0

**Tags:** Observability, Phoenix, Arize, Tracing, Evaluation, Monitoring, LLM Ops, OpenTelemetry

## When to use it

Open-source AI observability platform for LLM tracing, evaluation, and monitoring. Use when debugging LLM applications with detailed traces, running evaluations on datasets, or monitoring production AI systems with real-time insights.

## Example requests

Ask your agent in plain language, for example:

- *"How do I get Phoenix tracing running locally for my OpenAI calls?"*
- *"I'm running a RAG pipeline in LlamaIndex over our lab's protocol PDFs. The answers are sometimes wrong and I can't tell if retrieval or generation is at fault. I set up Phoenix at localhost:6006 but my project shows no traces, only an empty 'default' project. How do I fix that and then use the traces to find the failing step?"*
- *"I have 200 question-answer pairs from our clinical-trial summarization model and want to systematically score hallucination and relevance with an LLM judge, compare two prompt versions, and keep the test set versioned so I can rerun it in CI. Self-hosted only, no SaaS. What setup do you recommend?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill phoenix-observability

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills phoenix-observability
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-inference-and-ops` category with `/plugin install ml-inference-and-ops@research-agent-skills`.

## Related

- [`evaluating-cosmos-policy`](/skills/evaluating-cosmos-policy)
- [`langsmith-observability`](/skills/langsmith-observability)
- [`speculative-decoding`](/skills/speculative-decoding)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/phoenix-observability/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
