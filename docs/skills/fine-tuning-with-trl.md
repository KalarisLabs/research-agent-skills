---
title: "fine-tuning-with-trl — AI agent skill for ml training"
description: "Fine-tune LLMs using reinforcement learning with TRL - SFT for instruction tuning, DPO for preference alignment, PPO/GRPO for reward optimization, and reward…"
keywords: ["Post-Training", "TRL", "Reinforcement Learning", "Fine-Tuning", "SFT", "DPO", "PPO", "GRPO", "RLHF", "Preference Alignment", "HuggingFace"]
---

# `fine-tuning-with-trl`

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

**Tags:** Post-Training, TRL, Reinforcement Learning, Fine-Tuning, SFT, DPO, PPO, GRPO, RLHF, Preference Alignment, HuggingFace

## When to use it

Fine-tune LLMs using reinforcement learning with TRL - SFT for instruction tuning, DPO for preference alignment, PPO/GRPO for reward optimization, and reward model training. Use when need RLHF, align model with preferences, or train from human feedback. Works with HuggingFace Transformers.

## Example requests

Ask your agent in plain language, for example:

- *"How do I run DPO on my preference pairs with TRL?"*
- *"I'm fine-tuning Qwen2.5-7B on an A100 40GB with my file pairs.jsonl (fields: question, good_answer, bad_answer). DPOTrainer crashes with 'CUDA out of memory' about 20 steps in. The reference model is eating memory I guess. What should I change?"*
- *"I have a base 8B model and thousands of human-ranked response pairs from annotators. I want a model that follows instructions and matches those human rankings, and I'd like a reward model along the way so I can score generations. Walk me through the stages and how to check it worked."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill fine-tuning-with-trl

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills fine-tuning-with-trl
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-training` category with `/plugin install ml-training@research-agent-skills`.

## Related

- [`constitutional-ai`](/skills/constitutional-ai)
- [`grpo-rl-training`](/skills/grpo-rl-training)
- [`simpo-training`](/skills/simpo-training)
- [`verl-rl-training`](/skills/verl-rl-training)
- [`llava`](/skills/llava)
- [`openrlhf-training`](/skills/openrlhf-training)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/fine-tuning-with-trl/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
