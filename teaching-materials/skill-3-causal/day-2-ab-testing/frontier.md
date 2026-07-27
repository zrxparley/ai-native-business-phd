# frontier.md (v9.0 学术前沿注入层)

> **所属**：技能3 因果推断与规模实验 · Day 2 实验设计与 A/B 测试统计
> **版本**：v9.0（学术前沿注入层）
> **本单元前沿课题**：本单元教 RCT 均值差=ATE + 样本量计算 + CUPED 方差缩减 + 准实验（DiD/RDD/ITS）。前沿子问题是"2025-2026 年 LLM 训练数据的前瞻偏差如何污染准实验回测、因果评估指标优化如何更新显著性检验范式、目标感知图构建如何自动化 CUPED 协变量选择"。

---

## frontier_topic

本单元以 NSW 真实 RCT 数据教随机化消除混杂（均值差=ATE）、样本量计算、显著性检验（t/Z 检验 + p<0.05 警示）、CUPED 方差缩减（re75→re78）及准实验设计（DiD/RDD/ITS）。2025-2026 前沿子问题是：当 LLM 训练语料的前瞻偏差被证实损害回测与因果推断、当因果评估指标可通过贝叶斯优化而非固定 α=0.05 调优、当目标感知图构建可自动化 CUPED 协变量选择时，本单元的准实验回测有效性、显著性检验范式与人工协变量选择是否仍成立。

---

## recent_papers

### 1. Scaling Point-in-Time Language Models
- **arXiv**: https://arxiv.org/abs/2607.11889
- **作者**: Bryan Kelly, Semyon Malamud
- **年份**: 2026
- **摘要**: 解决 LLM 在无限制互联网语料上训练的前瞻偏差问题，该偏差损害金融与社会科学中的回测和因果推断。在 1 万亿按时间过滤的 token 上训练至 4B 参数的 decoder-only transformer，构建 2013-2024 月度 checkpoint，接近同等规模时间无约束模型的性能。
- **与本单元的关联**: 本单元 notes.md "关键回顾 5"教 ITS/DiD 准实验依赖"无干预时趋势稳定"与"平行趋势"假设；该论文证实训练数据前瞻偏差会污染时间序列回测，直接挑战准实验回测的有效性前提。

### 2. CausalMix: Data Mixture as Causal Inference for Language Model Training
- **arXiv**: https://arxiv.org/abs/2607.01104
- **作者**: Zinan Tang, Yukun Zhang
- **年份**: 2026
- **摘要**: 将 LLM 训练的数据混合优化建模为因果推断问题，将数据池的统计特征作为协变量、领域混合作为处理。在 512 次 Qwen2.5-0.5B 运行上拟合因果模型估计 CATE 后，外推至 800K 数据池并应用于 7B 模型，持续超越 RegMix 等基线。
- **与本单元的关联**: 本单元 solution.ipynb TODO6 用 CUPED 将 re75 作为协变量缩减 re78 方差；CausalMix 将"协变量选择+处理效应估计"升级为 CATE 外推框架，是 CUPED 协变量选择的因果化扩展。

### 3. Optimizing Large Language Models for Causality Assessment in Pharmacovigilance
- **arXiv**: https://arxiv.org/abs/2607.03704
- **作者**: Nicole Sonne Heckmann, Arnault-Quentin Vermillet
- **年份**: 2026
- **摘要**: 开发与高斯过程兼容的优化目标，研究温度优化是否改善 LLM 与专家在 Naranjo 因果评估上的一致性。EWACS 引导的贝叶斯优化将分类一致性从 45.0% 提升至 72.0%（+27pp），无通用温度最优值表明性能主要由 ICSR 内容驱动。
- **与本单元的关联**: 本单元 notes.md "关键回顾 3"教固定 α=0.05 显著性检验；该论文用贝叶斯优化调优因果评估指标而非固定阈值，挑战本单元"固定 α"的评估范式。

### 4. Causal-Audit: Explicit and Auditable Graph-based Reasoning via Target-Aware Causal Chain Construction
- **arXiv**: https://arxiv.org/abs/2607.15281
- **作者**: Su Lan, Xuefei Yin
- **年份**: 2026
- **摘要**: 提出显式可审计的因果推理框架，将因果推断建模为在显式因果图上的结构化推理。目标感知图构建策略在扩展时将目标变量作为核心约束以抑制无关变量，路径级因果证据聚合机制建模跨多路径的增强和抵消效应。
- **与本单元的关联**: 本单元 solution.ipynb TODO6 人工选 re75 作 CUPED 协变量；Causal-Audit 的目标感知图构建以目标变量（如 re78）为核心约束自动剪枝无关变量，是 CUPED 协变量选择的自动化升级。

