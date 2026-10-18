---
title: "moe-training — AI agent skill for multimodal and emerging"
description: "Train Mixture of Experts (MoE) models using DeepSpeed or HuggingFace."
keywords: ["Emerging Techniques", "MoE", "Mixture Of Experts", "Sparse Models", "DeepSpeed", "Expert Parallelism", "Mixtral", "DeepSeek", "Routing", "Load Balancing", "Efficient Training"]
---

# `moe-training`

**Category:** [multimodal-and-emerging](/skills#multimodal-and-emerging) · **License:** MIT · **Version:** 1.0.0

**Tags:** Emerging Techniques, MoE, Mixture Of Experts, Sparse Models, DeepSpeed, Expert Parallelism, Mixtral, DeepSeek, Routing, Load Balancing, Efficient Training

## When to use it

Train Mixture of Experts (MoE) models using DeepSpeed or HuggingFace. Use when training large-scale models with limited compute (5× cost reduction vs dense models), implementing sparse architectures like Mixtral 8x7B or DeepSeek-V3, or scaling model capacity without proportional compute increase. Covers MoE architectures, routing mechanisms, load balancing, expert parallelism, and inference optimization.

## Example requests

Ask your agent in plain language, for example:

- *"How do I fine-tune Mixtral 8x7B on a single 8-GPU node without running out of memory?"*
- *"I'm pretraining a 1.3B-base MoE with 16 experts using train_moe.py and DeepSpeed. After about 2k steps the loss spikes and the router logs show 3 experts getting nearly all the tokens (the others are under 1%). My ds_config has aux loss coef 0.01 and capacity_factor 1.0. What should I change?"*
- *"My lab has a small budget and I want a language model with much more parameter capacity than a dense 7B, but without paying proportionally more per training token. What architecture should I use, and how do I set it up and train it?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill moe-training

# Kalaris Labs installer with checksum verification
npx research-agent-skills install moe-training
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `multimodal-and-emerging` category with `/plugin install multimodal-and-emerging@research-agent-skills`.

## Related

- [`training-llms-megatron`](/skills/training-llms-megatron)
- [Skills for AI research](/fields/artificial-intelligence)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/moe-training/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
