## What does this change?

<!-- One or two sentences. Link related issues. -->

## Checklist

- [ ] `uv run tools/validate.py` passes for affected skills
- [ ] `uv run tools/lint_injection.py` reports no new findings
- [ ] `uv run tools/build_catalog.py` run and generated files committed
- [ ] Facts that change over time (venue limits, APIs) point to official sources
- [ ] No fabricated citations, data or tool capabilities
- [ ] Scripts: stdlib-first, `--help`, exit codes 0/1/2, timeouts, new domains added to `security/allowed-domains.txt`
- [ ] Written by me (not copied from other skill collections); I agree to license it under MIT
