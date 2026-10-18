---
title: "nemo-curator — AI agent skill for multimodal and emerging"
description: "GPU-accelerated data curation for LLM training. Supports text/image/video/audio."
keywords: ["Data Processing", "NeMo Curator", "Data Curation", "GPU Acceleration", "Deduplication", "Quality Filtering", "NVIDIA", "RAPIDS", "PII Redaction", "Multimodal", "LLM Training Data"]
---

# `nemo-curator`

**Category:** [multimodal-and-emerging](/skills#multimodal-and-emerging) · **License:** MIT · **Version:** 1.0.0

**Tags:** Data Processing, NeMo Curator, Data Curation, GPU Acceleration, Deduplication, Quality Filtering, NVIDIA, RAPIDS, PII Redaction, Multimodal, LLM Training Data

## When to use it

GPU-accelerated data curation for LLM training. Supports text/image/video/audio. Features fuzzy deduplication (16× faster), quality filtering (30+ heuristics), semantic deduplication, PII redaction, NSFW detection. Scales across GPUs with RAPIDS. Use for preparing high-quality training datasets, cleaning web data, or deduplicating large corpora.

## Example requests

Ask your agent in plain language, for example:

- *"How do I dedupe a big text corpus on GPUs with NeMo Curator?"*
- *"I have about 2TB of Common Crawl WARC-derived JSONL shards in /data/cc/*.jsonl with 'text' and 'url' fields. I need to drop low-quality docs, redact emails and phone numbers, and remove near-duplicates before pretraining a 7B model. I have 4 A100 80GB nodes. Can you set up a NeMo Curator pipeline and write the output as Parquet?"*
- *"I scraped millions of web pages for pretraining a language model. A lot of it is boilerplate, repeated pages, junk, and has personal info in it. What's the best way to get this into shape using my multi-GPU server before training?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill nemo-curator

# Kalaris Labs installer with checksum verification
npx research-agent-skills install nemo-curator
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `multimodal-and-emerging` category with `/plugin install multimodal-and-emerging@research-agent-skills`.

## Related

- [`exa-search`](/skills/exa-search)
- [`nemo-guardrails`](/skills/nemo-guardrails)
- [Skills for AI research](/fields/artificial-intelligence)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/nemo-curator/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
