# Source Retrieval and Synthesis / 信息读取与融合

Use this reference when a user wants the coach to read their cloud Notion system, source courses, articles, records, prompts, templates, or practice history before creating a course draft.

## Principle

The workflow is not:

```text
write from the prompt → add a few examples
```

It is:

```text
confirm course skeleton
→ turn each lesson into a set of teaching questions and required evidence
→ retrieve the user's materials by role
→ read the actual pages/files, not only titles or database fields
→ deconstruct and combine mechanisms into original teaching units
→ draft from the synthesis ledger
```

Do not mechanically read every database or every relation. Start with the current course object and user-supplied material, then resolve only sources that can substantively support a missing claim, learner scene, method, example, asset, boundary, or feedback rule.

## Phase A — Turn the Skeleton into Retrieval Questions

For every lesson that actually needs additional retrieval, create an internal `取材任务卡` before searching:

| Lesson part | Retrieval question | Material role needed | Expected output |
| --- | --- | --- | --- |
| Core judgment | What mechanism makes this claim true or useful? | external lens / user's judgment | causal explanation |
| Learner scene | How do real people describe this friction? | user language / consultation / content | opening scene and old frame |
| Method | What sequence or decision rule works in practice? | course note / SOP / practice record | reusable path |
| Example | What has actually happened or been demonstrated? | personal practice / case | bounded proof or demo |
| Asset | What can the learner create and use next? | Agent / SOP / template / system page | worksheet, prompt, or page |
| Boundary | When should the method not be applied or be simplified? | practice / reflection / counterexample | non-example and repair rule |

No fixed source count applies. The test is whether each important teaching job has credible material; missing material is visible rather than fabricated.

## Phase B — Build the Runtime Source Packet

1. **Course contract**: user-supplied outline/draft, Runtime `course`, and `product` when needed.
2. **Commercial boundary**: `commercial_positioning` only when the audience, promise, or external framing depends on it.
3. **Knowledge and mechanisms**: relevant `note`, `information`, `question`, `book`, `course`, or a user-named transcript/source.
4. **Real evidence**: the specific project, review, personal record, case, or user-provided material that supports the teaching claim.
5. **Learner language and product evidence**: `user_profile`, `user_feedback`, `content`, or the current customer source when available and relevant.
6. **Executable assets**: `sop`; resolve the real source name `Agent` when needed, plus user-supplied templates, prompts, system pages, or tools.

An ordinary handout can use only the sources that matter. Record hit/miss across all routed roles only for full-course, evidence-sensitive, or explicitly audited work.

## Phase C — Search and Read Protocol

1. Build queries from the lesson title, core judgment, target-user wording, desired asset, method keywords, product name, and known related tools.
2. Resolve each source through the current `$ai-life-system-init` Runtime. Read the live schema or ordinary-page structure, then search cloud Notion using the current title, summary, relation, status, or relevant property semantics.
3. Fetch/read promising records deeply enough to evaluate their actual mechanism, example, and boundary. A title, tag, property, or search snippet is not evidence.
4. Follow relevant relations and linked source pages when the record names an Agent, SOP, case, course transcript, or template that will become the student's asset.
5. Record both `命中` and `未命中`. If no user language or valid case exists, label the gap and use only a clearly marked hypothetical example.

## Phase D — Create the Synthesis Ledger

For each selected source, make an internal ledger entry:

| Source | Exact useful unit | Source role | Deconstruction | Migration / combination | Boundary |
| --- | --- | --- | --- | --- | --- |
| a course transcript / article | mechanism, decision rule, structure | external lens | what problem, causal chain, sequence, and feedback it uses | rewrite in this course's first principle and learner context | mechanism only; no copied proprietary expression |
| personal record / reflection | a real scene, choice, failure, or repair | real practice | what changed and why | turn into case, contrast, or boundary | do not generalize one person's result |
| user question / content | the learner's own wording | user language | unstated fear or old model | use in opening, examples, and task copy | anonymize when needed |
| Agent / SOP / template | runnable artifact | execution | required inputs, steps, output, self-check | simplify into the student-facing asset | do not expose sensitive system details |

## Phase E — Synthesize, Do Not Collage

Apply both methods deliberately:

```text
拆迁法 = 拆解 + 迁移
收租法 = 收集 + 组合
```

- **拆解 + 迁移**: take a useful mechanism from a course or article, then express it through the user's own course promise, examples, terminology, tasks, and boundary.
- **收集 + 组合**: combine a user scene, external mechanism, personal case, and runnable asset into one teaching unit rather than listing them separately.

A valid teaching unit normally has this shape:

```text
learner scene
→ old interpretation
→ causal mechanism
→ new judgment
→ method / decision rule
→ case or demonstration
→ learner asset and feedback signal
```

## Phase F — Draft Only From Accounted Material

Before drafting, check that every major statement is one of:

- `用户观点` — the user's own stated judgment;
- `实践证据` — a real, bounded user practice/case;
- `外部机制` — a rewritten, internalized idea from a named source;
- `待验证假设` — useful but not yet evidenced; phrase cautiously or leave out.

The final outward-facing handout does not need to expose every source. Keep a compact internal material pack and synthesis ledger when multiple sources materially shape the lesson; surface it only when the user asks, a source gap remains, or auditability matters.

## Phase G — Put the Mechanism Where It Teaches

Do not turn a source ledger into a learner-facing `理论背书` chapter. For every selected external mechanism, decide:

| Teaching node | What the learner is currently misunderstanding | Mechanism to make visible | Appropriate expression |
| --- | --- | --- | --- |
| old-path diagnosis | why their familiar move repeatedly fails | causal condition or missing link | `问题不在……，而在于……` |
| core judgment | what must be true for the new path to work | first principle | one memorable causal sentence |
| method explanation | why the steps are in this order | process or decision rule | a map, contrast, or worked example |
| demonstration | why this input produces a more relevant result | system mechanism | before/after or live test |
| boundary | when not to apply the method | constraint or counterexample | `这不等于……；当……时应当……` |

The learner should feel the mechanism making the explanation more precise, not feel that the instructor paused to display authorities. A named origin can be used sparingly after the explanation, for example: `认知科学把这种现象称为……`.
