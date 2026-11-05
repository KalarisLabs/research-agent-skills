---
title: "pathogen-variant-surveillance — AI agent skill for life sciences"
description: "Query live pathogen genomic surveillance data through the GenSpectrum LAPIS API to find which viral lineages are circulating now, how fast they are growing…"
keywords: ["pathogen genomics", "genomic surveillance", "viral lineages", "epidemiology"]
---

# `pathogen-variant-surveillance`

**Category:** [life-sciences](/skills#life-sciences) · **License:** MIT · **Version:** 1.1 · **Includes scripts**

**Tags:** pathogen genomics, genomic surveillance, viral lineages, epidemiology

## When to use it

Query live pathogen genomic surveillance data through the GenSpectrum LAPIS API to find which viral lineages are circulating now, how fast they are growing, and what mutations they carry. Use whenever a question depends on the current state of a pathogen population rather than on remembered facts - which SARS-CoV-2 variant is dominant, whether a Pango lineage is still designated or has been withdrawn, what clade or genotype of H5N1 is in a host or region, whether a PCR primer or assay target still matches circulating sequence, or how a lineage's prevalence has moved week to week. Triggers include "variant surveillance", "genomic surveillance", "what variant is circulating", "dominant variant", "Pango lineage", "lineage prevalence", "growth advantage", "SARS-CoV-2 variant", "XFG", "clade 2.3.4.4b", "H5N1 genotype", "influenza clade", "RSV/mpox/measles/dengue lineage", "CoV-Spectrum", "LAPIS", "Nextclade", "pango-designation", and any request to report what a pathogen population looks like today.

## Example requests

Ask your agent in plain language, for example:

- *"what's the dominant covid variant right now in the US?"*
- *"I'm finalizing the methods section of our manuscript and have a lineage list in lineages.txt (XFG.1.1, PC.2, XFG.20, PQ.17, plus a couple I typed from memory). Can you check they're all still valid before I submit? Also I need to know if PQ.17 is still going up in the last couple of months in the data."*
- *"We have a qPCR assay targeting the HA gene of avian flu H5 in dairy cattle. Before we order more probes, I want to know if the probe site is still conserved in what's being sequenced lately and which clade/genotype is showing up in cattle."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill pathogen-variant-surveillance

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills pathogen-variant-surveillance
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `life-sciences` category with `/plugin install life-sciences@research-agent-skills`.

## Related

- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/pathogen-variant-surveillance/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
