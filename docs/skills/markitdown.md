---
title: "markitdown — AI agent skill for literature review"
description: "Converts documents to Markdown with Microsoft MarkItDown (Python API, markitdown CLI, markitdown-ocr plugin, markitdown-mcp server), covering PDF, Word, P…"
---

# `markitdown`

> Converts documents to Markdown with Microsoft MarkItDown (Python API, markitdown CLI, markitdown-ocr plugin, markitdown-mcp server), covering PDF, Word, PowerPoint, Excel, HTML, CSV, EPUB, ZIP, and streams, plus Azure extraction. Use when preparing papers or reports for LLM/RAG ingestion; when batch-converting a literature folder to Markdown with provenance; when converting uploaded bytes or file streams; when OCR of scanned PDFs or image text is needed; when exposing conversion to a local agent through MCP. Do not use for bounding boxes or page coordinates (use LiteParse) or PDF merge/split/forms (use the pdf skill).

**Category:** [literature-review](/skills#literature-review) · **License:** MIT · **Version:** 2.2

## Install

```bash
npx research-agent-skills install markitdown
npx skills add KalarisLabs/research-agent-skills --skill markitdown
```

## When to use it

Converts documents to Markdown with Microsoft MarkItDown (Python API, markitdown CLI, markitdown-ocr plugin, markitdown-mcp server), covering PDF, Word, PowerPoint, Excel, HTML, CSV, EPUB, ZIP, and streams, plus Azure extraction. Use when preparing papers or reports for LLM/RAG ingestion; when batch-converting a literature folder to Markdown with provenance; when converting uploaded bytes or file streams; when OCR of scanned PDFs or image text is needed; when exposing conversion to a local agent through MCP. Do not use for bounding boxes or page coordinates (use LiteParse) or PDF merge/split/forms (use the pdf skill).

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/markitdown/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
