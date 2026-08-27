# Source Retrieval Rules

## Retrieval Goal

Collect only the evidence that can change the article. Use cloud Notion through `$ai-life-system-init`; do not read all relations or scan the full workspace for completeness.

Before retrieval, run `article-source-preflight.md`. Every selected item must retain a traceable Notion or public URL.

## Layered Reading Budget

Resolve every required Runtime concept and inspect the relevant source structure, but do not equate resolution or Relation membership with full-text reading.

Use four layers:

1. **Resolve:** confirm the live concept, page/database identity, and usable schema or page boundary.
2. **Screen:** query titles, dates, summaries, relation labels, and key fields. Start with up to roughly 10 candidates per relevant source rather than scanning the full database.
3. **Read deeply:** fetch the small set most likely to change the article. A practical starting point is 1–2 personal scenes, 1–3 knowledge or benchmark records, and 3–5 duplicate candidates when differentiation needs inspection.
4. **Expand deliberately:** widen the query or read more full records only when the material-sufficiency audit identifies an exact gap, sources conflict, a current factual claim needs stronger verification, or the user explicitly requests broader coverage.

These are retrieval defaults, not hard numerical caps. Never use the budget to skip a mandatory evidence gate; satisfy the gate through the smallest relevant reading set, then expand only for a named reason.

Historical feedback is also targeted retrieval. Do not scan all comments or all reviews. Start from the closest matching article and follow only relevant feedback or directly connected later reflection.

## Search Order

For a full article, use this order without removing any gate:

1. `commercial_positioning`: current audience, value, boundaries, offer language, and reader-facing commercial naming.
2. `content`: duplicate and published-content differentiation check; when the historical-feedback trigger fires, retrieve the closest old article, its relevant comments/feedback, and directly related later review or correction.
3. Personal path: `personal_story`, `life_moment`, `life_journey`; retrieve recent review/goal/project material only when it directly explains the topic.
4. Reader and commercial evidence as relevant: `user_profile`, `user_feedback`, `client_communication`, `product`, `account`.
5. Knowledge support as relevant: `note`, `information`, `book`, `question`.
6. `benchmark_content`: structure, hook, tension, rhythm, title grammar, and closing move only.
7. Web research only when internal sources cannot support a current fact, public case, named viewpoint, study, report, interview, talk, or book claim.
8. Voice and review sources: use `style_corpus` before drafting to build the temporary style card and again after drafting to check fit; use `ai_flavor_library` after drafting as the negative language filter. Neither source is evidence for the article’s factual claims.

If the user provides a Notion link, page title, outline, draft, or specific source, fetch it as a required named source before this route, then continue the full route.

## Required Database Resolution

Use Runtime stable concepts, never embedded IDs:

| Need | Concept | Required behavior |
| --- | --- | --- |
| Commercial boundary | `commercial_positioning` | Read the current ordinary page before deciding audience, offer, CTA, or product naming. |
| Existing articles/writeback | `content` | Search overlapping titles, questions, reader pain, and core judgments. |
| First-person evidence | `personal_story`, `life_moment`, `life_journey` | Produce 1–2 candidate scenes or record `no usable public scene`. |
| Reader evidence | `user_profile`, `user_feedback`, `client_communication` | Read only when audience pain, objections, language, or conversion matters. |
| Product proof | `product`, `account` | Use when the article contains product, delivery, campaign, or account claims. |
| Knowledge models | `note`, `information`, `book`, `question` | Select focused support; do not average-summarize every relation. |
| Benchmark patterns | `benchmark_content` | Borrow patterns, never wording or factual claims. |
| Positive voice | `style_corpus` | Select relevant user-authored examples and extract voice signals. |
| Negative language filter | `ai_flavor_library` | Apply live `必删 / 慎用 / 可保留` guidance. |

`not_found` does not authorize a fixed fallback. If the user provided a title or URL, search/fetch it in cloud Notion; otherwise record the gap.

## Historical Feedback Route

Use `editorial-claim-audit.md` to decide whether this route is triggered.

When triggered:

1. search `content` for the closest earlier article;
2. fetch relevant comments, replies, or feedback attached to it when available;
3. follow a directly linked or clearly matching daily review, cognitive note, post-publication review, or later correction;
4. record whether the feedback is a factual error, concept-boundary issue, value disagreement, or pure attack;
5. verify factual and concept-boundary corrections before adopting them.

Do not treat comments as automatically true. Their role is to expose a claim that needs verification, a boundary that needs clarification, or a reader defense the article should anticipate.