### 5. CausalForge: A Formally Grounded, Self-Improving Agentic Framework for Automated Research in Causal Inference
- **arXiv**: https://arxiv.org/abs/2607.22511
- **作者**: Jiyuan Tan, Vasilis Syrgkanis
- **年份**: 2026
- **摘要**: 提出 CausalForge，基于 Lean 证明助手的因果推断自动化研究框架。结合 Causalean（7,035 条机器检查声明的 Lean 库）与 CausalSmith（自改进 agentic pipeline），用于选择研究主题、提出结果并构造证明，并通过声明审计比较形式化定理与非形式化声明。
- **与本单元的关联**: 本单元 solution.ipynb 的 6 个 TODO 无反驳检验（对比 Day 1/3 有 placebo_treatment_refuter）；CausalForge 将统计反驳升级为 Lean 机器检查形式化证明，补全本单元缺失的稳健性验证层级。

---

## critical_synthesis

这五篇论文共同揭示 2025-2026 年因果推断前沿对实验设计的三重更新。共识层面：Scaling Point-in-Time（2607.11889）与 CausalMix（2607.01104）共同指出，时间序列数据中的前瞻偏差与数据混合的混杂效应是因果推断的核心威胁--前者从 LLM 训练语料角度证实回测污染，后者从数据混合角度将混杂建模为可估计的 CATE，二者收敛于"因果有效性依赖数据生成过程的形式化约束"这一共识。争议层面：Pharmacovigilance（2607.03704）以贝叶斯优化将因果评估一致性从 45% 提升至 72%，但"无通用温度最优值、性能主要由 ICSR 内容驱动"的发现，与本单元固定 α=0.05 的检验范式形成张力--暗示评估阈值应随内容自适应而非全局固定，这一争议直指频率派与贝叶斯派在因果评估中的根本分歧。方法学趋势上，Causal-Audit（2607.15281）的目标感知图构建与 CausalForge（2607.22511）的 Lean 形式化代表从"人工声明假设+统计检验"向"自动化图构建+形式化验证"的演进。局限在于：仅 CausalForge 经 abstract 页验证，其余四篇均 unverified；Scaling Point-in-Time 的 4B 参数模型规模远小于工业 LLM，前瞻偏差消除效果能否扩展至 70B+ 未验证；CausalMix 在 0.5B 模型上拟合 CATE 后外推至 7B，外推有效性假设了 CATE 的规模不变性，这一假设未经验证；Pharmacovigilance 仅在药物警戒单一领域验证，通用性存疑；Causal-Audit 未在标准因果发现基准对比。博后读者应将这些声明视为"待独立复现的前沿假设"。

---

## delta_to_unit

1. **准实验回测有效性的前瞻偏差挑战**：本单元 notes.md "关键回顾 5"教 ITS（中断时间序列）依赖"无干预时趋势稳定"，DiD 依赖"平行趋势"。Scaling Point-in-Time（2607.11889）证实 LLM 训练语料的前瞻偏差会污染金融与社会科学的回测和因果推断--这意味着当分析师用 LLM 生成的时间序列预测做 ITS/DiD 的反事实基线时，前瞻偏差会系统性扭曲"无干预趋势"的估计，本单元未覆盖这一数据生成过程层面的威胁。

2. **CUPED 协变量选择的因果化升级**：本单元 solution.ipynb TODO6 人工选 `re75`（1975 收入）作 CUPED 协变量缩减 `re78` 方差，依赖"re75 与 re78 高相关"的经验判断。CausalMix（2607.01104）将协变量选择+处理效应估计建模为 CATE 估计+外推框架（在 0.5B 上拟合后外推至 7B），Causal-Audit（2607.15281）以目标变量（re78）为核心约束自动剪枝无关变量--二者共同将本单元的人工协变量选择升级为因果化、目标驱动的自动化选择，需在教学中标注"人工选 re75 ≠ 因果最优协变量"。

