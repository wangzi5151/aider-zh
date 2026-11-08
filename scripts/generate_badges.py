#!/usr/bin/env python3
"""Generate the static badge block in README.md without third-party tools."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
START = "<!-- badges:start -->"
END = "<!-- badges:end -->"

# Snapshot values copied from the upstream README. Update them deliberately
# after checking the upstream source; do not treat them as live figures.
INSTALLS = "6.8M"
TOKENS_PER_WEEK = "15B"
OPENROUTER_RANK = "Top%2020"
SINGULARITY = "88"
REPO = "Aider-AI/aider"


def badges() -> str:
    return f'''  <a href="https://github.com/{REPO}/stargazers"><img alt="GitHub Stars" title="Total number of GitHub stars the Aider project has received"
src="https://img.shields.io/github/stars/{REPO}?style=flat-square&logo=github&color=f1c40f&labelColor=555555"/></a>
  <a href="https://pypi.org/project/aider-chat/"><img alt="PyPI Downloads" title="Total number of installations via pip from PyPI"
src="https://img.shields.io/badge/📦%20Installs-{INSTALLS}-2ecc71?style=flat-square&labelColor=555555"/></a>
  <img alt="Tokens per week" title="Number of tokens processed weekly by Aider users"
src="https://img.shields.io/badge/📈%20Tokens%2Fweek-{TOKENS_PER_WEEK}-3498db?style=flat-square&labelColor=555555"/>
  <a href="https://openrouter.ai/#options-menu"><img alt="OpenRouter Ranking" title="Aider's ranking among applications on the OpenRouter platform"
src="https://img.shields.io/badge/🏆%20OpenRouter-{OPENROUTER_RANK}-9b59b6?style=flat-square&labelColor=555555"/></a>
  <a href="https://aider.chat/HISTORY.html"><img alt="Singularity" title="Percentage of the new code in Aider's last release written by Aider itself"
src="https://img.shields.io/badge/🔄%20Singularity-{SINGULARITY}%25-e74c3c?style=flat-square&labelColor=555555"/></a>'''


def block_bounds(text: str) -> tuple[int, int]:
    start = text.index(START) + len(START)
    end = text.index(END, start)
    return start, end


def current_block(text: str) -> str:
    start, end = block_bounds(text)
    return text[start:end].strip("\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="verify README matches generated output")
    parser.add_argument("--write", action="store_true", help="update README in place")
    args = parser.parse_args()

    text = README.read_text(encoding="utf-8")
    expected = badges()
    actual = current_block(text)

    if args.write:
        start, end = block_bounds(text)
        replacement = f"\n{expected}\n"
        README.write_text(text[:start] + replacement + text[end:], encoding="utf-8")
        print("Updated badge block")
        return 0

    if args.check:
        if actual == expected:
            print("OK: badge block matches generated output")
            return 0
        print("Badge block differs from generated output; run --write", file=sys.stderr)
        return 1

    print(expected)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
