---
title: "pyhealth — AI agent skill for clinical and health"
description: "Builds clinical deep-learning pipelines with PyHealth using its Dataset → Task → Model → Trainer → Metrics pattern."
keywords: ["clinical machine learning", "EHR", "MIMIC", "healthcare AI", "deep learning"]
---

# `pyhealth`

**Category:** [clinical-and-health](/skills#clinical-and-health) · **License:** MIT · **Version:** 1.1

**Tags:** clinical machine learning, EHR, MIMIC, healthcare AI, deep learning

## When to use it

Builds clinical deep-learning pipelines with PyHealth using its Dataset → Task → Model → Trainer → Metrics pattern. Covers loading MIMIC-III/IV, eICU, OMOP, SleepEDF, ChestXray14 and EHRShot data, defining prediction tasks (mortality, readmission, length of stay, drug recommendation, sleep staging, ICD coding, EEG events), models such as Transformer, RETAIN, GAMENet, SafeDrug and StageNet, training with Trainer, and ICD/ATC/NDC/RxNorm code lookup and cross-mapping. Use when building a clinical prediction model on EHR data. Use when working with MIMIC or eICU datasets. Use when recommending drugs or staging sleep from signals. Use when mapping medical codes between ICD, ATC, NDC or RxNorm. Not for generic PyTorch on tabular data.

## Example requests

Ask your agent in plain language, for example:

- *"I have MIMIC-IV downloaded locally. How do I train a model to predict in-hospital mortality and evaluate it properly?"*
- *"My script crashes at `MortalityPredictionMIMIC3(...)` when I run it on `MIMIC4Dataset(root='/data/mimiciv/2.2', tables=['diagnoses_icd','procedures_icd'])`. Then I pass the dataset directly to `Transformer(dataset=base, feature_keys=['conditions','procedures'], label_key='label', mode='binary')` and get an error. Parsing also takes 40 minutes every time I rerun it. What's wrong?"*
- *"I've got nightly polysomnography recordings from a sleep clinic as EDF files with technician-scored hypnograms. I want a neural network that labels each 30-second epoch as wake, REM or N1-N3, and I'd like to avoid hand-writing the training loop. What's a good approach?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill pyhealth

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills pyhealth
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `clinical-and-health` category with `/plugin install clinical-and-health@research-agent-skills`.

## Related

- [Skills for medicine and clinical research](/fields/medicine)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/pyhealth/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
