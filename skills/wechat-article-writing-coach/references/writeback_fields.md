# Cloud Notion Writeback

Use only when the user asks to save or update the article.

## Resolve and Verify

1. Run Runtime `status` and resolve `content`.
2. Require one `ready`, `read_ready` Data Source. If multiple targets remain after context filtering, ask the user.
3. Fetch the live Data Source and read its current schema. Never copy field names or options from this reference.
4. Search the cloud target for duplicate or overlapping title/topic records. Fetch plausible matches before choosing create versus update.
5. Preserve unrelated existing properties and body content when updating.

## Field Selection

Use only live writable fields that serve the request:

- always set the real title property;
- set format, category, purpose, status, tags, dates, account, series, and source relations only when those fields and options exist and the evidence supports them;
- choose status from the live schema according to whether the record is an idea, active draft, publish-ready article, or published article;
- add relations only after resolving and confirming the target pages;
- never fill buttons, formulas, rollups, analytics, or invented performance numbers.

Before writing, call Runtime `check-write` with the resolved Data Source ID, operation, every field, and every select/status option being used. A passing check does not replace user authorization or the live fetch.

## Mutation and Readback

- Ask for confirmation immediately before create/update unless the user already explicitly authorized direct writeback.
- Write the article body without duplicating the page title at the top.
- Do not execute Notion buttons.
- Fetch the created/updated page and verify title, selected properties, source relations, and article body.
- If the live schema changes between preflight and mutation, stop and rebind or re-resolve instead of guessing.

