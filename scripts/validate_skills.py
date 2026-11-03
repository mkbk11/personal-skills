#!/usr/bin/env python3
"""Validate Agent Skill metadata and repository-local Markdown links."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

import yaml

ROOT = Path(__file__).resolve().parents[1]
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER_RE = re.compile(r"\A---\s*\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", re.S)
LINK_RE = re.compile(r"!??\[[^\]]*\]\(([^)]+)\)")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def local_link_target(raw_target: str) -> str | None:
    target = raw_target.strip().split()[0].strip("<>")
    parsed = urlparse(target)
    if parsed.scheme or parsed.netloc or target.startswith(("#", "/")):
        return None
    return unquote(parsed.path)


def validate_markdown_links(path: Path, errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for match in LINK_RE.finditer(text):
        raw_target = match.group(1)
        target = local_link_target(raw_target)
        if target is None or not target:
            continue
        resolved = (path.parent / target).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            fail(errors, f"{path.relative_to(ROOT)}: link escapes repository: {raw_target}")
            continue
        if not resolved.exists():
            fail(errors, f"{path.relative_to(ROOT)}: broken local link: {raw_target}")


def validate_skill(skill_dir: Path, errors: list[str], warnings: list[str]) -> None:
    skill_file = skill_dir / "SKILL.md"
    relative_dir = skill_dir.relative_to(ROOT)

    if not skill_file.is_file():
        fail(errors, f"{relative_dir}: missing SKILL.md")
        return

    content = skill_file.read_text(encoding="utf-8")
    if len(content.splitlines()) > 500:
        warnings.append(f"{relative_dir}/SKILL.md: over 500 lines; consider moving detail into references/")

    match = FRONTMATTER_RE.match(content)
    if not match:
        fail(errors, f"{relative_dir}/SKILL.md: missing or malformed YAML frontmatter")
        return

    try:
        metadata = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        fail(errors, f"{relative_dir}/SKILL.md: invalid YAML frontmatter: {exc}")
        return

    if not isinstance(metadata, dict):
        fail(errors, f"{relative_dir}/SKILL.md: frontmatter must be a YAML mapping")
        return

    name = metadata.get("name")
    description = metadata.get("description")

    if not isinstance(name, str) or not NAME_RE.fullmatch(name):
        fail(errors, f"{relative_dir}/SKILL.md: name must be lowercase kebab-case")
    elif name != skill_dir.name:
        fail(errors, f"{relative_dir}/SKILL.md: name '{name}' does not match directory '{skill_dir.name}'")

    if not isinstance(description, str) or not description.strip():
        fail(errors, f"{relative_dir}/SKILL.md: description must be a non-empty string")
    elif len(description) > 1024:
        fail(errors, f"{relative_dir}/SKILL.md: description exceeds 1024 characters")

    openai_yaml = skill_dir / "agents" / "openai.yaml"
    if openai_yaml.exists():
        try:
            interface_data = yaml.safe_load(openai_yaml.read_text(encoding="utf-8"))
            if not isinstance(interface_data, dict) or not isinstance(interface_data.get("interface"), dict):
                fail(errors, f"{openai_yaml.relative_to(ROOT)}: expected an 'interface' mapping")
        except yaml.YAMLError as exc:
            fail(errors, f"{openai_yaml.relative_to(ROOT)}: invalid YAML: {exc}")

    for markdown_file in skill_dir.rglob("*.md"):
        validate_markdown_links(markdown_file, errors)


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    skill_dirs = sorted(
        path for path in ROOT.iterdir()
        if path.is_dir() and (path / "SKILL.md").is_file()
    )

    if not skill_dirs:
        print("ERROR: no Skill directories containing SKILL.md were found.")
        return 1

    seen_names: set[str] = set()
    for skill_dir in skill_dirs:
        if skill_dir.name in seen_names:
            fail(errors, f"duplicate skill directory name: {skill_dir.name}")
        seen_names.add(skill_dir.name)
        validate_skill(skill_dir, errors, warnings)

    # Check local links in repository-level Markdown documentation too.
    for markdown_file in ROOT.glob("*.md"):
        validate_markdown_links(markdown_file, errors)
    docs_dir = ROOT / "docs"
    if docs_dir.exists():
        for markdown_file in docs_dir.rglob("*.md"):
            validate_markdown_links(markdown_file, errors)

    print(f"Checked {len(skill_dirs)} Skill(s): {', '.join(path.name for path in skill_dirs)}")
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        print(f"Validation failed with {len(errors)} error(s).")
        return 1

    print("Validation passed: metadata and repository-local Markdown links look valid.")
    print("Note: this is a structural check, not a content-quality or security audit.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
