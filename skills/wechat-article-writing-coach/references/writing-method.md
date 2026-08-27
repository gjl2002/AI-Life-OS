# Writing Method

## Operating Principle

Act as a 公众号总编, not just a drafter. Convert one sentence, a topic, or a draft into a publishable article through the full-article runbook, task classification, evidence routing, material preflight, context verification, structure selection, drafting, optional business-evidence visual insertion, paragraph revision, reader-flow review, live commercial naming review, script quality check, title design, and review.

Do not try to include everything. The article's value is to compress confusion into a clear judgment.

Default to strict execution. Do not skip steps for speed unless the user explicitly asks for quick mode.

For full article creation, read `full-article-runbook.md` first and treat it as the execution contract.

## Execution Log Requirement

Maintain a working execution log while producing a full article. Each major step must leave evidence:

```markdown
步骤：
Runtime 概念：
解析目标：
云端 Notion 检索：
联网检索：
找到：
选用：
未找到/未使用：
下一步：
```

Resolve stable sources through `$ai-life-system-init`, then query cloud Notion. If a source is user-pinned or run-specific, fetch it directly by its live link/title. If cloud Notion is unavailable, mark the source as unavailable instead of pretending it was checked.

Do not show the full execution log by default. The final response should include only:
- the article
- a concise source summary
- any missing/uncertain source warnings that affect truthfulness

Show the full step-by-step log only when the user asks for it, a source fails in a way that changes the result, or a writeback/verification step needs explicit confirmation.

Do not draft before the article battle card exists.

## Runbook Procedures

The following sections explain how to perform the modules in `full-article-runbook.md`. They do not define a second execution order. When numbering or wording differs, the canonical 23-step runbook wins.

### Step 0: Accept Input

The input may be:
- one sentence
- a topic
- a rough intention
- a personal story
- a product point
- an existing draft
- an existing outline
- a Notion page or database row that already contains a title, outline, evidence notes, or partial draft

If the user provides a draft, enter revision mode after checking the article task. Do not rewrite the full article before diagnosing paragraph functions.

If the user provides an outline or a Notion page with an outline, enter outline-audit mode first. The outline is source material, not a completed workflow. Do not skip classification, missing-information check, required source retrieval, article battle card, structure selection, drafting, evidence-visual decision when relevant, paragraph revision, reader-flow pass, review, or title design.

### Step 1: Classify Article Task

Read `article-structure-library.md` and choose one primary type:
- strong-judgment opinion
- pain-point teardown
- trend judgment
- personal story
- method list
- product conversion

Name the primary type and optional secondary type. Also name what structure should not be used.

If an outline already exists, classify the article independently from that outline. Then decide whether the existing outline should be kept, partially repaired, or replaced. Never assume the outline's structure is correct merely because it exists in Notion.

### Step 2: Check Missing Information

Collect only missing high-impact items:
- core topic or idea
- writing purpose
- stance/value judgment
- target reader and pain points
- main emotion
- personal story/scene
- desired product/conversion intensity
- concepts, cases, data, or sources the user wants included

If enough is known, do not ask a full questionnaire.

For an existing outline, explicitly identify:
- usable angle
- unsupported claim
- missing reader pain
- missing personal scene
- missing endorsement evidence
- missing product bridge
- repeated or weak section
- whether the outline matches the selected article type

### Step 3: Retrieve Sources

Follow `article-source-preflight.md` and `source-retrieval.md`. Decide the required Runtime concepts first, resolve them, then read the current records from cloud Notion. Use web search only for public cases, current facts, trend data, authoritative support, expert/author ideas, book-backed concepts, public talks/interviews, or public intellectual references.

When a Notion page, database row, or Markdown file already contains an outline, treat it as a required named source for this run. Read it fully and extract:
- current title or title candidates
- current outline
- existing claims
- existing sources or evidence
- unresolved gaps
- parts to preserve
- parts to discard

