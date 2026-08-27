# Evidence Audit

## Purpose

Use this before calling an avatar formal and before writeback. The audit ensures every claim is supported by evidence, every insight is separated from facts, and every weak conclusion is labeled as a hypothesis.

## Evidence Matrix

Build this internal matrix for formal avatars and important hypothesis avatars:

```markdown
证据矩阵：
- 结论：
  - 类型：已确认事实 / 合理洞察 / 待验证假设
  - 证据等级：Level 1 / Level 2 / Level 3 / Level 4
  - 来源：
  - 用户原话：
  - 可信度：
  - 是否可写入正式画像：
```

Do not include the full matrix in the final answer unless the user asks, source uncertainty matters, or the avatar is being written back.

## Formal Avatar Boundary

Only produce a formal avatar when at least one is true:
- multiple Level 1 materials show repeated patterns.
- one rich Level 1 material plus strong Level 2 support.
- an existing Notion avatar is strengthened by new direct user evidence.

Otherwise produce a hypothesis avatar.

## Segmentation Audit

Before merging users into one avatar, check whether the material contains different:
- jobs-to-be-done.
- trigger situations.
- purchase motivations.
- non-purchase reasons.
- trust requirements.
- price/time sensitivity.
- product use scenarios.
- content triggers.

If differences change selling, product, content, or delivery strategy, split the avatar.

Use:
- 核心用户画像: strongest evidence and best fit.
- 次级用户画像: real but less central.
- 潜在但未验证用户画像: plausible but thin evidence.
- 不适合用户: recurring poor-fit pattern.

## Business Assumption Filter

Mark a claim as hypothesis when it mainly comes from:
- the user's business hope.
- product positioning without user voice.
- theory-library concepts.
- competitor material.
- one intense but isolated story.
- demographic stereotypes.

Do not promote these into confirmed facts.

## Purchase Logic Audit

A usable buyer avatar must explain:
- why buy.
- why not buy.
- when urgency appears.
- what builds trust.
- what promise/result is worth paying for.
- what content or sales-page language activates the user.

If these are missing, output missing evidence and validation questions instead of a finished buyer persona.

## Final Decision

Before final output, state internally:
- `formal_avatar_allowed: yes/no`
- `segmentation_needed: yes/no`
- `main_evidence_gap: ...`
- `writeback_safe: yes/no`

If `formal_avatar_allowed=no`, use the hypothesis avatar format.
