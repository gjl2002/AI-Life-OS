---
name: ai-life-system-init
description: "初始化、重新绑定、健康检查并为其他 Skill 提供学员自己的 AI 人生系统 Notion 运行时底座。开始时由用户选择要连接的成长和生活模块，可提交一个或多个模块页面；从已选入口递归发现子页面、数据库及全部 Data Source，再建立本地结构索引。适用于首次连接、重新复制模板、切换工作区、页面或 Schema 变化，以及其他 AI 人生系统 Skill 需要定位真实 Notion 结构时。"
---

# AI 人生系统底座

## 目标与边界

把学员当前 Notion 模板的真实结构建立为本地事实索引，并为其他具体 Skill 提供统一的结构解析和写入前校验。Notion 实际读取结果是事实来源；本 Skill 不用预设数据库名单验收模板，也不把未出现的概念报告为缺失。

初始化、重新绑定和健康检查只读 Notion。`runtime` 只解析本地索引并预检，不自行执行业务写入。不要要求用户把 Notion token 粘贴到聊天中。

```text
用户选择成长系统、生活系统或两者，并提供入口链接
  -> 从每个已选模块入口递归发现页面、数据库及视图
  -> 发现实际数据库和 Data Source
  -> 读取实时 Schema
  -> 建立标题、字段、选项和 relation 索引
  -> 添加仅针对已发现对象的语义映射
  -> 校验、只读冒烟测试和报告
```

## 模式

- `initialize`：首次绑定，没有可用本地索引。
- `rebind`：用户更换工作区、重新复制模板或明确要求重新绑定。
- `health-check`：已有索引，只检查已连接模块入口与已索引对象；发现变化后转为 `rebind`。
- `runtime`：为目标、任务、复盘等具体 Skill 解析真实 Data Source、字段和选项，并在写入前执行本地预检。

本 Skill 负责结构，不负责业务含义：具体 Skill 决定“做什么”、组织内容、获取用户授权并调用 Notion；本 Skill 决定“写到哪里”、暴露歧义并检查本次字段是否安全。不要用本 Skill 单独生成或录入目标、任务、笔记或复盘。

## 本地状态

默认目录为 `~/.ai-life-system/`，可用 `AI_LIFE_SYSTEM_DATA_DIR` 覆盖。维护：

- `profile.json`：工作区、已选模块、模块入口、索引版本和健康状态；
- `discovery.json`：本次发现的候选、来源和失败证据；
- `notion-index.json`：后续 Skill 的主要入口，包含 Data Source、属性、选项、relation、访问能力和查找表；
- `semantic-map.json`：只保存实际匹配到的概念，不保存 `missing` 条目；
- `notion-schema.json`、`routing-rules.json`：兼容旧版消费者；
- `dimension-pages.json`：已连接模块入口及其实际子页面的非数据库页面映射；
- `initialization-report.md`：实际索引、已识别语义和真实故障；
- `backups/`：重新生成前的旧配置备份。

这些文件属于当前用户，不得放入共享 Skill、ZIP、GitHub 或课程资料。详细格式见 [index-format.md](references/index-format.md) 和 [profile-format.md](references/profile-format.md)。

## 初始化流程

### 1. 确认模块与入口链接

1. 使用当前环境已连接的 Notion 工具确认工作区和只读能力。
2. 先确认用户要连接成长系统、生活系统，还是同时连接两者。
3. 让用户发送所选模块对应的 Notion 页面链接。可以逐个给不同页面，也可以说明多个模块都在同一个 Hub/总页面中并只提供该页面一次。若用户只提供一个页面但没有说明它代表哪些模块，先确认关联模块。使用连接器返回的规范页面 URL 或 ID 核验入口。
4. 读取每个已选入口以确认页面身份和可读状态。入口不能读取时，保留其他可读模块并报告具体受影响的模块；所有已选入口都不可读时停止。

