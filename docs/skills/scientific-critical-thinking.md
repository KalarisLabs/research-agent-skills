---
title: "scientific-critical-thinking — AI agent skill for research writing"
description: "Evaluate scientific claims and evidence quality."
keywords: ["critical thinking", "evidence quality", "bias", "GRADE", "research methods"]
---

# `scientific-critical-thinking`

**Category:** [research-writing](/skills#research-writing) · **License:** MIT · **Version:** 1.3

**Tags:** critical thinking, evidence quality, bias, GRADE, research methods

## When to use it

Evaluate scientific claims and evidence quality. Use for assessing experimental design validity, identifying biases and confounders, applying evidence grading frameworks (GRADE, Cochrane Risk of Bias), or teaching critical analysis. Best for understanding evidence quality, identifying flaws. For formal peer review writing use peer-review.

## Example requests

Ask your agent in plain language, for example:

- *"Is this a good study? 40 mice, treated group housed in one cage, control in another, outcome scored by the same grad student who ran the injections. Authors claim the drug 'cures' anxiety."*
- *"I've attached smith2023_vitD_RCT.pdf, a meta-analysis of 14 vitamin D trials for respiratory infection prevention. Can you rate the certainty of evidence for the primary outcome using GRADE and tell me where each trial sits on Cochrane risk of bias? Several trials used per-protocol analysis and I2 is 68%."*
- *"I'm teaching a journal club for first-year PhD students. I want them to learn to tell what a paper actually showed from what the authors say it means. How should I structure a session around a recent nutrition cohort study that claims a food 'prevents' cancer?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill scientific-critical-thinking

# Kalaris Labs installer with checksum verification
npx research-agent-skills install scientific-critical-thinking
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `research-writing` category with `/plugin install research-writing@research-agent-skills`.

## Related

- [`bgpt-paper-search`](/skills/bgpt-paper-search)
- [`rebuttal-and-response-to-reviewers`](/skills/rebuttal-and-response-to-reviewers)
- [`citation-verification`](/skills/citation-verification)
- [`peer-review`](/skills/peer-review)
- [`systematic-review-prisma`](/skills/systematic-review-prisma)
- [`unslop-academic-writing`](/skills/unslop-academic-writing)
- [Write a research paper with AI](/guides/write-a-research-paper)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/scientific-critical-thinking/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
