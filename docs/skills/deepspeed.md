---
title: "deepspeed — AI agent skill for ml training"
description: "Covers DeepSpeed for distributed deep learning training and I/O: ZeRO optimization stages, pipeline parallelism, FP16/BF16/FP8 training, 1-bit Adam, sparse…"
keywords: ["DeepSpeed", "Distributed Training", "ZeRO", "Pipeline Parallelism", "Mixed Precision", "Optimization", "Microsoft", "Large-Scale Training", "FP16", "FP8"]
---

# `deepspeed`

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

**Tags:** DeepSpeed, Distributed Training, ZeRO, Pipeline Parallelism, Mixed Precision, Optimization, Microsoft, Large-Scale Training, FP16, FP8

## When to use it

Covers DeepSpeed for distributed deep learning training and I/O: ZeRO optimization stages, pipeline parallelism, FP16/BF16/FP8 training, 1-bit Adam, sparse attention, and DeepNVMe (aio_handle, gds_handle, async_io and gds operators, ds_nvme_tune, ds_report) for fast transfers between NVMe storage and host or GPU tensors. Use when configuring ZeRO stages for large-model training, enabling mixed precision or 1-bit Adam, offloading parameters or optimizer state to NVMe with ZeRO-Infinity, writing or reading tensors to files with blocking or non-blocking DeepNVMe calls, or tuning NVMe I/O settings such as block size, queue depth and parallelism. Not for plain PyTorch DistributedDataParallel without DeepSpeed.

## Example requests

Ask your agent in plain language, for example:

- *"How do I turn on ZeRO stage 3 with CPU offload in my DeepSpeed config?"*
- *"I'm fine-tuning a 13B model on 8x A100 with train.py and keep getting CUDA OOM during optimizer step even at stage 2. We have a 3.2TB local NVMe at /local_nvme. Can I push optimizer states and params there? What should the config look like and how do I know my drive is being used efficiently?"*
- *"I need to checkpoint a big CUDA tensor to disk without stalling my training loop, ideally overlapping the write with compute. What's the fastest way using DeepSpeed's I/O tools?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill deepspeed

# Kalaris Labs installer with checksum verification
npx research-agent-skills install deepspeed
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-training` category with `/plugin install ml-training@research-agent-skills`.

## Related

- [`huggingface-accelerate`](/skills/huggingface-accelerate)
- [`pytorch-lightning`](/skills/pytorch-lightning)
- [`training-llms-megatron`](/skills/training-llms-megatron)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/deepspeed/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
