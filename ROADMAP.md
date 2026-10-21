# Roadmap

What we plan to work on over the next 12 months. Dates are intentions, not promises. Changes to this plan are
proposed in a pull request or a [Discussion](https://github.com/KalarisLabs/research-agent-skills/discussions).
See [GOVERNANCE.md](GOVERNANCE.md) for how decisions are made.

## Next 3 months

- **Review the generated evals.** Eval suites for adapted skills are marked `pending review`. Review them with domain
  experts so they can join the pull-request gate in [`benchmarks/README.md`](benchmarks/README.md).
- **Larger benchmark runs.** Rerun the task-outcome and routing benchmarks with a stronger answer model, a different
  judge model and more prompts. Current numbers are pilots and say so.
- **OpenSSF Best Practices.** Reach the passing, then silver, badge level and keep the
  [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/KalarisLabs/research-agent-skills) at 9 or higher
  (steps in [`docs/maintainers/scorecard.md`](docs/maintainers/scorecard.md)).

## 3 to 12 months

- **Rewrite adapted skills.** Replace adapted skills with original, field-reviewed ones, starting with the most-used
  categories. Rewrites go through the same quality rubric and evals.
- **Domain reviewers.** Recruit researchers per field to review skills for scientific accuracy and to co-maintain.
- **More end-to-end case studies.** Publish studies produced with the skills, with the claims, numbers and limits
  stated, like the [fly-brain case study](docs/guides/case-study-fly-brain.md).
- **Broader harness coverage.** Keep installation tested against new agent harnesses that read the Agent Skills format.

## Not planned

- Features that need a hosted service or an account. The skills stay plain files that work offline.
- Skills that hide actions from the user or send data to undeclared domains.
