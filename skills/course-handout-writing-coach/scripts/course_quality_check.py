#!/usr/bin/env python3
"""Configurable structural checks for course teaching materials.

This catches obvious omissions without assuming every handout is a long live
lesson with slides and a demonstration. Semantic quality stays model-reviewed.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def contains_any(text: str, terms: list[str]) -> bool:
    return any(term.lower() in text.lower() for term in terms)


def check_course(
    text: str,
    deliverable: str = "handout",
    duration: int = 0,
    require_ppt: bool = False,
    require_demo: bool = False,
) -> dict[str, object]:
    headings = re.findall(r"(?m)^#{1,6}\s+(.+)$", text)
    chinese_chars = len(re.findall(r"[\u4e00-\u9fff]", text))
    blocking: list[str] = []
    warnings: list[str] = []

    required = {
        "learner action": ["作业", "行动", "练习", "任务"],
        "submission or asset": ["提交", "交付", "启动卡", "模板", "资产"],
        "self-check or feedback": ["自检", "反馈", "rubric", "检查"],
    }
    for label, terms in required.items():
        if not contains_any(text, terms):
            blocking.append(f"missing {label}")

    if len(headings) < 3:
        warnings.append("fewer than 3 headings: verify that the material is easy to navigate")
    if chinese_chars < 400:
        warnings.append(f"only {chinese_chars} Chinese characters: verify that the requested teaching job is actually complete")

    if not contains_any(text, ["案例", "示例", "演示", "情境"]):
        warnings.append("no visible case, example, demonstration, or learning scene")
    if not contains_any(text, ["下一节", "衔接", "下节", "下一步"]):
        warnings.append("no visible next action or lesson handoff")

    minute_mentions = re.findall(r"(?:约|预计|目标|时长)?\s*(\d{1,3})\s*分钟", text)
    if duration > 0:
        if not minute_mentions:
            blocking.append("timed lesson has no visible minute run or time-coded segments")
        if not contains_any(text, ["分钟运行表", "时间线", "时间预算"]):
            blocking.append("timed lesson has no explicit minute-run table or timeline")
        if duration >= 90 and chinese_chars < 5000:
            warnings.append(
                f"90-minute lesson has {chinese_chars} Chinese characters; verify the duration through cases, interaction, demo, and learner work rather than padding"
            )

    if require_ppt and not contains_any(text, ["PPT", "幻灯", "页面", "Slide"]):
        blocking.append("PPT was requested but no slide-rhythm evidence is visible")
    if require_demo and not contains_any(text, ["直播演示", "Live Demo", "现场演示", "演示"]):
        blocking.append("a demonstration was requested but no demo plan is visible")

    report = {
        "deliverable": deliverable,
        "duration_minutes": duration or None,
        "require_ppt": require_ppt,
        "require_demo": require_demo,
        "chinese_characters": chinese_chars,
        "heading_count": len(headings),
        "minute_mentions": [int(value) for value in minute_mentions],
        "blocking_failures": blocking,
        "warnings": warnings,
        "status": "pass" if not blocking else "blocked",
    }
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--markdown", required=True, help="Path to the teaching material")
    parser.add_argument(
        "--deliverable",
        choices=["handout", "workbook", "instructor-script", "live-lesson"],
        default="handout",
    )
    parser.add_argument("--duration", type=int, default=0, help="Promised delivery duration in minutes")
    parser.add_argument("--require-ppt", action="store_true", help="Use only when a PPT/deck is part of the request")
    parser.add_argument("--require-demo", action="store_true", help="Use only when a live or recorded demonstration is part of the request")
    args = parser.parse_args()

    text = Path(args.markdown).read_text(encoding="utf-8")
    report = check_course(text, args.deliverable, args.duration, args.require_ppt, args.require_demo)
    report["markdown"] = str(args.markdown)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if report["blocking_failures"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
