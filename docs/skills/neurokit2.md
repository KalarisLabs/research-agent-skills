---
title: "neurokit2 — AI agent skill for life sciences"
description: "Use NeuroKit2 to build or audit reproducible research workflows for physiological time-series preprocessing, event/interval analysis, multimodal alignment…"
keywords: ["physiological signals", "ECG", "EEG", "HRV", "biosignal processing", "neuroscience"]
---

# `neurokit2`

**Category:** [life-sciences](/skills#life-sciences) · **License:** MIT · **Version:** 1.2 · **Includes scripts**

**Tags:** physiological signals, ECG, EEG, HRV, biosignal processing, neuroscience

## When to use it

Use NeuroKit2 to build or audit reproducible research workflows for physiological time-series preprocessing, event/interval analysis, multimodal alignment, variability, and complexity. Trigger when code imports neurokit2 or needs its current APIs, schemas, and method-aware validation—not for diagnosis or device validation.

## Example requests

Ask your agent in plain language, for example:

- *"My EDA export has 'EDA' column and I want to split tonic and phasic and count SCRs. Which settings should I use?"*
- *"I'm getting NaNs in my epochs from epochs_create on events from events_find, using events from my stim channel in subject03_ecg.csv recorded at 1000 Hz. I set epochs_start=-0.5, epochs_end=2 and baseline_correction=True. I also passed event onsets I'd computed in milliseconds. Why, and how do I fix it?"*
- *"I have a 10-minute recording of ECG and a chest respiration belt from a stress task, and I want a heart rate variability and respiratory sinus arrhythmia analysis I can put in a paper. How should I set it up so it's defensible?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill neurokit2

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills neurokit2
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `life-sciences` category with `/plugin install life-sciences@research-agent-skills`.

## Related

- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/neurokit2/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
