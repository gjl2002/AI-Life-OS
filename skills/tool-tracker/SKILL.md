---
name: tool-tracker
description: 管理工具库到 Notion「工具箱」数据库。当用户说"加个工具""我用了XX这个工具""帮我记一下XX""这个工具加个logo"等场景时使用。自动搜索工具logo作为页面图标、生成一句话用途说明、判断使用场景、设置状态。
---
## 用户自己的 Notion 接入

本 Skill 使用 `$ai-life-system-init` 定位用户自己的 Notion 结构。执行前先运行 `scripts/runtime.py status`；状态为 `needs_init` 时先引导用户完成初始化。对本次操作涉及的每个概念运行 `scripts/runtime.py resolve --concept <key>`，只使用 Runtime 返回的目标 Data Source ID。读取该 Data Source 的实时 Schema，并在写入前运行 `scripts/runtime.py check-write` 校验本次属性、选项和 relation。

概念映射：`ai_toolbox, sop`。

创建时必须让当前 Notion connector 将新页面的 parent 指向已解析的 Data Source；写入后回读确认 parent 和属性。若概念未找到、结构不兼容、候选不唯一或 connector 无法确认 parent，应停止该写入并说明原因，不得猜 ID、扫描无关空间或复制已有个人记录。以下正文中的数据库路径、字段名、选项和默认值若与用户实时 Schema 不一致，均视为示例而非要求；只有语义和字段类型明确匹配时才映射，否则询问或安全停止。仅读取本次任务所需的数据；不得将用户本地索引、凭据、页面 ID 或个人样例打包发布。

# Tool Tracker — Notion 工具箱

## 数据库


**场景选项**（multi_select，不新建）：AI协作、学习、知识管理、创作、商业、效率

**状态选项**（status）：主力、辅助、备用、停用

## 场景一：新增工具

用户说"加个工具XX""我在用XX这个工具""帮我记一下XX"。

### 执行流程

1. 在 Runtime 已解析的用户 Data Source 中直接创建新记录；不复制现有记录。

2. **搜索工具 logo**（按优先级）：
   - **第一优先**：`image_search` 搜 `"<工具名>" logo icon 官方`，选清晰的方形 logo
   - **第二优先**：如果搜不到官方 logo，且用户给了工具链接，抓取该网页 HTML，找 `<link rel="icon">` 或 `<link rel="apple-touch-icon">` 的 href，拼接成完整 URL 直接用作 icon
   - **第三优先**：都找不到，用工具首字母 emoji 代替
   - 追踪直链：`curl -sL -o /dev/null -w "%{url_effective}" "<短链>"`

3. **判断字段**：
   - **一句话用途**：根据工具功能写一句简短说明（为什么留着、什么时候用）
   - **状态**：按用户明确说明和实时 Schema 填写；无法判断时留空，不推断为常用或主力。
   - **场景**：根据工具功能选：
     - AI相关（ChatGPT/Claude/Cursor等）→ AI协作
     - 笔记/知识管理（Notion/Obsidian/Flomo）→ 知识管理
     - 截图/录屏/启动器（Raycast/iShot）→ 效率
     - 视频/图片/写作 → 创作
     - 学习/翻译/阅读 → 学习
     - 付费/推广/接单 → 商业
   - **链接**：用户给了就填，没给留空

4. **一次性 update + 设置 icon**：

```json
{
  "工具": "<工具名>",
  "链接": "<URL或null>",
  "一句话用途": "<一句话说明>",
  "状态": "主力",
  "场景": ["<场景1>", "<场景2>"]
}
```

同时在同一调用中传 `icon` = logo 直链 URL（或 emoji）。

新页面只写本次记录明确提供的值；未提供的可选字段留空，不沿用其他记录的属性或正文。

5. **验证**：fetch 新记录确认落库。

## 场景二：补 logo

用户说"给这个工具加个logo""XX的图标怎么是空的"。

### 执行流程

1. 用 `notion_ai_search`（data_source_url=工具箱）按工具名搜
2. 找到后按优先级找 logo：
   - `image_search` 搜该工具官方 logo
   - 搜不到 → 抓工具链接网页 HTML，找 `<link rel="icon">` 或 `<link rel="apple-touch-icon">` 的 favicon
   - 都找不到 → 用 emoji 兜底
3. 追踪直链 → `notion_update_page` 传 `icon` = logo 直链
4. 告诉用户已补上

## 不碰

- **SOP流程**：用户自己建，不自动关联
