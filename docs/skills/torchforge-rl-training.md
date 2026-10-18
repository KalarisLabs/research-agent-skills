---
title: "torchforge-rl-training — AI agent skill for ml training"
description: "Provides guidance for PyTorch-native agentic RL using torchforge, Meta's library separating infra from algorithms."
keywords: ["Reinforcement Learning", "PyTorch", "GRPO", "SFT", "Monarch", "TorchTitan", "Meta"]
---

# `torchforge-rl-training`

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

**Tags:** Reinforcement Learning, PyTorch, GRPO, SFT, Monarch, TorchTitan, Meta

## When to use it

Provides guidance for PyTorch-native agentic RL using torchforge, Meta's library separating infra from algorithms. Use when you want clean RL abstractions, easy algorithm experimentation, or scalable training with Monarch and TorchTitan.

## Example requests

Ask your agent in plain language, for example:

- *"How do I write a custom RL loss in torchforge?"*
- *"I'm trying to run GRPO on Qwen3-1.7B with GSM8K using torchforge on a box with only 2 A100s and I get 'Insufficient GPU resources'. Config is in apps/grpo/gsm8k.yaml. What do I change?"*
- *"I want to experiment with a new policy-gradient variant for math reasoning, with group-relative advantages. I want the algorithm code kept separate from the distributed and inference plumbing, PyTorch-native with no Ray. What stack should I use and how do I get started?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill torchforge-rl-training

# Kalaris Labs installer with checksum verification
npx research-agent-skills install torchforge-rl-training
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-training` category with `/plugin install ml-training@research-agent-skills`.

## Related

- [`distributed-llm-pretraining-torchtitan`](/skills/distributed-llm-pretraining-torchtitan)
- [`pytorch-lightning-distributed`](/skills/pytorch-lightning-distributed)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/torchforge-rl-training/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
