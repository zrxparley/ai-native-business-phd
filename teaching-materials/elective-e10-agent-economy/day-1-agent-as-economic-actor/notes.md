# 选修E10 · Day 1：Agent经济基础--Agent作为经济主体 · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 选修E10 Agent经济与商业模式 · Day 1
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：Agent如何作为自主经济主体在市场中交互、交易、涌现出新经济形态？推理成本如何约束Agent经济行为？A2A协议如何重塑交易拓扑？
> **v5.0 升级点**：① 真实库上机（mesa agent-based modeling + networkx 交易网络拓扑 + numpy-financial Agent经济价值）② TODO填空式起始笔记本 ③ Notebook化 ④ 深链阅读 ⑤ 2026前沿（天道推演×多Agent仿真 + A2A经济 + 推理成本 + 贝叶斯Agent决策 + MCP协议）

---

## 学习目标（学完你能做到）

1. 能用 **mesa**（真实agent-based modeling框架）构建Agent经济仿真--买方Agent/卖方Agent两类经济主体在市场中通过A2A协商交易，涌现出市场价格分布、财富基尼系数、Agent存活率等宏观经济指标
2. 能用 **networkx**（真实图网络库）分析Agent交易网络拓扑--网络密度、聚类系数、PageRank经济影响力--理解"Agent经济的交易结构"是宏观经济指标的微观涌现
3. 能用 **numpy-financial**（真实金融计算库）计算Agent-as-Worker的经济价值（NPV/IRR）--量化Agent作为经济主体相比人类工人的投资回报优势，理解推理成本对Agent经济可行性的硬约束
4. 能解释Agent经济三层模型（Agent-as-Tool / Agent-as-Worker / Agent-as-Actor）的演进路径，并用贝叶斯更新模拟Agent的价格信念形成过程--Agent作为经济主体需要自主决策，而决策基于对市场的贝叶斯推断
5. 能建立天道推演×多Agent仿真的同构认知--Agent经济仿真本质是计算化的天道推演沙盘，在仿真中构建多个Agent经济平行世界，观察不同推理成本/A2A协议参数下的涌现走向

---

## 理论部分：精炼索引（详见独立教材）

