"""Quality gates that run on every PR: slop linter behavior, skill rubric, trigger routing."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import skill_quality
import trigger_bench
from common import SKILLS_DIR

SLOP = SKILLS_DIR / "unslop-academic-writing" / "scripts" / "slop_check.py"

SLOPPY = ("In today's rapidly evolving landscape, large language models play a pivotal role in science. "
          "It is important to note that they could potentially transform the realm of biology. "
          "This study delves into the intricate tapestry of protein folding. Not only does our approach "
          "improve accuracy, but it also reduces cost. Our groundbreaking framework paves the way for "
          "future research. Certainly! Here is a revised version of the paragraph.")
CLEAN = ("Across 412 CASP15 targets, the median GDT-TS rose from 61.2 to 68.9 (Wilcoxon signed-rank test, "
         "p < 0.001). The gain was concentrated in orphan proteins. For proteins with deep alignments the "
         "change was negligible, which we traced to saturation above roughly 1,000 effective sequences.")


def slop(text: str, tmp_path: Path, *args: str) -> tuple[int, dict]:
    f = tmp_path / "t.md"
    f.write_text(text, encoding="utf-8")
    r = subprocess.run([sys.executable, str(SLOP), str(f), "--json", *args], capture_output=True, text=True,
                       encoding="utf-8")
    return r.returncode, json.loads(r.stdout)


def test_slop_flags_sloppy_text(tmp_path: Path):
    code, res = slop(SLOPPY, tmp_path)
    cats = res["by_category"]
    assert code == 1 and res["band"] == "severe slop"
    assert {"chat-residue", "stock-vocabulary", "filler", "construction", "promotional", "hedge-stack"} <= set(cats)


def test_slop_passes_clean_text(tmp_path: Path):
    code, res = slop(CLEAN, tmp_path)
    assert code == 0 and res["slop_index"] < 5, res["findings"]


def test_slop_ignores_latex_math_citations_and_code(tmp_path: Path):
    tex = ("We delve \\cite{delve2020} into $\\mathrm{tapestry}$ data.\n"
           "\\begin{equation} x = \\text{pivotal role} \\end{equation}\n```\nleverage = 1\n```\n")
    _, res = slop(tex, tmp_path)
    matches = [f["match"].lower() for f in res["findings"]]
    assert matches == ["delve"], matches


def test_significance_with_statistics_is_not_flagged(tmp_path: Path):
    _, res = slop("Mortality was significantly lower in the treated group (HR 0.71, 95% CI 0.60-0.84).", tmp_path)
    assert "unsupported-significance" not in res["by_category"]


def test_original_skills_meet_quality_bar():
    assert skill_quality.main(["--origin", "original", "--min-score", "80"]) == 0


def test_trigger_routing_bm25():
    assert trigger_bench.main(["--min-hit3", "0.9", "--max-false", "0.15"]) == 0
