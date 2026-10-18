---
title: "ginkgo-cloud-lab — AI agent skill for lab automation"
description: "Submit and manage protocols on Ginkgo Bioworks Cloud Lab (cloud.ginkgo.bio), a web-based interface for autonomous lab execution on Reconfigurable Automation…"
keywords: ["cloud lab", "lab automation", "protein expression", "synthetic biology"]
---

# `ginkgo-cloud-lab`

**Category:** [lab-automation](/skills#lab-automation) · **License:** MIT · **Version:** 2.1

**Tags:** cloud lab, lab automation, protein expression, synthetic biology

## When to use it

Submit and manage protocols on Ginkgo Bioworks Cloud Lab (cloud.ginkgo.bio), a web-based interface for autonomous lab execution on Reconfigurable Automation Carts (RACs). Use when the user wants to run protein expression and purification (cell-free, E. coli, or Pichia), HiBiT or A280 or LabChip quantification, IVT mRNA/circRNA synthesis, thermal shift / developability assays, Echo-MS enzyme or analyte methods, SPR target onboarding, fluorescent pixel art, or otherwise interact with Ginkgo Cloud Lab services. Covers protocol selection, input preparation, pricing, and ordering workflows.

## Example requests

Ask your agent in plain language, for example:

- *"I have 48 de novo minibinder sequences and want to know which ones express in E. coli before I invest in SPR. What's the cheapest way to screen them on Ginkgo's cloud lab, and what would it cost?"*
- *"Need Tm values for my 12 nanobody variants (sequences in nb_variants.fasta). Can Ginkgo's cloud lab do thermal shift, and how do I submit?"*
- *"I'm trying to make a circular RNA for a stability study and want qPCR confirmation of the product, outsourced to a robotic cloud lab if possible. The template DNA is ready. What are my options and how do I get a quote?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill ginkgo-cloud-lab

# Kalaris Labs installer with checksum verification
npx research-agent-skills install ginkgo-cloud-lab
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `lab-automation` category with `/plugin install lab-automation@research-agent-skills`.

## Related

- [`adaptyv`](/skills/adaptyv)
- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/ginkgo-cloud-lab/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
