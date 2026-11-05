---
title: "pyopenms — AI agent skill for life sciences"
description: "Complete mass spectrometry analysis platform."
keywords: ["mass spectrometry", "proteomics", "metabolomics", "LC-MS", "bioinformatics"]
---

# `pyopenms`

**Category:** [life-sciences](/skills#life-sciences) · **License:** 3 clause BSD license · **Version:** 2.1 · **Includes scripts**

**Tags:** mass spectrometry, proteomics, metabolomics, LC-MS, bioinformatics

## When to use it

Complete mass spectrometry analysis platform. Use for proteomics and metabolomics workflows—feature detection, peptide/protein identification, label-free and isobaric quantification, adduct/accurate-mass annotation, and complex LC-MS/MS pipelines. Supports extensive file formats and algorithms. For simple spectral comparison and small-molecule library matching use matchms.

## Example requests

Ask your agent in plain language, for example:

- *"How do I run untargeted feature detection on a DDA mzML file in Python?"*
- *"I have 12 plasma metabolomics runs (QC_01.mzML ... S10.mzML) from a Q Exactive in positive mode. I need a samples-by-features intensity table across all runs. My old script calling FeatureFinder('centroided') now crashes after I upgraded to pyopenms 3.5. Can you fix this and also group adducts like [M+Na]+ with [M+H]+ before annotating against HMDB?"*
- *"I ran a database search on my tryptic HeLa digest and got an idXML file. I want to rescore it, keep only peptide hits at 1% FDR, and make sure each spectrum only keeps its best hit. I also have the FASTA I searched against."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill pyopenms

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills pyopenms
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `life-sciences` category with `/plugin install life-sciences@research-agent-skills`.

## Related

- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/pyopenms/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
