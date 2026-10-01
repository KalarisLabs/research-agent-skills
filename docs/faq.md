---
title: FAQ | Research Agent Skills
description: Answers about using AI agent skills for academic research, including hallucinated citations, AI slop, journal formatting, data privacy, supported agents and academic integrity.
---

# Frequently asked questions

??? question "What are agent skills?"
    Folders of instructions (`SKILL.md`), references and scripts that an AI agent loads when a task needs them.
    They follow the open [Agent Skills specification](https://agentskills.io) and work in Claude Code, Codex, Cursor,
    Gemini CLI, GitHub Copilot, OpenCode, Windsurf and Claude.ai.

??? question "Can AI write my research paper?"
    It can help you write it faster: outlining, drafting from your results, editing, formatting and checking references.
    You remain the author. Every claim, number and citation must be yours and verified. See
    [Write a research paper with AI](/guides/write-a-research-paper).

??? question "How do I stop AI from inventing citations?"
    Never accept references written from memory. Export them from publishers or Crossref, then run `citation-verification`,
    which checks each entry against Crossref, OpenAlex and arXiv and flags fabricated or mismatched references.

??? question "How do I make AI-assisted writing not sound like AI?"
    Use `unslop-academic-writing`. It finds stock phrasing, empty emphasis, stacked hedges and monotone rhythm, and it
    rewrites toward specific, evidence-backed prose in your own voice. It improves writing and is not a way to hide AI use.

??? question "Is this allowed by journals and universities?"
    Most publishers allow AI assistance with disclosure and forbid AI authorship, and universities set their own rules for theses.
    Check the current policy of your venue or institution. `reproducibility-statement` covers disclosure statements.

??? question "Does anything leave my computer?"
    Skills are local files. Some scripts query public scholarly APIs (Crossref, OpenAlex, arXiv, PubMed) or services
    you configure with your own key. Allowed domains are reviewed. The installer has no telemetry. Your agent's own data
    handling is governed by its provider.

??? question "Which skills should I install?"
    Start with `npx research-agent-skills` (the research-essentials bundle), then add your field's category.
    Installing everything works but places every skill description in your agent's context.

??? question "How do you know the skills are any good?"
    Every skill is scored by a static rubric, a trigger-routing benchmark and with-vs-without-skill task evaluations,
    and the citation and slop tools have their own benchmarks. See [Benchmarks and quality](/reference/benchmarks).

??? question "How do I cite this project?"
    Use GitHub's "Cite this repository" button (from `CITATION.cff`) or the BibTeX in the README.
