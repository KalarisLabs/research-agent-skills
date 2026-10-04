---
title: Medical and clinical research skills
description: Agent skills for DICOM imaging, pathology, health datasets and evidence synthesis in medical research.
---

# Medical and clinical research

These skills support research workflows. Check your institution's data rules before giving an agent access to patient information, and review clinical interpretations with qualified domain experts.

| Task | Skill | Research starting point |
|---|---|---|
| Inspect imaging metadata | [`pydicom`](/skills/pydicom) | Use de-identified DICOM files and verify pixel handling |
| Analyze pathology images | [`pathml`](/skills/pathml) | Document stain, scanner and slide-level split |
| Work with health ML datasets | [`pyhealth`](/skills/pyhealth) | Define cohort, outcome and leakage controls |
| Structure a research report | [`clinical-reports`](/skills/clinical-reports) | Provide verified findings and intended audience |
| Plan an evidence review | [`systematic-review-prisma`](/skills/systematic-review-prisma) | Specify question, eligibility and search strategy |

```bash
npx skills add KalarisLabs/research-agent-skills --skill systematic-review-prisma
```

Try: “Draft a PRISMA protocol for this research question. List databases, screening rules and outcomes before any search begins.” Continue with the [systematic review guide](/guides/systematic-review) and [citation verification](/skills/citation-verification).
