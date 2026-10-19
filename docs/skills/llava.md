---
title: "llava — AI agent skill for multimodal and emerging"
description: "Large Language and Vision Assistant. Enables visual instruction tuning and image-based conversations."
keywords: ["LLaVA", "Vision-Language", "Multimodal", "Visual Question Answering", "Image Chat", "CLIP", "Vicuna", "Conversational AI", "Instruction Tuning", "VQA"]
---

# `llava`

**Category:** [multimodal-and-emerging](/skills#multimodal-and-emerging) · **License:** MIT · **Version:** 1.0.0

**Tags:** LLaVA, Vision-Language, Multimodal, Visual Question Answering, Image Chat, CLIP, Vicuna, Conversational AI, Instruction Tuning, VQA

## When to use it

Large Language and Vision Assistant. Enables visual instruction tuning and image-based conversations. Combines CLIP vision encoder with Vicuna/LLaMA language models. Supports multi-turn image chat, visual question answering, and instruction following. Use for vision-language chatbots or image understanding tasks. Best for conversational image analysis.

## Example requests

Ask your agent in plain language, for example:

- *"How do I run LLaVA on a folder of microscopy screenshots and ask it questions about each one?"*
- *"I'm on a single 24 GB RTX 4090 and want to run llava-v1.5-13b on scanned lab notebook pages from notebooks_2024/. Loading it in fp16 gives 'CUDA out of memory'. What should I change, and how well will it read the handwriting?"*
- *"I want an open-source assistant that can look at a chest X-ray figure from a paper and then answer follow-up questions about it over several turns, running locally. What do you suggest, and how would I set it up?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill llava

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills llava
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `multimodal-and-emerging` category with `/plugin install multimodal-and-emerging@research-agent-skills`.

## Related

- [`blip-2-vision-language`](/skills/blip-2-vision-language)
- [`fine-tuning-with-trl`](/skills/fine-tuning-with-trl)
- [Skills for AI research](/fields/artificial-intelligence)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/llava/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
