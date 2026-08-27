# 写入动作局部校验

初始化、重新绑定和健康检查只读。后续 Skill 在真正写入前，先使用 `scripts/runtime.py check-write` 对本次动作涉及的目标和字段做本地预检，再读取实时 Schema。

## 创建页面

1. 目标 Data Source 必须唯一并且 `access.read_ready: true`。
2. `access.create_page_ready` 必须为 `true`，并使用索引中的真实 `title_field`。
3. 本次提交的每个字段必须存在于实时索引，且不属于 `readonly_fields`。
4. select、multi_select、status 值必须存在于该字段的真实 options；除非用户明确要求并授权创建新选项，否则不要猜测。
5. relation 只有 `resolved: true` 时才可自动填充，并校验目标页面属于解析出的数据库/Data Source。

## 更新页面

先确认页面所属 Data Source 与索引目标一致，再逐字段执行相同校验。不要把另一个同名数据库的字段用于当前页面。

## 更新普通页面正文

1. 先通过 `resolve --concept <page key>` 或 `resolve --page <真实标题>` 得到唯一 page ID。
2. 调用 `check-page-write --page-id <page ID>`；`multiple` 不得静默选第一个。
3. 调用 Notion 实时重新读取目标页面，核对 page ID、标题和当前内容。
4. 只更新业务 Skill 明确声明的章节或区块，保留其他内容与页面结构。
5. 写入后回读核对。页面正文更新不使用 Data Source 的 `check-write`。

## 索引过期

如果 Data Source 的 `last_edited_time`、实时字段，或普通页面的身份与索引不一致，停止写入并先运行健康检查或重新绑定。普通页面只有正文发生变化时不必重新绑定，但必须以实时正文为准。不要用旧索引猜测字段或页面内容。

## 授权边界

索引中的 `create_page_ready` 不是用户授权。业务 Skill 仍需根据当前请求判断是否被授权执行写入；初始化 Skill 永远不得借此写入业务数据。

`check-write` 返回的 `write_ready: true` 和 `check-page-write` 返回的 `page_write_ready: true` 同样不是用户授权，也不证明云端对象自索引生成后没有变化。
