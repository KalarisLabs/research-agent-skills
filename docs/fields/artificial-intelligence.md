---
title: AI research skills for agents and language models
description: Agent skills for LLM evaluation, interpretability, safety checks and clear AI research reporting.
---

# Artificial intelligence research

For agent and language-model studies, define the behavior you want to measure before asking an agent to run or summarize evaluations. Preserve prompts, model versions, judge settings and raw outputs so a reader can reproduce your conclusions.

| Task | Skill | Starting point |
|---|---|---|
| Compare model or agent behavior | [`evaluating-llms-harness`](/skills/evaluating-llms-harness) | Define cases, metrics and human review criteria |
| Inspect model mechanisms | [`transformer-lens-interpretability`](/skills/transformer-lens-interpretability) | State a hypothesis and select an interpretable model |
| Assess adversarial inputs | [`prompt-guard`](/skills/prompt-guard) | Include benign and attack examples, plus false positive checks |
| Report an AI study | [`ml-paper-writing`](/skills/ml-paper-writing) | Provide methods, ablations and uncertainty estimates |

```bash
npx skills add KalarisLabs/research-agent-skills --skill evaluating-llms-harness
```

Try: “Design an evaluation for our retrieval agent using the cases in `evals/`. Specify failure categories, scoring rules and which results require a human reviewer.” For training and reproducibility, see [machine learning research](/fields/machine-learning).
