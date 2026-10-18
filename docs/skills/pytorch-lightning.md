---
title: "pytorch-lightning — AI agent skill for data science and ml"
description: "Organizes PyTorch training code with the lightning package (PyTorch Lightning): LightningModule, LightningDataModule, Trainer, callbacks such as…"
keywords: ["PyTorch Lightning", "deep learning", "model training", "multi-GPU", "machine learning"]
---

# `pytorch-lightning`

**Category:** [data-science-and-ml](/skills#data-science-and-ml) · **License:** Apache-2.0 license · **Version:** 1.2 · **Includes scripts**

**Tags:** PyTorch Lightning, deep learning, model training, multi-GPU, machine learning

## When to use it

Organizes PyTorch training code with the lightning package (PyTorch Lightning): LightningModule, LightningDataModule, Trainer, callbacks such as ModelCheckpoint and EarlyStopping, loggers (TensorBoard, W&B, MLflow, Comet, CSV), and multi-GPU/TPU strategies (DDP, FSDP, DeepSpeed). Use when structuring a PyTorch model into training, validation and test steps. Use when configuring a Trainer for multi-GPU or TPU runs. Use when writing a LightningDataModule for data loading. Use when adding checkpointing, early stopping or experiment logging to a training run. Use when choosing between DDP, FSDP and DeepSpeed for a model size. Not for plain PyTorch loops without Lightning.

## Example requests

Ask your agent in plain language, for example:

- *"How do I make my PyTorch model stop training when val loss stops improving and keep only the best 3 checkpoints?"*
- *"I'm training a 1.3B-parameter transformer defined in model.py on a node with 8x A100 80GB. My current script uses a hand-written train loop and I keep getting 'CUDA out of memory' with DDP. I'd like to move it into LightningModule/Trainer form and shard it. Can you restructure it with bf16 mixed precision and tell me which strategy to use?"*
- *"I have a folder of microscopy images with a CSV of labels. I want a reusable class that downloads/prepares them once, makes a reproducible 80/10/10 split, and hands out train, val and test loaders that work on multiple GPUs without each process redoing the preprocessing. How should I structure that?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill pytorch-lightning

# Kalaris Labs installer with checksum verification
npx research-agent-skills install pytorch-lightning
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `data-science-and-ml` category with `/plugin install data-science-and-ml@research-agent-skills`.

## Related

- [`deepspeed`](/skills/deepspeed)
- [`huggingface-accelerate`](/skills/huggingface-accelerate)
- [`experiment-tracking-swanlab`](/skills/experiment-tracking-swanlab)
- [`pytorch-lightning-distributed`](/skills/pytorch-lightning-distributed)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/pytorch-lightning/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
