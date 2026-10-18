---
title: "clinical-decision-support — AI agent skill for clinical and health"
description: "Prepare and validate research-only clinical decision-support evaluation, evidence-profile, cohort, survival, biomarker/model, privacy, and governance…"
keywords: ["clinical research", "decision support", "evidence profiles", "survival analysis", "medicine"]
---

# `clinical-decision-support`

**Category:** [clinical-and-health](/skills#clinical-and-health) · **License:** MIT · **Version:** 2.2 · **Includes scripts**

**Tags:** clinical research, decision support, evidence profiles, survival analysis, medicine

## When to use it

Prepare and validate research-only clinical decision-support evaluation, evidence-profile, cohort, survival, biomarker/model, privacy, and governance artifacts. Use for aggregate or synthetic research documentation and traceability—not patient care or live clinical operation.

## Example requests

Ask your agent in plain language, for example:

- *"Can you check my survival analysis plan JSON before we submit the protocol?"*
- *"I have aggregate confusion counts and 10 calibration bins for our locked sepsis-biomarker v2.3 assay, split by sex and age band, in model_eval.json. I need descriptive sensitivity/specificity with confidence intervals and subgroup gaps for the TRIPOD+AI supplement. Small cells need suppressing. Can you run that?"*
- *"We're putting together a GRADE summary for a guideline-adjacent evidence review on anticoagulant outcomes. I want a structured table where each outcome's judgments are tied to our included studies, and I want to confirm every citation link resolves. Can you set it up so my panel can fill it in?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill clinical-decision-support

# Kalaris Labs installer with checksum verification
npx research-agent-skills install clinical-decision-support
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `clinical-and-health` category with `/plugin install clinical-and-health@research-agent-skills`.

## Related

- [`clinical-reports`](/skills/clinical-reports)
- [`treatment-plans`](/skills/treatment-plans)
- [`pathml`](/skills/pathml)
- [Skills for medicine and clinical research](/fields/medicine)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/clinical-decision-support/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
