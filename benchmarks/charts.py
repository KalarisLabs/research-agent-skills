"""Render the committed benchmark results as SVG charts for the README and docs.

Every number is read from benchmarks/results/*.json, so the charts can never drift from
the data. Each chart is written twice, for light and dark backgrounds, and the README
switches between them with <picture> and prefers-color-scheme.

Palette (validated for colour-vision deficiency, all pairs, in both modes):
skill = teal, baseline = orange, human reference = violet. Every bar is directly
labelled, so identity never depends on colour alone.

Usage:
    uv run benchmarks/charts.py            # regenerate PUBLIC/benchmarks/*.svg
    uv run benchmarks/charts.py --check    # exit 1 if a committed chart is out of date
"""

from __future__ import annotations

import argparse
import io
import json
import re
import sys
from collections import Counter
from pathlib import Path

import matplotlib

matplotlib.use("svg")
import matplotlib.pyplot as plt  # noqa: E402

for _stream in (sys.stdout, sys.stderr):  # Windows consoles default to cp1252
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "benchmarks" / "results"
OUT = ROOT / "PUBLIC" / "benchmarks"

THEMES = {
    "light": {"surface": "#fcfcfb", "text": "#0b0b0b", "text2": "#52514e", "muted": "#8a8986", "grid": "#e4e3df",
              "skill": "#00819f", "base": "#eb6834", "human": "#6250d6"},
    "dark": {"surface": "#1a1a19", "text": "#f0efec", "text2": "#c3c2b7", "muted": "#8a8986", "grid": "#33332f",
             "skill": "#1593b3", "base": "#d95926", "human": "#9085e9"},
}
# DejaVu Sans ships inside matplotlib, and text is written as outlines (svg.fonttype "path"), so the SVGs are
# identical on every machine and render the same in every browser, with no dependency on installed fonts.
FONT = ["DejaVu Sans"]


def load(name: str) -> dict:
    return json.loads((RESULTS / name).read_text(encoding="utf-8"))


def figure(t: dict, w: float, h: float, title: str, subtitle: str):
    fig, ax = plt.subplots(figsize=(w, h))
    fig.patch.set_facecolor(t["surface"])
    ax.set_facecolor(t["surface"])
    fig.text(0.02, 0.97, title, ha="left", va="top", fontsize=15, fontweight="bold", color=t["text"])
    fig.text(0.02, 0.97 - 0.42 / h, subtitle, ha="left", va="top", fontsize=10, color=t["text2"])
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(t["grid"])
    ax.tick_params(colors=t["text2"], labelsize=9, length=0)
    ax.grid(axis="x", color=t["grid"], linewidth=0.8)
    ax.set_axisbelow(True)
    return fig, ax


def footnote(fig, t: dict, text: str) -> None:
    fig.text(0.02, 0.015, text, ha="left", va="bottom", fontsize=8, color=t["muted"])


def bar(ax, y, value, color, t, label, height=0.62, fmt="{:.2f}"):
    ax.barh(y, value, height=height, color=color, edgecolor=t["surface"], linewidth=2)
    ax.text(value, y, "  " + (label if label is not None else fmt.format(value)), va="center", ha="left",
            fontsize=9, color=t["text"])


def task_outcomes(t: dict):
    d = load("task-evals-pilot-haiku.json")
    rows = sorted(d["results"], key=lambda r: (r["skill_score"] - r["baseline_score"], r["skill_score"]))
    wins = sum(r["winner"] == "skill" for r in rows)
    with_mean = sum(r["skill_score"] for r in rows) / len(rows)
    base_mean = sum(r["baseline_score"] for r in rows) / len(rows)
    fig, ax = figure(t, 9, 8.6, f"With the skill, answers win {wins} of {len(rows)} tasks",
                     f"Blind judge score out of 10, same prompt answered with and without the skill · "
                     f"mean {with_mean:.1f} vs {base_mean:.1f}")
    for i, r in enumerate(rows):
        a, b = r["baseline_score"], r["skill_score"]
        ax.plot([a, b], [i, i], color=t["grid"] if a <= b else t["base"], linewidth=2, solid_capstyle="round", zorder=1)
        ax.scatter([a], [i], s=64, color=t["base"], edgecolor=t["surface"], linewidth=2, zorder=2)
        ax.scatter([b], [i], s=64, color=t["skill"], edgecolor=t["surface"], linewidth=2, zorder=3)
    ax.set_yticks(range(len(rows)), [r["skill"] for r in rows], fontsize=8.5)
    ax.set_xlim(0, 10.4)
    ax.set_xticks(range(0, 11, 2))
    ax.set_ylim(-0.8, len(rows) - 0.2)
    top = len(rows) - 1
    ax.text(rows[top]["skill_score"] + 0.25, top, "with skill", va="center", fontsize=9, color=t["text"])
    ax.text(rows[top]["baseline_score"] - 0.25, top, "without", va="center", ha="right", fontsize=9, color=t["text"])
    fig.subplots_adjust(left=0.27, right=0.97, top=0.9, bottom=0.07)
    footnote(fig, t, f"Pilot: {d['model']} answers and judge, answer order randomized, tools off. "
                     "benchmarks/results/task-evals-pilot-haiku.json")
    return fig


