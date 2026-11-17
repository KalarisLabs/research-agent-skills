"""Tests for the --claims pre-pass of skills/unslop-academic-writing/scripts/slop_check.py."""

from __future__ import annotations

import importlib.util
import json
import sys

import pytest
from common import SKILLS_DIR

SCRIPT = SKILLS_DIR / "unslop-academic-writing" / "scripts" / "slop_check.py"

EMPTY = ("In recent years the field has seen a great deal of attention and many researchers have turned toward "
         "approaches that seem promising for a wide range of settings, and this trend is expected to continue as "
         "more people become interested in the topic and as more resources become available to the community.")
EVIDENCED = ("We trained a network on a large image collection for ninety epochs and observed a top-1 accuracy of "
             "76.1% (He et al., 2016), as shown in Figure 2, which improves on the baseline under identical "
             "augmentation and learning-rate schedules in every single run that we performed for this study.")


@pytest.fixture(scope="module")
def sc():
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location("slop_check", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["slop_check"] = mod  # @dataclass resolves its module through sys.modules
    spec.loader.exec_module(mod)
    return mod


def test_flags_only_the_paragraph_without_evidence(sc):
    found = sc.paragraph_audit(f"# Intro\n\n{EMPTY}\n\n{EVIDENCED}\n")
    assert [f["line"] for f in found] == [3]
    assert "what is the claim" in found[0]["note"]


@pytest.mark.parametrize("signal", ["12 patients", "as in \\cite{smith2020}", "see Table 3", "using BERT", "[12]"])
def test_any_single_evidence_signal_clears_a_paragraph(sc, signal):
    para = EMPTY.replace("turned toward", f"turned toward {signal}, and toward")
    assert sc.paragraph_audit(para) == []


def test_short_paragraphs_headings_and_code_are_ignored(sc):
    text = "# A heading with no evidence at all in it\n\nShort transition sentence here.\n\n```\n" + EMPTY + "\n```\n"
    assert sc.paragraph_audit(text) == []


def test_cli_claims_mode_never_fails_the_build(sc, tmp_path, monkeypatch, capsys):
    p = tmp_path / "d.md"
    p.write_text(EMPTY + "\n", encoding="utf-8")
    monkeypatch.setattr(sys, "argv", ["slop_check.py", str(p), "--claims", "--json"])
    assert sc.main() == 0
    assert json.loads(capsys.readouterr().out)["empty_paragraphs"][0]["line"] == 1
