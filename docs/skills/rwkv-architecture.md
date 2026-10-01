---
title: "rwkv-architecture — AI agent skill for ml training"
description: "Covers the RWKV (Receptance Weighted Key Value) architecture, an RNN/Transformer hybrid with O(n) inference and no KV cache, including RWKV-7, its paralle…"
---

# `rwkv-architecture`

> Covers the RWKV (Receptance Weighted Key Value) architecture, an RNN/Transformer hybrid with O(n) inference and no KV cache, including RWKV-7, its parallel GPT-mode training and sequential RNN-mode inference, state passing, fine-tuning with DeepSpeed, and CUDA kernel setup. Use when generating text token by token with constant memory, processing very long contexts of 100K+ tokens, fine-tuning an RWKV model, comparing RWKV memory and speed against Transformers, or debugging RWKV state handling, loading, or out-of-memory errors. Prefer a standard Transformer when peak accuracy matters more than memory, and Mamba for state-space models.

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

## Install

```bash
npx skills add KalarisLabs/research-agent-skills --skill rwkv-architecture
```

## When to use it

Covers the RWKV (Receptance Weighted Key Value) architecture, an RNN/Transformer hybrid with O(n) inference and no KV cache, including RWKV-7, its parallel GPT-mode training and sequential RNN-mode inference, state passing, fine-tuning with DeepSpeed, and CUDA kernel setup. Use when generating text token by token with constant memory, processing very long contexts of 100K+ tokens, fine-tuning an RWKV model, comparing RWKV memory and speed against Transformers, or debugging RWKV state handling, loading, or out-of-memory errors. Prefer a standard Transformer when peak accuracy matters more than memory, and Mamba for state-space models.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/rwkv-architecture/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
