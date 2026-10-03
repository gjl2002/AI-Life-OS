---
name: info-backfill
description: 补全信息库中缺失的结构化字段。当用户说"帮我补一下信息库""信息库哪些没填""补全信息""刚同步的帮我补一下""扫一下信息库"时运行。自动补全信息源关联、作者、类型、平台、时长/字数。不改状态，不碰已归档/完成的内容。
---
## 用户自己的 Notion 接入

本 Skill 使用 `$ai-life-system-init` 定位用户自己的 Notion 结构。执行前先运行 `scripts/runtime.py status`；状态为 `needs_init` 时先引导用户完成初始化。对本次操作涉及的每个概念运行 `scripts/runtime.py resolve --concept <key>`，只使用 Runtime 返回的目标 Data Source ID。读取该 Data Source 的实时 Schema，并在写入前运行 `scripts/runtime.py check-write` 校验本次属性、选项和 relation。

概念映射：`information, information_source, question`。

创建时必须让当前 Notion connector 将新页面的 parent 指向已解析的 Data Source；写入后回读确认 parent 和属性。若概念未找到、结构不兼容、候选不唯一或 connector 无法确认 parent，应停止该写入并说明原因，不得猜 ID、扫描无关空间或复制已有个人记录。以下正文中的数据库路径、字段名、选项和默认值若与用户实时 Schema 不一致，均视为示例而非要求；只有语义和字段类型明确匹配时才映射，否则询问或安全停止。仅读取本次任务所需的数据；不得将用户本地索引、凭据、页面 ID 或个人样例打包发布。

# Info Backfill — 信息库补全

## 数据库


## 补全范围

只处理满足以下条件的信息：
- **状态**：status 为"收集"或"学习"（注意：是"学习"不是"学习中"）
- **跳过**：已归档·过时、低价值·删除 的内容不碰
- **原则**：缺什么补什么，已有的字段不覆盖

## 需要补的字段

| 字段 | 怎么补 |
|---|---|
| **信息源** (relation) | 根据作者名/频道名/平台，在信息源库 `ai_search` 匹配，找到就关联，找不到不新建 |
| **作者** (text) | 从标题、URL、正文开头提取作者名；已有就不覆盖。纯文本字段，不关联人物库 |
| **类型** (select) | 视频/文章/播客/图文/帖子/网页 |
| **平台** (select) | 从 URL 判断：bilibili.com→B站；xiaohongshu.com→小红书；youtube.com→YouTube；mp.weixin.qq.com→公众号；substack/个人域名→个人博客 |
| **时长 (min)** (number) | 视频/播客类，**必须抓实际时长**，不能只靠标题猜（见下方 YouTube 抓时长方法） |
| **字数 (个)** (number) | 文章类，fetch 正文后估算字数 |
| **要解决的问题** (relation) | 根据内容判断它解决了什么问题，在问题库 `ai_search` 匹配，找到就关联，找不到不新建 |

## ⚠️ 工具选择（已验证）

- `notion_query_data_sources`：`data` 参数格式被服务端拒绝，**不能用**。
- `notion_query_multiple_data_sources`：**可以用**，但必须传至少 2 个 data_source_urls（即使只查信息库，也把信息源库 URL 一起传上）。
- `view://<uuid>` 直接 fetch 报 400。
- `notion_ai_search`：可以搜，但不能按状态过滤，适合找特定内容不适合批量扫描。

## 执行流程

### 路径 A：批量扫描（用户说"扫一下信息库"）

1. **SQL 查询拉列表**：用 `notion_query_multiple_data_sources`，data_source_urls 传两个：

```json
{
  "data_source_urls": [
  ],
}
```

   （查"学习"状态把 WHERE 改成 `状态 = '学习'`。）

2. **分析缺什么**：逐条看返回结果，标出缺信息源/缺类型/缺平台/缺时长/缺字数的记录。

3. **批量匹配信息源**：对缺信息源的记录，提取作者/频道名，并行 `ai_search` 信息源库（`data_source_url`=信息源库），拿到匹配的信息源页面 URL。

4. **抓时长/字数**：
   - **YouTube 视频**：用 `web.fetch`，URL 换成 **`m.youtube.com`**（移动端），不要用 `www.youtube.com`（桌面版 JS 渲染重，fetch 经常失败）。snippet query 设 `"duration length minutes chapters timestamps"`，页面会返回章节时间戳列表，**最后一个章节的时间戳 + 估算后续时长 = 视频总分钟数**。
   - **文章/博客**：`web.fetch` 文章页，根据正文长度估算字数（英文文章约 2000-3000 词）。
   - **标题直接写了时长**（如"2小时课程""90 minutes"）：可以直接用，但仍建议 fetch 验证。

5. **一次性 update**：对每条记录，`notion_update_page`（update_properties）只传缺失的字段。relation 传 URL 数组，数字传 number。

6. **报告结果**：列出每条补了什么，哪些没找到（如实说明）。

### 路径 B：实时补全（用户说"刚同步的帮我补一下"）

1. 用户提供页面 URL 或刚同步了内容。
2. `notion_fetch` 那条记录，看缺什么字段。
3. 按路径 A 步骤 3-5 补全。
4. 不改状态。

## update 注意事项

- update 时只传缺失的字段，已有值不传（Notion update 是合并语义）。
- relation 字段值是页面 URL 数组。
- 数字字段传 JavaScript number，不是字符串。
- 补完后**不改状态**（状态由用户自己推进）。

## 不碰

- **状态**：补完不改
- **标签**：不自动打标签
- **公式字段**（概览、学习进度、阅读时长、相关度等）：Notion 自动算
- **已归档/完成的内容**：跳过
- **人物关联**：作者只是 text 字段，不去人物库建关联
