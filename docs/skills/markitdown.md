---
title: "markitdown — AI agent skill for literature review"
description: "Converts documents to Markdown with Microsoft MarkItDown (Python API, markitdown CLI, markitdown-ocr plugin, markitdown-mcp server), covering PDF, Word…"
keywords: ["document conversion", "PDF to Markdown", "Word", "PowerPoint", "text extraction"]
---

# `markitdown`

**Category:** [literature-review](/skills#literature-review) · **License:** MIT · **Version:** 2.2 · **Includes scripts**

**Tags:** document conversion, PDF to Markdown, Word, PowerPoint, text extraction

## When to use it

Converts documents to Markdown with Microsoft MarkItDown (Python API, markitdown CLI, markitdown-ocr plugin, markitdown-mcp server), covering PDF, Word, PowerPoint, Excel, HTML, CSV, EPUB, ZIP, and streams, plus Azure extraction. Use when preparing papers or reports for LLM/RAG ingestion; when batch-converting a literature folder to Markdown with provenance; when converting uploaded bytes or file streams; when OCR of scanned PDFs or image text is needed; when exposing conversion to a local agent through MCP. Do not use for bounding boxes or page coordinates (use LiteParse) or PDF merge/split/forms (use the pdf skill).

## Example requests

Ask your agent in plain language, for example:

- *"How do I turn a .docx into markdown with python? Want it clean for feeding to an LLM."*
- *"I have ~300 PDFs in ./lit/ named like Smith_2025_CRISPR-screens.pdf and I need them as .md files for a RAG index. I want each one to record where it came from, and ideally they'd be grouped by year. Some are scans, though. What's the cleanest way to do this on Windows?"*
- *"My web backend receives uploaded report files as raw bytes (no filename on disk). I need to extract their text as markdown for a summarizer, and I'm worried about untrusted content. What should I do?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill markitdown

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills markitdown
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `literature-review` category with `/plugin install literature-review@research-agent-skills`.

## Related

- [Write a research paper with AI](/guides/write-a-research-paper)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/markitdown/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
