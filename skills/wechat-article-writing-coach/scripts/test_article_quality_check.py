#!/usr/bin/env python3
"""Regression tests for article_quality_check.py."""

import importlib.util
from pathlib import Path


SCRIPT = Path(__file__).with_name("article_quality_check.py")
SPEC = importlib.util.spec_from_file_location("article_quality_check", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


def test_multisection_body_is_not_truncated() -> None:
    markdown = """# 推荐标题：测试

## 正文

""" + "甲" * 500 + "\n\n## 第一部分\n\n" + "乙" * 500 + "\n\n## 第二部分\n\n" + "丙" * 500 + "\n\n## 来源说明\n\n[研究](https://example.com)"
    report = MODULE.check_article(markdown)
    assert report["summary"]["chinese_chars"] >= 1500
    assert not any(item["code"] == "article_may_be_too_short" for item in report["warnings"])


def test_vague_attribution_without_source_note_warns() -> None:
    markdown = """# 推荐标题：测试

## 正文

研究显示，""" + "甲" * 950
    report = MODULE.check_article(markdown)
    assert any(item["code"] == "vague_public_attribution" for item in report["warnings"])


def test_vague_attribution_with_reference_note_does_not_warn() -> None:
    markdown = """# 推荐标题：测试

## 正文

研究显示，""" + "甲" * 950 + "\n\n## 参考资料\n\nWilliams-Ceci et al. (2026). [资料](https://example.com)"
    report = MODULE.check_article(markdown)
    assert not any(item["code"] == "vague_public_attribution" for item in report["warnings"])


def test_product_name_is_not_blocked_without_live_positioning_context() -> None:
    markdown = """# 推荐标题：测试

## 正文

Project Atlas 是本次已授权活动中的产品名。""" + "甲" * 950 + "\n\n## 参考资料\n\n[产品资料](https://example.com)"
    report = MODULE.check_article(markdown)
    assert not any(item["code"] == "external_product_name_exposed" for item in report["blocking_failures"])


def test_short_article_with_many_internal_headings_warns() -> None:
    markdown = """# 推荐标题：测试

## 正文

""" + "甲" * 300 + "\n\n### 现象\n\n" + "乙" * 300 + "\n\n### 原因\n\n" + "丙" * 300 + "\n\n### 方法\n\n" + "丁" * 300 + "\n\n## 参考资料\n\n作者，《书名》"
    report = MODULE.check_article(markdown)
    assert any(item["code"] == "short_article_heading_density" for item in report["warnings"])
    assert report["summary"]["internal_headings"] == 3


def test_compact_article_without_internal_headings_does_not_warn() -> None:
    markdown = """# 推荐标题：测试

## 正文

""" + "甲" * 1200 + "\n\n## 参考资料\n\n作者，《书名》"
    report = MODULE.check_article(markdown)
    assert not any(item["code"] == "short_article_heading_density" for item in report["warnings"])


def test_medium_article_with_six_headings_warns() -> None:
    parts = ["# 推荐标题：测试", "## 正文", "甲" * 300]
    for index in range(6):
        parts.extend([f"### 第{index + 1}部分", "乙" * 380])
    parts.extend(["## 参考资料", "作者，《书名》"])
    report = MODULE.check_article("\n\n".join(parts))
    assert report["summary"]["chinese_chars"] <= 2800
    assert report["summary"]["internal_headings"] == 6
    assert any(item["code"] == "short_article_heading_density" for item in report["warnings"])


def test_unscoped_technical_definition_warns() -> None:
    markdown = """# 推荐标题：测试

## 正文

Agent 就是能够自主规划并完成任务的系统。""" + "甲" * 950 + "\n\n## 参考资料\n\n[官方文档](https://example.com)"
    report = MODULE.check_article(markdown)
    assert any(item["code"] == "technical_definition_needs_scope" for item in report["warnings"])


def test_scoped_technical_definition_does_not_warn() -> None:
    markdown = """# 推荐标题：测试

## 正文

在我的系统里，我把能够处理具体场景的 AI 助手称为智能体。""" + "甲" * 950 + "\n\n## 参考资料\n\n产品记录"
    report = MODULE.check_article(markdown)
    assert not any(item["code"] == "technical_definition_needs_scope" for item in report["warnings"])


def test_unrelated_scope_marker_does_not_hide_later_definition() -> None:
    markdown = """# 推荐标题：测试

## 正文

在我的系统里，我把文章放进内容库。""" + "甲" * 100 + "。Agent 就是能够自主规划并完成任务的系统。" + "乙" * 850 + "\n\n## 参考资料\n\n[官方文档](https://example.com)"
    report = MODULE.check_article(markdown)
    assert any(item["code"] == "technical_definition_needs_scope" for item in report["warnings"])


if __name__ == "__main__":
    test_multisection_body_is_not_truncated()
    test_vague_attribution_without_source_note_warns()
    test_vague_attribution_with_reference_note_does_not_warn()
    test_product_name_is_not_blocked_without_live_positioning_context()
    test_short_article_with_many_internal_headings_warns()
    test_compact_article_without_internal_headings_does_not_warn()
    test_medium_article_with_six_headings_warns()
    test_unscoped_technical_definition_warns()
    test_scoped_technical_definition_does_not_warn()
    test_unrelated_scope_marker_does_not_hide_later_definition()
    print("article_quality_check regression tests passed")
