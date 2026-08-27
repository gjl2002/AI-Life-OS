#!/usr/bin/env python3
"""Structural evidence gate for user-avatar artifacts.

The checker protects the formal/hypothesis boundary, user voice, purchase
logic, and downstream scope. It does not score the quality of research.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


FORMAL_SECTIONS = {
    "identity": "这个用户是谁",
    "trigger": "开始寻找帮助",
    "desired_change": "真正想改变什么",
    "current_alternative": "现在怎么解决",
    "buy": "为什么会购买",
    "not_buy": "为什么不会购买",
    "voice": "用户原话",
    "facts": "已确认事实",
    "insights": "合理洞察",
    "hypotheses": "待验证假设",
    "unknowns": "仍然需要验证什么",
    "sources": "证据来源",
}

HYPOTHESIS_SECTIONS = {
    "candidate": "目前可能是哪类用户",
    "support": "当前材料支持了什么",
    "unknowns": "还不能确认什么",
    "next_evidence": "下一步需要什么材料或访谈",
    "falsification": "支持或推翻假设",
}

PARTIAL_SECTIONS = {
    "confirmed": "本轮确认了什么",
    "uncertain": "仍然只是判断",
    "gap": "最大的证据缺口",
    "next": "下一个聚焦问题或材料",
}

GENERIC_PERSONA_WORDS = ["25-35", "一二线", "自我成长", "白领", "宝妈", "中产", "年轻人"]
DOWNSTREAM_OVERREACH = ["完整商业定位", "完整产品架构", "完整内容计划", "完整销售页", "销售 SOP"]


def issue(code: str, message: str, **extra: Any) -> dict[str, Any]:
    item = {"code": code, "message": message}
    item.update({key: value for key, value in extra.items() if value is not None})
    return item


def evidence_levels(text: str) -> list[str]:
    return sorted(
        set(
            re.findall(
                r"Level\s*[1-4]|一手强证据|行为与互动信号|业务背景材料|外部参考",
                text,
                flags=re.I,
            )
        )
    )


def artifact_type(text: str) -> str | None:
    if re.search(r"^#\s*用户画像假设", text, flags=re.M):
        return "hypothesis"
    if re.search(r"^#\s*用户洞察阶段小结", text, flags=re.M):
        return "partial"
    if re.search(r"^#\s*用户画像(?!假设)", text, flags=re.M):
        return "formal"
    return None


def missing_sections(text: str, sections: dict[str, str]) -> list[str]:
    return [key for key, marker in sections.items() if marker not in text]


def has_traceable_user_voice(text: str) -> bool:
    quoted = bool(re.search(r"「[^」]+」", text))
    sourced = "来源" in text
    return quoted and sourced


def has_strong_evidence(text: str) -> bool:
    return bool(re.search(r"Level\s*[12]|一手强证据|行为与互动信号", text, flags=re.I))


def check_artifact(markdown: str, mode: str) -> dict[str, Any]:
    blocking: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []
    kind = artifact_type(markdown)
    levels = evidence_levels(markdown)

    expected_kind = "formal" if mode == "writeback" else mode
    if kind is None:
        blocking.append(issue("missing_artifact_type", "Artifact must be a stage summary, avatar hypothesis, or formal user avatar."))
    elif kind != expected_kind:
        blocking.append(
            issue(
                "artifact_type_mismatch",
                "Artifact type does not match the requested quality-check mode.",
                expected=expected_kind,
                actual=kind,
            )
        )

    if kind == "formal":
        missing = missing_sections(markdown, FORMAL_SECTIONS)
        if missing:
            blocking.append(issue("missing_formal_sections", "Formal avatar is missing required decision sections.", sections=missing))
        if not has_traceable_user_voice(markdown):
            blocking.append(issue("formal_without_user_voice", "Formal avatar needs at least one traceable direct user quote."))
        if not has_strong_evidence(markdown):
            blocking.append(issue("formal_without_strong_evidence", "Formal avatar needs visible Level 1 or strong Level 2 evidence."))

    if kind == "hypothesis":
        missing = missing_sections(markdown, HYPOTHESIS_SECTIONS)
        if missing:
            blocking.append(issue("missing_hypothesis_sections", "Avatar hypothesis is missing its evidence or validation boundary.", sections=missing))

    if kind == "partial":
        missing = missing_sections(markdown, PARTIAL_SECTIONS)
        if missing:
            blocking.append(issue("missing_partial_sections", "Stage summary is missing its current evidence boundary.", sections=missing))

    generic_hits = [word for word in GENERIC_PERSONA_WORDS if word in markdown]
    if len(generic_hits) >= 2 and not has_traceable_user_voice(markdown):
        warnings.append(
            issue(
                "generic_demographic_persona",
                "The artifact may rely on demographic labels instead of behavior and purchase logic.",
                words=generic_hits,
            )
        )

    overreach_hits = [word for word in DOWNSTREAM_OVERREACH if word in markdown]
    if overreach_hits:
        warnings.append(
            issue(
                "downstream_scope_overreach",
                "User-avatar work should hand off constraints instead of completing downstream artifacts.",
                words=overreach_hits,
            )
        )

    return {
        "ok_to_publish": not blocking,
        "blocking_failures": blocking,
        "warnings": warnings,
        "summary": {
            "mode": mode,
            "artifact_type": kind,
            "evidence_levels": levels,
            "traceable_user_voice": has_traceable_user_voice(markdown),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Check user-avatar evidence and output boundaries.")
    parser.add_argument("--markdown", type=Path, required=True, help="Markdown artifact to check.")
    parser.add_argument("--mode", choices=["partial", "hypothesis", "formal", "writeback"], default="formal")
    parser.add_argument("--output", type=Path, help="Optional JSON output path.")
    args = parser.parse_args()

    report = check_artifact(args.markdown.read_text(encoding="utf-8"), args.mode)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["ok_to_publish"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
