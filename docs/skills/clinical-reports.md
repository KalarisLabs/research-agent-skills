---
title: "clinical-reports — AI agent skill for clinical and health"
description: "Generates fail-closed draft JSON templates and runs local deterministic structure and consistency checks for clinical reports: CARE case reports, radiology…"
keywords: ["clinical reports", "CONSORT", "case reports", "clinical trials", "medical writing"]
---

# `clinical-reports`

**Category:** [clinical-and-health](/skills#clinical-and-health) · **License:** MIT · **Version:** 2.1 · **Includes scripts**

**Tags:** clinical reports, CONSORT, case reports, clinical trials, medical writing

## When to use it

Generates fail-closed draft JSON templates and runs local deterministic structure and consistency checks for clinical reports: CARE case reports, radiology, pathology and lab scaffolds, CONSORT 2025, SPIRIT 2025, ICH E3 CSRs, aggregate adverse-event tables, provenance manifests, terminology schemas, and de-identification process checklists. Use when drafting a case report for publication from a verified source-fact manifest. Use when checking a trial results manuscript, protocol, or CSR draft against its reporting structure. Use when building an aggregate safety table from synthetic or de-identified data. Use when routing an artifact to the right guideline. Not for diagnosis, treatment advice, individual case safety report creation, or filing and submission.

## Example requests

Ask your agent in plain language, for example:

- *"Can you check my CONSORT 2025 draft for missing items? It's in results_manuscript.md."*
- *"I have a de-identified case manifest, case_facts.json, with fact IDs and SHA-256 hashes for a rare cutaneous reaction we want to publish. Please generate a draft case report JSON from it and run the structure check. The patient gave publication consent, and the journal wants CARE."*
- *"We have a synthetic dataset of treatment-emergent events by arm for our phase 3 study and need a safety summary table for the CSR appendix. How do we build it so the denominators and counts are traceable?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill clinical-reports

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills clinical-reports
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `clinical-and-health` category with `/plugin install clinical-and-health@research-agent-skills`.

## Related

- [`clinical-decision-support`](/skills/clinical-decision-support)
- [`scientific-writing`](/skills/scientific-writing)
- [Skills for medicine and clinical research](/fields/medicine)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/clinical-reports/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
