import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize("skill", ["langchain", "crewai-multi-agent", "dspy", "guidance"])
def test_calculator_examples_allow_only_bounded_arithmetic(skill):
    path = ROOT / "skills" / skill / "scripts" / "safe_arithmetic.py"
    spec = importlib.util.spec_from_file_location(f"safe_arithmetic_{skill}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    assert module.calculate("(25 * 4) + 10") == 110
    for expression in ("__import__('os').system('echo unsafe')", "2 ** 1000", "1e309", "0 or 1"):
        with pytest.raises((ValueError, SyntaxError, OverflowError)):
            module.calculate(expression)
