# 语义映射规则

语义映射的作用是把稳定意图连接到动态索引，不是验证模板完整性。

## 匹配原则

- 默认只做规范化后的精确匹配，不用部分标题相似度自动绑定。
- source 概念匹配 Data Source 或数据库容器标题。
- page 概念匹配 `dimension-pages.json` 中的普通页面标题，或用户明确绑定的页面能力。
- property 概念匹配真实字段名，可以有多个目标。
- option 概念同时校验来源 Data Source、字段和真实选项。
- 用户明确覆盖可以指定 source 概念，但仍须读取并校验真实 Schema。
- 未匹配概念直接省略，不影响整体健康状态。

例如：

- `todo` 应识别为“任务 → 情景 → ☑️ 待办”选项，而不是名为“待办”的数据库；
- `focus` 可以同时指向“任务.专注”和“计时.专注”，输出 `multiple`；
- `daily_record` 指向“每日记录”Data Source；名为“每日复盘”的 relation 或字段单独作为字段语义。
- `commercial_positioning` 指向“商业系统”下已发现并绑定的《商业定位》普通页面，不读取本地正文。

## 消费规则

业务 Skill 通过 `scripts/runtime.py resolve` 查询语义 key 后：

1. `ready` 可以直接作为读取目标；
2. `multiple` 必须结合动作对象、字段类型和用户上下文过滤；
3. 找不到语义 key 时改用 `--page`、`--source`、`--property` 或 `--option` 查询事实索引；
4. 仍有多个结果且上下文不能消歧时，让用户确认。

不要因为语义 key 不存在就断言学员模板缺少某项能力。
