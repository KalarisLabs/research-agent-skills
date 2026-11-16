"""Offline tests for skills/paper-corpus-rag (paper_convert.py, paper_index.py)."""

from __future__ import annotations

import importlib.util
import json
import sqlite3
import sys
from pathlib import Path

import pytest
from common import SKILLS_DIR

SCRIPTS = SKILLS_DIR / "paper-corpus-rag" / "scripts"


def load(name: str):
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def pi():
    return load("paper_index")


@pytest.fixture(scope="module")
def pc():
    return load("paper_convert")


def cli(mod, monkeypatch, capsys, *argv: str) -> tuple[int, str, str]:
    monkeypatch.setattr(sys, "argv", ["prog", *argv])
    code = mod.main()
    out = capsys.readouterr()
    return code, out.out, out.err


def words(n: int, stem: str = "alpha") -> str:
    return " ".join(f"{stem}{i % 50}" for i in range(n))


PAPER_A = f"""<!-- page: 1 -->
# Calibration of neural networks

## Abstract

We study temperature scaling for confidence calibration of deep classifiers.

## Methods

### Training details

{words(450)}.

<!-- page: 2 -->
The batch size was varied from 32 to 512 and label smoothing was compared with temperature scaling.

Table 2. Expected calibration error by batch size.

## Results

Larger batches increased calibration error by 4.2 points.

## References

1. Guo C. On calibration. 2017.

2. Another reference about zebra giraffe okapi.
"""

PAPER_B = """<!-- page: 1 -->
# Vehicle safety study

## Introduction

The car industry adopted new braking standards after the study.

<!-- page: 2 -->
## Discussion

Vehicles with the new brakes stopped sooner.
"""


@pytest.fixture
def corpus(tmp_path: Path) -> Path:
    d = tmp_path / "papers"
    d.mkdir()
    (d / "calib.md").write_text(PAPER_A, encoding="utf-8")
    (d / "calib.quality.json").write_text(json.dumps({"grade": "tables-poor", "pages": 2}), encoding="utf-8")
    (d / "cars.md").write_text(PAPER_B, encoding="utf-8")
    return d


# ---------------------------------------------------------------------------------------- chunking
def test_chunks_never_cross_headings_and_respect_size(pi):
    chunks = pi.chunk_text(PAPER_A)
    assert all(len(c["text"].split()) <= pi.MAX_WORDS for c in chunks)
    methods = [c for c in chunks if c["section"].endswith("Training details")]
    assert methods and methods[0]["section"] == "Calibration of neural networks > Methods > Training details"
    # no chunk mixes text from two sections
    for c in chunks:
        assert not ("Larger batches" in c["text"] and "temperature scaling for confidence" in c["text"])


def test_pages_are_tracked_and_markers_removed(pi):
    chunks = pi.chunk_text(PAPER_A)
    assert all("<!-- page" not in c["text"] for c in chunks)
    batch = next(c for c in chunks if "batch size was varied" in c["text"])
    # the short tail on page 2 is folded into the preceding chunk of the same section, so that chunk spans 1-2
    assert (batch["page_start"], batch["page_end"]) == (1, 2)
    first = next(c for c in chunks if "temperature scaling for confidence" in c["text"])
    assert first["page_start"] == 1


def test_reference_list_is_not_indexed_and_captions_stand_alone(pi):
    chunks = pi.chunk_text(PAPER_A)
    assert not any("zebra giraffe" in c["text"] for c in chunks)
    cap = [c for c in chunks if c["caption"]]
    assert len(cap) == 1 and cap[0]["text"].startswith("Table 2.") and cap[0]["section"].endswith("[caption]")


def test_long_paragraph_is_split_on_sentences(pi):
    text = "# T\n\n## S\n\n" + " ".join(f"Sentence number {i} has several words in it." for i in range(300))
    chunks = pi.chunk_text(text)
    assert len(chunks) > 1 and all(len(c["text"].split()) <= pi.MAX_WORDS for c in chunks)


# ------------------------------------------------------------------------------ index, query, read
def test_index_query_cites_file_chunk_pages_and_grade(pi, corpus, tmp_path, monkeypatch, capsys):
    db = str(tmp_path / "c.sqlite")
    assert cli(pi, monkeypatch, capsys, "index", str(corpus), "--db", db)[0] == 0
    code, out, _ = cli(pi, monkeypatch, capsys, "query", "label smoothing", "--db", db, "--json")
    hits = json.loads(out)
    assert code == 0 and hits[0]["paper"] == "calib.md" and "#" in hits[0]["cite"]
    assert hits[0]["pages"] == "1-2" and hits[0]["grade"] == "tables-poor"
    _, text, _ = cli(pi, monkeypatch, capsys, "query", "label smoothing", "--db", db)
    assert "check the PDF" in text