def slop(t: dict):
    d = load("slop.json")
    conds = [("Model, with unslop skill", d["ai_unslop"], t["skill"]),
             ("Model, no skill", d["ai_baseline"], t["base"]),
             ("Human abstracts, 2012-2018", d["human"], t["human"])]
    fig, ax = figure(t, 9, 3.6, f"{d['skill_reduction_pct']:.0f}% less AI slop with the skill",
                     "Mean slop index of scientific abstracts (lower is cleaner)")
    for i, (_name, c, color) in enumerate(conds):
        bar(ax, i, c["mean"], color, t, f"{c['mean']:.1f}   ·   {c['share_clean_lt5']:.0%} clean   ·   n = {c['n']}")
    ax.set_yticks(range(len(conds)), [c[0] for c in conds], fontsize=9.5)
    ax.set_xlim(0, max(c[1]["mean"] for c in conds) * 1.9)
    fig.subplots_adjust(left=0.25, right=0.97, top=0.76, bottom=0.2)
    footnote(fig, t, "Pilot: model abstracts for the same titles as the human set. Linter is a pattern detector, "
                     "not an AI-text detector. benchmarks/results/slop.json")
    return fig


def routing_metrics(cases: list[dict]) -> dict[str, float]:
    pos = [c for c in cases if c["should_trigger"]]
    neg = [c for c in cases if not c["should_trigger"]]
    return {"hit@1": sum(c["rank"] == 1 for c in pos) / len(pos),
            "hit@3": sum(c["rank"] is not None and c["rank"] <= 3 for c in pos) / len(pos),
            "False trigger": sum(c["rank"] == 1 for c in neg) / len(neg)}


def routing(t: dict):
    claude = load("trigger-claude-sample100.json")
    bm25_all = {c["prompt"]: c for c in load("trigger-bm25-all-evals.json")["cases"]}
    sample = [bm25_all[c["prompt"]] for c in claude["cases"]]  # same 100 prompts, keyword router
    m_claude, m_bm25 = routing_metrics(claude["cases"]), routing_metrics(sample)
    fig, ax = figure(t, 9, 4.2, f"Agents pick the right skill {m_claude['hit@3']:.0%} of the time",
                     f"Skill routing on the same {len(sample)} held-out prompts, including near misses "
                     "(false trigger: lower is better)")
    y = 0.0
    ticks = []
    for metric in m_claude:
        bar(ax, y - 0.19, m_claude[metric], t["skill"], t, f"{m_claude[metric]:.2f}  LLM router", height=0.36)
        bar(ax, y + 0.19, m_bm25[metric], t["base"], t, f"{m_bm25[metric]:.2f}  keyword (BM25)", height=0.36)
        ticks.append(y)
        y += 1.15
    ax.set_yticks(ticks, list(m_claude), fontsize=10)
    ax.invert_yaxis()
    ax.set_xlim(0, 1.45)
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1.0])
    fig.subplots_adjust(left=0.15, right=0.97, top=0.8, bottom=0.17)
    footnote(fig, t, "Pilot: Claude Haiku 4.5 choosing from every skill description; seed-7 sample of all eval suites. "
                     "benchmarks/results/trigger-*.json")
    return fig


