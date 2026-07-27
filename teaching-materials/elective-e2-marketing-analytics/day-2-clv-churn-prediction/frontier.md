# frontier.md (v9.0 学术前沿注入层)

> **所属**：elective-e2-marketing-analytics · day-2-clv-churn-prediction
> **版本**：v9.0（学术前沿注入层）
> **本单元前沿课题**：CLV 预测的 BG/NBD 静态行为假设如何被 2025-2026 因果结构学习 + 时序深度模型挑战，以及"CLV × 流失四象限行动矩阵"如何被利润反事实与归因市场理论重新形式化。

---

## frontier_topic

本单元教 BG/NBD 简化公式（Poisson 购买 + Beta 流失）、RFM 五分群、LogReg/RF 流失预测与 CLV × 流失四象限行动矩阵。前沿子问题是：2025-2026 年将 DAG 因果结构学习 + GRU 时序模式引入 CLV 建模（DeepCausalMMM）、将客户价值归因形式化为 Fisher 市场配分（Attribution Markets）、将 CLV 决策直接锚定到利润反事实（PBCE），如何系统性挑战 BG/NBD 的"购买率恒定 + 流失不可逆"假设与四象限矩阵的"高 CLV 高风险即应挽留"直觉。

---

## recent_papers

> 从 `_frontier_corpus/elective-e2-marketing-analytics.md` 共享语料库中挑选 4 篇最贴本单元的 2025-2026 论文。

### 1. DeepCausalMMM: A Deep Learning Framework for Marketing Mix Modeling with Causal Structure Learning
- **arXiv**: https://arxiv.org/abs/2510.13087
- **作者**: Aditya Puttaparthi Tirumala
- **年份**: 2025
- **摘要**: 结合 GRU 时序模式、DAG 因果结构学习和 Hill 方程饱和曲线，构建 DeepCausalMMM 营销组合建模框架。支持多区域建模（共享与区域特定参数），使用 Huber 损失和预算优化。
- **与本单元的关联**: 本单元 TODO3 的 BG/NBD 简化公式假设"购买率恒定、流失不可逆"；DeepCausalMMM 的 GRU 时序模式 + DAG 结构学习直接挑战这两个静态假设，提供动态因果版的 CLV 建模方向。

### 2. Attribution Markets: A Fisher-Market Formulation for Fractional Credit Assignment Between Planned Tasks and Performed Actions
- **arXiv**: https://arxiv.org/abs/2607.20694
- **作者**: Salavat Ishbulatov
- **年份**: 2026
- **摘要**: 将计划任务与执行动作之间的桥接形式化为拟线性 Fisher 市场，计划任务为买方，动作为可分割商品。引入熵正则化推广，与多触点归因（multi-touch attribution）、最优传输和在线 Fisher 市场算法相关联。
- **与本单元的关联**: 本单元 TODO2 用 RFM 五分群将客户分为 Champions/Recent/At Risk/Hibernating/Lost；Attribution Markets 把"谁应获功劳"重新形式化为 Fisher 市场配分，为本单元 RFM 静态分群提供动态博弈论替代。

### 3. Profit-Based Counterfactual Explanations for Product Improvement: A Case Study of Manga Sales in Japan
- **arXiv**: https://arxiv.org/abs/2607.01610
- **作者**: Keita Kinjo, Takeshi Ebina
- **年份**: 2026
- **摘要**: 将反事实解释形式化为管理和营销情境中的利润最大化问题，提出基于利润的反事实解释（PBCE）。通过直接最大化利润作为优化目标，消除外生目标设定，以日本漫画销售为案例验证。
- **与本单元的关联**: 本单元 TODO6 的 CLV × 流失四象限矩阵按"高 CLV × 高风险即优先挽留"做静态决策；PBCE 把"挽留决策"操作化为利润最大化反事实（调整哪个特征可最大化利润），是 TODO6 行动矩阵的直接前沿扩展。

