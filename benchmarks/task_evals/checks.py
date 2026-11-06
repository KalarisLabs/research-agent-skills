"""Deterministic checks for task answers (no LLM involved).

Each task in heldout.json may carry a ``checks`` mapping. Every key is one check; an answer
passes a task's checks only if it passes all of them. Most checks enforce a constraint the
prompt itself states (word limit, required element), so they do not depend on remembered
venue rules.

    max_words / min_words     whitespace-separated words in the whole answer
    max_chars                 characters in the whole answer (stripped)
    max_sentences             sentences in the whole answer
    max_paragraphs            blocks separated by blank lines
    line_count                exact number of non-empty lines (bullet markers stripped)
    line_count_range          [min, max] non-empty lines
    max_line_chars            every non-empty line, bullet markers stripped, is at most N characters
    max_list_items            top-level bullet or numbered items
    must_match                every regex matches (case-insensitive, multiline)
    must_not_match            no regex matches
    order                     the strings appear in this order
    dois_resolve              every DOI in the answer is registered (doi.org handle API)
    max_slop_index            unslop-academic-writing linter score is at most N
"""

from __future__ import annotations

import functools
import importlib.util
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FENCE_RE = re.compile(r"^\s*```.*$", re.M)
BULLET_RE = re.compile(r"^\s*(?:[-*•–]|\d+[.)])\s+")
DOI_RE = re.compile(r"\b10\.\d{4,9}/[^\s\"'<>\]\[(){},;]+", re.I)
FLAGS = re.I | re.M


def _lines(text: str) -> list[str]:
    """Handle lines."""
    body = FENCE_RE.sub("", text)
    return [BULLET_RE.sub("", ln).strip() for ln in body.splitlines() if ln.strip()]


def _list_items(text: str) -> int:
    """List items."""
    return sum(1 for ln in text.splitlines() if re.match(r"^(?:[-*•]|\d+[.)])\s+", ln))


def _sentences(text: str) -> int:
    """Handle sentences."""
    return len([s for s in re.split(r"(?<=[.!?])\s+(?=[A-Z0-9\"'(])", text.strip()) if s])


@functools.cache
def doi_registered(doi: str) -> bool:
    """True if doi.org knows the DOI (handle API responseCode 1)."""
    url = "https://doi.org/api/handles/" + urllib.parse.quote(doi, safe="/")
    req = urllib.request.Request(url, headers={"User-Agent": "research-agent-skills-benchmark/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:  # noqa: S310 - fixed https host
            return json.loads(r.read().decode("utf-8")).get("responseCode") == 1
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return False
        raise


@functools.lru_cache(maxsize=1)
def _slop():
    """Handle slop."""
    sys.dont_write_bytecode = True  # never leave __pycache__ inside skills/
    path = ROOT / "skills" / "unslop-academic-writing" / "scripts" / "slop_check.py"
    spec = importlib.util.spec_from_file_location("slop_check", path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["slop_check"] = mod
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod


def extract_dois(text: str) -> list[str]:
    """Extract dois."""
    return sorted({m.rstrip(".") for m in DOI_RE.findall(text)})


def run_checks(text: str, checks: dict) -> dict[str, bool]:
    """Return {check_name: passed} for every check configured on a task."""
    words = len(text.split())
    out: dict[str, bool] = {}
    for name, arg in checks.items():
        if name == "max_words":
            out[name] = words <= arg
        elif name == "min_words":
            out[name] = words >= arg
        elif name == "max_chars":
            out[name] = len(text.strip()) <= arg
        elif name == "max_sentences":
            out[name] = _sentences(text) <= arg
        elif name == "max_paragraphs":
            out[name] = len([p for p in re.split(r"\n\s*\n", text.strip()) if p.strip()]) <= arg
        elif name == "line_count":
            out[name] = len(_lines(text)) == arg
        elif name == "line_count_range":
            out[name] = arg[0] <= len(_lines(text)) <= arg[1]
        elif name == "max_line_chars":
            out[name] = all(len(ln) <= arg for ln in _lines(text))
        elif name == "max_list_items":
            out[name] = _list_items(text) <= arg
        elif name == "must_match":
            out[name] = all(re.search(rx, text, FLAGS) for rx in arg)
        elif name == "must_not_match":
            out[name] = not any(re.search(rx, text, FLAGS) for rx in arg)
        elif name == "order":
            pos = [text.find(s) for s in arg]
            out[name] = all(p >= 0 for p in pos) and pos == sorted(pos)
        elif name == "dois_resolve":
            out[name] = all(doi_registered(d) for d in extract_dois(text))
        elif name == "max_slop_index":
            out[name] = _slop().analyse(text)["slop_index"] <= arg
        else:
            raise ValueError(f"unknown check '{name}'")
    return out
