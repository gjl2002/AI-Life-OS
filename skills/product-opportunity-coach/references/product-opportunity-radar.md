# Base Product Opportunity Model

Use this after source retrieval to consolidate the base decision. Trend, new-species, naming, and Offer modules are conditional and do not belong in every base score.

## Six Base Dimensions

1. **真实需求**: a visible consequence, desire, repeated request, behavior, payment, or attempted workaround exists.
2. **首批用户**: a sufficiently specific first buyer/user can be named.
3. **触发场景**: time, context, emotion, and reason to act now are identifiable.
4. **当前替代**: the user’s present workaround, competing product, service, habit, or choice to do nothing is understood.
5. **可见优势**: the user can perceive a reason to switch, try, pay, or stay; “uses AI” is not enough.
6. **交付匹配**: product form, promise, founder capacity, and result/process demand fit each other.

## Working Card

```markdown
产品机会：

真实需求：
- 判断：强 / 部分 / 弱 / 未验证
- 证据：

首批用户：
- 判断：清晰 / 过宽 / 未知
- 证据：

触发场景：
- 判断：清晰 / 部分 / 未知
- 证据：

当前替代：
- 判断：已验证 / 推断 / 未知
- 证据：

可见优势：
- 判断：清晰 / 部分 / 口号 / 未知
- 证据：

交付匹配：
- 判断：匹配 / 需调整 / 不匹配 / 未验证
- 证据：

已验证证据：
合理推断：
待验证假设：
```

## Optional Comparison Score

Use a numerical score only when the user asks for scoring or compares multiple opportunities. Score each base dimension from 0 to 2:

- `0`: absent, contradicted, or unsupported;
- `1`: plausible or partially supported;
- `2`: direct evidence and clear fit.

The total is `/12`. It is a comparison aid, not a probability or automatic decision.

Useful interpretation:

- `10–12`: potentially `值得做` or `调整后做`, only if all hard gates pass;
- `7–9`: usually `先验证` or `调整后做`, depending on whether the gap is evidence or product form;
- `4–6`: usually `暂停` or a very small exploratory test;
- `0–3`: usually `放弃` unless the opportunity object was defined incorrectly.

## Decision Labels

### 值得做

Use only when direct evidence supports demand, first user, trigger scene, substitute/win logic, and delivery. A high score without direct evidence is not enough.

### 调整后做

Use when the opportunity is supported but one named correction—user, scene, promise, form, mechanism, channel, price, or delivery boundary—makes the difference between viable and weak.

### 先验证

Use when one decisive assumption still lacks direct evidence. Name that assumption and design one test capable of confirming or rejecting it.

### 暂停

Use when current timing, workload, access, missing prerequisites, or too many unknowns make immediate testing wasteful. State what change would justify reopening the opportunity.

### 放弃

Use when evidence indicates weak demand, no credible switch reason, structural delivery mismatch, unacceptable risk, or a clearly better opportunity cost.

## Hard Gates

- Without direct demand evidence, do not output `值得做`.
- Without a named first user and trigger scene, do not output `值得做` or `调整后做`.
- Without a current substitute or doing-nothing behavior, do not claim a proven win path.
- Without delivery evidence, recommend a conservative validation form.
- If current market evidence is absent, market claims remain hypotheses.
- If a conditional module was not run, omit its conclusion rather than filling the report mechanically.

## Decision Repair

When the decision is not `值得做`, select the smallest relevant repair:

- narrow or change the first user;
- strengthen or change the trigger scene;
- change the demand grab from pain to pleasure/identity or vice versa;
- make the visible advantage concrete;
- change product form to fit result/process demand;
- reduce delivery scope;
- test content or user language first;
- deliver manually before building a scalable product;
- run a truthful paid test when willingness to pay is the decisive unknown;
- pause or abandon when no repair addresses the structural weakness.

Every repair ends with a validation object, action, success threshold, failure interpretation, and next path.
