#!/usr/bin/env python3
"""
Quality gate for Xiaohongshu native image-text notes.

This checks deterministic public-domain trust, visual-evidence, and publishing
failures before a note is presented as final or written back to Notion.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


REQUIRED_MARKERS = ["图片排序建议", "标题", "正文方案", "标签", "评论区", "发布检查"]
IMAGE_MARKERS = ["图片排序", "封面", "图 2", "图2", "最后一张", "需要打码", "建议不发"]
PROOF_WORDS = ["客户", "同学", "反馈", "好评", "案例", "截图", "报名", "成交", "付款", "私域", "里程碑", "结果"]
RESULT_WORDS = ["收入", "成交", "涨粉", "用户数", "报名", "转化", "效率提升", "改变", "跑通", "爆了"]
PUBLIC_ATTRIBUTION_WORDS = ["研究显示", "研究发现", "研究表明", "数据显示", "报告指出", "一项研究"]
HARD_SELL_WORDS = ["不买就", "错过就", "最后机会", "立刻报名", "收割", "割韭菜", "闭眼入", "无脑冲"]
GENERIC_AI_WORDS = ["赋能", "底层逻辑", "闭环", "抓手", "矩阵", "链路", "打造", "沉淀", "长期主义"]
HEADING_RE = re.compile(r"(?m)^#{1,6}\s+")
MODE_LENGTH_LIMITS = {
    "quick": 900,
    "enhanced": 1200,
    "strict": 1500,
    "campaign": 1500,
}


def issue(code: str, message: str, **extra: Any) -> dict[str, Any]:
    item = {"code": code, "message": message}
    item.update({key: value for key, value in extra.items() if value is not None})
    return item


def rough_chinese_chars(text: str) -> int:
    return len(re.findall(r"[\u4e00-\u9fff]", text))


def contains_any(text: str, words: list[str]) -> bool:
    return any(word.lower() in text.lower() for word in words)


def paragraph_lengths(text: str) -> list[int]:
    parts = [part.strip() for part in re.split(r"\n\s*\n", text) if part.strip()]
    return [rough_chinese_chars(part) for part in parts]


def numbered_title_count(text: str) -> int:
    return len(re.findall(r"(?m)^\s*(?:\d+[.、]|[-*])\s*.+", text))


def check_native_note(markdown: str, mode: str, source_verified: bool = False, evidence_verified: bool = False) -> dict[str, Any]:
    blocking: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []
    char_count = rough_chinese_chars(markdown)

    missing = [marker for marker in REQUIRED_MARKERS if marker not in markdown]
    if missing:
        blocking.append(issue("missing_required_output_sections", "Final output is missing native-note sections.", sections=missing))

    if not contains_any(markdown, IMAGE_MARKERS):
        blocking.append(issue("missing_image_order_advice", "Native image-text notes require image order, cover, omission, and privacy advice."))

    hard_sell_hits = [word for word in HARD_SELL_WORDS if word in markdown]
    if hard_sell_hits:
        blocking.append(issue("hard_sell_language", "Draft uses heavy sales language; rewrite for public-domain trust and light conversion.", words=hard_sell_hits))

    result_hits = [word for word in RESULT_WORDS if word in markdown]
    if result_hits and mode in {"strict", "campaign"} and not evidence_verified:
        blocking.append(issue("result_claim_needs_evidence_verification", "Result/milestone claims need a confirmed user-owned evidence record; do not rely on a visible 'source' label alone.", words=result_hits))
    elif result_hits and not evidence_verified:
        warnings.append(issue("result_claim_needs_evidence_verification", "Result/milestone claims need a confirmed user-owned evidence record before publishing.", words=result_hits))

    if contains_any(markdown, PROOF_WORDS) and mode in {"strict", "campaign"} and not evidence_verified:
        blocking.append(issue("proof_claim_needs_evidence_verification", "Customer/private-domain/visual proof needs a confirmed user-owned evidence record."))

    public_hits = [word for word in PUBLIC_ATTRIBUTION_WORDS if word in markdown]
    if public_hits and mode in {"strict", "campaign"} and not source_verified:
        blocking.append(issue("public_claim_needs_source_verification", "Public research/case attribution needs a confirmed working source record; do not solve this by adding a bibliography block to the note.", words=public_hits))
    elif public_hits and mode == "enhanced" and not source_verified:
        warnings.append(issue("public_claim_needs_source_verification", "Public research/case attribution needs a confirmed working source record before publishing.", words=public_hits))

    if "标题备选" in markdown or "标题" in markdown:
        title_count = numbered_title_count(markdown)
        if title_count < 5:
            warnings.append(issue("title_package_may_be_incomplete", "Expected 5 title options for Xiaohongshu native output.", title_like_lines=title_count))

    limit = MODE_LENGTH_LIMITS.get(mode, 1200)
    if char_count > limit:
        warnings.append(issue("too_long_for_native_note", "Draft may read like a long article rather than a mobile-native Xiaohongshu note.", chinese_chars=char_count, suggested_limit=limit))

    headings = len(HEADING_RE.findall(markdown))
    if headings > 4:
        warnings.append(issue("too_many_markdown_headings", "Output has many Markdown headings; final note body should be phone-native and visually light.", headings=headings))

    lengths = paragraph_lengths(markdown)
    if lengths and max(lengths) > 260:
        warnings.append(issue("paragraph_too_dense", "At least one paragraph is dense for Xiaohongshu mobile reading.", longest_paragraph_chars=max(lengths)))

    generic_hits = [word for word in GENERIC_AI_WORDS if word in markdown]
    if len(generic_hits) >= 3:
        warnings.append(issue("generic_ai_terms", "Several generic AI/business words appear; translate them into image-led detail or concrete scenes.", words=generic_hits))

    if "私信" in markdown and ("关键词" not in markdown and "评论" not in markdown) and mode in {"strict", "campaign"}:
        warnings.append(issue("private_message_cue_unspecific", "Private-message CTA should be light and specific, preferably tied to a keyword or concrete help."))

    return {
        "ok_to_publish": not blocking,
        "blocking_failures": blocking,
        "warnings": warnings,
        "summary": {
            "mode": mode,
            "chinese_chars": char_count,
            "headings": headings,
            "longest_paragraph_chars": max(lengths) if lengths else 0,
            "source_verified": source_verified,
            "evidence_verified": evidence_verified,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Check Xiaohongshu native note quality before final output or Notion writeback.")
    parser.add_argument("--markdown", type=Path, required=True, help="Markdown draft to check.")
    parser.add_argument("--mode", choices=["quick", "enhanced", "strict", "campaign"], default="enhanced")
    parser.add_argument("--source-verified", action="store_true", help="Use only after public/book claim-to-source records have been checked.")
    parser.add_argument("--evidence-verified", action="store_true", help="Use only after user-owned result, product, milestone, or private-domain evidence has been checked.")
    parser.add_argument("--output", type=Path, help="Optional JSON output path.")
    args = parser.parse_args()

    markdown = args.markdown.read_text(encoding="utf-8")
    report = check_native_note(markdown, args.mode, source_verified=args.source_verified, evidence_verified=args.evidence_verified)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["ok_to_publish"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
