#!/usr/bin/env python3

import unittest

import avatar_quality_check as quality


FORMAL = """# 用户画像：反复重建系统的一人公司经营者

## 1. 这个用户是谁
核心任务 / JTBD：把分散工作重新组织成可持续系统。
## 2. 他在什么情况下开始寻找帮助
最近一次在交付失控后寻找帮助。
## 3. 他真正想改变什么
希望稳定交付，而不只是拥有更多工具。
## 4. 他现在怎么解决，为什么没有解决好
当前替代方案是拼接多个模板。
## 5. 他为什么会购买，又为什么不会购买
为什么会购买：看到真实交付案例。
为什么不会购买：担心系统太复杂、自己无法持续使用。
## 6. 什么建立信任，他会怎样表达问题
用户原话与来源：「我不是没有工具，是每次用两周又散了。」来源：2026-08 客户访谈 A。
## 7. 已经确认的事实、洞察与假设
已确认事实：访谈中两次描述重建行为。
合理洞察：真正阻力可能是持续使用成本。
待验证假设：陪伴机制比模板数量更重要。
## 8. 分群与边界
暂不拆分。
## 9. 对商业系统的影响与下游交接
交给产品机会教练继续验证陪伴机制。
## 10. 仍然需要验证什么
需要对照已购买但未使用的客户。
## 证据来源
Level 1 一手强证据：2026-08 客户访谈 A。
"""

HYPOTHESIS = """# 用户画像假设：需要稳定工作流的一人公司经营者

## 1. 目前可能是哪类用户
## 2. 当前材料支持了什么
业务背景材料支持其存在。
## 3. 还不能确认什么
缺少真实购买原因。
## 4. 为什么现在不能作为正式画像
只有 Level 3 业务背景材料。
## 5. 下一步需要什么材料或访谈
补充一次近期购买咨询记录。
## 6. 支持或推翻假设的信号
出现重复购买触发则支持；真实客户目标不同则推翻。
"""

PARTIAL = """# 用户洞察阶段小结

## 本轮确认了什么
## 哪些仍然只是判断
## 当前最大的证据缺口
## 下一个聚焦问题或材料
"""


class AvatarQualityCheckTest(unittest.TestCase):
    def test_evidence_backed_formal_avatar_passes(self):
        result = quality.check_artifact(FORMAL, "formal")
        self.assertTrue(result["ok_to_publish"])
        self.assertEqual([], result["blocking_failures"])

    def test_formal_avatar_without_traceable_quote_blocks(self):
        text = FORMAL.replace("「我不是没有工具，是每次用两周又散了。」来源：2026-08 客户访谈 A。", "用户表示系统难以持续。")
        result = quality.check_artifact(text, "formal")
        self.assertFalse(result["ok_to_publish"])
        self.assertTrue(any(item["code"] == "formal_without_user_voice" for item in result["blocking_failures"]))

    def test_formal_avatar_without_strong_evidence_blocks(self):
        text = FORMAL.replace("Level 1 一手强证据", "Level 3 业务背景材料")
        result = quality.check_artifact(text, "formal")
        self.assertFalse(result["ok_to_publish"])
        self.assertTrue(any(item["code"] == "formal_without_strong_evidence" for item in result["blocking_failures"]))

    def test_hypothesis_can_use_weak_evidence(self):
        result = quality.check_artifact(HYPOTHESIS, "hypothesis")
        self.assertTrue(result["ok_to_publish"])

    def test_stage_summary_does_not_require_purchase_logic(self):
        result = quality.check_artifact(PARTIAL, "partial")
        self.assertTrue(result["ok_to_publish"])

    def test_downstream_overreach_is_warning(self):
        result = quality.check_artifact(FORMAL + "\n完整销售页\n", "formal")
        self.assertTrue(result["ok_to_publish"])
        self.assertTrue(any(item["code"] == "downstream_scope_overreach" for item in result["warnings"]))


if __name__ == "__main__":
    unittest.main()
