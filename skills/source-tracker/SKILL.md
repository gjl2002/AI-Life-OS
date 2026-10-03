---
name: source-tracker
description: 录入信息源到 Notion「信息源」数据库。当用户给一个链接（B站UP主、YouTube频道、公众号、播客、Newsletter、博客等）并说"记一下这个信息源""录入这个""关注了一个XX"时使用。自动读取链接名称、搜索网络信息判断分类/来源/付费模式/更新频率/标签/内容风格，关联已有主题和人物，用户只需给一个链接即可。
---
## 用户自己的 Notion 接入

本 Skill 使用 `$ai-life-system-init` 定位用户自己的 Notion 结构。执行前先运行 `scripts/runtime.py status`；状态为 `needs_init` 时先引导用户完成初始化。对本次操作涉及的每个概念运行 `scripts/runtime.py resolve --concept <key>`，只使用 Runtime 返回的目标 Data Source ID。读取该 Data Source 的实时 Schema，并在写入前运行 `scripts/runtime.py check-write` 校验本次属性、选项和 relation。

概念映射：`information_source, knowledge_theme, person`。

创建时必须让当前 Notion connector 将新页面的 parent 指向已解析的 Data Source；写入后回读确认 parent 和属性。若概念未找到、结构不兼容、候选不唯一或 connector 无法确认 parent，应停止该写入并说明原因，不得猜 ID、扫描无关空间或复制已有个人记录。以下正文中的数据库路径、字段名、选项和默认值若与用户实时 Schema 不一致，均视为示例而非要求；只有语义和字段类型明确匹配时才映射，否则询问或安全停止。仅读取本次任务所需的数据；不得将用户本地索引、凭据、页面 ID 或个人样例打包发布。

# Source Tracker — Notion 信息源录入

## 数据库

- **目标数据源**：以 Runtime 对 `information_source` 的解析结果为准

## 输入

用户给一个 URL，可能是：
- YouTube 频道链接（youtube.com/@xxx）
- B站 UP 主空间（space.bilibili.com/xxx）
- 公众号文章链接
- 播客链接
- Newsletter / 博客网站链接
- 其他内容创作者主页

## 执行流程

### 1. 直接新建记录

在 Runtime 已解析的用户 Data Source 中直接创建新记录；不复制现有记录。


### 2. 获取信息源名称

用 `web.fetch` 抓取用户给的链接，提取页面标题/频道名称。
如果抓取失败，用 `general_search` 搜索链接域名 + "频道" / "UP主" / "公众号" 获取名称。

**B站空间页是 JS 渲染的，web.fetch 抓不到内容。** 用以下 API 绕过：

```bash
# 从 space URL 提取 mid（数字ID），然后调用视频列表 API
curl -s "https://api.bilibili.com/x/space/arc/search?mid=<MID>&ps=3&pn=1" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" \
  -H "Referer: https://space.bilibili.com/<MID>/video"
```

这个 API 不需要登录、不会被风控，返回数据里包含：
- `data.list.vlist[0].author` → UP主名称
- `data.list.vlist[0..2].title` → 最近视频标题（判断内容方向）
- `data.list.vlist[0..2].description` → 视频描述（判断内容风格）
- `data.list.tlist` → 内容分类（如 160=生活）
- `data.list.vlist[0].pic` → 视频封面图（可直接用作 icon/cover）
- 视频创建时间戳 `created` → 算更新频率

> 注意：`x/space/acc/info` 和 `x/space/wbi/acc/info` 这两个接口会被风控（-352 校验失败/-799 请求频繁），不要用。只用 `arc/search`。

### 3. 网络调研判断属性

用 `general_search` 并行搜索：
- `"<名称>" 频道 介绍 内容`
- `"<名称>" 更新频率 订阅`

判断以下字段：

| 字段 | 判断规则 |
|---|---|
| **类型** | 以思考/认知/思维模型为主→认知成长；以解决具体问题/教程/工具为主→解决问题 |
| **来源** | 从 URL 判断：youtube.com→YouTube；bilibili.com→B站；mp.weixin.qq.com→公众号；播客平台→播客；substack→Newsletter；个人域名→博客/网站 |
| **付费模式** | 完全免费内容→免费；有免费也有付费课程/社群→含付费；会员订阅制→订阅制；付费社群/知识星球→付费社群 |
| **更新频率** | 每周1-2更→周更；每天更→日更；每月→月更；不定期→不定期 |
| **标签** | 从内容主题选：科技/商业/创业/产品/文化/个人成长/自由职业/投资理财/情感/人际关系/一人公司/职场/Notion（可多选） |
| **内容风格** | 有真实产品/项目交付、能推动行动→造东西的人；无产品但表达朴素可操作→说清楚的人；情绪价值强、激发灵感→点燃型 |
| **语言** | 中文内容→中文；英文内容→英文 |
| **简介** | 一句话描述这个信息源是做什么的 |

