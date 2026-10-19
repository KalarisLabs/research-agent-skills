---
title: "gguf-quantization — AI agent skill for ml training"
description: "GGUF format and llama.cpp quantization for efficient CPU/GPU inference."
keywords: ["GGUF", "Quantization", "llama.cpp", "CPU Inference", "Apple Silicon", "Model Compression", "Optimization"]
---

# `gguf-quantization`

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

**Tags:** GGUF, Quantization, llama.cpp, CPU Inference, Apple Silicon, Model Compression, Optimization

## When to use it

GGUF format and llama.cpp quantization for efficient CPU/GPU inference. Use when deploying models on consumer hardware, Apple Silicon, or when needing flexible quantization from 2-8 bit without GPU requirements.

## Example requests

Ask your agent in plain language, for example:

- *"How do I turn a HF model into a Q4_K_M GGUF file?"*
- *"I have a fine-tuned Mistral-7B in ./checkpoints/mistral-ft (safetensors) and I want to run it on my M2 MacBook Air with 16GB RAM. I ran llama-quantize with Q2_K and the outputs are garbage now. What should I do?"*
- *"I want to run a language model locally on my old laptop that has no graphics card, using as little RAM as possible without the output becoming useless. I also want to expose it to my scripts through an OpenAI-style API. What's the best way to set this up?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill gguf-quantization

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills gguf-quantization
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-training` category with `/plugin install ml-training@research-agent-skills`.

## Related

- [`awq-quantization`](/skills/awq-quantization)
- [`hqq-quantization`](/skills/hqq-quantization)
- [`llama-cpp`](/skills/llama-cpp)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/gguf-quantization/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
