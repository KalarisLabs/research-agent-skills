---
title: "pptx-posters — AI agent skill for visualization and presentation"
description: "Create and audit editable scientific posters in macro-free PowerPoint (.pptx) from author-approved local content and assets."
keywords: ["research posters", "PowerPoint", "conference posters", "academic presentations"]
---

# `pptx-posters`

**Category:** [visualization-and-presentation](/skills#visualization-and-presentation) · **License:** MIT · **Version:** 2.2 · **Includes scripts**

**Tags:** research posters, PowerPoint, conference posters, academic presentations

## When to use it

Create and audit editable scientific posters in macro-free PowerPoint (.pptx) from author-approved local content and assets. Use when the requested deliverable is a PowerPoint research/conference poster and exact physical, printer, accessibility, provenance, and package-security checks are required.

## Example requests

Ask your agent in plain language, for example:

- *"I need an editable .pptx conference poster built from my approved content. Can you make it?"*
- *"My poster for the ISMB meeting is in ~/poster/ with manifest.json, fig1.png, fig2.png and a QR code PNG. The printer wants 36x48 in with 0.125 in bleed. Generate the .pptx and check that it's safe, with no macros. I've already signed off on the text."*
- *"I've got a one-page research poster to hand in for a symposium, and the organisers asked for a PowerPoint file their staff can still edit. Everything has been checked by my co-authors and the images are on my disk. How do I get it ready for the printer without anything unsafe in the file?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill pptx-posters

# Kalaris Labs installer with checksum verification
npx research-agent-skills install pptx-posters
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `visualization-and-presentation` category with `/plugin install visualization-and-presentation@research-agent-skills`.

## Related

- [`latex-posters`](/skills/latex-posters)
- [`presenting-conference-talks`](/skills/presenting-conference-talks)
- [`scientific-slides`](/skills/scientific-slides)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/pptx-posters/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
