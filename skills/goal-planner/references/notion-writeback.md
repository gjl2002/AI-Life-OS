# Notion Writeback

Use this only when the user explicitly asks to save/write/update planned objects in Notion.

## Default Rule

Write planned objects, not the whole report, unless the user explicitly asks to preserve the report body.

Never write automatically after a planning answer. Ask for confirmation unless the user clearly says:

- 直接写入
- 写回 Notion
- 更新这些记录
- 按这个方案创建

## Target Mapping

| Planned object | Target |
|---|---|
| Goal title, goal analysis, done state | live action-board goal data source, linked to the current quarter or goal-cycle record only when the live schema supports it |
| Deliverable projects | live action-board project data source |
| Recurring behaviors | live action-board habit data source |
| First-week/date-specific actions | live action-board task data source |
| Accepted planning summary | `复盘笔记` or explicitly named note page |
| Execution evidence/check-ins | `打卡`, `专注`, `每日复盘`, or relevant review workflow |

Do not assume a cycle launch page is the report database. Use any exact Notion cycle label only as verified storage context, not as part of the coaching model.

## Before Writing

Prepare this plan:

```markdown
写入计划：
- 目标：
- 项目：
- 习惯：
- 任务：
- 不写入/暂缓：
- 需要云端验证的字段：
- 待用户确认的问题：
```

Then verify:

- target database/page identity.
- current schema and required fields.
- current action-board and goal-cycle page/data-source identity; do not assume either label is itself a data source.
- relation targets such as the current goal-cycle record and existing `目标`, `项目`, `习惯`, or `任务`.
- duplicate existing goals/projects/habits/tasks.
- whether the planning report has passed `goal_planning_quality_check.py`.

## Writing Rules

- Use cloud Notion for writes and readback verification.
- Preserve existing user content unless the user asks to replace it.
- Do not invent relations when the target page cannot be verified.
- Mark planning assumptions as assumptions in body text; do not encode them as confirmed properties.
- If a numeric target has no current baseline, write baseline setup as a task/project instead of a fake precise metric.

## After Writing

Read back and verify:

- correct database/page.
- key fields present.
- goal/project/habit/task boundaries were preserved.
- no accidental KR/OKR fields were invented.
- no obvious truncation.

If readback fails, report what was written and what could not be verified.