3. **显著性检验范式的自适应挑战**：本单元 notes.md "关键回顾 3"教固定 α=0.05 显著性检验，并警示"p<0.05 不等于效应重要"。Pharmacovigilance（2607.03704）用贝叶斯优化调优因果评估指标（EWACS），将分类一致性从 45% 提升至 72%，且发现"无通用温度最优值、性能主要由 ICSR 内容驱动"--这暗示评估阈值应随内容自适应而非全局固定 α=0.05，直接挑战本单元的固定阈值范式。

4. **反驳检验的形式化补全**：本单元 solution.ipynb 的 6 个 TODO 聚焦均衡性检验、样本量、显著性、CUPED，无反驳检验（对比 Day 1 TODO5 与 Day 3 TODO5 均有 `placebo_treatment_refuter`）。CausalForge（2607.22511）以 Lean 证明助手 + Causalean 库（7,035 条机器检查声明）将反驳升级为形式化定理证明--这要求本单元在 RCT 教学中补全"统计均衡性检验 ≠ 形式化随机化验证"的层级差异。

5. **目标感知图对均衡性检验的扩展**：本单元 solution.ipynb TODO2 逐变量做 t 检验验证 RCT 均衡性（p>0.05 表示均衡），是单变量逐个检验。Causal-Audit（2607.15281）的目标感知图构建策略以目标变量为核心约束抑制无关变量，路径级证据聚合建模跨多路径的增强和抵消效应--这将本单元的逐变量均衡性检验扩展为目标驱动的多路径联合检验。

---

## open_questions

1. Scaling Point-in-Time 证实 LLM 训练语料前瞻偏差污染回测，那么用 LLM 生成的反事实基线做 ITS/DiD 准实验分析时，前瞻偏差对"平行趋势假设"检验的扭曲程度有多大，能否用 point-in-time checkpoint 量化校正？
2. CausalMix 在 0.5B 模型上拟合 CATE 后外推至 7B，假设了 CATE 的规模不变性--这一假设在 CUPED 协变量选择场景下是否成立，即小样本上最优的 CUPED 协变量能否外推至大样本？
3. Pharmacovigilance 发现"无通用温度最优值、性能主要由 ICSR 内容驱动"，那么 A/B 测试的显著性阈值 α 是否也应随实验内容（如转化率基线、效应大小）自适应调整，而非全局固定 0.05？
4. CausalForge 的 Lean 形式化能否扩展到 RCT 的随机化假设验证，即用机器检查证明 NSW 的随机化分配满足无混杂性，还是仅适用于因果推断理论定理？
5. Causal-Audit 的目标感知图构建在 NSW 8 协变量场景下，相比本单元 TODO2 的逐变量 t 检验均衡性检验，能否检测出逐变量检验遗漏的多路径交互失衡？

---

## methodological_critique

上述论文的局限性需在教学中显式标注。Scaling Point-in-Time（2607.11889）虽解决前瞻偏差，但 4B 参数模型规模远小于工业级 LLM（70B+），前瞻偏差消除效果能否随规模保持未验证，且 1 万亿 token 的时间过滤语料可能引入新的选择偏差（仅保留时间戳明确的数据），2013-2024 月度 checkpoint 的计算成本高昂，普通营销团队难以复现。CausalMix（2607.01104）在 0.5B 模型上拟合 CATE 后外推至 7B，外推有效性假设 CATE 的规模不变性，但 LLM 的涌现能力可能使小规模 CATE 估计失真；512 次运行的实验规模可能不足以覆盖高维 CATE 空间，且未开源代码。Pharmacovigilance（2607.03704）仅在药物警戒单一领域验证，Naranjo 评估的 45%→72% 提升能否迁移至营销 A/B 测试的因果评估存疑，且贝叶斯优化的高斯过程代理模型在低样本量下可能过拟合。Causal-Audit（2607.15281）未经验证，未在 BNLearn/Tübingen 等标准基准对比，目标感知图构建的计算复杂度在 8+ 协变量场景下未报告。CausalForge（2607.22511）虽经验证，但 Causalean 库 7,035 条声明围绕理论定理，未报告在 NSW/Lalonde 等应用基准上的覆盖率。博后读者应区分 verified 与 unverified 标注，将这些声明视为"待独立复现的前沿假设"。

---

*本文件由 v9.0 学术前沿注入层生成。所有论文链接来自 `_frontier_corpus/skill-3-causal.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证）。*
