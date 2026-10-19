---
title: "blip-2-vision-language — AI agent skill for multimodal and emerging"
description: "Explains how to use Salesforce BLIP-2 (Q-Former bridging a frozen image encoder and an LLM such as OPT or FlanT5) through HuggingFace Transformers and LAVIS…"
keywords: ["Multimodal", "Vision-Language", "Image Captioning", "VQA", "Zero-Shot"]
---

# `blip-2-vision-language`

**Category:** [multimodal-and-emerging](/skills#multimodal-and-emerging) · **License:** MIT · **Version:** 1.0.0

**Tags:** Multimodal, Vision-Language, Image Captioning, VQA, Zero-Shot

## When to use it

Explains how to use Salesforce BLIP-2 (Q-Former bridging a frozen image encoder and an LLM such as OPT or FlanT5) through HuggingFace Transformers and LAVIS for image captioning, visual question answering, image-text matching, and feature extraction. Use when generating captions for images, building a VQA system, doing zero-shot image-text understanding without task-specific training, matching or retrieving images against text, or fitting a BLIP-2 model into limited GPU memory with INT8/INT4 quantization. Prefer LLaVA or InstructBLIP for instruction-following multimodal chat, and CLIP for plain image-text similarity.

## Example requests

Ask your agent in plain language, for example:

- *"I've got a folder of 2,000 camera-trap photos. Can I auto-generate a short caption for each one with BLIP-2?"*
- *"I'm trying to load Salesforce/blip2-flan-t5-xxl in my lab's 16GB RTX 4080 with transformers and get 'CUDA out of memory' during from_pretrained. I'm running VQA on histology slide thumbnails in ./slides/*.png. How do I get this to fit?"*
- *"I want to build a tool where users upload a photo and type a natural-language question about it, like 'how many people are wearing helmets?', and the model answers without me having to train anything on labeled data. What open model and approach should I use?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill blip-2-vision-language

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills blip-2-vision-language
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `multimodal-and-emerging` category with `/plugin install multimodal-and-emerging@research-agent-skills`.

## Related

- [`quantizing-models-bitsandbytes`](/skills/quantizing-models-bitsandbytes)
- [`clip`](/skills/clip)
- [`llava`](/skills/llava)
- [`segment-anything-model`](/skills/segment-anything-model)
- [`stable-diffusion-image-generation`](/skills/stable-diffusion-image-generation)
- [Skills for AI research](/fields/artificial-intelligence)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/blip-2-vision-language/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
