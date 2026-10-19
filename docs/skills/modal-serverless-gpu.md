---
title: "modal-serverless-gpu — AI agent skill for ml inference and ops"
description: "Serverless GPU cloud platform for running ML workloads."
keywords: ["Infrastructure", "Serverless", "GPU", "Cloud", "Deployment", "Modal"]
---

# `modal-serverless-gpu`

**Category:** [ml-inference-and-ops](/skills#ml-inference-and-ops) · **License:** MIT · **Version:** 1.0.0

**Tags:** Infrastructure, Serverless, GPU, Cloud, Deployment, Modal

## When to use it

Serverless GPU cloud platform for running ML workloads. Use when you need on-demand GPU access without infrastructure management, deploying ML models as APIs, or running batch jobs with automatic scaling.

## Example requests

Ask your agent in plain language, for example:

- *"How do I run my PyTorch script on an H100 on Modal without setting up any servers?"*
- *"I have a Llama-3-8B model in a Modal Volume called 'llama-weights' and want to serve it as an HTTP endpoint from serve.py. Cold starts are taking 40+ seconds and I sometimes get CUDA out of memory on an A10G. What should I change?"*
- *"I need to embed about 2 million protein sequences with ESM-2 by tomorrow. I don't have a GPU cluster and don't want to buy or administer any hardware, and I'd like it to scale out automatically and only pay while it's running. What are my options?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill modal-serverless-gpu

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills modal-serverless-gpu
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-inference-and-ops` category with `/plugin install ml-inference-and-ops@research-agent-skills`.

## Related

- [`lambda-labs-gpu-cloud`](/skills/lambda-labs-gpu-cloud)
- [`modal`](/skills/modal)
- [`skypilot-multi-cloud-orchestration`](/skills/skypilot-multi-cloud-orchestration)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/modal-serverless-gpu/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
