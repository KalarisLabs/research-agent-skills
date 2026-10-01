---
title: "nemo-guardrails — AI agent skill for ml evaluation and safety"
description: "Adds runtime safety rails to LLM applications with NVIDIA NeMo Guardrails, configured through Colang 2.0 flows."
---

# `nemo-guardrails`

> Adds runtime safety rails to LLM applications with NVIDIA NeMo Guardrails, configured through Colang 2.0 flows. Covers jailbreak and prompt-injection detection, self-check input/output validation, retrieval-based fact-checking, hallucination detection, PII filtering via Presidio, toxicity detection via ActiveFence, and LlamaGuard integration. Use when adding programmable safety rules to a production LLM app, blocking jailbreaks or prompt injection, filtering PII from model inputs and outputs, verifying generated claims against retrieved sources, or tuning false positives and latency of guardrail checks. For standalone moderation only, use LlamaGuard or the OpenAI Moderation API instead.

**Category:** [ml-evaluation-and-safety](/skills#ml-evaluation-and-safety) · **License:** MIT · **Version:** 1.0.0

## Install

```bash
npx research-agent-skills install nemo-guardrails
npx skills add KalarisLabs/research-agent-skills --skill nemo-guardrails
```

## When to use it

Adds runtime safety rails to LLM applications with NVIDIA NeMo Guardrails, configured through Colang 2.0 flows. Covers jailbreak and prompt-injection detection, self-check input/output validation, retrieval-based fact-checking, hallucination detection, PII filtering via Presidio, toxicity detection via ActiveFence, and LlamaGuard integration. Use when adding programmable safety rules to a production LLM app, blocking jailbreaks or prompt injection, filtering PII from model inputs and outputs, verifying generated claims against retrieved sources, or tuning false positives and latency of guardrail checks. For standalone moderation only, use LlamaGuard or the OpenAI Moderation API instead.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/nemo-guardrails/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
