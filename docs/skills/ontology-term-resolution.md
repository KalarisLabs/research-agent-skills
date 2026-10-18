---
title: "ontology-term-resolution — AI agent skill for scientific databases"
description: "Resolve free-text scientific labels to ontology term IDs and validate existing CURIEs against the EBI Ontology Lookup Service (OLS4)."
keywords: ["ontologies", "CURIEs", "OLS", "metadata annotation", "FAIR data"]
---

# `ontology-term-resolution`

**Category:** [scientific-databases](/skills#scientific-databases) · **License:** MIT · **Version:** 1.2 · **Includes scripts**

**Tags:** ontologies, CURIEs, OLS, metadata annotation, FAIR data

## When to use it

Resolve free-text scientific labels to ontology term IDs and validate existing CURIEs against the EBI Ontology Lookup Service (OLS4). Also look up prefixes in Bioregistry, resolve compact identifiers via Identifiers.org, map lab shorthand with ZOOMA, and build Ontobee term pages. Use whenever an ontology identifier must be produced or checked - annotating tissue, cell type, disease, phenotype, assay, chemical, organism, sex, or developmental stage fields; preparing metadata for GEO, ENA, BioSamples, CELLxGENE, HCA, or ISA-Tab submission; auditing a metadata table of term IDs; checking whether a term is obsolete and what replaced it; or deciding HPO vs HP. Triggers include "ontology term", "ontology ID", "CURIE", "controlled vocabulary", "UBERON", "CL:", "MONDO", "HPO", "EFO", "ChEBI", "NCBITaxon", "GO term", "PATO", "Zooma", "Bioregistry", "Identifiers.org", "Ontobee", "annotate this tissue/cell type/disease", and any request to emit or verify an identifier shaped like PREFIX:0001234.

## Example requests

Ask your agent in plain language, for example:

- *"What's the UBERON ID for left ventricle?"*
- *"I have samples_metadata.tsv for a CELLxGENE submission with columns tissue_ontology_term_id, cell_type_ontology_term_id and disease_ontology_term_id, filled in by a postdoc who left. Some IDs look old. Can you check the whole table and tell me which ones will get rejected? One row has UBERON:0002108 labelled 'liver'."*
- *"My bench notes say 'PBMC', 'WT' and 'ctrl' for the sample type, genotype and treatment columns of a GEO submission. I need proper controlled-vocabulary identifiers for these before I upload."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill ontology-term-resolution

# Kalaris Labs installer with checksum verification
npx research-agent-skills install ontology-term-resolution
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `scientific-databases` category with `/plugin install scientific-databases@research-agent-skills`.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/ontology-term-resolution/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
