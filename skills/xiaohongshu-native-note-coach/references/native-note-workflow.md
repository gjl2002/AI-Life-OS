# Native Note Workflow

## Core Theory

Xiaohongshu native image-text notes are public-domain trust assets.

Use four principles:

1. Public trust chain: strangers judge image first, title second, proof third, usefulness fourth, and conversion last.
2. Image evidence: images prove lifestyle, process, product, feedback, result, milestone, or story context; they are not decoration.
3. Native note narrative: build around one scene and one useful judgment. Do not compress a whole WeChat article or copy WeChat Moments.
4. Positioning constraint: read and apply the current Runtime-resolved commercial positioning instead of embedding a fixed positioning in the Skill.

## Workflow

1. Diagnose input.
   - Identify available images, missing context, and whether the note is image-led.
   - Identify whether the user wants writing, review, polishing, repurposing, batch planning, or writeback.

2. Clarify intent when needed.
   - Ask only for missing details that affect truth or conversion.
   - Do not ask if the user already supplied image meaning, scene, target reader, and CTA.

3. Select execution mode.
   - Quick, enhanced, strict, or campaign.
   - Preserve the exact mode triggers and depth defined in `SKILL.md`.

4. Resolve the cloud foundation.
   - Check `$ai-life-system-init` Runtime status.
   - Resolve `commercial_positioning` and `content`.
   - Read the current commercial positioning before deciding the final note angle.

5. Classify image evidence.
   - Decide what each image proves.
   - Pick cover, supporting images, proof/conversion image, and images to omit.
   - Record privacy, cropping, internal-name, and publicability risks.

6. Classify note task.
   - Single note, polish, repurpose, review, batch plan, pinned note, campaign, or writeback.

7. Classify note type.
   - Use `note-type-library.md`.

8. Identify public trust role.
   - 认识我: first impression and identity.
   - 理解我: worldview and values.
   - 相信我: proof, process, result, or milestone.
   - 想靠近我: resonance, comments, private chat.
   - 想购买: product, class, consultation, or campaign conversion.

9. Identify first-impression emotion when it affects title, cover, opening, image order, product mention, milestone/result claim, or CTA.
   - Use `note-empathy-radar.md`.
   - Decide whether the note enters through 焦虑, 不爽, 爽, 羞耻, 防御, 愤怒, or a lighter 愉悦/recognition signal.
   - Check whether title and cover protect trust rather than creating shame or unsupported fear.

10. Retrieve the conditional source bundle.
   - Use the note-type route in `native-note-sources.md`.
   - Resolve only concepts that can change the angle or factual accuracy.
   - Keep a private execution log of searched sources, selected materials, and missing evidence.
   - For enhanced, strict, and campaign notes, search past Xiaohongshu content and record the new contribution before locking the angle.
   - For public research, interviews, cases, or books, keep a private claim-to-source record; do not turn it into a bibliography by default.

11. Reassess classification after retrieval.
   - Check whether new evidence changes the note type, target reader, public trust role, first-impression emotion, or evidence boundary.
   - If it does, update the classification and conditional source bundle before choosing the angle.
   - Do not preserve an early classification merely for workflow consistency.

12. Select the core angle.
   - Use `core-angle-selection.md` before drafting.
   - Quick mode may lock one obvious angle directly; compare candidates only when the material is ambiguous.
   - Enhanced, strict, and campaign mode compare 2-3 credible candidates and select one.
   - Lock a one-sentence statement of what this note alone will prove or explain.

13. Build battle card.
   - Required for enhanced, strict, campaign, and claim-heavy notes.
   - Optional one-line diagnosis for quick notes.

14. Run visual-context verification.
   - Required for enhanced, strict, campaign, and any note with result/product/customer/milestone claims.
   - Verify that title, cover, images, body, proof, and CTA describe the same reality.
   - Verify that external evidence supports the note but does not substitute for user-owned visual evidence.

15. Draft outputs.
   - Give image order advice.
   - Give 5 titles.
   - Draft two versions by default.
   - Add tags, comment cue, private-message cue if appropriate, and Moments reuse advice.

16. Review and revise.
   - Use `review-standard.md`.
   - Resolve and apply `ai_flavor_library`, then apply `$humanizer-zh`.
   - Run deterministic quality check when feasible, especially before final output or writeback.
   - Rewrite drafts that fail evidence, AI-flavor, native-note, or milestone checks.

17. Write back only on explicit request.
   - Resolve `content`, check the live schema, run Runtime `check-write`, write, and read back using `writeback-fields.md`.

## Battle Card

Use this format internally; include it in the final only when useful or requested.

```markdown
笔记任务：
笔记类型：
执行模式：
公域信任角色：
目标读者：
读者痛点/欲望：
首屏情绪入口：
标题/封面防御风险：
图片证据：
候选角度：
最终角度：
选择理由：
相似过往笔记：
本条新贡献：
公开/书籍来源：
来源与证据状态：
图文一致性：
核心判断：
真实材料：
产品/服务出现方式：
CTA：
标题方向：
正文结构：
最大风险：
修正策略：
```

## Public And Book Source Rule

Use external sources to sharpen a judgment, not to make an image-led note feel academic.

- Keep claim, source, author/speaker or organization, date/context, link/identifier, and fact/view/inference status in the working record.
- In the note, use a natural source anchor; do not default to author lists, DOIs, or reference blocks.
- If the external source is the main proof, use a readable source card in a supporting/final image or a pinned comment. Do not pretend a decorative image is evidence.
- For learning, attention, creativity, decision-making, identity, and other long-cycle topics, prefer relevant book records when available. Limit one note to one book and one concrete idea, then return to the user's scene or image.

## Default Final Format

```markdown
图片排序建议：

标题备选：
1.
2.
3.
4.
5.

正文方案 A：

正文方案 B：

标签：

评论区引导：

朋友圈复用建议：

发布检查：
```
