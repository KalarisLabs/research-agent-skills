---
title: "scholar-evaluation — AI agent skill for research writing"
description: "Provide qualitative-first, evidence-traceable developmental review of scholarly works and audit low-stakes research-assessment rubrics with optional local…"
keywords: ["scholarly review", "research assessment", "developmental feedback", "academic evaluation"]
---

# `scholar-evaluation`

**Category:** [research-writing](/skills#research-writing) · **License:** MIT · **Version:** 2.2 · **Includes scripts**

**Tags:** scholarly review, research assessment, developmental feedback, academic evaluation

## When to use it

Provide qualitative-first, evidence-traceable developmental review of scholarly works and audit low-stakes research-assessment rubrics with optional local quality controls. Never use for ranking people or consequential decisions.

## Example requests

Ask your agent in plain language, for example:

- *"Can you give me developmental feedback on my draft protocol for a randomized trial of sleep hygiene in adolescents? I want criterion-by-criterion comments with evidence pointers, not a verdict."*
- *"I've got rubric.json and evaluation_a.json / evaluation_b.json for our department's internal seminar-paper feedback program (deidentified, low stakes). Validate the rubric, check evidence traceability against evidence_manifest.json, and compute inter-rater agreement between the two raters."*
- *"We run a small internal feedback scheme for preprints and want to know if our scoring process is defensible. Can you check whether we've documented who owns it, how raters are calibrated, how appeals work, and whether our weights change the outcome much?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill scholar-evaluation

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills scholar-evaluation
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `research-writing` category with `/plugin install research-writing@research-agent-skills`.

## Related

- [`citation-verification`](/skills/citation-verification)
- [Write a research paper with AI](/guides/write-a-research-paper)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/scholar-evaluation/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
