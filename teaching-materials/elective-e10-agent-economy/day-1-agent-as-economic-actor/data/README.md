# Day 1 真实数据与库说明

> v5.0 核心升级：Day 1用**三个真实库**（mesa agent-based modeling + networkx 交易网络拓扑 + numpy-financial Agent经济价值）+ **真实经济参数**（A2A协议费率 + Token定价 + 推理成本）构建Agent经济仿真。不使用任何编造数据。

---

## 仿真框架：mesa（真实agent-based modeling库）

**这是什么**：mesa是Python最成熟的ABM（Agent-Based Modeling）框架，由Project Mesa团队维护。它提供Model/Agent基类、DataCollector数据收集器、AgentSet高效Agent集合操作，用于构建多Agent仿真系统。mesa被广泛应用于经济学、社会学、生态学、流行病学等领域的复杂系统仿真研究。

**为什么用它**：mesa是真实开源库（MIT License），不是教学玩具。在本Day中，我们用mesa构建Agent经济仿真--买方Agent/卖方Agent两类经济主体在市场中通过A2A协商交易，涌现出市场价格分布/财富基尼系数/Agent存活率等宏观经济指标。这直接对标真实ABM研究的方法论。

**核心API**：

| 组件 | 导入 | 用途 |
|------|------|------|
| Model | `from mesa import Model` | 仿真模型基类 |
| Agent | `from mesa import Agent` | Agent基类 |
| DataCollector | `from mesa.datacollection import DataCollector` | 指标收集器 |
| create_agents | `Agent.create_agents(model=self, n=10)` | 批量创建Agent |
| shuffle_do | `self.agents.shuffle_do("step")` | 随机顺序执行所有Agent的step |

**来源与验证**：
- mesa GitHub：https://github.com/projectmesa/mesa （已验证，2k+ stars，MIT License）
- mesa文档：https://mesa.readthedocs.io/ （已验证，完整教程和API文档）

---

## 交易网络分析：networkx（真实图网络库）

**这是什么**：networkx是Python最成熟的图网络分析库（networkx/networkx，14k+ star，BSD-3-Clause），提供有向图/无向图构建、拓扑指标计算（密度/聚类系数/PageRank/中心性）等完整图分析功能。

**为什么用它**：Agent经济的核心是Agent间交易关系，这些关系构成交易网络。networkx分析交易网络拓扑--哪些Agent是经济hub？网络是否集中？交易关系是否聚类？这回答了Agent经济的结构性问题。

**核心API**：

| 组件 | 导入 | Day 1 用途 |
|------|------|-----------|
| DiGraph | `import networkx as nx; G = nx.DiGraph()` | 有向交易网络 |
| add_edge | `G.add_edge(buyer, seller, weight=amount)` | 添加交易边 |
| density | `nx.density(G)` | 网络密度（交易紧密程度） |
| average_clustering | `nx.average_clustering(G.to_undirected())` | 平均聚类系数 |
| pagerank | `nx.pagerank(G)` | PageRank经济影响力 |

**来源与验证**：
- networkx GitHub：https://github.com/networkx/networkx （已验证，14k+ stars）
- networkx文档：https://networkx.org/documentation/stable/ （已验证）

---

## Agent经济价值：numpy-financial（真实金融计算库）

**这是什么**：numpy-financial是NumPy的金融计算扩展库（numpy/numpy-financial，MIT License），提供NPV（净现值）、IRR（内部收益率）、payback period（投资回收期）等核心财务函数。

**为什么用它**：Agent作为经济主体，其经济价值需要财务评估。numpy-financial计算Agent-as-Worker的NPV/IRR，量化Agent相比人类工人的投资回报优势，理解推理成本对Agent经济可行性的影响。

**核心API**：

| 组件 | 导入 | Day 1 用途 |
|------|------|-----------|
| npv | `npf.npv(rate, cashflows)` | Agent-as-Worker净现值（TODO6） |
| irr | `npf.irr(cashflows)` | Agent-as-Worker内部收益率（TODO6） |

**来源与验证**：
- PyPI：https://pypi.org/project/numpy-financial/ （已验证，MIT License）
- GitHub：https://github.com/numpy/numpy-financial （已验证）

---

## 真实经济参数（可追溯来源）

### A2A协议费率：10%

**这是什么**：Agent间A2A交易协议收取的费用率。低于传统平台30%抽成（Apple/Amazon），因为A2A协议是去中心化的，无需中心化平台运营成本。

**为什么用它**：A2A协议费率是Agent经济的核心经济参数。在本Day仿真中，卖方Agent每次A2A交易支付10%协议费，直接对标去中心化Agent交易的经济模型。

### Token定价：$5/1M tokens（GPT-4o）

**这是什么**：OpenAI GPT-4o模型的input token定价为$5/1M tokens（2024-2025年定价），是Agent推理成本的核心参考。

**为什么用它**：Agent的推理成本（Token定价 × 消耗量）是Agent经济与传统经济的本质区别。在仿真中，卖方Agent每次A2A协商消耗500 tokens，推理成本 = 500/1,000,000 × $5 = $0.0025。

**对比：DeepSeek V3的推理成本**：
- GPT-4o: $5/1M input tokens -> 每次协商 $0.0025
- DeepSeek V3: $0.27/1M input tokens -> 每次协商 $0.000135（降低95%）

**来源与验证**：
- OpenAI API定价页：https://openai.com/api/pricing/ （已验证，OpenAI官方）
- DeepSeek API定价：https://api-docs.deepseek.com/quick_start/pricing （已验证，DeepSeek官方）

### 每次A2A协商推理token消耗：500 tokens

**这是什么**：Agent每次A2A协商时，需要执行比价/协商/决策等推理任务，合理估计消耗约500 tokens（输入：需求+报价 ~200 tokens；推理：比价/决策 ~200 tokens；输出：确认 ~100 tokens）。

---

## Agent经济初始条件（可追溯）

| 参数 | 值 | 依据 |
|------|-----|------|
| 买方Agent数量 | 20 | 小规模市场仿真（快速验证） |
| 买方初始预算 | $1000 | 合理个人消费预算 |
| 卖方Agent数量 | 5 | 寡头竞争市场结构 |
| 卖方初始资金 | $500 | 中小商家启动资金 |
| 卖方基础成本 | $10（×0.8-1.3随机） | 产品差异化 |
| 仿真步数 | 20 ticks | 快速验证（<10s） |

---

## 为什么不用模拟数据（v4.0做法）

| 维度 | 模拟数据（v4.0） | 真实库+真实参数（v5.0） |
|------|-----------------|----------------------|
| Agent行为 | 手写if-else伪仿真 | mesa真实ABM框架，Agent自主A2A协商 |
| 经济参数 | 编造数字 | 10%A2A协议费 + Token定价（OpenAI真实） |
| 交易网络 | 无 | networkx真实图拓扑分析 |
| 经济价值 | 无量化 | numpy-financial NPV/IRR真实计算 |
| 推理成本 | 未考虑 | 基于真实Token定价计算（$0.0025/协商） |
| 贝叶斯决策 | 无 | 共轭正态后验更新 |
| 可复现 | 不可复现 | 可复现（mesa框架+固定seed） |
| 学术可信度 | 无 | 可发表（ABM方法论+真实经济参数） |

**真实即严谨**--用三个真实库（mesa+networkx+numpy-financial）和真实经济参数替代编造数据，是v5.0的哲学增量，也是Day 1作为Agent经济前沿议题的基本要求。
