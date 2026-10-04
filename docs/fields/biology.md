---
title: Biology and bioinformatics research skills
description: Agent skills for single-cell analysis, differential expression and biological database research.
---

# Biology and bioinformatics research

Start with the biological question, sample design and data provenance. For single-cell work, record quality-control thresholds and batch handling before interpreting clusters or marker genes.

| Task | Skill | Evidence to inspect |
|---|---|---|
| Explore single-cell RNA-seq | [`scanpy`](/skills/scanpy) | Count matrix, metadata and quality-control plots |
| Model batch effects and latent structure | [`scvi-tools`](/skills/scvi-tools) | Batch labels, model assumptions and diagnostics |
| Test differential expression | [`pydeseq2`](/skills/pydeseq2) | Replicates, design formula and adjusted p-values |
| Resolve genes and related records | [`gget`](/skills/gget) | Species, assembly and database identifiers |
| Query public cell atlases | [`cellxgene-census`](/skills/cellxgene-census) | Dataset version and cell-selection criteria |

```bash
npx skills add KalarisLabs/research-agent-skills --skill scanpy
```

Try: “Review this AnnData object and propose a single-cell QC workflow. Explain each threshold and save plots before filtering.” Validate gene annotations and statistical conclusions against the underlying data. For a review of the literature, use the [systematic review workflow](/guides/systematic-review).