### 4. Media Measurement and the Assisted Own Goal: Attribution, Marketing-Mix Models, and Individual-Level Incrementality
- **arXiv**: https://arxiv.org/abs/2607.09608
- **作者**: Tobias Konitzer
- **年份**: 2026
- **摘要**: 提出"助攻乌龙球"假说：上漏斗广告平台促成增量购买，但转化被归功于下游市场。构建基于增量测量的模型，使用"环境受众级随机化"和个体级 PIE 扩展实现无偏估计。
- **与本单元的关联**: 本单元 TODO1 计算 hist_clv = re74 + re75 + re78 假设所有历史消费都是"客户带来的价值"；Konitzer 的"助攻乌龙球"假说质疑部分 CLV 实际由上游营销助攻而非客户内生价值驱动，迫使 CLV 计算区分"内生 CLV"与"助攻 CLV"。

---

## critical_synthesis

这 4 篇论文 + 语料库其他论文共同揭示 2025-2026 CLV 与流失预测领域的三个共识与一个尖锐争议。**共识一**：BG/NBD 的静态行为假设已过时。Tirumala（#6）的 DeepCausalMMM 用 GRU 捕获时序非平稳性 + DAG 学习因果结构 + Hill 方程饱和曲线，是对 BG/NBD "购买率恒定 + 流失不可逆"假设的方法论升级。本单元 notes.md 已承认 BG/NBD 假设在 B2B 场景常被违背（合同周期、季节性），DeepCausalMMM 提供了具体的工程化替代路径。**共识二**：客户价值归因应从静态分群走向动态博弈配分。Ishbulatov（#7）的 Fisher 市场形式化将"谁应获功劳"从规则分桶（RFM 五分群）转为市场均衡问题，与多触点归因、最优传输形成理论统一。**共识三**：CLV 决策应直接优化利润而非 CLV 本身。Kinjo & Ebina（#8）的 PBCE 与本单元 TODO6 的四象限矩阵形成对照--四象限是描述性分桶，PBCE 是规范性利润优化，前者是后者的简化教学版本。

**尖锐争议**：CLV 中有多少比例是"内生价值"vs"营销助攻价值"？Konitzer（#1）的"助攻乌龙球"假说暗示 CLV 计算可能系统性高估客户内生价值，将营销助攻错记为客户忠诚。但 #6、#7、#8 均未显式分离这两种价值，这是 CLV 文献的结构性盲点。**方法学趋势**：从频率学派 BG/NBD（2005）→ 贝叶斯 CLV（PyMC，2026）→ DeepCausalMMM（2025，DAG + GRU + Hill），CLV 建模正从"概率模型 + 静态假设"走向"深度时序 + 因果结构 + 饱和曲线"的整合范式。**局限**：4 篇中仅 #1 Konitzer 经 verified，#6/#7/#8 均为 unverified；#6 的 DeepCausalMMM 未开源代码，DAG 学习的稳定性与 GRU 时序窗口选择未做 sensitivity analysis；#7 的 Fisher 市场形式化仅在理论层面，缺乏真实营销部署验证；#8 的日本漫画单一品类可推广性存疑。

---

## delta_to_unit

1. **TODO3 BG/NBD 简化公式应被 DeepCausalMMM 的 DAG + GRU + Hill 框架挑战**：本单元 solution.ipynb 的 BG/NBD 简化式 `bg_nbd_clv = F * (retention_rate^12) * avg_order_value * 12 * discount_factor` 假设购买率恒定、流失不可逆。Tirumala（#6）的 DeepCausalMMM 用 GRU 捕获购买率的时序非平稳 + DAG 学习渠道间因果结构 + Hill 方程饱和曲线，是对本单元 BG/NBD 假设的直接挑战。前沿 delta：TODO3 应补充"BG/NBD 假设违背诊断"步骤，并对比 DeepCausalMMM 风格的动态 CLV 估计。

2. **TODO2 RFM 五分群应被 Fisher 市场配分挑战**：本单元 solution.ipynb 用 `pd.qcut` 对 M 分四分位 + R/F 组合分五群（Champions/Recent/At Risk/Hibernating/Lost），是规则驱动的静态分桶。Ishbulatov（#7）的 Fisher 市场形式化将"客户价值归因"重新表述为买方-商品均衡问题，可动态响应营销动作变化。前沿 delta：TODO2 应在 RFM 五分群后追加"如果用 Fisher 市场配分，Champions 群的功劳分配会如何变化"的对比分析。

