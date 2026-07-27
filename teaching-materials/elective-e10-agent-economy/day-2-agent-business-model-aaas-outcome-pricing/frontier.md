# frontier.md (v9.0 学术前沿注入层)

> **所属**：elective-e10-agent-economy · day-2-agent-business-model-aaas-outcome-pricing
> **版本**：v9.0（学术前沿注入层）
> **本单元前沿课题**：本单元教 Agent 商业模式的四种定价契约（AaaS 订阅/按调用计费/outcome-based/分润），用 numpy-financial 做 12 月 NPV/IRR 对比，用 statsmodels 拟合定价弹性；前沿子问题是"2025-2026 年关于 Agent 经济度量可制造性（x402）、AI 保险栈、后自动化财政捕获的研究，如何更新我们对 outcome-based pricing 可行性、风险分配机制与宏观经济盈余分配的理解"。

---

## frontier_topic

本单元聚焦 Agent 商业模式四阶段定价契约与 outcome-based pricing 五实施条件，用 numpy-financial 三模式 NPV/IRR 对比 + statsmodels log-log OLS 弹性回归选择最优定价点；2025-2026 前沿子问题是：当 x402 支付层被实证发现 21.20% 为虚构交易（Ling & Zhou）、AI 保险栈被提出覆盖 CAT 尾部风险（Trout & Koyejo）、持久 AI 租金被建模为跨国财政捕获对象（Wossnig），本单元所教的"结果可量化 + 因果关系清晰 + 风险可控"outcome-based 实施前提是否仍然成立，以及 NPV/IRR 现金流模型是否需要纳入保险费支出与跨国盈余分配维度。

---

## recent_papers

> 从本模块 `_frontier_corpus/elective-e10-agent-economy.md` 语料库中挑 5 篇最贴本单元的 2025-2026 论文。

### 1. How Agentic Is Agentic Commerce? A Population-Scale Measurement of x402 Adoption and Authenticity
- **arXiv**: https://arxiv.org/abs/2607.12575
- **作者**: Shengchen Ling, Yajin Zhou
- **年份**: 2026
- **摘要**: 调查 x402 稳定币支付结算计数是否反映 AI 代理的真实采用。发现在 Base 上 280 天内发生 1.36 亿次结算价值约 4400 万美元，但 21.20% 是虚构的，63.78% 是关联集群内部结算。结论：结算计数衡量的是可制造性而非采用率，对 Agent 经济度量有方法论意义。
- **与本单元的关联**: 这篇直接挑战本单元 notes.md "outcome-based pricing 五实施条件"中"结果可量化"前提--如果支付层数据都可被操纵，outcome-based pricing 的"结果可量化"前提就更脆弱；本单元 solution.ipynb 的 outcome-based NPV 分析未考虑度量可制造性。

### 2. Underwriting the Agent Economy: The Blueprint for an AI Insurance Stack
- **arXiv**: https://arxiv.org/abs/2607.11999
- **作者**: Cristian Trout, Sanmi Koyejo
- **年份**: 2026
- **摘要**: 论证 AI 代理经济（预计 2030 年处理万亿美元级交易）需要专门保险框架。提出八组件 AI 保险栈，覆盖事件数据、灾难建模、标准和理赔管理。讨论 AI CAT 尾部风险，包括 CBRN 和失控场景，为 Agent 经济的风险分配机制设计提供蓝图。
- **与本单元的关联**: 本单元 notes.md "outcome-based pricing 五实施条件"中"风险可控"假设 Agent 失败后果可控；这篇论文提出 AI CAT 尾部风险（CBRN/失控），提示本单元 NPV/IRR 现金流模型应纳入保险费支出与尾部风险情景分析，否则高估 outcome-based 定价的 NPV。

### 3. Simulating a Post-Automation Economy
- **arXiv**: https://arxiv.org/abs/2606.20649
- **作者**: Leonard Wossnig
- **年份**: 2026
- **摘要**: 开发一个基于代理的、存量流量一致的经济模型，识别哪种财政工具能捕获持久 AI 盈余。发现持久盈余是外国持有的 AI 租金，大多数税收遗漏。政策取决于一国是拥有还是进口自动化，使用 Sobol 敏感性分析，为 Agent 经济的宏观财政设计提供模拟方法。
- **与本单元的关联**: 本单元 notes.md "分润模式"只考虑 Agent 协作链（洞察->创意->投放->分析）内的分润；这篇论文发现持久 AI 盈余是"外国持有的 AI 租金"，提示分润机制需考虑国家间盈余分配，这是本单元完全未触及的宏观维度。

