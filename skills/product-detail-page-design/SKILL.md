---
name: product-detail-page-design
description: 为知识产品、数字产品、课程、咨询服务、模板和 AI 系统产品，设计高转化的多图商品详情页，默认使用高级数据科技风格。Use when the user needs sales-page conversion structure, product-detail-page copy, copy-only landing page mode, 课程销售页文案, 长销售页文案, 主标题/副标题, 转型故事, Offer介绍, 价值点方案付费理由, 新物种销售表达, AI产品不是旧产品加功能, 销售页转化雷达, fear/defense/trust/objection analysis, buyer pain, proof, CTA, or 多图商品详情页 design.
---

# Product Detail Page Design

Create a complete sales argument as a sequence of product-detail images, not a decorative poster or one unreadable long image. Turn product evidence into an editable multi-page set that moves from attention to understanding, desire, trust, and action. Default to the user's premium data-tech visual system unless a different campaign style is explicitly requested.

Also support copy-only landing page mode when the user asks for sales-page copy, course sales copy, landing-page text, or a long-form private-domain/Feishu/WeChat conversion page without visual production.

## Non-negotiable rules

- Treat reference pages as structural evidence unless the user explicitly asks to imitate their visual style.
- Default to multiple portrait images. Each image must communicate one main idea and perform one persuasion job.
- Keep a consistent delivery width, but let each image height follow its content. A taller image is preferable to cramped copy or tiny type.
- Do not compress the full sales page into one image. Do not deliver only one extra-long image.
- Compose the images as one ordered detail-page set with shared visual rules and varied page layouts.
- Do not copy another seller's wording, identity, visual assets, or unsupported claims.
- Never invent sales, student counts, testimonials, outcomes, prices, scarcity, guarantees, credentials, or bonuses.
- Mark missing commercial facts as `[待确认]`; do not silently fill gaps.
- Write outcomes as concrete user-owned results or deliverables, not vague feature lists.
- Keep the product's own central narrative. Do not replace the user's verified positioning with generic phrases such as “AI 员工” or “超级个体.”
- Do not use HTML/CSS by default. Unless the user explicitly asks for HTML, web components, editable source, or deterministic layout, produce finished raster images directly.
- For benchmark-driven hero pages, use visual-first raster production and add exact text afterward only when needed.
- Keep critical Chinese copy accurate. If generated text is wrong, repair it through a separate text/compositing layer instead of accepting garbled copy.
- In copy-only mode, do not force image generation. Deliver the conversion thesis, page structure, headline options, and final sales copy in Markdown.

## Load references

Read [sales-architecture.md](references/sales-architecture.md) before drafting the page.

Read [conversion-empathy-radar.md](references/conversion-empathy-radar.md) before defining the conversion thesis when user materials include objections, hesitation, testimonials, comments, consultation records, FAQs, avatar insights, or any strong emotional signal.

Read [naming-word-of-mouth.md](references/naming-word-of-mouth.md) when the page needs a product name, hero promise, memorable slogan, referral sentence, testimonial framing, or "what users will tell others" section.

Read [new-species-expression.md](references/new-species-expression.md) when the product uses AI, automation, community, IP, data, commerce, or another new element and the sales page must explain why this is not merely an old product plus a feature.

Read [production-contract.md](references/production-contract.md) before creating visual files or code.

Read [visual-production.md](references/visual-production.md) before choosing full-raster generation, image editing, or rare user-requested deterministic layout.

Read [page-layouts.md](references/page-layouts.md) before assigning content to individual images.

Read [design-principles.md](references/design-principles.md) before designing the image set.

Read [visual-direction.md](references/visual-direction.md) when the user has not supplied a complete brand or campaign direction.

## Workflow

### 1. Build the evidence brief

Inspect every supplied source: product notes, PDFs, screenshots, course outlines, templates, brand assets, testimonials, pricing, and FAQs.

Extract:

- product name and category
- name impression, callability, cultural asset, and likely word-of-mouth sentence
- old-product baseline, added new element, and whether the offer claims new-species logic
- target buyer and purchase context
- desired future state
- present pain and failed alternatives
- unique mechanism
- demand shape: result-oriented, process-oriented, or hybrid; and the matching delivery path
- concrete deliverables
- curriculum or implementation path
- creator authority and available proof
- buyer awareness level: whether the buyer knows the problem, solution category, product mechanism, and creator trust basis
- included rights and bonuses
- price, deadline, capacity, refund terms, and CTA
- brand constraints and output channel