def test_incremental_index_skips_unchanged_and_drops_removed(pi, corpus, tmp_path, monkeypatch, capsys):
    db = str(tmp_path / "c.sqlite")
    cli(pi, monkeypatch, capsys, "index", str(corpus), "--db", db)
    _, out, _ = cli(pi, monkeypatch, capsys, "index", str(corpus), "--db", db)
    assert "0 documents, 2 unchanged" in out
    (corpus / "cars.md").unlink()
    cli(pi, monkeypatch, capsys, "index", str(corpus), "--db", db)
    assert sqlite3.connect(db).execute("SELECT COUNT(*) FROM docs").fetchone()[0] == 1


def test_by_paper_ranks_papers_not_chunks(pi, corpus, tmp_path, monkeypatch, capsys):
    db = str(tmp_path / "c.sqlite")
    cli(pi, monkeypatch, capsys, "index", str(corpus), "--db", db)
    _, out, _ = cli(pi, monkeypatch, capsys, "query", "calibration error batch", "--db", db, "--by-paper", "--json")
    papers = json.loads(out)
    assert papers[0]["paper"] == "calib.md" and "best" in papers[0]


def test_read_returns_whole_paper_with_grade_and_page_filter(pi, corpus, tmp_path, monkeypatch, capsys):
    db = str(tmp_path / "c.sqlite")
    cli(pi, monkeypatch, capsys, "index", str(corpus), "--db", db)
    _, out, _ = cli(pi, monkeypatch, capsys, "read", "calib.md", "--db", db)
    assert "grade: tables-poor" in out and "WARNING" in out and "Larger batches" in out
    _, out, _ = cli(pi, monkeypatch, capsys, "read", "calib.md", "--db", db, "--pages", "2")
    assert "batch size was varied" in out and "Training details" not in out


def test_read_rejects_paths_outside_the_indexed_folder(pi, corpus, tmp_path, monkeypatch, capsys):
    db = str(tmp_path / "c.sqlite")
    cli(pi, monkeypatch, capsys, "index", str(corpus), "--db", db)
    code, _, err = cli(pi, monkeypatch, capsys, "read", "../escape.md", "--db", db)
    assert code == 2 and "not in the index" in err


def test_old_index_is_refused_with_rebuild_hint(pi, corpus, tmp_path, monkeypatch, capsys):
    db = tmp_path / "old.sqlite"
    con = sqlite3.connect(db)
    con.execute("CREATE TABLE docs (path TEXT PRIMARY KEY, sha256 TEXT, title TEXT, n_chunks INTEGER)")
    con.commit()
    con.close()
    code, _, err = cli(pi, monkeypatch, capsys, "index", str(corpus), "--db", str(db))
    assert code == 2 and "--rebuild" in err
    assert cli(pi, monkeypatch, capsys, "index", str(corpus), "--db", str(db), "--rebuild")[0] == 0


# --------------------------------------------------------------------------------- eval and hybrid
def test_eval_reports_recall_and_gates_on_min_recall(pi, corpus, tmp_path, monkeypatch, capsys):
    db = str(tmp_path / "c.sqlite")
    cli(pi, monkeypatch, capsys, "index", str(corpus), "--db", db)
    q = tmp_path / "q.jsonl"
    q.write_text("\n".join(json.dumps(x) for x in [
        {"q": "label smoothing batch size", "expect_path": "calib.md", "expect_text": "label smoothing"},
        {"q": "braking standards", "expect_path": "cars.md"},
        {"q": "nonexistent zzzz", "expect_path": "cars.md"}]), encoding="utf-8")
    code, out, _ = cli(pi, monkeypatch, capsys, "eval", str(q), "--db", db, "--min-recall", "0.5")
    assert code == 0 and "recall@8=0.67" in out and "MISS: nonexistent zzzz" in out
    assert cli(pi, monkeypatch, capsys, "eval", str(q), "--db", db, "--min-recall", "0.9")[0] == 1


def test_rrf_rewards_agreement_between_rankings(pi):
    fused = dict(pi.rrf([[1, 2, 3], [3, 1, 4]]))
    assert fused[1] > fused[2] and fused[3] > fused[2] and fused[4] < fused[1]


