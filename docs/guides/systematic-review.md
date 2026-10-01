---
title: Systematic reviews and meta-analyses with AI agents (PRISMA 2020)
description: Run a reproducible systematic review with AI agents, covering protocol registration, database search strings, deduplication, screening, risk of bias, synthesis, the PRISMA 2020 flow diagram and checklist.
---

# Systematic reviews with PRISMA 2020

The `systematic-review-prisma` skill guides an agent through a review that another team could
reproduce, and its scripts keep the numbers consistent.

## Steps

1. **Protocol**: PICO question, eligibility criteria, outcomes, and registration on PROSPERO or OSF before screening.
2. **Search**: one concept block per PICO element, translated per database (PubMed, Embase, Scopus, Web of Science), with dates and hit counts recorded.
3. **Deduplicate**: `python scripts/dedupe_records.py pubmed.ris scopus.csv wos.bib -o screening.csv --summary counts.json`
4. **Screen**: two independent reviewers, reasons for full-text exclusion, and agreement reported. AI-assisted screening must be validated and never the sole reviewer.
5. **Extract and appraise**: RoB 2, ROBINS-I, QUADAS-2 or other tools matched to design. GRADE certainty per outcome.
6. **Synthesize**: a random-effects meta-analysis when appropriate, otherwise SWiM.
7. **Report**: `python scripts/prisma_flow.py counts.json` draws the PRISMA 2020 flow diagram and refuses arithmetic that doesn't add up. Complete the 27-item checklist.

## Helpful companions

`literature-review` (search), `citation-verification` (check included studies' records),
`research-knowledge-graph` (citation snowballing), `statistical-analysis` (meta-analysis methods),
`plos` or your journal's format skill, and `reproducibility-statement` (data and protocol availability).
[`firecrawl-research-index`](/skills/firecrawl-research-index) can help discover additional
papers and citation neighbors; record its query and date as a supplementary search source.
