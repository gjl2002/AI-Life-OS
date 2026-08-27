# Five-Layer Experience Diagnosis

Use this when the user says a product is "不好用", "用户不用", "用户掉队", or when the path feels unclear.

## Layers

| Layer | Core Question | Experience Meaning |
| --- | --- | --- |
| 感知层 | 用户第一眼听到、看到、摸到什么？ | surface clarity, visual language, tone, wording, perceived quality |
| 角色框架层 | 用户在这里扮演什么角色，按什么结构互动？ | navigation, roles, modules, interaction order, page relationship |
| 资源结构层 | 哪些资源、关系、工具、内容在支撑体验？ | operations, data, community, assistant, content, support, constraints |
| 能力圈层 | 这个产品能做什么，不能做什么？ | promise boundary, delivery capability, feature scope, service capacity |
| 战略存在层 | 用户为什么需要它，它和用户长期目标有什么关系？ | product meaning, user reliance, business/user value exchange |

## Diagnosis Rules

- Do not reduce every problem to the perceptual layer.
- If the user cannot see the goal, diagnose strategic existence and role framework.
- If the user sees the goal but cannot move, diagnose role framework and resource structure.
- If the user expects a result the product cannot deliver, diagnose capability circle.
- If the service relies on resources the provider cannot sustain, diagnose resource structure.
- If the product's promise is vague or misnamed, diagnose strategic existence before polishing UI.

## "不好用" Translation

| User Expression | Likely Layer | Check |
| --- | --- | --- |
| 我不知道这是干嘛的 | 战略存在层 / 感知层 | first glance, promise, user goal visibility |
| 我不知道下一步做什么 | 角色框架层 | path, next action, module order |
| 我做了也没结果 | 能力圈层 / 资源结构层 | promise-result fit, support resources |
| 太麻烦了 | 角色框架层 / 资源结构层 | effort cost, handoff, repeated friction |
| 感觉不专业 | 感知层 / 能力圈层 | surface trust and delivery proof |
| 后面坚持不下去 | 资源结构层 / 服务蓝图 | reminders, feedback, community, coach/AI support |

## Output Pattern

For each layer, write:

```markdown
层级:
当前证据:
体验问题:
用户感受:
修复动作:
优先级:
```

The final recommendation should identify the deepest broken layer. Fix that layer first.
