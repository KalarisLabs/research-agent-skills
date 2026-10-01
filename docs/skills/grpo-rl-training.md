---
title: "grpo-rl-training — AI agent skill for ml training"
description: "Guides GRPO (Group Relative Policy Optimization) fine-tuning of language models with the TRL library, including GRPOTrainer configuration, composing multi…"
---

# `grpo-rl-training`

> Guides GRPO (Group Relative Policy Optimization) fine-tuning of language models with the TRL library, including GRPOTrainer configuration, composing multiple reward functions (correctness, format, length, style), dataset prep in chat format, Unsloth setup, LoRA merging, and monitoring reward, reward_std and KL. Use when training a model to follow a strict output format such as XML or JSON. Use when teaching verifiable tasks like math or code with objective correctness rewards. Use when improving chain-of-thought reasoning with custom reward functions. Use when debugging flat rewards, mode collapse, or OOM in GRPO runs. Do not use for plain supervised fine-tuning (use SFT) or when high-quality preference pairs exist (use DPO or PPO).

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

## Install

```bash
npx research-agent-skills install grpo-rl-training
npx skills add KalarisLabs/research-agent-skills --skill grpo-rl-training
```

## When to use it

Guides GRPO (Group Relative Policy Optimization) fine-tuning of language models with the TRL library, including GRPOTrainer configuration, composing multiple reward functions (correctness, format, length, style), dataset prep in chat format, Unsloth setup, LoRA merging, and monitoring reward, reward_std and KL. Use when training a model to follow a strict output format such as XML or JSON. Use when teaching verifiable tasks like math or code with objective correctness rewards. Use when improving chain-of-thought reasoning with custom reward functions. Use when debugging flat rewards, mode collapse, or OOM in GRPO runs. Do not use for plain supervised fine-tuning (use SFT) or when high-quality preference pairs exist (use DPO or PPO).

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/grpo-rl-training/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
