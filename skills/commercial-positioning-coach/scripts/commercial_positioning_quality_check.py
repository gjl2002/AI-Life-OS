#!/usr/bin/env python3
"""Structural contract check for commercial-positioning artifacts."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


FINAL_REQUIRED = {
    "title": r"商业定位地图",
    "positioning": r"当前定位",
    "customer": r"核心客户与发生场景",
    "problem": r"核心问题与欲望差距",
    "value_mechanism": r"价值机制与产品假设",
    "difference": r"POV、相关差异与可信理由",
    "evidence": r"当前市场证据",
    "handoff": r"商业系统影响与下游交接",
    "unknown": r"未知、验证与更新条件",
}

HYPOTHESIS_REQUIRED = {
    "title": r"商业定位假设地图",
    "hypothesis": r"当前定位假设",
    "evidence": r"已有事实与证据",
    "missing": r"仍然缺少什么",
    "tasks": r"验证任务",
    "falsification": r"支持或推翻假设的信号",
    "strength": r"当前证据强度",
}

PARTIAL_REQUIRED = {
    "title": r"商业定位阶段小结",
    "confirmed": r"本轮确认了什么",
    "hypothesis": r"哪些仍是假设",
    "gap": r"当前最大的证据缺口",
    "next": r"下一个聚焦问题",
}

EVIDENCE_TERMS = r"客户原话|客户反馈|用户反馈|咨询|成交|收入|复购|退款|交付|内容反馈|私域|销售|对标"
ABSTRACT_POSITIONING = r"AI\s*赋能|个人品牌|长期主义|成长型人群"
OVERREACH_TERMS = r"完整用户研究报告|完整产品架构|完整内容日历|完整销售SOP"


def read_text(path: str | None) -> str:
    return Path(path).read_text(encoding="utf-8") if path else sys.stdin.read()


def check_artifact(text: str, artifact: str) -> dict[str, object]:
    required = {
        "final": FINAL_REQUIRED,
        "hypothesis": HYPOTHESIS_REQUIRED,
        "partial": PARTIAL_REQUIRED,
    }[artifact]
    blocking: list[str] = []
    warnings: list[str] = []

    for name, pattern in required.items():
        if not re.search(pattern, text, re.IGNORECASE):
            blocking.append(f"missing section: {name}")

    if artifact == "final" and not re.search(EVIDENCE_TERMS, text):
        blocking.append("final map lacks customer, content, consultation, sales, revenue, delivery, or market evidence")

    if artifact == "final" and not re.search(r"当前替代方案|替代方案", text):
        blocking.append("final map does not identify the customer's current alternative")

    if artifact == "final" and not re.search(r"下游|用户研究|产品机会|产品架构|内容.*约束", text):
        warnings.append("final map does not clearly state downstream business-system constraints or handoff")

    if re.search(ABSTRACT_POSITIONING, text, re.IGNORECASE):
        warnings.append("abstract positioning language appears; verify that specific audience, scene, problem, and value mechanism are also present")

    if re.search(r"AI[- ]?powered|AI\s*[+＋]|[+＋]\s*AI|Notion\s*[+＋]\s*AI", text, re.IGNORECASE):
        warnings.append("AI/tool label appears; verify it is a mechanism rather than the complete positioning")

    if re.search(r"唯一定位|必然成功|毫无疑问|已经验证", text) and not re.search(r"成交|收入|复购|案例|数据", text):
        warnings.append("commercial conclusion may be overconfident relative to the recorded evidence")

    if artifact in {"final", "hypothesis"} and not re.search(r"支持|推翻|验证|未知|缺少", text):
        warnings.append("artifact does not clearly preserve uncertainty or falsification conditions")

    if re.search(OVERREACH_TERMS, text, re.IGNORECASE):
        warnings.append("artifact may be completing downstream user research, product architecture, content, or sales work instead of passing constraints")

    return {
        "ok_to_finalize": not blocking,
        "artifact": artifact,
        "blocking_failures": blocking,
        "warnings": warnings,
        "scope": "structural_contract_only",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Check a commercial-positioning artifact.")
    parser.add_argument("draft", nargs="?", help="Markdown path; stdin when omitted")
    parser.add_argument("--artifact", choices=("final", "hypothesis", "partial"), default="final")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    text = read_text(args.draft)

    result = check_artifact(text, args.artifact)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("ok_to_finalize:", str(result["ok_to_finalize"]).lower())
        for label, items in (("blocking_failures", result["blocking_failures"]), ("warnings", result["warnings"])):
            if items:
                print(label + ":")
                for item in items:
                    print("-", item)
    return 0 if result["ok_to_finalize"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
