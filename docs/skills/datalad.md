---
title: "datalad — AI agent skill for data science and ml"
description: "Retrieve, version, and publish scientific datasets with DataLad and git-annex, and capture computational provenance with datalad run, rerun, and…"
keywords: ["research data management", "data versioning", "provenance", "reproducibility", "open science"]
---

# `datalad`

**Category:** [data-science-and-ml](/skills#data-science-and-ml) · **License:** MIT · **Version:** 1.0

**Tags:** research data management, data versioning, provenance, reproducibility, open science

## When to use it

Retrieve, version, and publish scientific datasets with DataLad and git-annex, and capture computational provenance with datalad run, rerun, and containers-run. Use when cloning or fetching data from OpenNeuro, DANDI, datasets.datalad.org, or any DataLad dataset; when a file in a dataset reads as a broken symlink or a small pointer instead of real data; when an analysis needs a machine-readable record of how each output was produced so it can be re-executed; or when publishing a dataset to siblings such as a GitHub repository plus a storage remote. Also use to decide between DataLad and plain Git for a data-carrying repository.

## Example requests

Ask your agent in plain language, for example:

- *"I cloned an OpenNeuro dataset and my script says one of the NIfTI files is 'not a gzip file', but ls shows the file is there. What's going on?"*
- *"I'm writing up a methods section for a paper. My repo has raw/sub-01_bold.nii.gz (about 2 GB per subject) and a script code/smooth.py that writes derivatives/sub-01_smoothed.nii.gz. I want anyone to be able to re-execute that step later and see exactly which inputs and command produced the output. Second runs of my script currently fail with 'Permission denied' on the output file. How should I set this up?"*
- *"I've got a 400 GB imaging dataset I want to share with collaborators. The code goes on GitHub, but the data should sit in an S3 bucket. I want people to be able to clone from GitHub and then pull the actual files without anything breaking. How do I publish it?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill datalad

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills datalad
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `data-science-and-ml` category with `/plugin install data-science-and-ml@research-agent-skills`.

## Related

- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/datalad/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
