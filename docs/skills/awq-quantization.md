---
title: "awq-quantization — AI agent skill for ml training"
description: "Activation-aware weight quantization for 4-bit LLM compression with 3x speedup and minimal accuracy loss."
---

# `awq-quantization`

> Activation-aware weight quantization for 4-bit LLM compression with 3x speedup and minimal accuracy loss. Use when deploying large models (7B-70B) on limited GPU memory, when you need faster inference than GPTQ with better accuracy preservation, or for instruction-tuned and multimodal models. MLSys 2024 Best Paper Award winner.

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

## Install

```bash
npx research-agent-skills install awq-quantization
npx skills add KalarisLabs/research-agent-skills --skill awq-quantization
```

## When to use it

Activation-aware weight quantization for 4-bit LLM compression with 3x speedup and minimal accuracy loss. Use when deploying large models (7B-70B) on limited GPU memory, when you need faster inference than GPTQ with better accuracy preservation, or for instruction-tuned and multimodal models. MLSys 2024 Best Paper Award winner.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/awq-quantization/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
