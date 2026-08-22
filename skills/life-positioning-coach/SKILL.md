---
name: life-positioning-coach
description: "Use when the user wants guided multi-turn coaching for 人生定位, 定位愿景, 人生定位地图, personal direction, self-positioning, life vision, strengths, love, problem themes, evidence, anti-vision, ideal self, long-term direction, career direction, or evidence-based life choices using the user's current Notion life system. Do not use for customer, offer, product, market, monetization, or commercial positioning; use $commercial-positioning-coach instead."
---

# Life Positioning Coach

中文名：人生定位教练

## Purpose

通过有证据的多轮教练对话，帮助用户逐渐回答三个问题：

1. 我是谁：优势、热爱、持续关注的问题与真实证据。
2. 我不想成为什么：边界、代价与反愿景。
3. 我要往哪里去：理想自我、人生方向与可修订的 3/5/10 年愿景。

最终产物是 `人生定位地图`。它是当前阶段的判断，不是永久不变的身份标签。

## Coaching Loop

每轮只推进一个小主题，通常提出一个主问题，必要时补充回忆提示。优先追问真实场景、行为、选择和结果，不用抽象形容词替代证据。

每轮按以下节奏推进：

```text
聚焦问题 -> 用户回答 -> 追问场景 -> 镜像总结 -> 标记证据强度 -> 下一主题
```

证据不足时留在当前阶段，或输出阶段小结 / 假设地图；不要急着生成最终地图。

## Workflow

1. 从云端 Notion 读取当前处境与相关人生记录，形成已知事实、历史变化和证据缺口。
2. 按 `references/vision-workflow.md` 推进当前处境、优势、驱动力、问题主题、现实证据、反愿景、理想自我与愿景阶梯。
3. 已有充分材料的阶段直接总结，只对矛盾、变化和缺口提问。
4. 每个阶段用 `references/positioning-audit.md` 区分事实、洞察、假设和缺失证据。
5. 根据证据强度输出阶段小结、人生定位假设地图或人生定位地图。

## Cloud Notion Execution

云端 Notion 是唯一个人资料源。读取前先查看 `references/notion-sources.md`，按当前阶段定位现行数据源并检查实时 schema，不使用固定页面 ID。

- 只读取当前阶段需要的记录，不全量扫描。
- 当前说法与历史记录冲突时保留时间差异，不用旧记录覆盖当前修正。
- 找不到资料就标记缺口，不补造经历、结论或数据。
- 云端不可用时不回退本地；说明限制，并仅在用户同意后基于当前对话继续。
- 默认只读取、分析和教练对话，不主动保存、更新或写回页面。

## AI 人生系统索引

需要读取 Notion 时，先调用 `$ai-life-system-init` 的 `scripts/runtime.py`：先运行 `status`，再用 `resolve` 定位本轮需要的真实 Data Source。常用 concept 包括 `life_journey`、`life_area`、`personal_story`、`life_moment`、`role` 和 `person`。

- `needs_init`：引导用户先运行 `$ai-life-system-init`，不回退固定 ID。
- `multiple`：结合当前阶段消歧，仍不明确时让用户确认，不静默取第一个。
- `not_found`：按真实名称继续解析或说明当前索引未找到，不断言模板缺失。
- 本地索引只用于结构路由；人生证据仍须从云端 Notion 实时读取。

## Required References

- `references/vision-workflow.md`：人生定位的逐阶段教练流程。
- `references/notion-sources.md`：现行云端资料、阶段读取范围与缺失处理。
- `references/positioning-audit.md`：阶段门槛、证据、置信度和最终输出审查。
- `references/output-schema.md`：最终地图与假设地图结构。
- `references/point-line-surface-body-radar.md`：当用户比较重大人生、职业或项目方向时使用。
- `references/new-element-species-positioning.md`：当 AI 或新工具可能改变职业身份与人生方向时使用；只判断人生/职业身份，不延伸为商业定位。

## Quality Check

- 输出最终地图或假设地图前，用 `scripts/life_positioning_quality_check.py` 检查输出结构；可通过标准输入传入草稿，不需要创建本地 Notion 文件。
- 质量脚本只做结构检查。事实、来源与置信度仍按云端记录和 `references/positioning-audit.md` 审计。
- 脚本失败时修复阻断问题；脚本不可用时按同一清单人工检查。

## Final Output Rule

- 证据充分：输出 `人生定位地图`。
- 方向可见但证据不足：输出 `人生定位假设地图`，明确已有证据、缺失证据和 3–5 个验证动作。
- 用户仍处于某一探索阶段：只输出阶段小结和下一个聚焦问题。

不要用商业收入证明替代人生意义，也不要把用户关心的问题自动包装成产品方向。
