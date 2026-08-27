# Moments Review Standard

## Mandatory Gate

Every draft must pass an AI-flavor gate before final output.

Apply the current account's positive style evidence before the negative AI-flavor filter. Preserve earned personal judgment, concrete contrast, metaphor, emotional texture, and a natural closing line. Do not flatten the copy into generic casual prose.

Enhanced, strict, and campaign mode must also pass the context verification gate from `moments-context-verification.md`. Strict and campaign mode should run `scripts/moments_quality_check.py` when feasible before final delivery or writeback.

Risk levels:
- **Low**: sounds like a real朋友圈 note; concrete, specific, and not over-explained.
- **Medium**: usable idea but has template phrases, abstract language, or公众号 rhythm; rewrite before final in enhanced/strict/campaign mode.
- **High**: generic, polished, slogan-like, over-complete, or not tied to a real scene/proof; reject and rebuild from source material.

Mode requirements:
- Quick mode: silently fix obvious AI-flavor issues before output.
- Enhanced mode: internally rate every draft; only present low-risk drafts as final versions. If showing a source summary, mention major revisions only when helpful.
- Strict mode: do not deliver a final draft until the selected version is low risk.
- Campaign mode: run the gate on each post; rewrite any medium/high-risk post before delivering the sequence.

Gate scorecard:

| Check | Pass condition | Failure signal |
|---|---|---|
| Real detail | Has scene, action, dialogue, feedback, product fact, or sensory detail | Only abstract point of view |
|朋友圈语感 | Reads like a warm private-domain post | Reads like公众号 paragraph, essay, or lesson |
| 段落节奏 | Related sentences stay together as semantic paragraphs; isolated lines are rare and intentional | Every sentence is separated into a caption-like paragraph |
| Personal口吻 | Sounds like the user's lived observation | Sounds like generic content account |
| Non-repetition | Each sentence adds a new function | Same meaning repeated in different words |
| Anti-template | No common AI transitions or grand summaries | "在这个时代", "真正重要的是", "归根结底", "不是...而是..." overuse |
| Human imperfection | Keeps uncertainty, texture, or concrete limitation when true | Over-perfect, over-certain, teacher-like |
| Source truth | Credibility-bearing claims are sourced, user-provided, or weakened | First-person/customer/product/price/deadline claims with no source |
| Public/book source fit | Public claims have a natural source anchor and a traceable working record; a book supports rather than replaces the post | Vague `研究显示`, decorative book title, or bibliography-like朋友圈 |
| External naming | Uses a current verified public product name or truthful category wording | Exposes an unverified internal, ambiguous, or stale name |
| Light conversion | CTA feels like a natural invitation | Fear-based, urgent, or manipulative sales pressure |

If a draft fails, revise by adding or restoring concrete material, shortening explanations, breaking公众号 rhythm, replacing slogans with scenes, and removing repeated abstract claims.

## Core Standard

The post should sound like a real person with a real context, not a polished generic copywriter.

Check:
- Is there a concrete scene, detail, action, feedback, or product fact?
- Does each sentence do a different job?
- Do paragraphs carry complete thought units instead of breaking after every sentence?
- Is the rhythm suitable for朋友圈, not公众号?
- Does the post match its trust-chain role?
- If selling, is there proof and a clear next action?
- If personal, is the emotion earned by detail rather than declared?

## AI-Flavor Checks

Revise or reject when the draft:
- uses generic transitions like "在这个时代", "真正重要的是", "归根结底".
- overuses contrast templates like "不是 X，而是 Y" without a lived scene.
- piles up abstract nouns without a scene.
- sounds like a lecture to strangers rather than a note to warm contacts.
- repeats the same meaning in several sentences.
- overuses slogans, empty motivation, or big conclusions.
- makes the user look artificially perfect.
- explains the structure of the post inside the post.
- uses blank lines after nearly every sentence and reads like short-video subtitles.
- tries to be complete instead of memorable.
- has no sentence that could only have come from this user's context.
- cites a public source in a way that interrupts the private-domain rhythm or relies on a book title without a concrete idea.

## Rewrite Rules

When AI-flavor risk is medium or high:
1. Identify the specific risk: empty abstraction,公众号 rhythm, fake completeness, repeated meaning, weak scene, weak proof, or generic CTA.
2. Return to the battle card or source material.
3. Replace at least one abstract claim with a concrete scene, quote, action, product fact, or customer detail.
4. Cut any sentence that only summarizes, moralizes, or repeats.
5. Merge adjacent one-sentence paragraphs when they belong to the same scene, example, or inference.
6. Re-run the gate.

Do not solve AI flavor by adding more adjectives, emoji, slang, or forced casualness.

## Private-Domain Fit

朋友圈 is not only content; it is relationship memory.

A good post should do at least one:
- make the user more visible as a person.
- make the user's value easier to remember.
- make a reader feel understood.
- make a product/service feel more trustworthy.
- invite a natural next step.

## Sales Review

For 营销卖货, verify:
- The target reader is specific.
- The pain or desire is concrete.
- The product promise is accurate.
- Proof is real and sourced.
- Scarcity is not fabricated.
- CTA is natural and unambiguous.
- The tone does not feel desperate or manipulative.

Default CTA should be a light next step: comment cue, private chat, checklist, diagnosis, or "适合的人我再详细介绍". Use direct报名 only when the post is explicitly a launch/sales post and product facts are verified.

## Life/Persona Review

For 人设生活, verify:
- The post contains a real image, action, place, or sensory detail.
- The reflection is small enough to feel true.
- It does not become motivational filler.
- It shows state, taste, values, or growth without overexplaining.

## Professional Value Review

For 专业价值, verify:
- The example or process is specific.
- The conclusion is not a generic tip.
- The user appears capable through action and judgment.
- It can stand alone even without a CTA.

## Final Output Format

When delivering drafts, prefer:

```markdown
判断：...

朋友圈正文
...

发布建议：
- 配图：
- 时间：
- CTA：
- 复用：
```

正文 must use semantic paragraphing informed by the current account's own published examples when available; do not format the whole post as one sentence per paragraph.

For strict mode, include a short source summary. Do not dump the full retrieval log unless asked or source uncertainty matters.

For enhanced, strict, and campaign mode, keep the AI-flavor risk rating in working notes. Surface it only when the user asks, when a draft had to be significantly rewritten, or when a source gap prevents a low-risk post.

If the deterministic quality gate reports blocking failures, fix them before presenting the draft as final. Warnings should be handled when they affect trust, conversion, or朋友圈语感.
