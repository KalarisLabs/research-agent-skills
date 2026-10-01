# Governance

## Roles

- **Lead maintainer:** Sayan Chowdhury ([@saynchowdhury](https://github.com/saynchowdhury)), Kalaris Labs. Sets direction, owns releases and security response.
- **Maintainers:** listed in `.github/CODEOWNERS`. Review and merge pull requests in their areas.
- **Domain reviewers:** researchers who review skills in their field for scientific accuracy. Ask in Discussions to join.
- **Contributors:** anyone who opens an issue or pull request.

## Decisions

Day-to-day changes merge after one maintainer approval and green CI. Changes to security controls
(`security/`, `.github/workflows/`, installers, CLI), the skill format, or categories need approval
from the lead maintainer. Disagreements are resolved in the pull request or a Discussion, and the lead maintainer decides if consensus is not reached.

## Quality bar for skills

A skill is merged when it passes CI (validation, security scans, quality rubric ≥ 80 for new skills,
trigger benchmark) and a domain reviewer confirms its guidance is accurate. See
[benchmarks/README.md](benchmarks/README.md) for how skills are evaluated.

## Releases

Semantic versioning. Releases are tagged by the lead maintainer. Artifacts are built, checksummed, attested
and signed by CI (see [SECURITY.md](SECURITY.md)). Notable changes are recorded in [CHANGELOG.md](CHANGELOG.md).
