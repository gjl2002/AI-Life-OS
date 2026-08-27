#!/usr/bin/env python3
"""
Quality gate for WeChat article drafts.

This checks hard structural and publishing failures before a draft is presented
as final or written back to Notion. It does not judge literary quality.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


TITLE_MARKERS = ["推荐标题", "主推标题", "标题包", "标题"]
ARTICLE_MARKERS = ["正文", "完整文章", "文章正文"]
SOURCE_MARKERS = ["来源", "source", "素材", "源说明", "source note", "参考资料", "参考文献", "资料来源"]
VISUAL_NOTE_MARKERS = ["业务证据配图", "配图建议", "视觉建议", "截图建议"]
CTA_MARKERS = ["轻转化", "转化路径", "CTA", "私域承接", "引流"]
HARD_SELL_WORDS = ["限时", "立刻报名", "最后机会", "不买就", "错过就", "割韭菜", "收割"]
GENERIC_AI_WORDS = ["赋能", "抓手", "闭环", "底层逻辑", "矩阵", "链路"]
LINK_RE = re.compile(r"https?://|\[[^\]]+\]\([^\)]+\)")
IMAGE_PLACEHOLDER_RE = re.compile(r"【图\s*\d+[^】]*】")
HEADING_RE = re.compile(r"(?m)^#{1,6}\s+(.+?)\s*$")
VAGUE_PUBLIC_ATTRIBUTIONS = ["研究显示", "研究发现", "研究表明", "科学家们发现", "有人说", "有人在访谈", "某个 workshop", "某个workshop"]
TECHNICAL_DEFINITION_RE = re.compile(
    r"(?:Agent|智能体|Skill|MCP|RAG|长期记忆|上下文工程)"
    r"[^。！？!?\n]{0,32}(?:是指|就是|意味着|具备|能够|可以自主|会自主)",
    re.IGNORECASE,
)
TECHNICAL_SCOPE_MARKERS = ["在本文里", "这里说的", "在我的系统里", "在这个产品里", "我把", "按官方定义", "从技术架构看", "从应用层看"]


def issue(code: str, message: str, **extra: Any) -> dict[str, Any]:
    item = {"code": code, "message": message}
    item.update({key: value for key, value in extra.items() if value is not None})
    return item


def contains_any(text: str, markers: list[str]) -> bool:
    return any(marker.lower() in text.lower() for marker in markers)


def section_after_marker(text: str, markers: list[str]) -> str:
    headings = list(HEADING_RE.finditer(text))
    for index, match in enumerate(headings):
        title = match.group(1)
        if contains_any(title, markers):
            start = match.end()
            end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
            return text[start:end].strip()
    return ""


def article_body(text: str) -> str:
    """Return the full article body while allowing normal internal headings."""
    headings = list(HEADING_RE.finditer(text))
    for index, match in enumerate(headings):
        if not contains_any(match.group(1), ARTICLE_MARKERS):
            continue
        start = match.end()
        end = len(text)
        for later in headings[index + 1 :]:
            if contains_any(later.group(1), SOURCE_MARKERS):
                end = later.start()
                break
        return text[start:end].strip()
    return ""


def rough_chinese_chars(text: str) -> int:
    return len(re.findall(r"[\u4e00-\u9fff]", text))


def repeated_sentence_stems(text: str) -> list[str]:
    sentences = re.split(r"[。！？!?]\s*", text)
    stems: dict[str, int] = {}
    for sentence in sentences:
        clean = re.sub(r"\s+", "", sentence)
        if len(clean) < 14:
            continue
        stem = clean[:18]
        stems[stem] = stems.get(stem, 0) + 1
    return sorted(stem for stem, count in stems.items() if count >= 2)


def internal_heading_count(article_text: str) -> int:
    return len(HEADING_RE.findall(article_text))


def unscoped_technical_definitions(article_text: str) -> list[str]:
    unscoped: list[str] = []
    for match in TECHNICAL_DEFINITION_RE.finditer(article_text):
        context_start = max(0, match.start() - 60)
        context_end = min(len(article_text), match.end() + 20)
        local_context = article_text[context_start:context_end]
        if not contains_any(local_context, TECHNICAL_SCOPE_MARKERS):
            unscoped.append(match.group(0))
    return unscoped


def check_article(markdown: str) -> dict[str, Any]:
    blocking: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []

    title_section = section_after_marker(markdown, TITLE_MARKERS)
    article_section = article_body(markdown)
    source_section = section_after_marker(markdown, SOURCE_MARKERS)

    if not contains_any(markdown, TITLE_MARKERS):
        blocking.append(issue("missing_title_package", "The draft is missing a visible title package or recommended title."))
    if not article_section:
        # Fallback: allow long markdown without an explicit article heading, but warn.
        if rough_chinese_chars(markdown) < 900:
            blocking.append(issue("missing_article_body", "The draft is missing a recognizable article body."))
        else:
            warnings.append(issue("article_body_heading_missing", "The article body is long enough but lacks a clear 正文/完整文章 heading."))

    body_for_length = article_section or markdown
    char_count = rough_chinese_chars(body_for_length)
    if char_count < 900:
        warnings.append(issue("article_may_be_too_short", "The article body appears short for a WeChat long-form draft.", chinese_chars=char_count))
    if char_count > 3200:
        warnings.append(issue("article_may_be_too_long", "The article body may be too long; check density and repetition.", chinese_chars=char_count))

    if not source_section and not contains_any(markdown, SOURCE_MARKERS):
        blocking.append(issue("missing_source_note", "The final output should include concise source notes or source labels."))

    placeholders = IMAGE_PLACEHOLDER_RE.findall(markdown)
    if placeholders and not contains_any(markdown, VISUAL_NOTE_MARKERS):
        blocking.append(issue("visual_placeholders_without_notes", "Image placeholders exist but matching business-evidence visual notes are missing.", placeholders=placeholders))

    if contains_any(markdown, CTA_MARKERS):
        hard_sell_hits = [word for word in HARD_SELL_WORDS if word in markdown]
        if hard_sell_hits:
            blocking.append(issue("hard_sell_cta", "CTA uses hard-sell or fear-based wording; rewrite as light conversion.", words=hard_sell_hits))

    generic_hits = [word for word in GENERIC_AI_WORDS if word in body_for_length]
    if len(generic_hits) >= 3:
        warnings.append(issue("generic_ai_terms", "The draft uses several generic AI/business terms; translate them into concrete language.", words=generic_hits))

    repeated = repeated_sentence_stems(body_for_length)
    if repeated:
        warnings.append(issue("repeated_sentence_openings", "Some sentence openings repeat; check paragraph progression.", stems=repeated[:8]))

    heading_count = internal_heading_count(article_section) if article_section else 0
    heading_density_warns = (
        (char_count <= 1400 and heading_count >= 3)
        or (char_count <= 1800 and heading_count >= 4)
        or (char_count <= 2800 and heading_count >= 6)
    )
    if heading_density_warns:
        warnings.append(issue(
            "short_article_heading_density",
            "This compact article has many internal headings; check whether the structure is over-labelled or course-handout-like.",
            chinese_chars=char_count,
            internal_headings=heading_count,
        ))

    technical_definitions = unscoped_technical_definitions(body_for_length)
    if technical_definitions:
        warnings.append(issue(
            "technical_definition_needs_scope",
            "A technical term is being defined or assigned capabilities without an explicit discussion layer; verify the current source and scope the wording.",
            examples=technical_definitions[:3],
        ))

    links = LINK_RE.findall(markdown)
    if contains_any(markdown, ["联网", "公开资料", "报告", "研究", "数据"]) and not links:
        warnings.append(issue("public_claims_without_links", "Public evidence or data is mentioned but no visible links were found."))

    vague_attributions = [phrase for phrase in VAGUE_PUBLIC_ATTRIBUTIONS if phrase in body_for_length]
    has_traceable_source_note = bool(source_section and links)
    if vague_attributions and not has_traceable_source_note:
        warnings.append(issue(
            "vague_public_attribution",
            "Add a natural in-text source anchor and a traceable final source note for this public claim.",
            phrases=vague_attributions,
        ))

    return {
        "ok_to_publish": not blocking,
        "blocking_failures": blocking,
        "warnings": warnings,
        "summary": {
            "chinese_chars": char_count,
            "image_placeholders": len(placeholders),
            "links": len(links),
            "has_title_package": contains_any(markdown, TITLE_MARKERS),
            "has_source_note": bool(source_section or contains_any(markdown, SOURCE_MARKERS)),
            "internal_headings": heading_count,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Check WeChat article draft quality before final output or Notion writeback.")
    parser.add_argument("--markdown", type=Path, required=True, help="Markdown draft to check.")
    parser.add_argument("--output", type=Path, help="Optional JSON output path.")
    args = parser.parse_args()

    markdown = args.markdown.read_text(encoding="utf-8")
    report = check_article(markdown)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["ok_to_publish"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
