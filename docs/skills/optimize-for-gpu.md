---
title: "optimize-for-gpu — AI agent skill for data science and ml"
description: "GPU-accelerates scientific Python on NVIDIA hardware and verifies that the result is correct and faster."
keywords: ["GPU acceleration", "CUDA", "performance optimization", "scientific Python"]
---

# `optimize-for-gpu`

**Category:** [data-science-and-ml](/skills#data-science-and-ml) · **License:** MIT · **Version:** 1.4

**Tags:** GPU acceleration, CUDA, performance optimization, scientific Python

## When to use it

GPU-accelerates scientific Python on NVIDIA hardware and verifies that the result is correct and faster. Use for CUDA/GPU optimization; CPU-bound NumPy, SciPy, pandas, scikit-learn, NetworkX, scikit-image, vector-search, image-processing, graph, simulation, or file-I/O workloads; CuPy, cuDF, cuML, cuGraph, cuVS, cuCIM, KvikIO, Warp, Newton, Numba-CUDA, or RAFT questions; and profiling, memory-transfer, kernel, or multi-GPU bottlenecks. Also use when large data-parallel Python code is slow and GPU acceleration is a plausible option, even if the user does not name CUDA.

## Example requests

Ask your agent in plain language, for example:

- *"My numpy simulation loop is crawling on 50M-element arrays. Can I put it on my RTX GPU?"*
- *"I have a 40 GB pandas script, `merge_cohorts.py`, that does groupby/merge on UK Biobank phenotype tables and takes 3 hours on one A100 box. I tried `import cudf` directly and got `MemoryError: std::bad_alloc` from RMM. How should I speed this up?"*
- *"We run a nearest-neighbor lookup over about 20 million protein embeddings with Faiss on CPU and queries take seconds. We'd like them much faster, and we need results close to what we get now. What are our options?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill optimize-for-gpu

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills optimize-for-gpu
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `data-science-and-ml` category with `/plugin install data-science-and-ml@research-agent-skills`.

## Related

- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/optimize-for-gpu/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
