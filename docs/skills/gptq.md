---
title: "gptq — AI agent skill for ml training"
description: "Quantizes LLMs to 4-bit (also 3-bit) with GPTQ using group-wise quantization (group size 128 by default), via AutoGPTQ and transformers."
keywords: ["Optimization", "GPTQ", "Quantization", "4-Bit", "Post-Training", "Memory Optimization", "Consumer GPUs", "Fast Inference", "QLoRA", "Group-Wise Quantization"]
---

# `gptq`

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

**Tags:** Optimization, GPTQ, Quantization, 4-Bit, Post-Training, Memory Optimization, Consumer GPUs, Fast Inference, QLoRA, Group-Wise Quantization

## When to use it

Quantizes LLMs to 4-bit (also 3-bit) with GPTQ using group-wise quantization (group size 128 by default), via AutoGPTQ and transformers. Covers loading pre-quantized GPTQ models, quantizing your own model, choosing group size, selecting ExLlamaV2, Marlin, or Triton kernels, and QLoRA fine-tuning with PEFT. Use when fitting 70B-class models onto limited or consumer GPUs, cutting memory about 4x versus FP16, speeding up inference, finding pre-quantized checkpoints on HuggingFace, or fine-tuning a quantized model with LoRA. For slightly better accuracy on newer GPUs use AWQ instead, and for simple 8-bit or on-the-fly quantization use bitsandbytes.

## Example requests

Ask your agent in plain language, for example:

- *"How do I get a 70B model running on a single 80GB A100 with GPTQ?"*
- *"I have a fine-tuned Mistral-7B at ./mistral-7b-legal and want to quantize it to 4-bit with AutoGPTQ using 512 samples from wikitext2 as calibration data. I'm on an RTX 3090 and my first attempt crashed with CUDA out of memory during layer-wise quantization. What config should I use and how do I fix the OOM?"*
- *"I want to fine-tune a 13B chat model on my lab's protein-function Q&A dataset, but I only have one 24GB consumer card. The weights are already compressed to 4 bits by calibrating on a small dataset with Hessian-based error correction, from a TheBloke repo. Which kernel should I use for fast inference, and how do I attach adapters for training?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill gptq

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills gptq
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-training` category with `/plugin install ml-training@research-agent-skills`.

## Related

- [`awq-quantization`](/skills/awq-quantization)
- [`hqq-quantization`](/skills/hqq-quantization)
- [`quantizing-models-bitsandbytes`](/skills/quantizing-models-bitsandbytes)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/gptq/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
