# frontier.md (v9.0 学术前沿注入层)

> **所属**：技能3 因果推断与规模实验 · Day 5 规模实验与营销应用
> **版本**：v9.0（学术前沿注入层）
> **本单元前沿课题**：本单元教 MAB 自适应实验 + 营销归因（MMM/增量/因果媒介分析）+ CATE 精准投放 + Uplift Modeling + 三大因果陷阱。前沿子问题是"2025-2026 年 LLM 训练前瞻偏差如何污染 MMM 回测、CATE 外推如何支撑规模化精准投放、因果评估指标优化如何更新 Uplift Qini 评估"。

---

## frontier_topic

本单元以 NSW 真实响应率驱动 Thompson Sampling MAB、以 CausalForestDML 估计 CATE 支撑精准投放、以 Uplift Modeling 四类用户分类优化增量营销，并教 MMM 媒体混合模型（adstock+饱和+协同）做营销归因。2025-2026 前沿子问题是：当 LLM 训练语料的前瞻偏差被证实污染时间序列回测、当 CATE 估计可跨规模外推、当因果评估指标可用贝叶斯优化调优、当多模态因果推理可从多触点诱导因果图时，本单元的 MMM 回测有效性、CATE 精准投放的规模外推、Uplift Qini 评估的固定阈值是否仍成立。

---

## recent_papers

### 1. Scaling Point-in-Time Language Models
- **arXiv**: https://arxiv.org/abs/2607.11889
- **作者**: Bryan Kelly, Semyon Malamud
- **年份**: 2026
- **摘要**: 解决 LLM 在无限制互联网语料上训练的前瞻偏差问题，该偏差损害金融与社会科学中的回测和因果推断。在 1 万亿按时间过滤的 token 上训练至 4B 参数的 decoder-only transformer，构建 2013-2024 月度 checkpoint，接近同等规模时间无约束模型的性能。
- **与本单元的关联**: 本单元 notes.md "关键回顾 2"教 MMM 媒体混合模型用 adstock+饱和+协同做时序回归归因；该论文证实 LLM 训练语料前瞻偏差污染回测，直接挑战用 LLM 生成预测做 MMM 反事实基线的有效性。

### 2. CausalMix: Data Mixture as Causal Inference for Language Model Training
- **arXiv**: https://arxiv.org/abs/2607.01104
- **作者**: Zinan Tang, Yukun Zhang
- **年份**: 2026
- **摘要**: 将 LLM 训练的数据混合优化建模为因果推断问题，将数据池的统计特征作为协变量、领域混合作为处理。在 512 次 Qwen2.5-0.5B 运行上拟合因果模型估计 CATE 后，外推至 800K 数据池并应用于 7B 模型，持续超越 RegMix 等基线。
- **与本单元的关联**: 本单元 solution.ipynb TODO4 用 CausalForestDML 估计 CATE 支撑精准投放；CausalMix 将 CATE 估计+外推（0.5B->7B）应用于数据混合优化，为本单元 CATE 精准投放提供了跨规模外推的工业级参照。

### 3. Optimizing Large Language Models for Causality Assessment in Pharmacovigilance
- **arXiv**: https://arxiv.org/abs/2607.03704
- **作者**: Nicole Sonne Heckmann, Arnault-Quentin Vermillet
- **年份**: 2026
- **摘要**: 开发与高斯过程兼容的优化目标，研究温度优化是否改善 LLM 与专家在 Naranjo 因果评估上的一致性。EWACS 引导的贝叶斯优化将分类一致性从 45.0% 提升至 72.0%（+27pp），无通用温度最优值表明性能主要由 ICSR 内容驱动。
- **与本单元的关联**: 本单元 notes.md "2026 前沿补充"教 Uplift Modeling 用 Qini 曲线评估累计增量转化；该论文用贝叶斯优化调优因果评估指标（EWACS）而非固定阈值，挑战 Qini 评估中"固定投放比例阈值"的评估范式。

### 4. Pruning via Causal Attribution Preserves Reasoning Performance in Large Language Models
- **arXiv**: https://arxiv.org/abs/2606.19350
- **作者**: Amogh Sheth, Biruk Assefa
- **年份**: 2026
- **摘要**: 提出 Causal Attribution Pruning（CAP），无训练方法通过测量注意力头对推理任务的因果影响来识别关键头，再将头级重要性分数转化为权重级重要性进行剪枝。在 ARC-Challenge 20% 稀疏度下相对 Wanda 准确率提升最高 61%。
- **与本单元的关联**: 本单元 solution.ipynb TODO4 用 CausalForestDML 的 CATE 识别"对优惠券响应最大"的用户群做精准投放；CAP 用因果归因识别驱动 LLM 推理的关键注意力头--二者同为"因果归因驱动精准资源分配"，CAP 将本单元的"用户级 CATE"扩展至"模型内部注意力头级因果重要性"。

