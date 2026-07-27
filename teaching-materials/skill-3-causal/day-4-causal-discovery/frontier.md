# frontier.md (v9.0 学术前沿注入层)

> **所属**：技能3 因果推断与规模实验 · Day 4 因果发现与 ML 因果推断
> **版本**：v9.0（学术前沿注入层）
> **本单元前沿课题**：本单元教 PC/FCI 因果发现算法 + NOTEARS 连续优化 + DML 去偏 + 因果森林 CATE + LLM 辅助因果发现。前沿子问题是"2025-2026 年 LLM 元裁判如何聚合 PC 统计发现专家、LLM 差分逻辑如何与数据驱动因果发现融合、Lean 形式化如何验证算法发现的因果图"。

---

## frontier_topic

本单元以 sklearn 糖尿病数据教 PC 算法自动发现因果图、以 NSW 数据教因果森林（CausalForestDML）估计异质处理效应，核心跃迁是从"人工画 DAG"到"算法学 DAG"。2025-2026 前沿子问题是：当 LLM 被定位为因果发现的元裁判聚合统计发现专家、当 LLM 的差分逻辑被论证可从文本学习因果结构、当 Lean 形式化可验证算法发现的因果图、当因果归因剪枝可识别 LLM 关键注意力头时，本单元的 PC 纯数据驱动发现与 LLM 自由辅助发现范式是否仍成立。

---

## recent_papers

### 1. Causal Ensemble Agent: Hierarchical Causal Discovery with LLM-guided Expert Reweighting
- **arXiv**: https://arxiv.org/abs/2606.10607
- **作者**: Xinyu Li, Yuanyuan Wang
- **年份**: 2026
- **摘要**: 提出 Causal Ensemble Agent（CEA），通过线性意见池聚合统计发现专家的结构洞察，使用 LLM 作为元裁判在聚合置信度接近决策边界时动态重新加权专家。LLM 用于元分析而非直接因果推断，在合成与真实数据集上达最强整体性能。
- **与本单元的关联**: 本单元 solution.ipynb TODO2 运行单一 PC 算法发现因果图；CEA 将多个统计发现专家（如 PC/FCI/NOTEARS）的输出聚合，用 LLM 在置信度边界重加权--将本单元的"单一 PC 发现"升级为"多专家聚合 + LLM 元裁判"。

### 2. Causal Discovery in the Era of Agents
- **arXiv**: https://arxiv.org/abs/2606.23608
- **作者**: Yujia Zheng, Vishal Verma
- **年份**: 2026
- **摘要**: 论证 agent 在因果发现中应辅助工作流（检查数据、检索上下文、解释假设），而因果声明须基于数据、显式假设和形式化算法。提出 causal-learn+ 在线平台，协调数据分析、预处理、方法推荐和形式化发现，在 Big Five 人格数据上展示 agent 辅助因果发现。
- **与本单元的关联**: 本单元 solution.ipynb TODO1-3 手动执行 PC 的加载-运行-解读流程；causal-learn+ 平台将这一流程协调为 agent 辅助的自动化工作流，且要求因果声明须形式化算法约束，挑战本单元"PC 发现即可信"的隐含假设。

### 3. Words as Difference Makers: How Large Language Models Determine Causal Structure in Text
- **arXiv**: https://arxiv.org/abs/2606.22430
- **作者**: Wolfgang Pietsch
- **年份**: 2026
- **摘要**: 论证 LLM 采用基于"差分逻辑"（difference-making logic / variational induction）的归纳方法从文本学习因果结构。LLM 需要来自多样上下文的海量文本数据来识别词序列中的差分与非差分制造者，分析 token 嵌入与自注意力如何实现该逻辑。
- **与本单元的关联**: 本单元 notes.md "2026 前沿补充"教 LLM 辅助因果发现（Kiciman 2023），定位为"LLM 提供候选因果图 + 数据驱动验证"；该论文论证 LLM 通过差分逻辑从文本归纳学习因果结构，为本单元的"LLM 提供候选"提供了机制解释--LLM 不是凭空生成，而是基于差分逻辑的归纳。

