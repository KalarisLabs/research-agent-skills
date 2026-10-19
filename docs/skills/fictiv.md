---
title: "fictiv — AI agent skill for lab automation"
description: "Drives the Fictiv on-demand manufacturing web app (app.fictiv.com) in the user's browser, since there is no public API."
keywords: ["manufacturing", "CAD", "prototyping", "lab hardware"]
---

# `fictiv`

**Category:** [lab-automation](/skills#lab-automation) · **License:** MIT · **Version:** 1.0 · **Includes scripts**

**Tags:** manufacturing, CAD, prototyping, lab hardware

## When to use it

Drives the Fictiv on-demand manufacturing web app (app.fictiv.com) in the user's browser, since there is no public API. Covers uploading CAD files (STEP, SLDPRT, STL), configuring process, material, finish, threads and tolerances, reading DFM feedback, instant or manual quotes, lead-time tiers, checkout by card or PO, order tracking and reorders. Use when the user mentions Fictiv. Use when they want a part CNC machined, 3D printed, sheet-metal fabricated, cast, or molded online. Use when they ask to get a quote or order parts from a STEP or STL file. Use when they need to check a Fictiv quote or order status. Use when a Fictiv upload, DFM warning, price or checkout fails. Not for ITAR-controlled parts, which Fictiv does not accept.

## Example requests

Ask your agent in plain language, for example:

- *"can you get me a quote on Fictiv for this bracket? bracket_v3.step, 10 pcs, 6061 aluminum"*
- *"I uploaded rotor_housing.sldprt to my Fictiv quote and now it says 'Please request a quote' on one part and the other parts have no price. The DFM badge also shows thin walls. What's going on and what should I do before my grant-funded build deadline on the 21st?"*
- *"My lab needs 25 black-anodized aluminum enclosures for a prototype instrument, made from a STEP file I have, and shipped to our lab in Boston within about two weeks. I'd like to order them from an online machine shop that takes CAD uploads. Can you handle it from start to finish?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill fictiv

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills fictiv
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `lab-automation` category with `/plugin install lab-automation@research-agent-skills`.

## Related

- [`lab-hardware-cad`](/skills/lab-hardware-cad)
- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/fictiv/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
