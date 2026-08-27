# AI Life OS Skill 套件

版本：`2.0.0`

本仓库合并了成长系统和商业系统，共 18 个功能 Skill，以及 1 个内容创作共享依赖。所有 Skill 共用 `ai-life-system-init` 建立的 Runtime；学员只需初始化一次，不需要分别配置数据库。

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

## 安装

本仓库只发布 Skill 文件，不包含任何 Notion 数据库、页面内容或个人配置。学员可以直接执行下面两条命令：

```bash
git clone https://github.com/gjl2002/AI-Life-OS.git "$HOME/.ai-life-os"
"$HOME/.ai-life-os/install.sh"
```

安装脚本会将 19 个 Skill/共享依赖复制到当前用户的：

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