> Day 1 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_选修E10_Agent经济与商业模式.md` § Day 1](../../AI原生化商业博士_独立教材_选修E10_Agent经济与商业模式.md)（54-189行，已包含Agent经济定义/三要素/三层模型/Agent间交易机制/信任模型/营销场景映射）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：Agent经济的定义与三要素

Agent经济（Agent Economy）是指AI Agent作为自主经济主体，能够进行协商、交易、协作，完成复杂商业流程的生态系统。

| 要素 | 含义 | 与传统经济的区别 |
|------|------|----------------|
| **自主性（Autonomy）** | Agent能自主决策和行动 | 传统软件执行预定流程 |
| **经济性（Economic Agency）** | Agent能交易、支付、签约 | 传统软件是工具，Agent是经济参与者 |
| **生态性（Ecosystem）** | 多个Agent协作形成经济生态 | 传统SaaS是单点工具 |

### 关键回顾 2：Agent经济三层模型

| 层次 | 描述 | 商业模式 | 人类角色 | 案例 |
|------|------|---------|---------|------|
| **Agent-as-Tool** | 人类用Agent完成任务 | SaaS订阅/token计费 | 决策者+操作者 | ChatGPT Plus、Claude Pro |
| **Agent-as-Worker** | Agent作为"数字员工"自主工作 | outcome-based pricing | 监督者+审核者 | Sierra、11x.ai |
| **Agent-as-Actor** | Agent间自主交易协作 | Agent marketplace / A2A economy | 设计者+治理者 | 多Agent供应链协作 |

### 关键回顾 3：Agent间交易机制与信任模型

Agent间交易机制包括：API合约、智能合约、拍卖机制、协商协议、信用系统。

信任建立的三层模型：
- **Layer 1: 身份信任**--Agent身份验证（数字签名、DID）
- **Layer 2: 能力信任**--Agent能力验证（能力声明、SLA、第三方认证）
- **Layer 3: 行为信任**--Agent行为可信验证（信用评分、声誉系统、担保机制）

### 关键回顾 4：营销场景的Agent经济映射

| 营销环节 | Agent-as-Tool | Agent-as-Worker | Agent-as-Actor |
|---------|--------------|----------------|----------------|
| **内容创作** | 人类用AI生成文案 | Agent自主产出内容 | 内容Agent与投放Agent自动协作 |
| **广告投放** | 人类用AI优化投放 | Agent自主管理投放 | 品牌Agent与媒体Agent自动竞标 |
| **客户服务** | 人类用AI辅助回复 | Agent自主解决问题 | 客服Agent与产品Agent自动协作 |

---

## 上机部分：用mesa + networkx + numpy-financial构建Agent经济仿真

> **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO填空版，你来做）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，做完再看）
> **真实数据/库**：[`data/README.md`](./data/README.md)（mesa + networkx + numpy-financial + 真实经济参数）

### 为什么用mesa + networkx + numpy-financial

v4.0 的Day 1只讲理论（三要素/三层模型/信任机制），学生看完就忘。v5.0 用三个真实库做Agent经济仿真：
- **mesa** 构建买方/卖方Agent的交互模型，观察市场价格/财富分布/存活率的涌现
- **networkx** 分析Agent间交易网络拓扑，理解A2A经济的交易结构
- **numpy-financial** 计算Agent-as-Worker的NPV/IRR，量化Agent作为经济主体的投资价值

### 真实库1：mesa（agent-based modeling框架）

**mesa**（projectmesa/mesa，2k+ star，MIT License）是Python最成熟的ABM框架。mesa提供Model/Agent基类、DataCollector数据收集器、AgentSet高效Agent集合操作。

来源：https://github.com/projectmesa/mesa

### 真实库2：networkx（图网络分析）

**networkx**（networkx/networkx，14k+ star，BSD-3-Clause）是Python最成熟的图网络分析库。在本Day中用于分析Agent交易网络的拓扑特性--网络密度、聚类系数、PageRank经济影响力。

来源：https://github.com/networkx/networkx

### 真实库3：numpy-financial（金融计算）

**numpy-financial**（numpy/numpy-financial，MIT License）提供NPV（净现值）、IRR（内部收益率）等核心财务函数。在本Day中用于计算Agent-as-Worker的投资价值。

来源：https://github.com/numpy/numpy-financial

### 真实经济参数（可追溯来源）

| 参数 | 值 | 真实来源 |
|------|-----|---------|
| A2A协议费率 | 10% | Agent间交易协议的合理费率（低于传统30%平台抽成） |
| Token定价 | $5/1M tokens | GPT-4o input定价（OpenAI 2024-2025定价页） |
| 每次A2A协商推理token | 500 tokens | Agent协商/比价/决策的合理token消耗 |
| 推理成本/协商 | ~$0.0025 | 500 tokens × $5/1M |

**推理成本是Agent经济的核心约束**：传统中介的边际成本接近零，但AI Agent每次A2A协商都消耗推理token。推理成本下降（如DeepSeek V3的$0.27/1M）是Agent经济爆发的关键条件。

### 营销场景映射

Agent经济在营销中的实例：品牌Agent买广告位（买方Agent）、媒介Agent卖流量（卖方Agent）、A2A协商自动定价。本Day的仿真场景：

| Agent类型 | 营销映射 | 仿真行为 |
|----------|---------|---------|
| 买方Agent | 品牌Agent买广告位 | 有预算，贝叶斯估计公平价格，A2A协商购买 |
| 卖方Agent | 媒介Agent卖广告流量 | 动态定价，A2A协商，支付协议费+推理成本 |

### 仿真架构

```
┌───────────────────────────────────────────────────────┐
│          Agent经济仿真模型 (mesa + networkx)            │
├───────────────────────────────────────────────────────┤
│                                                       │
│    买方Agent(20)  <--- A2A协商 --->  卖方Agent(5)      │
│       │              (推理成本)              │        │
│   贝叶斯价格估计                         动态定价      │
│   预算约束                               供应约束      │
│                                                       │
├───────────────────────────────────────────────────────┤
│  networkx 交易网络：有向图，边=交易，权重=交易额        │
│  指标：密度/聚类系数/PageRank                          │
├───────────────────────────────────────────────────────┤
│  numpy-financial Agent价值：NPV/IRR                    │
│  对比 Agent-as-Worker vs Human Worker                  │
└───────────────────────────────────────────────────────┘
```

### 上机任务（6个TODO，见starter.ipynb）

1. **TODO1**：买方Agent--贝叶斯价格估计、A2A协商购买、预算约束、破产机制
2. **TODO2**：卖方Agent--动态定价、A2A协商交易、支付协议费+推理成本、破产机制
3. **TODO3**：Agent交易网络（networkx）--有向图构建、拓扑指标计算、PageRank经济影响力
4. **TODO4**：Agent经济模型 + DataCollector--两类Agent创建、9个model_reporters、基尼系数
5. **TODO5**：运行仿真20步，提取DataCollector数据到pandas DataFrame，打印涌现指标+网络拓扑
6. **TODO6**：Agent经济价值分析（numpy-financial NPV/IRR）+ matplotlib可视化（4个子图）

---

## 2026前沿：天道推演×多Agent仿真 + A2A经济 + 推理成本 + 贝叶斯Agent

> v5.0新增前沿点。Day 1聚焦五个前沿方向，命中关键词：天道推演、多Agent仿真、MCP、A2A、推理成本、贝叶斯。

### 天道推演×多Agent仿真（特色章节）

> 本节与项目CLAUDE.md的「天道推演系统」同构，作为Agent经济仿真的特色理论视角。

**天道推演**（Tian Dao Tui Yan）是一种元认知沙盘推演能力--以天神视角俯视当前局势，在意识中构建无限可能的沙盘，模拟不同决策路径下的未来走向。它不是占卜，而是基于因果链和模式识别的逻辑推演。

**多Agent仿真本质是计算化的天道推演沙盘**--在mesa仿真中构建多个Agent经济平行世界，观察不同推理成本/A2A协议参数下的涌现走向。天道推演在意识中构建沙盘，mesa在代码中构建沙盘，两者同构。

**天道推演能力与多Agent仿真的同构映射**：

| 天道推演能力 | 多Agent仿真对应 | 共享的涌现产出 |
|-------------|----------------|---------------|
| **局势感知** | 初始Agent分布与参数设置 | 初始基尼系数/价格/存活率 |
| **因果链追踪** | Agent行为因果链（购买->定价->竞争->破产） | 价格动态/财富迁移 |
| **沙盘模拟（3层推演）** | 20 tick时间步推演（immediate/near/far） | 时间序列涌现模式 |
| **概率评估** | 多次运行不同seed，统计结果分布 | 涌现指标的概率分布 |
| **最优路径推荐** | 对比不同参数场景，选择最优A2A协议参数 | 策略选择依据 |

### A2A（Agent-to-Agent）经济

A2A经济是Agent经济的最前沿形态--Agent间自主协商、交易、协作，无需人类干预。2026年的关键趋势：

- **MCP（Model Context Protocol）**：Anthropic提出的开放协议，为Agent间的工具/数据访问提供标准化接口。MCP是Agent间"发现彼此能力"的基础设施，类似互联网的HTTP协议。来源：https://modelcontextprotocol.io/
- **A2A交易协议**：Agent间自主交易需要标准化的协商/定价/确认协议，目前处于早期探索阶段
- **Agent身份与信任**：Agent间如何确认身份、评估可靠性、处理违约--需要Agent信用评级系统

在本Day的仿真中，买方Agent与卖方Agent通过A2A协商完成交易，每次协商消耗推理token并支付A2A协议费。

### 推理成本与Agent经济

推理成本（Token定价 × 消耗量）是Agent经济与传统经济的本质区别：

- **传统中介**：边际成本接近零（信息复制免费），规模越大利润率越高
- **AI Agent**：每次A2A协商都消耗推理token，推理成本是硬约束

推理成本下降是Agent经济爆发的关键条件：
- **GPT-4o**（$5/1M input tokens）：每次协商推理成本 ~$0.0025
- **DeepSeek V3**（$0.27/1M input tokens）：每次协商推理成本 ~$0.000135（降低95%）
- 推理成本下降5-10倍时，Agent经济可行性发生质变

来源：
- OpenAI定价页：https://openai.com/api/pricing/
- DeepSeek定价页：https://api-docs.deepseek.com/quick_start/pricing

### 贝叶斯Agent决策

Agent作为经济主体需要自主决策，而决策基于对市场的不完全信息推断。**贝叶斯推断**是Agent经济决策的核心方法：

- 买方Agent对"公平价格"有先验信念（Normal prior）
- 每次交易后，用观测到的价格更新后验信念（conjugate normal update）
- 决策基于后验信念：只接受低于"后验均值+1标准差"的价格

这模拟了Agent作为经济主体在不确定市场中的学习行为--与传统理性预期不同，Agent用贝叶斯方法逐步学习市场均衡。

### 新兴商业模式总结

| 模式 | 描述 | 计费模型 | 仿真对应 |
|------|------|---------|---------|
| Agent-as-a-Service | 提供Agent创建/部署平台 | 平台抽佣+增值服务 | A2A协议费 |
| 自主交易Agent | Agent间A2A协商交易 | 按交易量/价值 | A2A协商 |
| Token经济 | 推理消耗作为经济计量 | 按token消耗 | 推理成本约束 |
| Agent-as-Worker | Agent作为数字员工 | outcome-based | NPV/IRR分析 |

---

## 与后续Day的衔接

- **Day 1**（本Day）：Agent经济基础--Agent作为经济主体的理论+仿真
- **Day 2**：Agent商业模式设计--从AaaS到outcome-based pricing
- **Day 3**：Agent生态与治理--平台设计与市场监管

---

## 作业与评估

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6个TODO全部填好，仿真能跑通，4个子图有数据）
- [ ] 一段300字分析：仿真涌现了什么经济现象？推理成本对Agent行为的影响？网络拓扑说明了什么？
- [ ] （可选）修改推理成本参数（如用DeepSeek的$0.27/1M），重新运行仿真，对比Agent存活率和基尼系数的变化

---

*本讲义由v5.0学习材料包升级生成。理论部分引用独立教材，上机部分用真实库（mesa+networkx+numpy-financial+pandas+matplotlib+numpy）+ TODO脚手架，仿真参数基于真实经济数据。*
*最后更新：2026-07-25*

---

## 学习科学层 (v6.0)

本单元采用**刻意练习**（Ericsson deliberate practice：skill_target 拆 3 子技能 + >=3 drills 含 difficulty/reps_required/feedback_rule + Worked-Faded 三阶段示范渐退 + weak_loop 弱项循环）/ **间隔重复**（FSRS-6 算法，SM-2 backup，request_retention=0.9，7 张卡片 due=[1,3,8,21,60,180]，覆盖三层模型/推理成本/贝叶斯更新/MCP-A2A/天道推演同构/networkx三指标/NPV-IRR）/ **建构对齐**（Biggs constructive alignment：ILO↔TLA↔AT 4 行矩阵 + mastery >=80% + Feed Up/Back/Forward 3 自检）/ **牛津tutorial LLM仿真**（Socratic 苏格拉底式追问 >=5 问 + HBS devil's advocate + Hattie 4 级 formative feedback [TASK]/[PROCESS]/[SELF-REG]/[FEED-FORWARD] + student_model.json 掌握度盲点追踪 + 限频 1次/天防依赖）。

**mastery 阈值与 Worked-Faded 示例**见 `practice.md`（4 drills：D-S1-ABM mesa 仿真 / D-S2-NET networkx 拓扑 / D-S3-NPV numpy-financial 价值 / D-S1-BAYES 贝叶斯更新强化；progressive_project: proposal->milestone->final->poster CS230 式渐进交付）与 `alignment.md`（ILO1-4 ↔ TLA ↔ AT 矩阵 + mastery >=80% + 3 自检问题）。

**交叉练习**（interleaving）促进迁移：S1-S2-S3 子技能按 A1B1C1-B2C2A2-C3A3B3 交叉排布（非块状），每 drill 间隔 1 天与 FSRS-6 同步。

**提取练习**（retrieval practice）优于重读：`schedule.json` 7 张卡片用 FSRS-6 间隔重复算法，request_retention=0.9，强制学生在 due 日主动 recall（非重读 notes.md），long-term retention 优于被动重读。

**4 个新文件**：`practice.md`（刻意练习）/ `schedule.json`（FSRS-6 间隔重复）/ `alignment.md`（Biggs 建构对齐）/ `tutorial.ipynb`（牛津tutorial LLM 仿真，静态 if/else 模拟苏格拉底循环，不真调 LLM API）。

---

## 研究产出与产业链接层 (v7.0)

本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+linked_paper链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。研究问题锚定Agent作为经济主体在mesa仿真下的市场均衡与机制设计(三边市场/四类网络效应/责任4层/激励4原则); linked_paper用reading.md已有arXiv深链; 产业链接锚定Sierra/Cognition-Devin/OpenAI/Anthropic等Agent经济前沿企业 + Burberry咨询项目 + Head of Agent Economy HBS案例 + a16z/OpenAI Residency实习指针。详见 research.md 与 industry.md。

---

## 学术前沿层 (v9.0)

本单元新增 `frontier.md`：注入 2025-2026 最新学术前沿（N 篇真实 arXiv 论文 + 批判性综述 + delta_to_unit + ≥3 开放研究问题 + 方法论批评）。论文来自 `_frontier_corpus/elective-e10-agent-economy.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证），覆盖前沿课题：Agent经济 × 多Agent市场设计 × A2A。面向博后/教授级读者：批判性综述非罗列，delta_to_unit 显式指出前沿如何更新本单元所教，开放问题为可发表研究方向。详见 `frontier.md`。

