---
title: "evaluating-llms-harness — AI agent skill for ml evaluation and safety"
description: "Evaluates LLMs across 60+ academic benchmarks (MMLU, HumanEval, GSM8K, TruthfulQA, HellaSwag)."
keywords: ["Evaluation", "LM Evaluation Harness", "Benchmarking", "MMLU", "HumanEval", "GSM8K", "EleutherAI", "Model Quality", "Academic Benchmarks", "Industry Standard"]
---

# `evaluating-llms-harness`

**Category:** [ml-evaluation-and-safety](/skills#ml-evaluation-and-safety) · **License:** MIT · **Version:** 1.0.0

**Tags:** Evaluation, LM Evaluation Harness, Benchmarking, MMLU, HumanEval, GSM8K, EleutherAI, Model Quality, Academic Benchmarks, Industry Standard

## When to use it

Evaluates LLMs across 60+ academic benchmarks (MMLU, HumanEval, GSM8K, TruthfulQA, HellaSwag). Use when benchmarking model quality, comparing models, reporting academic results, or tracking training progress. Industry standard used by EleutherAI, HuggingFace, and major labs. Supports HuggingFace, vLLM, APIs.

## Example requests

Ask your agent in plain language, for example:

- *"run MMLU and GSM8K on my llama-3-8b checkpoint"*
- *"I'm training a 1.3B model with a custom loop that saves checkpoints to ./ckpt/step_\{N\}. I want HellaSwag and PIQA numbers every 2000 steps so I can plot learning curves, but full MMLU takes too long. How should I set this up? Last time I got 'ValueError: Tasks not found: hellaswg' when I ran lm_eval."*
- *"We're deciding between Mistral-7B, Llama-3-8B and Qwen2-7B for an internal paper. I need a fair side-by-side on reasoning, truthfulness and common-sense tasks, and a table I can drop in the manuscript. Eval is slow on our single A100, so any speedup would help."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill evaluating-llms-harness

# Kalaris Labs installer with checksum verification
npx research-agent-skills install evaluating-llms-harness
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-evaluation-and-safety` category with `/plugin install ml-evaluation-and-safety@research-agent-skills`.

## Related

- [`evaluating-code-models`](/skills/evaluating-code-models)
- [`hqq-quantization`](/skills/hqq-quantization)
- [`nemo-evaluator-sdk`](/skills/nemo-evaluator-sdk)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/evaluating-llms-harness/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
