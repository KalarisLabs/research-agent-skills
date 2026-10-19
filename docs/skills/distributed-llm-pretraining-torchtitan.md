---
title: "distributed-llm-pretraining-torchtitan — AI agent skill for ml training"
description: "Provides PyTorch-native distributed LLM pretraining using torchtitan with 4D parallelism (FSDP2, TP, PP, CP)."
keywords: ["Model Architecture", "Distributed Training", "TorchTitan", "FSDP2", "Tensor Parallel", "Pipeline Parallel", "Context Parallel", "Float8", "Llama", "Pretraining"]
---

# `distributed-llm-pretraining-torchtitan`

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

**Tags:** Model Architecture, Distributed Training, TorchTitan, FSDP2, Tensor Parallel, Pipeline Parallel, Context Parallel, Float8, Llama, Pretraining

## When to use it

Provides PyTorch-native distributed LLM pretraining using torchtitan with 4D parallelism (FSDP2, TP, PP, CP). Use when pretraining Llama 3.1, DeepSeek V3, or custom models at scale from 8 to 512+ GPUs with Float8, torch.compile, and distributed checkpointing.

## Example requests

Ask your agent in plain language, for example:

- *"How do I set up torchtitan to pretrain a Llama 3.1 8B on one 8xH100 box?"*
- *"I'm pretraining a 70B Llama on 32 nodes (256 H100s) with torchtitan under SLURM. My job OOMs in the first few steps with FSDP+TP, using train_configs/llama3_70b.toml. Async TP seems to use a lot of memory. What should I change, and how do I make sure the job resumes cleanly if a node dies?"*
- *"I have a 512-GPU H100 cluster and want to train a 405B dense transformer from scratch using only PyTorch-native tooling, with no Megatron or DeepSpeed. The model needs to combine data, tensor, pipeline and sequence-length sharding, and I want FP8 to speed it up. What's the plan?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill distributed-llm-pretraining-torchtitan

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills distributed-llm-pretraining-torchtitan
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-training` category with `/plugin install ml-training@research-agent-skills`.

## Related

- [`pytorch-fsdp2`](/skills/pytorch-fsdp2)
- [`torchforge-rl-training`](/skills/torchforge-rl-training)
- [`waypoint-bio`](/skills/waypoint-bio)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/distributed-llm-pretraining-torchtitan/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
