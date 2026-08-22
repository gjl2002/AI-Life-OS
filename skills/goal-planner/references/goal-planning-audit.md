# Goal Planning Audit

Use this before producing a formal `目标教练报告` or writing planned objects to Notion. The goal is to make the plan executable without turning it into corporate OKR, fake metrics, or a giant task calendar.

## Planning Snapshot

Keep this working note:

```markdown
规划对象:
路线:
  - 新目标 / 修目标 / 拆项目习惯 / 推进不动 / 启动报告
领域:
当前目标周期:
用户输入事实:
系统记录证据:
方法论原则:
规划假设:
缺失数据:
```

## Objective Gate

A valid quarterly objective should be:

- short enough to become a `目标` title.
- visible within roughly one quarter.
- meaningful to the user, not copied from external expectation.
- narrow enough to guide tradeoffs.
- free of KR/OKR language unless the user explicitly asks.

When the user is choosing between directions or the goal may be only a doable point, read `goal-opportunity-radar.md` before finalizing the objective. Prefer a goal that can serve a stronger long-term line, borrow a useful surface, and still produce a quarterly done state.

If the best wording is long, split:

- `目标名`: 4-12 Chinese characters when possible.
- `目标分析`: rationale, context, completion state, and tradeoffs.

## Done-State Gate

The done state must answer:

- What artifact, rhythm, behavior change, experiment, or reviewed result exists at the end of the goal period?
- What minimum evidence prevents self-deception?
- Is any numeric target supported by a current baseline?

If a baseline is missing, do not invent a precise target. Make baseline setup a first project or first-week action.

## Project / Habit Boundary

Use this boundary test:

- If it produces a one-time artifact/system/deliverable, it can be a project.
- If it repeats indefinitely, it is probably a habit.
- If it can be completed in one sitting or one day, it is probably a task.

Projects:

- usually 2-4 per goal.
- must have deliverables.
- should directly serve the goal.
- should not be vague effort labels.

Habits:

- usually 1-3 key habits.
- must include frequency or cue/context when useful.
- should support the goal without duplicating a project.

## First-Week Action Gate

Give 1-3 first-week actions unless the user asks for a full task buildout. Each action should have:

```markdown
动作:
时间/触发:
完成标准:
服务目标/项目/习惯:
依据:
```

Avoid:

- "提升能力"
- "坚持执行"
- "多学习"
- "好好推进"
- a full-quarter task calendar on the first pass

## Risk And Tradeoff Gate

Every formal report should name:

- most likely failure mode.
- what must be paused, reduced, or not started.
- one if-then response for predictable friction.
- energy/time mismatch if the plan looks bigger than the user's current capacity.

## Evidence Basis Rule

Every non-obvious suggestion should label its basis:

- `系统记录`
- `用户输入`
- `领域常识`
- `方法论原则`
- `规划假设`
- `缺失数据`

Do not hide domain advice inside `系统记录`. Do not present planning hypotheses as known facts.

## Notion Boundary

Do not write automatically. If the user explicitly asks to save the accepted plan, use `notion-writeback.md` to map, verify, deduplicate, write, and read back the intended objects.
