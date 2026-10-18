---
title: "implementing-llms-litgpt — AI agent skill for ml training"
description: "Implements and trains LLMs using Lightning AI's LitGPT with 20+ pretrained architectures (Llama, Gemma, Phi, Qwen, Mistral)."
keywords: ["Model Architecture", "LitGPT", "Lightning AI", "LLM Implementation", "LoRA", "QLoRA", "Fine-Tuning", "Llama", "Gemma", "Phi", "Mistral", "Educational"]
---

# `implementing-llms-litgpt`

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

**Tags:** Model Architecture, LitGPT, Lightning AI, LLM Implementation, LoRA, QLoRA, Fine-Tuning, Llama, Gemma, Phi, Mistral, Educational

## When to use it

Implements and trains LLMs using Lightning AI's LitGPT with 20+ pretrained architectures (Llama, Gemma, Phi, Qwen, Mistral). Use when need clean model implementations, educational understanding of architectures, or production fine-tuning with LoRA/QLoRA. Single-file implementations, no abstraction layers.

## Example requests

Ask your agent in plain language, for example:

- *"How do I LoRA fine-tune Phi-2 with litgpt on a 16GB GPU?"*
- *"I have 8k instruction/response pairs in data/lab_protocols.json in Alpaca format. I want to fine-tune Llama 3 1B using litgpt, but I get CUDA out of memory on my 12GB RTX 3060 when I run full finetuning. What should I change?"*
- *"I want to read the actual code of a Llama-style transformer, then train a small 1B model from scratch on my own tokenized domain corpus across 4 GPUs. I want clean single-file implementations, not a framework with many abstraction layers. What do you suggest, and how would I set it up?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill implementing-llms-litgpt

# Kalaris Labs installer with checksum verification
npx research-agent-skills install implementing-llms-litgpt
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-training` category with `/plugin install ml-training@research-agent-skills`.

## Related

- [`peft-fine-tuning`](/skills/peft-fine-tuning)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/implementing-llms-litgpt/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
