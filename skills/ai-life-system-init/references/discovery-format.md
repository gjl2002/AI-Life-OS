# 标准化发现文件

`discovery.json` 是 Notion 读取工具与确定性配置生成器之间的接口。它只保存结构元数据，不保存记录正文。

## 最小结构

```json
{
  "schema_version": "0.4",
  "discovered_at": "2026-08-22T10:00:00+08:00",
  "workspace": {"id": "workspace-id", "name": "学员工作区"},
  "selected_modules": ["growth", "commercial"],
  "module_roots": [
    {"module_key": "growth", "entry_kind": "module_page", "page_id": "growth-page-id", "title": "成长系统", "url": "https://www.notion.so/...", "last_edited_time": "2026-08-22T01:00:00.000Z", "readable": true},
    {"module_key": "commercial", "entry_kind": "shared_hub", "page_id": "shared-hub-id", "title": "AI 人生系统", "url": "https://www.notion.so/...", "last_edited_time": "2026-08-22T01:00:00.000Z", "readable": true}
  ],
  "hub": {
    "page_id": "hub-page-id",
    "title": "数据管理",
    "url": "https://www.notion.so/...",
    "last_edited_time": "2026-08-22T01:00:00.000Z",
    "readable": true
  },
  "candidates": [],
  "dimension_pages": [],
  "smoke_tests": []
}
```

`workspace.id` 在连接工具不暴露时可以为空，但 `workspace.name`、`selected_modules`、`module_roots` 中每个 `page_id` 与 `readable` 必须来自真实读取结果。`module_key` 只允许 `growth`、`commercial`、`life`；`entry_kind` 使用 `module_page` 或 `shared_hub`。同一个共享 Hub 可为每个选中的模块建立一项入口，并通过该模块选项卡确定扫描范围。旧版只提供 `hub` 的文件仍可读取，按三合一处理；初始化应重新询问学员实际已购模块。

## 候选数据库

```json
{
  "database_id": "database-id",
  "title": "目标",
  "url": "https://www.notion.so/...",
  "archived": false,
  "last_edited_time": "2026-08-22T01:00:00.000Z",
  "source": "child_database",
  "source_page_id": "hub-page-id",
  "source_section": "成长系统 / 行动看板",
  "module_keys": ["growth"],
  "detection_reason": "来自 Hub 的成长系统选项卡 / 行动看板区块",
  "selected": true,
  "retrieve_failed": false,
  "error": "",
  "user_override": {"capability": "goal"},
  "data_sources": []
}
```

`module_keys` 记录这项数据库属于哪些已选择模块；数据库被多个模块引用时保留多个 key。`source_section` 可以记录选项卡名和可见标题分组路径，例如 `成长系统 / 行动看板`；它是路由线索，不是数据库身份。允许的 `source` 包括 `child_database`、`database_mention`、`link_to_page`、`rich_text_link`、`block_url` 和 `manual`。未知来源也可保留，但不能伪装成 Hub 直接发现。

当 Hub 使用 Notion `tabs` / `tab` 布局时，选项卡标题（例如“成长系统”）作为逻辑系统分组，不添加到 `dimension_pages`，也不生成虚构 page ID。遍历选项卡内可读取的数据库引用及其纯布局嵌套块，并把来源选项卡和标题分组写入候选的 `source_section` 与 `detection_reason`。数据库在选项卡内换列或换位置后仍以稳定 Notion ID 去重；如果读取工具未返回选项卡内容，保留读取限制并允许用户手动补充，不推断缺失。

同一个规范化 Notion ID 只保留一个候选；合并时保留最明确的来源和全部检测说明。`selected` 默认为 `true`，显式为 `false` 的候选只进入发现索引，不进入路由配置。

生成器兼容读取旧版 `0.2`、`0.3` 发现文件以及只含单个 `hub` 的 `0.4` 文件。输出使用当前 `0.4` 格式并附带模块选择和入口元数据。

## Data Source 与属性

```json
{
  "id": "data-source-id",
  "title": "目标",
  "url": "https://www.notion.so/...",
  "last_edited_time": "2026-08-22T01:00:00.000Z",
  "retrieve_failed": false,
  "error": "",
  "properties": [
    {"name": "名称", "type": "title"},
    {"name": "状态", "type": "status", "options": ["未开始", "进行中", "已完成"]},
    {
      "name": "所属项目",
      "type": "relation",
      "related_database_id": "database-id",
      "related_data_source_id": "data-source-id"
    }
  ]
}
```

数据库容器和 Data Source 是两层不同对象。发现数据库后必须读取容器返回的**全部** `<data-source>`，并把每个 Data Source 独立写入 `data_sources`：

- `candidate.title` 保存数据库容器标题；
- `data_sources[].title` 必须保存该 Data Source 自己的真实标题，不能用容器标题代替；
- 多 Data Source 数据库必须保留每个独立 ID、标题、Schema 和读取失败状态；
- 一个子 Data Source 读取失败时只标记该项，不能丢弃同容器下其他成功项；
- 容器返回两个 Data Source 时，发现文件也必须有两项，不能只保存当前视图对应的一项。

例如容器《AI 学习库》同时包含《去AI味库》和《文风语料库》时，应保存为一个候选数据库下的两个 `data_sources`，后续语义才能分别解析它们。

如果连接工具只返回传统数据库级 `properties`，可以把它们放在候选对象中；生成器会创建一个以 `database_id` 为 ID 的兼容 Data Source。属性可以是上述数组，也可以是以真实属性名为键的对象。

## 非数据库页面

`dimension_pages` 保存 Hub 直接普通页面，以及三个系统入口的直接子页面。初始化只采集结构元数据，不保存页面正文：

```json
{
  "key": "life_dashboard",
  "title": "人生仪表盘",
  "page_id": "page-id",
  "url": "https://www.notion.so/...",
  "source": "hub_direct",
  "parent_page_id": "hub-page-id",
  "parent_key": "hub",
  "depth": 1,
  "last_edited_time": "2026-08-22T01:00:00.000Z",
  "detection_reason": "Hub 直接页面",
  "readable": true
}
```

Hub 为 `depth: 0`，成长系统、商业系统、生活系统或用户明确指定的系统入口为 `depth: 1`，这些入口的直接子页面为 `depth: 2`。到 `depth: 2` 后停止，不继续递归普通子页面。`user_override.capability` 可以把用户确认的页面绑定到稳定 page concept，例如 `commercial_positioning`。

## 冒烟测试

```json
{
  "data_source_id": "data-source-id",
  "status": "passed",
  "empty": false,
  "checked_at": "2026-08-22T10:05:00+08:00",
  "error": ""
}
```

`status` 使用 `passed`、`failed` 或 `not_run`。空数据库只要查询成功仍为 `passed`。

## 禁止内容

不得写入 token、密钥、用户邮箱、数据库记录、页面正文或其他不需要的个人内容。ID 和 Schema 只允许存在于用户自己的本地状态目录或临时文件。
