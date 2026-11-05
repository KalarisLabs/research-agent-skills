---
title: OpenSSF Scorecard maintenance
description: What raises the repository's OpenSSF Scorecard and which steps need a repository admin.
---

# OpenSSF Scorecard maintenance

Live score: https://securityscorecards.dev/viewer/?uri=github.com/KalarisLabs/research-agent-skills
(the `scorecard.yml` workflow publishes it on every push to `main` and weekly).

## Baseline (2026-10-20): 6.9

| Check | Score | Why | Fix |
|---|---:|---|---|
| Dangerous-Workflow, Token-Permissions, Pinned-Dependencies, Packaging | -1 (not counted) | `.gitattributes` marked `/.github` and `/cli` `export-ignore`, and Scorecard reads the repository through GitHub's source tarball, so it saw no workflows | Fixed in code: release tarballs now exclude dev paths with `git archive` pathspecs in `release.yml` instead |
| Fuzzing | 0 | No fuzzer detected | Fixed in code: `fast-check` property tests in `cli/test/fuzz.test.mjs` (tar parser, archive paths, SHA256SUMS, argv) |
| Signed-Releases | 8 | No provenance file among release assets | Fixed in code: `release.yml` attaches the SLSA bundle as `*.intoto.jsonl` (takes effect from the next release) |
| Branch-Protection | 0 | No protection on `main` | **Admin step 1** |
| Code-Review | 2 | 7 of the last 27 changesets had an approving review | **Admin step 1**, then a second maintainer approves every PR |
| CII-Best-Practices | 0 | No OpenSSF Best Practices badge | **Admin step 2** |
| Contributors | 6 | Contributors from 2 organizations | Grows with outside contributions; no action |
| SAST | 9 | CodeQL did not run on every commit | Grows as all changes go through PRs |

Expected after the code fixes alone: about 7.5. After the admin steps, and once about 30 reviewed PRs have
merged: about 9.2.

## Admin step 1: protect `main` with a ruleset

Settings → Rules → Rulesets → New branch ruleset, target the default branch:

- Restrict deletions; block force pushes.
- Require a pull request before merging: 1 required approval, dismiss stale approvals on new commits,
  require review from Code Owners, require conversation resolution.
- Require status checks to pass: the jobs of the `Validate skills`, `Tests`, `Skill security` and `Benchmarks`
  workflows (for example `Spec, catalog and brand checks` and `Skill quality and trigger routing`). Pick them from
  the list GitHub offers after one PR has run.
- Do not add a bypass list. Admins bypassing the ruleset lowers the score.

Code-Review counts only changesets with an approval from someone other than the author, so each PR needs
a second maintainer's approval. The score rises as reviewed PRs replace the last 30 changesets.

## Admin step 2: OpenSSF Best Practices badge

The project is registered at https://www.bestpractices.dev/projects/15771 and the badge is in the README. Enter the
answers from [`best-practices-answers.md`](/maintainers/best-practices-answers) level by level: Passing first (Scorecard
scores the check 5), then Silver (7). Gold (10) needs more than code: a second unassociated contributor, a bus factor
of 2, two-person review on every change, enforced 2FA and a third-party security review.

## Verify

```bash
curl -s https://api.securityscorecards.dev/projects/github.com/KalarisLabs/research-agent-skills \
  | python3 -c "import json,sys; d=json.load(sys.stdin); print(d['score']); [print(c['score'], c['name']) for c in d['checks']]"
```
