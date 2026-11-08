#!/usr/bin/env python3
"""Zero-dependency Markdown lint and link checker for translation READMEs."""

from __future__ import annotations

import argparse
import html
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_FILE = ROOT / "README.md"

HTTP_OK = set(range(200, 400)) | {401, 403, 405, 406, 429}
USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)

INLINE_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+[\"'][^\"']*[\"'])?\)")
AUTOLINK_RE = re.compile(r"<(https?://[^>]+)>")
REF_DEF_RE = re.compile(r"^\s*\[[^\]]+\]:\s*(\S+)")
HTML_ATTR_RE = re.compile(r"""(?:href|src)\s*=\s*["']([^"']+)["']""")
BARE_URL_RE = re.compile(r"https?://[^\s<>\]\)]+")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
FENCE_RE = re.compile(r"^\s*(```+|~~~+)(.*)$")


def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()


def sanitize(lines: list[str]) -> list[str]:
    """Remove HTML comments and mask fenced code blocks for prose checks."""
    out: list[str] = []
    in_fence = False
    in_comment = False
    fence_marker = ""
    for line in lines:
        fence = FENCE_RE.match(line)
        if not in_fence and not in_comment and fence:
            in_fence = True
            fence_marker = fence.group(1)[:3]
            out.append("")
            continue
        if in_fence:
            if line.strip().startswith(fence_marker):
                in_fence = False
            out.append("")
            continue

        cleaned = []
        pos = 0
        while pos < len(line):
            if in_comment:
                end = line.find("-->", pos)
                if end == -1:
                    pos = len(line)
                else:
                    pos = end + 3
                    in_comment = False
            else:
                start = line.find("<!--", pos)
                if start == -1:
                    cleaned.append(line[pos:])
                    pos = len(line)
                else:
                    cleaned.append(line[pos:start])
                    pos = start + 4
                    in_comment = True
        out.append("".join(cleaned))
    return out


def lint(path: Path, lines: list[str]) -> list[str]:
    errors: list[str] = []
    prose = sanitize(lines)

    def add(rule: str, lineno: int, message: str) -> None:
        errors.append(f"{path}:{lineno}: {rule} {message}")

    if not lines:
        return [f"{path}:1: MD047 file is empty"]

    if lines[-1] == "":
        errors.append(f"{path}:{len(lines)}: MD047 file ends with extra blank line")
    if not path.read_bytes().endswith(b"\n"):
        errors.append(f"{path}:{len(lines)}: MD047 file must end with a newline")

    blank_run = 0
    for i, line in enumerate(lines, 1):
        if line.strip() == "":
            blank_run += 1
            if blank_run == 2:
                add("MD012", i, "multiple consecutive blank lines")
        else:
            blank_run = 0

        if "\t" in line and line.strip():
            add("MD010", i, "hard tab found")

        if line != line.rstrip():
            add("MD009", i, "trailing whitespace")

    for i, line in enumerate(prose, 1):
        match = HEADING_RE.match(line)
        if not match:
            continue
        level = len(match.group(1))
        if i > 1 and lines[i - 2].strip() != "":
            add("MD022", i, "heading should be preceded by a blank line")
        if i < len(lines) and lines[i].strip() != "":
            add("MD022", i, "heading should be followed by a blank line")

        previous = 0
        for j in range(i - 1, 0, -1):
            candidate = HEADING_RE.match(prose[j - 1])
            if candidate:
                previous = len(candidate.group(1))
                break
        if previous and level > previous + 1:
            add("MD001", i, f"heading level jumps from {previous} to {level}")

    headings = [len(m.group(1)) for m in (HEADING_RE.match(l) for l in prose) if m]
    if headings.count(1) > 1:
        add("MD025", 1, "more than one top-level heading")

    fence_start = None
    for i, line in enumerate(lines, 1):
        fence = FENCE_RE.match(line)
        if not fence:
            continue
        if fence_start is None:
            fence_start = i
            if not fence.group(2).strip():
                add("MD040", i, "fenced code block should specify a language")
            if i > 1 and lines[i - 2].strip() != "":
                add("MD031", i, "fenced code block should be preceded by a blank line")
        else:
            if i < len(lines) and lines[i].strip() != "":
                add("MD031", i, "fenced code block should be followed by a blank line")
            fence_start = None

    for i, line in enumerate(prose, 1):
        if not line.strip():
            continue
        if REF_DEF_RE.match(line):
            continue
        check = INLINE_LINK_RE.sub("", line)
        check = AUTOLINK_RE.sub("", check)
        check = HTML_ATTR_RE.sub("", check)
        check = re.sub(r"<[^>]+>", "", check)
        match = BARE_URL_RE.search(check)
        if match:
            add("MD034", i, f"bare URL should be wrapped in angle brackets: {match.group(0)}")

    return errors


def slugify(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text).strip().lower()
    text = re.sub(r"[^\w\- ]", "", text, flags=re.UNICODE)
    return text.replace(" ", "-")


