---
title: "rwkv-architecture — AI agent skill for ml training"
description: "Covers the RWKV (Receptance Weighted Key Value) architecture, an RNN/Transformer hybrid with O(n) inference and no KV cache, including RWKV-7, its parallel…"
keywords: ["RWKV", "Model Architecture", "RNN", "Transformer Hybrid", "Linear Complexity", "Infinite Context", "Efficient Inference", "Linux Foundation", "Alternative Architecture"]
---

# `rwkv-architecture`

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

**Tags:** RWKV, Model Architecture, RNN, Transformer Hybrid, Linear Complexity, Infinite Context, Efficient Inference, Linux Foundation, Alternative Architecture

## When to use it

Covers the RWKV (Receptance Weighted Key Value) architecture, an RNN/Transformer hybrid with O(n) inference and no KV cache, including RWKV-7, its parallel GPT-mode training and sequential RNN-mode inference, state passing, fine-tuning with DeepSpeed, and CUDA kernel setup. Use when generating text token by token with constant memory, processing very long contexts of 100K+ tokens, fine-tuning an RWKV model, comparing RWKV memory and speed against Transformers, or debugging RWKV state handling, loading, or out-of-memory errors. Prefer a standard Transformer when peak accuracy matters more than memory, and Mamba for state-space models.

## Example requests

Ask your agent in plain language, for example:

- *"How do I run an RWKV model one token at a time without the memory growing?"*
- *"I'm fine-tuning RWKV-7 on my own corpus (train.jsonl, about 2B tokens) on a single 24GB GPU using DeepSpeed, and I get 'CUDA out of memory' a few steps in. I'm using the RWKV-LM repo. What should I change?"*
- *"I need to run a language model over entire books and log files, a few hundred thousand tokens each, on a laptop GPU with 8GB of VRAM. Standard attention models blow up in memory. What are my options, and can you set up something that streams through the text in chunks?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill rwkv-architecture

# Kalaris Labs installer with checksum verification
npx research-agent-skills install rwkv-architecture
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-training` category with `/plugin install ml-training@research-agent-skills`.

## Related

- [`mamba-architecture`](/skills/mamba-architecture)
- [`optimizing-attention-flash`](/skills/optimizing-attention-flash)
- [`speculative-decoding`](/skills/speculative-decoding)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/rwkv-architecture/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
