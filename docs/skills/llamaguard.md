---
title: "llamaguard — AI agent skill for ml evaluation and safety"
description: "Classifies LLM prompts and responses as safe or unsafe using Meta's LlamaGuard (7B v1, 8B v2 and v3) across six categories: violence and hate, sexual cont…"
---

# `llamaguard`

> Classifies LLM prompts and responses as safe or unsafe using Meta's LlamaGuard (7B v1, 8B v2 and v3) across six categories: violence and hate, sexual content, guns and illegal weapons, regulated substances, suicide and self-harm, and criminal planning. Covers HuggingFace Transformers and vLLM inference, a FastAPI moderation endpoint, Sagemaker deployment, and NeMo Guardrails integration. Use when filtering user prompts before an LLM call, moderating model outputs before display, serving a self-hosted moderation API, or reducing latency and GPU memory of a moderation model with vLLM or quantization. Use when tuning thresholds to cut false positives. For a simpler hosted option, use the OpenAI Moderation API instead.

**Category:** [ml-evaluation-and-safety](/skills#ml-evaluation-and-safety) · **License:** MIT · **Version:** 1.0.0

## Install

```bash
npx skills add KalarisLabs/research-agent-skills --skill llamaguard
```

## When to use it

Classifies LLM prompts and responses as safe or unsafe using Meta's LlamaGuard (7B v1, 8B v2 and v3) across six categories: violence and hate, sexual content, guns and illegal weapons, regulated substances, suicide and self-harm, and criminal planning. Covers HuggingFace Transformers and vLLM inference, a FastAPI moderation endpoint, Sagemaker deployment, and NeMo Guardrails integration. Use when filtering user prompts before an LLM call, moderating model outputs before display, serving a self-hosted moderation API, or reducing latency and GPU memory of a moderation model with vLLM or quantization. Use when tuning thresholds to cut false positives. For a simpler hosted option, use the OpenAI Moderation API instead.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/llamaguard/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
