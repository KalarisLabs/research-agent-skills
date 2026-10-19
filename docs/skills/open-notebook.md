---
title: "open-notebook — AI agent skill for literature review"
description: "Self-hosted, open-source alternative to Google NotebookLM for AI-powered research and document analysis."
keywords: ["research notebooks", "document analysis", "NotebookLM alternative", "knowledge management"]
---

# `open-notebook`

**Category:** [literature-review](/skills#literature-review) · **License:** MIT · **Version:** 1.3 · **Includes scripts**

**Tags:** research notebooks, document analysis, NotebookLM alternative, knowledge management

## When to use it

Self-hosted, open-source alternative to Google NotebookLM for AI-powered research and document analysis. Use when organizing research materials into notebooks, ingesting diverse content sources (PDFs, videos, audio, web pages, Office documents), generating AI-powered notes and summaries, creating multi-speaker podcasts from research, chatting with documents using context-aware AI, searching across materials with full-text and vector search, or running custom content transformations. Supports 16+ AI providers including OpenAI, Anthropic, Google, Ollama, Groq, and Mistral with complete data privacy through self-hosting.

## Example requests

Ask your agent in plain language, for example:

- *"How do I set up Open Notebook locally with Ollama so I can chat with my PDFs?"*
- *"I have 40 PDFs from my glioblastoma review in ~/papers/gbm and a few YouTube talks. I'm running the self-hosted open-notebook container and POST /api/sources keeps returning an error after I created the notebook. Can you help me script ingesting everything into one notebook, then run a vector search for 'temozolomide resistance'?"*
- *"I'd like to turn my collected papers and interview recordings on microplastics into a short two-host audio discussion I can listen to on my commute, and keep everything on our own lab server because of consent restrictions. What are my options?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill open-notebook

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills open-notebook
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `literature-review` category with `/plugin install literature-review@research-agent-skills`.

## Related

- [`exa-search`](/skills/exa-search)
- [`liteparse`](/skills/liteparse)
- [`paper-corpus-rag`](/skills/paper-corpus-rag)
- [Write a research paper with AI](/guides/write-a-research-paper)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/open-notebook/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
