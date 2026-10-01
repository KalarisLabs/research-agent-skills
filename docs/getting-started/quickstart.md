---
title: Quickstart | Research Agent Skills
description: Install research agent skills and run your first paper-writing, citation-checking and journal-formatting tasks in ten minutes.
---

# Quickstart (10 minutes)

## 1. Install

```bash
npx research-agent-skills          # pick bundles and agents interactively
```

The default **research-essentials** bundle installs writing, journal-format, literature-review,
ideation and figure skills for every agent detected on your machine. Restart your agent afterwards.

## 2. Check the setup

```bash
npx research-agent-skills doctor
```

This shows detected agents, Python/uv availability (needed by skills with scripts) and the integrity of installed files.

## 3. Try these requests

Open your agent in a folder with your manuscript or data and ask:

| Task | Example request | Skill that activates |
|---|---|---|
| Draft from results | "Draft the Results section from `results/` and the figures in `figs/`." | `scientific-writing` |
| Remove AI slop | "This introduction sounds AI-written. Unslop it without changing any claims." | `unslop-academic-writing` |
| Check references | "Verify every entry in `refs.bib` and tell me which ones don't exist." | `citation-verification` |
| Clean the bibliography | "Find duplicates and broken DOIs in `refs.bib`." | `bibtex-hygiene` |
| Format for a journal | "Reformat this for Cell Reports: Summary, Highlights, STAR Methods." | `cell-press` |
| Respond to reviewers | "Draft a point-by-point response to these three reviews." | `rebuttal-and-response-to-reviewers` |
| Post a preprint | "Check my LaTeX folder before I upload to arXiv." | `arxiv-submission` |

You don't need to name the skill. The agent picks it from the request. Naming it ("use the
citation-verification skill") forces it.

## 4. Add your field

```bash
npx research-agent-skills list --categories
npx research-agent-skills install --category life-sciences     # or chemistry-and-drug-discovery, ml-training, ...
```

## 5. Stay current

```bash
npx research-agent-skills update
```

Next: [Write a research paper with AI](/guides/write-a-research-paper), or browse the [skill catalog](/skills).
