---
title: "vaex — AI agent skill for data science and ml"
description: "Processes and analyzes tabular datasets too large for RAM using Vaex, a Python library for lazy, out-of-core DataFrames over memory-mapped HDF5 and Arrow…"
keywords: ["big data", "out-of-core DataFrames", "HDF5", "data analysis", "Python"]
---

# `vaex`

**Category:** [data-science-and-ml](/skills#data-science-and-ml) · **License:** MIT · **Version:** 1.1

**Tags:** big data, out-of-core DataFrames, HDF5, data analysis, Python

## When to use it

Processes and analyzes tabular datasets too large for RAM using Vaex, a Python library for lazy, out-of-core DataFrames over memory-mapped HDF5 and Arrow files, with CSV and Parquet import/export. Covers virtual columns, filtering, groupby aggregations, large-data heatmaps and histograms, and vaex-ml transformers, PCA, and K-means. Use when opening or converting multi-gigabyte CSV/HDF5/Arrow/Parquet files, computing fast statistics on billions of rows, visualizing massive datasets, building ML pipelines that do not fit in memory, or speeding up slow aggregations with lazy evaluation and delay=True. Prefer polars when data fits in RAM, or dask for cluster-distributed work.

## Example requests

Ask your agent in plain language, for example:

- *"I have a 90 GB CSV of taxi trips and only 16 GB of RAM. What's the quickest way to get mean fare by pickup hour without crashing?"*
- *"I'm working with gaia_dr3_subset.hdf5, about 1.4 billion rows of stellar positions and magnitudes. I need a 2D density map of ra vs dec, plus a virtual column for galactic latitude, and I'm getting MemoryError when I load it with pandas.read_hdf. How do I fix this?"*
- *"We have several hundred million sensor readings in Parquet files that won't fit in memory. I want to standardize the features, run PCA down to 5 components, and cluster them with k-means, all without loading the data into memory. How should I set that up?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill vaex

# Kalaris Labs installer with checksum verification
npx research-agent-skills install vaex
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `data-science-and-ml` category with `/plugin install data-science-and-ml@research-agent-skills`.

## Related

- [`polars-bio`](/skills/polars-bio)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/vaex/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