Then continue the full required retrieval checklist. The existence of an outline never satisfies the personal-path gate, endorsement gate, benchmark step, reader-flow pass, AI-flavor review, or title design step by itself.

Personal-path retrieval is mandatory for full articles, including strong-judgment opinion articles. Search:
- `personal_story`
- `life_moment`
- `life_journey`
- relevant cloud Notion review, goal, or project sources only when the topic requires them

Do not invent a first-person scene. If no suitable public scene is found, record that and write the article without pretending a story exists.

Personal-scene integration is mandatory by default. Select 1-2 candidate scenes and decide exactly where one scene will enter the article: opening hook, user's real observation, turning point, method example, or product origin. Do not leave personal material only in working notes. If no scene is usable, mark that in the battle card and final source note.

Endorsement evidence is mandatory for full articles. Before drafting, select at least one credible support for the core judgment. Prefer user-owned evidence; if it is not enough, search high-quality content / deep articles, then the people-list route for expert or book-backed ideas, then web sources for public cases, data, trends, or authoritative viewpoints.

Separate sources into:
- `用户本人经历`
- `用户/私域证据`
- `第三方案例`
- `知识模型`
- `对标内容`
- `高质量内容`
- `联网/公开资料补充`
- `联网/公开思想补充`

For full articles, search the user's internal high-quality content / deep-article source before open web search. Search the people-list database when the article may benefit from expert, author, book-backed, or public-thought references.

### Step 3.5: Build Material Preflight Pool

Use `full-article-runbook.md` to create a working material pool before the battle card:
- candidate personal scenes
- candidate private-domain/user evidence
- candidate product/delivery evidence
- candidate knowledge models
- candidate high-quality/deep internal content
- candidate public/third-party support
- candidate benchmark structures
- candidate business visuals
- selected materials
- unused materials and reasons
- still-missing materials

Do not draft until the selected personal scene, core endorsement evidence, and material gaps have been decided or explicitly marked unavailable.

### Step 3.6: Verify Context Coverage

Read `context-verification-pass.md` after retrieval and before the article battle card.

Create a compact working context map:
- retrieval plan
- actual sources read
- claim-to-source support for the core judgment, personal scene, user pain, product bridge, and public claims
- missing, stale, unavailable, or sampled sources
- conflicts and uncertainty
- claims that can be written confidently
- claims that need weaker wording or more retrieval

Do not let the article imply that the user's full Notion, inbox, Drive, or personal system was completely read when only sampled retrieval happened. Write inside the verified coverage area.

### Step 3.7: Audit Claims, Cases, and Prior Corrections

Read `editorial-claim-audit.md` before the battle card.

- Map each candidate case, book, theory, study, and screenshot to the exact sentence or causal step it supports.
- Remove `adjacent` material from the proposed body even when it is true or interesting.
- Classify current/technical/product claims and mark what needs live verification or narrower wording.
- When triggered, inspect the closest old article, relevant comments/feedback, and directly related later review; verify factual or concept-boundary corrections before adopting them.
- Record the title's intended emotional conflict so the draft can close the same loop.

### Step 4: Build Article Battle Card

When reader emotion, private-domain feedback, comments, product conversion, or the user's requested emotion affects the angle, read `content-empathy-radar.md` before finalizing the battle card. Decide the reader emotion entry, article entry angle, defense risk, and conversion bridge.

Before drafting, create a working battle card. Show it to the user when the material choice or angle could change the article.

