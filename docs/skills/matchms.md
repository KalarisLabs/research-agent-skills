---
title: "matchms — AI agent skill for life sciences"
description: "Process, clean, compare, and search tandem mass spectra with matchms."
keywords: ["mass spectrometry", "MS/MS", "spectral matching", "metabolomics", "cheminformatics"]
---

# `matchms`

**Category:** [life-sciences](/skills#life-sciences) · **License:** Apache-2.0 · **Version:** 2.1 · **Includes scripts**

**Tags:** mass spectrometry, MS/MS, spectral matching, metabolomics, cheminformatics

## When to use it

Process, clean, compare, and search tandem mass spectra with matchms. Use for MS/MS file I/O, metadata harmonization, peak filtering, spectral similarity, library matching, score matrices, and molecular-similarity networks. Use pyopenms instead for LC-MS feature detection or proteomics pipelines.

## Example requests

Ask your agent in plain language, for example:

- *"How do I get the top 5 library hits for each spectrum in my query MGF using matchms?"*
- *"I'm running an old tutorial script on my GNPS export `gnps_library.mgf` and it fails with `ImportError: cannot import name 'ModifiedCosine' from matchms.similarity`. After I swapped that out, `spectrum.add_losses()` also breaks, and so does calling `processor(spectrum)` on my SpectrumProcessor. Can you fix the script so it runs on a current install?"*
- *"I have about 40,000 MS/MS spectra from a plant extract in one file. I want to group the ones that look like they share a similar fragmentation pattern into a network so I can see which compounds are related. Where do I start, and how do I keep the computation from blowing up?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill matchms

# Kalaris Labs installer with checksum verification
npx research-agent-skills install matchms
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `life-sciences` category with `/plugin install life-sciences@research-agent-skills`.

## Related

- [`qdrant-vector-search`](/skills/qdrant-vector-search)
- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/matchms/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
