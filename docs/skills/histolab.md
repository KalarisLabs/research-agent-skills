---
title: "histolab — AI agent skill for clinical and health"
description: "Extracts tiles and preprocesses H&E whole slide images with the histolab Python library (OpenSlide), covering slide inspection, tissue masks (TissueMask…"
keywords: ["digital pathology", "whole slide images", "H&E", "tile extraction", "medical imaging"]
---

# `histolab`

**Category:** [clinical-and-health](/skills#clinical-and-health) · **License:** Apache-2.0 license · **Version:** 1.3

**Tags:** digital pathology, whole slide images, H&E, tile extraction, medical imaging

## When to use it

Extracts tiles and preprocesses H&E whole slide images with the histolab Python library (OpenSlide), covering slide inspection, tissue masks (TissueMask, BiggestTissueBoxMask), RandomTiler, GridTiler and ScoreTiler extraction, image and morphological filters, and Macenko or Reinhard stain normalization. Use when building a tile dataset from WSI files for deep learning. Use when detecting tissue and excluding background or pen annotations. Use when previewing tile locations and exporting tile CSV reports. Use when normalizing stain variation across slides. Not for spatial proteomics, multiplexed imaging, or deep learning pipelines; use pathml for those.

## Example requests

Ask your agent in plain language, for example:

- *"How do I pull 512x512 tiles out of an H&E slide and skip the blank glass?"*
- *"I have 40 TCGA-BRCA .svs files in ./slides/ and need a training set of 20x patches for a ResNet. Some slides have green pen marks around the tumor and tiles over those regions are polluting my set. I'm using RandomTiler with n_tiles=200 and seed=42, but the pen regions still show up. Also I need a CSV with the tile coordinates. How should I set this up?"*
- *"My slides come from three different labs and the eosin intensity varies a lot, which is hurting my classifier's generalization. How can I make the colors consistent before I train?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill histolab

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills histolab
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `clinical-and-health` category with `/plugin install clinical-and-health@research-agent-skills`.

## Related

- [`scientific-slides`](/skills/scientific-slides)
- [`segment-anything-model`](/skills/segment-anything-model)
- [Skills for medicine and clinical research](/fields/medicine)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/histolab/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
