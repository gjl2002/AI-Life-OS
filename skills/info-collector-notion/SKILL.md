---
name: info-collector-notion
description: >
  支持平台：微信公众号文章、小红书图文笔记（图片长文 OCR）、即刻帖子、B站、通用网页。
  用户发送任意链接，自动识别平台类型，抓取标题/作者/正文/时长/字数，用 notion_create_pages 创建信息页，
  字段对齐信息库 schema（信息/作者/来源/平台/类型/字数/时长/摘要/状态）。
  触发词：发送链接、收藏文章、保存到知识库、存到信息库、抓取这条、信息收集。
---
## 用户自己的 Notion 接入

本 Skill 使用 `$ai-life-system-init` 定位用户自己的 Notion 结构。执行前先运行 `scripts/runtime.py status`；状态为 `needs_init` 时先引导用户完成初始化。对本次操作涉及的每个概念运行 `scripts/runtime.py resolve --concept <key>`，只使用 Runtime 返回的目标 Data Source ID。读取该 Data Source 的实时 Schema，并在写入前运行 `scripts/runtime.py check-write` 校验本次属性、选项和 relation。

必要概念为 `information`。仅在目标实时 Schema 支持对应关系时，按需解析 `information_source` 和 `question`。

创建时必须让当前 Notion connector 将新页面的 parent 指向已解析的 Data Source；写入后回读确认 parent 和属性。若概念未找到、结构不兼容、候选不唯一或 connector 无法确认 parent，应停止该写入并说明原因，不得猜 ID、扫描无关空间或复制已有个人记录。以下正文中的数据库路径、字段名、选项和默认值若与用户实时 Schema 不一致，均视为示例而非要求；只有语义和字段类型明确匹配时才映射，否则询问或安全停止。仅读取本次任务所需的数据；不得将用户本地索引、凭据、页面 ID 或个人样例打包发布。

# 信息收集自动化 → Notion 信息库

## 概述

用户从任意渠道发来一个链接，自动识别内容平台，抓取标题、作者、正文、时长等信息，直接创建为
Notion「信息」数据库中的一条记录（状态=收集），而不是写入本地 Obsidian。

对标：松月的信息收集工作流 + 用户自己的 info-backfill（本技能负责「抓取入库」，info-backfill 负责「补全字段」）。

## 目标数据库（示例 Schema；运行时以用户当前 Schema 为准）

- 使用连接器支持的 Data Source parent、实际属性名和 Notion Markdown 正文创建信息页。

## 字段映射（重要）

| 信息库字段 | 类型 | 抓取来源 | 说明 |
|---|---|---|---|
| `信息` | title | 标题 | 必填，页面标题 |
| `作者` | text | 作者名 | 公众号 og:article:author / 小红书 author / 即刻 author |
| `来源` | url | 原文链接 | 必填，用户发的原始 URL |
| `平台` | select | URL 识别 | B站/小红书/YouTube/直播公开课/公众号/个人博客/知得少 |
| `类型` | select | 内容类型 | 视频/文章/播客/图文/帖子/网页 |
| `字数 (个)` | number | 正文长度 | 文章/图文类：fetch 正文后估算，JavaScript number |
| `时长 (min)` | number | 视频/播客 | **必须抓实际时长**，不能只靠标题猜 |
| `摘要` | text | 正文开头 | 截取正文前 ~200 字，或视频描述 |
| `状态` | status | — | 新建一律 `收集`（info-backfill 只处理收集/学习，别设其他值） |
| `信息源` | relation | 作者/频道名 | 在信息源库 `ai_search` 匹配，找到就关联，找不到不新建 |
| `要解决的问题` | relation | 内容主题 | 在问题库 `ai_search` 匹配，找到就关联，找不到不新建 |

**不填的字段**：信息ID、标签、场景、所需精力、计划阅读等留给用户或后续流程，抓取时不要乱填。

## 输入处理

当用户发送一个 URL 时，按以下规则识别平台：

| URL 特征 | 平台 | 类型 | 处理方式 |
|----------|------|------|----------|
| `mp.weixin.qq.com` | 公众号 | 文章 | 脚本抓取 → 正文+字数 |
| `xiaohongshu.com` | 小红书 | 图文 | 脚本判断 is_video → 图文(图片长文 OCR) / 视频(仅标题/描述/时长，不转录) |
| `okjike.com` | 即刻 | 帖子 | 脚本抓取 → 正文+字数 |
| `bilibili.com` / `b23.tv` | B站 | 视频 | web_fetch 抓标题/UP主，**抓实际时长** |
| `youtube.com` / `youtu.be` | YouTube | 视频 | web_fetch（用 m.youtube.com），抓实际时长 |
| 其他链接 | — | 网页 | web_fetch 抓标题/正文 → 网页 |

