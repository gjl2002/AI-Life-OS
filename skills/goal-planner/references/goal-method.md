# Goal Method

Use this reference for the `目标教练` planning model and quality rules.

## Core Model

```text
季度目标 = 未来约三个月要抵达的状态
完成状态 = 不使用 KR，但说明什么出现时算基本完成
项目 = 有终点的交付路径
习惯 = 持续重复的行为系统
任务 = 最小行动颗粒
打卡/专注/复盘 = 执行证据
```

## Objective Rules

A good quarterly objective should be:

- one short sentence
- internally meaningful
- focused enough for roughly one quarter
- challenging but not fantasy-sized
- visible by the end of the goal period
- connected to current life/domain priorities
- not merely copied from social expectation

Recommended Chinese shape:

```text
为了____，我希望在未来三个月实现____状态。
```

Then compress it into a short objective if possible.

Use two layers:

- `目标名`: short title, preferably 4-12 Chinese characters.
- `目标分析`: longer explanation, rationale, and completion state.

Do not put a paragraph-length sentence into the objective field. If the best wording is long, keep the title short and move the longer wording into analysis.

## Done State

Do not use KR by default. Use `完成状态`.

`完成状态` answers:

- What concrete state, artifact, rhythm, or result would make this goal basically complete?
- What can be seen, checked, felt, or reviewed at the end of the goal period?
- What minimum evidence avoids pure self-deception?

Good done states can include:

- a shipped artifact
- a finished draft
- a stable weekly rhythm
- a visible behavior change
- a usable system
- a completed experiment
- a reviewed and archived deliverable

Do not create precise numeric targets from stale or missing baselines. For body metrics, money, learning scores, or similar measurable goals:

- If current baseline exists, use it cautiously and cite it.
- If only stale baseline exists, mark it as historical reference and request a new baseline.
- If no baseline exists, define the first project/action as establishing baseline.

## Projects

Projects are finite, deliverable paths that directly move the goal.

Rules:

- Usually create 2-4 projects per quarterly goal.
- Each project should have a clear output.
- Each project usually spans 1-4 weeks.
- Name projects as verb + noun when possible.
- Avoid projects that are just vague effort labels.

Good project examples:

- 完成六级听力诊断与错题系统
- 写完论文实验结果章节初稿
- 搭建目标教练 Skill 第一版
- 发布 6 篇定位验证内容

For habit-heavy goals, projects should create or improve the system, not duplicate the recurring action.

Examples:

- Project: 建立身体数据记录模板
- Habit: 每周一记录身体数据
- Project: 设计 3 条饮食底线与默认菜单
- Habit: 每天 2 餐蛋白质优先

Weak project examples:

- 提升英语
- 好好科研
- 做自媒体
- 学习 AI

## Habits

Habits are recurring support systems. They should not be forced into projects.

Use habits when the goal depends on repetition:

- daily/weekly practice
- health and energy stability
- review rhythm
- input/output cadence
- skill drills

Habit design should include:

- behavior
- frequency
- time/context cue when useful
- minimum version when activation cost is high
- check-in or打卡 method
- relation to the goal/project

## Tasks

Tasks are the smallest action grains.

In first-pass reports, give only first-week actions unless the user asks for full task creation.

Good tasks:

- specific
- checkable
- dated or context-bound when useful
- small enough to start

Avoid generating a full-quarter task calendar unless requested.

## Repair Heuristics

When a goal feels stuck, diagnose:

- false goal: looks good but has no inner pull
- oversized goal: too big for the next roughly three months
- empty goal: abstract ideal with no visible state
- totalizing goal: tries to include everything
- project gap: no deliverable projects
- habit gap: no recurring behavior support
- task fog: no first-week action
- evidence gap: no current records or historical feedback
- energy mismatch: plan exceeds available time/energy

## Quality Check

Before finalizing, use `goal-planning-audit.md` for the semantic review and run `goal_planning_quality_check.py` when available.
