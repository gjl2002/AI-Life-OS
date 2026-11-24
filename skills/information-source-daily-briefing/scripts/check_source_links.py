#!/usr/bin/env python3
"""Check that briefing source URLs are present as clickable Markdown links."""

import argparse
import html
import json
import re
from pathlib import Path

CODE = re.compile(r"^ {0,3}(`{3,}|~{3,})[^\n]*\n.*?^ {0,3}\1[ \t]*$|`+[^`\n]+`+", re.M | re.S)
LINK = re.compile(
    r"(?<!\\)(?P<image>!?)\[(?:\\.|[^\]\\\n])+\]\(\s*(?:"
    r"<(?P<angled>https?://[^<>\n]+)>|"
    r"(?P<plain>https?://(?:\\.|[^\s()\\]|\([^\s()]*\))+))"
    r"(?:[ \t]+[\"'][^\n]*?[\"'])?[ \t]*\)"
    r"|<(?P<autolink>https?://[^<>\s]+)>"
)


def normalize(url: str) -> str:
    return html.unescape(re.sub(r"\\([()])", r"\1", url.strip()))


def missing_links(expected: list[str], markdown: str) -> list[str]:
    text = CODE.sub("", markdown)
    linked = {
        normalize(match.group("angled") or match.group("plain") or match.group("autolink"))
        for match in LINK.finditer(text)
        if not match.group("image")
    }
    return sorted({normalize(url) for url in expected if url.strip()} - linked)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--expected", type=Path, required=True, help="One source URL per line")
    parser.add_argument("--markdown", type=Path, required=True, help="Draft or Notion readback Markdown")
    args = parser.parse_args()
    expected = args.expected.read_text(encoding="utf-8").splitlines()
    markdown = args.markdown.read_text(encoding="utf-8")
    missing = missing_links(expected, markdown)
    print(json.dumps({"ok": not missing, "missing_urls": missing}, ensure_ascii=False))
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
