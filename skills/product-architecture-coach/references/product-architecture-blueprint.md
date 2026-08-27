# Product Architecture Blueprint

Use this reference when producing a formal 产品架构蓝图.

## Blueprint Fields

### 一句话结论

State whether the current architecture should be:

- `可进入 MVP`
- `先补用户证据`
- `先缩小范围`
- `先重构承诺`
- `暂缓产品化`

### 产品对象与定位边界

Include:

- product/course/training camp name
- public category language
- target user
- current maturity
- what this product is not

### 读取来源与覆盖边界

State:

- runtime concepts actually resolved and read
- user-supplied files or pages actually used
- sources sampled rather than fully read
- unavailable, empty, or unresolved sources
- evidence conflicts that affect the architecture

Do not imply full-database coverage when only selected records were read.

### 证据与假设

Separate:

- `已验证证据`: user-owned notes, product records, paid history, consultation records, real feedback, source transcripts.
- `合理推断`: inferred from positioning, adjacent products, user avatar, or course notes.
- `待验证假设`: claims that still need interviews, presale, comments, benchmark checks, or paid tests.

### 核心承诺与非承诺

Use:

```text
帮助【用户】在【场景/周期】中，通过【机制/路径】，从【问题状态】走到【目标状态】。
```

Then state:

- what result is in scope
- what result is out of scope
- which claims need proof before appearing on sales pages

### 产品路径

Design 3-5 stages. Each stage needs:

- stage name
- user starting obstacle
- stage goal
- core lesson/module
- user task
- visible deliverable
- feedback method

### Delivery Matrix

Use this table:

| 阶段 | 用户卡点 | 方法/SOP | 工具/模板 | 用户任务 | 可见交付物 | 反馈 |
| --- | --- | --- | --- | --- | --- | --- |

### 原材料与加工方式

List:

- available materials
- missing materials
- processing method
- output artifact

Processing methods:

- 拆解: break down an excellent example into reusable parts
- 迁移: adapt a pattern into the user's domain
- 收集: gather cases, questions, screenshots, tools, prompts, and workflows
- 组合: assemble materials into a new path, template, SOP, or training task
- 提炼: turn messy experience into a principle, checklist, or decision rule
- 演示: convert a method into a visible example or walkthrough

### MVP Scope

Separate:

- `must-have`: required for a real delivery test
- `next`: improves conversion or experience after first validation
- `later`: nice but not needed for version 0.1

### Sales-Page Handoff

Prepare:

- value point
- solution
- payment reason
- available proof
- missing proof
- claim wording risks
- pricing logic hypothesis
- CTA/testing action

## Delivery Rule

Return this document as a reviewable blueprint only. Do not automatically create, update, archive, or append to any Notion record.

## Quality Check

Reject or revise the blueprint when:

- it has only content modules and no user deliverables
- it promises a result but provides no feedback loop
- it claims "训练营/陪跑" but no provider-side cadence exists
- it lists tools without naming user transformation
- it depends on fake proof or exaggerated outcomes
- it has no MVP boundary
