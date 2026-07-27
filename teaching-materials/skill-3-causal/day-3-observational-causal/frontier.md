# frontier.md (v9.0 学术前沿注入层)

> **所属**：技能3 因果推断与规模实验 · Day 3 观测数据的因果推断
> **版本**：v9.0（学术前沿注入层）
> **本单元前沿课题**：本单元教 PSM 倾向得分匹配 + IV 工具变量（2SLS/LATE）+ DML 双重机器学习 + 四大准实验方法选择。前沿子问题是"2025-2026 年 LLM 元裁判如何辅助 PSM/IV 方法选择、目标感知图如何强化可忽略性假设验证、LLM 从文本学因果结构如何挑战 PSM 协变量集的人工指定"。

---

## frontier_topic

本单元以 NSW+CPS 观测对照数据教 PSM 消除自选择偏差、以 close_college 数据教 IV（2SLS）估计 LATE、以 DML 放松函数形式假设，核心痛点是"可忽略性假设（无未观测混杂）无法从数据验证"。2025-2026 前沿子问题是：当 LLM 被定位为方法选择的元裁判、当目标感知图构建以目标变量约束抑制无关混杂、当 LLM 从文本归纳因果结构可自动发现协变量集时，本单元的四大方法人工决策框架、PSM 协变量人工指定与可忽略性假设的不可验证性是否仍成立。

---

## recent_papers

### 1. CausalMix: Data Mixture as Causal Inference for Language Model Training
- **arXiv**: https://arxiv.org/abs/2607.01104
- **作者**: Zinan Tang, Yukun Zhang
- **年份**: 2026
- **摘要**: 将 LLM 训练的数据混合优化建模为因果推断问题，将数据池的统计特征作为协变量、领域混合作为处理。在 512 次 Qwen2.5-0.5B 运行上拟合因果模型估计 CATE 后，外推至 800K 数据池并应用于 7B 模型，持续超越 RegMix 等基线。
- **与本单元的关联**: 本单元 notes.md 教 DML（Chernozhukov 2018）用 ML 估计 nuisance 参数 + 正交化；CausalMix 是 DML 的 CATE 应用实例--将"协变量→处理→结果"的 DML 框架应用于数据混合优化，为本单元 DML 提供了工业级应用参照。

### 2. Causal Ensemble Agent: Hierarchical Causal Discovery with LLM-guided Expert Reweighting
- **arXiv**: https://arxiv.org/abs/2606.10607
- **作者**: Xinyu Li, Yuanyuan Wang
- **年份**: 2026
- **摘要**: 提出 Causal Ensemble Agent（CEA），通过线性意见池聚合统计发现专家的结构洞察，使用 LLM 作为元裁判在聚合置信度接近决策边界时动态重新加权专家。LLM 用于元分析而非直接因果推断，在合成与真实数据集上达最强整体性能。
- **与本单元的关联**: 本单元 notes.md "关键回顾 1"教 PSM/DiD/IV/RDD 四大方法的人工选择决策框架；CEA 将方法选择升级为 LLM 元裁判在"置信度接近决策边界"时动态重加权专家集合，是本单元方法选择框架的自动化前沿。

### 3. Causal-Audit: Explicit and Auditable Graph-based Reasoning via Target-Aware Causal Chain Construction
- **arXiv**: https://arxiv.org/abs/2607.15281
- **作者**: Su Lan, Xuefei Yin
- **年份**: 2026
- **摘要**: 提出显式可审计的因果推理框架，将因果推断建模为在显式因果图上的结构化推理。目标感知图构建策略在扩展时将目标变量作为核心约束以抑制无关变量，路径级因果证据聚合机制建模跨多路径的增强和抵消效应。
- **与本单元的关联**: 本单元 notes.md "关键回顾 2"教 PSM 依赖可忽略性假设（无未观测混杂），但协变量集 X 人工指定；Causal-Audit 的目标感知图以目标变量（如 re78）为核心约束自动剪枝无关变量，将可忽略性假设的验证从"人工指定 X"升级为"目标驱动的图结构化剪枝"。

### 4. Words as Difference Makers: How Large Language Models Determine Causal Structure in Text
- **arXiv**: https://arxiv.org/abs/2606.22430
- **作者**: Wolfgang Pietsch
- **年份**: 2026
- **摘要**: 论证 LLM 采用基于"差分逻辑"（difference-making logic / variational induction）的归纳方法从文本学习因果结构。LLM 需要来自多样上下文的海量文本数据来识别词序列中的差分与非差分制造者，分析 token 嵌入与自注意力如何实现该逻辑。
- **与本单元的关联**: 本单元 PSM 第一步是估计倾向得分 e(X)=P(T=1|X)，需人工指定协变量集 X；该论文主张 LLM 从文本归纳学习因果结构，暗示 LLM 可自动发现 PSM 所需的协变量集 X，挑战本单元的人工指定范式。

