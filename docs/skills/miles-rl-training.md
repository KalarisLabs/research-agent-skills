---
title: "miles-rl-training — AI agent skill for ml training"
description: "Provides guidance for enterprise-grade RL training using miles, a production-ready fork of slime."
keywords: ["Reinforcement Learning", "MoE", "FP8", "INT4", "Enterprise", "SGLang", "Megatron-LM"]
---

# `miles-rl-training`

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

**Tags:** Reinforcement Learning, MoE, FP8, INT4, Enterprise, SGLang, Megatron-LM

## When to use it

Provides guidance for enterprise-grade RL training using miles, a production-ready fork of slime. Use when training large MoE models with FP8/INT4, needing train-inference alignment, or requiring speculative RL for maximum throughput.

## Example requests

Ask your agent in plain language, for example:

- *"How do I turn on FP8 rollout and training for a Qwen3-MoE run so RL doesn't collapse?"*
- *"I'm running GRPO on DeepSeek-V3 with miles on 4 nodes of H200. After about 200 steps the reward drops sharply and the logprobs from SGLang don't match Megatron's. Is this a train-inference mismatch, and how do I fix it? My args currently include --use-tis --tis-threshold 0.9 but I don't use any routing replay."*
- *"My RL rollouts are the bottleneck when post-training a big MoE model. Generation takes far longer than the gradient update. I'd like to speed up sampling by having a small helper model propose tokens that the main model checks, and the helper should stay in sync with the policy as it changes. What setup do I need?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill miles-rl-training

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills miles-rl-training
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-training` category with `/plugin install ml-training@research-agent-skills`.

## Related

- [`serving-llms-vllm`](/skills/serving-llms-vllm)
- [`slime-rl-training`](/skills/slime-rl-training)
- [`tensorrt-llm`](/skills/tensorrt-llm)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/miles-rl-training/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
