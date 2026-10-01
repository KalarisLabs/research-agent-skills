---
title: "citation-management — AI agent skill for literature review"
description: "Searches OpenAlex, PubMed, and Google Scholar, extracts metadata from DOIs, PMIDs, PMCIDs, arXiv IDs, and URLs via CrossRef, PubMed, and arXiv, then forma…"
---

# `citation-management`

> Searches OpenAlex, PubMed, and Google Scholar, extracts metadata from DOIs, PMIDs, PMCIDs, arXiv IDs, and URLs via CrossRef, PubMed, and arXiv, then formats, deduplicates, and validates BibTeX files using bundled Python scripts (search_openalex.py, extract_metadata.py, format_bibtex.py, validate_citations.py, doi_to_bibtex.py). Use when converting DOIs or PMIDs to BibTeX, finding papers on a topic, filling missing volume, pages, or DOI fields, cleaning or merging .bib files with duplicate entries, or checking a bibliography for errors before submission. Not for systematic review search methodology or synthesis; use literature-review for that.

**Category:** [literature-review](/skills#literature-review) · **License:** MIT · **Version:** 2.1

## Install

```bash
npx skills add KalarisLabs/research-agent-skills --skill citation-management
```

## When to use it

Searches OpenAlex, PubMed, and Google Scholar, extracts metadata from DOIs, PMIDs, PMCIDs, arXiv IDs, and URLs via CrossRef, PubMed, and arXiv, then formats, deduplicates, and validates BibTeX files using bundled Python scripts (search_openalex.py, extract_metadata.py, format_bibtex.py, validate_citations.py, doi_to_bibtex.py). Use when converting DOIs or PMIDs to BibTeX, finding papers on a topic, filling missing volume, pages, or DOI fields, cleaning or merging .bib files with duplicate entries, or checking a bibliography for errors before submission. Not for systematic review search methodology or synthesis; use literature-review for that.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/citation-management/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
