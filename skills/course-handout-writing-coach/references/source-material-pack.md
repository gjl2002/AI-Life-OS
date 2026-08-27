# Source Material Pack

Use this reference before drafting a lesson when the lesson should be grounded in the user's real knowledge base, course notes, product assets, or practice records.

## Search Contract

Do not rely only on the current prompt when the user expects the lesson to use their knowledge base or learned courses.

Use the smallest useful source packet. Search in this order when available:

1. User-supplied lesson brief, product architecture blueprint, course outline, or module plan.
2. Runtime `course` and `product` when the contract or delivery boundary is missing.
3. Runtime `commercial_positioning` only when commercial direction changes the lesson.
4. Runtime `user_profile`, `user_feedback`, `content`, or the current customer source when learner language or proof is needed.
5. Relevant user practice, project, review, screenshot, template, prompt, Agent, or SOP only when it supplies a real teaching unit or learner asset.
6. Runtime `note`, `information`, `question`, `book`, `course`, or a user-named transcript/source when a mechanism or example is missing.
7. Benchmark products or public content only when user-owned material is insufficient or the user asks for benchmarks.

## Retrieval Trigger

Do not search merely because a source exists. Search when the current material lacks one of these teaching roles:

- a credible mechanism;
- the user's own judgment;
- real practice or a bounded case;
- learner language;
- an executable asset.

Not every lesson needs all five. Record only gaps that affect the requested lesson. For full-course or evidence-sensitive work, use `course-retrieval-audit.md`.

Resolve sources through `$ai-life-system-init`, inspect the current schema or page structure, shortlist by title/summary/relation, and read promising records deeply enough to judge their actual value. Search by:

- lesson title
- module name
- target-user pain
- desired deliverable
- method keywords
- product name
- related tools, agents, templates, or prompts

If sources are missing, say so. Do not fill gaps with invented examples.

## Lesson Material Pack

Before writing a full lesson, produce or keep internally a material pack:

| 来源 | 类型 | 可拆解内容 | 可迁移机制 | 可用于本课 | 使用边界 |
| --- | --- | --- | --- | --- | --- |

Types:

- `用户本人实践`
- `用户/私域证据`
- `产品资产`
- `课程学习材料`
- `对标材料`
- `知识模型`

Also record `命中/未命中`, `素材职责`, and `关联的学员交付物` when an audit trail is needed. Ordinary handouts may keep only the selected sources and visible gaps.

## 拆迁法

```text
拆迁法 = 拆解 + 迁移
```

Use it when a course note, benchmark product, strong lesson, template, or workflow contains useful structure.

拆解:

- user problem
- lesson promise
- core judgment
- steps
- examples
- task
- feedback
- quality gate

迁移:

- adapt the mechanism into the user's target student
- rewrite in the user's voice
- replace examples with user's own practice, systems, or hypothetical samples clearly labeled
- turn the mechanism into a new task, SOP, prompt, or checklist

Do not copy another course's wording, proprietary sequence, screenshots, examples, testimonials, or claims.

## 收租法

```text
收租法 = 收集 + 组合
```

Use it when one useful node reveals multiple related materials.

Collect:

- related notes
- screenshots
- prompts
- workflows
- user questions
- cases
- templates
- existing skills or agents

Combine into:

- lesson method
- filled example
- worksheet
- prompt template
- assignment
- self-check
- feedback rubric

## Usage Boundaries

For user-owned practice and product assets:

- use directly when accurate and safe
- anonymize private user data
- mark screenshots or sensitive details that need masking

For paid-course or benchmark materials:

- use as internal inspiration
- extract mechanisms, structures, and quality gates
- rewrite through the user's own framework and examples
- do not reproduce proprietary content

For uncertain materials:

- label as `待验证`
- keep claims cautious
- avoid using them as proof
