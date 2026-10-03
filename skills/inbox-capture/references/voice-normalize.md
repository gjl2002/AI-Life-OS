# 语音输入整理规则

收到用户语音转写的原始文本时，在录入收集箱前先做轻度清洗。

## 处理原则

不是总结、不是扩写、不是重新创作，只做最小修正：

- 删掉口吃、重复、纯语气词（嗯、啊、呃、额、那个）
- 修正明显错别字和标点
- 根据高频词库，将发音相近的误识别词替换为正确写法
- 如有"第一、第二、第三"等枚举，转为"1. 2. 3."数字列表
- 中文数字转阿拉伯数字：三点五→3.5、二十三→23、一百二十→120、零点一→0.1
- 如有改口（"不对""不是…是…"），用改口后的内容替换改口前的

## 高频词库

如果文本中出现相近、同音、错误或不完整的表达，优先结合上下文修正为以下词汇：

ChatGPT, OpenAI, Claude, Claude Code, Anthropic, Gemini, Google Gemini, Kimi, Moonshot, 月之暗面, DeepSeek, 豆包, Doubao, 火山引擎, 火山方舟, Ark, 通义千问, Qwen, 阿里百炼, 智谱 AI, GLM, 腾讯混元, 文心一言, MiniMax, 讯飞星火, Perplexity, Grok, Cursor, Codex, GitHub Copilot, MCP, RAG, Agent, AI Agent, 智能体, 提示词, Prompt, System Prompt, API, API Key, Token, JSON, Webhook, 工作流, AI 工作流, 自动化, 快捷指令, Shortcuts, Notion, Notion AI, 数据库, 属性, 视图, 关系, Rollup, Formula, 按钮, Obsidian, Logseq, Heptabase, flomo, 飞书, Lark, 语雀, Typeless, OpenTypeless, 闪电说, Whisper, 语音输入, 语音识别, 语音转文字, 知识管理, 个人知识库, 第二大脑, Life OS, 游戏化人生管理, 12 周人生设计, 超级个体, 自媒体, AI 效率, 效率工具, 内容创作, 小红书, 爆款笔记, 选题, 公众号, B站, YouTube, Twitter, X, 即刻, Framer, Figma, Stripe, Gumroad, SaaS, 独立开发, 知识付费, 课程, 咨询, 模板, 微流控, PDMS, 软光刻, PMMA, 科研, 论文

## 常见误识别修正

- 泰勒斯、Type less、Tableless → Typeless
- OpenTablet、Open Type less → OpenTypeless
- 闪念说、闪电输、闪电缩 → 闪电说
- 快指令、快截指令 → 快捷指令
- 提示所在、提示语 → 提示词
- 杜邦、都包、抖包 → 豆包
- Deep sick、Deep seek → DeepSeek
- 可米、K米 → Kimi
- Moon shot、月亮暗面 → Moonshot / 月之暗面
- 诺神、No tion → Notion
- 欧比斯丁 → Obsidian
- 克劳德、Cloud → Claude
- Claude code、Cloud code → Claude Code
- 库索、科德克斯 → Codex
- 库瑟、Cursor 编辑器 → Cursor
- 杰森 → JSON
- 接口 → API
- 密钥 → API Key
- 令牌 → Token
- 智能体、代理 → Agent
- 小红书、XHS、小红薯 → 小红书
- 爆款 → 爆款笔记

## 输出

清洗后的文本作为收集箱的"内容"字段，"名称"字段从清洗后的内容提取一句话标题。
