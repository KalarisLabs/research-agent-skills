---
title: "lambda-labs-gpu-cloud — AI agent skill for ml inference and ops"
description: "Reserved and on-demand GPU cloud instances for ML training and inference."
keywords: ["Infrastructure", "GPU Cloud", "Training", "Inference", "Lambda Labs"]
---

# `lambda-labs-gpu-cloud`

**Category:** [ml-inference-and-ops](/skills#ml-inference-and-ops) · **License:** MIT · **Version:** 1.0.0

**Tags:** Infrastructure, GPU Cloud, Training, Inference, Lambda Labs

## When to use it

Reserved and on-demand GPU cloud instances for ML training and inference. Use when you need dedicated GPU instances with simple SSH access, persistent filesystems, or high-performance multi-node clusters for large-scale training.

## Example requests

Ask your agent in plain language, for example:

- *"How do I attach a persistent filesystem to a Lambda instance? I launched one yesterday and can't see it."*
- *"I'm fine-tuning Llama-3 70B with FSDP using train.py and need a box with 8x H100 and SSH access for about 3 days. My checkpoints are ~140GB each and I don't want to lose them if I terminate. Walk me through launching it with curl against the Lambda API and getting my dataset onto it."*
- *"I need to train across 128 GPUs with fast interconnect for a pretraining run. What are my options for a managed Slurm cluster with InfiniBand?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill lambda-labs-gpu-cloud

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills lambda-labs-gpu-cloud
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-inference-and-ops` category with `/plugin install ml-inference-and-ops@research-agent-skills`.

## Related

- [`modal-serverless-gpu`](/skills/modal-serverless-gpu)
- [`skypilot-multi-cloud-orchestration`](/skills/skypilot-multi-cloud-orchestration)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/lambda-labs-gpu-cloud/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
