---
title: "peft-fine-tuning — AI agent skill for ml training"
description: "Fine-tunes LLMs with Hugging Face PEFT, using LoRA, QLoRA, IA3, AdaLoRA, prefix tuning, and prompt tuning so that under 1% of parameters are trained."
keywords: ["Fine-Tuning", "PEFT", "LoRA", "QLoRA", "Parameter-Efficient", "Adapters", "Low-Rank", "Memory Optimization", "Multi-Adapter"]
---

# `peft-fine-tuning`

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

**Tags:** Fine-Tuning, PEFT, LoRA, QLoRA, Parameter-Efficient, Adapters, Low-Rank, Memory Optimization, Multi-Adapter

## When to use it

Fine-tunes LLMs with Hugging Face PEFT, using LoRA, QLoRA, IA3, AdaLoRA, prefix tuning, and prompt tuning so that under 1% of parameters are trained. Covers rank, alpha, and target module selection, loading and merging adapters, multi-adapter serving, and integration with TRL SFTTrainer, Axolotl, and vLLM. Use when fine-tuning 7B-70B models on limited GPU memory, when running QLoRA on a single 24GB GPU, when choosing LoRA rank and alpha, when merging or swapping adapters on one base model, or when debugging CUDA OOM or an adapter that does not apply. Not for full fine-tuning of small models under 1B parameters or cases needing all weights updated.

## Example requests

Ask your agent in plain language, for example:

- *"How do I pick LoRA rank and alpha for a 13B model?"*
- *"I'm trying to QLoRA fine-tune Llama-3.1-8B on my 24GB RTX 4090 using train.jsonl with TRL's SFTTrainer, but I get 'CUDA out of memory' after about 40 steps at max_seq_length 4096. Here's my BitsAndBytesConfig and LoraConfig (r=64, all linear layers). What should I change?"*
- *"I have one base Mistral-7B and three small task-specific fine-tunes (summarization, SQL generation, and clinical note extraction). I want to serve all three from a single GPU without keeping three full copies of the weights in memory, and be able to switch between them per request. How should I set that up?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill peft-fine-tuning

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills peft-fine-tuning
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-training` category with `/plugin install ml-training@research-agent-skills`.

## Related

- [`axolotl`](/skills/axolotl)
- [`implementing-llms-litgpt`](/skills/implementing-llms-litgpt)
- [`ml-training-recipes`](/skills/ml-training-recipes)
- [`stable-diffusion-image-generation`](/skills/stable-diffusion-image-generation)
- [`unsloth`](/skills/unsloth)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/peft-fine-tuning/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
