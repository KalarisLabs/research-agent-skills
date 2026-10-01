"""Smoke tests for every script shipped in skills/ (original and adapted), on every CI OS.

1. Every script compiles.
2. Every script with an argparse CLI and standard-library-only top-level imports runs
   `--help` offline. It must exit 0, or exit with a clear "install X" message when an optional
   scientific dependency is missing. A raw Python traceback is a failure.
"""

from __future__ import annotations

import os
import subprocess
import sys

import pytest
from script_inventory import SKILLS, help_testable, scripts

ALL = scripts()
HELP = [p for p in ALL if help_testable(p)]
ENV = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONIOENCODING="utf-8")


def _id(p):
    return p.relative_to(SKILLS).as_posix()


@pytest.mark.parametrize("path", ALL, ids=_id)
def test_script_compiles(path):
    compile(path.read_text(encoding="utf-8"), str(path), "exec")


@pytest.mark.parametrize("path", HELP, ids=_id)
def test_script_help_runs_offline(path):
    r = subprocess.run([sys.executable, str(path), "--help"], capture_output=True, text=True, encoding="utf-8",
                       errors="replace", timeout=60, cwd=path.parent, env=ENV)
    output = r.stdout + r.stderr
    assert "Traceback (most recent call last)" not in output, output[-1500:]
    if r.returncode != 0:
        assert any(w in output.lower() for w in ("install", "required", "not installed")), output[-800:]


def test_inventory_is_meaningful():
    assert len(ALL) > 400 and len(HELP) > 250
