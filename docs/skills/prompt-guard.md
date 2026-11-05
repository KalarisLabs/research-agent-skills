---
title: "prompt-guard — AI agent skill for ml evaluation and safety"
description: "Classifies text with Meta's Prompt Guard, an 86M-parameter model loaded from HuggingFace, into BENIGN, INJECTION or JAILBREAK labels to detect prompt…"
keywords: ["Safety Alignment", "Prompt Injection", "Jailbreak Detection", "Meta", "Input Validation", "Security", "Content Filtering", "Multilingual"]
---

# `prompt-guard`

**Category:** [ml-evaluation-and-safety](/skills#ml-evaluation-and-safety) · **License:** MIT · **Version:** 1.0.0

**Tags:** Safety Alignment, Prompt Injection, Jailbreak Detection, Meta, Input Validation, Security, Content Filtering, Multilingual

## When to use it

Classifies text with Meta's Prompt Guard, an 86M-parameter model loaded from HuggingFace, into BENIGN, INJECTION or JAILBREAK labels to detect prompt injections and jailbreak attempts in LLM applications. Covers user input filtering, third-party data and RAG document filtering, batch processing, threshold tuning, and sliding-window handling of texts over 512 tokens. Use when screening user prompts for jailbreaks before they reach an LLM. Use when filtering API responses or retrieved RAG documents for embedded instructions. Use when batch-scanning documents for injection. Use when tuning detection thresholds or false positives on security-related queries. Use when running a lightweight CPU or GPU classifier for 8 languages. Not for content moderation such as violence or hate; use LlamaGuard for that.

## Example requests

Ask your agent in plain language, for example:

- *"Can you scan this folder of scraped web pages for hidden instructions before I feed them into my summarizer?"*
- *"I'm loading meta-llama/Prompt-Guard-86M with AutoModelForSequenceClassification on my laptop with no GPU. My security-research chatbot keeps flagging questions like 'how does SQL injection work?' as INJECTION, while 40% of my 6k-token retrieved PDFs seem to pass without any flags. How do I fix both?"*
- *"We're building a literature-search assistant that pulls abstracts and web snippets from external APIs into an LLM's context. I'm worried some of those snippets might contain text that tries to hijack the model's behavior. I want a small, cheap classifier that runs locally and can handle the French and Hindi content too. What should I set up?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill prompt-guard

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills prompt-guard
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-evaluation-and-safety` category with `/plugin install ml-evaluation-and-safety@research-agent-skills`.

## Related

- [`llamaguard`](/skills/llamaguard)
- [`nemo-guardrails`](/skills/nemo-guardrails)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/prompt-guard/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
