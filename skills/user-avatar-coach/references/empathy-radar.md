# Empathy Radar

## Purpose

Use this reference to decode user emotion and behavior before clustering pain points, purchase motives, objections, or content triggers.

Empathy here means reading the emotion and need behind user behavior without rushing to judge, educate, persuade, or overwrite the user's world with role stereotypes.

Do not treat this as proof by itself. Use it as an interpretation layer over real user evidence.

## When To Use

Use the empathy radar when materials contain:
- emotional words such as 爽, 烦, 怕, 焦虑, 不值, 麻烦, 不敢, 没必要, 被坑, 被理解, 不舒服.
- objections, hesitation, non-purchase reasons, refunds, complaints, praise, or strong recommendations.
- conflict between what users say and what they choose.
- role-based assumptions such as 用户应该, 妈妈应该, 学生应该, 创业者应该, 做知识管理的人应该.
- content, sales-page, offer, or product-design decisions that depend on why users feel moved or resistant.

Skip it when the task only needs factual database cleanup, schema inspection, or mechanical writeback.

## Core Radar

For each important quote, behavior, or feedback item, decode:

```markdown
| User evidence | Surface expression | Emotion entry | Underlying need / fear | Defense or boundary | Product meaning | Evidence level |
| --- | --- | --- | --- | --- | --- | --- |
```

Keep the user's original wording when it carries emotion. Mark uncertain interpretations as hypotheses.

## Emotion Entries

### 愉悦

Signal: the user feels understood, respected, relieved, capable, safe, seen, or smoothly supported.

Ask:
- What need was satisfied?
- What part of the product, content, service, or interaction created this satisfaction?
- Is the satisfaction functional, emotional, social, identity-based, or status-based?

Product meaning:
- Value point.
- Trust trigger.
- Retention reason.
- Content proof point.

### 爽

Signal: a long-tightened need suddenly gets released. The user feels "finally", "exactly", "this is it", or unexpectedly strong relief.

Ask:
- What tension had been accumulating?
- What old friction, delay, shame, confusion, or fear was released?
- Was the release repeatable or only a one-off surprise?

Product meaning:
- Possible growth hook or activation moment.
- Strong sales-page before-after contrast.
- High-intensity content angle.

### 不爽

Signal: the user is annoyed, bored, disappointed, tired, confused, or says it is "麻烦", "鸡肋", "没用", "不值".

Ask:
- What expectation or need was not satisfied?
- Was something previously satisfying removed, slowed down, hidden, or made uncertain?
- Is the issue an optimization point or a deeper non-fit?

Product meaning:
- Friction.
- Optimization point.
- Weak promise.
- Possible churn reason.

### 愤怒

Signal: the user feels cheated, disrespected, interrupted, controlled, exposed, blamed, or unfairly treated.

Ask:
- What boundary did the user feel was violated?
- Did the product, seller, content, group, or delivery process overstep?
- What did the user believe should have been protected?

Product meaning:
- Risk point.
- Trust damage.
- Promise or expectation mismatch.
- Boundary language needed in sales or delivery.

### 恐惧

Signal: the user avoids action, delays purchase, asks for guarantees, over-checks details, or repeatedly worries about consequences.

Ask:
- What bad outcome is the user trying to avoid?
- What would this decision cost if it fails: money, time, identity, dignity, relationship, career, health, or safety?
- Is fear the actual pain point, or only a surface concern?

Product meaning:
- Core pain point.
- Urgency driver.
- Guarantee, proof, case, or onboarding requirement.
- Offer positioning clue.

### 焦虑

Signal: the user imagines future risk, compares constantly, cannot decide, collects information, or says "怕错过", "不知道怎么选", "来不及了".

Ask:
- What future scenario is the user mentally rehearsing?
- What uncertainty is not being contained?
- Does content need to reduce uncertainty or sharpen the urgency?

Product meaning:
- Content entry point.
- Lead magnet topic.
- Decision-support feature.
- Risk-reversal message.

### 羞耻

Signal: the user avoids exposing weakness, hides confusion, uses vague language, jokes about failure, or asks anonymously.

Ask:
- What does the user not want others to know?
- What identity would be threatened if this problem were visible?
- How can the product protect dignity and lower exposure risk?

Product meaning:
- Privacy requirement.
- Gentle onboarding.
- Non-judgmental copy.
- Safer consultation or community design.

### 防御

Signal: the user starts debating, asks many skeptical questions, says "我再想想", rejects explanation, or goes quiet after being educated.

Ask:
- What triggered resistance?
- Did the product, content, sales message, or researcher make the user think too hard?
- Is the user protecting money, time, autonomy, status, privacy, or self-image?

Product meaning:
- Conversion resistance.
- Copy or UX complexity.
- Trust gap.
- Need for proof, familiarity, simpler path, or less pressure.

## 潜意识与真实选择

Do not rely only on what users say in public, role-bound, or polite settings. Compare:
- stated preference vs actual choice.
- praise vs purchase.
- complaint vs continued use.
- claimed need vs repeated behavior.
- public identity vs private workaround.

When words and behavior conflict, treat behavior as stronger evidence, but do not invent motivation. State the conflict and label the interpretation as insight or hypothesis.

## 去角色化检查

Before writing an insight, check whether it secretly depends on "用户应该".

Risky assumptions:
- 妈妈应该更重视孩子.
- 学生应该爱学习.
- 创业者应该愿意折腾工具.
- 知识管理用户应该愿意整理.
- 付费用户应该更自律.

Replace role assumptions with evidence questions:
- In this scene, what was the person actually trying to protect or obtain?
- What did they choose when no one was watching?
- What pressure would be required for them to act like the role expects?
- Does this product serve a relaxed individual, a pressured role, or a collective organization?

## Analyst Self-Check

Before finalizing a product or avatar insight, check:
- Am I judging the user for being irrational, lazy, vain, fearful, or inconsistent?
- Am I trying to educate or persuade instead of understanding the emotion scene?
- Am I using my own self-discipline, taste, or product ideals as the standard?
- Did I separate user facts, my interpretation, and unverified hypotheses?

If any answer is yes, weaken the claim and return to user evidence.

## Output Guidance

把共情雷达结果整合进：

- 用户所处场景与真正想改变的部分；
- 购买动机与未购买原因；
- 信任触发点、边界和风险顾虑；
- 用户原话与内容、销售表达约束；
- 产品 Agent 需要继续验证的体验问题。

除非用户要求，不单独生成一章“共情分析”。只有它能解释关键推理、来源不确定性或言行冲突时才展示简洁雷达表。本 Skill 只传递下游约束，不据此直接完成销售页、内容计划或产品设计。
