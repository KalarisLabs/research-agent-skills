---
title: "llamaguard — AI agent skill for ml evaluation and safety"
description: "Classifies LLM prompts and responses as safe or unsafe using Meta's LlamaGuard (7B v1, 8B v2 and v3) across six categories: violence and hate, sexual content…"
keywords: ["Safety Alignment", "LlamaGuard", "Content Moderation", "Meta", "Guardrails", "Safety Classification", "Input Filtering", "Output Filtering", "AI Safety"]
---

# `llamaguard`

**Category:** [ml-evaluation-and-safety](/skills#ml-evaluation-and-safety) · **License:** MIT · **Version:** 1.0.0

**Tags:** Safety Alignment, LlamaGuard, Content Moderation, Meta, Guardrails, Safety Classification, Input Filtering, Output Filtering, AI Safety

## When to use it

Classifies LLM prompts and responses as safe or unsafe using Meta's LlamaGuard (7B v1, 8B v2 and v3) across six categories: violence and hate, sexual content, guns and illegal weapons, regulated substances, suicide and self-harm, and criminal planning. Covers HuggingFace Transformers and vLLM inference, a FastAPI moderation endpoint, Sagemaker deployment, and NeMo Guardrails integration. Use when filtering user prompts before an LLM call, moderating model outputs before display, serving a self-hosted moderation API, or reducing latency and GPU memory of a moderation model with vLLM or quantization. Use when tuning thresholds to cut false positives. For a simpler hosted option, use the OpenAI Moderation API instead.

## Example requests

Ask your agent in plain language, for example:

- *"How do I run LlamaGuard on user prompts before they hit my chatbot?"*
- *"I'm running Meta-Llama-Guard-3-8B through HF Transformers on a T4 in moderate.py and getting CUDA out of memory, plus each call takes ~450ms. I need to serve it to our team as an HTTP moderation endpoint. What should I change?"*
- *"Our assistant sometimes writes replies about drugs or self-harm that we don't want shown to users. I want a self-hosted classifier to check each model reply before display, and it's flagging too many harmless medical-education answers. How should I set this up and cut the false positives?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill llamaguard

# Kalaris Labs installer with checksum verification
npx research-agent-skills install llamaguard
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-evaluation-and-safety` category with `/plugin install ml-evaluation-and-safety@research-agent-skills`.

## Related

- [`nemo-guardrails`](/skills/nemo-guardrails)
- [`prompt-guard`](/skills/prompt-guard)
- [`serving-llms-vllm`](/skills/serving-llms-vllm)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/llamaguard/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
