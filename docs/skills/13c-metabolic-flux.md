---
title: "13c-metabolic-flux — AI agent skill for life sciences"
description: "Estimates intracellular metabolic fluxes from steady-state carbon-13 isotope-tracing measurements using validated atom maps, mfapy isotope simulation…"
keywords: ["13C-MFA", "metabolic flux analysis", "isotope tracing", "metabolomics", "systems biology"]
---

# `13c-metabolic-flux`

**Category:** [life-sciences](/skills#life-sciences) · **License:** MIT · **Version:** 1.0 · **Includes scripts**

**Tags:** 13C-MFA, metabolic flux analysis, isotope tracing, metabolomics, systems biology

## When to use it

Estimates intracellular metabolic fluxes from steady-state carbon-13 isotope-tracing measurements using validated atom maps, mfapy isotope simulation, constrained multistart fitting, and flux-profile diagnostics. Use for 13C-MFA, carbon tracing, mass isotopomer distributions (MDVs/MIDs), positional isotopomers, parallel tracer experiments, and determining whether labeling data constrain a pathway flux. Distinguishes measured-label inference from COBRA flux balance analysis and flags experiments requiring nonstationary MFA.

## Example requests

Ask your agent in plain language, for example:

- *"Can I get fluxes from my 13C glucose labeling data? I have MIDs for a few amino acids."*
- *"I'm working in E. coli on [1,2-13C]glucose and [U-13C]glucose parallel cultures, with corrected MDVs for alanine, serine and glutamate in dataset.json and model.json. Please run the contract check, then fit PPP vs glycolysis split with multistart and give me profile intervals. The fit residual is small but I want to know if the oxidative PPP flux is actually pinned down."*
- *"We fed cells labeled substrate and measured how labeling in TCA intermediates changes over 0, 30, 60, 120 seconds. Can we average the timepoints and estimate pathway rates with your flux tool?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill 13c-metabolic-flux

# Kalaris Labs installer with checksum verification
npx research-agent-skills install 13c-metabolic-flux
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `life-sciences` category with `/plugin install life-sciences@research-agent-skills`.

## Related

- [`cobrapy`](/skills/cobrapy)
- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/13c-metabolic-flux/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
