---
title: "serving-llms-vllm — AI agent skill for ml inference and ops"
description: "Serves LLMs with high throughput using vLLM's PagedAttention and continuous batching."
keywords: ["vLLM", "Inference Serving", "PagedAttention", "Continuous Batching", "High Throughput", "Production", "OpenAI API", "Quantization", "Tensor Parallelism"]
---

# `serving-llms-vllm`

**Category:** [ml-inference-and-ops](/skills#ml-inference-and-ops) · **License:** MIT · **Version:** 1.0.0

**Tags:** vLLM, Inference Serving, PagedAttention, Continuous Batching, High Throughput, Production, OpenAI API, Quantization, Tensor Parallelism

## When to use it

Serves LLMs with high throughput using vLLM's PagedAttention and continuous batching. Use when deploying production LLM APIs, optimizing inference latency/throughput, or serving models with limited GPU memory. Supports OpenAI-compatible endpoints, quantization (GPTQ/AWQ/FP8), and tensor parallelism.

## Example requests

Ask your agent in plain language, for example:

- *"How do I serve Llama-3-8B with vLLM behind an OpenAI-style API?"*
- *"I'm trying to load Qwen2.5-72B-Instruct-AWQ on 2x A100 80GB for our lab's chat tool and vLLM crashes with 'CUDA out of memory' during model loading. Command: vllm serve Qwen/Qwen2.5-72B-Instruct-AWQ --tensor-parallel-size 2. What should I change?"*
- *"I have 200,000 abstracts in abstracts.jsonl and need to run an open-weights model over all of them to extract structured summaries on one shared GPU server. What's the fastest way to do this without writing a request loop against an API?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill serving-llms-vllm

# Kalaris Labs installer with checksum verification
npx research-agent-skills install serving-llms-vllm
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-inference-and-ops` category with `/plugin install ml-inference-and-ops@research-agent-skills`.

## Related

- [`awq-quantization`](/skills/awq-quantization)
- [`llamaguard`](/skills/llamaguard)
- [`miles-rl-training`](/skills/miles-rl-training)
- [`ml-training-recipes`](/skills/ml-training-recipes)
- [`modal`](/skills/modal)
- [`tensorrt-llm`](/skills/tensorrt-llm)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/serving-llms-vllm/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