def heading_slugs(lines: list[str]) -> set[str]:
    slugs: set[str] = set()
    counts: dict[str, int] = {}
    in_fence = False
    for line in lines:
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = HEADING_RE.match(line)
        if not match:
            continue
        base = slugify(match.group(2))
        slug = base
        if slug in counts:
            counts[base] += 1
            slug = f"{base}-{counts[base]}"
        else:
            counts[base] = 0
        slugs.add(slug)
    return slugs


def extract_links(lines: list[str]) -> list[tuple[int, str]]:
    links: list[tuple[int, str]] = []
    for i, line in enumerate(lines, 1):
        for match in INLINE_LINK_RE.finditer(line):
            links.append((i, html.unescape(match.group(1))))
        for match in AUTOLINK_RE.finditer(line):
            links.append((i, html.unescape(match.group(1))))
        match = REF_DEF_RE.match(line)
        if match:
            links.append((i, html.unescape(match.group(1))))
        for match in HTML_ATTR_RE.finditer(line):
            links.append((i, html.unescape(match.group(1))))
    return links


def to_uri(url: str) -> str:
    return urllib.parse.quote(url, safe=":/?#[]@!$&'()*+,;=%-._~")


def check_external(url: str, timeout: float) -> tuple[str, str]:
    """Return (status, detail) where status is ok, dead, or warn."""
    request = urllib.request.Request(
        to_uri(url),
        headers={"User-Agent": USER_AGENT, "Accept": "*/*"},
        method="GET",
    )
    last_error = ""
    for _ in range(2):
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                if response.status in HTTP_OK:
                    return "ok", str(response.status)
                state = "dead" if response.status in {404, 410} else "warn"
                return state, f"HTTP {response.status}"
        except urllib.error.HTTPError as exc:
            if exc.code in HTTP_OK:
                return "ok", f"HTTP {exc.code}"
            state = "dead" if exc.code in {404, 410} else "warn"
            return state, f"HTTP {exc.code}"
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            last_error = str(exc)
    return "warn", last_error or "network error"


def check_links(
    path: Path, lines: list[str], external: bool, timeout: float
) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    targets: list[tuple[int, str]] = []
    root = path.parent
    anchors_by_file: dict[Path, set[str]] = {path: heading_slugs(lines)}

    for lineno, raw in extract_links(lines):
        target = raw.strip()
        if not target or target.startswith(("mailto:", "tel:", "data:")):
            continue
        parsed = urllib.parse.urlsplit(target)
        if parsed.scheme in {"http", "https"}:
            targets.append((lineno, target))
            continue
        if parsed.scheme:
            continue

        file_part = urllib.parse.unquote(parsed.path)
        if file_part:
            local = (root / file_part).resolve()
            try:
                local.relative_to(root.resolve())
            except ValueError:
                errors.append(f"{path}:{lineno}: link escapes repository: {target}")
                continue
            if not local.exists():
                errors.append(f"{path}:{lineno}: missing local target: {target}")
                continue
            if parsed.fragment and local.suffix.lower() == ".md":
                if local not in anchors_by_file:
                    anchors_by_file[local] = heading_slugs(read_lines(local))
                if parsed.fragment not in anchors_by_file[local]:
                    errors.append(f"{path}:{lineno}: missing anchor: {target}")
        elif parsed.fragment and parsed.fragment not in anchors_by_file[path]:
            errors.append(f"{path}:{lineno}: missing anchor: {target}")

    if not external:
        return errors, warnings

    unique = sorted({url for _, url in targets})
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = {pool.submit(check_external, url, timeout): url for url in unique}
        for future in as_completed(futures):
            url = futures[future]
            status, detail = future.result()
            lines_with = ",".join(str(n) for n, u in targets if u == url)
            if status == "dead":
                errors.append(f"{path}:{lines_with}: dead link ({detail}): {url}")
            elif status == "warn":
                warnings.append(f"{path}:{lines_with}: unverified link ({detail}): {url}")
    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", type=Path, default=[DEFAULT_FILE])
    parser.add_argument("--external", action="store_true", help="check external URLs over the network")
    parser.add_argument("--timeout", type=float, default=15.0, help="per-request timeout in seconds")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="treat unreachable or unverified external links as failures",
    )
    args = parser.parse_args()

    files = [f if f.is_absolute() else (ROOT / f) for f in args.files]
    all_errors: list[str] = []
    all_warnings: list[str] = []
    for path in files:
        if not path.exists():
            all_errors.append(f"{path}: file not found")
            continue
        lines = read_lines(path)
        all_errors.extend(lint(path, lines))
        errors, warnings = check_links(path, lines, args.external, args.timeout)
        all_errors.extend(errors)
        all_warnings.extend(warnings)

    if args.strict:
        all_errors.extend(all_warnings)
        all_warnings = []

    if all_warnings:
        print("Warnings (not fatal):", file=sys.stderr)
        print("\n".join(all_warnings), file=sys.stderr)
    if all_errors:
        print("\n".join(all_errors), file=sys.stderr)
        print(f"\n{len(all_errors)} problem(s) found", file=sys.stderr)
        return 1
    print(
        f"OK: {len(files)} file(s) checked "
        f"(external links: {'yes' if args.external else 'no'}, "
        f"warnings: {len(all_warnings)})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
