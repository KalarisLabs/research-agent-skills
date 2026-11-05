---
title: Machine learning research skills
description: Select agent skills for ML experiments, model evaluation, reproducibility and conference paper writing.
---

# Machine learning research

Use a skill that matches the stage of your experiment. Keep datasets, training code and metrics as the source of truth; ask the agent to identify missing evidence before it drafts claims.

| Task | Skill | What to provide |
|---|---|---|
| Plan or report a model evaluation | [`evaluating-llms-harness`](/skills/evaluating-llms-harness) | Task definitions, evaluation set and scoring rules |
| Train across multiple GPUs | [`pytorch-fsdp2`](/skills/pytorch-fsdp2) | Model, hardware, checkpoint and memory constraints |
| Write a conference paper | [`ml-paper-writing`](/skills/ml-paper-writing) | Results, baselines, figures and target venue |
| Document repeatability | [`reproducibility-statement`](/skills/reproducibility-statement) | Seeds, splits, compute budget, code and data access |

Install one skill into your current project:

```bash
npx skills add KalarisLabs/research-agent-skills --skill ml-paper-writing
```

Try: “Use the results in `runs/` and the comparison table to outline an ML paper. Mark every claim that needs another experiment.” Check the current venue requirements before submission. For interpretability work, also see [AI research](/fields/artificial-intelligence).
