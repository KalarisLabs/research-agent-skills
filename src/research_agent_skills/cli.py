"""Command line interface for research-agent-skills Python distribution."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import __version__
from .catalog import load_catalog
from .configure import auto_configure_all
from .harness import get_harnesses, resolve_harnesses
from .install import install_skills_to_dir, locate_local_skills_root, read_lock


def cmd_list(args: argparse.Namespace) -> int:
    """Run the list subcommand."""
    catalog = load_catalog()
    if args.categories:
        print(f"Categories in Research Agent Skills ({len(catalog.categories)}):")
        for c in catalog.categories:
            print(f"  {c.id:<32} ({c.count} skills) - {c.description}")
        return 0

    if args.category:
        skills = [s for s in catalog.skills if s.category == args.category]
        if not skills:
            print(f"No skills found in category '{args.category}'")
            return 1
        print(f"Skills in category '{args.category}' ({len(skills)}):")
    else:
        skills = catalog.skills
        print(f"Research Agent Skills v{catalog.version} ({len(skills)} skills):")

    for s in skills:
        scripts_tag = " [scripts]" if s.has_scripts else ""
        print(f"  {s.name:<32} {s.category:<22}{scripts_tag}")
        print(f"    {s.description[:90]}...")
    return 0


def cmd_search(args: argparse.Namespace) -> int:
    """Run the search subcommand."""
    catalog = load_catalog()
    results = catalog.search(args.query)
    if not results:
        print(f"No skills matched '{args.query}'")
        return 0
    print(f"Matches for '{args.query}' ({len(results)}):")
    for s in results[:25]:
        scripts_tag = " [scripts]" if s.has_scripts else ""
        print(f"  {s.name:<32} ({s.category}){scripts_tag}")
        print(f"    {s.description[:100]}...")
    if len(results) > 25:
        print(f"  ... and {len(results) - 25} more (use a more specific query)")
    return 0


def cmd_install(args: argparse.Namespace) -> int:
    """Run the install subcommand."""
    catalog = load_catalog()
    bundle_list = [b.strip() for b in args.bundle.split(",")] if args.bundle else None
    cat_list = [c.strip() for c in args.category.split(",")] if args.category else None

    # If no skills, category, or bundle specified, default to research-essentials
    if not args.skills and not bundle_list and not cat_list and not args.all:
        bundle_list = ["research-essentials"]
        print("No skills specified; defaulting to bundle 'research-essentials'")

    try:
        selected = catalog.select(
            names=args.skills,
            categories=cat_list,
            bundles=bundle_list,
            all_skills=args.all,
        )
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    if not selected:
        print("No skills selected to install.")
        return 0

    harness_list = resolve_harnesses(args.harness)
    print(f"Installing {len(selected)} skill(s) into target harnesses:")

    cwd = Path.cwd()
    mode = "symlink" if args.symlink else "copy"

    for h in harness_list:
        target_dir = (cwd / h.project_dir) if args.project else h.global_dir
        scope = f"project ({target_dir})" if args.project else f"global ({target_dir})"
        print(f"\n  -> {h.label} [{scope}]:")
        installed = install_skills_to_dir(
            skills=selected,
            target_dir=target_dir,
            catalog=catalog,
            mode=mode,
            force=args.force,
            dry_run=args.dry_run,
        )
        for name in installed:
            print(f"     + {name}")

    if getattr(args, "configure", False) and not args.dry_run:
        print("\nAuto-configuring instruction anchors and manifests:")
        cfg_results = auto_configure_all(harness_list, cwd, selected)
        for r in cfg_results:
            status = "+ created" if r.action == "created" else "~ updated" if r.action == "updated" else "= unchanged"
            print(f"  {status} {r.file} ({r.harness})")

    print("\nInstallation complete!")
    return 0


def cmd_configure(args: argparse.Namespace) -> int:
    """Run the configure subcommand."""
    harness_list = resolve_harnesses(args.harness)
    print(f"Auto-configuring instruction anchors for {len(harness_list)} harness(es):")
    results = auto_configure_all(harness_list, Path.cwd())
    for r in results:
        status = "+ created" if r.action == "created" else "~ updated" if r.action == "updated" else "= unchanged"
        print(f"  {status} {r.file} ({r.harness})")
    print("\nDone. Harnesses configured.")
    return 0


def cmd_installed(args: argparse.Namespace) -> int:
    """Run the installed subcommand."""
    harnesses = get_harnesses()
    cwd = Path.cwd()
    found_any = False

    for h in harnesses:
        for scope_name, target_dir in [("project", cwd / h.project_dir), ("global", h.global_dir)]:
            lock = read_lock(target_dir)
            if lock and lock.get("skills"):
                found_any = True
                skills = lock["skills"]
                print(f"{h.label} ({scope_name}: {target_dir}): {len(skills)} skills")
                for s_name, meta in sorted(skills.items()):
                    print(f"  - {s_name} (v{meta.get('version', '1.0')}, {meta.get('mode', 'copy')})")

    if not found_any:
        print("No skills installed by research-agent-skills detected in project or global harnesses.")
    return 0


def cmd_doctor(args: argparse.Namespace) -> int:
    """Run the doctor subcommand."""
    print(f"research-agent-skills v{__version__} Doctor Diagnostics\n")
    catalog = load_catalog()
    print(f"Catalog loaded: {len(catalog.skills)} skills across {len(catalog.categories)} categories")

    local_root = locate_local_skills_root()
    if local_root:
        print(f"Local checkout detected: {local_root}")
    else:
        print("Running in standalone distribution mode (releases fetched from GitHub)")

    print("\nDetected Agent Harnesses:")
    harnesses = get_harnesses()
    for h in harnesses:
        present = h.is_present()
        status = "FOUND" if present else "not found"
        print(f"  [{status:<9}] {h.label:<28} -> global: {h.global_dir}")

    return 0


def main(argv: list[str] | None = None) -> int:
    """Run the command-line interface."""
    parser = argparse.ArgumentParser(
        prog="research-agent-skills",
        description=f"Research Agent Skills v{__version__} (Python package & CLI)",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # install
    p_install = subparsers.add_parser("install", help="Install skills into agent harnesses")
    p_install.add_argument("skills", nargs="*", help="Skill names to install")
    p_install.add_argument("--bundle", "-b", help="Curated bundle (e.g. research-essentials, ml-research)")
    p_install.add_argument("--category", "-c", help="Category of skills")
    p_install.add_argument("--all", action="store_true", help="Install all skills (not recommended)")
    p_install.add_argument(
        "--harness",
        help="Target harness (claude-code, codex, cursor, gemini-cli, antigravity, copilot, opencode, ...)",
    )
    p_install.add_argument("--project", action="store_true", help="Install into current project instead of global home")
    p_install.add_argument("--symlink", action="store_true", help="Symlink instead of copy (when using local repo)")
    p_install.add_argument("--force", action="store_true", help="Overwrite existing folders")
    p_install.add_argument("--dry-run", action="store_true", help="Simulate without writing files")
    p_install.add_argument(
        "--configure",
        action="store_true",
        help="Auto-configure harness instruction anchors and manifests",
    )

    # configure
    p_configure = subparsers.add_parser(
        "configure",
        help="Auto-configure instruction anchors and manifests for harnesses",
    )
    p_configure.add_argument("--harness", help="Target harness (claude-science, t3-code, antigravity, aider, etc.)")

    # list
    p_list = subparsers.add_parser("list", help="List available skills or categories")
    p_list.add_argument("--category", "-c", help="Filter by category")
    p_list.add_argument("--categories", action="store_true", help="List categories only")

    # search
    p_search = subparsers.add_parser("search", help="Search skills by name, description, or tags")
    p_search.add_argument("query", help="Keyword or phrase")

    # installed
    subparsers.add_parser("installed", help="Display installed skills across harnesses")

    # doctor
    subparsers.add_parser("doctor", help="Check agent harnesses, environment, and catalog")

    args = parser.parse_args(argv)

    if not args.command:
        # Default to interactive/help
        parser.print_help()
        return 0

    commands = {
        "list": cmd_list,
        "search": cmd_search,
        "install": cmd_install,
        "configure": cmd_configure,
        "installed": cmd_installed,
        "doctor": cmd_doctor,
    }

    handler = commands.get(args.command)
    if handler:
        return handler(args)

    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
