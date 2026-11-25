# AI 人生系统底座 Skill

版本 `1.4.0`

一个 Skill 同时完成两件事：首次读取学员自己的 Notion 模板，从所选成长或生活入口递归发现子页面、数据库及全部 Data Source，为目标、任务、复盘等 Skill 提供统一的 Notion 定位和写入前校验。不需要再安装单独的 `notion-life-system`。

发布包不会包含任何学员的 Notion 数据、数据库 ID 或个人记录。

## 安装

按[套件的多平台安装说明](https://github.com/gjl2002/AI-Life-OS#选择你的-agent)导入完整的 `ai-life-system-init` 文件夹或单 Skill ZIP，保留 `scripts/` 和 `references/`。供其他 Skill 调用时，确认当前 Agent 能访问该包实际所在目录。

## 使用

确认当前 Agent 能读取你授权的 Notion 页面和 Data Source，能运行 Python 3，并允许在你的环境中建立本地索引。通过平台的技能入口调用 `ai-life-system-init`，或发「请使用 ai-life-system-init 初始化我的 AI 人生系统」。

选择成长系统、生活系统或两者，并提供对应的 Notion 页面链接。多个模块可共用一个 Hub。系统沿已选模块的实际子页面递归发现，以只读方式核验 Notion 结构。

## 其他 Skill 如何接入

在 `ai-life-system-init` 实际安装目录中运行 Runtime。

```text
python3 scripts/runtime.py status
python3 scripts/runtime.py resolve --concept task
python3 scripts/runtime.py resolve --concept life_positioning
```

数据库写入前调用 `check-write` 校验真实 Data Source、字段和选项；普通页面正文更新前调用 `check-page-write` 校验页面身份。Runtime 只做结构解析与本地预检，不会替业务 Skill 写入 Notion，也不代表用户已经授权。

在同一运行环境完成一次初始化后，其他 Skill 可以共享这份索引。以后模板发生变化时重新运行，所有接入它的具体 Skill 会读取新索引，无需逐个重新配置。

## 生成的本地文件

初始化结果默认保存在：

```text
~/.ai-life-system/
```

其中 `notion-index.json` 是事实索引，包含数据库、字段、选项、Relation 和查找表；`dimension-pages.json` 保存系统入口与核心普通页面的身份，不保存正文；`semantic-map.json` 只记录实际找到的概念。后续 Skill 应优先调用 `scripts/runtime.py`，不要重复实现解析逻辑。

注意：`~/.ai-life-system/` 属于学员个人本地状态，不要把它上传 GitHub、放进课程 ZIP 或分享给其他学员。

## 设计特点

- 以学员当前 Notion 页面为事实来源，不要求所有人使用完全相同的数据库名称。
- 在所选模块入口内沿实际子页面递归，按源 ID 合并多个视图对同一数据源的引用。
- “待办”可以是字段选项，“专注”可以出现在多个数据库字段中，不会被误判成独立数据库。
- 初始化与业务动作分离：初始化只建立索引；Runtime 负责结构解析和预检；具体 Skill 负责业务逻辑与获得授权后的实际动作。
- 如果模板发生变化，可以重新运行 Skill；旧本地配置会自动备份。
