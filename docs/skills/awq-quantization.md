---
title: "awq-quantization — AI agent skill for ml training"
description: "Activation-aware weight quantization for 4-bit LLM compression with 3x speedup and minimal accuracy loss."
keywords: ["Optimization", "AWQ", "Quantization", "4-Bit", "Activation-Aware", "Memory Optimization", "Fast Inference", "vLLM Integration", "Marlin Kernels"]
---

# `awq-quantization`

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

**Tags:** Optimization, AWQ, Quantization, 4-Bit, Activation-Aware, Memory Optimization, Fast Inference, vLLM Integration, Marlin Kernels

## When to use it

Activation-aware weight quantization for 4-bit LLM compression with 3x speedup and minimal accuracy loss. Use when deploying large models (7B-70B) on limited GPU memory, when you need faster inference than GPTQ with better accuracy preservation, or for instruction-tuned and multimodal models. MLSys 2024 Best Paper Award winner.

## Example requests

Ask your agent in plain language, for example:

- *"How do I load a 4-bit AWQ Llama 3 8B in transformers?"*
- *"I have a fine-tuned Mistral-7B-Instruct in ./checkpoints/mistral-ft that I want to quantize to 4-bit with activation-aware quantization for vLLM serving on an A100. I'm getting 'CUDA out of memory' during the calibration step on a 24GB card. How should I do this and fix the OOM?"*
- *"I need to fit a 70B chat model onto two 40GB GPUs for inference, with about 3% perplexity increase at most and as fast as possible decoding. Which compression approach should I use and how do I set it up?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill awq-quantization

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills awq-quantization
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-training` category with `/plugin install ml-training@research-agent-skills`.

## Related

- [`quantizing-models-bitsandbytes`](/skills/quantizing-models-bitsandbytes)
- [`serving-llms-vllm`](/skills/serving-llms-vllm)
- [`gguf-quantization`](/skills/gguf-quantization)
- [`gptq`](/skills/gptq)
- [`model-pruning`](/skills/model-pruning)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/awq-quantization/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
