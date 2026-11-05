---
title: "model-pruning — AI agent skill for multimodal and emerging"
description: "Reduce LLM size and accelerate inference using pruning techniques like Wanda and SparseGPT."
keywords: ["Emerging Techniques", "Model Pruning", "Wanda", "SparseGPT", "Sparsity", "Model Compression", "N:M Sparsity", "One-Shot Pruning", "Structured Pruning", "Unstructured Pruning", "Fast Inference"]
---

# `model-pruning`

**Category:** [multimodal-and-emerging](/skills#multimodal-and-emerging) · **License:** MIT · **Version:** 1.0.0

**Tags:** Emerging Techniques, Model Pruning, Wanda, SparseGPT, Sparsity, Model Compression, N:M Sparsity, One-Shot Pruning, Structured Pruning, Unstructured Pruning, Fast Inference

## When to use it

Reduce LLM size and accelerate inference using pruning techniques like Wanda and SparseGPT. Use when compressing models without retraining, achieving 50% sparsity with minimal accuracy loss, or enabling faster inference on hardware accelerators. Covers unstructured pruning, structured pruning, N:M sparsity, magnitude pruning, and one-shot methods.

## Example requests

Ask your agent in plain language, for example:

- *"How do I prune Llama-2-7B to 50% sparsity without retraining?"*
- *"I have llama-2-7b-hf checkpoint at ./models/llama2-7b and an A100 40GB. I want to run Wanda with 2:4 sparsity using 128 C4 calibration samples, then compare WikiText2 perplexity against the dense model. Running main.py gives a CUDA OOM error while computing activation norms. What should I do?"*
- *"My 13B model is too big for the edge devices we're targeting, and I can't afford to retrain it. I want to remove a large share of the weights and still have it run faster on Ampere GPUs. What are my options and tradeoffs?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill model-pruning

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills model-pruning
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `multimodal-and-emerging` category with `/plugin install multimodal-and-emerging@research-agent-skills`.

## Related

- [`awq-quantization`](/skills/awq-quantization)
- [`quantizing-models-bitsandbytes`](/skills/quantizing-models-bitsandbytes)
- [`speculative-decoding`](/skills/speculative-decoding)
- [Skills for AI research](/fields/artificial-intelligence)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/model-pruning/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
