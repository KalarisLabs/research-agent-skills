---
title: "simpo-training — AI agent skill for ml training"
description: "Simple Preference Optimization for LLM alignment. Reference-free alternative to DPO with better performance (+6.4 points on AlpacaEval 2.0)."
keywords: ["Post-Training", "SimPO", "Preference Optimization", "Alignment", "DPO Alternative", "Reference-Free", "LLM Alignment", "Efficient Training"]
---

# `simpo-training`

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

**Tags:** Post-Training, SimPO, Preference Optimization, Alignment, DPO Alternative, Reference-Free, LLM Alignment, Efficient Training

## When to use it

Simple Preference Optimization for LLM alignment. Reference-free alternative to DPO with better performance (+6.4 points on AlpacaEval 2.0). No reference model needed, more efficient than DPO. Use for preference alignment when want simpler, faster training than DPO/PPO.

## Example requests

Ask your agent in plain language, for example:

- *"How do I train a model with SimPO instead of DPO?"*
- *"I have 60k chosen/rejected pairs in ultrafeedback_binarized.jsonl and a single node with 2x A100 40GB. I want to align Llama-3-8B-Instruct. My last run with lr 1e-5 had the loss go to NaN after about 200 steps. Can you set up the config and help me stop it from diverging?"*
- *"I've got a Mistral 7B that's already been SFT'd, plus a pile of pairwise human preference labels. I want to push it toward preferred responses without the memory cost of keeping a frozen copy of the model around, and I don't want to build a reward model or run PPO. What's the simplest approach and how do I run it?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill simpo-training

# Kalaris Labs installer with checksum verification
npx research-agent-skills install simpo-training
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-training` category with `/plugin install ml-training@research-agent-skills`.

## Related

- [`fine-tuning-with-trl`](/skills/fine-tuning-with-trl)
- [`openrlhf-training`](/skills/openrlhf-training)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/simpo-training/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
