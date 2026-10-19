---
title: "llama-factory — AI agent skill for ml training"
description: "Guides fine-tuning of large language models with LLaMA-Factory, covering the WebUI no-code interface, training across 100+ supported models, quantized QLoRA…"
keywords: ["Fine-Tuning", "LLaMA Factory", "LLM", "WebUI", "No-Code", "QLoRA", "LoRA", "Multimodal", "HuggingFace", "Llama", "Qwen", "Gemma"]
---

# `llama-factory`

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

**Tags:** Fine-Tuning, LLaMA Factory, LLM, WebUI, No-Code, QLoRA, LoRA, Multimodal, HuggingFace, Llama, Qwen, Gemma

## When to use it

Guides fine-tuning of large language models with LLaMA-Factory, covering the WebUI no-code interface, training across 100+ supported models, quantized QLoRA at 2/3/4/5/6/8-bit precision, and multimodal model support. Use when setting up or configuring a LLaMA-Factory fine-tuning run, choosing a quantization level for QLoRA training, using the WebUI instead of writing training code, fine-tuning a multimodal model, or debugging a LLaMA-Factory training error. Not for general-purpose inference serving or for other training frameworks; use the matching skill for those.

## Example requests

Ask your agent in plain language, for example:

- *"How do I launch the LLaMA-Factory WebUI to fine-tune a model without writing code?"*
- *"I'm running QLoRA on Qwen2-7B with LLaMA-Factory on a single 24GB RTX 4090, dataset is my_data.json registered in dataset_info.json. I get 'CUDA out of memory' at step 3 with quantization_bit 8, cutoff_len 4096, batch size 4. What should I change?"*
- *"I want to adapt a vision-language model to read chest X-ray images and produce short captions, using my own image-text pairs on one GPU with limited VRAM. Where do I start, and how can I make it fit in memory?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill llama-factory

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills llama-factory
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-training` category with `/plugin install ml-training@research-agent-skills`.

## Related

- [`axolotl`](/skills/axolotl)
- [`ml-training-recipes`](/skills/ml-training-recipes)
- [`unsloth`](/skills/unsloth)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/llama-factory/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