### 5. Causal Discovery in the Era of Agents
- **arXiv**: https://arxiv.org/abs/2606.23608
- **作者**: Yujia Zheng, Vishal Verma
- **年份**: 2026
- **摘要**: 论证 agent 在因果发现中应辅助工作流（检查数据、检索上下文、解释假设），而因果声明须基于数据、显式假设和形式化算法。提出 causal-learn+ 在线平台，协调数据分析、预处理、方法推荐和形式化发现，在 Big Five 人格数据上展示 agent 辅助因果发现。
- **与本单元的关联**: 本单元 solution.ipynb TODO4 用 DoWhy + PSM 估计，DAG 与可忽略性假设人工声明；该论文要求 agent 辅助时因果声明须基于形式化算法约束，挑战本单元"人工声明可忽略性"的范式--可忽略性无法从数据验证，但 agent 可辅助检查其形式化前置条件。

---

## critical_synthesis

这五篇论文共同揭示 2025-2026 年观测因果推断前沿对"可忽略性假设不可验证性"这一核心痛点的多层次回应。共识层面：Causal Ensemble Agent（2606.10607）与 Causal Discovery in the Era of Agents（2606.23608）共同收敛于"LLM 辅助工作流、形式化算法主导因果声明"的方法论共识--前者将 LLM 限制为方法选择的元裁判（在置信度边界重加权专家），后者要求 agent 辅助数据检查与方法推荐但因果声明须形式化算法约束，二者共同将 LLM 定位为观测因果推断的"流程辅助者"而非"假设替代者"。争议层面：Words as Difference Makers（2606.22430）主张 LLM 通过差分逻辑从文本归纳因果结构，暗示 LLM 可自动发现 PSM 所需的协变量集 X，这与 Causal Discovery in the Era of Agents 的"因果声明须基于数据与形式化算法"立场形成张力--前者赋予 LLM 结构发现能力，后者限制 LLM 于流程辅助。方法学趋势上，CausalMix（2607.01104）将 DML 的 CATE 估计应用于数据混合优化（小模型拟合外推大模型），Causal-Audit（2607.15281）以目标感知图构建将可忽略性验证从"人工指定 X"升级为"目标驱动剪枝"--二者代表从"人工声明假设"向"数据驱动+目标驱动自动化"的演进。局限在于：本单元引用的 5 篇中仅 Causal Ensemble Agent 经 abstract 页验证，其余 4 篇 unverified；CausalMix 的 CATE 规模不变性假设（0.5B→7B 外推）未经验证；Words as Difference Makers 为纯理论论证无实验支撑；Causal-Audit 与 Causal Discovery in the Era of Agents 在自建平台展示，未在标准观测因果基准（如 NSW/Lalonde）对比。博后读者应将这些声明视为"待独立复现的前沿假设"。

---

## delta_to_unit

1. **PSM/IV 方法选择的自动化**：本单元 notes.md "关键回顾 1"教 PSM/DiD/IV/RDD 四大方法的人工选择决策框架（核心假设+适用场景+营销映射），依赖分析师判断。Causal Ensemble Agent（2606.10607）将方法选择升级为 LLM 元裁判在"聚合置信度接近决策边界时动态重加权专家"--这把本单元的"人工选方法"升级为"LLM 在决策边界重加权方法集合"，是本单元方法选择框架未覆盖的自动化前沿，需在教学中补充 LLM 介入方法选择的触发条件。

2. **PSM 协变量集 X 的人工指定挑战**：本单元 solution.ipynb TODO4 用 `common_causes = ["age", "educ", "black", "hisp", "marr", "nodegree", "re74", "re75"]` 人工指定 PSM 协变量集。Words as Difference Makers（2606.22430）主张 LLM 通过差分逻辑从文本归纳因果结构，暗示 LLM 可从领域文献自动发现协变量集 X；Causal-Audit（2607.15281）的目标感知图以目标变量（re78）为核心约束自动剪枝无关变量--二者共同挑战本单元"人工指定 X"的范式，要求教学标注"人工指定 X 可能遗漏未观测混杂"。

