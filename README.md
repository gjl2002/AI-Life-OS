# AI 人生系统 Skill 套件

版本：`1.1.0`

本套件包含 1 个 Notion 初始化底座和 7 个具体能力 Skill。学员只需初始化一次，后续 Skill 会共同读取学员本机的结构索引，不需要分别配置数据库。

## 包含的 Skill

1. `ai-life-system-init`：初始化、重新绑定、健康检查和 Runtime 索引。
2. `life-positioning-coach`：人生定位教练。
3. `goal-planner`：目标教练。
4. `question-clarification-coach`：问题澄清教练。
5. `question-synthesis-coach`：问题综合教练。
6. `stuck-point-insight-coach`：卡点洞察教练。
7. `information-source-daily-briefing`：信息源日报。
8. `sop-builder`：SOP 构建。

## 安装

本仓库只发布 Skill 文件，不包含任何 Notion 数据库、页面内容或个人配置。学员可以直接执行下面两条命令：

```bash
git clone https://github.com/gjl2002/AI---.git "$HOME/.ai-life-system-skill-suite"
"$HOME/.ai-life-system-skill-suite/install.sh"
```

安装脚本会将 8 个 Skill 复制到当前用户的：

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
4. 初始化成功后，直接使用其余 7 个 Skill。

初始化生成的个人配置默认位于 `~/.ai-life-system/`。该目录只属于当前学员，不应上传、分享或放回课程套件。

## 数据边界

- 云端 Notion 是个人记录和页面内容的事实来源。
- 本地 Runtime 索引只保存数据库结构、字段、选项和路由信息。
- 套件不包含发布者或学员的 Notion ID、页面内容、token、邮箱及个人配置。
- 云端不可用时，具体 Skill 不使用本地导出或同步副本冒充实时资料。

## 更新

用新版本的 8 个 Skill 文件夹覆盖旧文件夹即可。模板结构发生变化时，再运行一次 `$ai-life-system-init`。
