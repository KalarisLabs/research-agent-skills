---
title: "nemo-evaluator-sdk — AI agent skill for ml evaluation and safety"
description: "Evaluates LLMs across 100+ benchmarks from 18+ harnesses (MMLU, HumanEval, GSM8K, safety, VLM) with multi-backend execution."
keywords: ["Evaluation", "NeMo", "NVIDIA", "Benchmarking", "MMLU", "HumanEval", "Multi-Backend", "Slurm", "Docker", "Reproducible", "Enterprise"]
---

# `nemo-evaluator-sdk`

**Category:** [ml-evaluation-and-safety](/skills#ml-evaluation-and-safety) · **License:** MIT · **Version:** 1.0.0

**Tags:** Evaluation, NeMo, NVIDIA, Benchmarking, MMLU, HumanEval, Multi-Backend, Slurm, Docker, Reproducible, Enterprise

## When to use it

Evaluates LLMs across 100+ benchmarks from 18+ harnesses (MMLU, HumanEval, GSM8K, safety, VLM) with multi-backend execution. Use when needing scalable evaluation on local Docker, Slurm HPC, or cloud platforms. NVIDIA's enterprise-grade platform with container-first architecture for reproducible benchmarking.

## Example requests

Ask your agent in plain language, for example:

- *"How do I run MMLU and GSM8K on my vLLM endpoint with nemo evaluator?"*
- *"I need to benchmark llama-3.1-70b on mmlu, gpqa_diamond and ifeval on our Slurm cluster. The job sits in PENDING forever and `nemo-evaluator-launcher status` shows nothing useful. Here's my slurm config: account=ml-eval, partition=gpu_a100, nodes=2. How should I debug it and set up the deployment correctly?"*
- *"We're comparing three finetuned checkpoints on the same set of academic, safety and vision-language benchmarks, all in reproducible containers on our HPC cluster, and want the results pushed into W&B. What's the best way to set that up?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill nemo-evaluator-sdk

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills nemo-evaluator-sdk
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-evaluation-and-safety` category with `/plugin install ml-evaluation-and-safety@research-agent-skills`.

## Related

- [`evaluating-code-models`](/skills/evaluating-code-models)
- [`evaluating-llms-harness`](/skills/evaluating-llms-harness)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/nemo-evaluator-sdk/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
