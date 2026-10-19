---
title: "unsloth — AI agent skill for ml training"
description: "Provides guidance on fine-tuning large language models with Unsloth, a library for faster, lower-memory training using LoRA and QLoRA, based on its official…"
keywords: ["Fine-Tuning", "Unsloth", "Fast Training", "LoRA", "QLoRA", "Memory-Efficient", "Optimization", "Llama", "Mistral", "Gemma", "Qwen"]
---

# `unsloth`

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

**Tags:** Fine-Tuning, Unsloth, Fast Training, LoRA, QLoRA, Memory-Efficient, Optimization, Llama, Mistral, Gemma, Qwen

## When to use it

Provides guidance on fine-tuning large language models with Unsloth, a library for faster, lower-memory training using LoRA and QLoRA, based on its official documentation (references/llms-txt.md). Use when setting up LoRA or QLoRA fine-tuning of an LLM with Unsloth, reducing GPU memory use during training, looking up Unsloth features or APIs, debugging Unsloth training code, or learning Unsloth best practices. Not for general model training with plain Hugging Face Transformers or PEFT without Unsloth.

## Example requests

Ask your agent in plain language, for example:

- *"How do I load Llama 3 8B in 4-bit with Unsloth and add LoRA adapters?"*
- *"I'm fine-tuning Qwen2.5-7B with Unsloth on my 24GB RTX 4090 using train.py and a JSONL file, data/clinical_notes.jsonl, with 'instruction' and 'response' fields. It crashes with 'torch.OutOfMemoryError: CUDA out of memory' at step 12 with max_seq_length=8192 and per_device_train_batch_size=4. What should I change?"*
- *"I have a single consumer GPU with 16GB VRAM and want to adapt a 8B open-weight model to answer questions in my lab's protocol style, using as little memory and time as possible. Which library and setup would speed up the training and cut memory use, and how would I export the result to GGUF for local use?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill unsloth

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills unsloth
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-training` category with `/plugin install ml-training@research-agent-skills`.

## Related

- [`llama-factory`](/skills/llama-factory)
- [`peft-fine-tuning`](/skills/peft-fine-tuning)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/unsloth/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
