---
title: "ml-training-recipes — AI agent skill for ml training"
description: "Battle-tested PyTorch training recipes for all domains — LLMs, vision, diffusion, medical imaging, protein/drug discovery, spatial omics, genomics."
keywords: ["PyTorch", "Training", "Optimization", "LLM", "Vision", "Diffusion", "Biomedical", "Muon", "AdamW", "Debugging"]
---

# `ml-training-recipes`

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

**Tags:** PyTorch, Training, Optimization, LLM, Vision, Diffusion, Biomedical, Muon, AdamW, Debugging

## When to use it

Battle-tested PyTorch training recipes for all domains — LLMs, vision, diffusion, medical imaging, protein/drug discovery, spatial omics, genomics. Covers training loops, optimizer selection (AdamW, Muon), LR scheduling, mixed precision, debugging, and systematic experimentation. Use when training or fine-tuning neural networks, debugging loss spikes or OOM, choosing architectures, or optimizing GPU throughput.

## Example requests

Ask your agent in plain language, for example:

- *"My loss keeps spiking around step 4k when training a 350M GPT. What should I check?"*
- *"I'm fine-tuning ESM-2 650M on ~40k labeled protein sequences with train.py on a single A100 40GB. I'm hitting 'CUDA out of memory' in the backward pass at batch size 32 with fp32. How do I fit this and keep throughput decent?"*
- *"I have a fixed 8 GPU-hour budget on one GPU and want to pretrain the best small language model I can. How do I decide model size, how many tokens to feed it, and what optimizer and LR schedule to use?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill ml-training-recipes

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills ml-training-recipes
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-training` category with `/plugin install ml-training@research-agent-skills`.

## Related

- [`llama-factory`](/skills/llama-factory)
- [`peft-fine-tuning`](/skills/peft-fine-tuning)
- [`serving-llms-vllm`](/skills/serving-llms-vllm)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/ml-training-recipes/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