```markdown
文章类型：
输入状态：一句话 / 选题 / 已有大纲 / Notion页面 / 草稿
已有大纲诊断：保留 / 修复 / 重做；原因：
目标读者：
核心痛点：
核心冲突：
核心判断：
主情绪：
读者情绪入口：
防御风险：
共鸣切入方式：
我的真实素材：
候选素材池：
采用素材：
不采用素材及原因：
案例与核心主张映射：
仍缺素材：
候选个人场景：
入文个人场景：
个人场景位置：开头 / 中段观察 / 转折 / 方法例子 / 产品起源 / 不使用及原因
用户/私域证据：
第三方案例：
知识模型：
外部数据/趋势：
外部思想/权威观点：
高质量内容/人物来源：
核心背书证据：
历史反馈触发：是 / 否
查过的旧文章/评论/后续复盘：
需要继承的修正：
主张类型与时效：
术语使用层级：
上下文检索计划：
实际读取来源：
核心判断来源：
证据覆盖范围：
未覆盖/可能遗漏：
冲突与不确定：
可放心写的部分：
需要弱化表达的部分：
个人路径检索结果：
文风语料库状态：
去AI味库状态：
临时文风卡：
爆款结构参考：
产品承接方式：
风险点：
```

### Step 5: Select Structure

Use the selected article type's structure from `article-structure-library.md`. Do not force every article into the same template.

If an existing outline was provided, compare it against the selected structure. Keep only sections that serve the selected article type and verified core judgment. Delete or rewrite outline sections that repeat, over-explain, lack evidence, or point to the wrong reader.

For strong-judgment opinion articles, the default chain is:

```text
strong judgment
-> concrete phenomenon
-> first problem drilldown
-> user's real observation
-> optional external proof
-> core judgment elevation
-> one small action
-> light product bridge
-> closing echo
```

### Step 6: Draft

Draft from the temporary style card built from the selected `style_corpus`, current `commercial_positioning`, relevant `user_profile` evidence, and the user's explicit instructions. The explicit request wins when these sources differ.

The style card must state the intended first-person distance, sentence and paragraph rhythm, story density, judgment intensity, opening pattern, transition pattern, ending pattern, supported vocabulary, and expressions to avoid. Do not import a fixed audience, creator style, or permanent word list from this Skill.

Use first person only for verified user-owned experience.

Use at least one verified personal scene or user-owned observation by default. It can be compact, but it must appear in the reader-facing draft unless the user forbids personal material or no usable public scene exists.

### Step 7: Paragraph Revision

Before paragraph revision, read `evidence-visual-pass.md` when the article mentions the user's real system, product, workflow, Notion/personal-system setup, private-domain evidence, user feedback, service delivery, or commercial proof.

Decide whether business-evidence visuals are needed:
- If not needed, keep the article text-only and do not add decorative images.
- If needed, insert 1-3 inline placeholders inside the article body at the exact moment they support, such as `【图 1：创作大脑真实截图】`.
- Each placeholder must later have a matching `业务证据配图建议` note after the article.
- Prefer real screenshots and real business materials. Use conceptual visuals only when real evidence is unavailable.

Evidence visuals are part of the reading path. Do not put all visual suggestions only at the end without inline placeholders in the article.

Read `rhythm-revision.md` and revise paragraph by paragraph:
- identify each paragraph's function
- remove repeated information, repeated judgment, and repeated function
- make each paragraph's conclusion become the next paragraph's question
- translate abstract concepts into lived language
- keep product bridges short and naturally grown from the unresolved problem

### Step 8: Reader Flow Pass

Read `reader-flow-pass.md` and run the mandatory reader-flow pass before final review:
- identify what question each paragraph answers
- identify what question the reader naturally asks next
- confirm the next paragraph catches that question
- mark whether the paragraph creates progression, turn, explanation, example, scene shift, framework shift, or conclusion
- merge, cut, move, or rewrite paragraphs that explain the same judgment without a new question, scene, contrast, evidence, or action
- add bridges only when they explain why the article moves from A to B

The article must not move to title design while it still feels like separate correct paragraphs instead of one continuous reading path.

### Step 9: Final Review

