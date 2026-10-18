---
title: "pathml — AI agent skill for clinical and health"
description: "Covers local, research-only computational pathology with PathML 3.0.5: loading and tiling whole-slide images (OpenSlide, Bio-Formats), preprocessing and QC…"
keywords: ["computational pathology", "whole slide images", "digital pathology", "medical imaging"]
---

# `pathml`

**Category:** [clinical-and-health](/skills#clinical-and-health) · **License:** MIT · **Version:** 1.2 · **Includes scripts**

**Tags:** computational pathology, whole slide images, digital pathology, medical imaging

## When to use it

Covers local, research-only computational pathology with PathML 3.0.5: loading and tiling whole-slide images (OpenSlide, Bio-Formats), preprocessing and QC pipelines run via SlideData.run(), .h5path data management, multiplex image quantification, spatial graph construction (KNN, RAG, HACT), and bounded local ONNX model inference planning. Use when loading or tiling slides, building tissue-mask or stain pipelines, managing .h5path files and patient-level splits, quantifying CODEX or Vectra multiplex images, or building cell and tissue graphs. Not for clinical diagnosis or patient care decisions.

## Example requests

Ask your agent in plain language, for example:

- *"How do I tile a .svs slide with PathML and run a tissue mask on it?"*
- *"I'm on Python 3.11 and ran `pip install pathml[all]` for my lab's CODEX project, and it errored out with a javabridge build failure on Windows. I have a 40-channel qptiff (codex_run3.qptiff) and want to segment nuclei and get per-cell marker means into AnnData. What should I do?"*
- *"I have 120 H&E slides from 60 patients, with two or three slides per patient. I want to build a graph for each slide in which cells are nodes and neighbours within a certain distance are linked, and then train a classifier on it. How should I set this up so my evaluation isn't leaky?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill pathml

# Kalaris Labs installer with checksum verification
npx research-agent-skills install pathml
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `clinical-and-health` category with `/plugin install clinical-and-health@research-agent-skills`.

## Related

- [`clinical-decision-support`](/skills/clinical-decision-support)
- [`ray-data`](/skills/ray-data)
- [Skills for medicine and clinical research](/fields/medicine)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/pathml/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
