---
title: "bids — AI agent skill for life sciences"
description: "Organizes, queries, validates, and converts neuroscience and biomedical datasets using the Brain Imaging Data Structure (BIDS) standard, covering MRI, PET…"
keywords: ["neuroimaging", "BIDS", "MRI", "EEG", "data standards", "neuroscience"]
---

# `bids`

**Category:** [life-sciences](/skills#life-sciences) · **License:** https://creativecommons.org/licenses/by/4.0/ · **Version:** 1.1 · **Includes scripts**

**Tags:** neuroimaging, BIDS, MRI, EEG, data standards, neuroscience

## When to use it

Organizes, queries, validates, and converts neuroscience and biomedical datasets using the Brain Imaging Data Structure (BIDS) standard, covering MRI, PET, EEG, MEG, iEEG, EMG, NIRS, microscopy, motion capture, and behavioral data. Covers PyBIDS (BIDSLayout), the bids-validator, HeuDiConv, dcm2bids, BIDScoin, JSON sidecars, dataset_description.json, events.tsv, participants.tsv, .bidsignore, and derivatives. Use when arranging raw data into BIDS directories and filenames. Use when converting DICOM scans to BIDS. Use when validating a dataset before OpenNeuro or DANDI submission. Use when querying files or sidecar metadata with PyBIDS. Use when writing BIDS derivatives. For extracellular Neuropixels analysis, use neuropixels-analysis instead.

## Example requests

Ask your agent in plain language, for example:

- *"How do I get all the T1w files for sub-03 out of my BIDS folder in Python?"*
- *"I have DICOMs from a Siemens Prisma in sourcedata/dicom/sub-101/ses-1 with a T1 MPRAGE, two resting-state BOLD runs and an AP/PA spin-echo fieldmap pair. I ran dcm2bids_helper and now need a config so the output lands as sub-101_ses-1_task-rest_run-01_bold.nii.gz and so on, with the fieldmaps getting IntendedFor. The conversion keeps failing with 'No matching description' for the fieldmaps. What should I do?"*
- *"I'm about to put my EEG study with 40 participants on OpenNeuro. Its folders and files are named in my own lab convention and I have no idea what metadata I need. What do I need to do first so it's accepted?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill bids

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills bids
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `life-sciences` category with `/plugin install life-sciences@research-agent-skills`.

## Related

- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/bids/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
