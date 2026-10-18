---
title: "treatment-plans — AI agent skill for clinical and health"
description: "Format and structurally validate local treatment-plan documentation after clinical decisions have already been supplied and verified by authorized licensed…"
keywords: ["treatment plans", "clinical documentation", "medicine", "healthcare"]
---

# `treatment-plans`

**Category:** [clinical-and-health](/skills#clinical-and-health) · **License:** MIT · **Version:** 2.2 · **Includes scripts**

**Tags:** treatment plans, clinical documentation, medicine, healthcare

## When to use it

Format and structurally validate local treatment-plan documentation after clinical decisions have already been supplied and verified by authorized licensed professionals. Use for source traceability, clinician-authored intervention records, goals and checkpoints, shared-decision records, reconciliation handoffs, and release gates—not for clinical decision-making.

## Example requests

Ask your agent in plain language, for example:

- *"I have a synthetic treatment-plan package from our QA team. Can you run the structural validator on it and tell me what's blocking release?"*
- *"I'm building a de-identified research handoff for our oncology pathway study. I have ./pkg/transition_reconciliation.json and ./pkg/goals_checkpoints.json. The validator is complaining about 'unknown field' and 'duplicate key' errors, and the checkpoint dates aren't being scheduled. Can you help me fix the files so the derived schedule comes out right?"*
- *"Our clinic wants a consistent, traceable record of what the clinicians already decided for each patient's plan: who authored each intervention, who verified it, the source version, the shared-decision discussion and who takes over at discharge. How should I structure that as local files?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill treatment-plans

# Kalaris Labs installer with checksum verification
npx research-agent-skills install treatment-plans
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `clinical-and-health` category with `/plugin install clinical-and-health@research-agent-skills`.

## Related

- [`ara-research-manager`](/skills/ara-research-manager)
- [`clinical-decision-support`](/skills/clinical-decision-support)
- [Skills for medicine and clinical research](/fields/medicine)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/treatment-plans/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
