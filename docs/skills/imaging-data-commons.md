---
title: "imaging-data-commons — AI agent skill for scientific databases"
description: "Query and download public cancer imaging data from NCI Imaging Data Commons."
keywords: ["cancer imaging", "DICOM", "radiology", "pathology", "public datasets", "medical imaging"]
---

# `imaging-data-commons`

**Category:** [scientific-databases](/skills#scientific-databases) · **License:** This skill is provided under the MIT License. IDC data itself has individual licensing (mostly CC-BY, some CC-NC) that must be respected when using the data. · **Version:** 1.5 · **Includes scripts**

**Tags:** cancer imaging, DICOM, radiology, pathology, public datasets, medical imaging

## When to use it

Query and download public cancer imaging data from NCI Imaging Data Commons. Invoke for any question about IDC collections, cancer imaging datasets, DICOM data access, radiology (CT, MR, PET) or pathology AI training sets, metadata queries, visualization, or license checks — even when the user doesn't explicitly mention "IDC". No authentication required.

## Example requests

Ask your agent in plain language, for example:

- *"what TCIA-style lung CT collections are available in IDC with segmentations?"*
- *"I'm building a nodule detection model and need to pull all chest CT series from the nlst collection into ./data/nlst for training. Only keep series with slice thickness &lt;= 2.5 mm. I'd also like a total size estimate before I start, and I'm worried about disk space on my 500 GB drive. How should I do this?"*
- *"My lab wants to train a pathology foundation model on whole-slide images of breast and colon tumors from open sources, and we may eventually use it in a commercial product. Where can we get suitable public slide data and what should we check first?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill imaging-data-commons

# Kalaris Labs installer with checksum verification
npx research-agent-skills install imaging-data-commons
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `scientific-databases` category with `/plugin install scientific-databases@research-agent-skills`.

## Related

- [`depmap`](/skills/depmap)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/imaging-data-commons/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
