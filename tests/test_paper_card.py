"""Offline tests for skills/paper-card/scripts/check_card.py."""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest
from common import SKILLS_DIR

SCRIPT = SKILLS_DIR / "paper-card" / "scripts" / "check_card.py"

PAPER = """<!-- page: 1 -->
# Calibration study

We enrolled 1,200 patients across 3 sites.

<!-- page: 2 -->
Temperature scaling reduces ECE from 8.1 % to 2.3% on CIFAR-100, while label smoothing gave 4.0%.
The mean difference was −0.45 (95% CI −0.80 to −0.10), p = 0.012.
Data were collected in dis-
tributed centres.
"""


@pytest.fixture(scope="module")
def cc():
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location("check_card", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture
def src(tmp_path: Path) -> Path:
    d = tmp_path / "md"
    d.mkdir()
    (d / "p.md").write_text(PAPER, encoding="utf-8")
    return d


def claim(**kw) -> dict:
    base = {"id": "c1", "kind": "result", "claim": "ECE fell from 8.1% to 2.3%.",
            "evidence": [{"page": 2, "quote": "reduces ECE from 8.1 % to 2.3% on CIFAR-100",
                          "numbers": ["8.1%", "2.3%"]}]}
    base.update(kw)
    return base


def run(cc, src, claims, grade="good"):
    pages = cc.pages_of(PAPER)
    return [cc.check_claim(c, pages, grade) for c in claims]


def test_verified_claim_tolerates_spacing_dashes_and_hyphenation(cc, src):
    pages = cc.pages_of(PAPER)
    assert cc.check_claim(claim(), pages, "good")["status"] == "verified"
    c = claim(claim="The mean difference was -0.45.", evidence=[
        {"page": 2, "quote": "The mean difference was -0.45 (95% CI -0.80 to -0.10)", "numbers": ["-0.45"]}])
    assert cc.check_claim(c, pages, "good")["status"] == "verified"
    c = claim(claim="Data came from distributed centres.",
              evidence=[{"page": 2, "quote": "collected in distributed centres", "numbers": []}])
    assert cc.check_claim(c, pages, "good")["status"] == "verified"


def test_quote_must_be_on_the_cited_page(cc):
    pages = cc.pages_of(PAPER)
    wrong_page = claim(evidence=[{"page": 1, "quote": "reduces ECE from 8.1 % to 2.3%", "numbers": []}])
    assert cc.check_claim(wrong_page, pages, "good")["status"] == "quote-not-found"
    assert cc.check_claim(claim(evidence=[{"page": 9, "quote": "x", "numbers": []}]), pages, "good")[
        "status"] == "page-missing"


def test_numbers_must_appear_as_whole_numbers_on_the_page(cc):
    pages = cc.pages_of(PAPER)
    bad = claim(evidence=[{"page": 2, "quote": "reduces ECE from 8.1 % to 2.3% on CIFAR-100",
                           "numbers": ["2.3%", "5.1%"]}])
    r = cc.check_claim(bad, pages, "good")
    assert r["status"] == "number-not-found" and "5.1%" in r["problems"][0]
    # 0.45 must not be "found" inside -0.450 or 10.45; 200 must not match inside 1,200
    assert not cc.number_in("value 10.45 here", "0.45")
    assert not cc.number_in("1,200 patients", "200")
    assert cc.number_in("1,200 patients", "1200")


def test_claim_cannot_state_a_number_the_evidence_lacks(cc):
    pages = cc.pages_of(PAPER)
    r = cc.check_claim(claim(claim="ECE fell from 8.1% to 2.3%, a 72% reduction."), pages, "good")
    assert r["status"] == "unsupported-number" and "72%" in r["problems"][0]


def test_derived_numbers_are_recomputed_and_must_use_cited_inputs(cc):
    pages = cc.pages_of(PAPER)
    ok = claim(claim="ECE fell by 5.8 points.", derived_numbers=[{"value": "5.8", "from": "8.1 - 2.3"}])
    assert cc.check_claim(ok, pages, "good")["status"] == "verified"
    wrong = claim(claim="ECE fell by 6.8 points.", derived_numbers=[{"value": "6.8", "from": "8.1 - 2.3"}])
    assert cc.check_claim(wrong, pages, "good")["status"] == "bad-derivation"
    foreign = claim(claim="ECE fell by 4.1 points.", derived_numbers=[{"value": "4.1", "from": "8.1 - 4.0"}])
    assert cc.check_claim(foreign, pages, "good")["status"] == "bad-derivation"  # 4.0 is on the page but not cited


def test_safe_eval_rejects_code(cc):
    assert cc.safe_eval("(8.1 - 2.3) * 2") == pytest.approx(11.6)
    with pytest.raises(ValueError):
        cc.safe_eval("__import__('os').system('x')")


def test_poor_conversion_grade_requests_a_pdf_check_only_for_numeric_claims(cc):
    pages = cc.pages_of(PAPER)
    assert cc.check_claim(claim(), pages, "tables-poor")["pdf_check"] is True
    method = claim(claim="Data were collected in distributed centres.",
                   evidence=[{"page": 2, "quote": "collected in distributed centres", "numbers": []}])
    assert cc.check_claim(method, pages, "tables-poor")["pdf_check"] is False


def write_card(tmp_path: Path, claims: list[dict]) -> Path:
    p = tmp_path / "card.json"
    p.write_text(json.dumps({"paper": "p.md", "title": "T", "claims": claims}), encoding="utf-8")
    return p


def main(cc, monkeypatch, *argv) -> int:
    monkeypatch.setattr(sys, "argv", ["check_card.py", *argv])
    return cc.main()


def test_cli_exit_codes_and_review_flow(cc, src, tmp_path, monkeypatch, capsys):
    card = write_card(tmp_path, [claim()])
    assert main(cc, monkeypatch, str(card), "--source", str(src)) == 0
    assert "review pending" in capsys.readouterr().out
    packet = tmp_path / "review.md"
    assert main(cc, monkeypatch, str(card), "--source", str(src), "--review-packet", str(packet)) == 0
    text = packet.read_text(encoding="utf-8")
    assert "different model" in text and "reduces ECE" in text and "c1" in text

    good = tmp_path / "v.json"
    good.write_text(json.dumps({"c1": {"verdict": "supported", "reason": ""}}), encoding="utf-8")
    assert main(cc, monkeypatch, str(card), "--source", str(src), "--review", str(good)) == 0
    assert "accepted" in capsys.readouterr().out

    bad = tmp_path / "bad.json"
    bad.write_text(json.dumps({"c1": {"verdict": "misattributed", "reason": "that is label smoothing"}}),
                   encoding="utf-8")
    assert main(cc, monkeypatch, str(card), "--source", str(src), "--review", str(bad)) == 1
    out = capsys.readouterr().out
    assert "rejected" in out and "label smoothing" in out

    missing = tmp_path / "m.json"
    missing.write_text("{}", encoding="utf-8")
    assert main(cc, monkeypatch, str(card), "--source", str(src), "--review", str(missing)) == 1


def test_cli_fails_on_unverified_claim_even_with_a_supportive_review(cc, src, tmp_path, monkeypatch):
    card = write_card(tmp_path, [claim(evidence=[{"page": 2, "quote": "invented sentence", "numbers": []}])])
    verdicts = tmp_path / "v.json"
    verdicts.write_text(json.dumps({"c1": {"verdict": "supported"}}), encoding="utf-8")
    assert main(cc, monkeypatch, str(card), "--source", str(src)) == 1
    assert main(cc, monkeypatch, str(card), "--source", str(src), "--review", str(verdicts)) == 1


def test_cli_rejects_paths_outside_source_and_bad_input(cc, src, tmp_path, monkeypatch):
    p = tmp_path / "card.json"
    p.write_text(json.dumps({"paper": "../escape.md", "claims": [claim()]}), encoding="utf-8")
    assert main(cc, monkeypatch, str(p), "--source", str(src)) == 2
    assert main(cc, monkeypatch, str(tmp_path / "nope.json"), "--source", str(src)) == 2
    p.write_text(json.dumps({"paper": "p.md", "claims": []}), encoding="utf-8")
    assert main(cc, monkeypatch, str(p), "--source", str(src)) == 2


def test_template_is_valid_json(cc, monkeypatch, capsys):
    assert main(cc, monkeypatch, "--template") == 0
    card = json.loads(capsys.readouterr().out)
    assert card["claims"][0]["evidence"][0]["quote"]
