# Moments Media Decision

## Default Rule

Always decide what media best supports the朋友圈 post. Do not automatically generate images by default.

朋友圈 trust usually comes from real evidence: workspace photos, process screenshots, customer feedback, chat records, product/course/service screenshots, delivery material, payment/signup proof, planning boards, or real process material. Ian-style illustrations are strongest for concepts, methods, structures, status metaphors, and memorable cognitive anchors.

Default media advice should help the user show the real business, not decorate the post.

## Media Decision Gate

After the draft passes the AI-flavor gate, choose one primary media recommendation:

| Post situation | Preferred media | Why |
|---|---|---|
| 人设生活, daily scene, emotion, relationship, travel, study | real photo, selfie, scene photo, no image | Realness beats designed explanation |
| 客户反馈, service result, consultation question | customer feedback screenshot, chat screenshot, blurred proof | Trust depends on evidence |
| 报名, 付款, launch heat, social proof | payment/signup screenshot, product poster, blurred proof | Conversion needs visible proof |
| 产品介绍, deadline, launch CTA | product poster, offer screenshot, simple real asset | Clarify offer and next action |
| 概念解释, model, method, workflow, cognitive contrast | Ian-style illustration or shot idea | A visual metaphor helps memory |
| 过程记录 with strong scene | real process photo first; Ian illustration only if abstract structure matters | Preserve authenticity |
| Short sharp opinion | no image or simple screenshot | Avoid visual noise |

## Real Business Media Priority

Prefer these when available:
- screenshot of a real product page, delivery material, checklist, Notion page, planning board, or course/service document.
- customer feedback/chat screenshot with names, avatars, and sensitive details blurred.
- process photo from a real desk, meeting, consultation, review, recording, or writing scene.
- before/after material from a user journey, only when permission and context are clear.
- payment/signup proof only when it serves the trust-chain role and is verified.

Avoid defaulting to:
- generic cover posters.
- quote cards or golden-sentence cards.
- decorative AI images.
- over-designed campaign graphics that make the post feel like an ad.

## Ian Illustration Trigger Rules

Use or suggest `ian-xiaohei-illustrations` when:
- the user explicitly asks for 配图, 插图, 生成图, Ian 风格, 小黑图, 正文插图, 认知锚点图, or shot list.
- the post is a concept explanation, method, workflow, system structure, abstract contrast, or positioning anchor.
- strict/campaign mode needs a memorable visual anchor for a product philosophy, method, or misconception.
- a pinned朋友圈 explains an AI growth system, personal growth system, training camp, private context, or a signature method.

Do not suggest Ian illustration when:
- real customer proof is more persuasive.
- the post's point depends on a real life photo or screenshot.
- the post is ordinary daily content.
- using an illustration would make the朋友圈 feel over-produced.
- the post is already emotionally strong without media.
- real business proof would persuade more than an abstract visual.

If a screenshot or image contains a product name that is not verified as the current public name, recommend cropping, blurring, or using a truthful category-level caption until the user or current `product`/`commercial_positioning` source confirms it.

## Automation Policy

Default:
- Recommend media, do not generate.
- If Ian illustration is suitable, provide one concise shot idea.

Enhanced mode:
- Suggest Ian illustration only when it clearly strengthens concept/method memory.

Strict mode:
- If Ian illustration is highly suitable, ask or state: "这条适合生成一张 Ian 风格认知锚点图；如果你要，我可以继续生成。"

Campaign mode:
- Build a media map for the sequence.
- Use real proof for proof/CTA days.
- Use Ian illustration for 1-2 concept/method/positioning days at most.
- Do not turn every campaign post into an illustration-heavy sequence.

Full automatic generation:
- Only generate without asking when the user has explicitly said image generation should be automatic for this run, such as "配图也自动生成", "需要图就直接生成", or "发售战役里该生成图就生成".
- When generating, invoke `ian-xiaohei-illustrations` and follow its workflow: digest content, create shot strategy, generate single images only, inspect quality, and save assets.

## Media Output Format

For ordinary posts:

```markdown
发布建议：
- 配图：
- 时间：
- CTA：
- 复用：
```

When Ian illustration is suitable but not generated:

```markdown
配图建议：适合一张 Ian 风格认知锚点图。
Shot idea：...
是否生成：默认不自动生成；你说“生成”我再调用插图 Skill。
```

For campaign mode:

```markdown
媒体节奏：
- Day 1：
- Day 2：
- Day 3：
```
