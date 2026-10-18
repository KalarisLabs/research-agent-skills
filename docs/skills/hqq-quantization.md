---
title: "hqq-quantization — AI agent skill for ml training"
description: "Half-Quadratic Quantization for LLMs without calibration data."
keywords: ["Quantization", "HQQ", "Optimization", "Memory Efficiency", "Inference", "Model Compression"]
---

# `hqq-quantization`

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

**Tags:** Quantization, HQQ, Optimization, Memory Efficiency, Inference, Model Compression

## When to use it

Half-Quadratic Quantization for LLMs without calibration data. Use when quantizing models to 4/3/2-bit precision without needing calibration datasets, for fast quantization workflows, or when deploying with vLLM or HuggingFace Transformers.

## Example requests

Ask your agent in plain language, for example:

- *"How do I quantize Llama-3-8B to 4-bit when I don't have any calibration data?"*
- *"I'm on an A100 and need to quantize mistralai/Mistral-7B-Instruct-v0.3 for a benchmark. I'm working in quantize.py with transformers 4.44 and hqq 0.2.x. I want attention layers at 4-bit and the MLP layers at 2-bit, then I want to save it and reload it for generation. I also need the fastest 4-bit backend. How should I configure this?"*
- *"I want to compress a 70B model enough to fit on a single GPU, but I have no representative dataset and I can't spend hours on a long quantization run. I'd also like to fine-tune it with LoRA afterwards. What approach would work?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill hqq-quantization

# Kalaris Labs installer with checksum verification
npx research-agent-skills install hqq-quantization
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-training` category with `/plugin install ml-training@research-agent-skills`.

## Related

- [`evaluating-llms-harness`](/skills/evaluating-llms-harness)
- [`gguf-quantization`](/skills/gguf-quantization)
- [`gptq`](/skills/gptq)
- [`quantizing-models-bitsandbytes`](/skills/quantizing-models-bitsandbytes)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/hqq-quantization/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
