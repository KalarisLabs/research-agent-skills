---
title: "nanogpt — AI agent skill for ml training"
description: "Provides nanoGPT, Karpathy's minimal PyTorch GPT implementation (model.py and train.py), with workflows for training character-level Shakespeare on CPU…"
keywords: ["Model Architecture", "NanoGPT", "GPT-2", "Educational", "Andrej Karpathy", "Transformer", "Minimalist", "From Scratch", "Training"]
---

# `nanogpt`

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

**Tags:** Model Architecture, NanoGPT, GPT-2, Educational, Andrej Karpathy, Transformer, Minimalist, From Scratch, Training

## When to use it

Provides nanoGPT, Karpathy's minimal PyTorch GPT implementation (model.py and train.py), with workflows for training character-level Shakespeare on CPU, reproducing GPT-2 124M on OpenWebText with multi-GPU torchrun, fine-tuning pretrained GPT-2 checkpoints, and training on custom text. Use when learning how GPT and transformer blocks work from scratch. Use when running a small training experiment on CPU or a single GPU. Use when modifying a transformer variant in plain PyTorch. Use when preparing character-level or BPE binary datasets. Use when troubleshooting out-of-memory or slow training in nanoGPT. Not for production or large-scale distributed training; use HuggingFace Transformers or Megatron-LM instead.

## Example requests

Ask your agent in plain language, for example:

- *"I want to train a tiny GPT on my laptop with no GPU just to see it work. What's the quickest way to get something generating Shakespeare-like text?"*
- *"I'm running nanoGPT train.py on a single 16GB GPU with config/train_gpt2.py and get 'torch.cuda.OutOfMemoryError: CUDA out of memory'. How do I get it to fit without changing the model size?"*
- *"I have a 40MB text file of my lab's protocol notes and want to adapt a pretrained GPT-2 small to it so it writes in that style, plus read through the code so I understand how the attention blocks work. I want something minimal in plain PyTorch, not a big framework."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill nanogpt

# Kalaris Labs installer with checksum verification
npx research-agent-skills install nanogpt
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-training` category with `/plugin install ml-training@research-agent-skills`.

## Related

- [`huggingface-accelerate`](/skills/huggingface-accelerate)
- [`optimizing-attention-flash`](/skills/optimizing-attention-flash)
- [`ray-data`](/skills/ray-data)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/nanogpt/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
