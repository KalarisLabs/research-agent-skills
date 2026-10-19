---
title: "fine-tuning-openvla-oft — AI agent skill for multimodal and emerging"
description: "Fine-tunes and evaluates OpenVLA-OFT and OpenVLA-OFT+ policies for robot action generation with continuous action heads, LoRA adaptation, and FiLM…"
keywords: ["OpenVLA", "OpenVLA-OFT", "VLA", "Robotics", "Fine-Tuning", "LIBERO", "ALOHA", "LoRA", "FiLM", "Action Chunking", "Deployment", "Continuous Actions"]
---

# `fine-tuning-openvla-oft`

**Category:** [multimodal-and-emerging](/skills#multimodal-and-emerging) · **License:** MIT · **Version:** 1.0.0

**Tags:** OpenVLA, OpenVLA-OFT, VLA, Robotics, Fine-Tuning, LIBERO, ALOHA, LoRA, FiLM, Action Chunking, Deployment, Continuous Actions

## When to use it

Fine-tunes and evaluates OpenVLA-OFT and OpenVLA-OFT+ policies for robot action generation with continuous action heads, LoRA adaptation, and FiLM conditioning on LIBERO simulation and ALOHA real-world setups. Use when reproducing OpenVLA-OFT paper results, training custom VLA action heads (L1 or diffusion), deploying server-client inference for ALOHA, or debugging normalization, LoRA merge, and cross-GPU issues.

## Example requests

Ask your agent in plain language, for example:

- *"How do I evaluate the pretrained OpenVLA-OFT checkpoint on LIBERO-Goal?"*
- *"I fine-tuned an OFT+ policy on my own ALOHA data with 3 cameras. The server starts fine, but the arms move with the wrong scale and the actions look jittery. I trained with --use_film True --num_images_in_input 3 --image_aug True. The client calls http://gpu-box:8777/act. What should I check?"*
- *"I have a 7B vision-language-action model and about 200 teleoperated demos in RLDS format for a tabletop task. I want to adapt it with low-rank adapters and swap the discrete action-token output for a regression head. How should I set up the training run, and which checkpoints should I evaluate?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill fine-tuning-openvla-oft

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills fine-tuning-openvla-oft
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `multimodal-and-emerging` category with `/plugin install multimodal-and-emerging@research-agent-skills`.

## Related

- [`evaluating-cosmos-policy`](/skills/evaluating-cosmos-policy)
- [`fine-tuning-serving-openpi`](/skills/fine-tuning-serving-openpi)
- [`stable-diffusion-image-generation`](/skills/stable-diffusion-image-generation)
- [Skills for AI research](/fields/artificial-intelligence)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/fine-tuning-openvla-oft/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
