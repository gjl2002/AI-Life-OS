# AI Life OS Skill 套件

版本：`2.2.0`

AI Life OS Skills 帮你把目标、内容创作和日常生活工作流接入自己的 AI 助手。本版本包含 36 个功能 Skill，以及 1 个内容创作共享依赖。需要 Notion 数据的 Skill 共用 `ai-life-system-init`；学员只需连接并初始化自己的 Notion 一次，不需要逐个配置数据库。

## 成长系统

1. `ai-life-system-init`：初始化、重新绑定、健康检查和 Runtime 索引。
2. `life-positioning-coach`：人生定位教练。
3. `goal-planner`：目标教练。
4. `question-clarification-coach`：问题澄清教练。
5. `question-synthesis-coach`：问题综合教练。
6. `stuck-point-insight-coach`：卡点洞察教练。
7. `information-source-daily-briefing`：信息源日报。
8. `sop-builder`：SOP 构建。

## 商业系统

1. `commercial-positioning-coach`：商业定位教练。
2. `user-avatar-coach`：用户画像教练。
3. `product-opportunity-coach`：产品机会教练。
4. `product-architecture-coach`：产品架构教练。
5. `product-experience-coach`：产品体验教练。
6. `course-handout-writing-coach`：课程讲义写作教练。
7. `product-detail-page-design`：产品详情页设计教练。
8. `wechat-article-writing-coach`：公众号创作教练。
9. `wechat-moments-writing-coach`：朋友圈创作教练。
10. `xiaohongshu-native-note-coach`：小红书创作教练。

## 共享依赖

- `humanizer-zh`：为内容创作 Skill 提供通用的去 AI 味检查。

## 生活记录、知识与行动 Skills

这些 Skills 把你用自然语言说的记录和请求整理到你自己的 Notion 中。你可以只安装需要的能力，也可以按场景组合使用。

### 生活记录

| Skill | 能做什么 | 什么时候用 |
|---|---|---|
| `inbox-capture` | 快速收下灵感、想法、语音转写和临时待办，不要求先分类。 | “记一下：周末研究下家庭预算。” |
| `emotion-tracker` | 整理你讲述的情绪和事件，保存为情绪记录。 | “今天开会后很挫败，帮我记录下。” |
| `health-tracker` | 记录体重、腰围等你明确提供的身体数据。 | “今天体重 62 公斤。” |
| `food-tracker` | 记录吃了什么；提供照片时可协助识别食物并整理营养信息。 | “记录午饭：鸡胸肉、米饭和西兰花。” |
| `life-moment-tracker` | 保存重要经历、转折、高光、低谷或觉察，并在合适时关联目标或故事线。 | “记下今天第一次独立做完产品发布。” |
| `travel-tracker` | 整理旅行愿望、计划、逐日行程、地点和旅行支出。 | “帮我计划 3 天成都行，周五出发。” |

### 知识与内容

| Skill | 能做什么 | 什么时候用 |
|---|---|---|
| `info-collector-notion` | 从文章、视频、社交平台或网页链接提取信息，整理后保存到信息库。 | 发一个链接并说“收进信息库”。 |
| `info-backfill` | 检查已有信息记录，补齐能从原文确认的作者、平台、类型等资料。 | “帮我看看刚保存的信息还有什么字段没补。” |
| `source-tracker` | 记录值得持续关注的作者、频道、播客和网站等信息源。 | “把这个播客加入我的信息源。” |
| `book-tracker` | 记录想读、在读或读完的书，查找资料并尝试关联已有作者页面。 | “我开始读《深度工作》，帮我记一下。” |
| `film-tracker` | 记录看过、正在看、想看或弃看的电影、剧集、动漫等作品。 | “昨晚看完《沙丘》，记到观影记录里。” |

### 物品与工具

| Skill | 能做什么 | 什么时候用 |
|---|---|---|
| `item-tracker` | 记录衣物、数码产品和其他物品；收到礼物时可按你的要求关联送礼人和礼物。 | 发商品链接或照片，说“帮我记下这件东西”。 |
| `wardrobe-tracker` | 专门记录衣物信息，例如品牌、品类、颜色、尺码、价格和图片。 | “记一下这件新外套，品牌是……” |
| `tool-tracker` | 整理 AI、创作、学习和效率工具，记录用途、链接和使用状态。 | “把这个 AI 工具加到工具箱。” |
| `reward-tracker` | 记录给自己的奖励，以及奖励的兑换或使用情况；可在结构匹配时关联目标。 | “完成这个目标后奖励自己一次按摩。” |

### 行动与财务

| Skill | 能做什么 | 什么时候用 |
|---|---|---|
| `task-tracker` | 快速记录任务和待办，整理日期、项目等信息；也可辅助提取截图中的任务。 | “提醒我明天下午给客户发方案。” |
| `expense-tracker` | 记录支出、收入、账户转账、订阅和报销，并在你的财务结构支持时关联分类或报表。 | “午饭 38 元，记一笔。” |
| `season-sync` | 将个人 12 周赛季与选定的游戏、体育或活动赛季对齐，核实官方赛季名与海报后更新自己的复盘记录。 | “把这轮 12 周赛季同步到王者荣耀最新正式服赛季。” |

这些 Skills 使用你自己连接的 Notion 结构。若无法确认目标数据库或字段，Skill 会先提醒你，不会套用发布者的页面或个人记录。身体、财务和情绪等信息由你决定是否记录。

## 安装

本仓库只发布 Skill 文件，不包含任何 Notion 数据库、页面内容或个人配置。学员可以直接执行下面两条命令：

```bash
git clone https://github.com/gjl2002/AI-Life-OS.git "$HOME/.ai-life-os"
"$HOME/.ai-life-os/install.sh"
```

安装脚本会将 37 个 Skill/共享依赖复制到当前用户的：

```text
~/.codex/skills/
```

如果已经下载仓库，也可以在仓库目录运行：

```bash
./install.sh
```

复制完成后重新打开 Codex，或新建一个任务。

## 首次使用

安装本身不需要 Notion。需要使用 Notion-backed 能力时：

1. 在 Codex 中连接学员自己的 Notion。
2. 确保学员自己的模板 Hub 已分享给当前 Notion 连接。
3. 运行 `$ai-life-system-init`，完成一次初始化。
4. 初始化成功后，直接使用其余成长系统和商业系统 Skill。

初始化生成的个人配置默认位于 `~/.ai-life-system/`。该目录只属于当前学员，不应上传、分享或放回课程套件。

## 数据边界

- 云端 Notion 是个人记录和页面内容的事实来源。
- 本地 Runtime 索引只保存数据库结构、字段、选项和路由信息。
- 套件不包含发布者或学员的 Notion ID、页面内容、token、邮箱及个人配置。
- 云端不可用时，具体 Skill 不使用本地导出或同步副本冒充实时资料。
- 商业系统公开导出不包含发布者个人样稿、账号数据、私域内容或个人文风语料。

## 更新

用新版本仓库重新运行 `install.sh` 即可。模板结构发生变化时，再运行一次 `$ai-life-system-init`。

## 去重与版本说明

- 成长系统中与仓库已有的同名 Skill 保留已接入 Runtime 的较新版本，未用旧导出覆盖。
- 商业系统新增 10 个 Skill。
- `ai-life-system-init` 只保留一份，采用包含成长系统、商业系统和普通页面发现能力的新版。
- 不复制导出目录中的 `.DS_Store`、Notion 数据、同步 Markdown 或个人配置。
