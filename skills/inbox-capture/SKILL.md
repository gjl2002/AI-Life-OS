---
name: inbox-capture
description: 快速记录随手想到的任何内容到 Notion「收集箱」。当用户说任何想法、灵感、待办念头、看到的信息、语音转文字的内容，或者直接发一段话/一句想法时，直接录入收集箱。不需要分类、不需要结构化、不需要问用户，说什么记什么。
---
## 用户自己的 Notion 接入

本 Skill 使用 `$ai-life-system-init` 定位用户自己的 Notion 结构。执行前先运行 `scripts/runtime.py status`；状态为 `needs_init` 时先引导用户完成初始化。对本次操作涉及的每个概念运行 `scripts/runtime.py resolve --concept <key>`，只使用 Runtime 返回的目标 Data Source ID。读取该 Data Source 的实时 Schema，并在写入前运行 `scripts/runtime.py check-write` 校验本次属性、选项和 relation。

概念映射：`inbox, task, note, content, question`。

创建时必须让当前 Notion connector 将新页面的 parent 指向已解析的 Data Source；写入后回读确认 parent 和属性。若概念未找到、结构不兼容、候选不唯一或 connector 无法确认 parent，应停止该写入并说明原因，不得猜 ID、扫描无关空间或复制已有个人记录。以下正文中的数据库路径、字段名、选项和默认值若与用户实时 Schema 不一致，均视为示例而非要求；只有语义和字段类型明确匹配时才映射，否则询问或安全停止。仅读取本次任务所需的数据；不得将用户本地索引、凭据、页面 ID 或个人样例打包发布。

# Inbox Capture — Notion 收集箱快速记录

## 数据库

- **目标数据源**：以 Runtime 对 `inbox` 的解析结果为准

## 执行流程

### 1. 清洗语音文本（如适用）

如果输入明显是语音转写的原始文本（有重复、语气词、断句混乱），先按 [references/voice-normalize.md](references/voice-normalize.md) 做轻度清洗：删语气词、修错别字、转阿拉伯数字、修正AI/工具名误识别。

**注意**：不是总结或改写，只做最小修正，保留用户原意。

### 2. 解析目标并直接创建

使用 Runtime 已解析的 `inbox` Data Source。按实时 Schema 组装本次记录字段，并通过支持指定 Data Source parent 的 Notion 创建工具直接创建新记录。不得读取或复制既有记录作为模板。若当前 connector 无法指定并确认 parent，停止写入并报告限制。

### 3. 写入属性

```json
{
  "名称": "<一句话标题，不超过20字>",
  "内容": "<清洗后的完整内容>",
  "类型": "文字备忘录",
  "状态": "收集"
}
```

### 4. 设置正文

仅当用户输入确实需要正文保存且 Schema/工具支持时写入正文；否则保持正文为空，不做清空操作。

### 5. 验证

fetch 新页面，确认 parent、名称和内容已落库；若本次写入了正文，也确认正文内容。

## 原则

- **不提问、不分类、不总结**：用户说什么就记什么
- **轻度清洗**：语音输入删语气词、修错别字、转数字，但不改写原意
- **名称简短**：标题帮用户快速识别即可
- **不复制既有记录**：仅写入本次输入明确提供的信息，避免继承其他用户数据。
- **速度优先**：这是最快的录入，不要做多余操作

## 不碰

- 日期：自动填
- 按钮字段（转为任务/转为笔记/转为选题/快速归档/删除）：用户自己点
