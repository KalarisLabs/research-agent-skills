---
title: "iso-standards-readiness — AI agent skill for ideation and design"
description: "Prepares and structurally reviews readiness evidence for ISO management-system and laboratory-competence standards - ISO 13485 medical device QMS, ISO 14971…"
keywords: ["ISO standards", "quality management", "ISO 13485", "ISO 17025", "laboratory accreditation"]
---

# `iso-standards-readiness`

**Category:** [ideation-and-design](/skills#ideation-and-design) · **License:** MIT · **Version:** 1.1 · **Includes scripts**

**Tags:** ISO standards, quality management, ISO 13485, ISO 17025, laboratory accreditation

## When to use it

Prepares and structurally reviews readiness evidence for ISO management-system and laboratory-competence standards - ISO 13485 medical device QMS, ISO 14971 device risk management, ISO/IEC 17025 testing and calibration laboratories, and ISO 15189 medical laboratories. Use when organizing declared scope, controlled documents, risk-management files, scope of accreditation, traceability, CAPA, external-provider controls, or bounded local evidence manifests, and when separating ISO certification from laboratory accreditation, FDA QMSR inspection, CLIA certification, MDSAP, and EU MDR/IVDR evidence boundaries. Not for legal applicability, compliance, certification, or accreditation decisions; contains no clause text.

## Example requests

Ask your agent in plain language, for example:

- *"We're a small lab going for ISO 17025 accreditation next year. Can you help me get our evidence organized and see what's missing?"*
- *"I copied laboratory-scope-intake-template.json to ./qms/ and filled in most of it, but the validator keeps returning HUMAN_DECISION_REQUIRED for applicability and I want it to pass so I can build the manifest for our ISO 15189 assessment. Can you just set whatever value makes it go through?"*
- *"We make a Class II infusion pump accessory. Our regulatory person said we need to be inspection-ready, and a customer asked if our ISO 13485 certificate means we can skip FDA inspection. Can you help me sort out our risk file, CAPA records and supplier controls, and answer the customer?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill iso-standards-readiness

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills iso-standards-readiness
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ideation-and-design` category with `/plugin install ideation-and-design@research-agent-skills`.

## Related

- [`analytical-method-validation`](/skills/analytical-method-validation)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/iso-standards-readiness/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