## 执行流程

### 通用步骤

1. 核实标题、作者、发布日期、原文 URL 和能读取的正文。用户请求收藏原文且内容可完整读取并允许保存时，保留原文段落和小标题。只拿到片段、简介或受访问限制时，标明已取得的范围。
2. 用来源 URL 在用户的目标 Data Source 检查是否已有记录。有唯一记录时返回该页，只有用户明确提出更新才编辑现有内容。
3. 对用户库中支持的 relation，按作者或频道匹配已有信息源。按内容主题匹配用户的已有问题，只有语义吻合且候选唯一时才关联。缺失或有歧义时留空并说明，避免新建无关记录。
4. 组装经过 Runtime 预检的属性与正文。对原文中有助于理解的封面或少量关键插图，优先通过当前连接器支持的上传流程取得稳定引用，再按 Notion Markdown 规范嵌入。上传不可用时可保留已核实的图片链接，并说明保存范围。
5. 在目标 Data Source 创建页面。回读核对 parent、来源 URL、正文及实际写入的配图和关系。返回记录链接，并说明仅保存了片段、图片未嵌入或关系待确认等实际缺口。

### 流程 A：公众号文章（mp.weixin.qq.com）

```bash
python3 scripts/wechat_scraper.py "https://mp.weixin.qq.com/s/xxx"
```

脚本返回 `title`、`author`、`text` 和 `images`。每个成功取得的图片项含 `index`、`url` 和 `base64` 数据 URI。选取关键图片时使用对应 URL 或将数据解码成临时文件，通过连接器上传。平台及类型以用户实际选项为准。

### 流程 B：小红书（xiaohongshu.com）

**URL 必须带 `xsec_token`**（从 APP 分享链接复制），否则 `noteDetailMap` 为空抓不到。

```bash
python3 scripts/xhs_scraper.py "https://www.xiaohongshu.com/discovery/item/xxx?xsec_token=xxx"
```

- `is_video: false` → 图文：title/author/text/images。若 desc 很短但图片多（≥3张），正文在图片里 → **必须 OCR**：
  ```bash
  python3 scripts/ocr_images.py "<images_dir>"
  ```
  平台=小红书，类型=图文。
- `is_video: true` → 视频：JSON 返回 title/author/text（描述）+ video_url。**不转录**，只用描述做摘要，时长若能从 JSON 或页面拿到则填，拿不到留空待补。平台=小红书，类型=视频。

### 流程 C：即刻帖子（okjike.com）

```bash
python3 scripts/jike_scraper.py "https://web.okjike.com/u/xxx/post/xxx"
```

title/author/text 入 content，平台=知得少（或最接近的选项），类型=帖子。

### 流程 D：B站 / YouTube 视频

- B站：`web_fetch` 页面，snippet query `"时长 分钟 duration"`，拿标题、UP主、时长。
- YouTube：从视频页面或可靠的官方元数据核实时长。只有章节起始时间时，时长留空待补。
- 平台=B站/YouTube，类型=视频，`时长 (min)` 用 JavaScript number。

### 流程 E：通用网页

`web_fetch` 抓标题+正文，平台留空或归入「个人博客」，类型=网页，字数估算。

## 与 info-backfill 的分工

- **本技能（抓取入库）**：新链接来了，抓取 → 创建信息页，状态=收集，尽量填全基础字段。
- **info-backfill（补全）**：批量扫「收集/学习」状态，补信息源 relation、要解决的问题 relation、时长/字数验证。
- 抓完一批后建议顺手跑一次 backfill 补关联，形成闭环。

## 注意事项

- 小红书 URL 必须带 `xsec_token`；请求用 Chrome UA（脚本已内置）。
- 公众号图片由脚本从 `data-src` 获取。正文使用稳定媒体引用或已核实的图片链接。
- OCR 依赖 `rapidocr-onnxruntime`（仅在实际需要 OCR 时使用）；**不需要 whisper/视频转录**。
- 所有数字字段（时长/字数）用 JavaScript number，不是字符串。
- relation 字段传页面 URL 数组。
- 已有记录默认返回原页。用户要求更新既有页时，只调整本次明确要求的内容和属性。
