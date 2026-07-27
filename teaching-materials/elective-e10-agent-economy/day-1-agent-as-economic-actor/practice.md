---
unit: elective-e10-day-1
topic: Agent作为经济主体 (Agent as economic actor)
version: v6.0 学习科学层
skill_target: 能用 mesa 构建买方/卖方 Agent 经济仿真 (A2A 协商+贝叶斯价格信念+破产机制), 用 networkx 分析交易网络拓扑 (密度/聚类系数/PageRank 经济影响力), 用 numpy-financial 计算 Agent-as-Worker 的 NPV/IRR, 并解释推理成本对 Agent 经济可行性的硬约束。
---

# practice.md · 刻意练习 (Ericsson + MIT CS229 pset0 + Harvard/Stanford Worked-Faded)

> 本文件落实 Ericsson 刻意练习三要素：**具体可评估技能** + **即时反馈** + **重复到自动化**。所有 drill 的 feedback_rule 引用本单元真实库 (mesa/networkx/numpy-financial) 与真实参数 (A2A 协议费率 10% / GPT-4o $5/1M / DeepSeek V3 $0.27/1M / 500 tokens/协商)。

---

## diagnostic (先测, CS229 pset0 式 3 题, 探测先验缺口)

> 作答时间 15 分钟, 不计入评分, 仅用于暴露盲点。每题独立作答, 不查资料。

**D1. 贝叶斯先验后验**：买方 Agent 对公平广告位价格持有 Normal(μ=10, σ²=4) 的先验。第一次 A2A 协商中观测到卖方报价 12。假设观测噪声 σ_obs²=1。请手算后验 Normal(μ', σ'²) 的 μ' 和 σ'²。(提示：conjugate normal update)

**D2. 推理成本临界点**：A2A 协议费率 10%，每次协商消耗 500 tokens。若 Agent 单次交易额 \$1，GPT-4o 定价 \$5/1M tokens 时 Agent 净收益是多少？DeepSeek V3 \$0.27/1M 时呢？推理成本需下降到每 1M token 多少美元时, Agent 经济才在 \$1 交易额下盈亏平衡？

**D3. 网络拓扑经济意义**：mesa 仿真 20 步后, networkx 计算得到交易网络密度 0.15、聚类系数 0.42、PageRank top-1 节点 0.31。请用 1-2 句话解释这三个指标分别揭示了 Agent 经济的什么宏观现象？(避免 "网络密" 之类同义反复)

---

## subskills (3 个子技能, 拆自 skill_target)

| 子技能 | 描述 | 对应 TODO | 评估信号 |
|--------|------|----------|---------|
| **S1. mesa ABM 构建** | 买方/卖方 Agent 类、贝叶斯价格信念、A2A 协商、预算约束、破产机制、DataCollector 9 个 model_reporters | TODO1/TODO2/TODO4 | 仿真能跑通 20 步, 基尼系数有合理值 (0<)<1 |
| **S2. networkx 拓扑分析** | 有向交易图构建、密度/聚类系数/PageRank 计算、与宏观经济指标关联 | TODO3 | 三指标数值非 NaN, 能解释经济意义 |
| **S3. numpy-financial 价值分析** | Agent-as-Worker 现金流建模、NPV/IRR 计算、与人类工人对比、推理成本敏感性 | TODO5/TODO6 | NPV 符号正确, IRR 在合理区间, 4 子图齐全 |

---

## drills (>=3 个, 含 difficulty/reps_required/feedback_rule/worked_faded)

### drill_id: D-S1-ABM
- **difficulty**: 4
- **reps_required**: 3 (3 次独立运行, 不同 random_seed)
- **feedback_rule**: 跑通后, 检查 `model.datacollector.get_model_vars_dataframe()` 的 `gini` 列。若 gini 在 20 步内从 ~0 单调上升到 0.3-0.6 → 通过; 若 gini=0 或 NaN → 提示 "买方 Agent 的预算约束或破产机制未触发, 回看 TODO1 的 `if self.budget <= 0: self.remove()`"; 若 gini>0.9 → 提示 "卖方垄断, 检查 TODO2 卖方 Agent 数量是否太少 (本仿真 5 个)". 领域特定: 必须用 mesa 的 `DataCollector` 而非自建 list 收集; `model_reporters` 必须 >=9 项 (含 price_mean/price_std/gini/survival_rate/buyer_count/seller_count/total_trade_volume/a2a_fee_total/inference_cost_total)。
- **worked_faded** (三阶段, 示范->填空->独立):
  - **Worked (完整示范)**: 教师在 solution.ipynb 中完整展示 `class BuyerAgent(mesa.Agent)` 的 5 个方法 (`__init__/step/estimate_price/negotiate/pay`), 学生逐行注释每个方法对应贝叶斯更新的哪一步。
  - **Faded (部分填空)**: starter.ipynb TODO1 中保留 `__init__/step` 完整, 删除 `estimate_price/negotiate` 的 4 行核心代码 (后验均值/方差更新公式), 学生填空。
  - **Independent (独立解)**: 给定新的需求 (e.g., 把 Normal prior 改为 LogNormal prior), 学生独立修改 BuyerAgent 类, 不用 starter 模板。

