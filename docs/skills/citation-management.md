---
title: "citation-management — AI agent skill for literature review"
description: "Searches OpenAlex, PubMed, and Google Scholar, extracts metadata from DOIs, PMIDs, PMCIDs, arXiv IDs, and URLs via CrossRef, PubMed, and arXiv, then formats…"
keywords: ["citations", "BibTeX", "references", "DOI", "PubMed", "reference management"]
---

# `citation-management`

**Category:** [literature-review](/skills#literature-review) · **License:** MIT · **Version:** 2.1 · **Includes scripts**

**Tags:** citations, BibTeX, references, DOI, PubMed, reference management

## When to use it

Searches OpenAlex, PubMed, and Google Scholar, extracts metadata from DOIs, PMIDs, PMCIDs, arXiv IDs, and URLs via CrossRef, PubMed, and arXiv, then formats, deduplicates, and validates BibTeX files using bundled Python scripts (search_openalex.py, extract_metadata.py, format_bibtex.py, validate_citations.py, doi_to_bibtex.py). Use when converting DOIs or PMIDs to BibTeX, finding papers on a topic, filling missing volume, pages, or DOI fields, cleaning or merging .bib files with duplicate entries, or checking a bibliography for errors before submission. Not for systematic review search methodology or synthesis; use literature-review for that.

## Example requests

Ask your agent in plain language, for example:

- *"turn these into bibtex: 10.1038/s41586-021-03819-2, PMID 31452104, arXiv:1706.03762"*
- *"My refs.bib has ~120 entries merged from Zotero and a PubMed export, and I'm seeing the same paper under keys like smith2020 and Smith2020deep. Several @article entries have no volume or pages. Can you merge/dedupe it, fill in the gaps, and make sure it's clean before I submit to Bioinformatics? Don't overwrite the original file."*
- *"I'm writing a background section on single-cell foundation models and need a starter set of the most-cited recent papers on that topic, with entries I can drop straight into my LaTeX bibliography."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill citation-management

# Kalaris Labs installer with checksum verification
npx research-agent-skills install citation-management
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `literature-review` category with `/plugin install literature-review@research-agent-skills`.

## Related

- [`autoskill`](/skills/autoskill)
- [`bibtex-hygiene`](/skills/bibtex-hygiene)
- [`citation-verification`](/skills/citation-verification)
- [`literature-review`](/skills/literature-review)
- [`paper-lookup`](/skills/paper-lookup)
- [`pyzotero`](/skills/pyzotero)
- [`reference-manager-interop`](/skills/reference-manager-interop)
- [`research-lookup`](/skills/research-lookup)
- [Write a research paper with AI](/guides/write-a-research-paper)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/citation-management/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
