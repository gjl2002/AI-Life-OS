# AI 人生系统 Runtime 协议

`scripts/runtime.py` 是具体业务 Skill 与学员本地 Notion 事实索引之间的稳定接口。它只读取 `~/.ai-life-system/`，不连接 Notion，也不执行创建、更新或删除。

## 配置目录

默认读取 `~/.ai-life-system/`。测试或特殊部署可设置 `AI_LIFE_SYSTEM_DATA_DIR`，或在子命令前传入：

```bash
python3 scripts/runtime.py --config-dir <目录> status
```

不要把某位用户的配置目录、Notion ID 或索引文件放进共享 Skill。

## status

```bash
python3 scripts/runtime.py status
```

- 退出码 `0`：配置可读取；继续检查返回的 `health.status`。
- 退出码 `2`：配置缺失或损坏，返回 `runtime_status: needs_init`；运行 `$ai-life-system-init`。
- `runtime_status: needs_attention` 不等于全部不可用，但业务 Skill 必须检查目标自身状态，写入前优先健康检查或重新绑定。

## resolve

一次只提交一种查询：

```bash
python3 scripts/runtime.py resolve --concept task
python3 scripts/runtime.py resolve --source 任务
python3 scripts/runtime.py resolve --property 专注
python3 scripts/runtime.py resolve --option 待办
```

返回统一字段：

- `status: ready`：唯一真实目标，同时提供 `primary_target`；
- `status: multiple`：多个真实目标，`primary_target` 为 `null`；
- `status: not_found`：当前索引没有精确匹配，退出码为 `3`；
- `targets`：供业务上下文按 Data Source、字段类型和动作对象继续过滤。

名称查询使用 NFKC、转小写和移除常见分隔符后的精确匹配，不做模糊标题猜测。优先使用稳定 concept key；语义不存在时，再查询 source、property 或 option。

## check-write

```bash
python3 scripts/runtime.py check-write \
  --data-source-id <真实 Data Source ID> \
  --operation create \
  --field <真实 title 字段> \
  --field <本次字段> \
  --option '<字段>=<选项>'
```

`--field` 和 `--option` 可重复。创建页面必须显式声明真实 title 字段；更新页面使用 `--operation update`。

本地预检会阻止：

- 不存在或不可读取的 Data Source；
- 不存在、只读或规范化后有歧义的字段；
- 未解析 relation；
- 不属于目标字段的 status、select 或 multi-select 选项；
- 创建时未声明真实 title 字段。

只有 `write_ready: true` 才能继续，但业务 Skill 仍须：

1. 确认当前用户请求授权了这次写入；
2. 调用 Notion 时重新读取目标的实时 Schema；
3. 检查实时字段、选项和 relation 与返回的 `schema_fingerprint` 所代表索引一致；
4. 只提交用户授权范围内的数据。

Runtime 预检永远不授予写权限。

## 具体 Skill 接入片段

具体 Skill 可以加入以下依赖约定，并按自己的业务补充 concept key：

```text
本 Skill 使用 $ai-life-system-init 作为 AI 人生系统 Notion 运行时底座。
执行前先调用其 scripts/runtime.py status；再用 resolve 定位真实目标。
任何写入前把目标 Data Source、本次字段和选项传给 check-write。
multiple 不静默取第一个，needs_init 时引导用户运行 $ai-life-system-init。
```

接入后，学员只初始化一次。模板 Schema 更新时重新运行初始化，具体 Skill 不保存第二份配置。
