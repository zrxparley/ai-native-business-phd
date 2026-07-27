# 选修E10 · Day 2：Agent商业模式设计--从AaaS到outcome-based pricing · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 选修E10 Agent经济与商业模式 · Day 2
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：Agent时代的商业模式如何设计？从Agent-as-a-Service订阅制，到按调用计费、outcome-based pricing、分润模式，四种定价模式如何选择？推理成本（token定价）如何吃掉Agent利润？营销Agent如何收费？
> **v5.0 升级点**：① 真实库上机（pydantic 商业模式schema + numpy-financial 三种定价NPV/IRR + statsmodels 定价弹性回归） ② TODO填空式起始笔记本 ③ Notebook化 ④ 深链阅读 ⑤ 2026前沿（outcome-based pricing + 推理成本 + 天道推演×商业模式沙盘 + MCP协议 + A2A经济）

---

## 学习目标（学完你能做到）

1. 能用 **pydantic**（真实schema验证库）定义Agent商业模式的四种定价契约--AaaS订阅制、按调用计费、outcome-based pricing、收益分润--并用结构化输出（structured output）实现Agent可发现的能力声明（API Economy 2.0）
2. 能用 **numpy-financial**（真实金融计算库）对三种定价模式做财务对比--计算12月现金流NPV/IRR，量化推理成本（GPT-4o $5/1M vs DeepSeek V3 $0.27/1M）对Agent利润率的影响，找到盈亏平衡的推理成本阈值
3. 能用 **statsmodels**（真实计量经济学库）拟合定价弹性回归（log-log OLS：log(采纳率) ~ log(价格)），找出Agent产品的最优定价点--弹性需求下降价增收，非弹性需求下涨价增收
4. 能解释Agent商业模式演进的五个阶段（按席位 -> 按用量 -> 按任务 -> 按结果 -> 按价值分成），并能在营销Agent场景中设计混合定价方案（基础费+绩效费+分润），平衡收入稳定性与客户信任
5. 能建立天道推演×商业模式沙盘的同构认知--用三时间线推演（immediate/near/far）分析不同定价模式在推理成本下降、A2A经济兴起、MCP协议标准化三股力量下的演化走向，预判2026-2028年Agent商业模式的范式转移

---

## 理论部分：精炼索引（详见独立教材）