3. **TODO6 四象限行动矩阵应被 PBCE 利润反事实挑战**：本单元 solution.ipynb 的四象限矩阵按 `高 CLV × 高流失风险 = 优先挽留` 做静态决策。Kinjo & Ebina（#8）的 PBCE 把"挽留决策"操作化为"调整哪个客户特征可最大化利润"的反事实优化。前沿 delta：TODO6 的 Q1（高 CLV 高风险）决策应从"是否挽留"升级为"调整哪个特征挽留利润最大"的 PBCE 优化。

4. **TODO1 历史 CLV 计算应区分"内生 CLV"与"助攻 CLV"**：本单元 solution.ipynb 计算 `hist_clv = re74 + re75 + re78`，把所有历史消费都记为客户价值。Konitzer（#1）的"助攻乌龙球"假说暗示部分 CLV 实际由上游营销助攻驱动。前沿 delta：TODO1 应补充"助攻 CLV 占比"诊断步骤，将 hist_clv 分解为内生 + 助攻两部分。

---

## open_questions

1. DeepCausalMMM 的 DAG 因果结构学习在 NSW 445 样本上是否可稳定收敛--当样本量远小于 Day 3 MMM 的周度聚合数据时，DAG 学习的方差-偏差权衡如何，是否可发表为"小样本因果 CLV 的结构学习可行性"方法论文？
2. Attribution Markets 的 Fisher 市场均衡与本单元 RFM 五分群在 NSW 数据上的客户分级一致性有多大--若两类方法对 Champions 群的客户重叠率 < 60%，是否意味着 RFM 静态分群存在系统性误判，可发表为"RFM vs Fisher 市场配分的客户分级偏差"实证研究？
3. PBCE 利润反事实在 CLV × 流失四象限的 Q1（高 CLV 高风险）象限中，反事实特征调整的边际利润弹性有多大--若弹性高度依赖流失成本假设，是否可发表为"CLV 决策的利润反事实灵敏度分析"方法论？
4. Konitzer 的"助攻 CLV"概念在 NSW re74/re75/re78 三年收入数据上能否被识别--如果 NSW 的 treat 随机化使 re78 的"助攻部分"可被 treat 系数捕获，是否可发表为"用 RCT 数据识别 CLV 内生 vs 助攻成分"的因果识别研究？

---

## methodological_critique

这 4 篇论文存在三方面不能全信。**第一，验证级别严重不对称**：仅 #1 Konitzer 经 arXiv abstract 页 verified，#6 DeepCausalMMM、#7 Attribution Markets、#8 PBCE 均为 unverified，标题/作者/摘要可能存在 LLM 抽取误差，复现前必须人工核对 arXiv 页面。**第二，DAG 学习的 benchmark-gaming 风险**：Tirumala（#6）的 DeepCausalMMM 未报告 DAG 学习在不同 sparsity 假设下的 robustness，可能存在"在特定 DAG 稀疏度下结果最优"的隐式超参搜索；GRU 时序窗口选择也未做 sensitivity analysis，存在"窗口长度 gaming"风险。**第三，理论-部署鸿沟**：Ishbulatov（#7）的 Fisher 市场形式化仅在理论层面，未提供真实营销部署数据；Kinjo & Ebina（#8）的 PBCE 仅在日本漫画单一品类验证，PBCE 框架对品类利润结构（高毛利 vs 低毛利、长尾 vs 头部）的 sensitivity 未做压力测试。博后读者引用这些论文时，应将 #1 作为"已被验证存在"的引用源，对 #6/#7/#8 的具体方法保持批判性距离，并在论文方法部分标注"未经独立工业部署验证"。

---

*本文件由 v9.0 学术前沿注入层生成。所有论文链接来自 `_frontier_corpus/elective-e2-marketing-analytics.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证）。*
