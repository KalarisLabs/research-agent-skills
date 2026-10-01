---
title: "peft-fine-tuning — AI agent skill for ml training"
description: "Fine-tunes LLMs with Hugging Face PEFT, using LoRA, QLoRA, IA3, AdaLoRA, prefix tuning, and prompt tuning so that under 1% of parameters are trained."
---

# `peft-fine-tuning`

> Fine-tunes LLMs with Hugging Face PEFT, using LoRA, QLoRA, IA3, AdaLoRA, prefix tuning, and prompt tuning so that under 1% of parameters are trained. Covers rank, alpha, and target module selection, loading and merging adapters, multi-adapter serving, and integration with TRL SFTTrainer, Axolotl, and vLLM. Use when fine-tuning 7B-70B models on limited GPU memory, when running QLoRA on a single 24GB GPU, when choosing LoRA rank and alpha, when merging or swapping adapters on one base model, or when debugging CUDA OOM or an adapter that does not apply. Not for full fine-tuning of small models under 1B parameters or cases needing all weights updated.

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

## Install

```bash
npx skills add KalarisLabs/research-agent-skills --skill peft-fine-tuning
```

## When to use it

Fine-tunes LLMs with Hugging Face PEFT, using LoRA, QLoRA, IA3, AdaLoRA, prefix tuning, and prompt tuning so that under 1% of parameters are trained. Covers rank, alpha, and target module selection, loading and merging adapters, multi-adapter serving, and integration with TRL SFTTrainer, Axolotl, and vLLM. Use when fine-tuning 7B-70B models on limited GPU memory, when running QLoRA on a single 24GB GPU, when choosing LoRA rank and alpha, when merging or swapping adapters on one base model, or when debugging CUDA OOM or an adapter that does not apply. Not for full fine-tuning of small models under 1B parameters or cases needing all weights updated.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/peft-fine-tuning/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
