---
title: "paperzilla — AI agent skill for literature review"
description: "Chat with your agent about projects, recommendations, and canonical papers in Paperzilla."
keywords: ["paper recommendations", "research feeds", "literature monitoring"]
---

# `paperzilla`

**Category:** [literature-review](/skills#literature-review) · **License:** MIT · **Version:** 1.0

**Tags:** paper recommendations, research feeds, literature monitoring

## When to use it

Chat with your agent about projects, recommendations, and canonical papers in Paperzilla. Use when users ask for recent project recommendations, canonical paper details, markdown-based summaries, recommendation feedback, feed export, or Atom feed URLs.

## Example requests

Ask your agent in plain language, for example:

- *"what's new in my Paperzilla project on protein language models this week?"*
- *"I ran `pz feed crispr-offtarget --must-read --limit 5 --json` and got 5 items. Rec ID rec_8f21 looks interesting; can you pull the full markdown for it and tell me why it matters for my base-editing work? If it says it's not ready, what should I do?"*
- *"I'd like to subscribe to the stream of papers that my lab's curated literature-tracking project surfaces, in my RSS reader, and also mark the ones that were useful so the ranking improves. How do I do that?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill paperzilla

# Kalaris Labs installer with checksum verification
npx research-agent-skills install paperzilla
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `literature-review` category with `/plugin install literature-review@research-agent-skills`.

## Related

- [Write a research paper with AI](/guides/write-a-research-paper)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/paperzilla/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
