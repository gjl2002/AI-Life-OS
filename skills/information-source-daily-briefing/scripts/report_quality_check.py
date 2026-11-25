#!/usr/bin/env python3
"""Validate a briefing's source coverage, time window and clickable links."""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path
from urllib.parse import urlsplit

from check_source_links import CODE, missing_links, normalize

UPDATED = "有已验证更新"
NO_UPDATES = "已验证暂无更新"
UNVERIFIED = "未能验证"
STATUSES = {UPDATED, NO_UPDATES, UNVERIFIED}
SECTIONS = ("今日核心判断", "信息源读取覆盖", "今日新增")
HEADING = re.compile(r"^ {0,3}#{1,6}[ \t]+(.+?)[ \t]*#*[ \t]*$", re.M)


def timestamp(value: str) -> datetime:
    time = datetime.fromisoformat(value[:-1] + "+00:00" if value.endswith("Z") else value)
    if time.utcoffset() is None:
        raise ValueError(f"时间缺少时区：{value}")
    return time


def source_url(value: str) -> str:
    url = normalize(value)
    parts = urlsplit(url)
    if parts.scheme not in {"http", "https"} or not parts.hostname:
        raise ValueError(f"无效的来源链接：{value}")
    return url


def check_report(plan: dict, markdown: str) -> list[str]:
    errors: list[str] = []
    start = timestamp(plan["window_start"])
    end = timestamp(plan["window_end"])
    if start >= end:
        errors.append("时间窗口的起点必须早于终点")

    followed = plan["followed_sources"]
    if not isinstance(followed, list) or not all(isinstance(name, str) and name.strip() for name in followed):
        raise ValueError("followed_sources 必须是非空来源名称的列表")
    if len(set(followed)) != len(followed):
        errors.append("关注名单有重名，请为重名来源添加能区分的名称")

    coverage: dict[str, str] = {}
    candidates: set[str] = set()
    for row in plan["coverage"]:
        name, status = row["source"], row["status"]
        updates = row["updates"]
        if name in coverage:
            errors.append(f"覆盖结果重复：{name}")
        coverage[name] = status
        if status not in STATUSES or not row["detail"].strip():
            errors.append(f"覆盖状态或核验说明无效：{name}")
        if not isinstance(updates, list) or bool(updates) != (status == UPDATED):
            errors.append(f"更新条目与覆盖状态不一致：{name}")
            continue
        for item in updates:
            if not item["title"].strip() or not start <= timestamp(item["published_at"]) < end:
                errors.append(f"更新缺少标题或超出时间窗口：{name}")
                continue
            candidates.add(source_url(item["url"]))

    if set(coverage) != set(followed):
        errors.append("覆盖结果必须逐一对应关注名单")
    if followed and all(status == UNVERIFIED for status in coverage.values()):
        errors.append("关注源全部未能验证")

    text = CODE.sub("", markdown)
    headings = list(HEADING.finditer(text))
    sections = {}
    for i, heading in enumerate(headings):
        name = heading[1].strip()
        if name in SECTIONS and name in sections:
            errors.append(f"核心栏目重复：{name}")
        end_of_section = headings[i + 1].start() if i + 1 < len(headings) else len(text)
        sections[name] = text[heading.end():end_of_section].strip()
    for name in SECTIONS:
        if not sections.get(name):
            errors.append(f"缺少核心栏目或栏目为空：{name}")

    displayed: dict[str, str] = {}
    for line in sections.get("信息源读取覆盖", "").splitlines():
        line = line.strip()
        if not line.startswith("- "):
            continue
        parts = [part.strip() for part in line[2:].split("｜", 2)]
        if len(parts) != 3:
            continue
        source, status, detail = parts
        if source in displayed or not detail:
            errors.append(f"覆盖栏目中来源重复或缺少说明：{source}")
        displayed[source] = status
    if displayed != coverage:
        errors.append("报告中的逐源覆盖状态与核验结果不一致")

    expected = {source_url(url) for url in plan["report_urls"]}
    for url in sorted(expected - candidates):
        errors.append(f"报告引用了未经本轮关注源验证的条目：{url}")
    for url in missing_links(sorted(expected), sections.get("今日新增", "")):
        errors.append(f"今日新增缺少可点击的链接：{url}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, required=True, help="Verification plan from live-source checks")
    parser.add_argument("--markdown", type=Path, required=True, help="Draft or full Notion readback")
    args = parser.parse_args()
    try:
        plan = json.loads(args.plan.read_text(encoding="utf-8"))
        errors = check_report(plan, args.markdown.read_text(encoding="utf-8"))
    except (OSError, ValueError, TypeError, KeyError, AttributeError) as exc:
        errors = [f"无法读取或解析核验输入：{exc}"]
    print(json.dumps({"ok_to_write": not errors, "blocking_failures": errors}, ensure_ascii=False))
    return 2 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
