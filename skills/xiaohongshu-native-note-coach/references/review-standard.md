# Review Standard

Use this after drafting and before final output. Review is a gate loop, not a decorative publishing checklist.

## Mandatory Gate Loop

Run these five gates on every draft. If any gate fails, do not present the draft as final. Return to the weak step, rewrite, and check again.

Enhanced, strict, and campaign mode must also pass `visual-context-verification.md`. Strict and campaign mode should run `scripts/native_note_quality_check.py` when feasible before final delivery or writeback.

### Gate 1: Positioning Consistency

Compare the draft with the live Runtime-resolved `commercial_positioning` page. Do not use a positioning statement embedded in this Skill.

Pass standard:

- The note serves the current audience, promise, differentiation, and public identity.
- The note uses a confirmed public product name or safe category wording.
- Product/system details support the current positioning instead of becoming a detached feature list.
- The reader can understand why the scene, evidence, or judgment matters.

Fail signs:

- The note drifts into a generic tool tutorial, template pitch, productivity slogan, or product manual.
- It sells features before establishing scene, belief, proof, or reader relevance.
- The voice or promise conflicts with the current commercial-positioning page.

If it fails, return to commercial positioning, note type, public trust role, or core judgment.

### Gate 2: AI-Flavor

Use three layers in this order:

1. Apply the Xiaohongshu-native checks below.
2. Resolve `ai_flavor_library` through `$ai-life-system-init` Runtime. Search the live cloud database for patterns relevant to the current title, opening, body, CTA, and product wording. Read selected records before claiming this layer was applied.
3. Apply `$humanizer-zh` as a general second pass for LLM writing patterns.

Do not use a fixed database ID, page URL, local mirror, personal path, or hardcoded library title as the lookup mechanism.

If `ai_flavor_library` is `not_found` or unreadable, continue with the platform-native checks and `$humanizer-zh`. For enhanced, strict, campaign, or important notes, disclose that the dedicated library layer was unavailable. Never claim it was applied when it was not read.

Platform-native checks:

- Does the writing sound like a course handout?
- Is it correct but bloodless?
- Are there too many balanced, average-length sentences?
- Does it use empty terms such as 赋能, 闭环, 抓手, 底层逻辑, 认知升级, 长期主义, or 系统化 without concrete translation?
- Does it explain too much and judge too little?
- Does it contain a real scene, image, action, object, or quote in the first third?

Rewrite when the draft has repeated “本质上/核心是/真正的,” generic motivation, parallel slogans, fake personal tone, vague attribution, stiff summaries, promotional overclaiming, or claims larger than the evidence.

Preserve truthful native devices: strong hooks, short lines, image references, tags, comment cues, and direct reader address.

### Gate 3: Conversion Pressure

Check whether the note asks for a comment, follow, private message, purchase, or enrollment before earning trust.

Pass standard:

- CTA matches the trust role and note type.
- Private-message cue is light, specific, and natural.
- Product mention grows from the unresolved reader problem or shown evidence.

Fail signs:

- The first half feels like an ad.
- The CTA appears before the reader receives value.
- The CTA uses unsupported pressure, scarcity, or result promises.

If it fails, reduce CTA intensity, move it later, or switch to a comment/private-chat cue.

### Gate 4: Result Promise

Check every claim about results, user count, income, transformation, productivity, clarity, system effects, or product outcomes.

Pass standard:

- Every result or milestone is supported by user-provided material or verified user-owned cloud evidence.
- Unsupported broad claims become a scoped observation, hypothesis, or invitation.
- Milestone expression includes context, process, value, or lesson.

Fail signs:

- Broad transformation language has no scope or evidence.
- Public or benchmark outcomes are written as user-owned results.
- Product promises are stronger than the verified proof.

If it fails, verify, weaken, contextualize, or remove the claim.

### Gate 5: Visual Context

Check whether title, cover, image sequence, body, proof, and CTA describe the same reality.

Pass standard:

- The cover supports the title promise.
- Each important claim traces to an image, source, or user-provided context.
- Decorative images are not written as proof.
- Public/book claims have a confirmed source record; when central, use a concise source image or pinned-comment detail instead of a bibliography.
- Private details and unapproved internal names are blurred, cropped, generalized, or omitted.

Fail signs:

- The title promises a result the images do not show.
- Customer/result/milestone wording rests on an ambiguous screenshot.
- Product, price, deadline, quota, or keyword is not current.
- External evidence is presented as proof of the user's own result.
- An image exposes private data or an unapproved internal name.

If it fails, change the cover/title/body, weaken claims, add context, blur/crop/omit images, or retrieve/ask for stronger proof.

## Supporting Checks

After the gates pass, check:

- independent Xiaohongshu readability;
- clear public trust role;
- concrete scene or image-led object;
- clear core judgment;
- useful method, lesson, or resonance;
- no copied benchmark wording;
- no third-party result presented as user-owned;
- no unapproved internal name exposed;
- no conclusion introduced from outside the selected material without labeling it.

## Xiaohongshu Native Fit

The note should enter from an image, scene, result, or conflict; focus on one cut; read naturally on a phone; earn any CTA; keep paragraphs short; and add tags only after the value is complete.

## Milestone Expression Check

Milestone notes are allowed and encouraged when true.

Check whether the milestone is real, evidence/context exists, its importance is clear, process or lesson is shown, the reader receives something useful, and the note returns to current positioning instead of generic bragging.

Use:

```text
result
-> context
-> process
-> lesson
-> reader relevance
```

## Public Trust Risk

Reduce fake-lifestyle feeling, unsupported results, early hard selling, mentor-from-above tone, and self-praise without reader value.

Keep pride in real progress, honest uncertainty, process detail, specific evidence, and “this may help you” energy.

## Final Publishing Check

```markdown
发布检查：
- 原生小红书感：
- 图片证据：
- 真实/可验证：
- 读者收益：
- 里程碑表达：
- 产品承接：
- AI 味风险：
- 图文一致性：
- 外部命名风险：
```

Fix all deterministic blocking failures before presenting the draft as final. Address warnings when they affect public trust, proof, conversion, or native platform feel.