已有配置可以继续为成长与生活 Skill 提供索引。重新初始化或重新绑定时，按用户确认的成长或生活入口建立索引。即使共享 Hub 还有其他模块，也只展开已选模块对应的页面或选项卡。

### 2. 动态发现

1. 从已选模块的独立页面或共享 Hub 内已确认的模块页面/选项卡开始。共享 Hub 只用于定位这些入口。入口的归属不明确、页面结构未完整返回或找不到对应选项卡时，请用户提供模块页或目标数据源链接，并在报告中说明覆盖限制。
2. 在每个已选入口内递归读取实际子页面，直到没有新的子页面。可遍历分栏、选项卡及折叠等布局容器来定位内容。遇到明确属于其他模块的入口时停止该分支。按规范化 page ID 去重并保留最短发现路径。遇到分页或截断时继续读取可取得的部分，并标记仍有缺口的分支。
3. 每页定位数据库容器与已保存视图。沿视图元数据核实原始数据库和 Data Source。只索引属于已选范围的原始库，跨模块归属不明时请用户核实。同一个 Data Source 只挂在原始数据库下，多个页面或视图的引用作为来源证据。对每个已纳入的原始库读取全部 Data Source。
4. 递归只跟随实际页面子级。普通链接、提及、Relation、数据库记录和工作区搜索结果不扩大遍历范围。普通页面索引只保存身份和结构元数据。手动补充的目标必须在已选范围内核实。

详见 [discovery-format.md](references/discovery-format.md)。

### 3. 读取实时 Schema

读取每个数据库容器及其全部 Data Source。数据库容器标题与 Data Source 标题必须分别记录；`data_sources[].title` 使用工具返回的 Data Source 自身标题，不能用容器标题代替。多 Data Source 容器必须逐项保存独立 ID、标题和 Schema，不能只保存当前视图或第一项。记录最后编辑时间、属性名称与类型、select/status 选项、relation 目标，以及 formula、rollup 等只读性质。单个对象失败时保留其他成功结果；不用名称猜 ID，不用本地 Markdown 镜像代替云端 Schema。

按 [discovery-format.md](references/discovery-format.md) 写临时发现 JSON。只包含结构元数据，不包含数据库记录正文、邮箱、token 或密钥。

### 4. 生成索引

读取 [semantic-aliases.json](references/semantic-aliases.json) 和 [semantic-mapping.md](references/semantic-mapping.md)，从 Skill 根目录运行：

```bash
python3 scripts/build_config.py --discovery <临时发现文件> --output-dir <本地状态目录>
python3 scripts/validate_config.py --config-dir <本地状态目录>
```

生成器负责去重、结构指纹、查找表、字段访问判断、语义映射、报告、备份和原子替换。不要手工拼接最终 JSON。

语义别名只是查找捷径，不是模板契约：只有实际匹配的概念才进入 `semantic-map.json`。普通页面可映射为 `kind: page`，例如 `life_positioning` 指向用户自己的《愿景定位》；`待办` 可以映射到字段选项，`专注` 可以映射到多个数据库字段；它们不得被假设为独立数据库。

### 5. 只读冒烟测试

从实际索引中选择少量用户当前需要的数据源执行最小只读查询。查询成功但零记录仍为成功。不得通过创建记录测试连接。

### 6. 汇报

只摘要工作区、用户选择的模块、各模块入口的可读状态、实际数据库/Data Source 数量、读取失败、relation 警告、语义多目标和本地索引目录。对未选择模块说明“未连接/未扫描”，不得说成模板缺失；不要把完整 Schema 或私人记录正文贴进聊天。

## 后续 Skill 如何使用

1. 读取 `profile.json` 找到 `notion-index.json` 和 `semantic-map.json`。
2. 优先按语义 key 查找；不存在时按 `lookup.page_titles`、`source_titles`、`property_names`、`option_names` 查询真实名称。
3. 多目标结果必须结合当前任务上下文选择；上下文不足时让用户确认，不能静默取第一个。
4. 读取只需确认 `access.read_ready`。任何写入都必须按 [action-validation.md](references/action-validation.md) 对目标 Data Source 和本次字段逐项校验；初始化成功不等于所有字段都可写。

