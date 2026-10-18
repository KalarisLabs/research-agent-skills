---
title: "neuropixels-analysis — AI agent skill for life sciences"
description: "Analyze Neuropixels extracellular recordings end-to-end with SpikeInterface."
keywords: ["Neuropixels", "spike sorting", "electrophysiology", "SpikeInterface", "neuroscience"]
---

# `neuropixels-analysis`

**Category:** [life-sciences](/skills#life-sciences) · **License:** MIT · **Version:** 2.4 · **Includes scripts**

**Tags:** Neuropixels, spike sorting, electrophysiology, SpikeInterface, neuroscience

## When to use it

Analyze Neuropixels extracellular recordings end-to-end with SpikeInterface. Covers loading SpikeGLX/Open Ephys/NWB data, preprocessing, drift/motion correction, Kilosort4 (and CPU) spike sorting, quality metrics, and unit curation (threshold-based, model-based UnitRefine, and AI-assisted visual review). Use when working with Neuropixels 1.0/2.0 recordings, spike sorting, or extracellular electrophysiology analysis.

## Example requests

Ask your agent in plain language, for example:

- *"How do I get my Neuropixels 2.0 data sorted with Kilosort4 through SpikeInterface?"*
- *"I recorded from mouse V1 with a Neuropixels 1.0 probe using SpikeGLX. The folder is session01_g0/ with session01_g0_t0.imec0.ap.bin and the .meta file. I loaded it with si.read_spikeglx but the traces look noisy and the sorted units look split across depth, with the probe drifting a lot over the 90 min recording. What should I do before re-running Kilosort4?"*
- *"I have a sorted dataset with a few hundred units from a high-density silicon probe in mouse cortex. Many look like noise or multi-unit activity. How can I automatically decide which are good single neurons, and look at the borderline ones, without writing every rule myself?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill neuropixels-analysis

# Kalaris Labs installer with checksum verification
npx research-agent-skills install neuropixels-analysis
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `life-sciences` category with `/plugin install life-sciences@research-agent-skills`.

## Related

- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/neuropixels-analysis/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
