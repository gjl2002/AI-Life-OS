#!/usr/bin/env python3
"""Regression tests for Xiaohongshu note quality checks."""

import importlib.util
from pathlib import Path


SCRIPT = Path(__file__).with_name("native_note_quality_check.py")
SPEC = importlib.util.spec_from_file_location("native_note_quality_check", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


BASE = """图片排序建议：封面放图 1，图 2 说明过程，最后一张放行动提示。
标题：
1. 一个标题
2. 两个标题
3. 三个标题
4. 四个标题
5. 五个标题
正文方案 A：今天我重新看了一遍这张图。
正文方案 B：这件小事让我停下来想了想。
标签：#成长
评论区引导：你最近也有类似时刻吗？
发布检查：图片和文字已核对。"""


def codes(report):
    return {item["code"] for item in report["blocking_failures"] + report["warnings"]}


def test_public_claim_requires_working_source_record():
    report = MODULE.check_native_note(BASE + "\n研究显示，这个现象值得多想一步。", "enhanced")
    assert "public_claim_needs_source_verification" in codes(report)


def test_verified_public_claim_needs_no_bibliography_block():
    report = MODULE.check_native_note(BASE + "\n研究显示，这个现象值得多想一步。", "enhanced", source_verified=True)
    assert "public_claim_needs_source_verification" not in codes(report)


def test_strict_result_claim_needs_user_owned_evidence():
    report = MODULE.check_native_note(BASE + "\n这次报名终于跑通了。", "strict")
    assert "result_claim_needs_evidence_verification" in codes(report)
    verified = MODULE.check_native_note(BASE + "\n这次报名终于跑通了。", "strict", evidence_verified=True)
    assert "result_claim_needs_evidence_verification" not in codes(verified)


def test_execution_mode_limits_are_frozen():
    assert MODULE.MODE_LENGTH_LIMITS == {
        "quick": 900,
        "enhanced": 1200,
        "strict": 1500,
        "campaign": 1500,
    }


def test_strict_public_claim_blocks_without_source():
    report = MODULE.check_native_note(BASE + "\n研究显示，这个现象值得多想一步。", "strict")
    assert not report["ok_to_publish"]
    assert "public_claim_needs_source_verification" in codes(report)


def test_enhanced_public_claim_remains_warning():
    report = MODULE.check_native_note(BASE + "\n研究显示，这个现象值得多想一步。", "enhanced")
    assert report["ok_to_publish"]
    assert "public_claim_needs_source_verification" in codes(report)


def test_campaign_proof_claim_blocks_without_evidence():
    report = MODULE.check_native_note(BASE + "\n这是客户反馈截图。", "campaign")
    assert not report["ok_to_publish"]
    assert "proof_claim_needs_evidence_verification" in codes(report)


def test_hard_sell_blocks_in_every_mode():
    for mode in ("quick", "enhanced", "strict", "campaign"):
        report = MODULE.check_native_note(BASE + "\n这是最后机会，立刻报名。", mode)
        assert not report["ok_to_publish"]
        assert "hard_sell_language" in codes(report)


if __name__ == "__main__":
    test_public_claim_requires_working_source_record()
    test_verified_public_claim_needs_no_bibliography_block()
    test_strict_result_claim_needs_user_owned_evidence()
    test_execution_mode_limits_are_frozen()
    test_strict_public_claim_blocks_without_source()
    test_enhanced_public_claim_remains_warning()
    test_campaign_proof_claim_blocks_without_evidence()
    test_hard_sell_blocks_in_every_mode()
    print("native_note_quality_check regression tests passed")
