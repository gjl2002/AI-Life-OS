# Cloud Notion Writeback

## Authorization

Do not write automatically. Write or update only when the user explicitly asks to save, write back, sync, create a content page, or update an existing content record. The current message can provide authorization; do not ask again when it is already explicit.

## Resolve The Target

1. Run `$ai-life-system-init/scripts/runtime.py status`.
2. Resolve the stable concept `content`.
3. Use the target only when resolution is unique.
4. If `multiple`, disambiguate with the current system context and exact live title; ask if ambiguity remains.
5. If `not_found` or `needs_init`, stop. Do not fall back to a fixed database title, ID, URL, personal path, local mirror, or local index.

## Before Writing

1. Search the resolved cloud target for likely duplicates by title, topic, platform, core angle, and source material.
2. If a likely duplicate exists, fetch it and decide whether the user asked to update it or create a genuinely distinct note.
3. Fetch the live Data Source schema immediately before writing.
4. Map semantic content only to fields that actually exist. Do not assume title-field name, platform field, content type, status field, body field, relation, or option value.
5. Use only live select/status/multi-select options unless the user explicitly authorizes creating a new option.
6. Validate relation targets against the live schema and resolved target database.
7. Run Runtime `check-write` with the exact target Data Source, fields, relations, and option values involved.
8. Treat `write_ready: true` as a structural precheck, not as user authorization or a substitute for the live schema.
9. Do not write a final note with unresolved visual-context or deterministic blocking failures.

## Semantic Content To Preserve

Write as much of the following as the live schema and user request support:

- selected title;
- platform identity as Xiaohongshu;
- note type or content type;
- current workflow status;
- final body or active draft;
- title alternatives;
- tags;
- source/evidence summary;
- conversion intent;
- image-order and privacy advice;
- comment cue;
- Moments reuse suggestion;
- evidence labels or relations.

These are semantic intents, not fixed property names or fixed option values. If the live schema does not have a safe destination, keep the information in the page body rather than inventing a property.

## Page Body

Preserve the approved output package and keep operational advice separate from the publishable body. Do not accidentally place internal evidence logs, private identifiers, or quality-gate notes into public copy.

## After Writing

Read the cloud page back and verify:

- the correct page was created or updated;
- title and body match the approved version;
- mapped properties use valid live values;
- intended relations point to the correct pages;
- no private evidence or internal name leaked into public copy.

If verification fails, report the exact mismatch and correct it only within the user's authorization. Never claim success without readback.