### 4. CausalForge: A Formally Grounded, Self-Improving Agentic Framework for Automated Research in Causal Inference
- **arXiv**: https://arxiv.org/abs/2607.22511
- **作者**: Jiyuan Tan, Vasilis Syrgkanis
- **年份**: 2026
- **摘要**: 提出 CausalForge，基于 Lean 证明助手的因果推断自动化研究框架。结合 Causalean（7,035 条机器检查声明的 Lean 库）与 CausalSmith（自改进 agentic pipeline），用于选择研究主题、提出结果并构造证明，并通过声明审计比较形式化定理与非形式化声明。
- **与本单元的关联**: 本单元 PC 算法发现的因果图无形式化验证（PC 假设因果充分性，若有隐混杂则失真）；CausalForge 的 Causalean 库以 Lean 机器检查声明，可为 PC 发现的因果图提供形式化验证，补全本单元缺失的"发现后验证"环节。

### 5. Pruning via Causal Attribution Preserves Reasoning Performance in Large Language Models
- **arXiv**: https://arxiv.org/abs/2606.19350
- **作者**: Amogh Sheth, Biruk Assefa
- **年份**: 2026
- **摘要**: 提出 Causal Attribution Pruning（CAP），无训练方法通过测量注意力头对推理任务的因果影响来识别关键头，再将头级重要性分数转化为权重级重要性进行剪枝。在 ARC-Challenge 20% 稀疏度下相对 Wanda 准确率提升最高 61%。
- **与本单元的关联**: 本单元 solution.ipynb TODO6 用因果森林的 `feature_importances_` 识别驱动 CATE 异质性的特征；CAP 用因果归因识别驱动 LLM 推理的注意力头--二者同为"因果归因识别关键变量"，CAP 将本单元的"特征重要性"扩展至"注意力头因果重要性"。

---

## critical_synthesis

这五篇论文共同揭示 2025-2026 年因果发现前沿对"纯数据驱动发现"与"LLM 辅助发现"两条路线的整合。共识层面：Causal Ensemble Agent（2606.10607）与 Causal Discovery in the Era of Agents（2606.23608）共同收敛于"LLM 辅助工作流、形式化算法主导因果声明"的方法论共识--前者将 LLM 限制为多专家聚合的元裁判（在置信度边界重加权），后者要求 agent 辅助数据检查与方法推荐但因果声明须形式化算法约束，二者共同拒绝"LLM 直接输出因果图"的朴素范式。争议层面：Words as Difference Makers（2606.22430）主张 LLM 通过差分逻辑从文本归纳学习因果结构，赋予 LLM 独立的结构发现能力，这与 Causal Discovery in the Era of Agents 的"因果声明须基于数据与形式化算法"立场形成张力--前者暗示 LLM 内部已实现因果发现，后者坚持 LLM 仅辅助流程。方法学趋势上，CausalForge（2607.22511）以 Lean 机器检查定理将因果发现的形式化验证推进，Causal Attribution Pruning（2606.19350）以因果归因量化注意力头对推理的因果影响--二者代表因果发现向"形式化验证"与"模型内部因果结构"两个方向的延伸。局限在于：仅 CausalForge 与 Causal Ensemble Agent 经 abstract 页验证，其余三篇 unverified；Causal Ensemble Agent 未开源 LLM 元裁判 prompt 与重加权阈值；Words as Difference Makers 为纯理论论证无实验支撑；Causal Discovery in the Era of Agents 在自建平台 causal-learn+ 上展示，未在 BNLearn/Tübingen 标准基准对比；Causal Attribution Pruning 的因果归因方法可能依赖特定注意力机制假设，泛化性未验证。博后读者应将这些声明视为"待独立复现的前沿假设"。

---

## delta_to_unit

1. **单一 PC 发现向多专家聚合升级**：本单元 solution.ipynb TODO2 运行单一 `pc()` 算法发现糖尿病数据的因果图，PC 的因果充分性假设（无隐混杂）若被违背则发现失真。Causal Ensemble Agent（2606.10607）将多个统计发现专家（如 PC/FCI/NOTEARS）的输出通过线性意见池聚合，用 LLM 在置信度接近决策边界时动态重加权--这把本单元的"单一 PC 发现"升级为"多专家聚合 + LLM 元裁判"，需在教学中补充"单一 PC 的因果充分性假设可被多专家聚合部分缓解"。

2. **LLM 辅助因果发现的机制解释**：本单元 notes.md "2026 前沿补充"教 LLM 辅助因果发现（Kiciman 2023, arXiv 2305.00050），定位为"LLM 提供候选因果图 + 数据驱动验证"，但未解释 LLM 如何生成候选。Words as Difference Makers（2606.22430）论证 LLM 通过差分逻辑从多样上下文的海量文本中识别差分与非差分制造者，为本单元的"LLM 提供候选"提供了机制解释--LLM 不是凭空生成，而是基于差分逻辑的归纳，需在教学中补充这一机制。

