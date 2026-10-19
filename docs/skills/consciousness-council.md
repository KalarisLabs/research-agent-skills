---
title: "consciousness-council — AI agent skill for ideation and design"
description: "Run a multi-perspective Mind Council deliberation on any question, decision, or creative challenge."
keywords: ["brainstorming", "decision making", "multi-perspective analysis", "ideation"]
---

# `consciousness-council`

**Category:** [ideation-and-design](/skills#ideation-and-design) · **License:** MIT · **Version:** 1.0

**Tags:** brainstorming, decision making, multi-perspective analysis, ideation

## When to use it

Run a multi-perspective Mind Council deliberation on any question, decision, or creative challenge. Use this skill whenever the user wants diverse viewpoints, needs help making a tough decision, asks for a council/panel/board discussion, wants to explore a problem from multiple angles, requests devil's advocate analysis, or says things like "what would different experts think about this", "help me think through this from all sides", "council mode", "mind council", or "deliberate on this". Also trigger when the user faces a dilemma, trade-off, or complex choice with no obvious answer.

## Example requests

Ask your agent in plain language, for example:

- *"council mode: should our lab keep maintaining our in-house RNA-seq pipeline or switch to nf-core/rnaseq?"*
- *"I'm a postdoc in structural biology at a mid-size university. I have two offers: a tenure-track job at a teaching-focused college with a small cryo-EM facility, or a 3-year extension in my current PI's lab with a Nature-level project (draft in manuscript_v4.docx) but no guarantee of a faculty job after. My partner's job is in the college's city. I keep going in circles. Can you have a few different expert voices argue this out so I can see the trade-offs?"*
- *"We have a grant budget for only one big instrument purchase this year: a single-cell sequencing platform or a high-resolution mass spec. Our group is split and nobody can agree. I want to hear this argued from every angle, including someone who attacks whichever option looks most obvious, before I bring it to the group."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill consciousness-council

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills consciousness-council
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ideation-and-design` category with `/plugin install ideation-and-design@research-agent-skills`.

## Related

- [`dhdna-profiler`](/skills/dhdna-profiler)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/consciousness-council/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
