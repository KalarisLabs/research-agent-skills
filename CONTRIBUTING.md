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
