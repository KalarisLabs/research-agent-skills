---
title: How to write a research paper with AI agents (without slop or fake citations)
description: A step-by-step workflow for writing a journal or conference paper with Claude Code, Codex or Cursor using research agent skills, from outline to submission, with citation verification and no AI slop.
---

# Write a research paper with AI agents

AI agents can speed up every stage of a paper, but they also invent references, inflate claims
and produce recognizable "AI prose". This workflow keeps you, the author, in control and uses skills
to enforce the checks that stop those failures.

## The workflow

1. **Collect the evidence first.** Put results tables, figures, analysis notebooks and your notes in one
   folder. Ask the agent to summarize what the data shows *before* any drafting (`scientific-critical-thinking`,
   `statistical-analysis`).
2. **Outline the argument.** Ask for a one-sentence contribution, then a section outline in which every
   paragraph has one claim and its supporting figure or table (`scientific-writing`, or `ml-paper-writing` for ML venues).
3. **Draft section by section.** Start with Methods and Results, then Discussion, then Introduction, and write the
   Abstract and Title last (`abstract-and-title`). Review each section before moving on.
4. **Cite from real records only.** Find papers with `literature-review` / `paper-lookup`, or use
   [`firecrawl-research-index`](/skills/firecrawl-research-index) for hosted discovery and passage reads.
   Export BibTeX from the publisher or Crossref, and never let the agent write a reference from memory.
5. **Verify every citation.** Run `citation-verification` on the `.bib`. Fix or remove anything flagged
   `mismatch`, `doi-not-found` or `not-found`. Then check that each cited paper supports its sentence.
6. **Clean the bibliography.** `bibtex-hygiene` removes duplicates, fixes DOIs and protects acronym capitalization.
7. **Remove the slop.** Run `unslop-academic-writing`: fix content (vague claims, missing numbers) before words.
   Aim for a slop index under 5 in the abstract and introduction.
8. **Format for the venue.** Use the journal skill (`nature-portfolio`, `science-aaas`, `cell-press`, `ieee-transactions`,
   `acm-sigconf`, `elsevier-cas`, `springer-lncs`, `plos`, `apa7`) or `venue-templates`. The skill makes the agent read the
   current author guidelines.
9. **Prepare the statements.** `reproducibility-statement` covers data and code availability, checklists, CRediT
   and AI-use disclosure.
10. **Submit.** `cover-letter-to-editor` for the letter and reviewer suggestions, and `arxiv-submission` for the preprint.
11. **Revise.** `rebuttal-and-response-to-reviewers` triages the reviews and drafts point-by-point responses.

## Rules that protect you

- The author is responsible for every sentence. Read everything the agent writes.
- Disclose AI assistance as your venue requires. Never list an AI as an author.
- Never let an agent invent data, results, statistics or references.
- Keep your analysis reproducible: the numbers in the text must come from code you can rerun.

## Related guides

[Thesis and dissertation](/guides/thesis-and-dissertation) · [No-slop academic writing](/guides/no-slop-academic-writing) ·
[Systematic reviews](/guides/systematic-review)
