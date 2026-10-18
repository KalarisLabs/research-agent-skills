---
title: "scientific-writing — AI agent skill for research writing"
description: "Draft, revise, and audit scientific manuscripts or reports with explicit evidence provenance, reporting-guideline coverage, authorship accountability…"
keywords: ["scientific writing", "manuscripts", "academic writing", "research papers", "reporting guidelines"]
---

# `scientific-writing`

**Category:** [research-writing](/skills#research-writing) · **License:** MIT · **Version:** 2.1 · **Includes scripts**

**Tags:** scientific writing, manuscripts, academic writing, research papers, reporting guidelines

## When to use it

Draft, revise, and audit scientific manuscripts or reports with explicit evidence provenance, reporting-guideline coverage, authorship accountability, confidentiality controls, and local consistency checks. Use for manuscript sections, references, declarations, tables, figures, or submission preparation when scientific accuracy and traceability matter.

## Example requests

Ask your agent in plain language, for example:

- *"Help me write the Methods section for my RCT manuscript without making stuff up. I'll give you the protocol."*
- *"I have draft.md, claims.csv and source_manifest.json for my cohort study on statin use and dementia (target journal: JAMA Network Open). The abstract says n=4,212 but the results table says 4,128. Can you check consistency, run the local lint, and get the references and declarations ready for submission?"*
- *"My manuscript on a new soil microbiome sequencing method is almost done. I want to make sure every number and citation in it can be traced back to a real source, the funding and conflict statements are accurate, and that I'm not leaking anything confidential when I use an AI tool. What's the process?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill scientific-writing

# Kalaris Labs installer with checksum verification
npx research-agent-skills install scientific-writing
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `research-writing` category with `/plugin install research-writing@research-agent-skills`.

## Related

- [`abstract-and-title`](/skills/abstract-and-title)
- [`apa7`](/skills/apa7)
- [`autoskill`](/skills/autoskill)
- [`bulk-rnaseq`](/skills/bulk-rnaseq)
- [`clinical-reports`](/skills/clinical-reports)
- [`markdown-mermaid-writing`](/skills/markdown-mermaid-writing)
- [`pathway-enrichment`](/skills/pathway-enrichment)
- [`peer-review`](/skills/peer-review)
- [Write a research paper with AI](/guides/write-a-research-paper)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/scientific-writing/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
