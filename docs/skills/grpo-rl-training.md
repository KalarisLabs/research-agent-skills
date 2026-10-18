---
title: "grpo-rl-training — AI agent skill for ml training"
description: "Guides GRPO (Group Relative Policy Optimization) fine-tuning of language models with the TRL library, including GRPOTrainer configuration, composing multiple…"
keywords: ["Post-Training", "Reinforcement Learning", "GRPO", "TRL", "RLHF", "Reward Modeling", "Reasoning", "DPO", "PPO", "Structured Output"]
---

# `grpo-rl-training`

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

**Tags:** Post-Training, Reinforcement Learning, GRPO, TRL, RLHF, Reward Modeling, Reasoning, DPO, PPO, Structured Output

## When to use it

Guides GRPO (Group Relative Policy Optimization) fine-tuning of language models with the TRL library, including GRPOTrainer configuration, composing multiple reward functions (correctness, format, length, style), dataset prep in chat format, Unsloth setup, LoRA merging, and monitoring reward, reward_std and KL. Use when training a model to follow a strict output format such as XML or JSON. Use when teaching verifiable tasks like math or code with objective correctness rewards. Use when improving chain-of-thought reasoning with custom reward functions. Use when debugging flat rewards, mode collapse, or OOM in GRPO runs. Do not use for plain supervised fine-tuning (use SFT) or when high-quality preference pairs exist (use DPO or PPO).

## Example requests

Ask your agent in plain language, for example:

- *"How do I set up GRPO in TRL so my model always answers in &lt;reasoning>...&lt;/reasoning>&lt;answer>...&lt;/answer> tags?"*
- *"I'm running GRPOTrainer on Qwen2.5-1.5B-Instruct with GSM8K (train.jsonl has 'question' and 'answer' columns) on a single 24GB card. With num_generations=8 and max_completion_length=512 I get CUDA out of memory during generation. Also the reward curve in wandb has been flat at ~0.1 for 300 steps and reward_std is near zero. What should I change?"*
- *"I have a base LLM and a few thousand arithmetic and logic word problems with known final answers, but no human preference labels and no reward model. I want the model to learn to reason step by step and get the right answer. What training approach should I use and how would I wire it up?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill grpo-rl-training

# Kalaris Labs installer with checksum verification
npx research-agent-skills install grpo-rl-training
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-training` category with `/plugin install ml-training@research-agent-skills`.

## Related

- [`fine-tuning-with-trl`](/skills/fine-tuning-with-trl)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/grpo-rl-training/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
