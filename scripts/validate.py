#!/usr/bin/env python3
"""Check this repository's packaging; behavioral evaluation is separate."""

import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


def validate(root: Path) -> list[str]:
    errors = []
    required = ("SKILL.md", "agents/openai.yaml", "references/evaluation.md",
                "references/source-review.md", "references/hands-on.md", "evals/cases.json")
    for name in required:
        if not (root / name).is_file():
            errors.append(f"Missing required file: {name}")
    if errors:
        return errors

    # This skill uses simple one-line frontmatter. This is not a general YAML parser.
    skill = (root / "SKILL.md").read_text(encoding="utf-8")
    header = re.match(r"\A---\n(.*?)\n---\n", skill, re.S)
    if not header:
        errors.append("SKILL.md requires YAML frontmatter")
    else:
        fields = dict(re.findall(r"^([a-z_-]+): (.+)$", header[1], re.M))
        if fields.get("name") != "security-micro-training":
            errors.append("Unexpected skill name")
        if not fields.get("description", "").strip():
            errors.append("Missing skill description")

    for page in sorted(root.rglob("*.md")):
        if ".git" in page.parts:
            continue
        for target in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", page.read_text(encoding="utf-8")):
            link = urlsplit(target.strip("<>"))
            if link.scheme or link.netloc or not link.path:
                continue
            resolved = (page.parent / unquote(link.path)).resolve()
            if not resolved.is_relative_to(root.resolve()) or not resolved.exists():
                errors.append(f"Broken or external local link in {page.relative_to(root)}: {target}")

    try:
        suite = json.loads((root / "evals/cases.json").read_text(encoding="utf-8"))
        if not isinstance(suite, dict) or suite.get("schema_version") != 1:
            raise ValueError("Expected schema_version 1")
        cases = suite.get("cases")
        if not isinstance(cases, list) or not cases:
            raise ValueError("Expected nonempty cases list")
        seen = set()
        for case in cases:
            if not isinstance(case, dict):
                raise ValueError("Case must be an object")
            for field in ("id", "prompt", "environment"):
                if not isinstance(case.get(field), str) or not case[field].strip():
                    raise ValueError(f"Case needs nonempty {field}")
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", case["id"]):
                raise ValueError(f"Invalid case id: {case['id']}")
            if case["id"] in seen:
                raise ValueError(f"Duplicate case id: {case['id']}")
            seen.add(case["id"])
            for field in ("followups", "expectations"):
                value = case.get(field)
                if not isinstance(value, list) or any(not isinstance(v, str) or not v.strip() for v in value):
                    raise ValueError(f"{case['id']}: {field} must be a list of nonempty strings")
            if not case["expectations"]:
                raise ValueError(f"{case['id']}: missing expectations")
    except (ValueError, TypeError) as exc:
        errors.append(f"Invalid evaluation suite: {exc}")
    return errors


if __name__ == "__main__":
    project = Path(__file__).resolve().parents[1]
    problems = validate(project)
    if problems:
        print("\n".join(problems), file=sys.stderr)
        sys.exit(1)
    print("Packaging, local links, and evaluation schema passed. Behavioral tests are separate.")