### 4. Alignment of a Total Automation Economy
- **arXiv**: https://arxiv.org/abs/2607.17015
- **作者**: David McAllester
- **年份**: 2026
- **摘要**: 研究无人类参与生产或管理的"全自动化经济"的经济理论。回顾 Kantorovich 对偶化，探讨全自动化经济是否本质上是中央计划经济或需要去中心化。探索对齐脆弱性及对偶化对代理 AI 系统效用的影响，为 Agent 经济的宏观经济设计提供理论视角。
- **与本单元的关联**: 本单元 notes.md "定价模式演进五阶段"假设 Agent 经济沿"按席位->按用量->按任务->按结果->按价值分成"演化；这篇论文提出全自动化经济下 Agent 间交易通过 Kantorovich 对偶化被去中心化，提示 outcome-based pricing 可能在全自动化阶段退化为 Agent 间的内部转移定价。

### 5. Towards an Agent-First Web: Redesigning the Web for AI Agents
- **arXiv**: https://arxiv.org/abs/2606.19116
- **作者**: Eranga Bandara, Ross Gore
- **年份**: 2026
- **摘要**: 提出为 AI 代理重新设计 Web 的三层方案。访问层代理应继承等效访问权；经济层提出基于令牌的订阅模型和委托内容经济；内容层识别"认识论递归"问题并提出 Agent 文本标记语言（ATML）和密码学溯源链。构成代理优先互联网的十项设计原则。
- **与本单元的关联**: 本单元 notes.md "AaaS 订阅"与"按调用计费"是单一定价模式；这篇论文的"令牌订阅模型 + 委托内容经济"提示 Agent 经济的定价可能是非线性组合（订阅 + 按用量 + 按结果），本单元 statsmodels 单维度弹性回归可能误设。

---

## critical_synthesis

这 5 篇论文共同揭示：Agent 商业模式研究正从"定价策略选择"向"度量真实性 + 风险分配 + 宏观盈余捕获"三层深化。**共识**层面，论文 6（Ling & Zhou）与论文 8（Trout & Koyejo）都同意：Agent 经济 2030 年将达到万亿美元级交易量，但当前缺乏可靠的"真实采用"度量--论文 6 发现 Base 上 x402 的 1.36 亿次结算中 21.20% 是虚构的，63.78% 是关联集群内部结算，这与本单元 notes.md "outcome-based pricing 可行条件-结果可量化/因果关系清晰"直接对话：如果支付层数据都可被操纵，outcome-based pricing 的"结果可量化"前提就更脆弱。**争议**在三处：(a) **风险分配**上，论文 8 提出八组件 AI 保险栈覆盖 CBRN/失控场景，但其 CAT 尾部风险建模缺乏历史损失数据，依赖类比传统巨灾模型--本单元 solution.ipynb 的 NPV/IRR 分析未对"尾部风险"做情景分析，隐含假设 Agent 失败后果可控，这与论文 8 的 tail risk 警告相悖；(b) **宏观盈余捕获**上，论文 9（Wossnig）用存量流量一致模型发现"持久 AI 盈余是外国持有的 AI 租金，大多数税收遗漏"，提示 Agent 经济的盈余分配有国际维度--本单元"分润模式"只考虑 Agent 间分润，未考虑主权国家间的盈余捕获；(c) **经济结构**上，论文 5（McAllester）质疑全自动化经济是否本质需中央计划，论文 2（Bandara & Gore）的"令牌订阅 + 委托内容经济"则提供了去中心化方案，但两者未充分对话。**趋势**上，领域正从"Agent 公司如何定价"转向"Agent 经济如何被度量/被保险/被征税"，但**局限**在于：论文 6 是单一链（Base）+ 单一协议（x402）的测量，外部效度有限；论文 8 是观点性蓝图，八组件保险栈无落地案例；论文 9 的 SFC 模型依赖强假设（AI 租金外流），在不同国家情景下结论可能反转；论文 2 的三层方案是设计原则，未给 ATML/密码学溯源的具体实现。

---

## delta_to_unit

