---
title: "etetoolkit — AI agent skill for life sciences"
description: "Analyze, manipulate, compare, annotate, and visualize phylogenetic or other hierarchical trees with ETE 4."
keywords: ["phylogenetics", "phylogenetic trees", "Newick", "evolutionary biology", "bioinformatics"]
---

# `etetoolkit`

**Category:** [life-sciences](/skills#life-sciences) · **License:** GPL-3.0-or-later · **Version:** 2.1 · **Includes scripts**

**Tags:** phylogenetics, phylogenetic trees, Newick, evolutionary biology, bioinformatics

## When to use it

Analyze, manipulate, compare, annotate, and visualize phylogenetic or other hierarchical trees with ETE 4. Use for Newick/Nexus tree I/O, topology edits and pattern matching, Robinson-Foulds comparisons, gene-tree evolutionary events and reconciliation, NCBI/GTDB taxonomy, SmartView exploration, and publication rendering. Do not use it to infer trees from raw sequences; align sequences and infer a tree first.

## Example requests

Ask your agent in plain language, for example:

- *"How do I load a Newick file in ete4 and prune it down to just 12 taxa?"*
- *"I'm porting my lab's old ete3 script to ete4 and it now fails with 'NewickError' on gene_tree.nwk, which has bootstrap support on internal nodes. The old code used Tree('gene_tree.nwk', format=1) and `t & 'Hsap_1'`, then called node.is_leaf() and t.get_leaves(). Fix it and then label each internal node as duplication or speciation, where leaf names look like SPECIES_geneID."*
- *"I have two published trees for the same 40 bird species, one from mitochondrial genomes and one from nuclear loci. I want a number that tells me how different their branching patterns are, and I'd also like to know which splits they disagree on."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill etetoolkit

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills etetoolkit
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `life-sciences` category with `/plugin install life-sciences@research-agent-skills`.

## Related

- [`scikit-bio`](/skills/scikit-bio)
- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/etetoolkit/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
