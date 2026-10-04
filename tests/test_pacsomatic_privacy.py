"""Prevent patient identifiers from appearing in validation errors."""

import runpy
from pathlib import Path

import pytest


def test_invalid_patient_id_is_redacted(capsys):
    script = Path(__file__).resolve().parents[1] / "skills/pacsomatic/scripts/run_pacsomatic.py"
    ensure_no_spaces = runpy.run_path(str(script))["ensure_no_spaces"]
    private_id = "Jane Doe 12345"

    with pytest.raises(SystemExit):
        ensure_no_spaces("patient-id", private_id)

    error = capsys.readouterr().err
    assert "patient-id must not contain whitespace" in error
    assert private_id not in error