3. **DML 的 CATE 工业级应用参照**：本单元 notes.md "2026 前沿补充"教 DML（Chernozhukov 2018）用 ML 估计 nuisance 参数 + 正交化 + 交叉拟合，但仅停留在方法介绍。CausalMix（2607.01104）是 DML 的工业级 CATE 应用实例--在 512 次 0.5B 模型运行上拟合 CATE 后外推至 7B，将本单元的"DML 方法介绍"升级为"DML 的 CATE 估计+外推实践"，为本单元可选作业"用 econml DML 在 NSW+CPS 上再估一次"提供了外推范式参照。

4. **可忽略性假设的形式化辅助验证**：本单元 notes.md "关键回顾 2"明确指出 PSM"只能消除可观测混杂，若有未观测混杂仍需 IV"，但可忽略性假设无法从数据验证。Causal Discovery in the Era of Agents（2606.23608）要求 agent 辅助数据检查、预处理、方法推荐，但因果声明须基于形式化算法约束--这为本单元的可忽略性假设提供了"agent 辅助检查形式化前置条件"的验证路径，虽不能完全验证可忽略性，但可系统性检查其必要条件。

5. **反驳检验的目标驱动升级**：本单元 solution.ipynb TODO5 用 DoWhy 的 `placebo_treatment_refuter` 做统计反驳检验。Causal-Audit（2607.15281）的路径级因果证据聚合机制建模跨多路径的增强和抵消效应，将本单元的"安慰剂处理统计反驳"升级为"目标驱动的多路径证据聚合"--这要求本单元在反驳检验教学中引入"单路径安慰剂 ≠ 多路径联合稳健性"的层级差异。

---

## open_questions

1. Causal Ensemble Agent 的 LLM 元裁判在 PSM vs IV 方法选择边界（即可忽略性是否成立）重加权时，其重加权决策是否可形式化证明满足 IV 的排他性约束，还是仅经验性有效？
2. Words as Difference Makers 主张 LLM 从文本学因果结构，那么 LLM 能否从营销领域文献自动发现 PSM 所需的协变量集 X，其发现的 X 在 NSW+CPS 上是否比人工指定的 8 协变量集更满足可忽略性？
3. CausalMix 在 0.5B 模型上拟合 CATE 后外推至 7B 假设规模不变性--这一假设在 NSW+CPS 观测数据的 DML 估计中是否成立，即小样本 CATE 能否外推至大样本？
4. Causal-Audit 的目标感知图以 re78 为核心约束剪枝无关变量时，在 NSW+CPS 的 8 协变量场景下，相比本单元 PSM 的全协变量匹配，ATE 估计偏差是否系统性更小？
5. Causal Discovery in the Era of Agents 的 causal-learn+ 平台能否辅助验证 PSM 的可忽略性假设的形式化前置条件（如 DAG 的 d-分离），还是仅能检查数据质量与预处理？

---

## methodological_critique

上述论文的局限性需在教学中显式标注。CausalMix（2607.01104）在 0.5B 模型上拟合 CATE 后外推至 7B，外推有效性假设 CATE 的规模不变性，但 LLM 的涌现能力可能使小规模 CATE 估计失真；512 次运行的实验规模可能不足以覆盖高维 CATE 空间，且未开源代码。Causal Ensemble Agent（2606.10607）虽经 abstract 页验证，但未开源 LLM 元裁判 prompt 与决策边界阈值选取标准，"在合成与真实数据集达 SOTA"的声明无法独立复现，且 LLM 重加权的线性意见池假设专家独立性，若 PSM/IV/DiD/RDD 共享可忽略性假设基础则假设不成立。Words as Difference Makers（2606.22430）为纯理论论证，无任何实验支撑其"差分逻辑"主张，token 嵌入与自注意力的因果结构映射仅为推测。Causal-Audit（2607.15281）未经验证，且未在 NSW/Lalonde 等标准观测因果基准对比，目标感知图构建的计算复杂度在 8+ 协变量场景下未报告。Causal Discovery in the Era of Agents（2606.23608）未经验证，在自建平台 causal-learn+ 与 Big Five 人格数据上展示，作者既构建平台又评估平台，利益冲突明显，存在 benchmark-gaming 与选择性报告风险。博后读者应区分 verified 与 unverified 标注，将这些声明视为"待独立复现的前沿假设"。

---

*本文件由 v9.0 学术前沿注入层生成。所有论文链接来自 `_frontier_corpus/skill-3-causal.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证）。*
