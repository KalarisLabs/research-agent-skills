---
title: "scientific-schematics — AI agent skill for visualization and presentation"
description: "Generates publication-style scientific diagrams as raster PNG images from a natural-language prompt, using Nano Banana 2 via OpenRouter, then scores each…"
keywords: ["scientific diagrams", "schematics", "figures", "illustrations"]
---

# `scientific-schematics`

**Category:** [visualization-and-presentation](/skills#visualization-and-presentation) · **License:** MIT · **Version:** 1.7 · **Includes scripts**

**Tags:** scientific diagrams, schematics, figures, illustrations

## When to use it

Generates publication-style scientific diagrams as raster PNG images from a natural-language prompt, using Nano Banana 2 via OpenRouter, then scores each image with Gemini 3.6 Flash against a document-type threshold (journal, conference, thesis, grant, preprint, poster, etc.) and regenerates up to twice. Writes versioned PNGs and a review_log.json. Use when drawing neural network architectures, CONSORT or PRISMA flowcharts, biological signaling pathways, system or block diagrams, or circuit schematics. Use when a figure needs a quality score and critique recorded for a paper, poster, or grant. Not for vector, PDF, SVG, or EPS output, or for data plots; use a plotting skill for those. Prompts leave the machine, so avoid unpublished or patient data.

## Example requests

Ask your agent in plain language, for example:

- *"Draw me a PRISMA flow diagram for my systematic review: 1,240 records identified, 310 duplicates removed, 930 screened, 112 full-text assessed, 41 included."*
- *"I'm submitting to Nature Communications. I need a figure of our U-Net variant: 4 encoder blocks (64-512 channels) with 3x3 convs and max-pool, a bottleneck, 4 decoder blocks with skip connections, and a 1x1 conv output head. Save it to figures/unet_arch.png and tell me whether it would pass review for the journal threshold."*
- *"For my grant proposal I need a clear picture showing how EGF binding leads to a kinase cascade that ends with transcription changes in the nucleus. Something I can drop into the methods background section, with a quality check on it."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill scientific-schematics

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills scientific-schematics
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `visualization-and-presentation` category with `/plugin install visualization-and-presentation@research-agent-skills`.

## Related

- [`academic-plotting`](/skills/academic-plotting)
- [`autoskill`](/skills/autoskill)
- [`generate-image`](/skills/generate-image)
- [`infographics`](/skills/infographics)
- [`markdown-mermaid-writing`](/skills/markdown-mermaid-writing)
- [`matplotlib`](/skills/matplotlib)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/scientific-schematics/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
