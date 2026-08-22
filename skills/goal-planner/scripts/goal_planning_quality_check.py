#!/usr/bin/env python3
"""Quality gate for quarterly goal planning reports."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


REQUIRED_PATTERNS = {
    "planning_context": r"(本次主线|补线|参考记录)",
    "evidence_basis": r"(系统记录|用户输入|领域常识|方法论原则|规划假设|缺失数据)",
    "objective": r"(季度目标|阶段目标|12周目标|建议目标|目标名|目标描述)",
    "done_state": r"(完成状态|基本完成|目标周期结束|季度结束|三个月|3个月)",
    "projects": r"(项目拆解|项目\s*\|.*交付物|交付物)",
    "habits": r"(习惯支撑|习惯\s*\|.*频率|打卡)",
    "first_week": r"(本周启动动作|第一周|本周第一步|下周|启动动作)",
    "risks": r"(风险|取舍|失败|暂缓|放弃|预案)",
    "sedimentation": r"(可沉淀记录|写入计划|Notion)",
}


VAGUE_ACTIONS = ("提升能力", "坚持执行", "多学习", "好好推进", "持续努力", "加强自律")
KR_MARKERS = ("关键结果", "KR", "OKR")


def read_text(path: str | None) -> str:
    if path:
        return Path(path).read_text(encoding="utf-8")
    return sys.stdin.read()


def count_numbered_actions(text: str) -> int | None:
    marker = re.search(r"(本周启动动作|第一周|本周第一步|启动动作)", text)
    if not marker:
        return None
    section = text[marker.start() :]
    stop = re.search(r"\n#{1,3}\s+", section[1:])
    if stop:
        section = section[: stop.start() + 1]
    bullets = re.findall(r"(?m)^\s*(?:[-*]|\d+[.)、])\s+", section)
    return len(bullets)


def main() -> int:
    parser = argparse.ArgumentParser(description="Check a quarterly goal planning report draft.")
    parser.add_argument("draft", nargs="?", help="draft markdown path; stdin is used when omitted")
    parser.add_argument("--json", action="store_true", help="emit JSON")
    args = parser.parse_args()

    text = read_text(args.draft)
    blocking: list[str] = []
    warnings: list[str] = []

    for name, pattern in REQUIRED_PATTERNS.items():
        if not re.search(pattern, text, re.IGNORECASE | re.DOTALL):
            blocking.append(f"missing required section/signal: {name}")

    vague_hits = [word for word in VAGUE_ACTIONS if word in text]
    if vague_hits:
        blocking.append("vague action wording found: " + ", ".join(vague_hits))

    if any(marker in text for marker in KR_MARKERS):
        warnings.append("KR/OKR language appears; use only if user explicitly requested it")

    action_count = count_numbered_actions(text)
    if action_count is not None and action_count > 3:
        warnings.append(f"first-week actions exceed 3 on first-pass report: {action_count}")

    if re.search(r"(减重|收入|粉丝|阅读|分数|体脂|体重).{0,20}\d", text) and not re.search(r"(baseline|基线|当前数据|当前记录|数据来源|缺失数据|未记录)", text, re.IGNORECASE):
        warnings.append("numeric target appears without visible baseline or missing-data note")

    if re.search(r"(每天|每周|每月).{0,18}(项目|交付物)", text) and not re.search(r"(习惯|打卡|重复行为)", text):
        warnings.append("possible habit written as project; check project/habit boundary")

    if re.search(r"(报告全文|完整报告).{0,20}(12周启动|周期启动页)", text):
        blocking.append("do not assume a cycle launch page is the report database")

    if re.search(r"KnowMe OS", text):
        warnings.append("contains KnowMe OS; use only if user explicitly supplied it as the target system/product")

    ok = not blocking
    result = {
        "ok_to_finalize": ok,
        "blocking_failures": blocking,
        "warnings": warnings,
    }

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("ok_to_finalize:", str(ok).lower())
        if blocking:
            print("blocking_failures:")
            for item in blocking:
                print("-", item)
        if warnings:
            print("warnings:")
            for item in warnings:
                print("-", item)

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
