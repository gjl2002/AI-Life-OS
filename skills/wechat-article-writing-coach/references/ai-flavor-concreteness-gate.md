# AI-Flavor Concreteness Gate

Run this after reader-flow repair and after applying `AI赋能 / 去AI味库`, before the quality script and final output.

## Core Rule

A phrase marked `可保留` in the user's library is an allowed rhetorical form. It is not automatically publishable.

Reject an abstract standalone judgment unless the surrounding text supplies at least one of these anchors:

- a visible scene or action;
- a concrete object, choice, or consequence;
- a recognisable reader situation;
- a named and traceable piece of evidence;
- a first-person observation with a real, specific detail.

Do not keep a sentence just because it sounds sharp, could be highlighted, or has a familiar creator-style structure.

This gate applies at article level as well as sentence level. A draft can contain natural sentences and still feel AI-generated because its structure is too complete, symmetrical, and average.

## Hard Checks

For every standalone judgment, headline-like subheading, or sentence that could be screenshotted on its own, ask:

1. What exactly happens in the reader's life after this sentence?
2. What concrete noun or verb carries the claim?
3. Does the prior or next sentence show why this judgment follows?
4. Could this sentence be pasted unchanged into an unrelated AI, productivity, relationship, or growth article?

If questions 1-3 cannot be answered, or question 4 is yes, rewrite it with an anchor or delete it.

## High-Risk Forms

These forms require an anchor; do not ban them mechanically:

| Form | Weak example | Repair direction |
| --- | --- | --- |
| `你以为……其实……` | `你以为自己在使用建议，其实可能在练习接受建议。` | Show the actual moment: `屏幕上已经有了三个版本。你不用再从头想，只要挑一个顺眼的。` |
| `不是……而是……` | `这不是效率提升，而是认知升级。` | State the observed change: `它确实让我省了点时间，但更明显的是，我开始先写判断，再让 AI 帮我找漏洞。` |
| Abstract noun as conclusion | `你正在失去自己的主体性。` | Name the behavior and cost: `连续几次直接采用推荐后，你甚至说不清最初想表达什么。` |
| Isolated “golden sentence” | `工具越聪明，人越要保留一点笨拙。` | Keep only if the adjacent paragraph has already shown the tool, the human action, and the trade-off; otherwise turn it into ordinary prose or remove it. |

## Decision

- **Pass:** the sentence earns its sharpness from nearby evidence and reads like a conclusion someone arrived at, not a template supplied first.
- **Rewrite:** the core thought is useful but its nouns, verbs, or causal bridge are missing.
- **Delete:** it is interchangeable, motivational, or only makes the paragraph sound more profound.

Do not replace every sharp line with flat explanation. The goal is a judgment that grows out of a real paragraph, not the removal of judgment itself.

## Macro-Level Check

Reject or compress the draft when:

- every idea has a labelled subsection even though the transition is obvious;
- personal story, case, book, theory, method, and product appear as compulsory slots;
- several pieces of evidence prove the same point;
- the article explains the full framework when one judgment and one example would carry it;
- removing a complete section does not alter the conclusion;
- the reading experience resembles a course handout or a polished model answer more than a specific thought process.

Run the compression comparison in `editorial-claim-audit.md`. A short article may use no internal headings and fewer evidence types.
