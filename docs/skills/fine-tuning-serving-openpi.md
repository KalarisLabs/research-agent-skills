---
title: "fine-tuning-serving-openpi — AI agent skill for multimodal and emerging"
description: "Fine-tune and serve Physical Intelligence OpenPI models (pi0, pi0-fast, pi0.5) using JAX or PyTorch backends for robot policy inference across ALOHA, DROID…"
keywords: ["OpenPI", "Physical Intelligence", "VLA", "Robotics", "JAX", "PyTorch", "Fine-Tuning", "Policy Serving", "ALOHA", "DROID", "LIBERO", "pi0"]
---

# `fine-tuning-serving-openpi`

**Category:** [multimodal-and-emerging](/skills#multimodal-and-emerging) · **License:** MIT · **Version:** 1.0.0

**Tags:** OpenPI, Physical Intelligence, VLA, Robotics, JAX, PyTorch, Fine-Tuning, Policy Serving, ALOHA, DROID, LIBERO, pi0

## When to use it

Fine-tune and serve Physical Intelligence OpenPI models (pi0, pi0-fast, pi0.5) using JAX or PyTorch backends for robot policy inference across ALOHA, DROID, and LIBERO environments. Use when adapting pi0 models to custom datasets, converting JAX checkpoints to PyTorch, running policy inference servers, or debugging norm stats and GPU memory issues.

## Example requests

Ask your agent in plain language, for example:

- *"How do I serve the pi0.5 DROID policy on one GPU so my robot can query it?"*
- *"I'm fine-tuning on my own LeRobot dataset, hf repo my-lab/ur5_pick_place, starting from pi05_libero in openpi's config.py. I launched train.py and it died with a missing norm stats error. After I fixed that, JAX OOM'd on my 1x A100 80GB. What should I do?"*
- *"My lab's vision-language-action model checkpoint was trained in JAX, but our deployment stack only supports PyTorch and we want to train further with multiple GPUs. How do we get there?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill fine-tuning-serving-openpi

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills fine-tuning-serving-openpi
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `multimodal-and-emerging` category with `/plugin install multimodal-and-emerging@research-agent-skills`.

## Related

- [`evaluating-cosmos-policy`](/skills/evaluating-cosmos-policy)
- [`fine-tuning-openvla-oft`](/skills/fine-tuning-openvla-oft)
- [`pufferlib`](/skills/pufferlib)
- [Skills for AI research](/fields/artificial-intelligence)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/fine-tuning-serving-openpi/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
