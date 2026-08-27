# Full Article Runbook

Use this as the execution contract for full WeChat article creation.

The goal is a publishable final draft, not a good outline or an article that still needs an editor to find missing bridges, weak evidence, hard-sell CTAs, or unsafe product naming.

## Canonical 23-Step Runbook

This is the only canonical execution order. `SKILL.md` provides routing and invariants; `writing-method.md` explains how to carry out these steps without defining another sequence.

1. Accept the user's topic, sentence, story, product point, outline, draft, or Notion page.
2. Classify the primary article type and name the structure that should not be used.
3. Collect only missing high-impact intent: reader, stance, emotion, scene, evidence, and conversion intensity.
4. Build the required source checklist from `source-retrieval.md`.
5. Run `article-source-preflight.md`, confirm Runtime status, and resolve the required concepts.
6. Read current `commercial_positioning`, then search `content` for overlap and complete the published-content differentiation gate.
7. Retrieve personal, reader, commercial, knowledge, and benchmark evidence using the layered reading budget in `source-retrieval.md`; expand only when a later audit identifies a specific gap.
8. Build the material preflight pool.
9. Run `context-verification-pass.md` and map claims to the sources actually read.
10. Run `material-sufficiency-audit.md`; repair every hard missing/weak row through its exact source route, then repeat steps 7–10 until the hard gate passes.
11. Run the pre-draft half of `editorial-claim-audit.md`: remove merely adjacent materials, classify freshness/claim boundaries, and conditionally inspect the closest historical article, relevant comments, and later review.
12. Run `content-empathy-radar.md` when reader emotion, defense, comments, feedback, or conversion affects the angle, then build the article battle card with material, differentiation, attribution, context, sufficiency, relevance, historical-feedback, and empathy decisions.
13. When the run uses benchmark hit articles or requests 爆款大纲重构 / 深度二创, run `benchmark-outline-reconstruction.md`; otherwise skip this conditional module.
14. Select the article structure from `article-structure-library.md`.
15. Build the temporary style card from `style_corpus` using `source-retrieval.md`; explicit user instructions override corpus patterns.
16. Draft the complete article inside verified source and privacy boundaries.
17. Run `evidence-visual-pass.md` when real system, product, workflow, feedback, delivery, or commercial proof may need visual evidence.
18. Revise paragraph function, rhythm, and style-card fit with `rhythm-revision.md`.
19. Run the mandatory `reader-flow-pass.md` and repair progression before review.
20. Run `concise-writing-standard.md`, the post-draft half of `editorial-claim-audit.md`, the Voice and AI-Flavor Gate, `ai-flavor-concreteness-gate.md`, and any required return loop. Compare the coherent draft with a meaningfully compressed version; prefer the shorter version when truth, logic, personal evidence, and the intended product bridge survive.
21. Save the draft as Markdown when possible, run `scripts/article_quality_check.py --markdown <draft.md>`, repair every blocking failure, and investigate source/body-length warnings.
22. Design titles with `title-design.md`, run `emphasis-formatting-pass.md` on the stable body, then output the article, title package, visual notes when used, light conversion path when useful, concise sources, and truthfulness-relevant warnings.
23. Only when requested: hand the completed article to `$xiaohongshu-native-note-coach`, or follow `writeback_fields.md` to perform authorized Notion writeback and readback verification.

## Material Preflight Pool

Before drafting, create this working pool:

```markdown
候选个人场景：
候选私域/用户证据：
候选产品/交付证据：
候选书籍/书中观点：
候选知识模型：
候选高质量内容/深度文章：
候选公开/第三方背书：
候选爆款结构：
候选业务配图：
历史相关文章/评论/后续复盘：
相似已发布/在写内容：
新文章独有判断：
复用边界：
采用素材：
不采用素材及原因：
案例与核心主张映射：
时效/术语边界：
仍缺素材：
材料充分性审查：通过 / 条件通过 / 不通过
待补缺口及检索路由：
```

Selection rules:

- Choose one primary personal scene or user-owned observation by default.
- Choose one credible endorsement evidence item for the core judgment.
- For long-cycle human questions such as learning, agency, self-knowledge, decision-making, habits, attention, creativity, values, or life direction, search the user's book materials before using generic web thought-leadership. Select no more than one primary book unless comparing books is the article's purpose.
- Choose no more than 2-3 supporting materials unless the article type requires more.
- Treat the pool as candidates, not body slots. Remove a case, book, theory, or study that is true but does not directly support a sentence or causal step in this article.
- Use benchmark articles for structure and rhythm, not as factual evidence.
- Use real business visuals only when they support trust or conversion inside the reading path.
- If a required material is missing, decide whether to ask, retrieve more, weaken the claim, or continue with a warning.
- Do not turn the preceding rule into a drafting shortcut: run `material-sufficiency-audit.md` and repair every hard missing/weak row before building the battle card. A warning is allowed only for a non-hard gap that has already been reflected in weaker article wording.
- A repeated topic needs a distinct article contribution before drafting; a new title alone is not a contribution.
- When using public evidence, keep the author/speaker, work/event, date/year when available, direct link, and the claim it supports. The final source note must name specific sources instead of only saying `研究显示` or `公开研究`.
- In the body, use a natural source anchor such as a publication, institution, book title, person, or program; keep full bibliographic identity for the final `参考资料`. Do not make a公众号 paragraph read like an author-year citation.

