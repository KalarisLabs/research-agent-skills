---
title: "tensorrt-llm — AI agent skill for ml inference and ops"
description: "Optimizes LLM inference with NVIDIA TensorRT for maximum throughput and lowest latency."
keywords: ["Inference Serving", "TensorRT-LLM", "NVIDIA", "Inference Optimization", "High Throughput", "Low Latency", "Production", "FP8", "INT4", "In-Flight Batching", "Multi-GPU"]
---

# `tensorrt-llm`

**Category:** [ml-inference-and-ops](/skills#ml-inference-and-ops) · **License:** MIT · **Version:** 1.0.0

**Tags:** Inference Serving, TensorRT-LLM, NVIDIA, Inference Optimization, High Throughput, Low Latency, Production, FP8, INT4, In-Flight Batching, Multi-GPU

## When to use it

Optimizes LLM inference with NVIDIA TensorRT for maximum throughput and lowest latency. Use for production deployment on NVIDIA GPUs (A100/H100), when you need 10-100x faster inference than PyTorch, or for serving models with quantization (FP8/INT4), in-flight batching, and multi-GPU scaling.

## Example requests

Ask your agent in plain language, for example:

- *"How do I serve Llama 3 70B with TensorRT-LLM on 8 H100s?"*
- *"I'm trying to deploy meta-llama/Meta-Llama-3-8B-Instruct on a single H100 for our lab's chat tool, and p95 latency is too high with plain HF transformers generate(). I built an engine with trtllm-build but the server throws a CUDA out of memory error when I send 64 concurrent requests. Can you help me fix it and get the quantization settings right?"*
- *"We have a cluster of A100 80GB nodes and need to serve a 70B model to our research group with the lowest possible time per token and the highest tokens per second, using NVIDIA's compiled-engine approach with FP8 weights. What should the setup look like, and how do we check that the quantized model is still accurate?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill tensorrt-llm

# Kalaris Labs installer with checksum verification
npx research-agent-skills install tensorrt-llm
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-inference-and-ops` category with `/plugin install ml-inference-and-ops@research-agent-skills`.

## Related

- [`llama-cpp`](/skills/llama-cpp)
- [`miles-rl-training`](/skills/miles-rl-training)
- [`modal`](/skills/modal)
- [`optimizing-attention-flash`](/skills/optimizing-attention-flash)
- [`serving-llms-vllm`](/skills/serving-llms-vllm)
- [`sglang`](/skills/sglang)
- [`training-llms-megatron`](/skills/training-llms-megatron)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/tensorrt-llm/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
