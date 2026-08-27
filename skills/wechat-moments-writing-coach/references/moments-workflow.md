# Moments Workflow

## Mode Selection

Use the lightest mode that preserves truth and usefulness.

| Mode | Use when | Required output |
|---|---|---|
| Quick | ordinary daily post, casual scene, simple thought, simple rewrite | lightweight publishability decision, one-line diagnosis, one final draft by default, lightweight AI-flavor gate, media recommendation, publishing advice |
| Enhanced | professional value, customer feedback, product soft mention, concept explanation, service process, style reuse, queue-aware scheduling | publishability decision, minimal Runtime source packet, simplified battle card, context verification, one final draft by default, AI-flavor risk rating, media recommendation |
| Strict | pinned post, product intro, important launch, strong conversion, positioning post | Runtime source resolution, full battle card, source checklist, context verification, evidence-backed drafts, mandatory AI-flavor pass, deterministic quality gate, media decision gate |
| Campaign | 3-7 day launch sequence, content matrix, posting plan | campaign map, daily roles, Runtime source resolution, verification for each evidence-sensitive post, draft sequence, mandatory AI-flavor pass and media decision for each post |

## Full Workflow

1. Accept the input as candidate material. It may be a daily thought, current state, scene, draft, Notion page, customer evidence, or external idea.
2. Decide task shape: publishability judgment, single post, polish, repurpose, batch schedule, pinned post, campaign sequence, or review.
3. Run the publishability gate in `moments-publishability-scheduling.md` before drafting or scheduling.
4. If the material passes or is repairable, infer purpose and concrete category:
   - 人设生活: real life, emotion, growth, daily record, relationship, holiday.
   - 专业价值: process, method, judgment, service record, customer result, industry observation.
   - 营销卖货: product, offer, launch,报名, deadline, spots, payment proof, CTA.
   - 概念解释: explain a concept, model, method, or distinction.
   - 过程记录: record an experience, project, transformation, emotional arc, or creation process.
5. Identify trust-chain role:
   - 认识我: show a real person.
   - 理解我: show values and context.
   - 相信我: show capability and proof.
   - 想靠近我: build resonance and invitation.
   - 想购买: guide action.
6. Select mode.
7. When the user asks when to publish or requests a schedule, read the current cloud Notion queue according to `moments-publishability-scheduling.md` and decide now, schedule, hold, or reject.
8. Resolve only the required cloud concepts through the current `$ai-life-system-init` Runtime when the selected mode needs Notion context.
9. Retrieve sources only when the selected mode needs them. For enhanced, strict, and campaign mode, search prior朋友圈 for differentiation; for long-cycle human questions, search book materials before generic web thought-leadership.
10. Run context verification for enhanced, strict, and campaign mode, including public/book claim attribution when used.
11. Build a battle card.
12. Select structure and draft one final post in the current account's verified style.
13. Run the AI-flavor gate and private-domain fit review.
14. Run the deterministic quality gate when feasible, especially before final output or writeback.
15. Rewrite any draft that fails the required gate for the selected mode.
16. Run the media decision gate.
17. Give publishing advice, distinguishing verified queue-based scheduling from conditional timing advice.
18. Optionally write back and later review performance. Draft variants are only added when the user explicitly asks for options or comparison.

## AI-Flavor Gate Placement

Do not treat AI-flavor detection as an optional polish step. It is a required gate after drafting and before final delivery.

- Quick mode: run a lightweight gate silently; revise obvious template wording before output.
- Enhanced mode: rate risk as low, medium, or high; rewrite medium/high risk drafts before presenting them.
- Strict mode: the final selected draft must pass with low risk. If not, rewrite and run the gate again.
- Campaign mode: each post in the sequence must pass with low risk or be rewritten before final delivery.

## Source And Verification Gate Placement

Do not start important final copy from vibes alone.

- Enhanced mode: resolve the minimal source packet, then verify the main scene/proof/product fact before final drafts.
- Strict mode: resolve the necessary Runtime concepts and run context verification before drafting. Unverified first-person, customer, product, price, deadline, quota, or CTA claims must be removed, weakened, or verified in cloud Notion.
- Campaign mode: resolve one campaign-level source packet, then verify each day's evidence-sensitive claim before drafting that post.

## Battle Card

Use full battle card for strict and campaign mode. Use abbreviated battle card for enhanced mode. For quick mode, a one-line diagnosis is enough.

```markdown
朋友圈作战卡
- 任务：
- 候选素材来源：日常感想 / 真实场景 / 现有草稿 / Notion页面 / 用户证据 / 外部信息
- 发布适配判断：适合发布 / 有价值但需要改造 / 不建议发布
- 判断理由：
- 最小补充素材：
- 发布决策：现在发 / 进入排期 / 暂存补素材 / 不建议发布
- 内容类型：
- 具体分类：
- 信任链路：
- 目标读者：
- 核心情绪：
- 核心素材：
- 相似过往朋友圈：
- 本条新贡献：
- 公开/书籍来源：
- 来源预检：
- 证据来源：
- 事实边界：
- 可放心写：
- 需要弱化/删除：
- 结构选择：
- CTA：
- 当前队列摘要：
- 建议发布日期：
- 排期理由：
- 风险：
```

## Public And Book Source Rule

朋友圈 is not a bibliography. When a post uses a study, report, interview, podcast, named person, or book:

- Keep full source identity in working notes.
- Use a natural source anchor in the post: publication, institution, book title, person, or program.
- Put a full source in a first comment or offer it in private chat only when the reader needs to inspect the claim; do not append a `参考资料` block by default.
- For long-cycle human questions, select at most one relevant book and one exact idea, then return to the writer's real scene or judgment.

## Campaign Mode

For a launch or sales sprint, do not write isolated posts first. Build a sequence.

Default 7-day campaign:
1. Product-origin or personal story: why this exists.
2. User pain: what target readers are stuck in.
3. Professional value: one key misunderstanding or method.
4. Product/process: how the solution is built.
5. Proof: customer feedback, result, question, or case.
6. Fit and not-fit: qualify the reader.
7. Deadline/CTA: scarcity, confidence, and action.

For shorter campaigns, preserve the arc: story -> pain/value -> proof -> CTA.

## Closed Loop

When the user asks for a full workflow, help them close the loop:
- capture raw material.
- generate post.
- select or generate media when appropriate.
- schedule/publish.
- record data.
- mark reusable posts.
- extract lessons for future drafts.
