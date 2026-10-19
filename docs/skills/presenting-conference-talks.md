---
title: "presenting-conference-talks — AI agent skill for visualization and presentation"
description: "Generates conference presentation slides (Beamer LaTeX PDF and editable PPTX) from a compiled paper with speaker notes and talk script."
keywords: ["Presenting Conference Talks", "Beamer", "PPTX", "Slides", "Speaker Notes", "OSDI", "SOSP", "ASPLOS", "NeurIPS", "ICML"]
---

# `presenting-conference-talks`

**Category:** [visualization-and-presentation](/skills#visualization-and-presentation) · **License:** MIT · **Version:** 1.0.0

**Tags:** Presenting Conference Talks, Beamer, PPTX, Slides, Speaker Notes, OSDI, SOSP, ASPLOS, NeurIPS, ICML

## When to use it

Generates conference presentation slides (Beamer LaTeX PDF and editable PPTX) from a compiled paper with speaker notes and talk script. Use when preparing oral talks, spotlight presentations, or invited talks for ML and systems conferences.

## Example requests

Ask your agent in plain language, for example:

- *"Make me a spotlight talk from my paper. I have 6 minutes at ICML."*
- *"My OSDI paper is compiled at build/paper.pdf with figures in figures/. I need a 20-minute oral talk with a live demo of our storage system, plus a script I can rehearse. Can you build the Beamer slides and a PPTX copy?"*
- *"I got accepted for a talk at NSDI next month and I only have the camera-ready PDF. I'd like something I can present from and also tweak on the plane, with notes for each slide so I don't ramble past my time slot."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill presenting-conference-talks

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills presenting-conference-talks
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `visualization-and-presentation` category with `/plugin install visualization-and-presentation@research-agent-skills`.

## Related

- [`latex-posters`](/skills/latex-posters)
- [`pptx-posters`](/skills/pptx-posters)
- [`scientific-slides`](/skills/scientific-slides)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/presenting-conference-talks/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
