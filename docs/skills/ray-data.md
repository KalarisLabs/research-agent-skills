---
title: "ray-data — AI agent skill for multimodal and emerging"
description: "Scalable data processing for ML workloads. Streaming execution across CPU/GPU, supports Parquet/CSV/JSON/images."
keywords: ["Data Processing", "Ray Data", "Distributed Computing", "ML Pipelines", "Batch Inference", "ETL", "Scalable", "Ray", "PyTorch", "TensorFlow"]
---

# `ray-data`

**Category:** [multimodal-and-emerging](/skills#multimodal-and-emerging) · **License:** MIT · **Version:** 1.0.0

**Tags:** Data Processing, Ray Data, Distributed Computing, ML Pipelines, Batch Inference, ETL, Scalable, Ray, PyTorch, TensorFlow

## When to use it

Scalable data processing for ML workloads. Streaming execution across CPU/GPU, supports Parquet/CSV/JSON/images. Integrates with Ray Train, PyTorch, TensorFlow. Scales from single machine to 100s of nodes. Use for batch inference, data preprocessing, multi-modal data loading, or distributed ETL pipelines.

## Example requests

Ask your agent in plain language, for example:

- *"How do I read a folder of parquet files with Ray Data and apply a map_batches transform?"*
- *"I have about 2 TB of JPEGs in s3://lab-microscopy/plates/ and a ResNet-50 checkpoint. I need to run inference on all of them across 8 GPU nodes, but my current PyTorch DataLoader script runs out of memory and the GPUs sit idle. Write the pipeline and save predictions as parquet."*
- *"My preprocessing of a huge pile of sequencing-derived tables and microscopy images takes days on one workstation and won't fit in RAM. I'd like to stream it through tokenization and normalization steps over a cluster and feed the result straight into training. What's a good way to do this?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill ray-data

# Kalaris Labs installer with checksum verification
npx research-agent-skills install ray-data
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `multimodal-and-emerging` category with `/plugin install multimodal-and-emerging@research-agent-skills`.

## Related

- [`dask`](/skills/dask)
- [`nanogpt`](/skills/nanogpt)
- [`pathml`](/skills/pathml)
- [`polars`](/skills/polars)
- [`ray-train`](/skills/ray-train)
- [Skills for AI research](/fields/artificial-intelligence)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/ray-data/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
