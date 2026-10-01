---
title: No-slop academic writing | make AI-assisted research papers read like a human expert wrote them
description: How the unslop-academic-writing skill detects AI slop in academic prose (stock phrasing, empty emphasis, hedge stacks, monotone rhythm) and rewrites toward specific, evidence-backed writing in the author's voice.
---

# No-slop academic writing

"AI slop" is fluent text that says less than it seems to: *delves into the intricate tapestry*,
*plays a pivotal role*, *it is important to note that*, three stacked hedges, and every sentence the same
length. Reviewers recognize it immediately and trust the paper less.

The `unslop-academic-writing` skill fixes this with a linter and an editing playbook.

## How it works

1. **Measure.** `python scripts/slop_check.py draft.tex` ignores math, citations and code, then reports each
   problem with a line number and rewrite hint, plus a slop index (under 5 is clean, over 30 is severe).
2. **Fix content before words.** Replace vague claims with numbers, tie claims to evidence, and cut paragraphs that restate the field.
3. **Fix the words.** Delete framing phrases, replace stock vocabulary, keep one hedge sized to the evidence, and use normal punctuation.
4. **Keep your voice.** The skill calibrates to a sample of your own writing and your discipline's norms.
5. **Re-measure and read aloud.**

## What it detects

| Category | Examples |
|---|---|
| Chat residue | "Certainly!", "Here is a revised version", "As an AI language model" |
| Stock vocabulary | delve, tapestry, realm, pivotal role, underscores the importance, leverage, showcase |
| Promotional / empty emphasis | groundbreaking, unprecedented, remarkably, truly |
| Unsupported "significant" | "significantly better" with no statistical test nearby |
| Filler and signposting | "It is important to note that", "In order to", "In conclusion," |
| Constructions | "not only X but also Y", "it's not X, it's Y" |
| Hedge stacks | "may potentially", "could possibly suggest" |
| Rhythm | uniform sentence and paragraph lengths, transition-word openers, em-dash pileups |

## Does it work?

See the slop benchmark on the [benchmarks page](/reference/benchmarks). In short: with the skill in context, model-written
abstracts had a much lower slop index and more of them scored "clean". The linter is a checklist for
recognizable slop, **not an AI detector**, and it cannot tell careful modern model output from human writing.

!!! note "Integrity"
    This skill improves clarity and authorship. It is not a tool for hiding AI use. Follow your venue's disclosure policy.
