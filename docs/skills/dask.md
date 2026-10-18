---
title: "dask — AI agent skill for data science and ml"
description: "Distributed computing for larger-than-RAM pandas/NumPy workflows. Use when you need to scale existing pandas/NumPy code beyond memory or across clusters."
keywords: ["parallel computing", "big data", "pandas", "distributed computing", "data science"]
---

# `dask`

**Category:** [data-science-and-ml](/skills#data-science-and-ml) · **License:** BSD-3-Clause license · **Version:** 1.2

**Tags:** parallel computing, big data, pandas, distributed computing, data science

## When to use it

Distributed computing for larger-than-RAM pandas/NumPy workflows. Use when you need to scale existing pandas/NumPy code beyond memory or across clusters. Best for parallel file processing, distributed ML, integration with existing pandas code. For out-of-core analytics on single machine use vaex; for in-memory speed use polars.

## Example requests

Ask your agent in plain language, for example:

- *"my pandas script keeps getting OOM killed on a 40GB folder of CSVs, how do I make it work without rewriting everything?"*
- *"I have ~600 GB of Sentinel-2 derived GeoTIFF stacks converted to Zarr, shape (time, band, y, x). I'm computing per-pixel NDVI percentiles with NumPy on my 64 GB workstation and it crashes with MemoryError. I tried dask.array but the dashboard shows millions of tasks and the scheduler hangs for minutes before anything runs. What should I change?"*
- *"I need to run the same preprocessing function on about 5,000 independent log files and some of them depend on the output of others. I'd like to spread this over our 4-node cluster and add new jobs dynamically as results come in. What's a good way to set this up?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill dask

# Kalaris Labs installer with checksum verification
npx research-agent-skills install dask
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `data-science-and-ml` category with `/plugin install data-science-and-ml@research-agent-skills`.

## Related

- [`ray-data`](/skills/ray-data)
- [`ray-train`](/skills/ray-train)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/dask/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
