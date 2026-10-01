---
title: "huggingface-accelerate — AI agent skill for ml training"
description: "Wraps existing PyTorch training scripts with HuggingFace Accelerate (Accelerator class, accelerate config, accelerate launch) so the same code runs on CPU…"
---

# `huggingface-accelerate`

> Wraps existing PyTorch training scripts with HuggingFace Accelerate (Accelerator class, accelerate config, accelerate launch) so the same code runs on CPU, single GPU, multi-GPU, multi-node, TPU, or Apple MPS. Covers device placement, FP16/BF16/FP8 mixed precision, gradient accumulation, distributed checkpointing, and switching between DDP, DeepSpeed ZeRO, FSDP, and Megatron backends. Use when converting a single-GPU script to multi-GPU, enabling mixed precision, configuring DeepSpeed ZeRO or FSDP, or setting up gradient accumulation. Use when one script must run on different hardware. Not for callback-heavy training loops (use PyTorch Lightning) or multi-node orchestration with hyperparameter tuning (use Ray Train).

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

## Install

```bash
npx skills add KalarisLabs/research-agent-skills --skill huggingface-accelerate
```

## When to use it

Wraps existing PyTorch training scripts with HuggingFace Accelerate (Accelerator class, accelerate config, accelerate launch) so the same code runs on CPU, single GPU, multi-GPU, multi-node, TPU, or Apple MPS. Covers device placement, FP16/BF16/FP8 mixed precision, gradient accumulation, distributed checkpointing, and switching between DDP, DeepSpeed ZeRO, FSDP, and Megatron backends. Use when converting a single-GPU script to multi-GPU, enabling mixed precision, configuring DeepSpeed ZeRO or FSDP, or setting up gradient accumulation. Use when one script must run on different hardware. Not for callback-heavy training loops (use PyTorch Lightning) or multi-node orchestration with hyperparameter tuning (use Ray Train).

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/huggingface-accelerate/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