### drill_id: D-S2-NET
- **difficulty**: 3
- **reps_required**: 2
- **feedback_rule**: 用 networkx 的 `nx.DiGraph()`, 边权 = 交易额。若 `nx.density(G) < 0.05` → 提示 "Agent 间交易太少, 检查是否所有买方都只与 1 个卖方交易 (中心化垄断)"; 若 `nx.pagerank(G)` top-1 节点 PageRank > 0.5 → 提示 "高度中心化, 该卖方是事实上的做市商, 联系 A2A 经济的'Agent marketplace' 商业模式"; 若聚类系数 = 0 → 提示 "无三方交易环路, 这与 A2A 协议是否支持多边交易有关". 领域特定: 必须区分有向图 (买->卖) 与无向图, PageRank 用在有向图才有经济意义 (资金流向影响力)。
- **worked_faded**:
  - **Worked**: 教师在 solution 中展示完整 `build_trade_graph(model)` 函数, 逐行说明 `G.add_edge(buyer_id, seller_id, weight=trade_amount)` 的方向含义。
  - **Faded**: starter TODO3 保留 `G = nx.DiGraph()` 与遍历 model.agents 的循环, 删除 `density/pagerank/clustering` 三行计算, 学生填空。
  - **Independent**: 学生独立改写为 "时间切片图" -- 每个 tick 一个子图, 计算拓扑指标的时间序列。

### drill_id: D-S3-NPV
- **difficulty**: 5
- **reps_required**: 2
- **feedback_rule**: 用 `numpy_financial.npv(rate, cashflows)` 与 `.irr(cashflows)`。若 NPV<0 → 提示 "Agent-as-Worker 现金流含推理成本 (500 tokens/协商 × token定价) 与 A2A 协议费 (10%), 是否漏算?"; 若 IRR > 200% → 提示 "Agent 寿命设太长或人类工人成本基线过高, 检查人类工人年薪 \$50k 与 Agent 部署成本 \$2k 的比值"; 若 4 子图缺一 → 不通过. 领域特定: 必须做推理成本敏感性分析 (GPT-4o vs DeepSeek V3 vs 临界点), 不能只算单点 NPV。
- **worked_faded**:
  - **Worked**: 教师完整展示 Agent 5 年现金流建模 (初始部署/年推理成本/年产出价值/残值), 与 NPV/IRR 计算。
  - **Faded**: starter TODO6 保留现金流数组骨架, 删除推理成本敏感性循环与 matplotlib 4 子图代码, 学生填空。
  - **Independent**: 学生独立设计 "Agent 寿命敏感性" 场景 (Agent 寿命 1/3/5/10 年), 重画 NPV-寿命曲线。

### drill_id: D-S1-BAYES (额外强化, 覆盖 D1 盲点)
- **difficulty**: 3
- **reps_required**: 2
- **feedback_rule**: 手算与代码双轨。手算 D1 的 μ'/σ'² 后, 用 `scipy.stats.norm` 验证。若手算 μ' ≠ 代码结果 → 提示 "conjugate normal update 公式: μ' = (μ/σ²_prior + x/σ²_obs) / (1/σ²_prior + 1/σ²_obs), 检查权重". 领域特定: 解释 "为什么 Agent 用贝叶斯而非理性预期" -- Agent 在不确定市场中逐步学习均衡, 与天道推演的'概率评估'能力同构。
- **worked_faded**: Worked (教师完整推导公式) -> Faded (starter 给公式骨架, 学生代入数值) -> Independent (学生改 LogNormal 先验, 重推导)。

