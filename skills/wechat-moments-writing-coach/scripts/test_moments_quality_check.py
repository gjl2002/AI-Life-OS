#!/usr/bin/env python3
"""Regression tests for moments_quality_check.py."""

import importlib.util
from pathlib import Path


SCRIPT = Path(__file__).with_name("moments_quality_check.py")
SPEC = importlib.util.spec_from_file_location("moments_quality_check", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


def test_public_claim_requires_working_verification() -> None:
    report = MODULE.check_moments("研究显示，今天这个发现让我停下来想了很久。", "enhanced")
    assert any(item["code"] == "public_claim_needs_verification" for item in report["warnings"])


def test_verified_public_claim_does_not_need_bibliography() -> None:
    report = MODULE.check_moments("研究显示，今天这个发现让我停下来想了很久。", "enhanced", source_verified=True)
    assert not any(item["code"] == "public_claim_needs_verification" for item in report["warnings"])


def test_sentence_per_paragraph_rhythm_is_flagged() -> None:
    draft = "今天想到一件事。\n\n我以前一直没想明白。\n\n后来发生了一件小事。\n\n我突然有点懂了。\n\n这件事让我停下来想了很久。\n\n现在我有了新的判断。"
    report = MODULE.check_moments(draft, "quick")
    assert any(item["code"] == "fragmented_sentence_paragraphs" for item in report["warnings"])


def test_semantic_paragraph_rhythm_is_not_flagged() -> None:
    draft = "今天想到一件事。我以前一直没想明白，后来发生了一件小事，我突然有点懂了。\n\n这件事让我停下来想了很久。过去的经历也重新连在了一起，我开始有了新的判断。\n\n现在回头看，答案其实一直藏在自己的行动里。"
    report = MODULE.check_moments(draft, "quick")
    assert not any(item["code"] == "fragmented_sentence_paragraphs" for item in report["warnings"])


def test_strict_sales_fact_without_source_blocks() -> None:
    report = MODULE.check_moments("这次只剩三个名额，今晚截止报名。", "strict")
    assert any(item["code"] == "sales_fact_without_source_note" for item in report["blocking_failures"])


def test_hard_sell_language_blocks() -> None:
    report = MODULE.check_moments("这是最后机会，错过就没有了，赶紧冲。", "quick")
    assert any(item["code"] == "hard_sell_language" for item in report["blocking_failures"])


if __name__ == "__main__":
    test_public_claim_requires_working_verification()
    test_verified_public_claim_does_not_need_bibliography()
    test_sentence_per_paragraph_rhythm_is_flagged()
    test_semantic_paragraph_rhythm_is_not_flagged()
    test_strict_sales_fact_without_source_blocks()
    test_hard_sell_language_blocks()
    print("moments_quality_check regression tests passed")
