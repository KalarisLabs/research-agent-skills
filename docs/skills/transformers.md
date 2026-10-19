---
title: "transformers — AI agent skill for data science and ml"
description: "Hugging Face Transformers for loading Hub models, running pipeline inference, text generation, and Trainer fine-tuning on NLP, vision, audio, and multimodal…"
keywords: ["Hugging Face Transformers", "LLMs", "NLP", "fine-tuning", "deep learning"]
---

# `transformers`

**Category:** [data-science-and-ml](/skills#data-science-and-ml) · **License:** Apache-2.0 license · **Version:** 1.3

**Tags:** Hugging Face Transformers, LLMs, NLP, fine-tuning, deep learning

## When to use it

Hugging Face Transformers for loading Hub models, running pipeline inference, text generation, and Trainer fine-tuning on NLP, vision, audio, and multimodal tasks. Use when working with AutoModel, pipelines, tokenizers, or TrainingArguments—not for general ML outside the Transformers library.

## Example requests

Ask your agent in plain language, for example:

- *"How do I run sentiment analysis on a list of tweets with a pretrained model from the Hub?"*
- *"I'm fine-tuning bert-base-uncased on my CSV of clinical notes (train.csv, val.csv, columns 'text' and 'label', 5 classes) with Trainer, and I get 'RuntimeError: CUDA out of memory' at the first step with batch size 32 on a 16GB GPU. Here's my TrainingArguments(output_dir='out', per_device_train_batch_size=32, num_train_epochs=3, fp16=True). What should I change?"*
- *"I have about 2,000 recorded interviews as WAV files and I need written transcripts for them, ideally using an open model that runs on my own lab GPU. Can you set that up?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill transformers

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills transformers
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `data-science-and-ml` category with `/plugin install data-science-and-ml@research-agent-skills`.

## Related

- [`huggingface-tokenizers`](/skills/huggingface-tokenizers)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/transformers/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
