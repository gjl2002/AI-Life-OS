# Goal Planning Report Template

Use this template for a formal `目标教练报告`. Omit sections that do not apply.

```markdown
# 目标教练报告

## 本次主线

- 本次规划对象：
- 来源系统：成长 / 商业 / 生活
- 目标周期：未来约三个月
- 主线：
- 补线：
- 参考记录：
- 信息缺口：

## 1. 当前状态摘要

### 你直接说到的事实
- ...

### 系统记录里的线索
- ...

### 我的规划判断
- ...（依据：系统记录 / 用户输入 / 领域常识 / 规划假设）

### 仍需确认
- ...

## 2. 季度目标

### 建议目标

目标名：

> ...

目标描述：

> ...

### 完成状态

目标周期结束时，如果出现以下状态，就可以认为这个目标基本完成：

- ...

### 目标修正说明

- 原始表达：
- 修正原因：
- 取舍：
- 依据：

## 3. 项目拆解

| 项目 | 交付物 | 建议周期 | 服务目标的方式 | 风险 |
| --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... |

检查：项目必须有交付物。不要把重复行为写成项目；重复行为放到习惯支撑。

## 4. 习惯支撑

| 习惯 | 频率 | 作用 | 打卡/反馈方式 |
| --- | --- | --- | --- |
| ... | ... | ... | ... |

## 5. 本周启动动作

1. ...
2. ...
3. ...

## 6. 风险与取舍

### 最可能失败的原因
- ...

### 需要主动放弃或暂缓的事
- ...

### 执行卡点预案
- ...

## 7. 可沉淀记录

如果你觉得这版规划没问题，可以考虑这样沉淀：

- 目标本体：
- 项目拆解：
- 习惯支撑：
- 本周动作：
- 规划/复盘摘要：
```

Before sending a formal report, use `goal-planning-audit.md` and run `scripts/goal_planning_quality_check.py` when available. Fix blocking failures before final output.

## Short Output

Use this when the user wants a quick answer:

```markdown
## 建议目标

## 完成状态

## 项目

## 习惯

## 本周第一步

## 风险

## 可沉淀记录
```

## Evidence Block

When records were checked, include a compact audit block:

```markdown
参考记录：
- 当前目标周期：...
- 目标/项目/习惯：...
- 人生领域/人生设计：...
- 打卡/专注/每日复盘：...
- 人生时刻/复盘笔记：...

未查/未找到：
- ...
```

If cloud Notion retrieval or `goal_planning_quality_check.py` could not run, say so briefly when it affects confidence.

## Tone

Use warm, grounded Chinese. Avoid corporate OKR jargon. Be direct about tradeoffs. The output should feel like a planning coach who understands execution reality, not a productivity template generator.
