# Benchmarks and skill quality

A skill only helps if it is **well written**, **selected** for the right requests, and
**improves the outcome** when used. We measure all three, plus dedicated benchmarks for
skills whose correctness can be checked mechanically.

| Tier | Question | Tool | Cost | Runs |
|---|---|---|---|---|
| 1. Static quality | Is the skill written to a professional standard? | `tools/skill_quality.py` | free | every PR (gate: original skills ≥ 80) |
| 2. Trigger routing | Is the right skill picked for a request, and not for near misses? | `tools/trigger_bench.py` | free (BM25) / paid (Claude router) | reviewed evals on every PR (gate: hit@3 ≥ 0.9, false-trigger ≤ 0.15) |
| 3. Task outcomes | Are answers better with the skill than without? | `benchmarks/task_evals/run.py` | paid | manual (`benchmarks.yml` dispatch) |
| Domain | Does the skill's tool do its job? | `benchmarks/citation_verification/`, `benchmarks/slop/` | network / paid | weekly / manual |

## Current results

Results are committed in [`results/`](https://github.com/KalarisLabs/research-agent-skills/blob/main/benchmarks/results). Model-based numbers are **pilots**: small samples and a
small model, so treat them as indicative. Rerun with larger models and samples before quoting them.

### 1. Static quality rubric

| Scope | Skills | Mean | Min | ≥ 85 |
|---|---:|---:|---:|---:|
| Original skills | 24 | 95.5 | 82 | 23 |
| Adapted skills | 257 | 95.2 | 80 | 256 |
| All skills | 281 | 95.2 | 80 | 279 |

Full table: [`results/skill-quality.md`](https://github.com/KalarisLabs/research-agent-skills/blob/main/benchmarks/results/skill-quality.md). The report lists concrete fixes per skill
(e.g. missing "Use when" triggers, no numbered workflow, broken reference links).

**How adapted skills went from 80.9 to 95.2.** The import pipeline now enriches every adapted skill reproducibly:
- 84 descriptions rewritten with explicit "Use when" triggers and named tools (`third_party/description-overrides.yaml`).
- 31 oversized `SKILL.md` files split into `references/`, so every skill is within the 500-line budget.
- 80 dead links repaired.
- Popularity and marketing lines stripped, such as GitHub star counts and user numbers.
- A category-specific agent operating procedure added where a workflow, decision table or verification
  rules were missing (186 skills): environment check, small first run, validation, failure-recovery
  table and integrity rules (`third_party/operating-procedures.yaml`).
- Related-skill handoffs computed from description similarity (216 skills).

The procedures are written per category, not per skill. Part of the score gain therefore reflects consistent structure
rather than new domain content, and per-skill rewrites remain the path to deeper quality.

### 2. Trigger routing

| Router | Prompts | hit@1 | hit@3 | False-trigger |
|---|---:|---:|---:|---:|
| BM25, reviewed evals (PR gate) | 53 | 1.00 | 1.00 | 0.12 |
| BM25, all evals incl. generated (281 skills) | 1,335 | 0.50 | 0.65 | 0.07 |
| BM25, random sample of all evals (seed 7) | 100 | 0.65 | 0.77 | 0.04 |
| Claude Haiku 4.5 router, same sample | 100 | 0.92 | 0.96 | 0.00 |

Every skill now has an eval suite in `evals/<skill>/evals.json`: 3 realistic prompts plus 1-2 near misses that name
the better skill. Suites for adapted skills were generated from each skill's `SKILL.md` and are marked
`pending review`. The generated prompts deliberately avoid the description's wording and often describe the goal
without naming the tool, so keyword routing struggles (hit@3 0.65) while an LLM router, which is how agents actually
choose skills, reaches 0.96 with no false triggers on the sample.
Results: [`trigger-bm25-all-evals.json`](https://github.com/KalarisLabs/research-agent-skills/blob/main/benchmarks/results/trigger-bm25-all-evals.json),
[`trigger-claude-sample100.json`](https://github.com/KalarisLabs/research-agent-skills/blob/main/benchmarks/results/trigger-claude-sample100.json).

The benchmark already paid off: it exposed that "write a job application cover letter" triggered
`cover-letter-to-editor`, and the description was fixed. BM25 cannot read negations ("not for job
letters"), so its residual false triggers are an upper bound. The Claude router is the realistic measure.
Generated evals marked `pending review` are excluded from the PR gate. Run
`uv run tools/trigger_bench.py --include-pending` to inspect them before review.

### 3. Task outcomes (with vs without skill, blind judge)

<!-- task-evals:start -->
Pilot: 23 prompts across the 22 original skills. Answers and judge from Claude Haiku 4.5, answer order randomized,
tools disabled, and skills disabled for the baseline ([`task-evals-pilot-haiku.json`](https://github.com/KalarisLabs/research-agent-skills/blob/main/benchmarks/results/task-evals-pilot-haiku.json)).

| Skill wins | Baseline wins | Mean judge score with skill | without skill | Mean delta |
|---:|---:|---:|---:|---:|
| 21 / 23 | 2 / 23 | 7.4 | 4.3 | +3.1 |

What the losses taught us:
- `elsevier-cas` initially lost because the baseline produced a complete template and the skill only pointed to one.
  We added a full CAS skeleton, and the rerun flipped to a win (8 vs 5).
- `cell-press` loses narrowly because the judge rewards concrete character limits, while the skill deliberately tells the agent to
  verify current limits instead of quoting remembered ones. We keep this trade-off for accuracy.
- `plos`: judge preference on how strictly PLOS's data policy was worded.

Caveats: one small model for both answering and judging, one to two prompts per skill, and LLM-judge bias.
Rerun with a stronger answer model, a different judge model and more prompts before citing these numbers.
<!-- task-evals:end -->

### Citation verification (`citation-verification`)

18 labeled references: 10 correct (8 with DOI, 2 DOI-less arXiv/NeurIPS), 4 corrupted (wrong DOI, wrong year,
wrong first author, DOI typo) and 4 fabricated.

| Precision | Recall | Correct entries passed | Bad entries flagged |
|---:|---:|---:|---:|
| 1.00 | 1.00 | 10 / 10 | 8 / 8 |

### No-slop writing (`unslop-academic-writing`)

Human baseline: 40 open-access CC BY abstracts published 2012-2018 (before LLM writing assistants), fetched from
Europe PMC across 10 fields. AI conditions: abstracts written by Claude Haiku 4.5 for the same titles, plainly
and with the skill in context (n = 19 each).

| Condition | Mean slop index | Share scoring "clean" (< 5) |
|---|---:|---:|
| Human abstracts (2012-2018) | 2.9 | 78% |
| Model, no skill | 5.0 | 68% |
| Model, with skill | 0.8 | 89% |

- **Skill effect:** mean slop index 83% lower with the skill in context.
- **Linter as a detector:** AUROC 0.54 for separating plain model output from human abstracts, close to chance.
  The linter flags *recognizable slop patterns*. It is **not an AI-text detector**, and careful modern model output
  often contains none of the patterns. Human abstracts also trip some rules (e.g. "significantly" without a test).
- **Caveat:** the same human set was used to calibrate short-text thresholds. Validate on a fresh fetch
  (different fields and years) and longer genres (introductions, discussions) before drawing conclusions.

## External benchmarks worth running

For end-to-end research capability, pair these internal checks with published benchmarks:

- **SkillsBench** ([arXiv:2602.12670](https://arxiv.org/abs/2602.12670)): measures how much curated skills help agents
  across 86 tasks with deterministic verifiers, using the same no-skill / curated-skill comparison as tier 3.
- **BixBench** ([arXiv:2503.00096](https://arxiv.org/abs/2503.00096)): open-ended bioinformatics analyses, a good fit for the `life-sciences` skills.
- **ReplicationBench** ([arXiv:2510.24591](https://arxiv.org/abs/2510.24591)): replicating astrophysics papers, relevant to `physical-sciences` and reproducibility skills.
- **ScienceAgentBench**, **DiscoveryBench**, **LAB-Bench**, **CORE-Bench** and **PaperBench**: data-driven discovery,
  hypothesis search, biology research skills, computational reproducibility and paper replication.

A useful protocol: run the agent on a benchmark subset with no skills, then with the relevant category installed,
and report the difference. That mirrors SkillsBench's design.

## Running the benchmarks

```bash
make quality            # tier 1 report + gate
make bench-triggers     # tier 2 (BM25)
uv run tools/trigger_bench.py --router claude --model claude-sonnet-5-5     # tier 2 (paid)
make bench-citations    # citation precision/recall (network)
make bench-slop         # human vs model abstracts, with/without skill (paid generation step)
make bench-tasks        # tier 3 (paid)
```

Paid steps use the Claude Code CLI (`claude -p`) with your login or `ANTHROPIC_API_KEY`, skills disabled for the
baseline, and tools disabled in both conditions. In CI they run only on manual dispatch of `benchmarks.yml`
with the `ANTHROPIC_API_KEY` secret in the `benchmarks` environment.

## Adding evals for a skill

Create `evals/<skill>/evals.json` (the format used by Anthropic's skill-creator):

```json
{"skill_name": "my-skill", "evals": [
  {"id": 1, "prompt": "A realistic request that should use the skill", "expected_output": "What a strong answer contains", "files": []},
  {"id": 2, "prompt": "A near miss that should not", "expected_output": "Skill not used", "files": [], "should_trigger": false}
]}
```

Aim for 3-10 prompts per skill, phrased the way researchers actually ask, with at least one near miss.
