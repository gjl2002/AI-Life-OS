# Xiaohongshu Adapter

Use this only when the user asks to adapt a finished WeChat/公众号 article for Xiaohongshu, such as:
- 我想发小红书
- 顺便改成小红书
- 公众号转小红书
- 生成小红书笔记
- 这个发小红书怎么写

This is an optional distribution module after the WeChat article is complete. It is not part of the default WeChat drafting workflow.

## Core Position

The Xiaohongshu version is not a WeChat summary, not a朋友圈转发文案, and not a short traffic teaser.

It must be an independent Xiaohongshu note:
- readable inside Xiaohongshu without opening the WeChat article
- built around one small platform-friendly cut
- concrete enough to create resonance
- useful enough to be saved
- open enough to invite comments

Default length:
- 400-500 Chinese characters
- method notes can be up to 600 characters
- never exceed 800 characters

Do not create a 150-250 character short引流版 unless the user explicitly asks for a very short teaser. The default module is the independent-note version.

## Relation To WeChat Article

WeChat article usually explains a whole judgment. Xiaohongshu note extracts one cut.

Do not compress the whole article. Select the cut most likely to make the reader feel:

> 这说的是我。

Possible cuts:
- pain cut
- strong-judgment cut
- method cut
- story cut
- product-seeding cut

## Required Process

### Step 1: Identify Source Article Type

Classify the original WeChat article as:
- strong-judgment opinion
- pain-point teardown
- trend judgment
- personal story
- method list
- product conversion

### Step 2: Choose Xiaohongshu Cut

Pick one cut only:
- pain cut: best when the article has a concrete state readers recognize
- strong-judgment cut: best when the article has a sharp counterintuitive claim
- method cut: best when the article contains a small immediately usable action
- story cut: best when a personal scene or user case is the strongest material
- product-seeding cut: best when the article is already product-oriented

Selection standard:
- Which cut is most concrete?
- Which cut is easiest to read on a phone?
- Which cut creates save/comment value?
- Which cut can stand alone without the full WeChat article?

### Step 3: Decide Note Type

Choose one:
- 强观点型
- 痛点共鸣型
- 方法清单型
- 故事切片型
- 产品种草型

### Step 4: Extract Only Necessary Material

Extract from the WeChat article:
- one core judgment
- 1-2 concrete life scenes
- one key reversal
- one small actionable method or 2-3 points
- one closing golden sentence
- one light product bridge only if needed

Do not carry over the whole WeChat logic.

### Step 5: Rebuild For Xiaohongshu

Use this standard rhythm:

```text
title hook
-> pain scene
-> core judgment
-> 2-3 points or one small method
-> golden sentence
-> interaction question
```

The first sentence must be direct. Do not use a slow WeChat-style opening.

### Step 6: Create Titles

Give 3 recommended title directions:
- pain title
- judgment title
- method title

Xiaohongshu titles should be short, direct, and close to the reader's lived state. Prefer 20 Chinese characters or fewer when possible.

Title patterns:
- 你不是 X，是 Y
- 跟 AI 聊完就忘，才是 X
- 为什么你越 X，越 Y
- X 后，我只做这 3 件事
- 普通人 X，可以从这一步开始
- 强者都有一个特点：X

Do not use emoji. Do not use a number, result, authority, or product claim unless the source article supports it.

### Step 7: Final Check

Before output, check:
- Is it independent, not a summary?
- Does the opening stop scrolling?
- Is there a concrete scene?
- Is the judgment clear?
- Is the method small enough?
- Are abstract words translated into lived language?
- Is the product bridge light or absent?
- Is there save/comment value?
- Is there a natural interaction question?

## Note Type Structures

### Strong-judgment Note

Use for counterintuitive AI/growth/self-media mistakes.

```text
strong judgment
-> life scene
-> problem reversal
-> 3 reminders
-> golden sentence
```

### Pain-resonance Note

Use for readers who feel anxious, scattered, or effortful without progress.

```text
life state
-> emotional resonance
-> root judgment
-> one direction
-> interaction question
```

Start from status, not theory.

### Method-list Note

Use for AI, Notion, goal management, review, or workflow content.

```text
specific problem
-> common mistake
-> correct principle
-> 3-5 steps
-> closing reminder
```

Keep the method small. Prefer 3 steps. Avoid full-system explanations.

### Story-slice Note

Use when the personal scene is strongest.

```text
real scene
-> confusion at the time
-> later recognition
-> reminder for readers
```

Do not turn it into a full method article.

### Product-seeding Note

Use only when the source article is product-oriented or the user asks for product seeding.

```text
problem observed
-> why existing methods are not enough
-> what I built or believe
-> who it fits
-> light action
```

Do not list benefits, price, purchase route, or excessive promises. Write why the product exists, not why it is amazing.

## Style Rules

- Use short sentences and short paragraphs.
- Keep each paragraph within 3 phone-screen lines when possible.
- Use numbering when it helps saving.
- Translate abstract words immediately.
- Prefer concrete reader states over external evidence.
- Use external authority very sparingly.
- Do not write `这篇文章讲了...`.
- Do not write a WeChat-style long opening.
- Do not over-explain.
- Do not make it sound like an ad.
- Do not use emoji.

Abstract-to-lived-language examples:
- Do not only write: `你需要成长上下文。`
- Write: `AI 要知道你最近在推进什么、过去为什么总是半途而废、哪些问题一直困扰着你。`

Product bridge rule:
- Non-product note: at most one light sentence, such as `我做这套系统，其实也是想解决这件事。` Do not expose an internal codename or another concrete template/product name unless the user explicitly asks to promote that named product.
- Product note: explain problem, belief, and fit; do not sell aggressively.

## Output Format

```markdown
原文类型：
小红书切口：
笔记类型：

推荐标题：
1. 痛点型标题：
2. 判断型标题：
3. 方法型标题：

小红书正文方案 A：

小红书正文方案 B：（可选，使用不同切口或结构）

发布检查：
- 独立可读：
- 具体场景：
- 核心判断：
- 收藏/互动理由：
- 产品承接是否克制：
```
