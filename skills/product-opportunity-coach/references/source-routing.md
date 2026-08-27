# Cloud Source Routing

Use this before retrieving Notion context. The goal is to read the smallest evidence set that can change the opportunity decision.

## Runtime Contract

Use `$ai-life-system-init` as the only structural foundation.

1. Run Runtime `status`.
2. Resolve only the concepts required for this opportunity.
3. Fetch the resolved cloud Notion object and confirm its live identity.
4. For `multiple`, filter by the opportunity object and current business context; ask only if ambiguity remains material.
5. For `not_found`, search/fetch an exact user-provided title or URL when available; otherwise record the source as unavailable.

Do not use local Notion Sync, Markdown mirrors, separate database indexes, fixed IDs, URLs, or personal paths.

## Source Priority

1. User-provided product idea, page, title, URL, draft offer, evidence, or explicit decision question.
2. Current `commercial_positioning` ordinary page.
3. Relevant `product` record, if one exists.
4. Direct demand and user evidence.
5. Substitute/market evidence and delivery-capacity evidence as needed.
6. Current web verification only when the decision depends on present-day market, competitor, price, policy, platform, or trend facts.

## Stable Concept Routes

| Decision need | Runtime concepts | Use |
| --- | --- | --- |
| Business boundary | `commercial_positioning` | current audience, value, public language, product boundary, commercial direction |
| Product state | `product` | existing offer, state, promise, form, price, delivery, linked evidence |
| User definition | `user_profile` | target-user hypotheses, goals, purchase context, behavior |
| Direct demand | `user_feedback`, `client_communication` | user language, objections, requests, outcomes, payment and service signals when recorded |
| Content-market signal | `content`, `account` | repeated questions, response, conversion intent, channel fit; metrics count only when actually recorded |
| Substitutes and competitors | `benchmark_product`, `benchmark_content`, `benchmark_account` | current alternatives, price/form patterns, positioning, entry path, market language |
| Delivery capacity | `project`, `task`, `weekly_review`, `twelve_week_review` | current workload, execution limits, repeated delivery evidence, constraints |
| Knowledge or trend context | user-named sources; `information` when actually mapped | mechanisms, trend signals, relevant research or records |

Concept resolution is not a command to read every database. Relation means candidate relevance, not mandatory full-text reading.

## Layered Reading Budget

Use four layers:

1. **Resolve:** confirm target identity, kind, read readiness, and live cloud object.
2. **Screen:** query titles, dates, statuses, summaries, relation labels, and relevant fields. Start with a narrow candidate set, usually up to about 10 per relevant source.
3. **Read deeply:** fetch only the records most likely to change the decision—typically 2–5 direct user signals, 1–3 product/delivery records, and 1–3 substitute records.
4. **Expand deliberately:** widen retrieval only when a named evidence gap, conflict, current factual claim, or explicit user request requires it.

These are defaults, not hard caps. Mandatory decision gates still must be satisfied or reported as missing.

## Evidence Coverage Map

Keep this working map:

```markdown
机会对象：
本次决策：
用户提供信息：
商业定位：
产品现状：
直接需求证据：
首批用户证据：
触发场景证据：
替代方案/竞品证据：
可见胜出理由证据：
交付能力证据：
已验证证据：
合理推断：
待验证假设：
冲突与过期信息：
未读取/不可用来源：
需要弱化的判断：
```

## Missing Data Rules

- No product record: evaluate it as a new idea; do not block the run.
- No direct user evidence: demand is unproven; cap the decision at `先验证`.
- No first user or trigger scene: do not output `值得做` or `调整后做`.
- No substitute evidence: do not claim market whitespace or a proven win path.
- No delivery evidence: recommend a conservative test such as content, interview, manual service, prototype, or transparent presale.
- Conflicting records: preserve the conflict and prefer current cloud identity/status; do not average contradictions away.
- Current market claims without current internal or web evidence: label them `待验证假设`.

## Current Web Research

Browse when the user asks for, or the decision depends on, current competitors, prices, market size, platform rules, product availability, public company facts, or trend timing. Prefer primary sources and official product pages for technical and commercial facts.

Public research supplements the user's evidence; it does not turn market interest into proof that this user's audience will buy.

## Writeback Boundary

Source retrieval never implies permission to write. If the user explicitly asks to save or update the judgment, hand off to `writeback-safety.md` after the analysis is final.
