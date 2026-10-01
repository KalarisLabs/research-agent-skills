---
title: "deepspeed — AI agent skill for ml training"
description: "Covers DeepSpeed for distributed deep learning training and I/O: ZeRO optimization stages, pipeline parallelism, FP16/BF16/FP8 training, 1-bit Adam, spars…"
---

# `deepspeed`

> Covers DeepSpeed for distributed deep learning training and I/O: ZeRO optimization stages, pipeline parallelism, FP16/BF16/FP8 training, 1-bit Adam, sparse attention, and DeepNVMe (aio_handle, gds_handle, async_io and gds operators, ds_nvme_tune, ds_report) for fast transfers between NVMe storage and host or GPU tensors. Use when configuring ZeRO stages for large-model training, enabling mixed precision or 1-bit Adam, offloading parameters or optimizer state to NVMe with ZeRO-Infinity, writing or reading tensors to files with blocking or non-blocking DeepNVMe calls, or tuning NVMe I/O settings such as block size, queue depth and parallelism. Not for plain PyTorch DistributedDataParallel without DeepSpeed.

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

## Install

```bash
npx skills add KalarisLabs/research-agent-skills --skill deepspeed
```

## When to use it

Covers DeepSpeed for distributed deep learning training and I/O: ZeRO optimization stages, pipeline parallelism, FP16/BF16/FP8 training, 1-bit Adam, sparse attention, and DeepNVMe (aio_handle, gds_handle, async_io and gds operators, ds_nvme_tune, ds_report) for fast transfers between NVMe storage and host or GPU tensors. Use when configuring ZeRO stages for large-model training, enabling mixed precision or 1-bit Adam, offloading parameters or optimizer state to NVMe with ZeRO-Infinity, writing or reading tensors to files with blocking or non-blocking DeepNVMe calls, or tuning NVMe I/O settings such as block size, queue depth and parallelism. Not for plain PyTorch DistributedDataParallel without DeepSpeed.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/deepspeed/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
