# 本地配置格式

所有文件由 `scripts/build_config.py` 生成，默认位于 `~/.ai-life-system/`，可用 `AI_LIFE_SYSTEM_DATA_DIR` 或 `--output-dir` 覆盖。

## profile.json

保存配置格式、工作区、Hub、已匹配语义摘要和各索引文件名。健康状态使用：

- `ready`：Hub 与至少一个 Schema 可读，且没有真实读取或冒烟测试故障；
- `needs_attention`：部分成功，但有 Data Source 读取失败或只读冒烟测试失败；
- `blocked`：Hub 不可读或没有任何可用 Schema。

语义概念不存在、出现多个真实目标或某个数据库不在模板中，都不会被当成模板缺失。

## 主要文件

- `discovery.json`：原始发现证据；
- `notion-index.json`：事实索引和 lookup；
- `semantic-map.json`：只包含实际匹配概念；
- `dimension-pages.json`：系统入口及其直接子页面的结构身份，不保存正文；
- `initialization-report.md`：实际结构与真实故障摘要。

`notion-schema.json` 和 `routing-rules.json` 是旧版兼容文件。新 Skill 必须先读取 `profile.json`，再使用其中的 `source_index_file` 与 `semantic_map_file`。

具体 Skill 不应重复这一加载逻辑；统一调用 `scripts/runtime.py status/resolve/check-write/check-page-write`。缺少配置时 Runtime 会返回 `needs_init`，由用户运行 `$ai-life-system-init`。

## 指纹与隐私

`schema_fingerprint` 只由数据库/Data Source ID、标题和规范化属性结构计算，不包含抓取时间或业务记录。所有用户 ID 与 Schema 只保存在用户自己的本地状态目录。

## 原子更新与备份

生成器先写入临时目录并校验全部 JSON，再备份旧配置并替换。任何替换失败都应恢复旧文件。备份位于 `backups/<UTC时间>/`。
