---
name: information-source-daily-briefing
description: Create a Chinese daily briefing exclusively from sources the user has marked as followed in a connected cloud Notion information-source database, and write the report to the user's shared Notion 日报 data source with 标签 = 日报 by default. Use when the user asks for 信息源日报, 我的关注源日报, 关注源摘要, Notion 信息源早报, or a recurring briefing that reads the user's own selected sources. Verify recent timestamps and links, disclose unreadable sources, never add unlisted public, official, trending, or paper sources, and skip Notion writeback only when the user explicitly asks for preview-only output.
---

# 信息源日报

## Purpose

把用户主动关注的信息源在指定时间窗口内的新内容，整理成一份可追溯、有重点、能帮助理解和行动的中文日报。

最高原则：

> 只整理用户选择的信息世界；没有足够新增时如实说明，不用公共来源填满日报。

这不是行业新闻聚合器、公共趋势扫描或研究日报。默认时间窗口为过去 24 小时；使用用户或运行环境的时区，不写死个人时区。

## Required Reference

正式运行前读取 `references/source-daily-runbook.md`。首次连接、字段识别、来源核验、报告结构、写回和失败处理都以该文件为准。

## Data Boundary

- 云端 Notion 是唯一的个人数据来源。
- 默认运行需要用户自己的「信息源」和已确认的共享「日报」数据源。需要消歧时才请求准确链接。仅预览只需定位「信息源」。
- 不读取本地 Notion Sync、Markdown 导出、数据库索引或固定个人目录。
- 不读取商业定位、人生系统或其他个人数据库，除非用户在本次请求中主动提供一段关注重点。
- 使用当前用户的实时数据库结构和连接权限。写回所需的「标签」及选项「日报」均须通过实时 Schema 核验。
- 不自动加入 OpenAI、Anthropic、新闻网站、热门榜单、GitHub、论文或任何未被用户关注的来源。
- 可以沿着关注源给出的原始链接或引用链接核实事实，但不能因此把新来源加入日报候选池。

## AI 人生系统索引

正式运行时先调用 `$ai-life-system-init` 的 `scripts/runtime.py status`。用 `resolve --concept information_source` 定位真实`信息源`数据源；用 `resolve --concept daily_report` 定位共享「日报」。语义未识别时可用 `resolve --source 日报` 精确查找。首次写入须由用户确认目标数据源。可选概念库只有用户已启用时才按真实名称解析。

- `needs_init`：引导用户先运行 `$ai-life-system-init`，不回退固定 ID，也不要求学员重新配置数据库清单。
- `multiple`：不静默取第一个；根据用户链接或已确认自动化配置消歧。
- `not_found`：请求正确链接或权限，不断言模板缺少该数据库。
- 本地索引只负责 Notion 结构路由；关注状态、记录内容和实时 Schema 仍从云端 Notion 读取。
- 默认写入日报时，写入前调用 `check-write`；通过后仍须实时查重、核对 Schema 并写后回读。用户明确要求仅预览时不执行写入预检。

## Modes

默认按`写入日报`模式运行：

- `写入日报`：普通调用和自动日报都在生成后写入用户确认的共享「日报」，设置 `标签 = 日报` 并回读。
- `仅预览`：只有用户明确说“只预览”“不要写入”或语义等价表达时，才只在对话中交付 Markdown。

概念库始终是可选能力。只有用户已提供概念库、明确启用概念沉淀，并且当天出现合格概念时才写入。

## Workflow

### 1. Resolve The Live Source Database

使用用户提供的 Notion 数据库链接、数据库名称或已确认的自动化配置定位云端`信息源`。

读取实时 schema，识别名称、关注状态和来源网址的语义字段。字段含义不明确时向用户确认，不擅自创建字段或状态选项。

只查询被用户标记为正在关注、Following、Active 或语义等价状态的来源。若无法读取云端数据库或无法得到关注列表，停止，不使用本地文件或公共来源替代。

### 2. Verify Source Coverage

