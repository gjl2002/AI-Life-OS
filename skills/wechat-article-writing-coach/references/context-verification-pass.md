# Context Verification Pass

Run this after source retrieval and before the article battle card for every full article.

## Purpose

Treat cloud Notion, connectors, and web search as sampled retrieval, not complete knowledge.

The goal is not to make the agent "know everything". The goal is to make the retrieval plan, actual coverage, source basis, gaps, and uncertainty visible enough that the article only makes claims the searched context can support.

## Core Principle

Write inside the verified coverage area.

If the source coverage is narrow, ambiguous, or sampled, weaken the claim, add a source warning, or retrieve more evidence before drafting.

## Required Audit

Before drafting, create a compact working context map:

```markdown
上下文检索计划：
实际读取来源：
核心判断来源：
个人场景来源：
私域/产品证据来源：
公开/第三方支撑来源：
已发布内容差异化：
公开证据归属：
书籍背书：
证据覆盖范围：
未覆盖/可能遗漏：
冲突与不确定：
可放心写的部分：
需要弱化表达的部分：
是否需要补检索：
```

Do not include this full map in the final answer unless the user asks, a blocker occurs, or source uncertainty affects truthfulness.

## Verification Questions

Answer these in working notes:

1. Search plan: which Runtime concepts, cloud Notion sources, user-provided files, keywords, time windows, and source types were searched?
2. Actual coverage: what pages, files, database rows, screenshots, feedback records, benchmark articles, or web sources were actually read?
3. Claim-to-source map: what source supports the core judgment, selected personal scene, user pain, product bridge, and any public claim? For a study/person/interview/talk/workshop/book/report, record the named source, work/event, date/year when available, direct link, and whether the article presents a fact, an attributed view, or an inference.
4. Missing areas: what likely relevant source was not checked, unavailable, too thin, or only sampled?
5. Conflicts: did sources disagree on product wording, user pain, timeline, evidence strength, or conversion intensity?
6. Permission and minimization: did the article use only context needed for this task, and avoid exposing unnecessary private or named-product details?

## Claim Strength Rules

Use the strongest wording only when the searched context supports it.

- If multiple user-owned sources support a judgment, write confidently.
- If only one thin source supports it, write as an observation, not a universal conclusion.
- If evidence is public or third-party, label it as reference, not first-person truth.
- If retrieval only sampled a large source, avoid phrases like `我完整看过`, `所有资料都说明`, `系统里都证明了`.
- If the selected source is incomplete, retrieve more cloud Notion evidence or add a source warning.
- If no credible endorsement evidence supports the core judgment, return to retrieval or weaken the article's claim.
- If a public source is identifiable, give it a natural source anchor at first use, such as a publication, institution, book title, person, or program; include full author/speaker/work/date/link details in the final `参考资料`. Do not leave a claim with neither an in-text source anchor nor a traceable source note.
- For long-cycle human questions, record whether relevant user book materials were searched and, if a book is used, the exact idea and article claim it supports.
- If the draft overlaps with an existing published article, confirm that the new article has a distinct judgment, evidence, reader question, consequence, or clearly labeled sequel angle before continuing.

## Battle Card Fields

Add these fields to the article battle card:

```markdown
上下文检索计划：
实际读取来源：
核心判断来源：
已发布内容差异化：
公开证据归属：
书籍背书：
证据覆盖范围：
未覆盖/可能遗漏：
冲突与不确定：
可放心写的部分：
需要弱化表达的部分：
```

## Final Review Gate

Before title design, confirm:

- The context verification pass happened after retrieval.
- The article does not imply a broader source coverage than was actually checked.
- Unsupported or weakly supported claims were weakened.
- Missing, unavailable, or sampled sources that affect truthfulness are surfaced in the final source warning.
- External product naming and privacy treatment still pass after any source-derived details enter the article.
- Every material public claim is traceable to a named source, or has been rewritten as an observation/inference without fake specificity.
- The draft does not repackage an existing published article without a distinct contribution.

If any item fails, return to source retrieval, source labeling, claim weakening, or article revision before final output.
