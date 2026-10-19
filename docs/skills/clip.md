---
title: "clip — AI agent skill for multimodal and emerging"
description: "OpenAI's model connecting vision and language. Enables zero-shot image classification, image-text matching, and cross-modal retrieval."
keywords: ["Multimodal", "CLIP", "Vision-Language", "Zero-Shot", "Image Classification", "OpenAI", "Image Search", "Cross-Modal Retrieval", "Content Moderation"]
---

# `clip`

**Category:** [multimodal-and-emerging](/skills#multimodal-and-emerging) · **License:** MIT · **Version:** 1.0.0

**Tags:** Multimodal, CLIP, Vision-Language, Zero-Shot, Image Classification, OpenAI, Image Search, Cross-Modal Retrieval, Content Moderation

## When to use it

OpenAI's model connecting vision and language. Enables zero-shot image classification, image-text matching, and cross-modal retrieval. Trained on 400M image-text pairs. Use for image search, content moderation, or vision-language tasks without fine-tuning. Best for general-purpose image understanding.

## Example requests

Ask your agent in plain language, for example:

- *"How do I do zero-shot labeling of a folder of photos with CLIP?"*
- *"I have ~40k product photos in /data/catalog/ as JPGs and want a text search box so users can type 'red leather ankle boots' and get the closest images back. I was thinking of ViT-L/14 embeddings stored in FAISS, but my laptop only has 6GB of VRAM and I keep getting CUDA out of memory when I encode in batches of 256. What should I change?"*
- *"We're building a moderation pipeline for user-uploaded images on our research forum. We have no labeled data and no budget to train anything. Can we flag violent or explicit images by comparing the pictures against text descriptions of those categories? How would you set it up and how far can we trust it?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill clip

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills clip
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `multimodal-and-emerging` category with `/plugin install multimodal-and-emerging@research-agent-skills`.

## Related

- [`blip-2-vision-language`](/skills/blip-2-vision-language)
- [`segment-anything-model`](/skills/segment-anything-model)
- [Skills for AI research](/fields/artificial-intelligence)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/clip/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
