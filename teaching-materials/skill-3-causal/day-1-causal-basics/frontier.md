# frontier.md (v9.0 学术前沿注入层)

> **所属**：技能3 因果推断与规模实验 · Day 1 因果推断基础
> **版本**：v9.0（学术前沿注入层）
> **本单元前沿课题**：本单元教 Pearl 因果阶梯 + 后门调整 + DoWhy 四步 + LLM-as-a-judge 审查因果论证。前沿子问题是"2025-2026 年 LLM 在因果发现/推断中的角色定位（元裁判 vs 直接推断器）与形式化可审计因果推理如何更新本单元的手画 DAG + LLM 审查范式"。

---

## frontier_topic

本单元以 NSW/Lalonde 真实数据教后门调整估计与 DoWhy 四步（建模→识别→估计→反驳），并以 LLM-as-a-judge 审查因果论证质量（定位为因果阶梯 L1）。2025-2026 前沿子问题是：当 LLM 被重新定位为因果发现的"元裁判"而非直接推断器、当反驳检验被升级为 Lean 机器检查定理、当手画 DAG 被目标感知可审计图取代时，本单元的 LLM 审查定位与统计反驳方法是否仍成立。

---

## recent_papers

> 从 `_frontier_corpus/skill-3-causal.md` 语料库中挑 5 篇最贴本单元的 2025-2026 论文。**严禁引用语料库之外的论文**。

### 1. CausalForge: A Formally Grounded, Self-Improving Agentic Framework for Automated Research in Causal Inference
- **arXiv**: https://arxiv.org/abs/2607.22511
- **作者**: Jiyuan Tan, Vasilis Syrgkanis
- **年份**: 2026
- **摘要**: 提出 CausalForge，基于 Lean 证明助手的因果推断自动化研究框架。结合 Causalean（7,035 条机器检查声明的 Lean 库）与 CausalSmith（自改进 agentic pipeline），用于选择研究主题、提出结果并构造证明，并通过声明审计比较形式化定理与非形式化声明。
- **与本单元的关联**: 本单元 solution.ipynb TODO5 用 DoWhy 的 placebo_treatment_refuter 做统计反驳；CausalForge 将反驳升级为 Lean 机器检查形式化证明，是本单元统计反驳方法的可复现性升级方向。

### 2. Causal Ensemble Agent: Hierarchical Causal Discovery with LLM-guided Expert Reweighting
- **arXiv**: https://arxiv.org/abs/2606.10607
- **作者**: Xinyu Li, Yuanyuan Wang
- **年份**: 2026
- **摘要**: 提出 Causal Ensemble Agent（CEA），通过线性意见池聚合统计发现专家的结构洞察，使用 LLM 作为元裁判在聚合置信度接近决策边界时动态重新加权专家。LLM 用于元分析而非直接因果推断，在合成与真实数据集上达最强整体性能。
- **与本单元的关联**: 本单元 notes.md 将 LLM-as-a-judge 定位为"审查 DAG 质量"；CEA 将 LLM 精确化为"专家聚合置信度接近边界时的元裁判"，是本单元 LLM 角色定位的前沿细化。

### 3. Causal Discovery in the Era of Agents
- **arXiv**: https://arxiv.org/abs/2606.23608
- **作者**: Yujia Zheng, Vishal Verma
- **年份**: 2026
- **摘要**: 论证 agent 在因果发现中应辅助工作流（检查数据、检索上下文、解释假设），而因果声明须基于数据、显式假设和形式化算法。提出 causal-learn+ 在线平台，协调数据分析、预处理、方法推荐和形式化发现，在 Big Five 人格数据上展示 agent 辅助因果发现。
- **与本单元的关联**: 本单元 DoWhy 四步中 DAG 与识别策略由人工声明；该论文要求 agent 辅助时因果声明必须形式化算法约束，挑战本单元"LLM 自由审查 DAG"的范式。

