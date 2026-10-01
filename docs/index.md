---
title: AI agent skills for scientific research and writing | Kalaris Labs
description: Open-source AI agent skills for academic writing, literature reviews, citations and scientific data analysis in biology, chemistry, medicine, physics, social science and machine learning.
---

# Research Agent Skills

**Open-source AI agent skills for researchers, students and labs.** Use them for manuscripts, theses,
grant proposals, systematic reviews, reviewer responses and scientific data analysis. Skills help you
revise prose in your own voice and verify references against scholarly records.

Built for academia across machine learning, AI, biology, chemistry, medicine and physics.

```bash
npx skills add KalarisLabs/research-agent-skills
```

Created by **Sayan Chowdhury** at **Kalaris Labs** · MIT licensed. Choose the skills and agent
harnesses you need for this project, or add `--global` for your user account. [See installation
options](/getting-started/installation) for Claude Code, OpenAI Codex, Cursor, Gemini CLI,
GitHub Copilot, OpenCode and Windsurf.

## Choose a research workflow

| Goal | Guide or skill |
|---|---|
| Write a research paper or thesis | [Paper writing guide](/guides/write-a-research-paper), [thesis and dissertation guide](/guides/thesis-and-dissertation) |
| Search literature and verify citations | [Systematic review guide](/guides/systematic-review), [`citation-verification`](/skills/citation-verification) |
| Discover papers across arXiv and life sciences | [`firecrawl-research-index`](/skills/firecrawl-research-index) for hosted search and passage reads |
| Analyze data in your discipline | [Skills by field](/guides/by-field), [full skill catalog](/skills) |
| Prepare a submission | [`arxiv-submission`](/skills/arxiv-submission), [`rebuttal-and-response-to-reviewers`](/skills/rebuttal-and-response-to-reviewers) |

## Built for academics

| If you are... | Start with |
|---|---|
| A PhD student writing a thesis or first paper | [Thesis and dissertation guide](/guides/thesis-and-dissertation), `scientific-writing`, `unslop-academic-writing`, `apa7` or your journal's format skill |
| A researcher submitting to a journal | [Write a research paper with AI](/guides/write-a-research-paper), `nature-portfolio`, `cell-press`, `ieee-transactions` and the other journal-format skills, `cover-letter-to-editor` |
| Running a systematic review or meta-analysis | [Systematic review guide](/guides/systematic-review), `systematic-review-prisma`, `citation-verification` |
| An ML researcher | `ml-paper-writing` (NeurIPS/ICML/ICLR/ACL templates), `arxiv-submission`, the `ml-training` and `ml-evaluation-and-safety` categories |
| In the life, chemical, clinical or physical sciences | [Skills by field](/guides/by-field): 100+ databases and analysis packages |
| A librarian or research-software engineer | `reference-manager-interop`, `paper-corpus-rag`, `research-knowledge-graph`, `research-skill-creator` |

## What makes it different

- **No AI slop.** `unslop-academic-writing` finds stock phrasing, empty emphasis, stacked hedges and
  monotone rhythm, then rewrites toward specific, evidence-backed prose in your own voice.
  [How it works](/guides/no-slop-academic-writing)
- **No hallucinated citations.** `citation-verification` checks every reference against Crossref, OpenAlex
  and arXiv. On our labeled benchmark it flags every fabricated and corrupted reference
  ([results](/reference/benchmarks)).
- **Current venue rules, not remembered ones.** Journal skills make the agent read the current author
  guidelines before formatting.
- **Measured.** Every skill receives a static quality score. Reviewed prompt sets test trigger routing;
  selected skills have with-vs-without-skill task evaluations. [Benchmarks](/reference/benchmarks)
- **Secure.** Every file is scanned for prompt injection and malicious code, and releases are checksummed, signed and attested.

[Install Research Agent Skills](/getting-started/installation) · [Browse all skills](/skills)
