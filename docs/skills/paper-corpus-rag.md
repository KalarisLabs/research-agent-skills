---
title: "paper-corpus-rag — AI agent skill for knowledge and rag"
description: "Build grounded question answering over your own collection of research papers, with answers that cite the exact paper, page and passage."
keywords: ["RAG", "retrieval", "hybrid search", "SQLite FTS5", "BM25", "PDF conversion", "literature synthesis", "citations", "evaluation"]
---

# `paper-corpus-rag`

**Category:** [knowledge-and-rag](/skills#knowledge-and-rag) · **License:** MIT · **Version:** 1.1 · **Includes scripts**

**Tags:** RAG, retrieval, hybrid search, SQLite FTS5, BM25, PDF conversion, literature synthesis, citations, evaluation

## When to use it

Build grounded question answering over your own collection of research papers, with answers that cite the exact paper, page and passage. Use when a user wants to chat with or search a folder of PDFs, summarize what a set of papers says, synthesize evidence across a literature corpus, find which paper says X, convert PDFs to citable Markdown with a quality grade, handle scanned PDFs or damaged tables, decide whether a vector database is needed, evaluate whether a paper-QA pipeline is any good, or build a hybrid index (SQLite FTS5 BM25 plus embeddings fused by reciprocal rank). Search locates papers; the agent then reads the full converted file before synthesizing.

## Example requests

Ask your agent in plain language, for example:

- *"I have 300 PDFs of papers in a folder. Let me ask questions and get answers with citations to the exact page."*
- *"My RAG over our lab's papers keeps giving the right paper but the wrong number from a table. What is going on?"*
- *"Some of my PDFs are scans. The search finds nothing for papers I know are in the folder."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill paper-corpus-rag

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills paper-corpus-rag
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `knowledge-and-rag` category with `/plugin install knowledge-and-rag@research-agent-skills`.

## Related

- [`firecrawl-research-index`](/skills/firecrawl-research-index)
- [`fulltext-acquisition`](/skills/fulltext-acquisition)
- [`paper-card`](/skills/paper-card)
- [`citation-verification`](/skills/citation-verification)
- [`literature-review`](/skills/literature-review)
- [`paper-lookup`](/skills/paper-lookup)
- [`qdrant-vector-search`](/skills/qdrant-vector-search)
- [`research-knowledge-graph`](/skills/research-knowledge-graph)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/paper-corpus-rag/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
