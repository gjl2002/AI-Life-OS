# 标准化发现文件

`discovery.json` 是 Notion 读取工具与确定性配置生成器之间的接口。它只保存结构元数据，不保存记录正文。

## 最小结构

```json
{
  "schema_version": "0.3",
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

生成器兼容读取旧版 `0.2` 发现文件，但输出统一升级为当前 `0.3` 格式。

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

如果连接工具只返回传统数据库级 `properties`，可以把它们放在候选对象中；生成器会创建一个以 `database_id` 为 ID 的兼容 Data Source。属性可以是上述数组，也可以是以真实属性名为键的对象。

## 非数据库页面

`dimension_pages` 可保存首页、状态页、人生领域页等后续读取需要的页面：

```json
{
  "key": "life_dashboard",
  "title": "人生仪表盘",
  "page_id": "page-id",
  "url": "https://www.notion.so/...",
  "source": "hub_direct",
  "readable": true
}
```

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
