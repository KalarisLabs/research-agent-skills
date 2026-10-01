---
title: AI agent skills by research field | biology, chemistry, medicine, physics and ML
description: Choose research agent skills for bioinformatics, drug discovery, clinical research, physical sciences, psychology, social science or machine learning, with field-specific installation commands and example tasks.
---

# AI agent skills by research field

Research Agent Skills from Kalaris Labs combines scientific data tools with skills for literature review,
academic writing, citations and publication. Researchers in academia can start with a focused bundle:
`ml-research`, `ai-research`, `biology-research`, `chemistry-research`, `medicine-research` or
`physics-research`. For example, run `npx research-agent-skills install --bundle biology-research --project`.
Install an entire field category with `npx research-agent-skills install --category <name>`.
The default **research-essentials** bundle covers
writing, journal formats, literature review, ideation and figures across disciplines.

| Field | Categories | Examples |
|---|---|---|
| Genomics, single-cell, bioinformatics | `life-sciences`, `scientific-databases` | scanpy, scvi-tools, pydeseq2, pysam, deeptools, nextflow, gget, cellxgene-census |
| Neuroscience | `life-sciences` | neuropixels-analysis, neurokit2, bids |
| Chemistry and drug discovery | `chemistry-and-drug-discovery` | rdkit, datamol, deepchem, medchem, diffdock, molecular-dynamics, pkpd-modeling |
| Clinical and health research | `clinical-and-health` | clinical-reports, treatment-plans, pydicom, pathml, pyhealth |
| Physics, astronomy, materials, earth science | `physical-sciences` | astropy, qiskit, pennylane, pymatgen, geopandas |
| Machine learning research | `ml-training`, `ml-evaluation-and-safety`, `ml-inference-and-ops`, `llm-applications`, `multimodal-and-emerging` | fine-tuning, distributed training, evaluation harnesses, interpretability, inference serving |
| Data science and statistics | `data-science-and-ml` | scikit-learn, statsmodels, pymc, shap, polars, dask |
| Social sciences and psychology | `research-writing`, `ideation-and-design`, `journal-formats` | apa7, statistical-analysis, experimental-design, statistical-power |
| Lab automation | `lab-automation` | opentrons-integration, pylabrobot, benchling-integration, protocolsio-integration |
| Literature and knowledge work | `literature-review`, `knowledge-and-rag` | firecrawl-research-index, systematic-review-prisma, citation-verification, paper-corpus-rag, research-knowledge-graph |

## Life sciences, genomics and bioinformatics

Install `life-sciences` for workflows involving sequencing, single-cell analysis, biological networks and
biomedical data. For example, [`scanpy`](/skills/scanpy) explores single-cell RNA-seq data,
[`scvi-tools`](/skills/scvi-tools) covers probabilistic single-cell models, and
[`pydeseq2`](/skills/pydeseq2) supports differential expression analysis. Add
`scientific-databases` when the task needs external records and identifiers.

## Chemistry, drug discovery and materials

Install `chemistry-and-drug-discovery` for molecule handling and computational chemistry. Start with
[`rdkit`](/skills/rdkit) for cheminformatics, [`deepchem`](/skills/deepchem)
for molecular machine learning and [`molecular-dynamics`](/skills/molecular-dynamics)
for simulation workflows. Materials researchers can add [`pymatgen`](/skills/pymatgen).

## Clinical and health research

Install `clinical-and-health` for research workflows involving medical images, biomedical datasets and
clinical reporting. [`pydicom`](/skills/pydicom) helps inspect DICOM data,
[`pathml`](/skills/pathml) covers computational pathology, and
[`clinical-reports`](/skills/clinical-reports) helps structure research reports. Check
institutional rules before sharing patient data with any agent or external service.

## Physics, astronomy and earth science

Install `physical-sciences` for scientific computing in these fields. [`astropy`](/skills/astropy)
handles astronomy data and coordinates, [`qiskit`](/skills/qiskit) supports quantum circuits,
[`pymatgen`](/skills/pymatgen) covers materials analysis, and
[`geopandas`](/skills/geopandas) supports geospatial research.

## Psychology, social science and statistics

Start with `research-essentials` and `data-science-and-ml`. Use
[`experimental-design`](/skills/experimental-design) for study plans,
[`statistical-power`](/skills/statistical-power) for sample-size reasoning,
[`statistical-analysis`](/skills/statistical-analysis) for analyses, and
[`apa7`](/skills/apa7) for APA-formatted manuscripts. For evidence synthesis, follow the
[systematic review guide](/guides/systematic-review).

## AI and machine learning research

Install the relevant `ml-training`, `ml-evaluation-and-safety`, `ml-inference-and-ops`, or
`multimodal-and-emerging` category. [`ml-paper-writing`](/skills/ml-paper-writing)
covers ML conference papers; [`evaluating-llms-harness`](/skills/evaluating-llms-harness)
addresses model evaluation; [`pytorch-fsdp2`](/skills/pytorch-fsdp2) covers distributed training.
Use [`reproducibility-statement`](/skills/reproducibility-statement) to document experimental details.

## Lab automation and research operations

Install `lab-automation` for supported instruments and protocol systems. Start with
[`opentrons-integration`](/skills/opentrons-integration),
[`pylabrobot`](/skills/pylabrobot), or
[`protocolsio-integration`](/skills/protocolsio-integration), depending on your equipment
and workflow. Review generated protocols before executing them in a lab.

Browse every skill in the [catalog](/skills). Missing your field? [Request a skill](https://github.com/KalarisLabs/research-agent-skills/issues/new/choose).

For paper discovery across fields, [`firecrawl-research-index`](/skills/firecrawl-research-index)
queries Firecrawl's hosted paper index. For questions over PDFs already in your lab,
use [`paper-corpus-rag`](/skills/paper-corpus-rag).
