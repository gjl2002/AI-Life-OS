# Moments Publishability And Scheduling

## Candidate Material

Treat every input as `朋友圈候选素材`, not as a confirmed topic and not necessarily as a Notion 灵感 page.

Candidate material can be:
- a daily thought, mood, state, or unfinished realization.
- a real life or work scene.
- an existing draft or previously unpublished post.
- a Notion 灵感, 内容, review, product, or personal-system page.
- customer feedback, an external quote, a book idea, or public information.
- a direct message such as `我今天想发个朋友圈`.

Do not assume that valuable material should become a朋友圈 immediately. Run the publishability gate first.

## Mandatory Publishability Gate

Evaluate the candidate on these dimensions before classification, drafting, or scheduling:

1. **Personal ownership**: Is it connected to the user's real experience, observation, current work, relationship, or ongoing state? If it comes from another person or public source, is the user's own scene or judgment present?
2. **Positioning fit**: Does it reveal a useful part of the user's identity, values, growth path, professional capability, product logic, or relationship with readers?
3. **Truth and attribution**: Are first-person scenes, customer evidence, product claims, dates, prices, results, and external ideas supported and correctly attributed?
4. **朋友圈 fit**: Does it sound suitable for a relationship channel and familiar readers, rather than an article excerpt, lecture, abstract slogan, or context-free观点?
5. **Trust-chain value**: Does it help readers 认识我, 理解我, 相信我, 想靠近我, or 想购买?
6. **Distinct contribution**: Compared with recent朋友圈, does it add a new scene, proof, emotion, consequence, stage, method, or CTA role?
7. **Publication risk**: Does it expose private information, overstate a result, misuse a customer story, create product ambiguity, or produce excessive marketing pressure?

Use one of these internal verdicts:
- `适合发布`: the material is truthful, account-fit, Moments-native, and useful. Continue.
- `有价值但需要改造`: the core idea is useful, but it needs a real scene, personal anchor, evidence, narrower claim, different structure, or safer wording. Repair before drafting or scheduling.
- `暂缓`: the material may be publishable, but evidence, timing, or queue conditions are not ready.
- `仅做素材`: the material is useful but currently belongs in notes, long-form content, product material, or later review.
- `不建议发布`: it is off-positioning, unsupported, privacy-sensitive, duplicative without a new contribution, or unsafe to publish.

Use one of these user-facing decisions when the user asks for judgment or planning:
- `现在发`
- `进入排期`
- `暂存补素材`
- `不建议发布`

Always give a short reason. For `暂存补素材`, state the smallest missing item and the next action. Do not turn the gate into a visible scorecard unless the user asks for detailed evaluation.

## Purpose And Category Inference

Only after the candidate passes or has a clear repair path, infer its primary role and closest category. Use the current account and live content schema when available; do not assume every user has the same purpose/category options.

Infer both from the material by default. Ask the user only when the ambiguity would materially change the scene questions, evidence boundary, product claim, CTA, or publication decision.

Treat `目的` as the role this post plays in the trust sequence. Treat `分类` as the specific subject/scene family. Do not use `优先级` as a substitute for either.

## Notion Queue Source Of Truth

For current-state scheduling, resolve Runtime concept `content` and use that cloud target as the source of truth.

1. Read the live schema before querying.
2. Identify fields that actually express platform/form, account, status, purpose, category, planned time, publication time, title and body. Names and option values are not fixed.
3. If a platform/form field exists, use its real option to identify朋友圈 records. If not, combine account, title, body and relations; do not invent a missing field.
4. Infer missing purpose/category in working notes when useful. Missing values do not remove a relevant record from the queue.
5. Map the real status options to the conceptual stages candidate, drafting, ready and published. Do not create or rename options during a read-only scheduling task.

Notion reflects recorded state, not the live WeChat backend. If the user may have published a post without updating Notion, flag the possible state gap before relying on the schedule.

## Scheduling Decision

Do not recommend a publication date until the candidate passes the publishability gate.

When scheduling is requested or would materially affect the answer, read:
- recent `发布`朋友圈, including purpose, category, date, topic, and CTA pattern.
- all current `写稿中` and `待发布`朋友圈.
- relevant `选题` records when comparing topic collisions or upcoming themes.
- overdue and upcoming `预计发布日期` values.
- current campaign, launch, deadline, holiday, event, or time-sensitive context.

Then decide based on:
- recent mix across personal/life, professional/trust, and product/conversion roles.
- category and topic repetition.
- emotional and trust-chain rhythm.
- whether an existing overdue post should be rescheduled, replaced, merged, or held.
- freshness and time sensitivity of the new material.
- conversion density around an actual launch or campaign.

Do not hardcode a universal daily or weekly volume. Follow the user's current cadence and context. `值得写` does not mean `现在发`.

Return a concrete recommendation when enough state is available:

```markdown
发布判断：现在发 / 进入排期 / 暂存补素材 / 不建议发布
作用：...
分类：...
建议时间：YYYY-MM-DD HH:mm，或明确的时间段
原因：...
需要动作：写稿 / 补素材 / 调整旧排期 / 更新状态 / 无
```

If current queue data cannot be read, give a conditional timing suggestion and explicitly say that it is not a verified schedule.

## Write Permission

A recommendation does not authorize Notion changes.

Write or update Notion only when the user explicitly asks to execute, save, schedule, update, or write back. After writeback, fetch the page again and verify the pipeline fields and dates.