Separate facts into:

- `confirmed`: directly supported by user material
- `inferred`: reasonable interpretation requiring careful language
- `missing`: cannot be claimed until the user supplies it

Ask only for missing facts that materially block the page. Otherwise proceed with `[待确认]` placeholders.

### 2. Define the conversion thesis

Use `conversion-empathy-radar.md` when buyer evidence contains fear, anxiety, defense, shame, frustration, anger, or a clear release moment. Translate these signals into page jobs before writing the thesis.

Write these four sentences before page copy:

1. The buyer wants to become or own: `...`
2. They are currently blocked because: `...`
3. The old approach fails because: `...`
4. This product works through: `...`
5. After a good experience, the buyer would tell a friend: `...`
6. The new element changes the product by: `...`

Reject a thesis that merely says “内容丰富,” “提高效率,” or lists tools.

### 3. Create the image-sequence blueprint

Use the 11-module architecture in `sales-architecture.md`. Merge modules only when the product is simple; preserve the persuasion order.

Map the modules to a default set of 7-11 images. Adjust both image count and individual image height when needed; never solve density by shrinking text.

For every image specify:

- image number and role in the sequence
- conversion job
- single main message
- headline
- key claim
- supporting evidence
- recommended visual form
- CTA or transition

Present the blueprint before or alongside implementation when the user is still shaping the offer. If the user says “执行,” build the artifact directly.

### 3B. Copy-only landing page mode

Use this mode when the user asks for `课程销售页文案`, `落地页文案`, `长销售页`, `销售页成稿`, or when the channel is private-domain chat, Feishu/Notion document, WeChat article bridge, or a text-first sales page.

Do not skip evidence discipline. Build the same evidence brief and conversion thesis first.

Deliver:

- `标题方案`: 3 headline options based on problem, transformation, time frame, or unique mechanism.
- `副标题方案`: 3 subtitle options that clarify audience, outcome, and mechanism.
- `导语`: name the buyer's current stuck state and failed alternatives without fake fear.
- `转型故事/产品由来`: use a real founder, user, or product-origin story only when supported; otherwise label as `[待补真实故事]`.
- `独特机制`: explain the actual system, workflow, feedback, template, AI agent, method, or service path.
- `Offer介绍`: describe deliverables as benefits, but keep concrete items visible.
- `适合/不适合人群`: reduce mismatch risk and buyer anxiety.
- `权益/赠品`: include only items that improve completion or reduce risk.
- `证明与风险降低`: use truthful proof, transparent presale terms, sample lesson, refund/exit rule, or `[待确认]`.
- `行动号召`: include price, next action, delivery status, and terms when known.

For low-awareness buyers, use a longer education-and-diagnosis page. For warm/high-awareness buyers, use a shorter page with clearer offer, proof, price, and CTA.

### Feedback iteration rule

When the user corrects a detail page, fix the current page set first, then judge whether the feedback should change future runs.

Classify feedback as:
- `one_time_preference`: this offer's visual direction, page count, CTA strength, or copy emphasis.
- `long_term_user_standard`: stable sales philosophy, public product wording, proof threshold, visual system, or forbidden claim style.
- `workflow_gap`: missing evidence brief, conversion thesis, emotion radar, naming/word-of-mouth check, new-species explanation, image-sequence blueprint, or production contract.
- `reference_gap`: missing offer facts, testimonial rules, product materials, buyer objections, benchmark page patterns, visual direction, or typography/layout rules.
- `quality_gate_gap`: repeated issues such as feature-list pages, unsupported claims, cramped copy, fake urgency, weak trust proof, too much generic AI language, or old-product-plus-feature expression.
- `script_or_template_gap`: a deterministic layout/claim check, image-set template, or copy QA tool would prevent recurring failures.

For durable feedback, update the smallest stable surface: SKILL.md for core workflow changes, references/ for sales/design rules, scripts/ for checks, or assets/ for reusable layouts. Do not turn every campaign-specific design taste into a permanent rule.

### 4. Write production copy

Write concise Chinese suited to mobile image scanning. Every page set must make three things legible before asking for purchase:

- **价值点**: what problem is resolved and what change the user can see;
- **方案**: the actual course, SOP, tool, template, service, or feedback path that creates the change;
- **付费理由**: why this specific delivery is worth paying for, using truthful proof and comparison rather than inflated claims.

Then follow these rules:

- one dominant claim per image
- headline first, explanation second
- short paragraphs and high-information bullets
- desire plus obstacle for audience descriptions
- phase results plus deliverables for curriculum
- evidence beside claims
- truthful, explicit CTA

Avoid empty urgency, exaggerated multipliers, generic AI slogans, fabricated proof, and long unbroken prose. If the offer is presale or still being built, state that delivery status and terms plainly.

### 5. Design the image set

Choose the output by context:

- Default: finished numbered PNG/JPG images produced through visual-first raster generation or image editing.
- Hybrid: generate cinematic/key-art backgrounds and system visuals first, then add exact copy through a separate text layer only when needed to repair text.
- Deterministic layout: use HTML/CSS, SVG, Canvas, Figma, or slides only when the user explicitly requests HTML, editable source, web components, or fully deterministic text layout.
- Marketplace/social detail page: export numbered portrait PNG/JPG images in reading order.
- Web product page: create production-ready responsive components in the user's existing stack.
- Copy-only request: deliver Markdown blueprint and final copy without forcing a visual artifact.

Use a repeated design system: delivery width, safe margins, typography scale, spacing scale, card rules, color tokens, image treatment, footer/page-number system, and section rhythm. Let image heights vary by content while keeping the set recognizably unified.

Use the supplied PDFs as layout references:

- one idea per portrait page
- strong oversized headline
- clear vertical hierarchy
- diagrams, cards, timelines, or bundle stacks chosen by message
- enough breathing room to understand the page without zooming

Do not automatically imitate their black/red styling, metallic typography, or space imagery.

### Built-in design specialists

This skill is self-contained. It already includes the core principles needed for:

- commercial-poster hierarchy, focal point, safe zones, and campaign-series consistency
- Chinese marketing readability, mobile scanning, template discipline, and social-commerce export thinking
- editorial headline hierarchy, deliberate information rhythm, grid discipline, and typographic contrast

Use [design-principles.md](references/design-principles.md) as the source of truth for these principles. Do not require users to install external companion skills for normal use.

For normal use, image generation should create the whole commercial composition. If text accuracy is unreliable, repair or composite exact Chinese text afterward rather than switching the whole page to HTML/CSS.

### 6. Create supporting visuals

Use diagrams for mechanisms, system blueprints, curricula, and bundle maps. Use generated imagery sparingly for atmosphere or conceptual anchors.

When generating an image:

- omit all critical copy from the image
- reserve predictable negative space
- keep one visual purpose per asset
- match the active page design system
- save project-bound assets inside the project

### 7. Generate and inspect

Generate every image and inspect the complete ordered set. Check:

- image 1 names the product and outcome immediately
- the page establishes need before curriculum and price
- each image is understandable on its own but naturally leads to the next
- no image contains two competing central messages
- every claim has evidence or cautious wording
- text is readable at normal mobile viewing size
- no clipping, overflow, tiny type, or awkward gaps
- images feel like one narrative rather than unrelated posters
- CTA, price, terms, and next action are unambiguous
- all Chinese text is correct in the final image; if not, repair it before delivery

Iterate on the weakest conversion break, not merely surface decoration.

## Required deliverables

Unless the user narrows scope, provide:

1. evidence brief with missing facts
2. conversion thesis
3. numbered image-sequence blueprint
4. final page copy
5. numbered PNG/JPG image set
6. contact sheet showing the complete sequence when producing multiple images
7. prompts/art direction or revision notes when useful
8. short list of unresolved commercial facts

For copy-only mode, provide:

1. evidence brief with missing facts
2. conversion thesis
3. headline and subtitle options
4. final long-form sales copy
5. CTA and terms
6. unresolved commercial facts and risky claims

## Definition of done

The result is done only when a buyer can answer:

- What is this?
- Is it for me?
- Why did my previous approach fail?
- What is the new mechanism?
- Why should I trust this offer?
- What will I own or be able to do afterward?
- What happens during the program?
- What exactly is included?
- What does it cost and what should I do next?
