# Runtime Source Routing

## Authority

Cloud Notion is the source of truth. Resolve all Notion targets through `$ai-life-system-init/scripts/runtime.py`; never embed database IDs, page URLs, personal paths, local Notion Sync paths, or a local database index.

Run Runtime `status` first. Prefer stable concept keys. If a concept is unavailable, use an exact live title only when the current task provides enough context to identify it safely.

## Always Resolve

| Concept | Purpose | Read rule |
| --- | --- | --- |
| `commercial_positioning` | audience, promise, differentiation, product bridge, tone, CTA boundary, public naming | Always read the current relevant section before drafting. |
| `content` | published/draft Xiaohongshu notes, differentiation, reuse, duplicate checks, optional writeback | Resolve every run; read past notes only under the mode rules. |

This preserves the current execution modes: commercial positioning is always read, while the depth of supporting retrieval depends on Quick, Enhanced, Strict, or Campaign mode.

## Conditional Concepts

Resolve only concepts that can materially change the current note.

| Concept | Use when | Typical evidence |
| --- | --- | --- |
| `product` | product mention, feature, offer, price, deadline, quota, delivery, or conversion | verified product facts and current public wording |
| `user_profile` | the note depends on a specific audience segment or reader language | recorded needs, contexts, objections, and vocabulary |
| `user_feedback` | feedback, result, testimonial, or customer-proof note | user-owned feedback and permission/publicability context |
| `client_communication` | consultation, objection, sales conversation, or recurring wording | anonymized customer language and real objections |
| `account` | account identity, platform strategy, public persona, or naming | current Xiaohongshu account context |
| `benchmark_content` | explicit benchmark note, cover, opening, structure, or image-order reconstruction | structural patterns, not borrowed claims |
| `benchmark_account` | explicit benchmark-account analysis | public account patterns, not personal facts |
| `life_moment` | first-person scene, milestone, turning point, or lived detail | user-owned events and dates |
| `note` | a user-authored insight or knowledge model shapes the note | current personal understanding |
| `book` | a book is used for a long-cycle human topic | one relevant idea with source context |
| `project` | workflow, progress, delivery, or implementation proof | user-owned actions, artifacts, and outcomes |
| `goal` | current priority or progress context materially affects the note | active target and current stage |
| `ai_flavor_library` | mandatory wording review stage when available | account-specific bad patterns and corrections |

If the user's image, supplied scene, or attached evidence already answers the factual question, it remains the primary source. Notion context should sharpen the note, not overwrite the material in front of the user.

## Retrieval Sequence

1. Understand the note's intended claim, image evidence, reader, and CTA.
2. Resolve `commercial_positioning` and `content`.
3. List the smallest conditional concept set required by the selected mode and note type.
4. Inspect titles, descriptions, summaries, dates, platform/type properties, and relations to rank relevance.
5. Fetch only pages that may change the angle, facts, publicability, or CTA.
6. Record missing sources and unresolved ambiguities internally.
7. Reassess the initial note type, target reader, public trust role, and evidence boundary when selected records change the original understanding.
8. At the review stage, resolve and query `ai_flavor_library` separately; do not scan it as a generic content source.

Relation means “candidate source,” not “must read every related page.” Avoid full-database and full-relation scans.

## Note-Type Source Bundles

Use these as retrieval starting points after resolving the always-required concepts. They are priority routes, not mandatory full reads: remove irrelevant concepts, add a conditional concept only when it can change the angle or factual accuracy, and inspect candidate metadata before fetching full pages.

| Note type | Priority conditional concepts | Retrieval focus |
| --- | --- | --- |
| 生活方式观点型 | `life_moment`, `note`; add `goal` or `project` only when central | lived scene, current reflection, concrete choice |
| 工作流证明型 | `project`; add `product` when the workflow supports a product claim | real process, artifact, before/after friction, verified outcome |
| 产品种草型 | `product`, `user_profile`; add `user_feedback` or `client_communication` when proof is used | product origin, fit, current facts, reader problem, proof |
| 用户案例拆解型 | `user_feedback`, `client_communication`, `user_profile`; add `product` when the solution depends on it | real wording, problem, objection, outcome, publicability |
| 第三方故事隐喻型 | `note`; add `benchmark_content` only for an explicit benchmark source | named public story, user's own judgment, verified parallel |
| 发售/公开课转化型 | `product`, `user_profile`, `user_feedback`, `account` | current offer, time, CTA, audience fit, proof, account context |
| 里程碑背书型 | `project`, `goal`; add `life_moment` or `user_feedback` when relevant | real milestone, process, context, lesson, supporting evidence |
| 认知判断型 | `note`; add `book`, `project`, or `life_moment` only when they support the judgment | one sharp claim, one concrete example, one evidence chain |
| 图片海报变化/视觉迭代型 | `project`; add `product` or `benchmark_content` when relevant | iteration sequence, what changed, what the images actually prove |

The Runtime-resolved `content` source still follows mode rules: Quick mode does not search past notes unless repurposing; enhanced, strict, and campaign mode use it for differentiation.

## Mode Depth

- **Quick mode**: current positioning, current material, and directly relevant Runtime-resolved cloud sources. Search past content only when repurposing.
- **Enhanced mode**: add a source checklist, mapped evidence, and past-content differentiation.
- **Strict mode**: confirm every claim that depends on product, user, result, milestone, conversion, or public source evidence and complete a full battle card.
- **Campaign mode**: use strict evidence discipline and also read the source records needed to prevent sequence-level repetition.

These descriptions clarify source depth only; they do not change the mode triggers or outputs in `SKILL.md`.

## Source Labels

Keep these labels in the private working record:

- `用户本人经历`
- `用户/私域证据`
- `产品证据`
- `知识模型`
- `过往内容`
- `对标内容`
- `第三方案例`
- `图片证据`
- `里程碑证据`
- `公开来源`
- `书籍来源`
- `AI 综合推断`

Do not blend external views, user-owned practice, and model inference into one voice.

## Truth And Privacy Rules

- Do not invent a first-person experience, customer quote, result, milestone, product fact, public name, price, deadline, quota, or CTA.
- Do not present a benchmark or third-party result as the user's result.
- For customer and private-domain records, minimize disclosure, anonymize by default, and verify that the image and wording are publishable.
- For internal names visible in images, recommend crop, blur, cover, or omission unless the user has explicitly approved the public name.
- A visible “source” label is not verification. Read the source record and confirm that it supports the claim.
- If evidence is incomplete, narrow the claim or state the gap; do not silently search wider or fill it with model knowledge.

## Public Research Boundary

Do not automatically browse for more information. Use current supplied and Runtime-resolved sources by default.

Browse only when:

- the user asks for research or verification;
- a current public fact is essential to publishing the note;
- a named public source must be checked and is not available in Notion.

Keep public-source verification in the private working record and write the note in a native, non-academic way.

## Failure Handling

- `ready`: use the unique target.
- `multiple`: filter with business object and exact live title; if ambiguity remains, ask the user.
- `not_found` for optional evidence: continue and disclose the gap if important.
- `not_found` for `commercial_positioning`, `content`, or an essential factual source: stop instead of guessing.
- `needs_init`: ask the user to run `$ai-life-system-init`; do not use fixed fallback identifiers.
