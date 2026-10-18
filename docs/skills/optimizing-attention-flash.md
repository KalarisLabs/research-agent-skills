---
title: "optimizing-attention-flash — AI agent skill for ml training"
description: "Enables Flash Attention for transformer models using PyTorch native scaled_dot_product_attention (PyTorch 2.2+) or the flash-attn library, including…"
keywords: ["Optimization", "Flash Attention", "Attention Optimization", "Memory Efficiency", "Speed Optimization", "Long Context", "PyTorch", "SDPA", "H100", "FP8", "Transformers"]
---

# `optimizing-attention-flash`

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

**Tags:** Optimization, Flash Attention, Attention Optimization, Memory Efficiency, Speed Optimization, Long Context, PyTorch, SDPA, H100, FP8, Transformers

## When to use it

Enables Flash Attention for transformer models using PyTorch native scaled_dot_product_attention (PyTorch 2.2+) or the flash-attn library, including multi-query attention, sliding window attention, and FP8 on H100 (FlashAttention-3). Covers profiling speedup, checking accuracy against a baseline, and troubleshooting install and GPU support errors. Use when training or running transformers on long sequences (over 512 tokens), when standard attention runs out of GPU memory, when attention is the inference bottleneck, when switching a PyTorch model to the flash backend, or when tuning attention on H100 GPUs. Not for CPU inference, V100 GPUs, or sequences under 256 tokens; consider xFormers for other attention variants.

## Example requests

Ask your agent in plain language, for example:

- *"Can I make my PyTorch training loop use flash attention? Sequences are 4096 tokens."*
- *"I'm fine-tuning Llama-3-8B on an A100 80GB with 16k context using my train.py and keep getting 'CUDA out of memory' inside the attention forward pass. I'm on PyTorch 2.3 and the HF model loads with the default eager attention. How do I fix this without shrinking the context?"*
- *"We have a few H100 nodes and attention is the main bottleneck for our long-document model at inference. I'd like to squeeze out the most throughput using lower precision for the attention math, and also have each token attend only to a local window of neighbors. What should I do?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill optimizing-attention-flash

# Kalaris Labs installer with checksum verification
npx research-agent-skills install optimizing-attention-flash
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-training` category with `/plugin install ml-training@research-agent-skills`.

## Related

- [`mamba-architecture`](/skills/mamba-architecture)
- [`nanogpt`](/skills/nanogpt)
- [`llama-cpp`](/skills/llama-cpp)
- [`rwkv-architecture`](/skills/rwkv-architecture)
- [`tensorrt-llm`](/skills/tensorrt-llm)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/optimizing-attention-flash/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
