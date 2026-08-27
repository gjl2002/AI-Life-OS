# Cloud Source Routing

Use this reference before retrieving product and user evidence. The goal is to design from the user's current system without scanning every database or relying on local mirrors.

## Source Priority

1. User-supplied product page, Notion URL, document, transcript, screenshot, or explicit context.
2. Target `product` record.
3. `commercial_positioning` for public category, promise, audience, and product-family boundaries.
4. First-party user evidence from `user_profile`, `user_feedback`, and `client_communication`.
5. Conditional sources selected by mode.

## Mode Routing

| Mode | Read first | Read only when useful |
| --- | --- | --- |
| Experience Design | `product`, `commercial_positioning`, `user_profile`, `user_feedback` | `client_communication`, `content`, `benchmark_product`, capacity sources |
| Experience Diagnosis | `product`, `user_feedback`, `client_communication` | `user_profile`, `content`, `benchmark_product`, capacity sources |
| Onboarding And Activation | `product`, `user_profile`, `client_communication` | `user_feedback`, `content`, `benchmark_product` |
| Retention And Return | `product`, `user_feedback`, `client_communication` | `user_profile`, capacity sources, `benchmark_product` |
| Naming And Word Of Mouth | `product`, `commercial_positioning`, `user_feedback` | `user_profile`, `client_communication`, `content`, `benchmark_product` |

Capacity sources are `goal`, `project`, `weekly_review`, `twelve_week_review`, and `year_review`. Read only records that reveal current delivery resources, workload, bottlenecks, or sustainable service boundaries.

## Retrieval Rules

- Use `$ai-life-system-init` runtime to resolve concepts; do not copy database IDs into this skill.
- Cloud Notion page bodies and current records are the content authority.
- Relations are candidates, not mandatory full-text reads.
- Inspect title, description, summary, date, product/user relation, and record type before fetching a page body.
- Prefer recent and object-specific evidence over large generic archives.
- Search by product name, first-user identity, arrival scene, desired result, objection, drop-off language, and service stage.
- User-supplied local files are valid explicit inputs, but this skill must not assume any local folder, sync tree, or database index exists.
- Public web research is separate and should be used only when the user asks for external benchmarks or current market facts.

## Evidence Coverage Note

Keep this working note for formal runs:

```markdown
体验对象:
运行模式:
用户直接提供:
已解析并读取:
抽样读取:
未找到/不可用:
第一只羊证据:
用户反馈与原话:
对标证据:
交付能力证据:
相互冲突的记录:
需要弱化的判断:
```

Do not imply full-database coverage when only selected records were read.

## Evidence Levels

- `已验证证据`: direct product record, user statement, observed behavior, actual feedback, service record, or verified operating constraint.
- `合理推断`: a cross-source interpretation supported by more than one relevant signal.
- `待验证假设`: plausible experience claim without enough first-party evidence.

AI synthesis is not automatically user evidence. Label it as inference.

## Missing Data Rules

- No target product record: treat it as a new product and state that product-state evidence is missing.
- No first-user evidence: do not assert exact motives, emotions, or behavior; return a hypothesis map.
- No feedback or communication evidence: do not claim objections, drop-off causes, delight moments, or return reasons are proven.
- No capacity evidence: keep service and human-feedback recommendations conservative.
- Conflicting historical and current records: describe the change or conflict; prefer the current live record for current-state claims.
- Empty or unreadable sources are evidence gaps, not evidence that the product experience is good or bad.

## Notion Boundary

All retrieval is read-only. This skill does not create, update, archive, or append to Notion pages.
