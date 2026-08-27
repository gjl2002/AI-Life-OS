# 商业定位 Runtime 来源路由

## 总原则

云端 Notion 与用户本轮提供的当前事实是内容来源。`$ai-life-system-init` Runtime 只负责定位用户真实页面和 Data Source，不是内容来源。

每次先运行：

```bash
python3 scripts/runtime.py status
python3 scripts/runtime.py resolve --concept commercial_positioning
```

这里的 `scripts/runtime.py` 指已安装 `$ai-life-system-init` 根目录下的脚本。不要把任何用户的页面 ID、数据库 ID 或本地路径写进本 Skill。

解析规则：

- `ready`：确认 `read_ready` 后实时读取云端；
- `multiple`：结合当前系统和业务对象消歧，仍不唯一才让用户确认；
- `not_found`：运行或引导用户运行 `$ai-life-system-init` 的 health-check / rebind；
- `needs_init`：先初始化，不退回固定 ID、全局模糊搜索或本地内容副本。

## 核心普通页面

| 作用 | 首选解析 | 读取条件 |
| --- | --- | --- |
| 当前定位资产 | `--concept commercial_positioning` | 每次正式定位调用 |
| 人生方向约束 | `--concept life_positioning` | 从 0 到 1、方向冲突或边界变化时 |
| 咨询事实 | `--page 咨询` | 当前证据确实涉及咨询与交付时 |
| 商业变现判断 | `--page 商业变现` | 当前议题涉及产品路径或变现关系时 |
| 私域行为 | `--page 私域` | 需要判断线索、沟通或成交链路时 |
| 账号体系 | `--page 账号体系` | 只在校准定位表达时 |

普通页面的 Relation 或引用只代表可能相关，不代表必须读取全文。

## 数据库概念路由

优先使用稳定 concept key：

| 证据类型 | Runtime concept |
| --- | --- |
| 产品与交付 | `product`、`brand_deal` |
| 用户与客户 | `user_profile`、`client_management`、`client_communication`、`user_feedback` |
| 内容与表达 | `content`、`account`、`series` |
| 市场与替代 | `benchmark_account`、`benchmark_content`、`benchmark_product` |
| 商业结果 | `income`、`income_category` |
| 行动约束 | `goal`、`project`、`weekly_review`、`twelve_week_review` |

概念不存在时，才按真实 Data Source 标题精确执行 `resolve --source <标题>`。不要因为某个概念未映射就断言用户没有相关资料。

## 阶段到最少来源

| 当前任务 | 优先读取 |
| --- | --- |
| 从 0 到 1 | 商业定位 + 愿景定位 + 用户画像 + 一个最相关市场/现实请求来源 |
| 校准客户和问题 | 商业定位 + 客户沟通 + 用户反馈 + 咨询/案例 |
| 校准价值机制与产品假设 | 商业定位 + 产品 + 交付反馈 + 异议/成交 |
| 校准表达 | 商业定位 + 内容 + 账号体系 + 用户反馈 |
| 判断市场验证 | 客户、咨询、成交、收入、交付中最相关的 2–3 类 |
| 比较商业方向 | 当前产品证据 + 对标 + 必要趋势证据 |
| 定位刷新 | 当前商业定位 + 最近客户/产品事实 + 近期复盘 |

先查看标题、描述、摘要、时间和 Relation，再决定是否读取全文。不全库扫描，也不全 Relation 扫描。

## 证据优先级

同一结论出现冲突时，通常按以下优先级处理：

1. 用户本轮提供的近期真实客户原话、行为、成交和交付结果；
2. 云端近期客户沟通、用户反馈、产品与收入记录；
3. 内容、咨询和私域行为信号；
4. 对标产品与公开市场行为；
5. 用户画像、创始人判断、宏观趋势和 AI 推断。

用户画像可能仍是假设。对标只能证明市场已有行为，不能证明用户自己的方向已经成立。涉及收入、转化、内容表现和客户结果时必须注明时间范围。

## 缺失来源

找不到客户、市场或结果证据时：

1. 明确当前只是定位假设；
2. 列出最小访谈、内容、销售、小产品或交付验证；
3. 说明什么信号支持假设，什么信号会推翻；
4. 不用人生热爱、创始人信念、公开趋势或对标存在补造需求。