def test_hybrid_finds_a_synonym_that_bm25_misses(pi, corpus, tmp_path, monkeypatch, capsys):
    np = pytest.importorskip("numpy")
    synonyms = {"automobile": 0, "car": 0, "vehicles": 0, "calibration": 1, "braking": 2, "brakes": 2}

    def fake_embed(model, texts, is_query=False):
        mat = np.zeros((len(texts), 8), dtype="float32")
        for i, t in enumerate(texts):
            for w in t.lower().replace(".", " ").split():
                mat[i, synonyms.get(w, 3)] += 1.0
            mat[i] /= max(float(np.linalg.norm(mat[i])), 1e-9)
        return mat

    monkeypatch.setattr(pi, "embed_texts", fake_embed)
    db = str(tmp_path / "c.sqlite")
    cli(pi, monkeypatch, capsys, "index", str(corpus), "--db", db)
    # no embeddings yet: hybrid mode must fail loudly, auto mode must fall back to BM25 silently
    assert cli(pi, monkeypatch, capsys, "query", "automobile", "--db", db, "--mode", "hybrid")[0] == 2
    cli(pi, monkeypatch, capsys, "embed", "--db", db, "--model", "fake")
    _, out, _ = cli(pi, monkeypatch, capsys, "query", "automobile", "--db", db, "--mode", "bm25", "--json")
    assert json.loads(out) == []  # the word "automobile" appears in no paper, so keyword search finds nothing
    _, out, _ = cli(pi, monkeypatch, capsys, "query", "automobile", "--db", db, "--mode", "hybrid", "--json")
    hybrid = json.loads(out)
    assert hybrid and hybrid[0]["paper"] == "cars.md"
    _, out, _ = cli(pi, monkeypatch, capsys, "stats", "--db", db)
    assert "embeddings: fake" in out


# ---------------------------------------------------------------------------------------- convert
PROSE = "Normal prose line with plenty of readable words about the study design. " * 5
PDFTOTEXT = (
    "Results. The effect was significant (P 5 0.04) and larger in group A (n 5 12). " + PROSE + "\f"
    "Table 1. Outcomes.\n12 14 15 16 18 20\n22 24 25 26 28 30\n31 33 35 36 38 40\n" + PROSE + "\f" + PROSE
)


def test_convert_adds_page_markers_logs_repairs_and_grades(pc, tmp_path):
    src = tmp_path / "p.txt"
    src.write_text(PDFTOTEXT, encoding="utf-8")
    report = pc.convert(src, tmp_path / "out", "auto", None)
    md = (tmp_path / "out" / "p.md").read_text(encoding="utf-8")
    assert "<!-- page: 1 -->" in md and "<!-- page: 3 -->" in md
    assert "P = 0.04" in md and "n = 12" in md
    assert {r["before"] for r in report["repairs"]} == {"P 5", "n 5"}
    assert report["grade"] == "tables-poor" and any("flattened" in f for f in report["flags"])
    side = json.loads((tmp_path / "out" / "p.quality.json").read_text(encoding="utf-8"))
    assert side["grade"] == "tables-poor" and side["pages"] == 3


def test_convert_grades_scans_and_symbol_damage(pc):
    scan, _, _ = pc.grade_pages(["", "", "short"])
    assert scan == "scan-poor"
    damaged, flags, _ = pc.grade_pages(["Normal text " * 40 + "(cid:12)" * 12])
    assert damaged == "math-poor" and any("damaged" in f for f in flags)
    assert pc.grade_pages(["Clean prose sentence. " * 40])[0] == "good"


def test_convert_checks_abstract_numbers(pc):
    res = pc.check_abstract("Accuracy rose to 91.5% (n = 120, p = 0.03).", "Accuracy was 91.5% with n = 120.")
    assert res["missing"] == ["0.03"]


def test_convert_cli_end_to_end_and_index_picks_up_grade(pi, pc, tmp_path, monkeypatch, capsys):
    src = tmp_path / "in"
    src.mkdir()
    (src / "p.txt").write_text(PDFTOTEXT, encoding="utf-8")
    out = tmp_path / "out"
    assert cli(pc, monkeypatch, capsys, str(src), "-o", str(out))[0] == 0
    db = str(tmp_path / "c.sqlite")
    cli(pi, monkeypatch, capsys, "index", str(out), "--db", db)
    _, stats, _ = cli(pi, monkeypatch, capsys, "stats", "--db", db)
    assert "tables-poor 1" in stats
    assert cli(pc, monkeypatch, capsys, str(tmp_path / "missing.pdf"))[0] == 2
