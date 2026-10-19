---
title: "lamindb — AI agent skill for data science and ml"
description: "Use when working with LaminDB, the open-source lineage-native lakehouse for biological datasets and models."
keywords: ["data lineage", "biological data", "data management", "ontologies", "MLOps"]
---

# `lamindb`

**Category:** [data-science-and-ml](/skills#data-science-and-ml) · **License:** Apache-2.0 license · **Version:** 1.2

**Tags:** data lineage, biological data, data management, ontologies, MLOps

## When to use it

Use when working with LaminDB, the open-source lineage-native lakehouse for biological datasets and models. Covers setup, artifact registration, query/search, lineage tracking, validation, ontology-backed annotation with Bionty, collections, branches, storage, and workflow integrations.

## Example requests

Ask your agent in plain language, for example:

- *"How do I register a parquet file as an artifact in LaminDB and see which notebook produced it?"*
- *"I have a 10x PBMC dataset in pbmc_filtered.h5ad (human, 18k cells) and I'm getting 'N terms are not validated' for obs['cell_type'] and obs['tissue'] when I run curator.validate(). I want to map them to Cell Ontology and Uberon before saving. What should I do?"*
- *"Our lab has hundreds of flow cytometry and RNA-seq files scattered across S3 buckets. I want one place where I can filter them by tissue, donor and experiment date, and trace each processed file back to the script and inputs that made it. What setup would you suggest?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill lamindb

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills lamindb
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `data-science-and-ml` category with `/plugin install data-science-and-ml@research-agent-skills`.

## Related

- [`qdrant-vector-search`](/skills/qdrant-vector-search)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/lamindb/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