### 5. From Prompts to Tokens: Internalizing Causal Supervision in Vision-Language Model for Multi-Image Causal Reasoning
- **arXiv**: https://arxiv.org/abs/2606.11745
- **作者**: Haoping Yu, Yuanxi Li
- **年份**: 2026
- **摘要**: 提出 BridgeVLM，从多图像输入诱导因果图并转化为结构化 Causal Tokens，由注入 LLM 解码器的 RAMP 层执行。统一训练接口 M3S 提供局部和全局因果监督，在 CausalVLBench 干预任务上达 54.4% 准确率（prompt 级仅 33.2%）。
- **与本单元的关联**: 本单元 notes.md "关键回顾 2"教营销归因从启发式（末次/首次/线性触点）升级到因果方法；BridgeVLM 从多图像诱导因果图是多触点因果归因的视觉类比--从多触点行为日志诱导因果图，将本单元的"统计归因"扩展为"结构化因果图归因"。

---

## critical_synthesis

这五篇论文共同揭示 2025-2026 年营销因果应用前沿对"回测有效性""规模外推""评估阈值"三个核心问题的更新。共识层面：Scaling Point-in-Time（2607.11889）与 CausalMix（2607.01104）共同指出，时间序列数据中的前瞻偏差与数据混合的规模外推是因果应用的核心挑战--前者从 LLM 训练语料角度证实回测污染，后者从 CATE 跨规模外推角度验证可行性，二者收敛于"因果应用的有效性依赖数据生成过程与规模不变性假设"这一共识。争议层面：Pharmacovigilance（2607.03704）以贝叶斯优化将因果评估一致性从 45% 提升至 72%，但"无通用温度最优值、性能主要由 ICSR 内容驱动"的发现，与 Uplift Modeling 的 Qini 曲线"固定投放比例阈值"评估范式形成张力--暗示评估阈值应随内容自适应而非全局固定。方法学趋势上，Causal Attribution Pruning（2606.19350）以因果归因量化注意力头对推理的因果影响，BridgeVLM（2606.11745）以多图像因果图诱导实现结构化因果推理--二者代表因果应用向"模型内部因果结构"与"多模态因果归因"两个方向延伸。局限在于：本单元引用的 5 篇全部 unverified；Scaling Point-in-Time 的 4B 模型规模远小于工业 LLM，前瞻偏差消除效果能否扩展至 70B+ 未验证；CausalMix 的 0.5B->7B 外推假设 CATE 规模不变性，LLM 涌现能力可能使假设失效；Pharmacovigilance 仅在药物警戒单一领域验证；Causal Attribution Pruning 在 ARC-Challenge 单一基准展示；BridgeVLM 的 CausalVLBench 为自建基准，存在 benchmark-gaming 风险。博后读者应将这些声明视为"待独立复现的前沿假设"。

---

## delta_to_unit

1. **MMM 回测的前瞻偏差挑战**：本单元 notes.md "关键回顾 2"教 MMM 媒体混合模型用 adstock 变换（广告效果延迟衰减）+ 饱和效应 + 协同效应做时序回归归因，依赖历史数据的回测有效性。Scaling Point-in-Time（2607.11889）证实 LLM 训练语料前瞻偏差损害回测和因果推断--这意味着当营销团队用 LLM 生成的需求预测做 MMM 的反事实基线（"若无广告，销量会是多少"）时，前瞻偏差会系统性扭曲归因结果，本单元未覆盖这一数据生成过程层面的威胁。

2. **CATE 精准投放的跨规模外推参照**：本单元 solution.ipynb TODO4 用 CausalForestDML 在 NSW 445 样本上估计 CATE，支撑"对谁全量"的精准投放决策，但未涉及 CATE 的跨规模外推。CausalMix（2607.01104）在 512 次 0.5B 模型运行上拟合 CATE 后外推至 7B + 800K 数据池，为本单元 CATE 精准投放提供了"小样本 CATE 估计->大规模外推投放"的工业级范式，需在教学中标注"NSW 445 样本 CATE 能否外推至百万用户投放"。