逐个核验正在关注且已启用的来源。先保留来自实时查询的完整关注名单，再按运行手册为每个来源记录覆盖状态、证据和失败原因。优先使用该源的 RSS、订阅页、原始页面或公开接口，遇到临时失败时按手册重试或走同一来源的备用入口。

每条候选必须有标题、原始链接和时区明确的发布时间。报告里把已验证更新、已验证暂无更新、未能验证区分开。只有部分来源失败时继续并披露覆盖缺口。关注源非空且全部无法验证时停止。

### 3. Build The Candidate Pool

候选池只能来自关注列表中已经验证的新内容。

- 去除重复转载、广告、无有效内容的更新和明显离题内容。
- 不因为当天内容少而补充公共新闻。
- 用户在本次请求中给出关注重点时，可用它调整排序，但不能改变来源边界。
- 论文、官方公告或公共页面只有本来就在关注列表中，或被关注内容直接引用用于事实核验时才读取。

### 4. Read And Verify The Content

先核对发布时间和原始链接，再按条目补充正文或证据。视频源的订阅结果只用于发现条目。仅有标题时记录更新事实。简介或章节支持范围判断。对论点作判断时，应有可定位的正文、字幕或文字稿。每条入选内容记录证据等级，区分来源事实、观点和日报判断。

### 5. Synthesize The Briefing

不要逐条机械摘要。先识别当天不同来源共同出现的信号、值得深看的差异、可复用的方法和对用户当前关注重点的启发。

内容少时生成短日报；没有已验证新增时，生成如实的无新增简报，并保留来源覆盖情况。不要强制凑固定条数。

### 6. Deliver Or Write Back

- 先按[写前质量检查](references/source-daily-runbook.md#写前质量检查)验证来源覆盖、时间窗口、必需栏目和入选链接。预览模式在校验通过后交付 Markdown。
- 在共享「日报」实时核验标题字段和「标签」单选项「日报」。按完整标题 `YYYY-MM-DD 信息源日报` 与 `标签 = 日报` 查重，唯一匹配时局部更新，没有匹配时按手册处理。检查同标题不同标签的历史记录后再决定是否创建。
- 用 `check-write` 对本次动作预检。写后核对数据源、完整标题、标签、正文和入选链接。对完整回读的正文再次运行质量检查。连接、选项或回读有问题时，说明草稿或写入的实际状态。

### 7. Update The Optional Concept Library

只在概念库已启用时执行。合格概念必须：

- 能跨场景复用；
- 有可靠来源；
- 对用户后续理解、表达或实践有价值；
- 不是一次性的产品名、论文术语或模型指标。

写入前搜索同名和近似概念，优先更新已有页面。没有合格概念时如实说明，不强行创建。

## Output Contract

根据当天内容自然使用以下结构：

```markdown
# YYYY-MM-DD 信息源日报

## 今日核心判断

## 信息源读取覆盖

## 今日新增

## 值得深看

## 可以学习

## 可以收藏

## 对我的启发

## 今日行动建议

## 概念库更新
```

`今日核心判断`、`信息源读取覆盖`和`今日新增`是核心栏目。其余栏目没有合适内容时可以省略；不要为完整而填充空洞文字。

## Failure Protection

以下情况停止生成和写入，并说明具体依赖。

- 云端 Notion 无法访问；
- 用户的关注源数据库无法读取；
- 无法识别必要语义字段且用户尚未确认；
- 关注源非空且全部无法在窗口内核实是否更新。

默认写回时，目标「日报」未确认、实时 Schema 无法核实或缺少单选项「日报」都会阻止写入。可以保留已生成草稿。

部分来源失败不阻塞整份日报，但必须列出未能验证的来源，并在核心判断中说明覆盖是否完整。

## Guardrails

- 不自动搜索或加入用户未关注的信息源。
- 不用模型已有知识替代当前来源证据。
- 不把来源读取失败写成没有更新。
- 不把摘要写成来源没有表达的结论。
- 不强制生成固定数量的必看、收藏或行动项。
- 不读取商业定位或其他个人数据库作为默认筛选器。
- 用户明确要求仅预览时，不写入、创建或更新 Notion。
- 不在写入后跳过云端回读验证。
