#!/usr/bin/env python3
"""
Quality gate for WeChat Moments drafts.

This checks hard trust and private-domain publishing failures before a draft is
presented as final or written back to Notion. Product naming is verified from
the current account/product context, not from a hard-coded personal blacklist.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


PUBLISHING_MARKERS = ["配图", "时间", "CTA", "复用", "发布建议"]
PROOF_WORDS = ["客户", "同学", "反馈", "好评", "案例", "截图", "报名", "成交", "付款", "私域"]
SOURCE_WORDS = ["来源", "证据", "截图", "聊天记录", "用户提供", "Notion", "产品", "反馈"]
HARD_SELL_WORDS = ["不买就", "错过就", "最后机会", "立刻报名", "收割", "割韭菜", "赶紧冲", "闭眼入"]
SALES_FACT_WORDS = ["价格", "原价", "现价", "名额", "仅剩", "截止", "报名", "付款", "成交", "限时"]
GENERIC_AI_WORDS = ["赋能", "底层逻辑", "闭环", "抓手", "矩阵", "链路", "打造", "沉淀"]
PUBLIC_ATTRIBUTION_WORDS = ["研究显示", "研究发现", "研究表明", "数据显示", "报告指出", "一项研究"]
PUBLIC_HEADING_RE = re.compile(r"(?m)^#{1,6}\s+")


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


def prose_paragraphs(text: str) -> list[str]:
    parts = [part.strip() for part in re.split(r"\n\s*\n", text) if part.strip()]
    return [
        part
        for part in parts
        if rough_chinese_chars(part) >= 5
        and not part.startswith(("#", "- ", "* ", ">", "```"))
        and not any(part.startswith(marker) for marker in PUBLISHING_MARKERS)
    ]


def sentence_count(text: str) -> int:
    sentences = [part for part in re.split(r"[。！？!?…]+", text) if rough_chinese_chars(part) > 0]
    return max(1, len(sentences)) if rough_chinese_chars(text) else 0


def contrast_overuse(text: str) -> int:
    return len(re.findall(r"不是.{0,18}而是", text))


def check_moments(markdown: str, mode: str, source_verified: bool = False) -> dict[str, Any]:
    blocking: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []
    char_count = rough_chinese_chars(markdown)

    hard_sell_hits = [word for word in HARD_SELL_WORDS if word in markdown]
    if hard_sell_hits:
        blocking.append(issue("hard_sell_language", "Draft uses fear-based or heavy sales language; rewrite as light conversion.", words=hard_sell_hits))

    length_limits = {
        "quick": 350,
        "enhanced": 420,
        "strict": 650,
        "campaign": 650,
    }
    limit = length_limits.get(mode, 420)
    if char_count > limit:
        warnings.append(issue("too_long_for_moments", "Draft may read like a公众号 paragraph rather than朋友圈; tighten if this is one post.", chinese_chars=char_count, suggested_limit=limit))
    if char_count < 20:
        warnings.append(issue("too_short_to_judge", "Draft is very short; make sure the scene, proof, or CTA is not missing.", chinese_chars=char_count))

    if mode in {"enhanced", "strict", "campaign"} and not contains_any(markdown, PUBLISHING_MARKERS):
        warnings.append(issue("missing_publishing_advice", "Final output should include concise publishing advice: media, timing, CTA, and reuse."))

    sales_fact_hits = [word for word in SALES_FACT_WORDS if word in markdown]
    if sales_fact_hits and mode in {"strict", "campaign"} and not contains_any(markdown, SOURCE_WORDS):
        blocking.append(issue("sales_fact_without_source_note", "Sales facts appear without a visible source/proof note; verify price, quota, deadline,报名, or payment claims.", words=sales_fact_hits))
    elif sales_fact_hits and not contains_any(markdown, SOURCE_WORDS):
        warnings.append(issue("sales_fact_without_source_note", "Sales facts appear without a visible source/proof note; verify before publishing.", words=sales_fact_hits))

    if contains_any(markdown, PROOF_WORDS) and mode in {"strict", "campaign"} and not contains_any(markdown, SOURCE_WORDS):
        blocking.append(issue("proof_claim_without_source_note", "Customer/private-domain proof appears without source or evidence notes."))

    heading_count = len(PUBLIC_HEADING_RE.findall(markdown))
    if heading_count > 2:
        warnings.append(issue("too_many_headings", "朋友圈 output has multiple Markdown headings; final post should feel like a natural note.", headings=heading_count))

    lengths = paragraph_lengths(markdown)
    if lengths and max(lengths) > 220:
        warnings.append(issue("paragraph_too_dense", "At least one paragraph is dense for朋友圈; split or shorten it.", longest_paragraph_chars=max(lengths)))

    prose = prose_paragraphs(markdown)
    single_sentence_paragraphs = sum(sentence_count(part) == 1 for part in prose)
    single_sentence_ratio = single_sentence_paragraphs / len(prose) if prose else 0.0
    if len(prose) >= 5 and single_sentence_ratio >= 0.75:
        warnings.append(issue(
            "fragmented_sentence_paragraphs",
            "Most body paragraphs contain only one sentence; merge related lines into semantic paragraphs instead of short-video-caption formatting.",
            prose_paragraphs=len(prose),
            single_sentence_paragraphs=single_sentence_paragraphs,
        ))

    generic_hits = [word for word in GENERIC_AI_WORDS if word in markdown]
    if len(generic_hits) >= 3:
        warnings.append(issue("generic_ai_terms", "Several generic AI/business words appear; translate them into concrete scenes or product facts.", words=generic_hits))

    contrast_count = contrast_overuse(markdown)
    if contrast_count >= 2:
        warnings.append(issue("contrast_template_overuse", "The draft overuses '不是...而是...' contrast rhythm; vary the movement or add a real scene.", count=contrast_count))

    public_claim_hits = [word for word in PUBLIC_ATTRIBUTION_WORDS if word in markdown]
    if public_claim_hits and mode in {"enhanced", "strict", "campaign"} and not source_verified:
        warnings.append(issue(
            "public_claim_needs_verification",
            "Public attribution appears without a confirmed working source record. Verify it before publishing; do not add a bibliography block to the朋友圈 by default.",
            words=public_claim_hits,
        ))

    return {
        "ok_to_publish": not blocking,
        "blocking_failures": blocking,
        "warnings": warnings,
        "summary": {
            "mode": mode,
            "chinese_chars": char_count,
            "headings": heading_count,
            "longest_paragraph_chars": max(lengths) if lengths else 0,
            "prose_paragraphs": len(prose),
            "single_sentence_paragraph_ratio": round(single_sentence_ratio, 2),
            "source_verified": source_verified,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Check WeChat Moments draft quality before final output or Notion writeback.")
    parser.add_argument("--markdown", type=Path, required=True, help="Markdown draft to check.")
    parser.add_argument("--mode", choices=["quick", "enhanced", "strict", "campaign"], default="enhanced")
    parser.add_argument("--source-verified", action="store_true", help="Use only after the post's public/book claim-to-source record has been checked.")
    parser.add_argument("--output", type=Path, help="Optional JSON output path.")
    args = parser.parse_args()

    markdown = args.markdown.read_text(encoding="utf-8")
    report = check_moments(markdown, args.mode, args.source_verified)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["ok_to_publish"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
