#!/usr/bin/env python3
"""Regression tests for course_quality_check.py."""

import importlib.util
from pathlib import Path


SCRIPT = Path(__file__).with_name("course_quality_check.py")
SPEC = importlib.util.spec_from_file_location("course_quality_check", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


BASE_HANDOUT = """# 本节课目标
理解为什么真实输入会影响 AI 输出。

# 方法与任务
完成一个输入整理任务，并把结果提交为一张模板资产。

# 示例与自检
下面是一个假设示例。完成后使用自检清单检查结果，并进入下一步。
"""


def test_ordinary_handout_does_not_require_ppt_or_demo() -> None:
    report = MODULE.check_course(BASE_HANDOUT)
    assert report["status"] == "pass"
    assert not any("PPT" in item for item in report["blocking_failures"])


def test_timed_lesson_requires_timeline() -> None:
    report = MODULE.check_course(BASE_HANDOUT, deliverable="live-lesson", duration=60)
    assert any("time-coded" in item or "timeline" in item for item in report["blocking_failures"])


def test_ppt_gate_only_applies_when_requested() -> None:
    ordinary = MODULE.check_course(BASE_HANDOUT)
    requested = MODULE.check_course(BASE_HANDOUT, require_ppt=True)
    assert not any("PPT" in item for item in ordinary["blocking_failures"])
    assert any("PPT" in item for item in requested["blocking_failures"])


def test_missing_learner_asset_blocks() -> None:
    report = MODULE.check_course("# 目标\n讲清楚一个概念。\n\n# 内容\n这里只解释理论。\n\n# 结尾\n谢谢。")
    assert report["status"] == "blocked"
    assert any("submission or asset" in item for item in report["blocking_failures"])


if __name__ == "__main__":
    test_ordinary_handout_does_not_require_ppt_or_demo()
    test_timed_lesson_requires_timeline()
    test_ppt_gate_only_applies_when_requested()
    test_missing_learner_asset_blocks()
    print("course_quality_check regression tests passed")
