---
title: "slime-rl-training — AI agent skill for ml training"
description: "Provides guidance for LLM post-training with RL using slime, a Megatron+SGLang framework."
keywords: ["Reinforcement Learning", "Megatron-LM", "SGLang", "GRPO", "Post-Training", "GLM"]
---

# `slime-rl-training`

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

**Tags:** Reinforcement Learning, Megatron-LM, SGLang, GRPO, Post-Training, GLM

## When to use it

Provides guidance for LLM post-training with RL using slime, a Megatron+SGLang framework. Use when training GLM models, implementing custom data generation workflows, or needing tight Megatron-LM integration for RL scaling.

## Example requests

Ask your agent in plain language, for example:

- *"How do I launch a GRPO run with slime on GLM-4.7?"*
- *"I'm running THUDM/slime in Docker on 2 nodes of 8xH100 to RL-train Qwen3-30B-A3B on my train.jsonl, which has prompt and label fields. Training hangs right after the first rollout finishes, and then I get a weight sync timeout. What should I check?"*
- *"I want to train a search agent with RL. It should call a retrieval tool over several turns, get a reward from the final answer, and run on a Megatron-LM stack with SGLang serving the rollouts. The pipeline should overlap generation and training to avoid idle GPUs. How should I set this up?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill slime-rl-training

# Kalaris Labs installer with checksum verification
npx research-agent-skills install slime-rl-training
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-training` category with `/plugin install ml-training@research-agent-skills`.

## Related

- [`miles-rl-training`](/skills/miles-rl-training)
- [`nnsight-remote-interpretability`](/skills/nnsight-remote-interpretability)
- [`verl-rl-training`](/skills/verl-rl-training)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/slime-rl-training/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