### 4. Causal-Audit: Explicit and Auditable Graph-based Reasoning via Target-Aware Causal Chain Construction
- **arXiv**: https://arxiv.org/abs/2607.15281
- **作者**: Su Lan, Xuefei Yin
- **年份**: 2026
- **摘要**: 提出显式可审计的因果推理框架，将因果推断建模为在显式因果图上的结构化推理。目标感知图构建策略在扩展时将目标变量作为核心约束以抑制无关变量，路径级因果证据聚合机制建模跨多路径的增强和抵消效应。
- **与本单元的关联**: 本单元教学生手画静态 DAG 识别后门路径；Causal-Audit 的目标感知图构建与路径级证据聚合将静态 DAG 扩展为动态目标约束的可审计因果图。

### 5. Words as Difference Makers: How Large Language Models Determine Causal Structure in Text
- **arXiv**: https://arxiv.org/abs/2606.22430
- **作者**: Wolfgang Pietsch
- **年份**: 2026
- **摘要**: 论证 LLM 采用基于"差分逻辑"（difference-making logic / variational induction）的归纳方法从文本学习因果结构。LLM 需要来自多样上下文的海量文本数据来识别词序列中的差分与非差分制造者，分析 token 嵌入与自注意力如何实现该逻辑。
- **与本单元的关联**: 本单元 notes.md 断言 LLM 停留因果阶梯 L1；该论文主张 LLM 从文本归纳学习因果结构，直接挑战本单元的 L1 天花板论断。

---

## critical_synthesis

这五篇论文共同揭示 2025-2026 年"LLM×因果"前沿的核心共识：LLM 不应作为因果效应的直接推断器，而应定位为因果工作流的辅助者与元裁判。Causal Ensemble Agent（2606.10607）将 LLM 限制在"聚合置信度接近决策边界时动态重加权专家"的元角色，Causal Discovery in the Era of Agents（2606.23608）进一步要求因果声明必须基于数据、显式假设与形式化算法，agent 仅负责检查数据、检索上下文、解释假设——二者共同收敛于"LLM 辅助、形式化主导"的方法论共识。然而该共识存在显著争议：Words as Difference Makers（2606.22430）主张 LLM 通过"差分逻辑"从海量文本归纳学习因果结构，暗示 LLM 具备超越因果阶梯 L1 的结构发现能力，与"LLM 停留 L1"的保守定位形成张力。方法学趋势上，CausalForge（2607.22511）以 Lean 机器检查定理将因果推断研究形式化，Causal-Audit（2607.15281）以目标感知图构建与路径级证据聚合实现可审计推理，二者代表从"统计反驳"向"形式化可审计"的演进。局限在于：除 CausalForge 与 Causal Ensemble Agent 经 abstract 页验证外，其余三篇未经验证；Causal Ensemble Agent 未开源代码与 LLM 元裁判 prompt，可复现性存疑；Words as Difference Makers 为纯理论论证无实验支撑；Causal-Audit 与 Causal Discovery in the Era of Agents 在自建平台（causal-learn+）上展示，未在 BNLearn/Tübingen 等标准因果发现基准对比，存在 benchmark-gaming 与选择性报告风险。博后读者应将这些声明视为"待独立复现的前沿假设"而非"已确立的方法"。

---

## delta_to_unit

1. **LLM 角色定位的精确化**：本单元 notes.md "2026 前沿补充"将 LLM-as-a-judge 定位为"辅助审查因果论证质量，不能替代统计估计"，对应因果阶梯 L1。Causal Ensemble Agent（2606.10607）将此定位精确化：LLM 应作为"元裁判"在统计发现专家聚合置信度接近决策边界时动态重加权，而非直接判断 DAG 合理性——这把本单元的"LLM 审查 DAG"升级为"LLM 重加权专家集合"，是本单元未覆盖的角色细分，需在教学中补充 LLM 介入因果发现的触发条件（决策边界邻近）。

2. **反驳检验的形式化升级**：本单元 solution.ipynb TODO5 用 DoWhy 的 `placebo_treatment_refuter` 做统计反驳检验，依赖扰动估计的统计稳定性。CausalForge（2607.22511）以 Lean 证明助手 + Causalean 库（7,035 条机器检查声明）将反驳升级为形式化定理证明，并通过声明审计比较形式化定理与非形式化声明——这是本单元统计反驳无法触及的可复现性层级，要求教学标注"统计反驳 ≠ 形式化证明"的层级差异。