### 4. 关联主题

用 `notion_ai_search`（data_source_url=主题数据源）搜索与信息源内容相关的主题。
- 找到匹配的主题 → 填入 `主题` relation（URL 数组）
- 没找到 → 留空，不新建主题

### 5. 关联人物

用 `notion_ai_search`（data_source_url=人物数据源）搜索信息源主持人/创作者姓名。
- **找到** → 填入 `人物` relation
- **没找到** → **不创建人物页**，留空（这是与 book-tracker 的关键区别）

### 6. 搜索并上传 Icon 和封面

**B站信息源**：第2步 API 返回的 `vlist[0].pic` 就是视频封面，直接用它做 icon 和 cover，不用再 image_search。URL 是 `http://i0.hdslb.com/bfs/archive/xxx.jpg`，直接 curl 下载即可。

**其他平台**：用 `image_search` 搜索两张图：

1. **Icon（方形头像）**：搜 `"<名称>" 频道 logo 头像 avatar`，选清晰的方形 logo/头像图
2. **封面（宽幅背景）**：搜 `"<名称>" banner 频道背景`，选宽幅横幅图；如果没有合适的横幅，用频道代表作品的封面图

上传流程（两张图都走一遍）：
1. 下载图片到本地：`curl -sL -o /tmp/icon.jpg "<image_search返回的URL>"`
2. `FileBatchUpload` 获取 aka.doubaocdn.com 短链
3. 追踪直链：`curl -sL -o /dev/null -w "%{url_effective}" "<短链>"`
4. 在下一步 update_page 时，用 `icon` 参数传头像直链，`cover` 参数传封面直链

> 如果搜不到合适的封面图，用头像图同时作为 icon 和 cover（参考 Matt Wolfe 的做法）。
> 如果图片实在找不到，icon 用 emoji（如 📺 / 🎙️ / ✍️），cover 设为 "none"。

### 7. 一次性 update 属性 + 设置 Icon/封面

在 `notion_update_page`（command=update_properties）中同时传入：

```json
{
  "名称": "<信息源名称>",
  "首选网址": "<用户给的原始URL>",
  "类型": "认知成长" / "解决问题",
  "关注状态": "正在关注",
  "来源": ["<平台>"],
  "付费模式": "免费" / "含付费" / "订阅制" / "会员制" / "买断制",
  "更新频率": "日更" / "周更" / "月更" / "不定期",
  "标签": ["<标签1>", "<标签2>"],
  "内容风格": "造东西的人" / "说清楚的人" / "点燃型",
  "语言": "中文" / "英文",
  "简介": "<一句话描述>",
  "主题": ["<主题URL>"],
  "人物": ["<人物URL>"]
}
```

同时在同一个调用中设置：
- `icon`: `<头像直链URL>` 或 emoji 字符
- `cover`: `<封面直链URL>` 或 `"none"`

新页面只写本次记录明确提供的值；未提供的可选字段留空，不沿用其他记录的属性或正文。
- `信息` → null（Matt Wolfe 的旧信息条目）
- `主题` → 覆盖为新主题（如果没找到新主题则置 null）
- `人物` → 覆盖为新人物（如果没找到则置 null）
- `备用网址` → null（Matt Wolfe 的 RSS feed 链接）
- `次选网址` → null

### 8. 清空页面正文

新页面只写本次记录明确提供的值；未提供的可选字段留空，不沿用其他记录的属性或正文。

### 9. 验证

`notion_fetch` 新记录，确认：
- parent-data-source = 信息源
- 名称、首选网址、类型、来源等属性落库
- Icon 和封面已设置
- 旧 relation 已清理
- 主题/人物关联正确

向用户报告填了什么，哪些留空待补充。

## 不碰

- **公式字段**（介绍、信息数、学习、学习时长/h、学习进度、文章数、视频数）：Notion 自动算
- **备用网址/次选网址**：默认清空，不自动填 RSS

## 边界

- 链接无法抓取 → 告诉用户链接打不开，让用户确认名称
- 人物搜不到 → 不创建，留空
- 主题搜不到 → 不创建，留空
- 付费模式不确定 → 默认"含付费"
- 内容风格判断不准 → 选最接近的，在报告里说明让用户确认
- 头像/封面图搜不到 → icon 用平台 emoji（YouTube→📺、B站→📺、公众号→💬、播客→🎙️、Newsletter→📧、博客→✍️），cover 设为 none