Read `concise-writing-standard.md` and review:
- Confirm the context verification pass happened. If it did not, return to source retrieval before final output.
- Confirm the article does not imply broader context coverage than was actually checked. If it does, weaken the claim, add a source warning, or retrieve more support.
- Voice source gate: resolve `style_corpus`, select relevant user-authored examples through the layered reading budget, build the temporary style card, and compare the draft against that card before negative cleanup.
- AI-flavor source gate: resolve `ai_flavor_library` and apply its live `必删 / 慎用 / 可保留` guidance; then apply `$humanizer-zh` and `ai-flavor-concreteness-gate.md`.
- If either Notion review source was not read, mark it in the working log and include a short final warning. Do not claim account-specific去AI味.
- Confirm personal-path retrieval happened. If it did not, return to source retrieval before final output.
- If the input included an outline or Notion page outline, confirm the workflow did not merely expand that outline. The final article must pass all required gates independently.
- Confirm the reader-flow pass happened. If it did not, return to paragraph revision before final output.
- Confirm both halves of `editorial-claim-audit.md` happened: selected material is directly relevant, triggered historical feedback was checked, freshness/terminology boundaries are explicit, screenshots do not duplicate prose, and the title conflict is answered by the body.
- Confirm the live commercial naming gate passed: article body, title package, CTA, image copy, and visual notes must match current `commercial_positioning`, relevant `product` records, and the user's authorized promotion boundary.
- Confirm the selected personal scene or user-owned observation appears in the article unless the user forbids personal material or no usable public scene exists.
- Confirm at least one credible endorsement evidence item supports the core judgment. If not, return to source retrieval; if no credible source exists, weaken unsupported claims and include a short final source warning.
- Does every paragraph add new judgment, scene, turn, information, or emotion?
- Has the coherent draft been compared with a 30–40% shorter version where appropriate, and was the shorter version preferred when the argument survived?
- Does each judgment use only the strongest scene?
- Is the ending elevated rather than a summary?
- Is any third-party or web material mislabeled as personal experience?
- Is product conversion natural?
- Is product/category naming appropriate for the article's conversion intensity?

If a full draft is saved as Markdown, run `scripts/article_quality_check.py --markdown <draft.md>` before final output or Notion writeback. If the script returns `blocking_failures`, repair the draft and run it again. Treat warnings as editorial prompts, not automatic blockers.

If it fails, return to the exact weak step: source retrieval, material preflight, context verification, editorial claim audit, structure selection, drafting, paragraph revision, reader-flow repair, live commercial naming repair, product bridge, or script quality repair.

### Step 10: Title Design

Read `title-design.md` after the draft passes review. Use real benchmark title samples as structure references, not wording to copy.

Before generating titles, extract:
- core judgment
- reader identity
- strongest pain
- counterintuitive point
- personal scene or user-owned observation
- endorsement evidence or authority source
- product/conversion intensity

Generate 8-10 titles covering at least 3 angles:
- pain resonance
- counterintuitive trap
- reader identity
- authority/thought source
- personal transformation
- golden judgment
- method promise

Select:
- one recommended title
- 2-3 backup titles
- title directions not recommended because they exaggerate, attract the wrong reader, or are unsupported by the article

Do not use a named person, institution, number, year, income figure, or strong factual claim in a title unless it appears in the article or source notes. Do not copy benchmark titles directly.

### Step 11: Final Output

Output:
- recommended title
- 2-3 alternate titles
- optional larger title pool with strategy analysis when useful
- short summary/opening hook if useful
- complete article
- CTA or private-domain bridge if requested or appropriate
- source note listing source labels and benchmark structures used
- short source warning when context coverage is sampled, incomplete, or materially narrower than a claim might imply
- short source warning when a required source, personal-path scan, selected personal scene, `style_corpus`, or `ai_flavor_library` could not be read or used
- short source warning when the article's core judgment lacks credible endorsement evidence

Do not over-explain the writing unless the user asks.

### Step 12: Optional Xiaohongshu Handoff

Run only when the user asks to adapt the finished WeChat article to Xiaohongshu. Hand the completed article, selected sources, truthfulness boundaries, and promotion intensity to `$xiaohongshu-native-note-coach`. Do not duplicate that platform's workflow inside this Skill.
