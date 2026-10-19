---
title: "pkpd-modeling — AI agent skill for chemistry and drug discovery"
description: "Pharmacokinetic and pharmacodynamic modelling and simulation - non-compartmental analysis, compartmental and population PK, PK/PD and exposure-response, TMDD…"
keywords: ["pharmacokinetics", "pharmacodynamics", "PK/PD", "drug development", "pharmacology"]
---

# `pkpd-modeling`

**Category:** [chemistry-and-drug-discovery](/skills#chemistry-and-drug-discovery) · **License:** MIT · **Version:** 1.2 · **Includes scripts**

**Tags:** pharmacokinetics, pharmacodynamics, PK/PD, drug development, pharmacology

## When to use it

Pharmacokinetic and pharmacodynamic modelling and simulation - non-compartmental analysis, compartmental and population PK, PK/PD and exposure-response, TMDD, PBPK orientation, bioequivalence, allometric scaling and first-in-human dose, drug interaction prediction, and Bayesian therapeutic drug monitoring. Use when analysing concentration-time data, deriving exposure metrics, fitting PK or PD models, or evaluating dosing regimens. Triggers include "pharmacokinetics", "pharmacodynamics", "PK/PD", "NCA", "non-compartmental", "AUC", "Cmax", "lambda z", "half-life", "clearance", "volume of distribution", "compartmental model", "population PK", "popPK", "NONMEM", "nlmixr2", "Pharmpy", "Monolix", "exposure-response", "Emax", "EC50", "indirect response", "effect compartment", "TMDD", "PBPK", "bioequivalence", "RSABE", "ABEL", "allometric scaling", "first-in-human", "MABEL", "drug-drug interaction", "DDI", "ICH M12", "concentration-QTc", "therapeutic drug monitoring", "MIPD", and "dosing regimen".

## Example requests

Ask your agent in plain language, for example:

- *"How do I get the half-life and AUC from my plasma concentration data after an oral dose?"*
- *"I've got a NONMEM-style CSV, study101_pk.csv, with columns ID, TIME, AMT, ADDL, II, DV, EVID, WT. Some DV cells say 'BLQ' and a few WT cells are blank. Before I run my two-compartment model, what should I check, and will NONMEM choke on this?"*
- *"We're planning a twice-daily regimen for a new antibiotic with high between-patient variability in clearance. I want to know what share of patients would keep their trough above the target concentration, not just what the average patient does."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill pkpd-modeling

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills pkpd-modeling
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `chemistry-and-drug-discovery` category with `/plugin install chemistry-and-drug-discovery@research-agent-skills`.

## Related

- [Skills for chemistry and drug discovery](/fields/chemistry)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/pkpd-modeling/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
