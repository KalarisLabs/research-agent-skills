---
title: "histolab — AI agent skill for clinical and health"
description: "Extracts tiles and preprocesses H&E whole slide images with the histolab Python library (OpenSlide), covering slide inspection, tissue masks (TissueMask,…"
---

# `histolab`

> Extracts tiles and preprocesses H&E whole slide images with the histolab Python library (OpenSlide), covering slide inspection, tissue masks (TissueMask, BiggestTissueBoxMask), RandomTiler, GridTiler and ScoreTiler extraction, image and morphological filters, and Macenko or Reinhard stain normalization. Use when building a tile dataset from WSI files for deep learning. Use when detecting tissue and excluding background or pen annotations. Use when previewing tile locations and exporting tile CSV reports. Use when normalizing stain variation across slides. Not for spatial proteomics, multiplexed imaging, or deep learning pipelines; use pathml for those.

**Category:** [clinical-and-health](/skills#clinical-and-health) · **License:** Apache-2.0 license · **Version:** 1.3

## Install

```bash
npx skills add KalarisLabs/research-agent-skills --skill histolab
```

## When to use it

Extracts tiles and preprocesses H&E whole slide images with the histolab Python library (OpenSlide), covering slide inspection, tissue masks (TissueMask, BiggestTissueBoxMask), RandomTiler, GridTiler and ScoreTiler extraction, image and morphological filters, and Macenko or Reinhard stain normalization. Use when building a tile dataset from WSI files for deep learning. Use when detecting tissue and excluding background or pen annotations. Use when previewing tile locations and exporting tile CSV reports. Use when normalizing stain variation across slides. Not for spatial proteomics, multiplexed imaging, or deep learning pipelines; use pathml for those.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/histolab/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
