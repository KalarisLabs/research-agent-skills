---
title: "exa-search — AI agent skill for literature review"
description: "Web toolkit powered by Exa, tuned for scientific and technical content. Use this skill when the user needs to search the web or fetch/extract URL content."
keywords: ["web search", "research search", "scientific content", "URL extraction"]
---

# `exa-search`

**Category:** [literature-review](/skills#literature-review) · **License:** MIT · **Version:** 1.2 · **Includes scripts**

**Tags:** web search, research search, scientific content, URL extraction

## When to use it

Web toolkit powered by Exa, tuned for scientific and technical content. Use this skill when the user needs to search the web or fetch/extract URL content. Covers: web search (semantic lookups, research, current info — with optional research-paper category and academic domain filtering) and URL extraction (fetching pages, articles, academic PDFs in batch). Use this skill for web-related tasks when the user wants high-quality search or scholarly filtering via category=research paper. Triggers on requests to search, look up, fetch a page, or extract an article.

## Example requests

Ask your agent in plain language, for example:

- *"find recent papers on diffusion models for protein design"*
- *"I'm writing the related-work section for my ICLR submission on sparse autoencoders for interpreting LLM activations. Find me peer-reviewed or arXiv sources from 2024 onward, and skip blog posts and news coverage. Show which search parameters you used."*
- *"Here are 12 links to PDFs and journal pages from our lab's reading list. I need the full text of each pulled into one place so I can skim them for methods details."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill exa-search

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills exa-search
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `literature-review` category with `/plugin install literature-review@research-agent-skills`.

## Related

- [`open-notebook`](/skills/open-notebook)
- [`parallel-web`](/skills/parallel-web)
- [`research-lookup`](/skills/research-lookup)
- [`nemo-curator`](/skills/nemo-curator)
- [Write a research paper with AI](/guides/write-a-research-paper)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/exa-search/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