3. **手画 DAG 向目标感知图演进**：本单元 notes.md "关键回顾 2"教学生"人为画因果 DAG"识别后门路径，DAG 是静态的全局结构。Causal-Audit（2607.15281）提出目标感知图构建策略（以目标变量如 `re78` 为核心约束抑制无关变量）与路径级因果证据聚合机制（建模跨多路径的增强与抵消效应），将本单元的静态手画 DAG 扩展为动态目标约束的可审计因果图——这要求本单元在 DAG 教学中引入"目标变量驱动的图剪枝"概念。

4. **因果阶梯 L1 天花板的争议**：本单元 notes.md 与 solution.ipynb 反思部分均明确断言 LLM-as-judge"停留在因果阶梯 L1，不能上升到 L2/L3"。Words as Difference Makers（2606.22430）论证 LLM 通过差分逻辑从多样上下文的海量文本中识别词序列中的差分与非差分制造者，暗示 LLM 具备从文本归纳因果结构的能力——这直接挑战本单元的 L1 天花板论断，需在教学中将其从"定论"降级为"开放争议"。

5. **LLM 辅助的形式化算法约束**：本单元 solution.ipynb 的 DoWhy 四步流程中，DAG 与识别策略由人工声明，LLM 仅作后置审查。Causal Discovery in the Era of Agents（2606.23608）主张 agent 辅助数据检查、预处理、方法推荐，但因果声明须基于数据与形式化算法——这要求本单元在引入 LLM 辅助时，必须配套形式化算法约束（如 PC/FCI），而非仅让 LLM 自由审查论证文本。

---

## open_questions

1. LLM 作为因果发现元裁判重加权专家时，其重加权决策是否可形式化证明满足后门准则，还是仅经验性有效？
2. CausalForge 的 Lean 形式化能否扩展到 NSW 这类观测数据的后门调整估计，还是仅适用于因果推断理论定理的机器检查？
3. Words as Difference Makers 主张 LLM 从文本学因果结构，这是否意味着 LLM 可越过因果阶梯 L1 直接做 L2 干预推断，从而颠覆 Pearl 阶梯的层级不可还原性？
4. Causal-Audit 的目标感知图构建在 NSW 8 协变量场景下，相比本单元手画 DAG 的后门调整估计，ATE 估计差异有多大，是否系统性偏离 Dehejia-Wahba $1794 基准？
5. Causal Discovery in the Era of Agents 的 causal-learn+ 平台在营销场景（如优惠券增量效应）中，agent 辅助的因果声明能否满足本单元 DoWhy 识别所需的可忽略性假设？

---

## methodological_critique

上述论文的局限性需在教学中显式标注。CausalForge（2607.22511）虽经 abstract 页验证，但 Causalean 库 7,035 条声明均围绕因果推断理论定理，未报告在 NSW/Lalonde 等观测数据基准上的形式化覆盖率，其形式化方法向应用因果估计的可迁移性未经验证。Causal Ensemble Agent（2606.10607）同样已验证，但未开源代码与 LLM 元裁判 prompt，"在合成与真实数据集达 SOTA"的声明无法独立复现，且 LLM 重加权的决策边界阈值选取标准未公开。Words as Difference Makers（2606.22430）为纯理论论证，无任何实验支撑其"差分逻辑"主张，token 嵌入与自注意力的因果结构映射仅为推测。Causal-Audit（2607.15281）与 Causal Discovery in the Era of Agents（2606.23608）均未经验证，且在自建平台 causal-learn+ 与 Big Five 人格数据上展示，未在 BNLearn/Tübingen 等标准因果发现基准对比，存在 benchmark-gaming 与选择性报告风险——作者既构建平台又评估平台，利益冲突明显。此外，多数论文作者为小团队，缺乏独立第三方复现。博后读者应将这些声明视为"待验证的前沿假设"而非"已确立的方法"，在引用时须区分 verified 与 unverified 标注。

---

*本文件由 v9.0 学术前沿注入层生成。所有论文链接来自 `_frontier_corpus/skill-3-causal.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证）。*
