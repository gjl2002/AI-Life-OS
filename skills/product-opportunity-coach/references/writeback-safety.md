# Cloud Notion Writeback Safety

Use only when the user explicitly asks to save, create, or update the opportunity judgment.

## Destination Boundary

Do not assume a fixed report database, page, board, field, option, or folder.

Choose the destination in this order:

1. the exact page/database/record explicitly named or linked by the user;
2. an existing report target the user explicitly confirms;
3. a specific `product` record only when the user explicitly asks to update that product.

If the user says only “保存” and more than one destination is plausible, ask where to save. Do not automatically change the source product record.

## Runtime and Live Checks

Before any mutation:

1. Run Runtime `status`.
2. Resolve the exact page or Data Source by concept, real title, or user-provided URL.
3. For a database target, fetch the live Data Source and inspect its current schema.
4. For an ordinary page, fetch the current body and identify the exact authorized section.
5. Search for an existing report or same-opportunity record before creating a duplicate.
6. Confirm the user has authorized this exact create/update action.

For database writes, call Runtime `check-write` with the real Data Source, operation, every field, and every select/status option used. For ordinary-page updates, call `check-page-write` with the resolved page ID.

Runtime readiness does not grant permission and does not replace the live cloud check.

## Mutation Rules

- Write only the final checked report or the explicitly requested fields/section.
- Preserve unrelated fields, relations, blocks, comments, and prior analysis.
- Do not execute Notion buttons.
- Do not invent status, board, category, or relation values.
- Do not overwrite a product description, user evidence, or market record merely to store the report.
- If creating a separate report, preserve a traceable link to the evaluated product when the live schema supports it and the relation is verified.

## Duplicate Rule

Before creating, search for:

- same opportunity/product;
- same report purpose;
- same decision period or explicit version;
- same user-provided target.

Update a clear matching record when that matches the user's intent. Create a separate record only when no suitable match exists or the user explicitly wants a new version.

## Readback

After writing, fetch the cloud page and verify:

- destination identity;
- title and any modified properties;
- report body or authorized section;
- source product/user/market records were not unintentionally changed.

Report what was written and what was intentionally left unchanged.
