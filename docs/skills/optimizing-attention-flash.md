---
title: "optimizing-attention-flash — AI agent skill for ml training"
description: "Enables Flash Attention for transformer models using PyTorch native scaled_dot_product_attention (PyTorch 2.2+) or the flash-attn library, including multi…"
---

# `optimizing-attention-flash`

> Enables Flash Attention for transformer models using PyTorch native scaled_dot_product_attention (PyTorch 2.2+) or the flash-attn library, including multi-query attention, sliding window attention, and FP8 on H100 (FlashAttention-3). Covers profiling speedup, checking accuracy against a baseline, and troubleshooting install and GPU support errors. Use when training or running transformers on long sequences (over 512 tokens), when standard attention runs out of GPU memory, when attention is the inference bottleneck, when switching a PyTorch model to the flash backend, or when tuning attention on H100 GPUs. Not for CPU inference, V100 GPUs, or sequences under 256 tokens; consider xFormers for other attention variants.

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

## Install

```bash
npx research-agent-skills install optimizing-attention-flash
npx skills add KalarisLabs/research-agent-skills --skill optimizing-attention-flash
```

## When to use it

Enables Flash Attention for transformer models using PyTorch native scaled_dot_product_attention (PyTorch 2.2+) or the flash-attn library, including multi-query attention, sliding window attention, and FP8 on H100 (FlashAttention-3). Covers profiling speedup, checking accuracy against a baseline, and troubleshooting install and GPU support errors. Use when training or running transformers on long sequences (over 512 tokens), when standard attention runs out of GPU memory, when attention is the inference bottleneck, when switching a PyTorch model to the flash backend, or when tuning attention on H100 GPUs. Not for CPU inference, V100 GPUs, or sequences under 256 tokens; consider xFormers for other attention variants.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/optimizing-attention-flash/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