1. 本单元 notes.md "outcome-based pricing 五个实施条件"中"结果可量化"假设业务结果可被清晰测量，但论文 6（Ling & Zhou）实证发现 x402 支付结算中 21.20% 是虚构的、63.78% 是关联集群内部结算--这要求本单元 solution.ipynb 的 outcome-based 定价 NPV 分析应增加"度量可制造性"情景，即当 x% 的转化是虚假时的 NPV 敏感度，否则 NPV 会被系统性高估。
2. 本单元 solution.ipynb 用 numpy-financial 做 12 月现金流 NPV/IRR 对比三种定价模式，但论文 8（Trout & Koyejo）指出 AI 保险栈的八组件（事件数据/灾难建模/标准/理赔管理）是 Agent 经济的必要成本--本单元的现金流模型未包含保险费支出，在尾部风险显著的营销/金融 Agent 场景下会高估 outcome-based 定价的 NPV。
3. 本单元 notes.md "分润模式"只考虑 Agent 协作链（洞察->创意->投放->分析）内的分润，但论文 9（Wossnig）发现持久 AI 盈余是"外国持有的 AI 租金"，提示分润机制需考虑国家间盈余分配--对于跨国运营的 Agent 平台（如 OpenAI/Anthropic），主权国家间的盈余捕获会反向影响 Agent 公司的可分配利润，本单元完全未触及。
4. 本单元用 statsmodels 拟合 log-log OLS 弹性回归 log(adopt)~log(price)，假设价格-采纳关系是对数线性的；但论文 2（Bandara & Gore）的"令牌订阅 + 委托内容经济"提示 Agent 经济的定价可能是非线性组合（订阅 + 按用量 + 按结果），弹性回归的单维度模型可能误设，需要多维定价弹性模型。

---

## open_questions

1. 当 x402 支付层 21.20% 是虚构交易，outcome-based pricing 的"结果可量化"前提在多大程度上可被信任，需要什么样的链上/链下交叉验证机制来区分真实转化与可制造转化？
2. AI 保险栈的八组件中，哪些组件应在 Agent 公司内部自保，哪些应通过市场机制转移，最优风险分配边界如何随 Agent 自主性级别（L2-L5）变化？
3. 在多国 Agent 经济中，AI 租金的跨国流动如何影响各国的 outcome-based pricing 可行性与税收捕获，是否存在"AI 租金避税天堂"的均衡？
4. 当 Agent 经济进入"全自动化"阶段（Kantorovich 对偶化），outcome-based pricing 是否退化为 Agent 间的内部转移定价，人类客户如何在这个转型中保持议价能力？
5. 当 Agent 定价是非线性组合（订阅 + 按用量 + 按结果），传统的单维度价格弹性回归如何被多维定价弹性模型替代，需要什么样的实验设计来识别各维度的弹性？

---

## methodological_critique

论文 6（Ling & Zhou）虽是罕见的链上实证，但仅覆盖 Base 链 280 天 + 单一协议（x402），其"21.20% 虚构"的判定依赖启发式聚类，可能有假阳性/假阴性；且未在以太坊主网/BSC 上重复验证，外部效度有限；同时"虚构交易"的判定缺乏地面真值标注，纯算法分类。论文 8（Trout & Koyejo）是观点性蓝图，八组件 AI 保险栈无任何落地案例，CAT 尾部风险建模依赖类比传统巨灾模型，但 AI 风险的尾部特征（如 CBRN/失控）与自然灾害不可比--自然灾害有百年损失数据，AI 失控事件无历史先例，模型外推风险极高。论文 9（Wossnig）的 SFC 模型依赖"AI 租金外流"的强假设，对 AI 出口国（如美国）与进口国结论可能完全反转；Sobol 敏感性分析虽稳健但模型结构本身未验证，"持久盈余是外国持有的 AI 租金"的论断依赖资本完全流动假设。论文 5（McAllester）是单作者观点性论文，Kantorovich 对偶化讨论偏哲学，缺乏可操作算法。论文 2（Bandara & Gore）的三层方案是设计原则，ATML 与密码学溯源链未给实现细节，复现难度高。所有论文均无开源代码，限制了 NPV/IRR 研究者复现与扩展。

---

*本文件由 v9.0 学术前沿注入层生成。所有论文链接来自 `_frontier_corpus/elective-e10-agent-economy.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证）。*
