---
title: "quantizing-models-bitsandbytes — AI agent skill for ml training"
description: "Quantizes LLMs to 8-bit or 4-bit for 50-75% memory reduction with minimal accuracy loss."
keywords: ["Optimization", "Bitsandbytes", "Quantization", "8-Bit", "4-Bit", "Memory Optimization", "QLoRA", "NF4", "INT8", "HuggingFace", "Efficient Inference"]
---

# `quantizing-models-bitsandbytes`

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

**Tags:** Optimization, Bitsandbytes, Quantization, 8-Bit, 4-Bit, Memory Optimization, QLoRA, NF4, INT8, HuggingFace, Efficient Inference

## When to use it

Quantizes LLMs to 8-bit or 4-bit for 50-75% memory reduction with minimal accuracy loss. Use when GPU memory is limited, need to fit larger models, or want faster inference. Supports INT8, NF4, FP4 formats, QLoRA training, and 8-bit optimizers. Works with HuggingFace Transformers.

## Example requests

Ask your agent in plain language, for example:

- *"how do i load llama 2 13b in 4-bit on my 12GB 3060?"*
- *"I'm fine-tuning Mistral-7B on my instruction dataset `train.jsonl` with a single 24GB RTX 4090. Full-precision LoRA hits `torch.cuda.OutOfMemoryError` at step 0 with batch size 8. Can you set it up so it fits? I'd like to use the HF Trainer and keep the loss comparable to what I got on the A100."*
- *"My lab only has a couple of older 16GB GPUs, and I need to run a 7B language model for inference and also cut the optimizer state memory while training a small adapter. What's the least invasive way to shrink memory without changing my HuggingFace code much?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill quantizing-models-bitsandbytes

# Kalaris Labs installer with checksum verification
npx research-agent-skills install quantizing-models-bitsandbytes
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-training` category with `/plugin install ml-training@research-agent-skills`.

## Related

- [`awq-quantization`](/skills/awq-quantization)
- [`blip-2-vision-language`](/skills/blip-2-vision-language)
- [`gptq`](/skills/gptq)
- [`hqq-quantization`](/skills/hqq-quantization)
- [`model-pruning`](/skills/model-pruning)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/quantizing-models-bitsandbytes/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
