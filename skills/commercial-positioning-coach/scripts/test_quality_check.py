#!/usr/bin/env python3

import unittest

import commercial_positioning_quality_check as quality


FINAL = """# 商业定位地图

## 1. 当前定位
## 2. 核心客户与发生场景
客户原话：我需要更稳定的工作流。
## 3. 核心问题与欲望差距
当前替代方案：碎片化工具。
## 4. 价值机制与产品假设
## 5. POV、相关差异与可信理由
## 6. 当前市场证据
已有咨询与交付反馈。
## 7. 商业系统影响与下游交接
下一步交给用户研究与产品机会 Skill。
## 8. 未知、验证与更新条件
需要验证并记录支持或推翻信号。
"""


class QualityCheckTest(unittest.TestCase):
    def test_complete_final_contract_passes(self):
        result = quality.check_artifact(FINAL, "final")
        self.assertTrue(result["ok_to_finalize"])
        self.assertEqual([], result["blocking_failures"])

    def test_missing_value_mechanism_blocks_final(self):
        result = quality.check_artifact(FINAL.replace("## 4. 价值机制与产品假设", "## 4. 产品"), "final")
        self.assertFalse(result["ok_to_finalize"])
        self.assertIn("missing section: value_mechanism", result["blocking_failures"])

    def test_downstream_overreach_is_warning_not_fake_quality_score(self):
        result = quality.check_artifact(FINAL + "\n完整产品架构\n", "final")
        self.assertTrue(result["ok_to_finalize"])
        self.assertTrue(any("downstream" in warning for warning in result["warnings"]))

    def test_partial_contract_does_not_require_market_evidence(self):
        text = """# 商业定位阶段小结
## 本轮确认了什么
## 哪些仍是假设
## 当前最大的证据缺口
## 下一个聚焦问题
"""
        result = quality.check_artifact(text, "partial")
        self.assertTrue(result["ok_to_finalize"])


if __name__ == "__main__":
    unittest.main()
