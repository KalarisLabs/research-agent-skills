---
title: "hypothesis-generation — AI agent skill for ideation and design"
description: "Formulate evidence-bounded scientific questions, candidate hypotheses, rival explanations, causal or associational claims, discriminating predictions…"
keywords: ["hypothesis generation", "research questions", "preregistration", "study design", "scientific method"]
---

# `hypothesis-generation`

**Category:** [ideation-and-design](/skills#ideation-and-design) · **License:** MIT · **Version:** 2.2 · **Includes scripts**

**Tags:** hypothesis generation, research questions, preregistration, study design, scientific method

## When to use it

Formulate evidence-bounded scientific questions, candidate hypotheses, rival explanations, causal or associational claims, discriminating predictions, measurements, and preregistration-ready analysis plans. Use when turning observations or preliminary findings into transparent, testable research plans without treating hypotheses as facts.

## Example requests

Ask your agent in plain language, for example:

- *"My knockout mice gain less weight on high-fat diet than wild-type. What could explain that and how would I test it?"*
- *"I have a cohort file, ehr_statin_dementia_v3.csv (n≈48k, de-identified, from our hospital). Statin users show lower dementia incidence over 8 years. I want to write a preregistration for a follow-up paper at an epidemiology journal. Can you help me turn this into a testable plan?"*
- *"We saw a surprising dip in soil microbial diversity after the wildfire at our three field sites, and I'm not sure what to make of it or what to measure next. Help me think through what's going on and design a sensible next study."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill hypothesis-generation

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills hypothesis-generation
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ideation-and-design` category with `/plugin install ideation-and-design@research-agent-skills`.

## Related

- [`arbor`](/skills/arbor)
- [`pyvene-interventions`](/skills/pyvene-interventions)
- [`scientific-brainstorming`](/skills/scientific-brainstorming)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/hypothesis-generation/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
