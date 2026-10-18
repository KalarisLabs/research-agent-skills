---
title: "stable-baselines3 — AI agent skill for data science and ml"
description: "Production-ready reinforcement learning algorithms (PPO, SAC, DQN, TD3, DDPG, A2C) with scikit-learn-like API."
keywords: ["reinforcement learning", "PPO", "SAC", "DQN", "Gymnasium"]
---

# `stable-baselines3`

**Category:** [data-science-and-ml](/skills#data-science-and-ml) · **License:** MIT · **Version:** 1.3 · **Includes scripts**

**Tags:** reinforcement learning, PPO, SAC, DQN, Gymnasium

## When to use it

Production-ready reinforcement learning algorithms (PPO, SAC, DQN, TD3, DDPG, A2C) with scikit-learn-like API. Use for standard RL experiments, quick prototyping, and well-documented algorithm implementations. Best for single-agent RL with Gymnasium environments. For high-performance parallel training, multi-agent systems, or custom vectorized environments, use pufferlib instead.

## Example requests

Ask your agent in plain language, for example:

- *"Train a PPO agent on CartPole and show me how to save and evaluate it."*
- *"I wrote a custom Gymnasium env in warehouse_env.py with a Box observation space of shape (84,84,3) uint8 images, and SAC throws 'You have passed a tuple to the constructor' / complains about the observation space when I call model = SAC('CnnPolicy', env). Also SAC doesn't make sense for discrete actions, I think my action space is Discrete(4) with start=1. What's going on and how do I fix it?"*
- *"I have a simulated robot arm with continuous joint torques and a reward function I've defined. I want a sample-efficient learner I can get running quickly with checkpoints, periodic evaluation that keeps the best model, and TensorBoard curves. Where do I start?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill stable-baselines3

# Kalaris Labs installer with checksum verification
npx research-agent-skills install stable-baselines3
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `data-science-and-ml` category with `/plugin install data-science-and-ml@research-agent-skills`.

## Related

- [`pufferlib`](/skills/pufferlib)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/stable-baselines3/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
