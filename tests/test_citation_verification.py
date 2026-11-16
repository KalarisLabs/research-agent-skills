"""Offline tests for skills/citation-verification/scripts/verify_citations.py (HTTP is monkeypatched)."""

from __future__ import annotations

import importlib.util
import urllib.error
from pathlib import Path

import pytest
from common import SKILLS_DIR

SCRIPT = SKILLS_DIR / "citation-verification" / "scripts" / "verify_citations.py"


@pytest.fixture(scope="module")
def vc():
    import sys

    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location("verify_citations", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def crossref_msg(title: str, year: int, family: str, updated_by=None) -> dict:
    msg = {"DOI": "10.1/x", "title": [title], "author": [{"family": family}], "issued": {"date-parts": [[year]]}}
    if updated_by:
        msg["updated-by"] = updated_by
    return {"message": msg}


def fake_http(routes: dict):
    def fn(url: str, retries: int = 3):
        for prefix, value in routes.items():
            if url.startswith(prefix):
                if isinstance(value, Exception):
                    raise value
                return value
        return None

    return fn


UNKNOWN = {"_key": "n", "title": "A completely unknown title here", "author": "Nobody, N", "year": "2020"}
ENTRY = {"_key": "k", "title": "A study of things", "author": "Smith, Jane", "year": "2020", "doi": "10.1/x"}


def test_retraction_notice_gives_retracted_status(vc, monkeypatch):
    notice = [{"DOI": "10.1/notice", "type": "retraction", "label": "Retraction", "source": "retraction-watch"}]
    monkeypatch.setattr(vc, "http_json", fake_http({"https://api.crossref.org/works/": crossref_msg(
        "A study of things", 2020, "Smith", notice)}))
    res = vc.check_entry(ENTRY)
    assert res["status"] == "retracted"
    assert "RETRACTED" in res["problems"][0] and "10.1/notice" in res["problems"][0]


def test_correction_notice_does_not_flag(vc, monkeypatch):
    notice = [{"DOI": "10.1/c", "type": "correction", "source": "publisher"}]
    monkeypatch.setattr(vc, "http_json", fake_http({
        "https://api.crossref.org/works/": crossref_msg("A study of things", 2020, "Smith", notice),
        "https://api.openalex.org/": {"is_retracted": False}}))
    assert vc.check_entry(ENTRY)["status"] == "verified"


def test_expression_of_concern_is_uncertain(vc, monkeypatch):
    notice = [{"DOI": "10.1/eoc", "type": "expression_of_concern", "source": "publisher"}]
    monkeypatch.setattr(vc, "http_json", fake_http({"https://api.crossref.org/works/": crossref_msg(
        "A study of things", 2020, "Smith", notice)}))
    assert vc.check_entry(ENTRY)["status"] == "uncertain"


def test_openalex_is_retracted_is_an_independent_signal(vc, monkeypatch):
    monkeypatch.setattr(vc, "http_json", fake_http({
        "https://api.crossref.org/works/": crossref_msg("A study of things", 2020, "Smith"),
        "https://api.openalex.org/": {"is_retracted": True}}))
    res = vc.check_entry(ENTRY)
    assert res["status"] == "retracted" and "openalex" in res["problems"][0]


def test_datacite_doi_resolves_instead_of_doi_not_found(vc, monkeypatch):
    dc = {"data": {"attributes": {"titles": [{"title": "tool: 1.0"}], "publicationYear": 2019,
                                  "creators": [{"familyName": "Brett"}], "publisher": "Zenodo"}}}
    monkeypatch.setattr(vc, "http_json", fake_http({"https://api.datacite.org/dois/": dc,
                                                    "https://api.crossref.org/works/": None}))
    res = vc.check_entry({"_key": "d", "title": "tool: 1.0", "author": "Brett, Matthew", "year": "2019",
                          "doi": "10.5281/zenodo.1"})
    assert res["status"] == "verified"


def test_unresolved_doi_is_doi_not_found(vc, monkeypatch):
    monkeypatch.setattr(vc, "http_json", fake_http({}))
    assert vc.check_entry(ENTRY)["status"] == "doi-not-found"


def test_not_found_is_downgraded_when_a_source_was_down(vc, monkeypatch):
    err = urllib.error.HTTPError("u", 429, "Too Many Requests", {}, None)
    monkeypatch.setattr(vc, "http_json", fake_http({"https://api.crossref.org/works?": {"message": {"items": []}},
                                                    "https://api.openalex.org/": err}))
    monkeypatch.setattr(vc, "arxiv_search", lambda *a, **k: [])
    res = vc.check_entry(UNKNOWN)
    assert res["status"] == "uncertain" and "OpenAlex" in res["problems"][0]


def test_not_found_when_all_sources_answered_empty(vc, monkeypatch):
    monkeypatch.setattr(vc, "http_json", fake_http({"https://api.crossref.org/works?": {"message": {"items": []}},
                                                    "https://api.openalex.org/": {"results": []}}))
    monkeypatch.setattr(vc, "arxiv_search", lambda *a, **k: [])
    res = vc.check_entry(UNKNOWN)
    assert res["status"] == "not-found"


BIB = """@article{good, title={Good}, year={2020}}
% a normal comment
@article{bad, title={Bad}, year={2021}}
"""


def test_annotate_adds_marker_only_above_bad_entries_and_keeps_bodies(vc):
    report = [{"key": "good", "status": "verified", "problems": []},
              {"key": "bad", "status": "retracted", "problems": ["RETRACTED: notice"]}]
    out = vc.annotate_bib(BIB, report)
    assert "% UNVERIFIED (retracted): RETRACTED: notice\n@article{bad," in out
    assert out.count("UNVERIFIED") == 1
    assert "@article{good, title={Good}, year={2020}}" in out and "@article{bad, title={Bad}, year={2021}}" in out


def test_annotate_is_idempotent_and_removes_stale_markers(vc):
    report = [{"key": "bad", "status": "not-found", "problems": ["x"]}]
    once = vc.annotate_bib(BIB, report)
    assert vc.annotate_bib(once, report) == once
    fixed = vc.annotate_bib(once, [{"key": "bad", "status": "verified", "problems": []}])
    assert fixed == BIB


def test_annotate_cli_rewrites_file(vc, tmp_path: Path, monkeypatch):
    bib = tmp_path / "r.bib"
    bib.write_text("@article{k, title={A study of things}, author={Smith, Jane}, year={2020}, doi={10.1/x}}\n",
                   encoding="utf-8")
    monkeypatch.setattr(vc, "http_json", fake_http({}))
    monkeypatch.setattr("sys.argv", ["verify_citations.py", str(bib), "--annotate", "--delay", "0"])
    assert vc.main() == 1
    assert bib.read_text(encoding="utf-8").startswith("% UNVERIFIED (doi-not-found)")