def citations(t: dict):
    d = load("citation-verification.json")
    groups: dict[str, list[dict]] = {}
    for r in d["rows"]:
        groups.setdefault(r["label"], []).append(r)
    order = [k for k in ("real", "corrupted", "fabricated") if k in groups]
    names = {"real": "Real references: passed", "corrupted": "Corrupted (wrong DOI, year, author): flagged",
             "fabricated": "Fabricated: flagged"}
    fig, ax = figure(t, 9, 3.4, "Every fabricated and corrupted reference caught",
                     f"citation-verification on {len(d['rows'])} labeled references · "
                     f"precision {d['precision']:.2f} · recall {d['recall']:.2f}")
    for i, k in enumerate(order):
        ok = sum(r["correct"] for r in groups[k])
        bar(ax, i, ok, t["skill"], t, f"{ok} / {len(groups[k])}")
        miss = len(groups[k]) - ok
        if miss:
            ax.barh(i, miss, left=ok, height=0.62, color=t["base"], edgecolor=t["surface"], linewidth=2)
    ax.set_yticks(range(len(order)), [names[k] for k in order], fontsize=9.5)
    ax.invert_yaxis()
    ax.set_xlim(0, max(len(g) for g in groups.values()) * 1.25)
    fig.subplots_adjust(left=0.4, right=0.97, top=0.74, bottom=0.2)
    footnote(fig, t, "Checked live against Crossref, OpenAlex and arXiv. benchmarks/results/citation-verification.json")
    return fig


def quality(t: dict):
    d = load("skill-quality.json")
    scores = [s["score"] for s in d["skills"]]
    counts = Counter(min(int(s // 2) * 2, 98) for s in scores)
    mean = sum(scores) / len(scores)
    fig, ax = figure(t, 9, 3.6, f"All {len(scores)} skills score {int(min(scores))}+ on the quality rubric",
                     f"Static rubric: triggers, workflow, verification, references, tests · mean {mean:.1f} / 100")
    xs = list(range(80, 100, 2))
    ax.bar([x + 1 for x in xs], [counts.get(x, 0) for x in xs], width=1.7, color=t["skill"],
           edgecolor=t["surface"], linewidth=2)
    for x in xs:
        if counts.get(x):
            ax.text(x + 1, counts[x], str(counts[x]), ha="center", va="bottom", fontsize=9, color=t["text"])
    ax.grid(axis="x", visible=False)
    ax.grid(axis="y", color=t["grid"], linewidth=0.8)
    ax.set_xticks(range(80, 101, 2))
    ax.set_xlim(79.5, 100.5)
    ax.set_xlabel("score", color=t["text2"], fontsize=9)
    ax.set_ylabel("skills", color=t["text2"], fontsize=9)
    fig.subplots_adjust(left=0.08, right=0.97, top=0.76, bottom=0.24)
    footnote(fig, t, "Gate on every pull request: original skills must score 80 or more. "
                     "benchmarks/results/skill-quality.json")
    return fig


CHARTS = {"task-outcomes": task_outcomes, "slop": slop, "routing": routing, "citations": citations,
          "quality": quality}


def normalize(svg: bytes) -> str:
    """Round floats to 2 decimals so harmless platform float noise cannot fail --check."""
    return re.sub(r"-?\d+\.\d{3,}", lambda m: f"{float(m.group()):.2f}", svg.decode("utf-8"))


def render(fn, theme: str) -> bytes:
    plt.rcParams.update({"font.family": "sans-serif", "font.sans-serif": FONT, "svg.fonttype": "path",
                         "svg.hashsalt": "research-agent-skills", "axes.unicode_minus": False})
    fig = fn(THEMES[theme])
    buf = io.StringIO()
    fig.savefig(buf, format="svg", facecolor=fig.get_facecolor(), metadata={"Date": None, "Creator": None})
    plt.close(fig)
    return buf.getvalue().encode("utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="exit 1 if a committed chart differs from the results")
    args = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    stale = []
    for name, fn in CHARTS.items():
        for theme in THEMES:
            path = OUT / f"{name}-{theme}.svg"
            svg = render(fn, theme)
            if args.check:
                if not path.exists() or normalize(path.read_bytes()) != normalize(svg):
                    stale.append(path.relative_to(ROOT).as_posix())
            else:
                path.write_bytes(svg)
                print(f"wrote {path.relative_to(ROOT).as_posix()}")
    if stale:
        print("Out of date (run `uv run benchmarks/charts.py`):\n  " + "\n  ".join(stale), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
