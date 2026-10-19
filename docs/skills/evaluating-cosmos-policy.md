---
title: "evaluating-cosmos-policy — AI agent skill for multimodal and emerging"
description: "Evaluates NVIDIA Cosmos Policy on LIBERO and RoboCasa simulation environments."
keywords: ["Cosmos Policy", "VLA", "Robotics", "LIBERO", "RoboCasa", "Simulation", "Evaluation", "Profiling", "EGL Rendering"]
---

# `evaluating-cosmos-policy`

**Category:** [multimodal-and-emerging](/skills#multimodal-and-emerging) · **License:** MIT · **Version:** 1.0.0

**Tags:** Cosmos Policy, VLA, Robotics, LIBERO, RoboCasa, Simulation, Evaluation, Profiling, EGL Rendering

## When to use it

Evaluates NVIDIA Cosmos Policy on LIBERO and RoboCasa simulation environments. Use when setting up cosmos-policy for robot manipulation evaluation, running headless GPU evaluations with EGL rendering, or profiling inference latency on cluster or local GPU machines.

## Example requests

Ask your agent in plain language, for example:

- *"How do I run a quick cosmos policy eval on LIBERO?"*
- *"I'm on a headless A100 node and trying to run run_robocasa_eval for Cosmos Policy. Kitchen object sampling gives NaNs and some asset lookups fail. I installed robocasa from the upstream PyPI/GitHub repo. What should I do?"*
- *"I want to reproduce NVIDIA's published numbers for their video-model-based robot policy on the LIBERO suites on our cluster, starting from a fresh machine with nothing installed. Also, I'd like to know whether my reproduced average will match the reported one."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill evaluating-cosmos-policy

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills evaluating-cosmos-policy
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `multimodal-and-emerging` category with `/plugin install multimodal-and-emerging@research-agent-skills`.

## Related

- [`fine-tuning-openvla-oft`](/skills/fine-tuning-openvla-oft)
- [`fine-tuning-serving-openpi`](/skills/fine-tuning-serving-openpi)
- [`phoenix-observability`](/skills/phoenix-observability)
- [`pufferlib`](/skills/pufferlib)
- [Skills for AI research](/fields/artificial-intelligence)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/evaluating-cosmos-policy/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
