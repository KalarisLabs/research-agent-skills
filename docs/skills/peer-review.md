---
title: "peer-review — AI agent skill for research writing"
description: "Prepare evidence-bounded, constructive peer-review drafts and structured manuscript assessments."
keywords: ["peer review", "manuscript review", "reporting guidelines", "academic publishing"]
---

# `peer-review`

**Category:** [research-writing](/skills#research-writing) · **License:** MIT · **Version:** 2.2 · **Includes scripts**

**Tags:** peer review, manuscript review, reporting guidelines, academic publishing

## When to use it

Prepare evidence-bounded, constructive peer-review drafts and structured manuscript assessments. Use for authorized review of scientific manuscripts, protocols, preprints, or research proposals; reporting-guideline selection; claim–evidence checks; methods, statistics, reproducibility, ethics, figure/table, and citation critique; or revision-response planning.

## Example requests

Ask your agent in plain language, for example:

- *"I've been invited to review a Nature Communications manuscript on single-cell atlas integration. Can you help me draft my referee report?"*
- *"I'm a reviewer for BMJ Open and have the editor's invitation. The paper is a stratified cluster RCT of a school-based vaccination reminder (manuscript_v1.docx and supplement S1.pdf are saved locally). The abstract says the intervention 'reduced HPV vaccine hesitancy by 30%', but the primary outcome in the registry entry looks like uptake. Help me work out which reporting guideline applies and whether the claims match the evidence. I don't want anything uploaded anywhere."*
- *"Our grant resubmission got three reviewer reports back and I have to write the rebuttal. Reviewer 2 says our mixed-effects model ignores clustering by site and wants a sensitivity analysis. Help me plan how to respond to each comment point by point."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill peer-review

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills peer-review
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `research-writing` category with `/plugin install research-writing@research-agent-skills`.

## Related

- [`cell-press`](/skills/cell-press)
- [`citation-verification`](/skills/citation-verification)
- [`reproducibility-statement`](/skills/reproducibility-statement)
- [`scientific-writing`](/skills/scientific-writing)
- [`rebuttal-and-response-to-reviewers`](/skills/rebuttal-and-response-to-reviewers)
- [`scientific-brainstorming`](/skills/scientific-brainstorming)
- [`scientific-critical-thinking`](/skills/scientific-critical-thinking)
- [`systematic-review-prisma`](/skills/systematic-review-prisma)
- [Write a research paper with AI](/guides/write-a-research-paper)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/peer-review/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
