---
title: "paper-lookup — AI agent skill for literature review"
description: "Search 18 scholarly APIs for papers, preprints, citations, open-access full text, repository records, and journal OA status, and return results with…"
keywords: ["paper search", "PubMed", "arXiv", "OpenAlex", "Crossref", "open access", "citations"]
---

# `paper-lookup`

**Category:** [literature-review](/skills#literature-review) · **License:** MIT · **Version:** 2.2 · **Includes scripts**

**Tags:** paper search, PubMed, arXiv, OpenAlex, Crossref, open access, citations

## When to use it

Search 18 scholarly APIs for papers, preprints, citations, open-access full text, repository records, and journal OA status, and return results with reproducible provenance. Covers PubMed, PMC, Europe PMC, bioRxiv, medRxiv, arXiv, OpenAlex, Crossref, Semantic Scholar, CORE, Unpaywall, OpenCitations, PubTator3, Zenodo, Figshare, ROR, BioStudies, and DOAJ. Use when searching for papers, citations, DOI/PMID/arXiv lookups, abstracts, full text, open-access PDFs, preprints, citation graphs, author publications, biomedical entity annotations, deposited records (Zenodo, Figshare, BioStudies), institution ROR IDs, or any scholarly literature query. Triggers on mentions of any supported database or requests like "find papers on X", "look up this DOI", "who cites this paper", or "get me the PDF".

## Example requests

Ask your agent in plain language, for example:

- *"who cites 10.1038/nature12373? need the list"*
- *"I'm writing the methods for a paper on SARS-CoV-2 spike mutations and need the open-access full text of PMID 34567890 so I can check which variants they sequenced. Pull the PDF if there is one, otherwise the XML body. NCBI eFetch gave me a 200 but the article has no body section. What's going on?"*
- *"Our lab is putting together a table of everything our collaborators at the University of Tartu have deposited as datasets or software, plus a stable ID for the institution so we can link their works. Can you track that down?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill paper-lookup

# Kalaris Labs installer with checksum verification
npx research-agent-skills install paper-lookup
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `literature-review` category with `/plugin install literature-review@research-agent-skills`.

## Related

- [`firecrawl-research-index`](/skills/firecrawl-research-index)
- [`literature-review`](/skills/literature-review)
- [`citation-management`](/skills/citation-management)
- [`citation-verification`](/skills/citation-verification)
- [Write a research paper with AI](/guides/write-a-research-paper)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/paper-lookup/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
