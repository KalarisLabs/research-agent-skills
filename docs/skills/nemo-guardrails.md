---
title: "nemo-guardrails — AI agent skill for ml evaluation and safety"
description: "Adds runtime safety rails to LLM applications with NVIDIA NeMo Guardrails, configured through Colang 2.0 flows."
keywords: ["Safety Alignment", "NeMo Guardrails", "NVIDIA", "Jailbreak Detection", "Guardrails", "Colang", "Runtime Safety", "Hallucination Detection", "PII Filtering", "Production"]
---

# `nemo-guardrails`

**Category:** [ml-evaluation-and-safety](/skills#ml-evaluation-and-safety) · **License:** MIT · **Version:** 1.0.0

**Tags:** Safety Alignment, NeMo Guardrails, NVIDIA, Jailbreak Detection, Guardrails, Colang, Runtime Safety, Hallucination Detection, PII Filtering, Production

## When to use it

Adds runtime safety rails to LLM applications with NVIDIA NeMo Guardrails, configured through Colang 2.0 flows. Covers jailbreak and prompt-injection detection, self-check input/output validation, retrieval-based fact-checking, hallucination detection, PII filtering via Presidio, toxicity detection via ActiveFence, and LlamaGuard integration. Use when adding programmable safety rules to a production LLM app, blocking jailbreaks or prompt injection, filtering PII from model inputs and outputs, verifying generated claims against retrieved sources, or tuning false positives and latency of guardrail checks. For standalone moderation only, use LlamaGuard or the OpenAI Moderation API instead.

## Example requests

Ask your agent in plain language, for example:

- *"How do I block jailbreaks in my chatbot with NeMo Guardrails?"*
- *"I have a RAG app for clinical trial summaries in ./app using LangChain and GPT-4o. Users sometimes paste patient names, phone numbers and MRNs into the chat, and the model sometimes states trial results that aren't in the retrieved PDFs. I want programmable rails so PII is masked on input and output and unsupported claims get caught before the answer is shown. I'm getting `ValueError: Could not find a rail named 'mask sensitive data on input'` when loading my config. How do I set this up?"*
- *"Our lab's LLM assistant is going to be deployed to students. I need a layer that sits between users and the model, lets me write rules in a declarative way for what topics it will refuse, checks answers for made-up facts against our document store, and adds under half a second of latency. Where do I start?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill nemo-guardrails

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills nemo-guardrails
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-evaluation-and-safety` category with `/plugin install ml-evaluation-and-safety@research-agent-skills`.

## Related

- [`llamaguard`](/skills/llamaguard)
- [`nemo-curator`](/skills/nemo-curator)
- [`langsmith-observability`](/skills/langsmith-observability)
- [`prompt-guard`](/skills/prompt-guard)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/nemo-guardrails/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