## Temporary Style Card

After evidence retrieval and before drafting, resolve `style_corpus` and select 3–5 relevant user-authored examples when available. Rank by platform, article type, topic, recency, and proven performance when such evidence exists. Do not read the entire corpus by default.

Build this working card:

```markdown
临时文风卡
- 参考文章：
- 目标读者：
- 第一人称距离：
- 句长与节奏：
- 段落长度：
- 故事密度：
- 判断锋利度：
- 常用开头：
- 过渡方式：
- 结尾方式：
- 支持的常用表达：
- 应避免表达：
- 本次不继承特征：
```

Explicit article instructions override corpus patterns. Current `commercial_positioning` and relevant `user_profile` evidence constrain audience and offer language. The card should capture repeated signals across selected examples without mechanically imitating one article or averaging the full corpus into a generic style.

## Personal Story Asset Source

The personal-path layer combines `personal_story`, `life_moment`, and `life_journey`; it is not a new database. Search by topic, stage, conflict, result, and publicability.

For each candidate, record:

- scene and time context
- conflict
- action
- result or learning
- publicability: 可公开 / 需模糊 / 不可公开
- article function: opening / observation / turn / method example / product origin / closing echo
- source URL

## Personal Scene Integration Gate

Full article retrieval must end with either:

- 1–2 real candidate scenes and one selected default scene; or
- `no usable public scene` with the reason.

By default, insert one selected scene or user-owned observation into the reader-facing article. Blur identifying details without changing the truth when necessary. Never invent a first-person scene.

## Benchmark Content Library

Resolve `benchmark_content`. Select records by topic, reader pain, emotion, business/growth angle, or title signal. Extract:

- title pattern
- opening hook
- central conflict
- story/argument order
- paragraph rhythm
- emotional escalation
- closing move
- structure worth borrowing
- wording or claims that must not be copied

Benchmark content is a learning source, not factual endorsement evidence.

## Source Labels

Label every candidate as one of:

- `用户本人经历`
- `用户/私域证据`
- `第三方案例`
- `知识模型`
- `对标内容`
- `高质量内容`
- `联网/公开资料补充`
- `联网/公开思想补充`

## Endorsement Evidence Gate

Find at least one credible item supporting the core judgment:

1. user-owned scene, observation, feedback, delivery, or product evidence;
2. focused internal Note, Information, Book, or Question material;
3. clearly labeled third-party case;
4. verified public data, report, study, expert/author/book idea, interview, or talk.

If no credible support exists, weaken or remove the strong claim. Benchmark structure, generic model definitions, motivational sentences, and invented personal stories do not count.

For public claims, maintain a claim-to-source record with the named author/speaker/organization, work or event, publication/host, date/year when available, direct link, and the exact article claim it supports.

## Book-Backed Endorsement Procedure

For long-cycle human questions such as learning, agency, self-knowledge, decisions, habits, attention, creativity, values, or life direction:

1. resolve and search `book` before generic web thought-leadership;
2. prefer a book the user actually read, highlighted, or connected to a Note;
3. select one book and one concrete idea unless the article compares books;
4. record author, title, exact idea/chapter/passage, supported claim, source status, and URL;
5. introduce the book conversationally and return to the user’s scene or judgment;
6. keep quotations short and put full details in `参考资料`.

## Candidate Format

```markdown
素材名称
- 类型：
- 简介：
- 行动/结果：
- 可用角度：
- 来源：
```

For benchmark records:

```markdown
对标内容标题
- 类型：对标内容
- 匹配原因：
- 可借鉴结构：
- 可借鉴表达/节奏：
- 不应照搬：
- 来源：
```

## Truth Rules

- Never invent or reassign a personal story.
- Never imply complete workspace coverage when retrieval was sampled.
- Never treat an outline as proof that retrieval and review are complete.
- Never use web evidence as a personally witnessed case.
- Preserve source links and source identity.
- When a named public source cannot be verified, retrieve it, relabel the point as the user’s inference, weaken it, or remove it.
- If a selected source conflicts with current commercial positioning or user evidence, preserve the conflict in the battle card instead of averaging it away.
- Relation means “candidate”, not “must read in full”.

## Strict Retrieval Log

```markdown
步骤：
Runtime 概念：
解析目标：
云端检索：
联网检索：
找到：
选用：
未找到/未使用：
原因：
```

Keep the full log as working context. Surface only a concise source summary and truthfulness-relevant warnings unless the user asks for the log.
