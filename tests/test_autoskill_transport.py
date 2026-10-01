import importlib.util
from pathlib import Path

import pytest

BACKENDS = Path(__file__).resolve().parents[1] / "skills" / "autoskill" / "scripts" / "backends.py"


def _load_backends():
    spec = importlib.util.spec_from_file_location("autoskill_backends_test", BACKENDS)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_remote_screenpipe_endpoint_requires_https():
    check = _load_backends().check_remote_endpoint
    assert check("http://localhost:3030", "screenpipe") == "http://localhost:3030"
    assert check("https://research.example/screenpipe", "screenpipe") == "https://research.example/screenpipe"
    with pytest.raises(ValueError, match="plaintext HTTP"):
        check("http://research.example/screenpipe", "screenpipe")
