# Contributing to Research Agent Skills

Thanks for helping researchers work faster and more rigorously. This guide covers
adding a skill, improving one, and the checks your pull request must pass.

## Ground rules

- **Accuracy over breadth.** Every factual claim (venue limits, API behavior, statistical
  advice) must be correct and, where it changes over time, point to the official source.
- **Never fabricate** citations, data, results, or tool capabilities in skills or examples.
- **Original work only.** Write skills yourself. Don't paste text from other skill
  collections, books or paywalled guides. By contributing you agree to license your
  contribution under the repository's MIT license.
- **Security first.** No obfuscated code, no network calls to undeclared domains, no
  credential access, no instructions that hide actions from the user.

## Add a new skill

1. Check `catalog/skills.json` for overlap. Improving an existing skill beats adding a near-duplicate.
2. Scaffold (writes spec-compliant frontmatter and an eval stub):

   ```bash
   python skills/research-skill-creator/scripts/new_skill.py my-skill \
     --category literature-review --description "What it does. Use when ..." --scripts
   ```

3. Follow `skills/research-skill-creator/SKILL.md` for structure, description writing, script conventions and testing.
   Anthropic's official `skill-creator` (`/plugin marketplace add anthropics/skills`) runs the eval loop.
4. Categories are defined in `third_party/categories.yaml`. Propose a new one in your PR if none fits.

## What we accept

A contribution is accepted when it meets all of these:

- **Scope:** one skill or one focused change per pull request, with a clear reason in the description.
- **Coding standard:** Python follows the ruff rules in `pyproject.toml` (line length 120, rule sets E, F, W, I, B, UP, S),
  TypeScript compiles under `cli/tsconfig.json`, and `.editorconfig` sets whitespace and line endings. CI runs ruff and the
  compiler on every pull request, so a failing check is the whole standard; `make lint` runs it locally.
- **Checks:** every CI check passes, including the skill requirements below and the security scans described in
  [SECURITY.md](SECURITY.md).
- **Tests:** see [Tests](#tests).
- **Licence and origin:** your own work, licensed under MIT (see the ground rules).
- **Review:** one maintainer approves. Changes under `.github/`, `security/`, the installers and the CLI need the
  lead maintainer (see [`.github/CODEOWNERS`](.github/CODEOWNERS)).

## Tests

New functionality ships with automated tests, and bug fixes ship with a regression test that fails without the fix.

- Python tooling in `tools/` and skill scripts: add tests in `tests/` and run `uv run python -m pytest -q --cov`.
  Statement coverage of `tools/` must stay at or above 80% (`[tool.coverage.report]` in `pyproject.toml`).
- The installer CLI in `cli/`: add tests in `cli/test/` and run `cd cli && npm test && npm run test:coverage`.
  Line and branch coverage must stay at or above 80%. Parsers that read untrusted input also get a property-based
  test in `cli/test/fuzz.test.mjs`.
- New skills need `evals/<name>/evals.json` (see the table below). Skill scripts need an offline smoke test.

Pull requests that add code without tests are asked to add them before merge. The pull request template has a
checkbox for this.

## Skill requirements (enforced by CI)

| Requirement | Tool |
|---|---|
| Frontmatter: `name` (kebab-case, ≤64, equals folder), `description` (≤1024 chars, includes "Use when"), only spec fields at top level, `metadata.version/category/maintainer` as strings | `tools/validate.py`, `skills-ref` |
| `SKILL.md` ≤ 500 lines; long material in `references/` | `tools/validate.py` |
| Allowed file types only; ≤ 2 MiB per file, ≤ 15 MiB per skill; no symlinks; UTF-8 text | `tools/validate.py` |
| Relative links resolve and stay inside the skill | `tools/validate.py` |
| No prompt-injection patterns, hidden Unicode, encoded blobs, pipe-to-shell, credential access | `tools/lint_injection.py`, Cisco skill-scanner |
| Script network access only to domains in `security/allowed-domains.txt` | `tools/lint_injection.py` |
| Generated files up to date | `tools/build_catalog.py --check` |
| Quality rubric ≥ 80 for new skills (structure, triggers, verification rules, tested scripts) | `tools/skill_quality.py` |
| Evals in `evals/<name>/evals.json`; the skill is picked for its prompts and not for near misses | `tools/trigger_bench.py` |

Run everything locally before pushing (`make check` does all of this):

```bash
uv sync
uv run tools/validate.py skills/my-skill
uv run tools/lint_injection.py skills/my-skill
uv run tools/skill_quality.py my-skill
uv run tools/trigger_bench.py
uv run tools/build_catalog.py          # regenerates marketplace, catalog, README tables, llms.txt
uv run python -m pytest -q
```

Optional but encouraged: `pre-commit install` to run these checks on every commit, and
`benchmarks/task_evals/run.py --skills my-skill` to show the skill improves answers (see `benchmarks/README.md`).

## Scripts

Python 3.9+ standard library preferred (declare any dependency in `compatibility`), `argparse`
CLI with `--help`, exit codes `0/1/2`, UTF-8 console setup for Windows, descriptive `User-Agent`
for HTTP, timeouts on every request, no `eval`/`exec` of fetched data. Add an offline smoke test
in `tests/` when the script is non-trivial.

## Pull requests

- One skill or one focused change per PR. Fill in the PR template checklist.
- Changes to `skills/**/scripts/**`, `security/**`, `.github/**`, installers and the CLI require maintainer review (CODEOWNERS).
- Commit messages: imperative mood ("Add systematic review skill"). Reference issues.
- Be kind in reviews. See [CODE_OF_CONDUCT.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/CODE_OF_CONDUCT.md).

## Adapted skills

Some skills are adapted from MIT-licensed upstream projects (see `THIRD_PARTY_NOTICES.md`).
They are refreshed with `uv run tools/import_upstream.py` from pinned revisions. Fixes to
them go in `third_party/patches/` as patch files, so re-imports keep them. Full rewrites
are welcome: see "Rewriting an adapted skill" in the research-skill-creator skill.

## Maintainers

Created and maintained by **Sayan Chowdhury** at **Kalaris Labs**.
