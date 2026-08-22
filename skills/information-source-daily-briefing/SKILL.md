---
name: information-source-daily-briefing
description: Create a Chinese daily briefing exclusively from sources the user has marked as followed in a connected cloud Notion information-source database, and write the report to the user's Notion daily-report database by default. Use when the user asks for 信息源日报, 我的关注源日报, 关注源摘要, Notion 信息源早报, or a recurring briefing that reads the user's own selected sources. Verify recent timestamps and links, disclose unreadable sources, never add unlisted public, official, trending, or paper sources, and skip Notion writeback only when the user explicitly asks for preview-only output.
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
- 默认运行需要用户自己的`信息源`和`信息日报`数据库；首次运行未提供准确链接时先请求两个数据库链接。只有明确要求仅预览时，才只要求`信息源`。
- 不读取本地 Notion Sync、Markdown 导出、数据库索引或固定个人目录。
- 不读取商业定位、人生系统或其他个人数据库，除非用户在本次请求中主动提供一段关注重点。
- 不使用硬编码的页面 ID、数据库 ID、字段名或个人路径。
- 不自动加入 OpenAI、Anthropic、新闻网站、热门榜单、GitHub、论文或任何未被用户关注的来源。
- 可以沿着关注源给出的原始链接或引用链接核实事实，但不能因此把新来源加入日报候选池。

## AI 人生系统索引

正式运行时先调用 `$ai-life-system-init` 的 `scripts/runtime.py status`。用 `resolve --concept information_source` 定位真实`信息源`数据源；用 `resolve --source 信息日报`定位日报数据源。可选概念库只有用户已启用时才按真实名称解析。

- `needs_init`：引导用户先运行 `$ai-life-system-init`，不回退固定 ID，也不要求学员重新配置数据库清单。
- `multiple`：不静默取第一个；根据用户链接或已确认自动化配置消歧。
- `not_found`：请求正确链接或权限，不断言模板缺少该数据库。
- 本地索引只负责 Notion 结构路由；关注状态、记录内容和实时 Schema 仍从云端 Notion 读取。
- 默认写入日报时，写入前调用 `check-write`；通过后仍须实时查重、核对 Schema 并写后回读。用户明确要求仅预览时不执行写入预检。

## Modes

默认按`写入日报`模式运行：

- `写入日报`：普通调用和自动日报都在生成后写入用户指定的云端`信息日报`数据库，并完成回读验证。
- `仅预览`：只有用户明确说“只预览”“不要写入”或语义等价表达时，才只在对话中交付 Markdown。

概念库始终是可选能力。只有用户已提供概念库、明确启用概念沉淀，并且当天出现合格概念时才写入。

## Workflow

### 1. Resolve The Live Source Database

使用用户提供的 Notion 数据库链接、数据库名称或已确认的自动化配置定位云端`信息源`。

读取实时 schema，识别名称、关注状态和来源网址的语义字段。字段含义不明确时向用户确认，不擅自创建字段或状态选项。

只查询被用户标记为正在关注、Following、Active 或语义等价状态的来源。若无法读取云端数据库或无法得到关注列表，停止，不使用本地文件或公共来源替代。

### 2. Verify Source Coverage

逐个检查关注源在时间窗口内是否有可验证的新内容。优先使用 RSS/Atom 或来源提供的稳定订阅地址，再使用原始网页、频道页或公开接口。

为每个来源保留一种覆盖状态：

- `有已验证更新`
- `已验证暂无更新`
- `未能验证`

读取失败、反爬、网络错误或只有旧缓存时写成`未能验证`，不能写成`无新增`。若全部关注源都无法进行当前验证，停止生成日报；若只有部分失败，继续并公开覆盖缺口。

### 3. Build The Candidate Pool

候选池只能来自关注列表中已经验证的新内容。

- 去除重复转载、广告、无有效内容的更新和明显离题内容。
- 不因为当天内容少而补充公共新闻。
- 用户在本次请求中给出关注重点时，可用它调整排序，但不能改变来源边界。
- 论文、官方公告或公共页面只有本来就在关注列表中，或被关注内容直接引用用于事实核验时才读取。

### 4. Read And Verify The Content

尽量获取标题、链接、发布时间和正文、摘要、描述或文字稿。区分来源事实、来源观点和综合理解。

如果只能取得标题与简介，可以进行有限判断，但必须明确资料限制。每个进入日报的信息项都要保留可点击的来源链接。

### 5. Synthesize The Briefing

不要逐条机械摘要。先识别当天不同来源共同出现的信号、值得深看的差异、可复用的方法和对用户当前关注重点的启发。

内容少时生成短日报；没有已验证新增时，生成如实的无新增简报，并保留来源覆盖情况。不要强制凑固定条数。

### 6. Deliver Or Write Back

默认完成 Notion 写回：

- 普通调用和自动日报：先读取目标日报数据库实时 schema，并以日期和规范化标题检查重复；优先更新同一天已有日报，否则创建新页面。
- 仅预览：用户明确要求不写入时，直接交付 Markdown。
- 写入后重新读取云端页面，验证关键属性和正文。

默认模式下，如果没有提供日报数据库或无法确认实时 schema，停止写入并请求正确链接或权限；可以说明已经形成的草稿状态，但不能静默降级为仅预览，也不得声称已保存。

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

以下情况停止生成和写入，并说明具体依赖：

- 云端 Notion 无法访问；
- 用户的关注源数据库无法读取；
- 无法识别必要语义字段且用户尚未确认；
- 所有当前来源都无法验证发布时间或链接；
- 默认运行时无法定位`信息日报`或确认其实时 schema。

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
