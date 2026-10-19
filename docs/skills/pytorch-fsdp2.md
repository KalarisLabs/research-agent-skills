---
title: "pytorch-fsdp2 — AI agent skill for ml training"
description: "Adds PyTorch FSDP2 (fully_shard) to training scripts with correct init, sharding, mixed precision/offload config, and distributed checkpointing."
keywords: ["PyTorch", "FSDP2", "Fully Sharded Data Parallel", "Distributed Training", "DTensor", "Device Mesh", "Sharded Checkpointing", "Mixed Precision", "Offload", "Torch Distributed"]
---

# `pytorch-fsdp2`

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

**Tags:** PyTorch, FSDP2, Fully Sharded Data Parallel, Distributed Training, DTensor, Device Mesh, Sharded Checkpointing, Mixed Precision, Offload, Torch Distributed

## When to use it

Adds PyTorch FSDP2 (fully_shard) to training scripts with correct init, sharding, mixed precision/offload config, and distributed checkpointing. Use when models exceed single-GPU memory or when you need DTensor-based sharding with DeviceMesh.

## Example requests

Ask your agent in plain language, for example:

- *"convert my train.py to FSDP2"*
- *"I'm fine-tuning a 13B Llama in finetune.py on 8xA100 and get CUDA OOM during optimizer.step() with DDP. I'd like to shard params, grads and optimizer state with the new per-parameter DTensor approach (not the old FSDP1 wrapper), use bf16 with fp32 gradient reduction, and save checkpoints that I can reload on a different number of GPUs. Can you update the script?"*
- *"My model's weights, gradients and Adam states don't fit in one GPU's memory, but I have a node with 4 GPUs. I want training to split the memory across them while still doing data parallelism, and later I might add tensor parallelism with a 2D device mesh. How should I set up my PyTorch training loop?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill pytorch-fsdp2

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills pytorch-fsdp2
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-training` category with `/plugin install ml-training@research-agent-skills`.

## Related

- [`distributed-llm-pretraining-torchtitan`](/skills/distributed-llm-pretraining-torchtitan)
- [`huggingface-accelerate`](/skills/huggingface-accelerate)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/pytorch-fsdp2/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
