---
title: "nanogpt — AI agent skill for ml training"
description: "Provides nanoGPT, Karpathy's minimal PyTorch GPT implementation (model.py and train.py), with workflows for training character-level Shakespeare on CPU, r…"
---

# `nanogpt`

> Provides nanoGPT, Karpathy's minimal PyTorch GPT implementation (model.py and train.py), with workflows for training character-level Shakespeare on CPU, reproducing GPT-2 124M on OpenWebText with multi-GPU torchrun, fine-tuning pretrained GPT-2 checkpoints, and training on custom text. Use when learning how GPT and transformer blocks work from scratch. Use when running a small training experiment on CPU or a single GPU. Use when modifying a transformer variant in plain PyTorch. Use when preparing character-level or BPE binary datasets. Use when troubleshooting out-of-memory or slow training in nanoGPT. Not for production or large-scale distributed training; use HuggingFace Transformers or Megatron-LM instead.

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

## Install

```bash
npx research-agent-skills install nanogpt
npx skills add KalarisLabs/research-agent-skills --skill nanogpt
```

## When to use it

Provides nanoGPT, Karpathy's minimal PyTorch GPT implementation (model.py and train.py), with workflows for training character-level Shakespeare on CPU, reproducing GPT-2 124M on OpenWebText with multi-GPU torchrun, fine-tuning pretrained GPT-2 checkpoints, and training on custom text. Use when learning how GPT and transformer blocks work from scratch. Use when running a small training experiment on CPU or a single GPU. Use when modifying a transformer variant in plain PyTorch. Use when preparing character-level or BPE binary datasets. Use when troubleshooting out-of-memory or slow training in nanoGPT. Not for production or large-scale distributed training; use HuggingFace Transformers or Megatron-LM instead.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/nanogpt/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
