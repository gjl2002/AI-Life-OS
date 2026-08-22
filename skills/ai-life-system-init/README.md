# AI 人生系统底座 Skill

版本：`1.1.0`

一个 Skill 同时完成两件事：首次读取学员自己的 Notion 模板并建立本地动态索引；为目标、任务、复盘等具体 Skill 提供统一的目标解析和写入前校验。不需要再安装单独的 `notion-life-system`。

发布包不会包含任何学员的 Notion 数据、数据库 ID 或个人记录。

## 安装

解压后，将整个 `ai-life-system-init` 文件夹放到：

```text
~/.codex/skills/
```

最终目录应为：

```text
~/.codex/skills/ai-life-system-init/SKILL.md
```

然后重新打开 Codex 或新建一个对话。

## 使用

先确保 Codex 已连接 Notion，并且学员的模板 Hub 已分享给当前连接。然后输入：

```text
$ai-life-system-init
```

当 Skill 找到多个候选 Hub 时，让学员选择自己的模板总入口；不要选择普通课程说明页。

初始化只读 Notion，不会创建、修改、移动或删除页面和数据库记录。

## 其他 Skill 如何接入

具体 Skill 先调用本包中的 Runtime：

```text
python3 ~/.codex/skills/ai-life-system-init/scripts/runtime.py status
python3 ~/.codex/skills/ai-life-system-init/scripts/runtime.py resolve --concept task
```

写入前再调用 `check-write` 校验真实 Data Source、字段和选项。Runtime 只做结构解析与本地预检，不会替业务 Skill 写入 Notion，也不代表用户已经授权。

学员只需运行一次 `$ai-life-system-init`。以后模板发生变化时重新运行，所有接入它的具体 Skill 会读取新索引，无需逐个重新配置。

## 生成的本地文件

初始化结果默认保存在：

```text
~/.ai-life-system/
```

其中 `notion-index.json` 是事实索引，包含数据库、字段、选项、Relation 和查找表；`semantic-map.json` 只记录实际找到的概念。后续 Skill 应优先调用 `scripts/runtime.py`，不要重复实现解析逻辑。

注意：`~/.ai-life-system/` 属于学员个人本地状态，不要把它上传 GitHub、放进课程 ZIP 或分享给其他学员。

## 设计特点

- 以学员当前 Notion 页面为事实来源，不要求所有人使用完全相同的数据库名称。
- “待办”可以是字段选项，“专注”可以出现在多个数据库字段中，不会被误判成独立数据库。
- 初始化与业务动作分离：初始化只建立索引；Runtime 负责结构解析和预检；具体 Skill 负责业务逻辑与获得授权后的实际动作。
- 如果模板发生变化，可以重新运行 Skill；旧本地配置会自动备份。