3. **Uplift Qini 评估的自适应阈值挑战**：本单元 notes.md "2026 前沿补充"教 Uplift Modeling 用 Qini 曲线评估"按预测 CATE 从高到低投放，累计增量转化"，Qini 曲线的投放比例阈值固定。Pharmacovigilance（2607.03704）用贝叶斯优化调优因果评估指标（EWACS），将一致性从 45% 提升至 72%，且发现"无通用温度最优值、性能主要由 ICSR 内容驱动"--这暗示 Qini 评估的投放比例阈值应随用户群内容自适应，挑战本单元的"固定阈值 Qini 评估"范式。

4. **CATE 特征重要性的模型内部扩展**：本单元 solution.ipynb TODO4 用 CausalForestDML 的 CATE 识别"对优惠券响应最大"的用户群，依赖 `feature_importances_` 排序用户特征。Causal Attribution Pruning（2606.19350）用因果归因测量注意力头对推理任务的因果影响，将头级重要性转化为权重级重要性--这将本单元的"用户特征级 CATE 重要性"扩展至"LLM 注意力头级因果重要性"，为 CATE 在 LLM 推荐系统内部归因中的应用提供参照。

5. **多触点归因的结构化因果图升级**：本单元 notes.md "关键回顾 2"教营销归因从启发式（末次/首次/线性触点）升级到因果方法（增量测试/因果媒介分析/MMM），但仍以统计回归为主。BridgeVLM（2606.11745）从多图像输入诱导因果图并转化为结构化 Causal Tokens，在干预任务上达 54.4% 准确率（prompt 级仅 33.2%）--这为多触点营销归因提供了"从行为日志诱导结构化因果图"的新范式，将本单元的"统计归因"扩展为"结构化因果图归因"。

---

## open_questions

1. Scaling Point-in-Time 证实 LLM 训练前瞻偏差污染回测，那么用 LLM 生成需求预测做 MMM 反事实基线时，前瞻偏差对 adstock 参数估计的扭曲程度有多大，能否用 point-in-time checkpoint 量化校正？
2. CausalMix 在 0.5B 模型上拟合 CATE 后外推至 7B 假设规模不变性--这一假设在营销精准投放场景下是否成立，即 NSW 445 样本上的 CATE 能否外推至百万用户规模的投放决策？
3. Pharmacovigilance 发现"无通用温度最优值、性能主要由 ICSR 内容驱动"，那么 Uplift Modeling 的 Qini 曲线投放比例阈值是否也应随用户群内容（如用户活跃度分群）自适应调整，而非全局固定？
4. Causal Attribution Pruning 的注意力头因果归因方法，能否迁移至推荐系统的 CATE 估计--即用因果归因识别驱动用户响应的注意力头，而非仅用用户画像特征做 CausalForestDML？
5. BridgeVLM 从多图像诱导因果图的多模态方法，能否迁移至多触点营销归因--即从用户多触点行为日志（搜索/点击/加购/下单）诱导因果图，相比本单元的 MMM 统计回归归因，能否更准确识别增量转化路径？

---

## methodological_critique

上述论文的局限性需在教学中显式标注。Scaling Point-in-Time（2607.11889）的 4B 参数模型规模远小于工业级 LLM（70B+），前瞻偏差消除效果能否随规模保持未验证，且 1 万亿 token 的时间过滤语料可能引入新的选择偏差（仅保留时间戳明确的数据），2013-2024 月度 checkpoint 的计算成本高昂，普通营销团队难以复现。CausalMix（2607.01104）在 0.5B 模型上拟合 CATE 后外推至 7B，外推有效性假设 CATE 规模不变性，但 LLM 的涌现能力可能使小规模 CATE 估计失真；512 次运行的实验规模可能不足以覆盖高维 CATE 空间，且未开源代码。Pharmacovigilance（2607.03704）仅在药物警戒单一领域验证，Naranjo 评估的 45%->72% 提升能否迁移至营销 Uplift 评估存疑，贝叶斯优化的高斯过程代理模型在低样本量下可能过拟合，且"无通用温度最优值"暗示优化结果可能不稳定。Causal Attribution Pruning（2606.19350）在 ARC-Challenge 单一基准上的 61% 提升能否迁移至其他推理任务未验证，因果归因方法可能依赖特定 transformer 注意力机制假设，且 20% 稀疏度下的准确率提升可能以牺牲其他稀疏度下的性能为代价。BridgeVLM（2606.11745）的 CausalVLBench 为自建基准，作者既构建基准又评估方法，存在 benchmark-gaming 风险，54.4% vs 33.2% 的对比未报告统计显著性，且多图像因果推理能否迁移至多触点营销归因未验证。博后读者应将这 5 篇全部 unverified 的声明视为"待独立复现的前沿假设"。

---

*本文件由 v9.0 学术前沿注入层生成。所有论文链接来自 `_frontier_corpus/skill-3-causal.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证）。*
