---
title: "stable-diffusion-image-generation — AI agent skill for multimodal and emerging"
description: "Generates images with Stable Diffusion models (SD 1.5, SDXL, SD 3.0, Flux) through the HuggingFace Diffusers library, covering text-to-image, image-to-image…"
keywords: ["Image Generation", "Stable Diffusion", "Diffusers", "Text-to-Image", "Multimodal", "Computer Vision"]
---

# `stable-diffusion-image-generation`

**Category:** [multimodal-and-emerging](/skills#multimodal-and-emerging) · **License:** MIT · **Version:** 1.0.0

**Tags:** Image Generation, Stable Diffusion, Diffusers, Text-to-Image, Multimodal, Computer Vision

## When to use it

Generates images with Stable Diffusion models (SD 1.5, SDXL, SD 3.0, Flux) through the HuggingFace Diffusers library, covering text-to-image, image-to-image, inpainting, outpainting, ControlNet conditioning, LoRA adapters, scheduler swapping, and GPU memory optimization. Use when generating images from text prompts, transforming or restyling an existing image, filling masked regions of an image, adding spatial control from edges, poses, or depth maps, loading LoRA style adapters, or fixing out-of-memory and black-image errors in a Diffusers pipeline. Not for API-only generation without a GPU, where DALL-E 3 fits better.

## Example requests

Ask your agent in plain language, for example:

- *"How do I make SDXL fit on my 8GB card? I keep getting CUDA out of memory in diffusers."*
- *"I'm running StableDiffusionXLPipeline.from_pretrained('stabilityai/stable-diffusion-xl-base-1.0', torch_dtype=torch.float16) on an RTX 3090 and every image comes out as pure black. A warning says 'invalid value encountered in cast'. How do I fix it? I'm making figures for a methods paper on histology slide augmentation."*
- *"I have a set of grayscale microscope photos of cell cultures. I want to turn each one into a colorized, painted look while keeping the cell layout and shapes the same. I have a local GPU. What's a good way to do this?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill stable-diffusion-image-generation

# Kalaris Labs installer with checksum verification
npx research-agent-skills install stable-diffusion-image-generation
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `multimodal-and-emerging` category with `/plugin install multimodal-and-emerging@research-agent-skills`.

## Related

- [`fine-tuning-openvla-oft`](/skills/fine-tuning-openvla-oft)
- [`peft-fine-tuning`](/skills/peft-fine-tuning)
- [`blip-2-vision-language`](/skills/blip-2-vision-language)
- [Skills for AI research](/fields/artificial-intelligence)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/stable-diffusion-image-generation/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
