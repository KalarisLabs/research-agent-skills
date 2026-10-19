---
title: "segment-anything-model — AI agent skill for multimodal and emerging"
description: "Foundation model for image segmentation with zero-shot transfer."
keywords: ["Multimodal", "Image Segmentation", "Computer Vision", "SAM", "Zero-Shot"]
---

# `segment-anything-model`

**Category:** [multimodal-and-emerging](/skills#multimodal-and-emerging) · **License:** MIT · **Version:** 1.0.0

**Tags:** Multimodal, Image Segmentation, Computer Vision, SAM, Zero-Shot

## When to use it

Foundation model for image segmentation with zero-shot transfer. Use when you need to segment any object in images using points, boxes, or masks as prompts, or automatically generate all object masks in an image.

## Example requests

Ask your agent in plain language, for example:

- *"Can you click-segment the tumor in this ultrasound image for me? I've got a point on it."*
- *"I'm working with ~400 SEM micrographs in ./sem_images/ (PNG, 2048x2048) and want per-particle masks for sizing. I ran SamAutomaticMaskGenerator with vit_h from sam_vit_h_4b8939.pth and got CUDA out of memory on a 12GB GPU. Small particles are also being missed. How do I fix this?"*
- *"I need to cut out every individual cell from my fluorescence microscopy images without training anything, and then use the masks as labels to train a smaller model later. What's a good approach?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill segment-anything-model

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills segment-anything-model
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `multimodal-and-emerging` category with `/plugin install multimodal-and-emerging@research-agent-skills`.

## Related

- [`clip`](/skills/clip)
- [`histolab`](/skills/histolab)
- [`blip-2-vision-language`](/skills/blip-2-vision-language)
- [`generate-image`](/skills/generate-image)
- [`timesfm-forecasting`](/skills/timesfm-forecasting)
- [Skills for AI research](/fields/artificial-intelligence)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/segment-anything-model/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
