#!/usr/bin/env python3
"""Quality gate for life-positioning final and hypothesis maps."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


FINAL_REQUIRED = {
    "title": r"人生定位地图",
    "stage": r"当前阶段",
    "strengths": r"优势地图",
    "drive": r"热爱与驱动力",
    "problems": r"持续关注的问题",
    "evidence": r"现实证据",
    "anti_vision": r"反愿景与边界",
    "ideal_self": r"理想自我",
    "vision": r"愿景阶梯",
    "confidence": r"证据与置信度",
}

HYPOTHESIS_REQUIRED = {
    "title": r"人生定位假设地图",
    "hypothesis": r"当前假设",
    "available_evidence": r"已有证据",
    "missing_evidence": r"缺失证据",
    "validation": r"验证动作",
    "confidence": r"当前置信度",
}


def read_text(path: str | None) -> str:
    return Path(path).read_text(encoding="utf-8") if path else sys.stdin.read()


def main() -> int:
    parser = argparse.ArgumentParser(description="Check a life-positioning map draft.")
    parser.add_argument("draft", nargs="?", help="Markdown path; stdin when omitted")
    parser.add_argument("--artifact", choices=("final", "hypothesis", "partial"), default="final")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    text = read_text(args.draft)
    blocking: list[str] = []
    warnings: list[str] = []

    required = FINAL_REQUIRED if args.artifact == "final" else HYPOTHESIS_REQUIRED if args.artifact == "hypothesis" else {}
    for name, pattern in required.items():
        if not re.search(pattern, text, re.IGNORECASE):
            blocking.append(f"missing section: {name}")

    if args.artifact == "final":
        concrete_patterns = (
            r"\d{4}|\d+月|\d+次|\d+年",
            r"场景|当时|有一次|具体|记录|原话",
            r"反馈|邀请|请求|作品|结果|项目|复盘",
        )
        if sum(bool(re.search(pattern, text)) for pattern in concrete_patterns) < 2:
            blocking.append("final map lacks enough concrete evidence signals; use a hypothesis map")

    if re.search(r"人生探索\s*/\s*(自我认知|人生问题)", text):
        blocking.append("uses retired source; use 认知笔记 or 第二大脑/问题")
    if re.search(r"立刻变现|马上商业化|直接卖课", text):
        warnings.append("life direction may be forced into commercialization")
    if re.search(r"最终确定|唯一方向|毫无疑问|就是你的人生定位", text):
        warnings.append("positioning wording is too permanent or overconfident")

    result = {"ok_to_finalize": not blocking, "blocking_failures": blocking, "warnings": warnings}
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("ok_to_finalize:", str(not blocking).lower())
        for label, items in (("blocking_failures", blocking), ("warnings", warnings)):
            if items:
                print(label + ":")
                for item in items:
                    print("-", item)
    return 0 if not blocking else 1


if __name__ == "__main__":
    raise SystemExit(main())