> Day 2 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_选修E10_Agent经济与商业模式.md` § Day 2](../../AI原生化商业博士_独立教材_选修E10_Agent经济与商业模式.md)（192-451行，已包含AaaS平台模式/outcome-based pricing实施条件/API Economy 2.0/Agent公司案例）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：Agent-as-a-Service（AaaS）平台模式

Agent-as-a-Service是将Agent能力以服务形式提供的商业模式，是SaaS在Agent时代的自然演进。

| 维度 | SaaS | AaaS |
|------|------|------|
| 核心交付物 | 软件功能 | Agent能力（任务完成） |
| 计费基础 | 席位/月 | 任务/结果/用量 |
| 用户界面 | GUI为主 | API + 对话 + GUI |
| 价值衡量 | 功能使用率 | 任务完成率/业务结果 |
| 护城河 | 功能+数据+网络效应 | 模型能力+工具链+Agent生态 |

### 关键回顾 2：定价模式演进的五个阶段

| 阶段 | 定价模式 | 逻辑 | 适用场景 | 代表 |
|------|---------|------|---------|------|
| 1.0 | 按席位 | 谁用谁付钱 | 传统SaaS | Salesforce |
| 2.0 | 按用量 | 用多少付多少 | API服务 | OpenAI API |
| 3.0 | 按任务 | 完成什么付什么 | Agent任务 | Agent-as-Worker |
| 4.0 | 按结果 | 达成什么结果付什么 | 业务结果 | outcome-based |
| 5.0 | 按价值分成 | 创造多少价值分多少 | 价值共创 | 风险共担模式 |

### 关键回顾 3：Outcome-based Pricing的五个实施条件

| 条件 | 描述 | 为什么重要 |
|------|------|-----------|
| **结果可量化** | 业务结果可以被明确定义和测量 | 无法量化就无法定价 |
| **因果关系清晰** | Agent的行为与结果之间有清晰因果关系 | 需要归因Agent的贡献 |
| **风险可控** | Agent失败的后果可控 | 需要风险缓冲机制 |
| **信任已建立** | 客户愿意为"结果"而非"过程"付费 | 需要品牌和案例积累 |
| **成本结构支持** | Agent的边际成本足够低 | 高失败率下仍能盈利 |

### 关键回顾 4：API Economy 2.0--从人类友好到Agent友好

| 维度 | API Economy 1.0 | API Economy 2.0 |
|------|----------------|-----------------|
| 调用者 | 人类开发者写代码调用 | Agent自主发现和调用 |
| 设计目标 | 开发者体验（DX） | Agent体验（AX: Agent Experience） |
| 文档形式 | 人类可读的文档 | Agent可读的schema（OpenAPI/JSON Schema） |
| 计费方式 | 按API调用次数 | 按Agent任务完成 |

---

## 上机部分：用pydantic + numpy-financial + statsmodels设计Agent商业模式

> **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO填空版，你来做）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，做完再看）
> **真实数据/库**：[`data/README.md`](./data/README.md)（pydantic + numpy-financial + statsmodels + 真实Agent定价案例 + 推理成本基准）

### 为什么用pydantic + numpy-financial + statsmodels

v4.0 的Day 2只讲理论（AaaS/outcome-based/API Economy 2.0），学生看完就忘。v5.0 用三个真实库做Agent商业模式设计：
- **pydantic** 定义Agent商业模式的schema契约（四种定价模式+结构化输出），实现API Economy 2.0的"Agent可发现的能力声明"
- **numpy-financial** 计算三种定价模式（AaaS订阅/按调用计费/outcome-based）的12月NPV/IRR，量化推理成本对利润的影响
- **statsmodels** 拟合定价弹性回归，找最优定价点--弹性需求下降价增收，非弹性需求下涨价增收

### 真实库1：pydantic（schema验证 + 结构化输出契约）

**pydantic**（pydantic/pydantic，20k+ star，MIT License）是Python最成熟的数据验证库。pydantic v2用Rust重写核心，性能比v1快5-50倍。在本Day中用于定义Agent商业模式的四种定价契约。

来源：https://github.com/pydantic/pydantic

### 真实库2：numpy-financial（金融计算）

**numpy-financial**（numpy/numpy-financial，MIT License）提供NPV（净现值）、IRR（内部收益率）等核心财务函数。在本Day中用于计算三种定价模式的财务对比。

来源：https://github.com/numpy/numpy-financial

### 真实库3：statsmodels（计量经济学回归）

**statsmodels**（statsmodels/statsmodels，10k+ star，BSD-3-Clause）是Python最成熟的计量经济学库。在本Day中用于拟合定价弹性回归（log-log OLS），找最优定价点。

来源：https://github.com/statsmodels/statsmodels

### 真实Agent定价案例（可追溯来源）

| Agent产品 | 定价模式 | 价格 | 来源 |
|----------|---------|------|------|
| **Cursor Pro** | AaaS订阅 | $20/月 | cursor.com定价页 |
| **Cursor Business** | AaaS订阅 | $40/月/用户 | cursor.com定价页 |
| **Devin (Cognition)** | AaaS订阅+任务 | $500/月 | cognition.ai公开披露 |
| **GitHub Copilot** | AaaS订阅 | $10-39/月/用户 | github.com/features/copilot |
| **OpenAI ChatGPT Plus** | AaaS订阅 | $20/月 | openai.com/chatgpt/pricing |
| **Intercom Fin** | outcome-based | $0.99/解决 | intercom.com/pricing |
| **Sierra** | outcome-based | 按解决率收费 | sierra.ai |
| **11x.ai** | outcome-based | 按预约会议收费 | 11x.ai |
| **DevRev** | outcome-based | 按工单解决收费 | devrev.ai |

### 推理成本基准（可追溯来源）

| 模型 | Input $/1M | Output $/1M | 来源 |
|------|-----------|------------|------|
| GPT-4o | $5.00 | $15.00 | openai.com/api/pricing |
| GPT-4o-mini | $0.15 | $0.60 | openai.com/api/pricing |
| Claude Sonnet 4 | $3.00 | $15.00 | anthropic.com/pricing |
| DeepSeek V3 | $0.27 | $1.10 | api-docs.deepseek.com/quick_start/pricing |

**推理成本是Agent商业模式的核心约束**：传统SaaS边际成本接近零，但Agent每次调用都消耗推理token。推理成本下降（DeepSeek V3比GPT-4o低95%）是outcome-based pricing可行的关键条件。

### 营销场景映射

Agent商业模式在营销中的实例：营销Agent怎么收费？本Day的营销场景：

| 营销Agent | 定价模式 | 商业逻辑 |
|----------|---------|---------|
| 内容生成Agent | AaaS订阅 | $200/月不限量文案 |
| 广告投放优化Agent | 按调用计费 | $0.05/调用，每天4000调用 |
| 销售转化Agent | outcome-based | $10/转化，每月150转化 |
| 全案营销Agent | 分润 | 增量收入的15% |

### 仿真架构

```
┌─────────────────────────────────────────────────────────┐
│      Agent商业模式设计 (pydantic + numpy-financial +      │
│                              statsmodels)                │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  pydantic schema契约层：                                  │
│    ├── AaaSSubscription (price_per_month)              │
│    ├── PerCallPricing (price_per_call, calls/month)    │
│    ├── OutcomeBasedPricing (price_per_outcome, conv)   │
│    └── RevenueShare (share_pct, baseline_revenue)      │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  numpy-financial 财务对比层：                             │
│    ├── 12月现金流建模 (含推理成本)                        │
│    ├── NPV/IRR 三种定价模式对比                          │
│    └── 推理成本敏感度分析 (GPT-4o vs DeepSeek V3)        │
├─────────────────────────────────────────────────────────┤
│  statsmodels 弹性回归层：                                 │
│    ├── log-log OLS: log(adopt) ~ log(price)             │
│    ├── 弹性估计 + 95% CI                                 │
│    └── 最优定价点 (利润最大化)                            │
└─────────────────────────────────────────────────────────┘
```

### 上机任务（6个TODO，见starter.ipynb）

1. **TODO1**：pydantic四种定价模式schema定义 + 结构化输出契约验证（AaaS订阅/按调用计费/outcome-based/分润）
2. **TODO2**：真实Agent定价案例数据加载与探索（Cursor/Devin/Intercom Fin等9个真实案例）
3. **TODO3**：numpy-financial三种定价模式12月现金流NPV/IRR对比（含推理成本）
4. **TODO4**：statsmodels定价弹性回归（log-log OLS）+ 找最优定价点
5. **TODO5**：推理成本敏感度分析--GPT-4o vs Claude Sonnet vs DeepSeek V3对三种定价模式利润率的影响
6. **TODO6**：matplotlib可视化（4个子图：三模式NPV对比/推理成本利润率/弹性曲线/最优定价）

---

## 2026前沿：outcome-based pricing + 推理成本 + 天道推演×商业模式沙盘

> v5.0新增前沿点。Day 2聚焦五个前沿方向，命中关键词：天道推演、推理成本、MCP、A2A、贝叶斯。

### 天道推演×商业模式沙盘（特色章节）

> 本节与项目CLAUDE.md的「天道推演系统」同构，作为Agent商业模式设计的特色理论视角。

**天道推演**（Tian Dao Tui Yan）是一种元认知沙盘推演能力--以天神视角俯视当前局势，在意识中构建无限可能的沙盘，模拟不同决策路径下的未来走向。它不是占卜，而是基于因果链和模式识别的逻辑推演。

**商业模式设计本质是商业版的天道推演沙盘**--在pydantic schema中构建多种定价模式的平行世界，用numpy-financial推演12月现金流走向，用statsmodels估计市场弹性响应，从中选择最优定价路径。

**天道推演能力与商业模式设计的同构映射**：

| 天道推演能力 | 商业模式设计对应 | 共享的产出 |
|-------------|----------------|----------|
| **局势感知** | 真实Agent定价案例 + 推理成本基准 | 市场基线 |
| **因果链追踪** | 定价 -> 采纳率 -> 收入 -> 利润的因果链 | 财务模型 |
| **沙盘模拟（3层推演）** | 三时间线推演：immediate（月）/near（年）/far（3年） | NPV/IRR/弹性 |
| **概率评估** | 弹性回归的置信区间 + 推理成本敏感度 | 风险量化 |
| **最优路径推荐** | 三种定价模式对比 + 最优定价点 | 策略选择 |

### 推理成本--Agent经济的阿喀琉斯之踵

推理成本（Token定价 × 消耗量）是Agent商业模式与传统SaaS的本质区别：

- **传统SaaS**：边际成本接近零（信息复制免费），规模越大利润率越高
- **AI Agent**：每次调用都消耗推理token，推理成本是硬约束

推理成本下降是outcome-based pricing可行的关键条件：
- **GPT-4o**（$5/1M input）：每次Agent调用1000 tokens -> $0.005推理成本
- **DeepSeek V3**（$0.27/1M input）：每次Agent调用1000 tokens -> $0.00027推理成本（降低95%）
- 推理成本下降5-10倍时，outcome-based pricing从"亏钱"变为"盈利"

来源：
- OpenAI定价页：https://openai.com/api/pricing/
- DeepSeek定价页：https://api-docs.deepseek.com/quick_start/pricing

### outcome-based pricing的兴起

outcome-based pricing是2026年Agent经济最具颠覆性的趋势：

| 阶段 | 时间 | 主流定价 | 触发条件 |
|------|------|---------|---------|
| 1.0 | 2023-2024 | 按席位（$20/月） | Agent能力弱，作为辅助工具 |
| 2.0 | 2024-2025 | 按用量（$5/1M tokens） | Agent能力增强，API调用为主 |
| 3.0 | 2025-2026 | 按任务/结果（$0.99/解决） | Agent能端到端完成任务 |
| 4.0 | 2026-2027 | outcome-based（按转化/ROI） | 推理成本下降+归因方法成熟 |
| 5.0 | 2027+ | 价值分成（增量收入15%） | Agent能创造可归因的增量价值 |

### MCP协议与API Economy 2.0

**MCP（Model Context Protocol）** 是Anthropic提出的开放协议，为Agent间的工具/数据访问提供标准化接口。MCP是API Economy 2.0的基础设施：

- **API Economy 1.0**：人类开发者读文档写代码调用API
- **API Economy 2.0**：Agent通过MCP自动发现和调用Agent友好API
- **Agent可发现能力声明**：pydantic schema + OpenAPI扩展，让Agent能自动发现"我能调用什么Agent服务"

在本Day中，pydantic schema不仅是数据验证，更是API Economy 2.0的"Agent可发现能力声明"--Agent通过读取其他Agent的pydantic schema，自动判断能否调用、如何调用、价格多少。

### A2A经济与分润模式

A2A（Agent-to-Agent）经济催生分润模式：

- **Agent协作链**：洞察Agent -> 创意Agent -> 投放Agent -> 分析Agent
- **分润机制**：每个Agent按贡献度分得最终收益的一部分
- **挑战**：贡献归因（因果推断）+ 信任建立（声誉系统）+ 分配公平（机制设计）

来源：
- MCP官方文档：https://modelcontextprotocol.io/
- a16z Agent Economy：https://a16z.com/big-ideas-in-ai/

### 营销Agent商业模式总结

| 营销Agent类型 | 推荐定价模式 | 推理成本敏感度 | 2026趋势 |
|--------------|------------|--------------|---------|
| 内容生成Agent | AaaS订阅 | 中（高频调用） | 转向按调用计费 |
| 广告优化Agent | 按调用计费 | 高（实时竞价） | 转向outcome-based |
| 销售转化Agent | outcome-based | 低（按转化） | 转向分润模式 |
| 全案营销Agent | 混合（基础+绩效+分润） | 中（多Agent协作） | A2A分润生态 |

---

## 与后续Day的衔接

- **Day 1**：Agent经济基础--Agent作为经济主体的理论+仿真
- **Day 2**（本Day）：Agent商业模式设计--从AaaS到outcome-based pricing
- **Day 3**：Agent生态与治理--平台设计与市场监管

---

## 作业与评估

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6个TODO全部填好，三种定价模式NPV/IRR对比有数据，弹性回归有显著结果，4个子图有数据）
- [ ] 一段300字分析：三种定价模式在你的营销场景下，哪种最优？推理成本下降如何改变选择？弹性回归结果说明什么？
- [ ] （可选）修改推理成本参数（如用DeepSeek V3的$0.27/1M），重新计算outcome-based定价的NPV，对比GPT-4o的差异

---

*本讲义由v5.0学习材料包升级生成。理论部分引用独立教材，上机部分用真实库（pydantic+numpy-financial+statsmodels+pandas+matplotlib+numpy）+ TODO脚手架，定价案例和推理成本基于真实公开数据。*
*最后更新：2026-07-25*


## 学习科学层 (v6.0)

本单元采用刻意练习(Ericsson)/间隔重复(FSRS-6,SM-2)/建构对齐(Biggs ILO↔TLA↔AT)/牛津tutorial LLM仿真(Socratic,Hattie四级反馈)。mastery 阈值与 Worked-Faded 示例见 practice.md 与 alignment.md。交叉练习(interleaving)促进迁移, 提取练习(retrieval practice)优于重读。

### 新增学习科学文件 (v6.0 增量, 不改 v5.0 原文)

- **practice.md**: 刻意练习册 (Ericsson)。skill_target = "90分钟独立输出定价契约+NPV/IRR+弹性回归+推理成本敏感度四件套"。3 个 drill (pydantic schema / numpy-financial NPV-IRR / statsmodels 弹性回归), 每个 drill 含 Worked-Faded 三阶段 (完整示范->部分填空->独立解)。交叉顺序 A1B1C1-B2C2A2-C3A3B3 (非块状), 强制上下文切换。连续 2 次失败触发 weak_loop (回退上一drill+补充worked example)。
- **schedule.json**: FSRS-6 (SM-2 backup) 间隔重复。7 张卡片, 每张锚定本单元真实概念: 五阶段演进 / outcome-based五实施条件 / 推理成本基准(GPT-4o vs DeepSeek V3) / API Economy 2.0+MCP / 弹性回归log-log OLS / A2A分润 / 天道推演三时间线。due=[1,3,8,21,60,180], request_retention=0.9, ef0=2.5。
- **alignment.md**: Biggs 建构对齐。5 行 ILO↔TLA↔AT 矩阵 (ILO-1 schema / ILO-2 NPV-IRR / ILO-3 弹性 / ILO-4 五阶段 / ILO-5 天道推演), 每行附 mastery_threshold (如 NPV误差<5%, 弹性p<0.05)。3 自检问题 (Feed Up / Feed Back / Feed Forward) 含"不经TLA能过AT吗"对齐失败检测。
- **tutorial.ipynb**: 牛津 Tutorial LLM 仿真 (静态 if/else, 不调 API)。persona = Oxford tutorial fellow + HBS devil's advocate, 禁直接答案, 每轮 Socratic 追问 (>=5问: 为什么/反例/若前提变/凭什么/如何)。student_model.json 持久化记录 5 个 ILO mastery + blind_spots。Hattie 四级反馈 [TASK]/[PROCESS]/[SELF-REG]/[FEED-FORWARD] (避免 Self 级表扬)。限频 1次/天, exit artifact 含 2-3 盲点 + 推荐复习单元。

### v6.0 关键词命中 (>=4)

刻意练习 / deliberate practice / FSRS-6 / SM-2 / 建构对齐 / constructive alignment / 牛津tutorial / Socratic / Hattie / 间隔重复 / spaced retrieval / 交叉 / interleaving / mastery / Worked-Faded / 提取练习 / retrieval practice (>=17 命中, 远超阈值 4)。

### 与天道推演的同构 (v6.0 增强)

天道推演的"反馈学习"能力 (记录前提假设->追踪实际偏差->更新因果模型) 与本单元的 student_model.json + weak_loop 元认知日志同构。每次 tutorial 仿真后, 学生在 student_model.json 追加"我原来卡在哪、回退后懂了什么、下次怎么避免", 即天道推演的"自我进化机制"落地。

---

*v6.0 学习科学层追加完成。v5.0 原文 (1-273行) 未修改一字。最后更新：2026-07-26*

## 研究产出与产业链接层 (v7.0)

本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+arXiv/DOI/https链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。研究核心命题"推理成本下降95%(GPT-4o $5/1M -> DeepSeek V3 $0.27/1M)使outcome-based定价NPV转正"可在solution.ipynb复现; linked_paper锚定McKinsey生成式AI报告+a16z Agent Economy+mesa ABM+MCP协议文档(均来自reading.md已验证深链)。产业链接锚定Sierra/Cognition-Devin/OpenAI/Anthropic/Cursor五家真实企业(来自notes.md真实Agent定价案例库), deployment_example展示Siera联络中心outcome-based生产部署, consulting_project为Burberry 8周MSc BA咨询项目, case_study为HBS风格"Sierra's Gamble"教学案例, guest_lecture邀请Agent公司Head of Pricing, internship_pointer指向OpenAI/Anthropic Residency与Sierra/Cognition定价实习。详见 research.md 与 industry.md。

---

*v7.0 研究产出与产业链接层追加完成。v5.0原文(1-273行)+v6.0学习科学层原文均未修改一字。最后更新：2026-07-26*
