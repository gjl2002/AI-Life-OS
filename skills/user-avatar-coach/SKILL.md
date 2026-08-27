---
name: user-avatar-coach
description: "Use when the user wants evidence-based 用户画像, 买家画像, 用户洞察, 用户分群, 痛点聚类, 购买动机, 未成交原因, or analysis of interviews, chats, comments, feedback, delivery records, screenshots, and related cloud Notion materials. Uses the AI Life System Runtime and can update the existing Notion 用户画像 database only after explicit authorization. Do not use it to choose the overall commercial positioning, design a complete product, produce content, or build a sales system."
---

# User Avatar Coach

中文名：用户画像教练

## Purpose

围绕一个明确的商业研究对象，从真实访谈、咨询、聊天、评论、购买行为、未成交原因和交付反馈中理解用户：

- 谁在什么场景下开始寻找帮助；
- 他真正想完成什么改变；
- 现在如何解决，为什么原方案失效；
- 为什么购买、为什么不购买、什么建立信任；
- 哪些用户属于同一类，哪些必须分开；
- 当前能够确认什么，仍然需要验证什么。

先找证据，再抽象画像。最终结果进入用户现有云端“用户画像”数据库，不创建平行画像库。

## Boundary

本 Skill 是商业系统的用户研究与用户理解层：

- `$commercial-positioning-coach`：选择现阶段优先服务谁、解决什么以及价值机制；
- 本 Skill：用真实用户材料验证、修正和细化用户假设、分群与购买逻辑；
- `$product-opportunity-coach`：判断具体问题是否值得产品化；
- `$product-architecture-coach`：设计产品、模块、交付、定价与升级路径；
- 创作与销售类 Skill：把用户洞察转化为内容、销售页和沟通执行。

本 Skill 可以说明用户证据对商业定位、产品、内容和销售表达形成了什么约束，但不继续产出完整定位、产品架构、内容计划、销售页或销售 SOP。

## Required References

开始分析前读取：

- [references/workflow.md](references/workflow.md)：研究流程与对话方式。
- [references/evidence-standard.md](references/evidence-standard.md)：证据等级、原话和正式画像门槛。

按任务读取：

- 使用 Notion：读取 [references/source-routing.md](references/source-routing.md)。
- 正式画像、重要分群或写回：读取 [references/evidence-audit.md](references/evidence-audit.md)。
- 情绪、抗拒、投诉、赞美或言行冲突：读取 [references/empathy-radar.md](references/empathy-radar.md)。
- 生成阶段小结、假设画像或正式画像：读取 [references/avatar-output-schema.md](references/avatar-output-schema.md)。
- 输出正式画像或写回：读取 [references/review-checklist.md](references/review-checklist.md)。
- 写回 Notion：读取 [references/notion-writeback.md](references/notion-writeback.md)。
- 需要 JTBD、Buyer Persona、访谈或定性分析方法时：读取 [references/theory-library.md](references/theory-library.md)。

正式画像或写回前，在可行时运行 `scripts/avatar_quality_check.py`。脚本只检查证据边界与产物契约，不能代替研究判断。

## AI Life System Runtime Contract

本 Skill 使用 `$ai-life-system-init` 作为 Notion 运行时底座。云端 Notion 正文、记录与实时 Schema 是事实来源；Runtime 只保存当前用户自己的结构索引，不保存访谈、反馈或画像正文。

每次需要访问 AI 人生系统时：

1. 从 `$ai-life-system-init` 根目录运行 `scripts/runtime.py status`。
2. 用 `resolve --concept user_profile` 定位用户现有“用户画像”Data Source。
3. 需要商业解释时，用 `resolve --concept commercial_positioning` 定位云端“商业定位”页面。
4. 其他证据来源按 `source-routing.md` 中的稳定 concept key 按需解析；概念不存在时才按真实页面或 Data Source 标题精确解析。
5. `needs_init` 时运行或引导用户运行 `$ai-life-system-init`；`multiple` 不静默选择；`not_found` 不退回固定 ID 或模糊标题猜测。
6. 读取前确认 `read_ready`，然后实时读取目标内容。

