# 标准化发现文件

`discovery.json` 是 Notion 读取工具与确定性配置生成器之间的接口。它只保存结构元数据，不保存记录正文。

## 最小结构

```json
{
  "schema_version": "0.4",
  "discovered_at": "2026-08-22T10:00:00+08:00",
  "workspace": {"id": "workspace-id", "name": "学员工作区"},
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

`workspace.id` 在连接工具不暴露时可以为空，但 `workspace.name`、`hub.page_id` 和 `hub.readable` 必须来自真实读取结果。

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
  "source_section": "12周行动",
  "detection_reason": "来自 Hub 的 12周行动区块",
  "selected": true,
  "retrieve_failed": false,
  "error": "",
  "user_override": {"capability": "goal"},
  "data_sources": []
}
```

允许的 `source` 包括 `child_database`、`database_mention`、`link_to_page`、`rich_text_link`、`block_url` 和 `manual`。未知来源也可保留，但不能伪装成 Hub 直接发现。

同一个规范化 Notion ID 只保留一个候选；合并时保留最明确的来源和全部检测说明。`selected` 默认为 `true`，显式为 `false` 的候选只进入发现索引，不进入路由配置。

生成器兼容读取旧版 `0.2`、`0.3` 发现文件，但输出统一升级为当前 `0.4` 格式。

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
