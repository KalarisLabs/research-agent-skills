"""Tests for tools/claim_audit.py: a SKILL.md may only promise what its scripts do."""
# ruff: noqa: E501

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import claim_audit  # noqa: E402

SKILL = """---
name: demo
description: {description}
compatibility: {compat}
---

# Demo

```bash
python scripts/check.py refs.bib --annotate
python scripts/check.py refs.bib --nonexistent
```

| Status | Meaning |
|---|---|
| `verified` | ok |
| `retracted` | retracted |

Also see `systematic-review-prisma/scripts/other.py` and run `python scripts/ghost.py`.
"""

SCRIPT = '''
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("--annotate")
HOST = "https://api.crossref.org/works"
STATUSES = ["verified"]
'''


def make(tmp_path: Path, description="Queries Crossref and DataCite.", compat="Needs api.crossref.org and api.datacite.org.") -> Path:
    d = tmp_path / "demo"
    (d / "scripts").mkdir(parents=True)
    (d / "SKILL.md").write_text(SKILL.format(description=description, compat=compat), encoding="utf-8")
    (d / "scripts" / "check.py").write_text(SCRIPT, encoding="utf-8")
    return d


def kinds(findings):
    return {(f["kind"], f["token"]) for f in findings}


def test_each_unsupported_claim_is_reported(tmp_path):
    found = kinds(claim_audit.audit_skill(make(tmp_path)))
    assert ("missing-flag", "--nonexistent") in found
    assert ("missing-script", "ghost.py") in found
    assert ("missing-host", "api.datacite.org") in found
    assert ("missing-service", "datacite") in found
    assert ("missing-status", "retracted") in found


def test_supported_claims_are_not_reported(tmp_path):
    found = kinds(claim_audit.audit_skill(make(tmp_path)))
    assert ("missing-flag", "--annotate") not in found
    assert ("missing-host", "api.crossref.org") not in found
    assert ("missing-service", "crossref") not in found
    assert ("missing-status", "verified") not in found
    assert not any(token == "other.py" for _, token in found)  # another skill's script path is not this skill's claim


def test_service_claim_only_applies_to_querying_sentences(tmp_path):
    d = make(tmp_path, description="Plan reviews. Use when searching PubMed by hand and citing Zenodo.", compat="Python 3.9+")
    assert not [f for f in claim_audit.audit_skill(d) if f["kind"] == "missing-service"]


def test_skill_without_scripts_makes_no_host_or_status_claims(tmp_path):
    d = make(tmp_path)
    for f in (d / "scripts").iterdir():
        f.unlink()
    assert not [f for f in claim_audit.audit_skill(d) if f["kind"] in ("missing-host", "missing-status", "missing-service")]


def test_ignore_list_suppresses_listed_findings(tmp_path, monkeypatch, capsys):
    d = make(tmp_path)
    ignore = tmp_path / "ignore.txt"
    ignore.write_text("\n".join(f"demo:{k}:{t}  # reason" for k, t in kinds(claim_audit.audit_skill(d))), encoding="utf-8")
    monkeypatch.setattr(claim_audit, "IGNORE_FILE", ignore)
    assert claim_audit.main([str(d)]) == 0
    monkeypatch.setattr(claim_audit, "IGNORE_FILE", tmp_path / "none.txt")
    assert claim_audit.main([str(d)]) == 1


@pytest.mark.parametrize("name", ["citation-verification", "paper-corpus-rag", "paper-card", "fulltext-acquisition",
                                  "systematic-review-prisma", "unslop-academic-writing"])
def test_shipped_skills_keep_their_promises(name):
    assert claim_audit.audit_skill(claim_audit.SKILLS_DIR / name) == []


def test_every_original_skill_is_clean():
    assert claim_audit.main([]) == 0


def test_eval_floor_flags_thin_eval_suites(tmp_path, monkeypatch):
    import validate

    root = tmp_path
    (root / "evals" / "demo").mkdir(parents=True)
    skill = root / "skills" / "demo"
    (skill / "scripts").mkdir(parents=True)
    monkeypatch.setattr(validate, "ROOT", root)

    def run(evals, baseline=frozenset()):
        (root / "evals" / "demo" / "evals.json").write_text(json.dumps({"evals": evals}), encoding="utf-8")
        rep = validate.Report()
        validate.check_eval_floor(skill, rep, {"demo"}, set(baseline))
        return rep

    thin = [{"id": 1, "prompt": "x"}]
    assert run(thin).errors and not run(thin).warnings
    assert run(thin, {"demo"}).warnings and not run(thin, {"demo"}).errors
    full = [{"id": i, "prompt": "x"} for i in range(7)] + [{"id": 9 + i, "prompt": "y", "should_trigger": False} for i in range(3)]
    assert not run(full).errors
    rep = validate.Report()
    validate.check_eval_floor(skill, rep, set(), set())  # imported skills are exempt
    assert not rep.errors
