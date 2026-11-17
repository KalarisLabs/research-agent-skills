"""Offline tests for skills/fulltext-acquisition (fulltext_status.py, match_pdf.py)."""

from __future__ import annotations

import csv
import importlib.util
import json
import sys
from pathlib import Path

import pytest
from common import SKILLS_DIR

SCRIPTS = SKILLS_DIR / "fulltext-acquisition" / "scripts"


def load(name: str):
    sys.dont_write_bytecode = True
    sys.path.insert(0, str(SCRIPTS))
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def fs():
    return load("fulltext_status")


@pytest.fixture(scope="module")
def mp(fs):
    return load("match_pdf")


RECORDS = [
    {"record_id": "R00001", "doi": "https://doi.org/10.1038/NATURE14539", "pmid": "26017442",
     "title": "Deep learning", "authors": "LeCun Y; Bengio Y", "year": "2015", "journal": "Nature"},
    {"record_id": "R00002", "doi": "10.1126/science.aaa8415", "pmid": "",
     "title": "Machine learning: trends, perspectives, and prospects",
     "authors": "Jordan MI; Mitchell TM", "year": "2015", "journal": "Science", "volume": "349", "pages": "255-260"},
    {"record_id": "R00003", "doi": "", "pmid": "",
     "title": "A study of the calibration of modern neural networks in practice",
     "authors": "Guo C", "year": "2017", "journal": "ICML"},
    {"record_id": "R00004", "doi": "", "pmid": "",
     "title": "A study of the calibration of modern neural networks in theory",
     "authors": "Guo C", "year": "2017", "journal": "ICML"},
]


@pytest.fixture
def recs(tmp_path: Path) -> Path:
    p = tmp_path / "included.csv"
    cols = ["record_id", "doi", "pmid", "title", "authors", "year", "journal", "volume", "pages"]
    with p.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(RECORDS)
    return p


def run(mod, monkeypatch, *argv) -> int:
    monkeypatch.setattr(sys, "argv", ["prog", *argv])
    return mod.main()


def test_status_lists_only_missing_papers_and_builds_links(fs, recs, tmp_path, monkeypatch, capsys):
    lib = tmp_path / "papers"
    lib.mkdir()
    (lib / "R00001.pdf").write_bytes(b"%PDF-1.4 x")
    (lib / "R00003.pdf").write_bytes(b"")  # an empty file is not a full text
    out = tmp_path / "work"
    code = run(fs, monkeypatch, str(recs), "--library", str(lib), "-o", str(out), "--resolver",
               "https://resolver.research-agent-skills.local/openurl?")
    summary = json.loads(capsys.readouterr().out.splitlines()[0])
    assert code == 0 and summary["total"] == 4 and summary["have"] == 1 and summary["missing"] == 3
    assert summary["no_doi"] == 2
    rows = list(csv.DictReader((out / "missing.csv").open(encoding="utf-8")))
    assert [r["id"] for r in rows] == ["R00002", "R00003", "R00004"]
    page = (out / "retrieval.md").read_text(encoding="utf-8")
    assert "https://doi.org/10.1126/science.aaa8415" in page and "Institution resolver" in page
    assert "rft_id=info%3Adoi%2F10.1126%2Fscience.aaa8415" in page
    assert "| Pages | 255-260 |" in page and "ILL request fields" in page


def test_resolve_oa_requires_email_and_is_never_called_offline(fs, recs, tmp_path, monkeypatch):
    lib = tmp_path / "p"
    lib.mkdir()
    with pytest.raises(SystemExit):
        run(fs, monkeypatch, str(recs), "--library", str(lib), "--resolve-oa")
    monkeypatch.setattr(fs, "unpaywall", lambda *a, **k: (_ for _ in ()).throw(AssertionError("network used")))
    assert run(fs, monkeypatch, str(recs), "--library", str(lib), "-o", str(tmp_path / "w")) == 0


def test_unpaywall_result_is_recorded(fs, recs, tmp_path, monkeypatch, capsys):
    lib = tmp_path / "p"
    lib.mkdir()
    monkeypatch.setattr(fs, "unpaywall", lambda doi, email: {"oa_url": f"https://oa.example/{doi}.pdf",
                                                             "oa_status": "green", "is_oa": True})
    monkeypatch.setattr(fs.time, "sleep", lambda s: None)
    run(fs, monkeypatch, str(recs), "--library", str(lib), "-o", str(tmp_path / "w"), "--resolve-oa",
        "--email", "a@b.c")
    assert json.loads(capsys.readouterr().out.splitlines()[0])["open_access"] == 2  # only R00001 and R00002 have DOIs
    assert "Open-access PDF" in (tmp_path / "w" / "retrieval.md").read_text(encoding="utf-8")


def test_bad_records_file_exits_2(fs, tmp_path, monkeypatch):
    empty = tmp_path / "e.csv"
    empty.write_text("record_id,title\n", encoding="utf-8")
    assert run(fs, monkeypatch, str(empty), "--library", str(tmp_path)) == 2
    dup = tmp_path / "d.csv"
    dup.write_text("record_id,title\nR1,a\nR1,b\n", encoding="utf-8")
    assert run(fs, monkeypatch, str(dup), "--library", str(tmp_path)) == 2


