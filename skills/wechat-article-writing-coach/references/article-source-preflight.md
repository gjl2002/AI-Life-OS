# Article Source Preflight

Run this before any cloud Notion retrieval for a full article. It preserves the source-preflight step while using `$ai-life-system-init` as the only structural foundation.

## Runtime Contract

1. From the `$ai-life-system-init` root, run `python3 scripts/runtime.py status`.
2. If status is `needs_init`, stop Notion retrieval and ask the user to initialize or rebind. Do not fall back to fixed IDs, local Notion Sync, or a copied database list.
3. Resolve each required concept with `python3 scripts/runtime.py resolve --concept <key>`.
4. `ready`: record the unique target and continue only if `read_ready: true`.
5. `multiple`: filter using the current article object and user context; if that still changes truthfulness, ask the user.
6. `not_found`: search cloud Notion by the user-provided title or link when one exists. Otherwise record the source as unavailable; absence from the index is not proof that the template lacks the capability.
7. Fetch the resolved cloud object before querying its records and confirm its title/Data Source identity matches the Runtime target.

## Stable Concepts

Resolve only the concepts required for the current article:

- always: `commercial_positioning`, `content`, `personal_story`, `life_moment`, `life_journey`, `benchmark_content`, `style_corpus`, `ai_flavor_library`
- reader and commercial evidence when relevant: `user_profile`, `user_feedback`, `client_communication`, `product`, `account`
- knowledge support when relevant: `note`, `information`, `book`, `question`

Relation means “possibly relevant”, not “read every related page”. Inspect titles, properties, summaries, and dates first; fetch only records likely to change the current article.

## Working Summary

```markdown
来源预检：
- Runtime 状态：
- 必需概念：
- 已唯一解析：
- 需要消歧：
- 用户指定来源：
- 云端已核实：
- 不可用来源：
- blocking_failures：
- non_blocking_failures：
```

Blocking failures stop drafting when they affect a required first-person scene, core positioning, duplicate detection, account-specific style review, or a strong factual claim. A non-blocking failure must still narrow claims or produce a short source warning.

## Forbidden Fallbacks

- local Notion Sync or Markdown mirrors
- local database indexes other than the `$ai-life-system-init` Runtime
- freshness fields such as `notion_synced_at`
- fixed database IDs, Data Source IDs, URLs, or personal paths
- guessing that a database container title is also the Data Source title

