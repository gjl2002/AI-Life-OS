# Core Angle Selection

## Purpose

Choose the one angle the current images and evidence can support best before writing titles or body copy. This gate prevents a polished note from being built on a weak, repetitive, or visually unsupported premise.

Run it only after any classification changes caused by source retrieval have been applied.

It does not change execution modes or add a user-facing approval step by default.

## When To Run

- **Quick mode**: lock the obvious angle in one sentence. Generate alternatives only when the material supports several substantially different interpretations.
- **Enhanced mode**: compare 2-3 credible angles before drafting.
- **Strict mode**: compare 2-3 evidence-backed angles and reject any angle whose promise exceeds verified proof.
- **Campaign mode**: first select the role of each note in the sequence, then run this gate for every individual note to prevent overlap.

## Candidate Rule

Generate only credible candidates from the selected material. Each candidate must state:

```markdown
候选角度：
给读者的一句话价值：
主要图片/证据：
与商业定位的连接：
与过往内容的差异：
最大风险：
```

Do not create artificial variants that differ only in wording. Candidates should represent meaningfully different reader entry points, judgments, or proof structures.

## Selection Criteria

Choose using these five criteria, in this order:

1. **图片与证据支持度**：Can the supplied image and verified source actually support the promise?
2. **商业定位一致性**：Does it reinforce the current audience, belief, differentiation, or product bridge?
3. **内容新贡献**：Does it add a new scene, judgment, evidence, or reader use instead of repainting an old note?
4. **读者价值**：Will the reader receive recognition, a useful judgment, a method, proof, or a decision aid?
5. **转化自然度**：If a CTA exists, does it grow naturally from the shown problem and evidence?

Evidence support is a hard gate. A commercially attractive angle cannot win when the images and sources do not support it.

## Reject An Angle When

- the cover cannot carry the title promise;
- the result, customer, product, or milestone claim lacks verified user-owned evidence;
- it repeats a past note without a new contribution;
- it requires inventing a scene, emotion, quote, or causal conclusion;
- it depends mainly on abstract concepts rather than the current image or scene;
- the CTA becomes the real subject before trust is earned;
- it mixes several topics that should become separate notes.

## Lock The Angle

Before drafting, record internally:

```markdown
最终角度：这篇笔记只讲……
核心承诺：读者看完会得到……
关键证据：……
主动放弃：这篇不展开……
```

Both default draft variants must express the same selected angle and evidence boundary. Version A and Version B may differ in tone, depth, rhythm, or opening, but must not become two different notes.

Include angle candidates or scoring in the user-facing answer only when the user asks to compare directions or when no candidate can be selected safely without their choice.
