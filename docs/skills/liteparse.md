---
title: "liteparse — AI agent skill for literature review"
description: "Local document and PDF parsing that returns spatial text with bounding boxes."
keywords: ["PDF parsing", "OCR", "document extraction", "RAG", "papers"]
---

# `liteparse`

**Category:** [literature-review](/skills#literature-review) · **License:** Apache-2.0 · **Version:** 1.2 · **Includes scripts**

**Tags:** PDF parsing, OCR, document extraction, RAG, papers

## When to use it

Local document and PDF parsing that returns spatial text with bounding boxes. Use for extracting text from PDFs, DOCX, Office files, and images; running OCR on scans; producing layout-preserved JSON for RAG; batch-ingesting folders of papers; or rendering pages to PNG for multimodal agents. Distinguishing capabilities are per-token bounding boxes, page raster output, and fully local processing with no cloud API.

## Example requests

Ask your agent in plain language, for example:

- *"How do I get word-level bounding boxes out of a PDF locally? No cloud APIs please."*
- *"I have a folder of ~300 scanned supplementary PDFs in ./supp_pdfs/ from a proteomics project. Some are image-only scans and OCR is crawling. I need layout-preserved JSON for each, written to ./parsed/, and only pages 5-12 of each since that's where the methods are. What should I run, and how do I speed it up?"*
- *"I'm building a RAG system over my lab's papers, and I want to highlight the exact region of the page where an answer came from, and also show a vision model the page image alongside it. How should I set up the ingestion?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill liteparse

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills liteparse
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `literature-review` category with `/plugin install literature-review@research-agent-skills`.

## Related

- [`open-notebook`](/skills/open-notebook)
- [Write a research paper with AI](/guides/write-a-research-paper)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/liteparse/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
