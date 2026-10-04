"""Benchmark skills/citation-verification against a labeled reference set (network required).

Positives are corrupted or fabricated entries (the tool should flag them); negatives are
correct entries (the tool should pass them, possibly suggesting a DOI).

Usage:
    uv run benchmarks/citation_verification/run.py [--json benchmarks/results/citation-verification.json]
Exit 1 if recall < 0.9 or precision < 0.9.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

for _stream in (sys.stdout, sys.stderr):  # Windows consoles default to cp1252
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "skills" / "citation-verification" / "scripts" / "verify_citations.py"
LABELED = Path(__file__).with_name("labeled.bib")
OK = {"verified", "found-add-doi"}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", type=Path)
    args = ap.parse_args()
    text = LABELED.read_text(encoding="utf-8")
    labels = dict(re.findall(r"@\w+\{([^,]+),.*?note=\{label:(\w+)\}", text, re.S))
    with tempfile.TemporaryDirectory() as tmp:
        report_path = Path(tmp) / "report.json"
        subprocess.run([sys.executable, str(SCRIPT), str(LABELED), "--json", str(report_path)],
                       capture_output=True, text=True, encoding="utf-8", timeout=900)
        report = {r["key"]: r for r in json.loads(report_path.read_text(encoding="utf-8"))}
    tp = fp = fn = tn = 0
    rows = []
    for key, label in labels.items():
        status = report.get(key, {}).get("status", "missing")
        flagged = status not in OK
        bad = label != "real"
        tp += flagged and bad
        fp += flagged and not bad
        fn += (not flagged) and bad
        tn += (not flagged) and not bad
        mark = "ok " if flagged == bad else "ERR"
        rows.append({"key": key, "label": label, "status": status, "correct": flagged == bad})
        print(f"{mark} {label:<10} {status:<14} {key}")
    precision = tp / (tp + fp) if tp + fp else 1.0
    recall = tp / (tp + fn) if tp + fn else 1.0
    print(f"\n{len(labels)} entries  precision={precision:.2f}  recall={recall:.2f}  "
          f"(tp={tp} fp={fp} fn={fn} tn={tn})")
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps({"precision": precision, "recall": recall, "rows": rows}, indent=2) + "\n",
                             encoding="utf-8")
    return 0 if precision >= 0.9 and recall >= 0.9 else 1


if __name__ == "__main__":
    sys.exit(main())
