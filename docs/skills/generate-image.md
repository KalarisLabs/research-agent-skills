---
title: "generate-image — AI agent skill for visualization and presentation"
description: "Generate or edit images with AI models through the OpenRouter Image API (Gemini, Seedream, Recraft, GPT-Image, Riverflow)."
keywords: ["image generation", "illustrations", "figures", "visual assets", "AI images"]
---

# `generate-image`

**Category:** [visualization-and-presentation](/skills#visualization-and-presentation) · **License:** MIT · **Version:** 3.1 · **Includes scripts**

**Tags:** image generation, illustrations, figures, visual assets, AI images

## When to use it

Generate or edit images with AI models through the OpenRouter Image API (Gemini, Seedream, Recraft, GPT-Image, Riverflow). Use for photos, illustrations, artwork, concept art, visual assets, logos, and image editing or compositing from reference images. For flowcharts, circuits, pathways, and other technical diagrams, use the scientific-schematics skill instead.

## Example requests

Ask your agent in plain language, for example:

- *"Make me a cover image for my lab's seminar poster: a moody, photorealistic close-up of a petri dish with glowing bioluminescent bacteria, lots of dark space on the left for the title."*
- *"I need a transparent-background PNG of a stylized mouse silhouette for my slide deck. I tried `--model openai/gpt-image-2 --background transparent` and it got rejected. What should I do?"*
- *"I have field_site.jpg, a photo of our alpine sampling station. Can you change the sky so it looks like sunset and keep everything else the same? Then give me a few variations to choose from."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill generate-image

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills generate-image
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `visualization-and-presentation` category with `/plugin install visualization-and-presentation@research-agent-skills`.

## Related

- [`autoskill`](/skills/autoskill)
- [`latex-posters`](/skills/latex-posters)
- [`scientific-schematics`](/skills/scientific-schematics)
- [`scientific-slides`](/skills/scientific-slides)
- [`infographics`](/skills/infographics)
- [`segment-anything-model`](/skills/segment-anything-model)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/generate-image/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
