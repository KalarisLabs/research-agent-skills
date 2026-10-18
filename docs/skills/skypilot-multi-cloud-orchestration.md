---
title: "skypilot-multi-cloud-orchestration — AI agent skill for ml inference and ops"
description: "Multi-cloud orchestration for ML workloads with automatic cost optimization."
keywords: ["Infrastructure", "Multi-Cloud", "Orchestration", "GPU", "Cost Optimization", "SkyPilot"]
---

# `skypilot-multi-cloud-orchestration`

**Category:** [ml-inference-and-ops](/skills#ml-inference-and-ops) · **License:** MIT · **Version:** 1.0.0

**Tags:** Infrastructure, Multi-Cloud, Orchestration, GPU, Cost Optimization, SkyPilot

## When to use it

Multi-cloud orchestration for ML workloads with automatic cost optimization. Use when you need to run training or batch jobs across multiple clouds, leverage spot instances with auto-recovery, or optimize GPU costs across providers.

## Example requests

Ask your agent in plain language, for example:

- *"How do I get my training job to run on whichever cloud has the cheapest A100s right now?"*
- *"My spot instance on GCP keeps getting preempted halfway through fine-tuning llama-3-8b with train.py, and I lose everything each time. Checkpoints are written to /outputs. How do I make this resume automatically without babysitting it?"*
- *"I have a 4-node, 8xH100 pretraining run and a grant that lets me use credits on AWS, Azure and Lambda. I'd rather not rewrite my launch scripts for each provider. What's a sane way to set this up so the same job spec works everywhere and fails over if one is out of capacity?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill skypilot-multi-cloud-orchestration

# Kalaris Labs installer with checksum verification
npx research-agent-skills install skypilot-multi-cloud-orchestration
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-inference-and-ops` category with `/plugin install ml-inference-and-ops@research-agent-skills`.

## Related

- [`lambda-labs-gpu-cloud`](/skills/lambda-labs-gpu-cloud)
- [`modal-serverless-gpu`](/skills/modal-serverless-gpu)
- [`ray-train`](/skills/ray-train)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/skypilot-multi-cloud-orchestration/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
