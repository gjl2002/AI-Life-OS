# Benchmark Note Reconstruction

Use this only when a Xiaohongshu run explicitly uses benchmark notes, user-supplied benchmark covers/titles/openings/image order, or asks for `小红书爆款二创`, `对标重构`, or "参考这篇爆款笔记".

This module is conditional. It must not replace the native note workflow: source retrieval, visual evidence classification, battle card, visual context verification, note type selection, title/hook design, review gates, and writeback rules still apply.

## Purpose

Convert benchmark note patterns into a native note grounded in the user's real image evidence, scene, experience, and commercial positioning.

Core path:

```text
对标笔记 -> 封面/标题/开头/图片顺序拆解 -> 亮点/盲点/缺点 -> 真实图片证据重构 -> 用户经验表达 -> 原生笔记
```

## Benchmark Breakdown

For each benchmark, extract:

```markdown
封面亮点:
标题亮点:
开头亮点:
图片顺序亮点:
互动/评论引导:
盲点:
缺点:
可借结构:
禁止复用:
```

Borrow visual and structural logic only. Do not reuse benchmark claims, life scenes, screenshots, results, or personal story.

## Reconstruction Rules

- Rebuild around the user's real photos, screenshots, product assets, customer feedback, service scenes, or milestone evidence.
- If the user lacks real image evidence, mark the note as weak for Xiaohongshu and suggest the smallest image/proof to capture.
- Keep the note image-led. Do not turn it into a WeChat-style text essay.
- Keep the opening tied to the cover image; the first sentence should explain why the image matters.
- Replace benchmark "lifestyle/result proof" with the user's verified evidence or remove the claim.

## Output Template

```markdown
## 小红书爆款二创卡

### 对标来源

- 对标笔记:

### 三点剖析

| 模块 | 亮点 | 盲点 | 缺点 | 可借 | 禁止复用 |
| --- | --- | --- | --- | --- | --- |
| 封面 |  |  |  |  |  |
| 标题 |  |  |  |  |  |
| 开头 |  |  |  |  |  |
| 图片顺序 |  |  |  |  |  |

### 我的真实证据重构

- 可用图片/截图:
- 可用真实场景:
- 可用用户反馈/产品证据:
- 可用个人经验:
- 缺失证据:

### 新笔记结构

- 封面建议:
- 标题方向:
- 第一段:
- 图片顺序:
- 正文主线:
- 评论引导:
- 风险:
```

## Anti-Move

Do not create "搬运味小红书": generic benchmark-like title, borrowed lifestyle scene, copied image order without matching real evidence, or text that sounds true but cannot be seen in the user's images.
