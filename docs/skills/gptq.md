---
title: "gptq — AI agent skill for ml training"
description: "Quantizes LLMs to 4-bit (also 3-bit) with GPTQ using group-wise quantization (group size 128 by default), via AutoGPTQ and transformers."
---

# `gptq`

> Quantizes LLMs to 4-bit (also 3-bit) with GPTQ using group-wise quantization (group size 128 by default), via AutoGPTQ and transformers. Covers loading pre-quantized GPTQ models, quantizing your own model, choosing group size, selecting ExLlamaV2, Marlin, or Triton kernels, and QLoRA fine-tuning with PEFT. Use when fitting 70B-class models onto limited or consumer GPUs, cutting memory about 4x versus FP16, speeding up inference, finding pre-quantized checkpoints on HuggingFace, or fine-tuning a quantized model with LoRA. For slightly better accuracy on newer GPUs use AWQ instead, and for simple 8-bit or on-the-fly quantization use bitsandbytes.

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

## Install

```bash
npx skills add KalarisLabs/research-agent-skills --skill gptq
```

## When to use it

Quantizes LLMs to 4-bit (also 3-bit) with GPTQ using group-wise quantization (group size 128 by default), via AutoGPTQ and transformers. Covers loading pre-quantized GPTQ models, quantizing your own model, choosing group size, selecting ExLlamaV2, Marlin, or Triton kernels, and QLoRA fine-tuning with PEFT. Use when fitting 70B-class models onto limited or consumer GPUs, cutting memory about 4x versus FP16, speeding up inference, finding pre-quantized checkpoints on HuggingFace, or fine-tuning a quantized model with LoRA. For slightly better accuracy on newer GPUs use AWQ instead, and for simple 8-bit or on-the-fly quantization use bitsandbytes.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/gptq/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
