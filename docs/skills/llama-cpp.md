---
title: "llama-cpp — AI agent skill for ml inference and ops"
description: "Runs LLM inference on CPU, Apple Silicon, and consumer GPUs without NVIDIA hardware."
keywords: ["Inference Serving", "Llama.cpp", "CPU Inference", "Apple Silicon", "Edge Deployment", "GGUF", "Quantization", "Non-NVIDIA", "AMD GPUs", "Intel GPUs", "Embedded"]
---

# `llama-cpp`

**Category:** [ml-inference-and-ops](/skills#ml-inference-and-ops) · **License:** MIT · **Version:** 1.0.0

**Tags:** Inference Serving, Llama.cpp, CPU Inference, Apple Silicon, Edge Deployment, GGUF, Quantization, Non-NVIDIA, AMD GPUs, Intel GPUs, Embedded

## When to use it

Runs LLM inference on CPU, Apple Silicon, and consumer GPUs without NVIDIA hardware. Use for edge deployment, M1/M2/M3 Macs, AMD/Intel GPUs, or when CUDA is unavailable. Supports GGUF quantization (1.5-8 bit) for reduced memory and 4-10× speedup vs PyTorch on CPU.

## Example requests

Ask your agent in plain language, for example:

- *"How do I run a 7B chat model on my M2 MacBook Air without a GPU server?"*
- *"I'm on a Ryzen 9 7950X workstation with 64 GB RAM and no GPU. I downloaded Meta-Llama-3-8B-Instruct.Q5_K_M.gguf from Hugging Face and want to serve it locally for a team script. When I start the server with a 32k context it gets very slow and then the process is killed. What should I check and how do I fix it?"*
- *"Our lab has a few old Raspberry Pi 5 boards and an Intel Arc laptop but no NVIDIA cards. We want a small language model to summarize field notes offline. What's a realistic way to set that up, and what speed should we expect?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill llama-cpp

# Kalaris Labs installer with checksum verification
npx research-agent-skills install llama-cpp
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-inference-and-ops` category with `/plugin install ml-inference-and-ops@research-agent-skills`.

## Related

- [`gguf-quantization`](/skills/gguf-quantization)
- [`tensorrt-llm`](/skills/tensorrt-llm)
- [`optimizing-attention-flash`](/skills/optimizing-attention-flash)
- [`sglang`](/skills/sglang)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/llama-cpp/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
