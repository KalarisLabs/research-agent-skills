"""Offline smoke tests for scripts shipped in original skills (run on every OS in CI)."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest
from common import SKILLS_DIR

BIB = """@article{lecun2015deep, title={Deep learning in NLP}, author={LeCun, Yann and Bengio, Yoshua},
  journal={Nature}, year={2015}, pages={436-444}, doi={https://doi.org/10.1038/nature14539}}
@inproceedings{dup, title={Deep Learning in NLP}, author={LeCun, Yann}, booktitle={Conf}, year={2015}}
@article{dup, title={Other}, author={Doe, Jane}, year={20}}
"""


def run(script: str, *args: str, cwd: Path | None = None) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(SKILLS_DIR / script), *args], capture_output=True, text=True,
                          encoding="utf-8", cwd=cwd, timeout=120)


@pytest.fixture
def bib(tmp_path: Path) -> Path:
    p = tmp_path / "refs.bib"
    p.write_text(BIB, encoding="utf-8")
    return p


def test_bib_lint(bib: Path, tmp_path: Path):
    r = run("bibtex-hygiene/scripts/bib_lint.py", str(bib), "--json", "--fix", str(tmp_path / "clean.bib"))
    assert r.returncode == 1, r.stderr
    codes = {f["code"] for f in json.loads(r.stdout)["findings"]}
    assert {"duplicate-key", "doi-url", "title-case", "year-format", "missing-field"} <= codes
    clean = (tmp_path / "clean.bib").read_text(encoding="utf-8")
    assert "doi     = {10.1038/nature14539}" in clean and "436--444" in clean


def test_convert_refs_roundtrip(bib: Path, tmp_path: Path):
    ris, csl, out = tmp_path / "a.ris", tmp_path / "a.json", tmp_path / "b.bib"
    steps = [(bib, ris), (ris, csl), (csl, out)]
    for src, dst in steps:
        r = run("reference-manager-interop/scripts/convert_refs.py", str(src), str(dst))
        assert r.returncode == 0, r.stderr
    items = json.loads((tmp_path / "a.json").read_text(encoding="utf-8"))
    assert items[0]["DOI"].endswith("10.1038/nature14539") and items[0]["author"][0]["family"] == "LeCun"
    assert "@article{" in (tmp_path / "b.bib").read_text(encoding="utf-8")


def test_prisma_flow_consistency(tmp_path: Path):
    counts = {"identification": {"databases": {"A": 100}, "registers": {}, "other_sources": {}},
              "removed_before_screening": {"duplicates": 20}, "records_excluded_screening": 50,
              "reports_not_retrieved": 5, "reports_excluded": {"reason": 10}, "studies_included": 15,
              "reports_included": 15}
    p = tmp_path / "c.json"
    p.write_text(json.dumps(counts), encoding="utf-8")
    r = run("systematic-review-prisma/scripts/prisma_flow.py", str(p))
    assert r.returncode == 0 and "Records screened<br/>(n = 80)" in r.stdout
    counts["reports_included"] = 99
    p.write_text(json.dumps(counts), encoding="utf-8")
    assert run("systematic-review-prisma/scripts/prisma_flow.py", str(p), "--format", "dot").returncode == 1


def test_dedupe_records(bib: Path, tmp_path: Path):
    ris = tmp_path / "a.ris"
    ris.write_text("TY  - JOUR\nTI  - Deep learning in NLP\nAU  - LeCun, Yann\nPY  - 2015\n"
                   "DO  - 10.1038/NATURE14539\nER  - \n", encoding="utf-8")
    r = run("systematic-review-prisma/scripts/dedupe_records.py", str(ris), str(bib), "-o", str(tmp_path / "o.csv"))
    assert r.returncode == 0, r.stderr
    summary = json.loads(r.stdout)
    assert summary["records_identified"] == 4 and summary["duplicates_removed"] >= 1


def test_paper_index(tmp_path: Path):
    docs = tmp_path / "papers"
    docs.mkdir()
    (docs / "a.md").write_text("# Methods\n\nWe used contrastive learning with temperature 0.07.\n", encoding="utf-8")
    (docs / "b.md").write_text("# Results\n\nCalibration improved with label smoothing.\n", encoding="utf-8")
    db = str(tmp_path / "c.sqlite")
    assert run("paper-corpus-rag/scripts/paper_index.py", "index", str(docs), "--db", db).returncode == 0
    r = run("paper-corpus-rag/scripts/paper_index.py", "query", "contrastive temperature", "--db", db, "--json")
    hits = json.loads(r.stdout)
    assert hits and hits[0]["cite"] == "a.md#0"


def test_build_graph_offline(bib: Path, tmp_path: Path):
    out = tmp_path / "kg"
    r = run("research-knowledge-graph/scripts/build_graph.py", str(bib), "--out", str(out))
    assert r.returncode == 0, r.stderr
    g = json.loads((out / "graph.json").read_text(encoding="utf-8"))
    assert {n["type"] for n in g["nodes"]} >= {"paper", "author"} and g["links"]
    assert (out / "graph.graphml").exists() and (out / "edges.csv").exists()
    assert any((out / "vault" / "papers").glob("*.md"))


def test_arxiv_preflight(tmp_path: Path):
    (tmp_path / "main.tex").write_text("\\documentclass{article}\n\\begin{document}\n\\includegraphics{Fig}\n"
                                       "\\bibliography{refs}\n\\end{document}\n", encoding="utf-8")
    (tmp_path / "fig.pdf").write_bytes(b"%PDF-1.4")
    r = run("arxiv-submission/scripts/arxiv_preflight.py", str(tmp_path), "--json")
    msgs = " ".join(f["message"] for f in json.loads(r.stdout)["findings"])
    assert r.returncode == 1 and "case mismatch" in msgs and "no .bbl" in msgs


def test_new_skill_scaffold(tmp_path: Path):
    root = tmp_path / "repo"
    (root / "skills").mkdir(parents=True)
    (root / "third_party").mkdir()
    (root / "third_party" / "categories.yaml").write_text("categories:\n  research-writing: x\n\nassign: {}\n",
                                                          encoding="utf-8")
    r = run("research-skill-creator/scripts/new_skill.py", "my-skill", "--category", "research-writing",
            "--description", "Does X. Use when Y.", "--scripts", "--root", str(root))
    assert r.returncode == 0, r.stderr
    assert (root / "skills" / "my-skill" / "SKILL.md").exists()
    assert (root / "evals" / "my-skill" / "evals.json").exists()
