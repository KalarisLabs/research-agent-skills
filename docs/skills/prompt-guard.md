---
title: "prompt-guard — AI agent skill for ml evaluation and safety"
description: "Classifies text with Meta's Prompt Guard, an 86M-parameter model loaded from HuggingFace, into BENIGN, INJECTION or JAILBREAK labels to detect prompt inje…"
---

# `prompt-guard`

> Classifies text with Meta's Prompt Guard, an 86M-parameter model loaded from HuggingFace, into BENIGN, INJECTION or JAILBREAK labels to detect prompt injections and jailbreak attempts in LLM applications. Covers user input filtering, third-party data and RAG document filtering, batch processing, threshold tuning, and sliding-window handling of texts over 512 tokens. Use when screening user prompts for jailbreaks before they reach an LLM. Use when filtering API responses or retrieved RAG documents for embedded instructions. Use when batch-scanning documents for injection. Use when tuning detection thresholds or false positives on security-related queries. Use when running a lightweight CPU or GPU classifier for 8 languages. Not for content moderation such as violence or hate; use LlamaGuard for that.

**Category:** [ml-evaluation-and-safety](/skills#ml-evaluation-and-safety) · **License:** MIT · **Version:** 1.0.0

## Install

```bash
npx skills add KalarisLabs/research-agent-skills --skill prompt-guard
```

## When to use it

Classifies text with Meta's Prompt Guard, an 86M-parameter model loaded from HuggingFace, into BENIGN, INJECTION or JAILBREAK labels to detect prompt injections and jailbreak attempts in LLM applications. Covers user input filtering, third-party data and RAG document filtering, batch processing, threshold tuning, and sliding-window handling of texts over 512 tokens. Use when screening user prompts for jailbreaks before they reach an LLM. Use when filtering API responses or retrieved RAG documents for embedded instructions. Use when batch-scanning documents for injection. Use when tuning detection thresholds or false positives on security-related queries. Use when running a lightweight CPU or GPU classifier for 8 languages. Not for content moderation such as violence or hate; use LlamaGuard for that.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/prompt-guard/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