不读取本地 Notion Sync、本地 Markdown 内容副本或本地数据库索引，不保存固定数据库 ID、页面 ID、个人路径或个人工作区 URL。Runtime 不可用时，可以仅基于用户本轮明确提供的材料分析，但必须说明没有核对云端，也不得写入云端。

## Evidence Discipline

- 用户本轮提供的访谈、聊天、反馈、截图和录音转写是核心证据。
- Notion 商业定位、产品和既有画像用于解释业务背景，不能证明用户真实想法。
- 竞品、公开评论和理论只能作为外部参考，不能证明用户自己的客户。
- 保留能体现情绪、场景、抗拒、选择和购买意图的用户原话；转述必须标注。
- 区分：已确认事实、合理洞察、待验证假设。
- 没有 Level 1 或强 Level 2 证据时，只输出用户画像假设，不把业务愿望写成正式画像。
- Relation 只表示可能相关，不代表必须读取全部关联记录；先看标题、描述、时间与摘要，再选择会改变判断的材料。

## Research Interaction

- 已有材料足够时直接分析，不先让用户完成固定问卷。
- 已有记录能回答的内容不重复询问。
- 一次只澄清一个会改变分群、购买逻辑或画像结论的关键缺口。
- 抽象回答要追问最近一次具体场景、实际行为、当前替代、原话、选择或结果。
- 确认用户当前没有相关证据后停止盘问，明确缺口并转成访谈问题或验证材料清单。
- 用户要求查看或总结已有资料时直接回答，不以“教练不能给答案”为由拒绝。
- 用户当前说法与旧记录不一致时，优先确认变化发生在什么阶段，不把旧记录视为永远正确。

## Workflow

1. 明确本次研究对象：新画像、更新已有画像、某个产品的用户、批量材料分群，或为证据不足设计访谈。
2. 解析并按需读取已有用户画像、商业定位和最少相关商业来源。
3. 建立当前材料包，标明来源、时间、用户身份和证据等级。
4. 提取用户原话及其场景、行为、替代方案、结果、购买与抗拒信号。
5. 合并重复信号，保留冲突与反例，区分频率和强度。
6. 根据 JTBD、触发场景、购买动机、抗拒、信任要求和使用场景判断是否需要分群。
7. 运行证据审计，决定输出阶段小结、用户画像假设或正式用户画像。
8. 说明画像对商业系统的约束与应交给哪个下游 Skill，不替下游完成执行。
9. 只有用户明确要求保存、更新或直接写入时才操作云端用户画像数据库；写后回读核对。

## Result Branches

- 材料仍在形成：`用户洞察阶段小结`与下一个聚焦问题。
- 方向出现但证据不足：`用户画像假设`与需要补充的材料或访谈问题。
- 真实用户材料和购买逻辑相对充分：`用户画像`。
- 多组用户在 JTBD、触发、购买逻辑或产品使用方式上存在会改变商业决策的差异：拆分画像，并说明拆分依据。

不要为了丰富而制造分群，也不要用年龄、城市、职业或“成长型人群”等人口标签替代行为、场景与购买逻辑。

## Cloud Writeback

- 探索过程中不逐轮写入画像库。
- 用户明确授权后，重新解析 `user_profile`，实时读取 Schema 与现有相关记录并检查重复。
- 创建或更新前运行 Runtime `check-write`，传入本次实际使用的字段与选项。
- 优先更新已有相关画像；只有出现不同 JTBD、触发或购买逻辑且没有合适记录时才新建。
- 不发明 Schema 中不存在的字段；无对应字段的研究内容放入页面正文。
- 写后回读，核对标题、画像类型、关键原话、购买逻辑、事实/洞察/假设和证据来源。

Runtime 的 `create_page_ready` 或 `write_ready` 不代表用户已经授权。

## Stop Conditions

只有以下情况阻止继续：

- 关键材料无法辨认或来源身份不清，继续会造成错误归因；
- 用户要求写回，但 Runtime、云端访问、Schema 或重复记录无法确认；
- 正式画像的质量检查存在未解决阻塞项。

证据不足本身不是阻塞：降级为用户画像假设，并明确下一步需要什么。
