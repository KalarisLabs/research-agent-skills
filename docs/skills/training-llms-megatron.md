---
title: "training-llms-megatron — AI agent skill for ml training"
description: "Trains large language models (2B-462B parameters) with NVIDIA Megatron-Core using tensor, pipeline, sequence, context, and expert parallelism, plus FP8 on…"
keywords: ["Megatron-Core", "Large-Scale Training", "NVIDIA", "Tensor Parallelism", "Pipeline Parallelism", "Model Parallelism", "H100", "Distributed Training", "Production"]
---

# `training-llms-megatron`

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

**Tags:** Megatron-Core, Large-Scale Training, NVIDIA, Tensor Parallelism, Pipeline Parallelism, Model Parallelism, H100, Distributed Training, Production

## When to use it

Trains large language models (2B-462B parameters) with NVIDIA Megatron-Core using tensor, pipeline, sequence, context, and expert parallelism, plus FP8 on H100 and MoE configuration for Mixtral-style models. Covers choosing TP/PP/DP/CP sizes, launching distributed training, tuning micro-batch size, and fixing low MFU, out-of-memory errors, and diverging loss. Use when training models above 10B parameters on NVIDIA A100/H100 GPUs, when setting up 3D parallelism for a LLaMA-style model, when configuring expert parallelism for MoE training, or when trying to raise MFU toward 40-47%. Use PyTorch FSDP, DeepSpeed, or HuggingFace Accelerate instead for models under 70B or simpler setups.

## Example requests

Ask your agent in plain language, for example:

- *"How should I split TP/PP/DP for a 70B LLaMA on 64 H100s with Megatron?"*
- *"I'm pretraining a 13B GPT on 2 nodes of 8xA100-80GB with Megatron-LM, using pretrain_gpt.py and torchrun. At micro-batch 4 with TP=2, PP=1, I get 'CUDA out of memory' in the first forward pass. MFU was around 28% on a smaller test. What should I change, and in what order?"*
- *"We want to train a Mixtral-style 8x7B sparse model from scratch on a 64-GPU H100 cluster and keep the experts spread across devices so it fits. Our loss also spikes after a few thousand steps. How do we set it up?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill training-llms-megatron

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills training-llms-megatron
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-training` category with `/plugin install ml-training@research-agent-skills`.

## Related

- [`deepspeed`](/skills/deepspeed)
- [`moe-training`](/skills/moe-training)
- [`tensorrt-llm`](/skills/tensorrt-llm)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/training-llms-megatron/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