## Source Preflight Contract

Before substantive cloud retrieval, keep this working summary:

```markdown
来源预检：
- Runtime status:
- required concepts:
- resolved targets:
- user-named sources:
- cloud-verified sources:
- unavailable sources:
- blocking_failures:
- non_blocking_failures:
```

Follow `article-source-preflight.md`. Its `blocking_failures` stop final output until repaired. Its `non_blocking_failures` go into context verification when they affect truthfulness.

## Failure Decision Table

| Condition | Blocks final output? | Required action |
| --- | --- | --- |
| Core topic or stance is unclear | Yes | Ask a concise follow-up. |
| User-requested personal story cannot be verified | Yes for first-person story | Ask for the real scene or remove first-person story claims. |
| Personal-path scan finds no usable public scene | No | Continue only with a source warning and no invented scene. |
| Core judgment has no credible endorsement evidence | Yes for strong claim | Retrieve more support or weaken the claim. |
| New draft substantially repeats an existing article without a distinct contribution | Yes | Change the angle, add genuinely new evidence, or label it as a sequel/update. |
| Public claim uses vague or unverifiable attribution | Yes for factual certainty | Identify and cite the named source, rewrite as an observation, or remove it. |
| Context verification was skipped | Yes | Run `context-verification-pass.md` before drafting or finalizing. |
| Material-sufficiency audit has a hard missing or weak row | Yes for drafting | Return to its specified source route, retrieve the missing material, and re-run the audit. If it cannot be repaired, weaken/remove the claim or ask only for user-owned information that cannot be retrieved. |
| A selected case is true but only adjacent to the central claim | Yes for that material | Remove it from the body or replace it with direct support; do not keep it to make the article look complete. |
| Historical feedback trigger fires but relevant correction history was not checked | Yes for the affected claim | Search the closest old article and relevant feedback/review, classify the correction, then verify or rescope the claim. |
| A current AI/product fact or technical term is stale, unverified, or used across layers | Yes for factual certainty | Verify with a current primary/official source, name the discussion layer, or weaken/remove the claim. |
| A mechanism-heavy article has no credible explanation of why the proposed method works | Yes for drafting | Retrieve one focused book, deep article, original research, or clearly framed user observation; do not fill the gap with generic `研究显示`. |
| Source coverage is sampled or incomplete | No by itself | Weaken claims and disclose only when it affects truthfulness. |
| Reader-flow pass fails | Yes | Repair progression before title design. |
| The coherent draft has not been tested against a meaningfully shorter version | Yes for finalization | Run the compression comparison and keep the shorter version when the argument survives. |
| The final emphasis pass was skipped | Yes for publishable formatting | Run `emphasis-formatting-pass.md`; remove decorative slogan bolding, then keep only emphasis that reveals the article's actual argument path. Zero bold placements is allowed when justified. |
| Live commercial naming gate fails | Yes | Re-read current positioning/product evidence and align naming with the authorized campaign boundary. |
| Business visual placeholders exist without matching notes | Yes | Add matching capture notes or remove placeholders. |
| CTA is hard-sell, fear-based, or suddenly product-heavy | Yes | Rewrite from the current reader problem and live commercial boundary as a light diagnosis, low-pressure reply path, or truthful category-level bridge. |
| Public factual/current claim needs verification but web/source access is unavailable | Yes for factual certainty | Verify, remove, or weaken the claim. |
| Article source preflight returns `blocking_failures` | Yes | Resolve cloud source, ask user, or remove the unsupported claim/material. |
| Notion writeback schema cannot be verified | Yes for writeback | Stop before writing and report the dependency. |
| Article quality script returns `blocking_failures` | Yes | Fix and re-run the script. |

## Script Quality Gate

When a full draft exists, run:

```bash
python3 scripts/article_quality_check.py --markdown <draft.md>
```

The script checks structural completeness and common hard failures. It does not replace human/editorial judgment. If it passes, still run the reader-flow, source, title, and AI-flavor review gates.

## Final Output Contract

Normal final output should include:

- Recommended title.
- 2-3 backup titles.
- Complete article.
- Final emphasis already applied in the article body; do not append a separate list of manufactured gold sentences unless the user asks.
- Business-evidence visual notes when placeholders were used.
- Light conversion path when commercially relevant.
- Concise source note and source warnings when needed.

Do not include the full execution log unless the user asks or source uncertainty changes the truthfulness of the result.