---

## interleaving (A1B1C1...B2C2A2...C3A3B3 交叉排布, 不块状)

> 研究显示 interleaving 优于 block practice, 促进迁移。本单元 3 子技能 (S1=mesa ABM, S2=networkx, S3=numpy-financial) 按以下顺序交叉, 而非 S1×3 → S2×3 → S3×3:

```
Day1-A: S1-drill1 (mesa BuyerAgent 贝叶斯更新)
Day1-B: S2-drill1 (networkx DiGraph 构建)
Day1-C: S3-drill1 (numpy-financial NPV 基础)
Day2-A: S2-drill2 (networkx 三指标计算)
Day2-B: S3-drill2 (IRR + 推理成本敏感性)
Day2-C: S1-drill2 (mesa SellerAgent 动态定价)
Day3-A: S3-drill3 (4 子图可视化)
Day3-B: S1-drill3 (mesa DataCollector 9 reporters)
Day3-C: S2-drill3 (PageRank 经济影响力解读)
```

每 drill 间隔 1 天, 利用间隔重复 (与 schedule.json FSRS-6 同步)。

---

## retry_policy (CS230 式, 失败重试不罚分)

- **10 free late days**: 整个学期 10 天宽限, 自动扣用, 不需申请。
- **失败重试不罚分**: 任一 drill 首次未通过 (gini 异常 / NPV<0 / 子图缺失等), 可无限次重试, 重试通过记满分。
- **Weak loop 触发**: 见下节, 不算 "失败", 是教学干预而非惩罚。

---

## weak_loop (连续 2 次失败触发弱项循环)

> 连续 2 次同一 drill 失败 → 自动触发:
> 1. 回退到上一难度 drill (e.g., D-S1-ABM 失败 2 次 → 回退做 D-S1-BAYES 的 Worked 阶段重读)
> 2. 补充 worked example (重看 solution.ipynb 对应 TODO 的完整解)
> 3. 与 LLM tutorial (tutorial.ipynb) 做 1 次苏格拉底对话, 定位概念盲点
> 4. 通过后, 重新进入原 drill 的 Faded 阶段

典型弱项模式 (本单元预期):
- 贝叶斯更新公式记错 → 触发 D-S1-BAYES Worked 重读
- networkx 有向 vs 无向混淆 → 触发 D-S2-NET Worked 重读
- 推理成本漏算 → 触发 D-S3-NPV Worked 重读

---

## progressive_project (CS230 式, proposal -> milestone -> final -> poster)

| 阶段 | 交付物 | 字数/代码量 | 评估 |
|------|--------|------------|------|
| **Proposal (Day 1)** | 选定一个营销场景 (e.g., 品牌Agent买广告位 / 媒介Agent卖流量), 说明 Agent 数量/参数/假设 | 300字 | 教师反馈 feasibility |
| **Milestone (Day 3)** | mesa 仿真跑通 20 步, DataCollector 输出 9 个指标, networkx 三拓扑指标可计算 | starter.ipynb TODO1-4 完成 | 同伴互评 + 自动化检测 gini/survival_rate 非 NaN |
| **Final (Day 5)** | starter.ipynb 6 TODO 全完成, 4 子图 (价格分布/基尼时间序列/网络拓扑/NPV-IRR) 有数据 | 完整 notebook | 教师评分 (mastery >=80%) |
| **Poster (Day 7)** | 1 页 PDF: 涌现现象解读 + 推理成本敏感性结论 + 天道推演×多Agent仿真同构反思 | 1页 | 全班 poster session, 3 位同伴评分 |

---

## 评分标准 (mastery_threshold)

- 单 drill 通过: feedback_rule 中所有检查项通过 (gini 合理 / 三指标非 NaN / NPV 符号正确)
- 单元 mastery: 全部 3 个核心 drill (D-S1-ABM/D-S2-NET/D-S3-NPV) 通过 + progressive_project Final >=80%
- **mastery 阈值 >=80%** (与 alignment.md 一致)

---

*本文件基于 Ericsson 刻意练习理论 + MIT CS229 pset0 先测 + Harvard/Stanford Worked-Faded 示范渐退 + CS230 progressive project + interleaving 研究设计。所有 feedback_rule 引用本单元真实库 (mesa/networkx/numpy-financial) 与真实经济参数。*
