---
name: book-tracker
description: 录入书籍到用户自己的 Notion 数据库。当用户提到读了/在读/想读某本书、记录书籍、或直接提供书名时使用。依据用户实时 Schema 与明确提供的信息填写字段；作者关联仅匹配当前用户已有页面，不猜测阅读平台或个人偏好。
---
## 用户自己的 Notion 接入

本 Skill 使用 `$ai-life-system-init` 定位用户自己的 Notion 结构。执行前先运行 `scripts/runtime.py status`；状态为 `needs_init` 时先引导用户完成初始化。对本次操作涉及的每个概念运行 `scripts/runtime.py resolve --concept <key>`，只使用 Runtime 返回的目标 Data Source ID。读取该 Data Source 的实时 Schema，并在写入前运行 `scripts/runtime.py check-write` 校验本次属性、选项和 relation。

概念映射：`book, person`。

创建时必须让当前 Notion connector 将新页面的 parent 指向已解析的 Data Source；写入后回读确认 parent 和属性。若概念未找到、结构不兼容、候选不唯一或 connector 无法确认 parent，应停止该写入并说明原因，不得猜 ID、扫描无关空间或复制已有个人记录。以下正文中的数据库路径、字段名、选项和默认值若与用户实时 Schema 不一致，均视为示例而非要求；只有语义和字段类型明确匹配时才映射，否则询问或安全停止。仅读取本次任务所需的数据；不得将用户本地索引、凭据、页面 ID 或个人样例打包发布。

# Book Tracker — Notion 书籍录入

## 数据库

- **目标数据源**：以 Runtime 对 `book` 的解析结果为准

## 执行流程（照此执行）

### 1. 直接新建记录



### 2. 检索书籍信息

用 `general_search` 搜索：
- `"<书名>" 作者 豆瓣`

提取：作者名、豆瓣链接、判断书籍分类。

**书籍分类选项**（multi_select，可多选）：商业、心理学、个人成长、AI、历史、哲学、小说、传记。

### 3. 查找作者

在人物库搜作者名：
- `notion_ai_search`（data_source_url=人物数据源）按作者名搜
- **找到** → 用现有作者页面 URL
- **没找到** → **不新建人物页**，作者字段留空，在报告中告知用户

### 4. 上传封面

1. `image_search` 搜 `"<书名>" 书籍封面 正式封面`
2. 追踪直链：`curl -sL -o /dev/null -w "%{url_effective}" "<短链>"`
3. `notion_create_attachment` → `file_upload_id`

### 5. 一次性 update 属性

```json
{
  "书名": "<书名>",
  "作者": ["<作者页面URL>"] 或 null（人物库找不到作者时留空）,
  "书籍分类": ["<分类>"],
  "书籍格式": null,
  "豆瓣链接": "https://book.douban.com/subject/xxx/",
  "书籍封面": [{"type":"file_upload","file_upload":{"id":"<file_upload_id>"}}],
  "状态": "准备阅读",
  "书籍评分": null,
  "阅读时长(min)": null,
  "date:开始日期:start": null,
  "date:结束日期:start": null,
  "date:上次阅读:start": null,
  "每日复盘": null,
  "计时": null,
  "知识主题": null,
  "笔记": null,
  "当前书籍": null,
  "问题": null,
  "情绪记录": null,
  "书籍原文": null,
  "角色数据": null,
  "项目": null,
  "积分设定": null
}
```

新页面只写本次记录明确提供的值；未提供的可选字段留空，不沿用其他记录的属性或正文。

### 6. 清空页面正文

新页面只写本次记录明确提供的值；未提供的可选字段留空，不沿用其他记录的属性或正文。

### 7. 验证

fetch 新记录，确认 parent-data-source = 书籍、属性落库、封面挂载、作者已关联。向用户报告。

## 不碰

- **书籍评分**：用户主观评分
- **公式字段**（主题、星级评分、经验、跃点、金币、游戏化概览）：Notion 自动算
- **按钮字段**（阅读、已阅读、写笔记、休息）：用户自己点
- **阅读状态/阅读时长**：用户阅读时记录

## 边界

- 搜不到豆瓣 → 豆瓣链接留空
- 封面找不到 → 留空告知
- 作者是外国人 → 用中文译名搜索人物库
- 作者在人物库找不到 → 不新建，作者留空，告知用户
