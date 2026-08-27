# Editorial Claim Audit

Run this audit twice: after the material-sufficiency audit and before the battle card, then again after the complete draft. It prevents a source-rich article from becoming overbuilt, weakly related, technically careless, or disconnected from what readers previously corrected.

## Core Principle

Retrieval creates a candidate pool. It does not create an obligation to put every personal story, case, book, theory, screenshot, and product fact into the article.

The body should contain only the material needed to defend one central judgment in this article.

## Working Record

```markdown
核心判断：
标题核心冲突：
候选材料审查：
历史反馈触发：是 / 否
查过的旧文章与反馈：
需要继承的修正：
主张类型与时效：
需要联网/原始来源复核：
术语使用层级：
正文采用材料：
正文删除材料及原因：
压缩前后字数：
压缩后是否损害逻辑：
```

## 1. Case-to-Claim Relevance Gate

For every personal story, user case, third-party case, book, study, and screenshot, answer:

1. Which exact sentence or causal step does this material support?
2. Is it direct evidence, conceptual explanation, lived illustration, or merely related to the topic?
3. If it is removed, does the central proof actually break?
4. Is there a shorter or stronger piece of evidence already in the pool?
5. Is the transition cost greater than the proof value?

Classify each candidate:

- `core`: the article's judgment cannot be responsibly defended without it;
- `direct_support`: directly explains or verifies one important step;
- `illustration`: makes an already-supported point visible or memorable;
- `adjacent`: relevant to the broad topic but does not prove this article's claim.

Use `core` and the strongest `direct_support`. Use an `illustration` only when it adds a real scene that prose otherwise lacks. Keep `adjacent` material out of the body.

A true case can still fail this gate. Truthfulness is necessary; relevance is separate.

Default body budget for a compact judgment-led article:

- one personal scene or owned observation;
- one direct theory, book idea, study, or other endorsement item when the mechanism needs it;
- one screenshot/product-evidence group when conversion or system reality needs visible proof.

This is a default, not a quota. An article may use fewer. Add more only when each item proves a different indispensable step.

## 2. Historical Feedback Audit

Run this conditionally, not for every article. Trigger it when any of these is true:

- a similar article previously attracted factual or conceptual correction;
- the topic uses terms the audience has misunderstood or challenged before;
- the draft makes a strong technical, industry, trend, or product-mechanism claim;
- the user has a post-publication review, daily review, cognitive note, or later correction about the topic;
- the article updates an older position.

Retrieval path:

1. Search `content` for the closest earlier article, not every old article.
2. Read relevant comments, replies, or feedback attached to that article when available.
3. Follow only directly linked or clearly matching post-publication reviews, daily reviews, cognitive notes, or later corrections.
4. Record the original claim, the feedback, later evidence, and the correction that should survive in the new draft.

Classify feedback before turning it into a rule:

- `factual_error`: a verifiable fact was wrong or stale;
- `concept_boundary`: a term or causal claim was too broad, ambiguous, or used at the wrong layer;
- `value_disagreement`: the reader rejects the stance but has not disproved the fact;
- `pure_attack`: no checkable claim or useful reader confusion is present.

Verify `factual_error` and `concept_boundary` feedback before adopting it. Treat `value_disagreement` as reader-defense input, not an automatic correction. Do not convert `pure_attack` into a writing rule.

If the audit reveals a material error, return to source retrieval and rewrite the claim before drafting or finalizing.

## 3. Freshness and Professional-Boundary Gate

Classify every material claim as one of:

- personal practice or observation;
- technical fact or definition;
- current product capability, price, feature, policy, or platform behavior;
- theory or named author's view;
- inference from evidence;
- product promise.

Required treatment:

- Personal practice may be stated directly, but must not silently become an industry-wide fact.
- Technical definitions and current AI claims require current primary/official evidence when they affect the argument.
- Current product facts must be checked against live product or official sources.
- A theory should be attributed to its source and presented as a lens, not proof that the user's product works.
- An inference must be signaled as the writer's interpretation.
- A product promise must be no stronger than product records, delivery evidence, or user evidence support.

For AI, Agent, Skill, MCP, RAG, memory, autonomy, and similar terms, name the discussion layer when ambiguity matters:

- technical architecture;
- model or platform feature;
- the user's application workflow;
- the user's product/system design.

Do not call a prompt, fixed workflow, or Skill an autonomous Agent unless the described behavior actually supports that label. Prefer scoped wording such as `在我的系统里，我把这些面向具体场景的 AI 助手称为……` when the article is describing the user's application layer.

Do not repeatedly weaken the writer with `我不是技术专家`. State the practice boundary once when needed, then make the claim at the level the evidence supports.

## 4. Post-Draft Compression and Macro AI-Flavor Gate

After the first coherent draft, create a serious shorter version. For a judgment-led, pain-point, or light-conversion article, test a 30–40% reduction rather than only line-editing individual sentences.

Cut in this order:

1. adjacent cases and theories;
2. explanations already made visible by a screenshot;
3. a second paragraph that performs the same function as the first;
4. framework completeness added only to make the article look systematic;
5. section headings that merely label an obvious transition;
6. repeated product explanation after the reader already understands the mechanism.

Prefer the shorter version when it preserves:

- the central judgment and causal bridge;
- one real personal anchor;
- necessary evidence and truthfulness boundaries;
- the product bridge when conversion is intended;
- the intended emotional movement.

The 30–40% test is a comparison tool, not a mandatory deletion target. Do not amputate necessary proof to reach a number.

Reject macro-level AI flavor when the article feels assembled from a completeness checklist:

- every idea receives its own heading;
- personal story, user case, book, theory, method, and product all appear because the template has slots;
- transitions announce structure instead of carrying the reader's question forward;
- the draft reads like a course handout or exhaustive answer rather than a thought the writer actually arrived at;
- removing one entire section changes almost nothing about the conclusion.

A short article may have no internal headings. Evidence types are optional; the central judgment is not.

## 5. Evidence-Visual Substitution

When a real screenshot already demonstrates structure, workflow, usage, or product reality, let it carry that proof.

The surrounding text should tell the reader:

- what to look at;
- why it matters to the current claim;
- what the image cannot prove by itself.

Delete prose that merely inventories what is already visible. A decorative image cannot substitute for evidence.

## 6. Title-to-Body Loop

Identify the title's emotional conflict or promised judgment. It must reappear in:

1. the opening scene or question;
2. the mechanism or turning point in the body;
3. the ending decision, consequence, or invitation.

Do not mechanically repeat the title wording. The reader should feel that the body answered the tension the title created.

## Pass Criteria

The audit passes only when:

- every body case has a named role and no `adjacent` material remains;
- triggered historical feedback was checked and classified;
- current or technical claims are verified, scoped, weakened, or removed;
- the article has been compared with a meaningfully shorter version;
- headings and evidence types serve the argument rather than a completeness template;
- screenshots replace, rather than duplicate, suitable explanatory prose;
- the title's central conflict is resolved by the body and ending.

If any item fails, return to the smallest affected stage: retrieval for evidence/freshness failures, battle card for angle/relevance failures, or revision for compression/structure/visual duplication failures.
