---
title: "Case study: a whole-brain fly simulation study run with Research Agent Skills"
sidebarTitle: "Case study: fly brain"
description: How Claude, working through Research Agent Skills, took a connectome-constrained Drosophila study from preregistered hypotheses to a 30-page paper, with verified citations and a falsified hypothesis reported as such.
---

# Case study: reviving a model fly brain

[Reviving a model fly brain](https://github.com/KalarisLabs/fly-brain-resuscitation) is a Kalaris Labs preprint on
anoxia, brain death and resuscitation in a connectome-constrained simulation of the whole adult *Drosophila* brain
(139,255 neurons, FlyWire FAFB v783). Claude worked through Research Agent Skills and Kalaris Labs Myriad under the
author's direction, from the first hypothesis to the finished paper. The paper discloses this, and Claude is not an
author.

![Simulated adult fly brain during the reperfusion runaway](https://raw.githubusercontent.com/KalarisLabs/fly-brain-resuscitation/main/assets/banner.png)

## What the skills did at each stage

| Stage | Output | Skill and evidence |
|---|---|---|
| Question | 6 preregistered hypotheses with rival explanations, discriminating predictions and falsification thresholds, frozen before any simulation ran | `hypothesis-generation` v2.2, cited in the [preregistration](https://github.com/KalarisLabs/fly-brain-resuscitation/blob/main/docs/HYPOTHESES.md) |
| Literature | 82 Crossref-verified sources; an 81-row parameter table with 6 values flagged `UNVERIFIED` | `citation-verification` rule: 2 DOIs that resolved to unrelated papers were discarded ([bibliography](https://github.com/KalarisLabs/fly-brain-resuscitation/blob/main/docs/lit/bibliography.md)) |
| Experiments | 3,487 analysed condition-seed runs: structure in 4 connectomes, dynamics in 2 (FAFB, MCNS) | Preregistered analysis plan. Graded reperfusion (H3) was falsified, direction reversed, and reported |
| Output | 30-page paper, supplement, 19 figures, narrated explainers, unit-tested code | Headline claims listed with source file, number and confidence in [`KEY_CLAIMS.json`](https://github.com/KalarisLabs/fly-brain-resuscitation/blob/main/paper/KEY_CLAIMS.json) |

## Headline results

These follow the study's `KEY_CLAIMS.json`, with its numbers and confidence levels.

- Abrupt reoxygenation can trap the model brain in a self-sustained K⁺-coupled high-activity state. After 180 s of
  anoxia this happened in 48/48 FAFB parameter sets and 5/5 MCNS runs (confidence high). After 30 s it is
  sign-sensitive: with antennal-lobe local neurons inhibitory, 0/3 FAFB runs ran away (confidence moderate).
- A 20-second total activity block at reperfusion restored the stimulus-response map (FAFB FII<sub>norm</sub> 1.001
  and 0.953 at 30 and 180 s of anoxia); 2–5 s blocks failed (confidence high).
- Graded (ramped or pulsed) reperfusion did not beat abrupt reperfusion plus a block, so the preregistered H3 was
  falsified (confidence high within the model).

<Warning>
All results are predictions of a simplified simulation (connectome-constrained LIF neurons and phenomenological
metabolism, constants not fitted to *Drosophila*). They are not evidence about living tissue, clinical brain death or
human resuscitation, and resuscitation of a brain-dead organism has not been demonstrated.
</Warning>

## Run the same workflow

Install the skills the study relied on and ask your agent in plain language:

```bash
npx skills add KalarisLabs/research-agent-skills --skill hypothesis-generation citation-verification
```

```text
"Preregister hypotheses for this question, with rivals, falsification thresholds and an analysis plan."
"Verify every DOI in bibliography.md against Crossref and drop any that resolve to a different paper."
```

## Next steps

- [Write a research paper](/guides/write-a-research-paper)
- [Benchmarks](/reference/benchmarks)
