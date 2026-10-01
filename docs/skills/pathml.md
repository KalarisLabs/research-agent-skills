---
title: "pathml — AI agent skill for clinical and health"
description: "Covers local, research-only computational pathology with PathML 3.0.5: loading and tiling whole-slide images (OpenSlide, Bio-Formats), preprocessing and Q…"
---

# `pathml`

> Covers local, research-only computational pathology with PathML 3.0.5: loading and tiling whole-slide images (OpenSlide, Bio-Formats), preprocessing and QC pipelines run via SlideData.run(), .h5path data management, multiplex image quantification, spatial graph construction (KNN, RAG, HACT), and bounded local ONNX model inference planning. Use when loading or tiling slides, building tissue-mask or stain pipelines, managing .h5path files and patient-level splits, quantifying CODEX or Vectra multiplex images, or building cell and tissue graphs. Not for clinical diagnosis or patient care decisions.

**Category:** [clinical-and-health](/skills#clinical-and-health) · **License:** MIT · **Version:** 1.2

## Install

```bash
npx skills add KalarisLabs/research-agent-skills --skill pathml
```

## When to use it

Covers local, research-only computational pathology with PathML 3.0.5: loading and tiling whole-slide images (OpenSlide, Bio-Formats), preprocessing and QC pipelines run via SlideData.run(), .h5path data management, multiplex image quantification, spatial graph construction (KNN, RAG, HACT), and bounded local ONNX model inference planning. Use when loading or tiling slides, building tissue-mask or stain pipelines, managing .h5path files and patient-level splits, quantifying CODEX or Vectra multiplex images, or building cell and tissue graphs. Not for clinical diagnosis or patient care decisions.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/pathml/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
