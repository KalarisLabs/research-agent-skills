---
title: "modal — AI agent skill for data science and ml"
description: "Modal is a serverless cloud platform for running Python on demand, including on-demand GPUs."
keywords: ["serverless GPU", "cloud computing", "model deployment", "ML inference"]
---

# `modal`

**Category:** [data-science-and-ml](/skills#data-science-and-ml) · **License:** Apache-2.0 · **Version:** 1.3

**Tags:** serverless GPU, cloud computing, model deployment, ML inference

## When to use it

Modal is a serverless cloud platform for running Python on demand, including on-demand GPUs. Use when deploying or serving AI/ML models, running GPU-accelerated workloads (training, fine-tuning, inference), serving web endpoints, scheduling batch jobs, or scaling Python code to cloud containers with the Modal SDK.

## Example requests

Ask your agent in plain language, for example:

- *"How do I run my PyTorch script on an H100 without owning one?"*
- *"I'm fine-tuning Llama-3-8B with LoRA using train.py and my checkpoints keep vanishing when the container exits. I need to run it on 4 A100-80GB GPUs on Modal, keep the base weights cached between runs, and pull the HF_TOKEN from a secret. Can you restructure it?"*
- *"I have 5,000 protein FASTA files and a Python function that scores each one. It takes about 10 minutes per file on my laptop. I'd like it to fan out across lots of cloud machines, then run again automatically every Sunday night with the results collected in one place."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill modal

# Kalaris Labs installer with checksum verification
npx research-agent-skills install modal
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `data-science-and-ml` category with `/plugin install data-science-and-ml@research-agent-skills`.

## Related

- [`modal-serverless-gpu`](/skills/modal-serverless-gpu)
- [`serving-llms-vllm`](/skills/serving-llms-vllm)
- [`tensorrt-llm`](/skills/tensorrt-llm)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/modal/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
