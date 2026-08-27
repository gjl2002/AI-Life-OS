# Concise Writing Standard

Use this after drafting and before final output.

## Core Standard

The article is not a net that catches everything. It is a knife that leaves the sharpest judgment and cuts through the issue.

Do not prove depth by length. Prove depth by judgment density.

## Review Rules

1. Each paragraph must add one new function:
   - new judgment
   - new scene
   - new turn
   - new explanation
   - new evidence
   - new emotion

2. Each judgment gets only the strongest scene. Do not stack similar examples.

3. Repeat core judgment if useful, but do not repeat the same explanation.

4. Do not turn opinion articles into course notes. If a framework appears, each point needs one sharp angle, not a full definition.

5. The ending must elevate, not summarize.

6. Product bridges must grow from the unresolved problem. Do not suddenly introduce a product.

7. Compression comparison: after the first coherent draft, test a 30–40% shorter version for judgment-led, pain-point, and light-conversion articles. Prefer it when the central judgment, causal bridge, personal anchor, necessary evidence, and product bridge survive. This is a comparison tool, not a mechanical deletion target.

8. Material preflight gate: read `full-article-runbook.md` and confirm a material preflight pool was built before drafting. The final article should be based on selected materials, not everything retrieved. If the pool lacks a personal scene, endorsement evidence, product proof, or visual proof needed by the article's claim, retrieve more, weaken the claim, or surface a warning.

9. Context verification gate: read `context-verification-pass.md` and confirm the article stays inside the verified source coverage area. The article must not imply complete Notion, connector, workspace, or personal-system coverage when only sampled retrieval happened. Unsupported, stale, or thinly supported claims must be weakened, supplemented, or surfaced as source warnings.

10. Evidence-visual gate: if the article would benefit from real business proof, read `evidence-visual-pass.md` and insert business-evidence visual placeholders inside the article body, such as `【图 1：创作大脑真实截图】`. Do not recommend cover images, golden sentence images, or decorative flowcharts by default. Every inserted placeholder must have a matching final visual note with position, source material, privacy treatment, and article function.

11. Existing-outline gate: if the input included an existing outline, Notion page outline, or partial draft structure, confirm the article did not merely expand it. The final article must independently pass task classification, required retrieval, material preflight, context verification, battle card, structure selection, personal-scene integration, endorsement evidence, evidence-visual decision when relevant, paragraph revision, reader-flow review, AI-flavor review, script quality check when possible, and title truth checks.

12. Reader-flow gate: read `reader-flow-pass.md` and confirm the article has forward motion. Each paragraph must answer a distinct reader question or raise the next one; the following paragraph must catch that question; major lens shifts must explain why the article moves from A to B; adjacent paragraphs must not merely restate the same judgment in different words. If this fails, return to paragraph revision before title design.

13. Live commercial naming gate: read current `commercial_positioning` and relevant `product` records, then align article body, title package, CTA, image copy, and visual notes with the user's authorized promotion boundary. Do not use a fixed banned name or fixed replacement category. If this fails, revise the outward-facing copy before final output.

14. Personal-scene integration gate: unless the user forbids personal material or no usable public scene exists, the article must include at least one verified personal scene or user-owned observation. It can be compact, but it must be visible in the reader-facing draft, not only in working notes.

15. Endorsement evidence gate: the core judgment needs at least one credible support. Accept user-owned scene/result, private-domain feedback, product evidence, high-quality/deep internal article, clearly labeled third-party case, public data/trend, authoritative viewpoint, or expert/author/book-backed idea. Do not count benchmark structure, generic model definitions, or invented scenes as endorsement evidence. If no credible support exists, weaken the claim and surface a short source warning.

16. Script quality gate: when the final draft exists as Markdown, run `scripts/article_quality_check.py --markdown <draft.md>` before final output or writeback. Fix `blocking_failures`; use warnings as prompts for manual review.

17. Title truth gate: final title options must come from the article's actual claim, reader pain, personal scene, evidence, and product intensity. Do not use named authorities, numbers, years, income figures, or hard factual claims unless the article supports them. Do not copy benchmark titles directly.

18. AI-flavor source gate: resolve and read `style_corpus` for positive voice signals, then `ai_flavor_library` for live `必删 / 慎用 / 可保留` guidance. Apply `$humanizer-zh`, then run `ai-flavor-concreteness-gate.md`. A `可保留` phrase is an allowed rhetorical form, not blanket approval: it still fails without a visible scene, action, object, reader situation, or traceable article evidence. If either Notion source is unavailable, record the fallback, surface a short warning, and do not claim account-specific去AI味. Default checks:
   - Does the writing sound like a course handout?
   - Is it correct but bloodless?
   - Are there too many balanced, average-length sentences?
   - Does it use empty terms such as 赋能, 闭环, 抓手, 底层逻辑 without concrete translation?
   - Does it explain too much and judge too little?
   - Would a reader know what physically happened, who did what, or what exact choice changed? If not, rewrite or delete the sentence.

19. Editorial claim gate: run `editorial-claim-audit.md`. Every case in the body must support an exact sentence or causal step; merely related material stays out. Trigger historical-feedback review when required, verify current technical/product claims, state the terminology layer, and ensure the title's conflict returns in the opening, mechanism, and ending.

20. Macro AI-flavor gate: reject completeness-by-template. A compact article does not need separate slots for a personal story, user case, book, theory, method, and product. Remove headings that only label obvious transitions, sections whose deletion changes nothing, and explanation already proven by a screenshot.

## Length Guidance

| Article type | Suggested length |
|---|---|
| Strong-judgment opinion | 1200-1600 Chinese characters |
| Pain-point teardown | 1500-1800 Chinese characters |
| Trend judgment | 1600-2200 Chinese characters |
| Method list | 1500-2200 Chinese characters |
| Product conversion | 1800-2500 Chinese characters |
| Personal story | Fit the story, usually 1200-2000 Chinese characters |

## Final Reminder

Use this sentence as the standard:

> We are not explaining all the material. We are compressing confusion into one clear judgment.
