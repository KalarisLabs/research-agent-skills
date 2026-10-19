---
title: "latex-posters — AI agent skill for visualization and presentation"
description: "Creates research posters in LaTeX with beamerposter, tikzposter, or baposter, covering page sizes (A0, A1, 36x48 inch), multi-column layouts, color schemes…"
keywords: ["research posters", "LaTeX", "conference posters", "beamerposter", "academic presentations"]
---

# `latex-posters`

**Category:** [visualization-and-presentation](/skills#visualization-and-presentation) · **License:** MIT · **Version:** 1.7 · **Includes scripts**

**Tags:** research posters, LaTeX, conference posters, beamerposter, academic presentations

## When to use it

Creates research posters in LaTeX with beamerposter, tikzposter, or baposter, covering page sizes (A0, A1, 36x48 inch), multi-column layouts, color schemes, figure and QR code placement, and pdflatex/overfull-box checks before printing. Also guides generating poster graphics with AI schematic tools under strict element and word limits. Use when preparing a conference or symposium poster, converting a paper into a poster, building a department poster template, or fitting a conference's size rules. Use when fixing overflow or unreadable text on a compiled poster. For slide decks, use a presentation skill instead.

## Example requests

Ask your agent in plain language, for example:

- *"I need a poster for my lab's symposium next month, A0 portrait, 3 columns. Can you set up a LaTeX template?"*
- *"My poster.tex compiled with tikzposter on 36x48 inch, but the log shows a pile of 'Overfull \hbox' warnings and the right column text runs off the edge. Figures are in figures/ at width=\linewidth. How do I fix it before sending to the print shop?"*
- *"I just got my paper accepted and the conference wants a printed poster summarizing it, 841x1189 mm. I have the PDF and a few figure files. I'd like AI-made diagrams for the methods and results sections, and it must be readable from a few meters away. How should I go about it?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill latex-posters

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills latex-posters
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `visualization-and-presentation` category with `/plugin install visualization-and-presentation@research-agent-skills`.

## Related

- [`academic-plotting`](/skills/academic-plotting)
- [`generate-image`](/skills/generate-image)
- [`pptx-posters`](/skills/pptx-posters)
- [`presenting-conference-talks`](/skills/presenting-conference-talks)
- [`venue-templates`](/skills/venue-templates)
- [`scientific-slides`](/skills/scientific-slides)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/latex-posters/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
