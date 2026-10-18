---
title: "pydicom — AI agent skill for clinical and health"
description: "Reads, inspects, writes, and transforms local DICOM files with pydicom 3.x (dcmread, dcmwrite, pydicom.pixels), including metadata, transfer syntaxes…"
keywords: ["DICOM", "medical imaging", "radiology", "de-identification", "Python"]
---

# `pydicom`

**Category:** [clinical-and-health](/skills#clinical-and-health) · **License:** MIT · **Version:** 1.2 · **Includes scripts**

**Tags:** DICOM, medical imaging, radiology, de-identification, Python

## When to use it

Reads, inspects, writes, and transforms local DICOM files with pydicom 3.x (dcmread, dcmwrite, pydicom.pixels), including metadata, transfer syntaxes, compressed pixel data plugins, frame decoding, private elements, DICOM JSON, and bounded pseudonymization review using bundled helper scripts. Use when extracting aggregate metadata from DICOM datasets without printing PHI, checking which transfer syntaxes and codec plugins a deployment needs, planning frame or memory limits before decoding pixel data, rendering one non-diagnostic frame, compressing or decompressing pixel data, or building and auditing a pseudonymized derivative. Not for diagnostic viewing, or for claiming DICOM PS3.15, HIPAA, or GDPR compliance.

## Example requests

Ask your agent in plain language, for example:

- *"Can you give me a quick summary of the modalities and transfer syntaxes across the DICOM files in ./scans without dumping any patient info?"*
- *"I have a 4D cardiac cine MR series in ./cine/ (about 400 multi-frame files, JPEG 2000 Lossless compressed). Running ds.pixel_array on one file killed my kernel with a MemoryError, and some files raise 'missing required dependencies' for the pixel handler. Help me work out which codec plugins I need to install and how many frames I can safely decode at a time, then pull out frame 12 of one file as a PNG to eyeball."*
- *"I need to share a set of CT studies with an external collaborator for a methods project. Patient names, IDs and dates have to be replaced, but I still want the series and studies to stay linked to each other. How should I go about producing that copy?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill pydicom

# Kalaris Labs installer with checksum verification
npx research-agent-skills install pydicom
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `clinical-and-health` category with `/plugin install clinical-and-health@research-agent-skills`.

## Related

- [Skills for medicine and clinical research](/fields/medicine)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/pydicom/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
