---
title: "training-llms-megatron — AI agent skill for ml training"
description: "Trains large language models (2B-462B parameters) with NVIDIA Megatron-Core using tensor, pipeline, sequence, context, and expert parallelism, plus FP8 on…"
---

# `training-llms-megatron`

> Trains large language models (2B-462B parameters) with NVIDIA Megatron-Core using tensor, pipeline, sequence, context, and expert parallelism, plus FP8 on H100 and MoE configuration for Mixtral-style models. Covers choosing TP/PP/DP/CP sizes, launching distributed training, tuning micro-batch size, and fixing low MFU, out-of-memory errors, and diverging loss. Use when training models above 10B parameters on NVIDIA A100/H100 GPUs, when setting up 3D parallelism for a LLaMA-style model, when configuring expert parallelism for MoE training, or when trying to raise MFU toward 40-47%. Use PyTorch FSDP, DeepSpeed, or HuggingFace Accelerate instead for models under 70B or simpler setups.

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

## Install

```bash
npx research-agent-skills install training-llms-megatron
npx skills add KalarisLabs/research-agent-skills --skill training-llms-megatron
```

## When to use it

Trains large language models (2B-462B parameters) with NVIDIA Megatron-Core using tensor, pipeline, sequence, context, and expert parallelism, plus FP8 on H100 and MoE configuration for Mixtral-style models. Covers choosing TP/PP/DP/CP sizes, launching distributed training, tuning micro-batch size, and fixing low MFU, out-of-memory errors, and diverging loss. Use when training models above 10B parameters on NVIDIA A100/H100 GPUs, when setting up 3D parallelism for a LLaMA-style model, when configuring expert parallelism for MoE training, or when trying to raise MFU toward 40-47%. Use PyTorch FSDP, DeepSpeed, or HuggingFace Accelerate instead for models under 70B or simpler setups.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/training-llms-megatron/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