## 健康检查与停止条件

比较各已选模块入口、已索引页面的父子关系及 Data Source 的 `last_edited_time` 和 `schema_fingerprint`。发生入口变化、核心页面被替换、工作区变化、指纹变化、配置校验失败或用户明确要求时重新绑定。普通页面仅正文变化时，业务 Skill 重新读取云端最新正文，不要求重新初始化。

- 所有已选入口不可读或没有任何可用 Schema：`blocked`。
- 部分已选模块入口不可读：其他模块照常建立索引，整体为 `needs_attention`，报告无法读取的模块。
- 未选择的模块不参与健康检查，也不构成缺失或故障。
- 个别 Data Source 不可读、页面树发现不完整或只读冒烟测试失败，标记为 `needs_attention` 并报告受影响路径。
- relation 目标未解析：允许读取，相关字段禁止自动写入并给出警告。
- 某个语义概念未匹配：不构成故障，也不写入 `missing`。
- 某个普通页面不可读：`needs_attention`；只阻止依赖该页面的业务动作，不使其他已解析目标失效。
- 生成或校验失败：保留旧配置，不留下半份新配置。

详细失败处理见 [failure-modes.md](references/failure-modes.md)。

## Runtime 流程

其他具体 Skill 需要访问 AI 人生系统时，先阅读 [runtime-protocol.md](references/runtime-protocol.md)，从本 Skill 根目录调用确定性脚本，不要各自解析 JSON 或复制数据库 ID：

```bash
python3 scripts/runtime.py status
python3 scripts/runtime.py resolve --concept task
python3 scripts/runtime.py resolve --concept life_positioning
python3 scripts/runtime.py resolve --page 愿景定位
python3 scripts/runtime.py resolve --source 任务
python3 scripts/runtime.py resolve --property 专注
```

处理规则：

1. `status` 返回 `needs_init` 时，引导用户运行 `$ai-life-system-init`；不要退回硬编码 ID。
2. `resolve` 返回 `ready` 时使用唯一目标；返回 `multiple` 时结合当前业务对象过滤，仍无法消歧才让用户确认；返回 `not_found` 时说明当前索引未找到，不推断模板缺失。
3. 读取前确认目标的 `read_ready`，并在调用 Notion 后检查实时对象与索引目标一致。
4. 创建或更新数据库页面前调用 `check-write`，把本次涉及的所有字段和选项显式传入。例如：

```bash
python3 scripts/runtime.py check-write \
  --data-source-id <已解析的真实 Data Source ID> \
  --operation create \
  --field 任务 \
  --field 状态 \
  --option '状态=进行中'
```

5. 更新普通页面正文前先解析唯一页面，再调用 `check-page-write --page-id <已解析页面 ID>`。它只校验本地页面身份与可读状态；业务 Skill 仍须实时重新读取页面，限制更新范围并获得用户授权。
6. `write_ready: true` 或 `page_write_ready: true` 只代表本地索引预检通过，不代表用户已经授权，也不替代写入前的实时云端检查。

## 具体 Skill 的接入约定

具体 Skill 只需依赖当前 `ai-life-system-init`，不需要再安装 `notion-life-system`：

1. 在自己的说明中声明使用 `$ai-life-system-init` 作为 Notion 运行时底座。
2. 每次任务先调用 `runtime.py status`，再用稳定 concept key 或真实名称解析目标。
3. 业务 Skill 保留自己的分析、内容生成和读写动作；结构发现、同名消歧和字段预检交给本 Skill。
4. 如果模板发生变化，重新运行 `$ai-life-system-init`，所有接入的具体 Skill 随即读取新索引，无需逐个重新配置。
