# Service Blueprint

Use this after the user journey map. The journey map shows what the user experiences; the service blueprint shows what the provider must arrange so that path does not collapse.

## Core Structure

```text
一眼 + 一条路 + 三个点
```

## One Glance

The first moment must show the user's goal, not just the provider's function list.

Check:

- What does the user see first?
- Can the user recognize "this is for my goal" within seconds?
- Is the next action obvious?
- Does wording use the user's language?

## One Path

Give the user a clear path from current state to result.

Check:

- What is step 1?
- What is the first small success?
- What happens after success or failure?
- Where does the product/coach/AI/system intervene?
- What is the minimum path, not the complete feature map?

## Three Points

| Point | Meaning | Design Rule |
| --- | --- | --- |
| 忍耐底线 | The minimum acceptable experience; crossing it breaks trust | Guard this first |
| 峰值 | The most memorable emotional high or progress moment | Concentrate resources here |
| 终值 | The ending feeling users carry away | Design the close deliberately |

Resource rule:

```text
资源有限时，不要平均优化所有体验点。先守住忍耐底线，再集中制造峰值和终值。
```

## Blueprint Table

| User Stage | Frontstage Touchpoint | User Emotion | Backstage Work | Support Resource | Role Owner | Cost/Risk | Design Priority |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Role / Resource Checklist

- User-facing role: user, buyer, learner, member, client, creator, operator, or manager?
- Provider-facing role: founder, coach, assistant, AI agent, community manager, operations, content system?
- Resource: template, prompt, video, checklist, private group, dashboard, data, automation, human feedback?
- Handoff: what must move from content to private domain, private domain to product, product to action, action to review?
- Failure recovery: what happens when the user does not act, misunderstands, or misses a step?
- Resource sustainability: who does the work, how often, what can be automated, and what must stay human?
- Cost boundary: which touchpoints are good enough, and which deserve concentrated resources?

## Blueprint Output

For each key stage, write:

```markdown
用户看到:
用户动作:
后台要发生:
需要的资源:
负责人/角色:
资源可承受性:
可能崩在哪里:
失败恢复:
修复方式:
是否属于忍耐底线/峰值/终值:
```

## Anti-Patterns

- Designing every touchpoint equally.
- Adding more modules when the path is unclear.
- Treating reminders as service design without solving the user's real resistance.
- Making a peak moment that is expensive but not connected to the user's goal.
- Ending with silence after the user finishes or fails.
