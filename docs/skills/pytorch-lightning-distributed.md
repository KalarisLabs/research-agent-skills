---
title: "pytorch-lightning-distributed — AI agent skill for ml training"
description: "High-level PyTorch framework with Trainer class, automatic distributed training (DDP/FSDP/DeepSpeed), callbacks system, and minimal boilerplate."
keywords: ["PyTorch Lightning", "Training Framework", "Distributed Training", "DDP", "FSDP", "DeepSpeed", "High-Level API", "Callbacks", "Best Practices", "Scalable"]
---

# `pytorch-lightning-distributed`

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

**Tags:** PyTorch Lightning, Training Framework, Distributed Training, DDP, FSDP, DeepSpeed, High-Level API, Callbacks, Best Practices, Scalable

## When to use it

High-level PyTorch framework with Trainer class, automatic distributed training (DDP/FSDP/DeepSpeed), callbacks system, and minimal boilerplate. Scales from laptop to supercomputer with same code. Use when you want clean training loops with built-in best practices.

## Example requests

Ask your agent in plain language, for example:

- *"How do I turn my plain PyTorch training loop into a Lightning Trainer setup with DDP on 4 GPUs?"*
- *"I'm training a ResNet-50 on my cell-imaging dataset (train.py) on a 2-node cluster, 8 A100s each. Job launched with sbatch but I get 'RuntimeError: Timed out initializing process group in store based barrier' and Lightning seems to spawn extra processes. How do I set up the Trainer so it works across both nodes?"*
- *"I want my model training to automatically save the 3 best checkpoints by validation loss, stop if it hasn't improved in 5 epochs, and log the learning rate, without writing all that loop code myself. What's the cleanest way to do it in PyTorch?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill pytorch-lightning-distributed

# Kalaris Labs installer with checksum verification
npx research-agent-skills install pytorch-lightning-distributed
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-training` category with `/plugin install ml-training@research-agent-skills`.

## Related

- [`huggingface-accelerate`](/skills/huggingface-accelerate)
- [`pytorch-lightning`](/skills/pytorch-lightning)
- [`ray-train`](/skills/ray-train)
- [`torchforge-rl-training`](/skills/torchforge-rl-training)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/pytorch-lightning-distributed/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
