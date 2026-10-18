---
title: "verl-rl-training — AI agent skill for ml training"
description: "Provides guidance for training LLMs with reinforcement learning using verl (Volcano Engine RL)."
keywords: ["Reinforcement Learning", "RLHF", "GRPO", "PPO", "Post-Training", "Distributed Training"]
---

# `verl-rl-training`

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

**Tags:** Reinforcement Learning, RLHF, GRPO, PPO, Post-Training, Distributed Training

## When to use it

Provides guidance for training LLMs with reinforcement learning using verl (Volcano Engine RL). Use when implementing RLHF, GRPO, PPO, or other RL algorithms for LLM post-training at scale with flexible infrastructure backends.

## Example requests

Ask your agent in plain language, for example:

- *"How do I set up GRPO training on GSM8K with verl?"*
- *"I'm running verl on 2 nodes of 8xH100 to RL-train Qwen3-32B on my math dataset at /data/math_train.parquet. During the rollout phase I get 'CUDA out of memory' from vLLM, and the pauses between rollout and training are very long. Config is FSDP2 with vLLM rollout and gpu_memory_utilization=0.9. What should I change?"*
- *"I want to post-train an open LLM to solve competition math using only a programmatic right/wrong answer checker, with no value model, on a multi-node GPU cluster where I can swap the inference engine and the training backend (FSDP vs Megatron) without rewriting my code. What framework and setup would you recommend?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill verl-rl-training

# Kalaris Labs installer with checksum verification
npx research-agent-skills install verl-rl-training
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-training` category with `/plugin install ml-training@research-agent-skills`.

## Related

- [`fine-tuning-with-trl`](/skills/fine-tuning-with-trl)
- [`openrlhf-training`](/skills/openrlhf-training)
- [`slime-rl-training`](/skills/slime-rl-training)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/verl-rl-training/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
