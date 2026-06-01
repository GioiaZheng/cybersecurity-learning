"""Repository safety scan for learning notes and writeups."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


TEXT_EXTENSIONS = {
    ".md",
    ".py",
    ".txt",
    ".yml",
    ".yaml",
    ".json",
    ".sh",
}

SKIP_DIRS = {
    ".git",
    "__pycache__",
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    "venv",
}

PLACEHOLDER_FLAG_VALUES = {
    "...",
    "something_here",
    "redacted",
    "omitted",
    "flag_omitted",
    "flag omitted",
}


@dataclass(frozen=True)
class Finding:
    path: Path
    line_number: int
    rule: str
    excerpt: str


@dataclass(frozen=True)
class Rule:
    name: str
    pattern: re.Pattern[str]


RULES = [
    Rule("private-key", re.compile(r"-----BEGIN [A-Z0-9 ]*PRIVATE KEY-----")),
    Rule("aws-access-key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    Rule("github-token", re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{30,}\b")),
    Rule("slack-token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b")),
    Rule("ctf-flag", re.compile(r"\b(?:THM|HTB|picoCTF|flag|crypto)\{([^}\n]+)\}")),
]


def _is_placeholder_flag(match: re.Match[str]) -> bool:
    if match.lastindex != 1:
        return False
    value = match.group(1).strip().lower()
    return value in PLACEHOLDER_FLAG_VALUES or "..." in value


def _iter_text_files(root: Path):
    for path in root.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if not path.is_file():
            continue
        if path.suffix.lower() in TEXT_EXTENSIONS:
            yield path


def scan_file(path: Path) -> list[Finding]:
    findings: list[Finding] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError:
        return findings

    for line_number, line in enumerate(lines, start=1):
        for rule in RULES:
            for match in rule.pattern.finditer(line):
                if rule.name == "ctf-flag" and _is_placeholder_flag(match):
                    continue
                findings.append(
                    Finding(
                        path=path,
                        line_number=line_number,
                        rule=rule.name,
                        excerpt=line.strip()[:160],
                    )
                )
    return findings


def scan_repository(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    for path in _iter_text_files(root):
        findings.extend(scan_file(path))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()

    root = args.root.resolve()
    findings = scan_repository(root)
    if findings:
        print("Security review failed:")
        for finding in findings:
            rel = finding.path.resolve().relative_to(root)
            print(f"  {rel}:{finding.line_number}: {finding.rule}: {finding.excerpt}")
        return 1

    print("Security review passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
