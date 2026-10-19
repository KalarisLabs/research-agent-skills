---
title: "pufferlib — AI agent skill for data science and ml"
description: "Version-aware guidance for PufferLib reinforcement-learning environments, vectorization, policies, PuffeRL training, evaluation, and safe checkpoint review."
keywords: ["reinforcement learning", "RL environments", "training", "machine learning"]
---

# `pufferlib`

**Category:** [data-science-and-ml](/skills#data-science-and-ml) · **License:** MIT · **Version:** 1.2 · **Includes scripts**

**Tags:** reinforcement learning, RL environments, training, machine learning

## When to use it

Version-aware guidance for PufferLib reinforcement-learning environments, vectorization, policies, PuffeRL training, evaluation, and safe checkpoint review. Use when adapting Gymnasium/PettingZoo environments to published PufferLib 3.0.0 or working with the redesigned native 4.0 source line.

## Example requests

Ask your agent in plain language, for example:

- *"How do I wrap my PettingZoo parallel env for PufferLib without breaking anything?"*
- *"I ran `pip install pufferlib` and copied the 4.0 README's `puffer train` config into my script, but now `from pufferlib import vector` works while the config keys I copied are rejected. My env is a Gymnasium CartPole variant in my_env.py. What's going on and how do I get it training?"*
- *"A collaborator sent me a trained policy file, model_final.pt, for our multi-agent sim. I want to evaluate it on held-out seeds and log results to Weights & Biases. How should I proceed safely?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill pufferlib

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills pufferlib
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `data-science-and-ml` category with `/plugin install data-science-and-ml@research-agent-skills`.

## Related

- [`evaluating-cosmos-policy`](/skills/evaluating-cosmos-policy)
- [`fine-tuning-serving-openpi`](/skills/fine-tuning-serving-openpi)
- [`stable-baselines3`](/skills/stable-baselines3)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/pufferlib/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
