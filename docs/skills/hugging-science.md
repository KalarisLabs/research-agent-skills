---
title: "hugging-science — AI agent skill for data science and ml"
description: "Use when the user is doing AI/ML work in a scientific domain such as biology, chemistry, physics, astronomy, climate, genomics, materials, medicine, ecology…"
keywords: ["AI for science", "scientific datasets", "foundation models", "Hugging Face", "machine learning"]
---

# `hugging-science`

**Category:** [data-science-and-ml](/skills#data-science-and-ml) · **License:** MIT · **Version:** 1.3 · **Includes scripts**

**Tags:** AI for science, scientific datasets, foundation models, Hugging Face, machine learning

## When to use it

Use when the user is doing AI/ML work in a scientific domain such as biology, chemistry, physics, astronomy, climate, genomics, materials, medicine, ecology, energy, engineering, math, drug discovery, protein design, weather modeling, theorem proving, single-cell, or PDE solving. Hugging Science is a curated catalog of scientific datasets, models, blog posts, and interactive Spaces. This skill helps discover and use resources via `datasets`, `transformers`, the HF Inference API, `gradio_client`, and methodology citations.

## Example requests

Ask your agent in plain language, for example:

- *"Is there a good open dataset for single-cell RNA-seq of human immune cells on the HF Hub?"*
- *"I'm fine-tuning ESM2 650M on my stability labels in stability.csv (about 12k sequences) and keep hitting CUDA OOM on a 16GB GPU with batch size 16. Is there a smaller ESM variant or a better setup in the HF ecosystem, and is there a methodology write-up I should cite?"*
- *"I want to design a protein binder against a target I have a PDB file for, but I don't have a big GPU. What are my options?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill hugging-science

# Kalaris Labs installer with checksum verification
npx research-agent-skills install hugging-science
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `data-science-and-ml` category with `/plugin install data-science-and-ml@research-agent-skills`.

## Related

- [`brainstorming-research-ideas`](/skills/brainstorming-research-ideas)
- [`science-aaas`](/skills/science-aaas)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/hugging-science/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
