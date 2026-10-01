---
title: "pydicom — AI agent skill for clinical and health"
description: "Reads, inspects, writes, and transforms local DICOM files with pydicom 3.x (dcmread, dcmwrite, pydicom.pixels), including metadata, transfer syntaxes, com…"
---

# `pydicom`

> Reads, inspects, writes, and transforms local DICOM files with pydicom 3.x (dcmread, dcmwrite, pydicom.pixels), including metadata, transfer syntaxes, compressed pixel data plugins, frame decoding, private elements, DICOM JSON, and bounded pseudonymization review using bundled helper scripts. Use when extracting aggregate metadata from DICOM datasets without printing PHI, checking which transfer syntaxes and codec plugins a deployment needs, planning frame or memory limits before decoding pixel data, rendering one non-diagnostic frame, compressing or decompressing pixel data, or building and auditing a pseudonymized derivative. Not for diagnostic viewing, or for claiming DICOM PS3.15, HIPAA, or GDPR compliance.

**Category:** [clinical-and-health](/skills#clinical-and-health) · **License:** MIT · **Version:** 1.2

## Install

```bash
npx skills add KalarisLabs/research-agent-skills --skill pydicom
```

## When to use it

Reads, inspects, writes, and transforms local DICOM files with pydicom 3.x (dcmread, dcmwrite, pydicom.pixels), including metadata, transfer syntaxes, compressed pixel data plugins, frame decoding, private elements, DICOM JSON, and bounded pseudonymization review using bundled helper scripts. Use when extracting aggregate metadata from DICOM datasets without printing PHI, checking which transfer syntaxes and codec plugins a deployment needs, planning frame or memory limits before decoding pixel data, rendering one non-diagnostic frame, compressing or decompressing pixel data, or building and auditing a pseudonymized derivative. Not for diagnostic viewing, or for claiming DICOM PS3.15, HIPAA, or GDPR compliance.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/pydicom/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
