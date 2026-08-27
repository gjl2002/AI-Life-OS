#!/usr/bin/env python3
"""Structural quality gate for formal product-opportunity reports.

This script checks observable report invariants. It cannot verify whether cited
evidence is true, sufficient, current, or interpreted well.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


REQUIRED_PATTERNS = {
    "decision": r"(值得做|调整后做|先验证|暂停|放弃)",
    "evidence_ladder": r"已验证证据[：:]?.*合理推断[：:]?.*待验证假设",
    "demand": r"(真实需求|需求证据|用户为什么需要)",
    "first_user": r"(首批用户|谁会先买)",
    "trigger_scene": r"(触发场景|触发时间|真实触发场景|为什么需要现在行动)",
    "substitute": r"(当前替代|替代方案|现在怎么解决|不解决|什么都不做)",
    "visible_advantage": r"(可见优势|为什么可能选择|为什么愿意切换|胜出理由)",
    "delivery_fit": r"(交付匹配|产品形态|需求形态|交付能力)",
    "risk_unknown": r"(最大风险|仍然未知|最大未知)",
    "validation_action": r"(第一验证动作|要验证的关键假设)",
}


def read_text(path: str | None) -> str:
    if path:
        return Path(path).read_text(encoding="utf-8")
    return sys.stdin.read()


def validation_has_full_shape(text: str) -> bool:
    checks = (
        r"(验证对象|对象)[：:]",
        r"(验证动作|真实 Offer|动作或真实 Offer)[：:]",
        r"(成功信号|成功标准|成功.*阈值)[：:]",
        r"(失败说明什么|失败后|调整.*路径|暂停.*路径|放弃.*路径)[：:]",
    )
    return all(re.search(pattern, text, re.IGNORECASE) for pattern in checks)


def has_direct_evidence_shape(text: str) -> bool:
    return bool(
        re.search(
            r"(用户原话|真实反馈|实际付费|成交记录|咨询记录|重复行为|交付结果|内容响应|已验证证据[：:].{1,160}\S)",
            text,
            re.DOTALL,
        )
    )


def has_market_source_shape(text: str) -> bool:
    return bool(
        re.search(
            r"(来源|链接|对标产品|对标内容|对标账号|竞品官网|官方定价|公开数据|web|https?://)",
            text,
            re.IGNORECASE,
        )
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Check a formal product-opportunity report.")
    parser.add_argument("draft", nargs="?", help="Markdown report path; stdin when omitted")
    parser.add_argument("--json", action="store_true", help="emit JSON")
    args = parser.parse_args()

    text = read_text(args.draft)
    blocking: list[str] = []
    warnings: list[str] = []

    for name, pattern in REQUIRED_PATTERNS.items():
        if not re.search(pattern, text, re.IGNORECASE | re.DOTALL):
            blocking.append(f"missing required report signal: {name}")

    if not validation_has_full_shape(text):
        blocking.append(
            "first validation lacks object + action/offer + success threshold + failure/adjustment path"
        )

    if re.search(r"决策[：:]\s*值得做", text) and not has_direct_evidence_shape(text):
        blocking.append("worth-doing decision lacks an explicit direct-evidence signal")

    if re.search(r"(市场空白|蓝海|没有竞争|没人做|竞品很少)", text) and not has_market_source_shape(text):
        blocking.append("market-whitespace claim lacks a visible market source")

    if re.search(r"(新物种|AI[- ]?native|AI原生|变革型)", text, re.IGNORECASE) and not re.search(
        r"(用户价值|使用方式|资源结构|收入来源|增长方式|用户关系|产品身份|后台逻辑)",
        text,
    ):
        blocking.append("new-species claim lacks changed-dimension analysis")

    if re.search(r"(可见优势|胜出理由).{0,100}(因为|靠|使用|基于)\s*AI", text, re.DOTALL):
        warnings.append("AI appears as the advantage itself; state the visible user benefit")

    if re.search(r"痛点.{0,60}(方便|便利|效率|整理|自动化)", text, re.DOTALL):
        warnings.append("possible convenience demand mislabeled as a strong pain point")

    if re.search(r"(转化率|成交|收入|销量|用户数|阅读量|收藏|评论).{0,50}(估计|大概|应该|可能)", text):
        warnings.append("possible inferred metric presented near a factual label")

    result = {
        "ok_to_finalize": not blocking,
        "blocking_failures": blocking,
        "warnings": warnings,
        "scope_note": "structural checks only; manually verify evidence truth, freshness, and interpretation",
    }

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("ok_to_finalize:", str(not blocking).lower())
        for label, items in (("blocking_failures", blocking), ("warnings", warnings)):
            if items:
                print(f"{label}:")
                for item in items:
                    print("-", item)
        print("scope_note:", result["scope_note"])

    return 0 if not blocking else 1


if __name__ == "__main__":
    raise SystemExit(main())
