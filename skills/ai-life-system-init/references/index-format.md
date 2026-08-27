# 动态索引格式

`notion-index.json` 是当前学员 Notion 结构的事实来源。具体 Skill 应优先调用 `scripts/runtime.py` 访问它，而不是各自实现 JSON 解析；索引记录事实，不声明模板应该拥有什么。

## sources

每个 Data Source 保存：

- `database_id`、`data_source_id`、数据库标题、Data Source 标题和 URL；
- 来源 Hub、区块、检测原因、最后编辑和抓取时间；
- `properties`、`relations`、`writable_fields`、`readonly_fields`；
- `schema_fingerprint`、`retrieve_failed` 和错误信息；
- `access.read_ready`、`access.create_page_ready`、标题字段和阻塞原因。

`create_page_ready` 只说明 Data Source 可访问且存在 title 属性，不代表任意业务字段都可以写入。

## lookup

查找表包括：

- `source_titles`：Data Source 标题到真实 ID；
- `database_titles`：数据库容器标题到真实 ID；
- `property_names`：字段名到所在 Data Source 和字段类型；
- `option_names`：select、multi_select、status 选项到所在字段。
- `page_titles`：普通页面标题到真实 page ID、父页面和可读状态。

键使用 NFKC、转小写并移除常见分隔符后的规范化文本。值始终是数组，因为相同名称可以合法地出现在多个 Data Source 中。

## semantic-map.json

语义映射只包含当前索引里实际找到的概念：

- `kind: source` 指向 Data Source；
- `kind: page` 指向 `dimension-pages.json` 中已绑定的普通页面；
- `kind: property` 指向字段；
- `kind: option` 指向字段中的真实选项；
- `status: ready` 表示唯一目标；
- `status: multiple` 表示多个真实目标，需要结合业务上下文选择。

没有匹配的概念直接省略，不使用 `missing`。

## dimension-pages.json

每个普通页面保存稳定 key、标题、page ID、URL、最后编辑时间、父页面、发现深度、来源和可读状态。它只负责页面身份，不保存页面正文。Hub 为深度 0，系统入口为深度 1，系统入口的直接子页面为深度 2。

## 兼容文件

`notion-schema.json` 复制主要 Schema 数据，`routing-rules.json` 复制已匹配语义，供旧版消费者迁移。新 Skill 应读取 `profile.json` 中声明的文件名，不要依赖兼容文件长期存在。

Runtime 接口和退出码见 [runtime-protocol.md](runtime-protocol.md)。
