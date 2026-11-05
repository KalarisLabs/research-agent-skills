---
title: "evaluating-code-models — AI agent skill for ml evaluation and safety"
description: "Evaluates code generation models across HumanEval, MBPP, MultiPL-E, and 15+ benchmarks with pass@k metrics."
keywords: ["Evaluation", "Code Generation", "HumanEval", "MBPP", "MultiPL-E", "Pass@k", "BigCode", "Benchmarking", "Code Models"]
---

# `evaluating-code-models`

**Category:** [ml-evaluation-and-safety](/skills#ml-evaluation-and-safety) · **License:** MIT · **Version:** 1.0.0

**Tags:** Evaluation, Code Generation, HumanEval, MBPP, MultiPL-E, Pass@k, BigCode, Benchmarking, Code Models

## When to use it

Evaluates code generation models across HumanEval, MBPP, MultiPL-E, and 15+ benchmarks with pass@k metrics. Use when benchmarking code models, comparing coding abilities, testing multi-language support, or measuring code generation quality. Industry standard from BigCode Project used by HuggingFace leaderboards.

## Example requests

Ask your agent in plain language, for example:

- *"Run HumanEval on my StarCoder2-7B checkpoint and give me pass@1."*
- *"I've got a fine-tuned model at ./ckpt/mycoder-13b and I need pass@10 on HumanEval and MBPP for a paper table. I'm on a single A100 40GB and the last run hit CUDA out of memory with batch_size 8. Published numbers for the base model are about 5 points higher than what I get. How do I set this up properly?"*
- *"We want to know whether our code LLM is just as good at Rust, Go and Java as it is at Python. What's the best way to measure that and compare the languages fairly?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill evaluating-code-models

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills evaluating-code-models
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-evaluation-and-safety` category with `/plugin install ml-evaluation-and-safety@research-agent-skills`.

## Related

- [`evaluating-llms-harness`](/skills/evaluating-llms-harness)
- [`nemo-evaluator-sdk`](/skills/nemo-evaluator-sdk)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/evaluating-code-models/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
