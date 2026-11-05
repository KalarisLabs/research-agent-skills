---
title: "ray-train — AI agent skill for ml training"
description: "Distributed training orchestration across clusters. Scales PyTorch/TensorFlow/HuggingFace from laptop to 1000s of nodes."
keywords: ["Ray Train", "Distributed Training", "Orchestration", "Ray", "Hyperparameter Tuning", "Fault Tolerance", "Elastic Scaling", "Multi-Node", "PyTorch", "TensorFlow"]
---

# `ray-train`

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

**Tags:** Ray Train, Distributed Training, Orchestration, Ray, Hyperparameter Tuning, Fault Tolerance, Elastic Scaling, Multi-Node, PyTorch, TensorFlow

## When to use it

Distributed training orchestration across clusters. Scales PyTorch/TensorFlow/HuggingFace from laptop to 1000s of nodes. Built-in hyperparameter tuning with Ray Tune, fault tolerance, elastic scaling. Use when training massive models across multiple machines or running distributed hyperparameter sweeps.

## Example requests

Ask your agent in plain language, for example:

- *"How do I run my PyTorch training across 4 machines with 8 GPUs each?"*
- *"My train.py fine-tunes a Llama-style model with HF Trainer on a single A100 and I now have a 6-node Ray cluster. Running ray status shows only the head node, and workers fail with 'Unable to connect to GCS at 10.0.0.5:6379'. How do I get this training across the whole cluster with checkpointing so it survives a node dying?"*
- *"I need to find the best learning rate, weight decay and batch size for my ResNet on our shared cluster. I'd like to try a couple hundred configs in parallel and stop the bad ones early. What's the approach?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill ray-train

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills ray-train
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-training` category with `/plugin install ml-training@research-agent-skills`.

## Related

- [`dask`](/skills/dask)
- [`pytorch-lightning-distributed`](/skills/pytorch-lightning-distributed)
- [`ray-data`](/skills/ray-data)
- [`weights-and-biases`](/skills/weights-and-biases)
- [`skypilot-multi-cloud-orchestration`](/skills/skypilot-multi-cloud-orchestration)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/ray-train/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