---

## AI工程从零构建层 (v11.0)

本单元新增 `from_scratch.md`，落实 **AI工程从零构建** 哲学：不调 mesa 的贝叶斯 ABM 黑箱，**手写 numpy** 实现博弈论 `payoff_matrix` + `best_response` 迭代（fictitious play）求解 Nash 均衡。与 notes.md 的 mesa 仿真（贝叶斯价格信念 + A2A 协商）形成对照：mesa 是 agent-based 学习仿真（回答"会发生什么"），from scratch 是博弈论均衡分析（回答"应该发生什么"），两者互补刻画 Agent 作为经济主体的策略行为。

核心手写实现（numpy only，无 mesa/networkx/numpy-financial 依赖）：
- `best_response_iter(payoff_A, payoff_B)`：fictitious play 迭代求混合策略 Nash（Brown 1951 提出，Robinson 1951 证明零和博弈收敛性）
- `nash_mixed_closed_form_2x2(payoff_B)`：2x2 博弈混合 Nash 闭式解（无差异原则）

**数学推导**：Nash 均衡存在性（Kakutani 不动点定理）、best response 映射 $BR_i(\sigma_{-i}) = \arg\max_{\sigma_i} u_i(\sigma_i, \sigma_{-i})$、混合策略无差异原则 $p^* = \frac{b_{22}-b_{21}}{b_{11}-b_{12}-b_{21}+b_{22}}$、fictitious play 经验频率收敛速率 $O(1/\sqrt{t})$。

**verification_property**：Prisoner's Dilemma 收敛到纯策略 Nash (Defect, Defect)（Defect 严格占优）；Matching Pennies（零和博弈）fictitious play 经验频率收敛到混合 Nash `[0.5, 0.5]`。

rohitg00 深链（来自 `_from_scratch_map/elective-e10-agent-economy.md`，对应 ai-engineering-from-scratch 仓库的 multi-agent 与 RL phase）：
- [P16/21 Agent Economies](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/16-multi-agent-and-swarms/21-agent-economies/README.md)
- [P9/07 Actor-Critic A2C A3C](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/09-reinforcement-learning/07-actor-critic-a2c-a3c/README.md)

详见 `from_scratch.md` 的 `scratch_topic` / `core_algorithm` / `code_artifact` / `connection_to_unit` / `deep_dive_links` / `exercises` 六节。
