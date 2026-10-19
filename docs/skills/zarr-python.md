---
title: "zarr-python — AI agent skill for data science and ml"
description: "Guides use of Zarr-Python 3 for storing chunked, compressed N-dimensional arrays and groups, with local, in-memory, ZIP, and fsspec-backed S3/GCS/HTTP stores…"
keywords: ["Zarr", "chunked arrays", "cloud storage", "N-dimensional data", "scientific data"]
---

# `zarr-python`

**Category:** [data-science-and-ml](/skills#data-science-and-ml) · **License:** MIT · **Version:** 1.3

**Tags:** Zarr, chunked arrays, cloud storage, N-dimensional data, scientific data

## When to use it

Guides use of Zarr-Python 3 for storing chunked, compressed N-dimensional arrays and groups, with local, in-memory, ZIP, and fsspec-backed S3/GCS/HTTP stores, plus NumPy, Dask, and Xarray integration. Covers array creation, resizing and appending, attributes, chunk and shard sizing, codecs, consolidated metadata, and v2-to-v3 migration. Use when creating or opening Zarr arrays or groups, choosing chunk sizes or compression for large datasets, reading or writing arrays on S3 or GCS, appending to time-series arrays, or migrating code from Zarr-Python 2 to 3. Use when setting up parallel I/O with Dask or Xarray. For labeled multi-dimensional datasets, use Xarray instead.

## Example requests

Ask your agent in plain language, for example:

- *"How do I append new rows to a zarr array as data comes in?"*
- *"I'm upgrading our pipeline in `ingest/store_frames.py` from zarr 2.16 to the latest release. I'm now getting `AttributeError: 'Group' object has no attribute 'create_dataset'` and `zarr.open(..., mode='a')` behaves differently with my old `.zarr` directory made with `DirectoryStore`. What changed and how do I fix it?"*
- *"I have a 2 TB stack of microscopy images (T x Z x Y x X, uint16) sitting in a bucket on S3. I want to convert it into something that many Dask workers can read slices from in parallel without downloading everything, and compression should keep storage costs down. How should I lay this out?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill zarr-python

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills zarr-python
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `data-science-and-ml` category with `/plugin install data-science-and-ml@research-agent-skills`.

## Related

- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/zarr-python/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
