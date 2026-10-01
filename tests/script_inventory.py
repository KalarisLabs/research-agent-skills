"""Inventory of skill scripts for smoke tests: which compile, and which can run `--help` offline.

A script is "help-testable" when it defines an argparse CLI behind `if __name__ == "__main__"` and
imports only the standard library or sibling modules from its own scripts/ folder, so it runs
without installing the scientific packages it documents.
"""

from __future__ import annotations

import ast
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
STDLIB = set(sys.stdlib_module_names) | {"__future__"}


def scripts() -> list[Path]:
    return sorted(p for p in SKILLS.glob("*/scripts/**/*.py") if "__pycache__" not in p.parts)


def top_imports(tree: ast.AST) -> set[str]:
    """Module-level imports only (imports inside functions are optional/lazy)."""
    names: set[str] = set()
    for node in getattr(tree, "body", []):
        nodes = [node]
        if isinstance(node, (ast.If, ast.Try)):  # e.g. `try: import x except ImportError`
            continue
        for n in nodes:
            if isinstance(n, ast.Import):
                names.update(a.name.split(".")[0] for a in n.names)
            elif isinstance(n, ast.ImportFrom) and n.level == 0 and n.module:
                names.add(n.module.split(".")[0])
    return names


def help_testable(path: Path) -> bool:
    try:
        source = path.read_text(encoding="utf-8")
        tree = ast.parse(source)
    except (SyntaxError, UnicodeDecodeError):
        return False
    if "argparse" not in source or "__main__" not in source:
        return False
    siblings = {p.stem for p in path.parent.glob("*.py")} | {p.name for p in path.parent.iterdir() if p.is_dir()}
    return all(m in STDLIB or m in siblings for m in top_imports(tree))