3. **PC 发现的形式化验证补全**：本单元 solution.ipynb TODO3 提取 PC 发现的因果结构（有向边/无向边），但无形式化验证 PC 发现的正确性。CausalForge（2607.22511）的 Causalean 库（7,035 条 Lean 机器检查声明）可为 PC 发现的因果图提供形式化验证，通过声明审计比较形式化定理与非形式化声明--这补全了本单元缺失的"发现后形式化验证"环节，要求教学标注"PC 发现 ≠ 形式化证明"。

4. **因果森林特征重要性的注意力头扩展**：本单元 solution.ipynb TODO6 用因果森林的 `feature_importances_` 识别驱动 CATE 异质性的特征（如 age/re75）。Causal Attribution Pruning（2606.19350）用因果归因测量注意力头对推理任务的因果影响，将头级重要性转化为权重级重要性--这将本单元的"特征级因果重要性"扩展至"注意力头级因果重要性"，为因果森林在 LLM 内部结构分析中的应用提供参照。

5. **PC 工作流的 agent 辅助协调**：本单元 solution.ipynb TODO1-3 手动执行 PC 的"加载->运行->解读"流程，依赖分析师逐步骤操作。Causal Discovery in the Era of Agents（2606.23608）的 causal-learn+ 平台将这一流程协调为 agent 辅助的自动化工作流（数据分析、预处理、方法推荐、形式化发现），且要求因果声明须形式化算法约束--这挑战本单元"PC 发现即可信"的隐含假设，要求教学标注"agent 辅助时因果声明须配套形式化算法（如 PC/FCI）约束"。

---

## open_questions

1. Causal Ensemble Agent 的 LLM 元裁判聚合 PC/FCI/NOTEARS 多专家输出时，在糖尿病 10 变量场景下，相比本单元单一 PC 发现，聚合后的因果图结构准确率是否系统性更高，且能否缓解 PC 的因果充分性假设违背？
2. Words as Difference Makers 论证 LLM 通过差分逻辑学因果结构，那么 LLM 能否从医学文献中归纳糖尿病 10 变量的因果结构，其发现的图与本单元 PC 算法从数据发现的图的一致率有多高？
3. CausalForge 的 Causalean 库能否形式化验证 PC 算法发现的因果图的 d-分离声明，还是仅适用于因果推断理论定理的机器检查？
4. Causal Attribution Pruning 的注意力头因果归因方法，能否迁移至因果森林的分裂标准设计--即用因果归因而非子节点效应差异作为分裂准则，以提升 CATE 估计精度？
5. Causal Discovery in the Era of Agents 的 causal-learn+ 平台在糖尿病数据上 agent 辅助推荐的因果发现方法，是否与本单元人工选 PC 的决策一致，若不一致 agent 推荐的方法（如 FCI/NOTEARS）是否更适合？

---

## methodological_critique

上述论文的局限性需在教学中显式标注。Causal Ensemble Agent（2606.10607）虽经 abstract 页验证，但未开源 LLM 元裁判 prompt 与决策边界阈值选取标准，"在合成与真实数据集达 SOTA"的声明无法独立复现，且 LLM 重加权的线性意见池假设专家独立性，若 PC/FCI/NOTEARS 共享条件独立性检验基础则假设不成立。Causal Discovery in the Era of Agents（2606.23608）未经验证，在自建平台 causal-learn+ 与 Big Five 人格数据上展示，作者既构建平台又评估平台，利益冲突明显，存在 benchmark-gaming 与选择性报告风险。Words as Difference Makers（2606.22430）为纯理论论证，无任何实验支撑其"差分逻辑"主张，token 嵌入与自注意力的因果结构映射仅为推测，且未与 PC/FCI 等数据驱动方法定量对比。CausalForge（2607.22511）虽经验证，但 Causalean 库 7,035 条声明围绕因果推断理论定理，未报告在糖尿病/NSW 等应用数据集上 PC 发现因果图的形式化覆盖率。Causal Attribution Pruning（2606.19350）未经验证，因果归因方法可能依赖特定 transformer 注意力机制假设，在 ARC-Challenge 单一基准上的 61% 提升能否迁移至其他推理任务未验证，且 20% 稀疏度下的准确率提升可能以牺牲其他稀疏度下的性能为代价。博后读者应区分 verified 与 unverified 标注。

---

*本文件由 v9.0 学术前沿注入层生成。所有论文链接来自 `_frontier_corpus/skill-3-causal.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证）。*
