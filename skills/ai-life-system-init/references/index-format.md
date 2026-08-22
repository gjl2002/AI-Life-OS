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

键使用 NFKC、转小写并移除常见分隔符后的规范化文本。值始终是数组，因为相同名称可以合法地出现在多个 Data Source 中。

## semantic-map.json

语义映射只包含当前索引里实际找到的概念：

- `kind: source` 指向 Data Source；
- `kind: property` 指向字段；
- `kind: option` 指向字段中的真实选项；
- `status: ready` 表示唯一目标；
- `status: multiple` 表示多个真实目标，需要结合业务上下文选择。

没有匹配的概念直接省略，不使用 `missing`。

## 兼容文件

`notion-schema.json` 复制主要 Schema 数据，`routing-rules.json` 复制已匹配语义，供旧版消费者迁移。新 Skill 应读取 `profile.json` 中声明的文件名，不要依赖兼容文件长期存在。

Runtime 接口和退出码见 [runtime-protocol.md](runtime-protocol.md)。
