# Benchmark Outline Reconstruction

Use this only when a WeChat article run explicitly uses benchmark hit articles, user-supplied benchmark outlines, or asks for `爆款大纲重构`, `深度二创`, or "参考爆款重构我的大纲".

This module is conditional. It must not replace the standard full-article workflow: source retrieval, context verification, article battle card, structure selection, drafting, reader-flow repair, AI-flavor gates, title design, and writeback rules still apply.

## Purpose

Convert benchmark structure into an original outline that fits the user's positioning, readers, evidence, and real experience.

Core path:

```text
对标内容 -> 亮点/盲点/缺点 -> 融合定位 -> 复用高光 -> 跨平台创新 -> 融入真实体验 -> 原创大纲
```

## When To Skip

Skip this module when:

- the user did not provide or request benchmark-based structure.
- the article is mainly a personal story, current reflection, or source-grounded knowledge article with no benchmark dependency.
- benchmark material is too thin or unsafe to borrow from.
- using this module would delay an ordinary full-article request without adding structural value.

## Five Reconstruction Principles

### 1. Analyze Benchmark Bright Spots, Blind Spots, And Weaknesses

For each benchmark, extract:

```markdown
亮点:
  - strongest angle:
  - strongest structure:
  - strongest scene/case:
  - strongest hook or conflict:
盲点:
  - user questions it does not answer:
  - missing scenarios:
  - missing proof or nuance:
缺点:
  - logic jump:
  - weak case:
  - shallow conclusion:
  - platform or reader mismatch:
```

Borrow only the structural lesson. Do not reuse wording, claims, personal stories, or unverified examples.

### 2. Fuse With The User's Positioning And Reader

Rewrite the benchmark structure through:

- the user's commercial positioning.
- target reader and emotional entry.
- product or conversion boundary.
- the user's public language: prefer `AI成长系统`, `个人成长系统`, `训练营`, `私有上下文系统`, or exact user-provided names over internal product names.

The reconstructed outline should answer: "Why must this article be written by the user, for this reader, from this positioning?"

### 3. Reuse The User's High-Signal Themes

Use the user's own high-performing or high-feedback themes when evidence exists:

- past articles with strong response.
- private-domain questions.
- user praise, objections, comments, consultation forms.
- product evidence or recurring scenes.
- themes repeatedly appearing in the user's system.

If no data is retrieved, mark `高光数据缺失` and avoid pretending the angle is proven.

### 4. Add Cross-Platform Perspective

Use cross-platform material only for new angle discovery, not copy:

- WeChat: argument depth, long-form narrative, system explanation.
- Xiaohongshu: first-impression hook, concrete scene, image-led proof.
- Zhihu: question framing, counterargument, logic chain.
- Bilibili/YouTube: workflow demonstration, step-by-step proof, audience interaction.

The goal is not to make a platform mashup. The goal is to find a fresher way to solve the reader's real problem.

### 5. Insert Real Experience And Personal Insight

Every reconstructed outline should reserve places for:

- the user's own scene or test.
- a concrete observation from Notion/personal-system evidence.
- a user/private-domain signal.
- a product or workflow artifact if commercial relevance exists.

If no real experience can be verified, label the outline as `结构假设` and do not invent first-person details.

## Output Template

Use this working output before drafting:

```markdown
## 爆款大纲重构卡

### 对标来源

- 对标 1:
- 对标 2:
- 对标 3:

### 三点剖析

| 对标 | 亮点 | 盲点 | 缺点 | 可借结构 | 禁止复用 |
| --- | --- | --- | --- | --- | --- |

### 融合定位

- 我的账号/商业定位:
- 本文目标读者:
- 本文情绪入口:
- 本文必须不同于对标的地方:

### 高光复用

- 已验证的高反馈主题:
- 可复用用户问题/评论/私域信号:
- 可嵌入个人经验:
- 缺失证据:

### 跨平台创新

- 借到的新切口:
- 借到的新结构:
- 不适合照搬的部分:

### 原创大纲

1. 开头:
2. 冲突/问题:
3. 核心判断:
4. 论证一:
5. 论证二:
6. 个人场景/用户证据:
7. 方法/系统:
8. 结尾/轻转化:

### 草稿与润色顺序

1. 逻辑清晰度: 论点、概念、因果、论证链是否清楚。
2. 平台与语言风格: 是否适合公众号长文，是否口语但不松散。
3. 个人风格校准: 是否接近用户代表作的判断、节奏、表达习惯。
4. AI 味清理: 进入专属 AI 味库和 `humanizer-zh` 双层 gate。
```

## Drafting Boundary

Do not use this module to decide who writes the first draft. In this skill, Codex may draft the article, but the draft must be grounded in retrieved sources, the reconstructed outline, personal evidence, reader-flow repair, and the existing AI-flavor gates.

Do not add generic "AI writing assistant roles" to the workflow. The skill already has concrete modules for retrieval, structure, revision, title design, reader flow, and AI-flavor cleanup.