# ----------------------------------------------------------------------------------------- matching
def inbox_with(tmp_path: Path, files: dict[str, str]) -> Path:
    d = tmp_path / "inbox"
    d.mkdir()
    for name, text in files.items():
        (d / name).write_text(text, encoding="utf-8")
    return d


PAGE_DEEP = ("Deep learning\nYann LeCun, Yoshua Bengio\nNature 521, 436-444 (2015)\ndoi:10.1038/nature14539\n"
             + "body " * 30)
PAGE_ML = ("Machine learning: trends,\nperspectives, and prospects\nM. I. Jordan, T. M. Mitchell\n"
           "Science 349 (2015)\n" + "body " * 30)


def test_matches_by_doi_in_text_even_with_a_useless_filename(mp, recs, tmp_path, monkeypatch, capsys):
    inbox = inbox_with(tmp_path, {"download (3).txt": PAGE_DEEP})
    code = run(mp, monkeypatch, str(recs), "--inbox", str(inbox), "--library", str(tmp_path / "lib"))
    out = capsys.readouterr().out
    assert code == 0 and "matched" in out and "R00001" in out and "text:doi" in out
    assert not (tmp_path / "lib").exists()  # report only: nothing copied without --attach


def test_matches_by_title_across_wrapped_lines(mp, recs, tmp_path, monkeypatch, capsys):
    inbox = inbox_with(tmp_path, {"x.txt": PAGE_ML})
    assert run(mp, monkeypatch, str(recs), "--inbox", str(inbox), "--library", str(tmp_path / "lib")) == 0
    assert "R00002" in capsys.readouterr().out


def test_misnamed_file_is_a_conflict_and_never_attached(mp, recs, tmp_path, monkeypatch, capsys):
    inbox = inbox_with(tmp_path, {"10.1126_science.aaa8415.txt": PAGE_DEEP})
    lib = tmp_path / "lib"
    code = run(mp, monkeypatch, str(recs), "--inbox", str(inbox), "--library", str(lib), "--attach")
    out = capsys.readouterr().out
    assert code == 1 and "conflict" in out and "misnamed" in out
    assert not lib.exists() or not list(lib.glob("*.txt"))


def test_paper_that_only_cites_a_record_is_not_matched(mp, recs, tmp_path, monkeypatch, capsys):
    text = ("An unrelated paper about protein folding\nA. Author\n" + "body " * 40
            + "\nReferences\n1. doi:10.1038/nature14539\n")
    inbox = inbox_with(tmp_path, {"y.txt": text})
    assert run(mp, monkeypatch, str(recs), "--inbox", str(inbox), "--library", str(tmp_path / "lib")) == 1
    assert "unmatched" in capsys.readouterr().out


def test_near_identical_titles_are_ambiguous(mp, recs, tmp_path, monkeypatch, capsys):
    inbox = inbox_with(tmp_path, {"z.txt": "A study of the calibration of modern neural networks in\n" + "body " * 40})
    assert run(mp, monkeypatch, str(recs), "--inbox", str(inbox), "--library", str(tmp_path / "lib")) == 1
    assert "ambiguous" in capsys.readouterr().out


def test_attach_copies_logs_manifest_and_never_overwrites(mp, recs, tmp_path, monkeypatch, capsys):
    inbox = inbox_with(tmp_path, {"a.txt": PAGE_DEEP, "b.txt": PAGE_ML})
    lib = tmp_path / "lib"
    assert run(mp, monkeypatch, str(recs), "--inbox", str(inbox), "--library", str(lib), "--attach") == 0
    assert (lib / "R00001.txt").is_file() and (lib / "R00002.txt").is_file()
    manifest = json.loads((lib / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["R00001"]["verified_by"] == "text:doi" and len(manifest["R00001"]["sha256"]) == 64
    (inbox / "c.txt").write_text(PAGE_DEEP + " second copy", encoding="utf-8")
    run(mp, monkeypatch, str(recs), "--inbox", str(inbox), "--library", str(lib), "--attach")
    assert "duplicate" in capsys.readouterr().out
    assert "second copy" not in (lib / "R00001.txt").read_text(encoding="utf-8")


def test_filename_only_needs_explicit_permission(mp, recs, tmp_path, monkeypatch, capsys):
    inbox = tmp_path / "inbox"
    inbox.mkdir()
    (inbox / "PMID26017442.pdf").write_bytes(b"%PDF-1.4 binary with no text layer")
    lib = tmp_path / "lib"
    assert run(mp, monkeypatch, str(recs), "--inbox", str(inbox), "--library", str(lib), "--attach") == 1
    assert "filename-only" in capsys.readouterr().out and not lib.exists()
    assert run(mp, monkeypatch, str(recs), "--inbox", str(inbox), "--library", str(lib), "--attach",
               "--allow-filename-only") == 1  # still reported as needing a look, but now attached
    assert (lib / "R00001.pdf").is_file()


def test_doi_from_name_handles_common_download_names(mp):
    assert mp.doi_from_name("10.1038_nature14539.pdf") == "10.1038/nature14539"
    assert mp.doi_from_name("10.1038%2Fnature14539.pdf") == "10.1038/nature14539"
    assert mp.doi_from_name("paper (1).pdf") is None
