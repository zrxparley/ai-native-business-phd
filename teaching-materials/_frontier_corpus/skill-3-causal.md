# 前沿语料库: skill-3-causal - 因果推断×大语言模型

> v9.0 前沿注入层共享语料库. 论文来自 arXiv 搜索 (2025-09 ~ 2026-07, post 2025-08 cutoff). 标注 verified 的论文经 abstract 页抽查. wave agent 仅可引用本文档列出的论文, 禁止编造.

## 论文

### 1. CausalForge: A Formally Grounded, Self-Improving Agentic Framework for Automated Research in Causal Inference
- **arXiv**: https://arxiv.org/abs/2607.22511
- **作者**: Jiyuan Tan, Vasilis Syrgkanis
- **年份**: 2026
- **摘要**: 提出 CausalForge, 基于 Lean 证明助手的因果推断自动化理论研究框架. 结合 Causalean (7,035 条机器检查声明的 Lean 库) 与 CausalSmith (自改进 agentic pipeline), 用于选择研究主题、提出结果并构造证明, 并通过声明审计比较形式化定理与非形式化声明.
- **验证**: verified

### 2. Causal Ensemble Agent: Hierarchical Causal Discovery with LLM-guided Expert Reweighting
- **arXiv**: https://arxiv.org/abs/2606.10607
- **作者**: Xinyu Li, Yuanyuan Wang
- **年份**: 2026
- **摘要**: 提出 Causal Ensemble Agent (CEA), 通过线性意见池聚合统计发现专家的结构洞察, 使用 LLM 作为元裁判在聚合置信度接近决策边界时动态重新加权专家. LLM 用于元分析而非直接因果推断, 在合成和真实数据集上达到最强整体性能.
- **验证**: verified

### 3. Scaling Point-in-Time Language Models
- **arXiv**: https://arxiv.org/abs/2607.11889
- **作者**: Bryan Kelly, Semyon Malamud
- **年份**: 2026
- **摘要**: 解决 LLM 在无限制互联网语料上训练的前瞻偏差问题, 该偏差损害金融与社会科学中的回测和因果推断. 在 1 万亿按时间过滤的 token 上训练至 4B 参数的 decoder-only transformer, 构建 2013-2024 月度 checkpoint, 接近同等规模时间无约束模型的性能.
- **验证**: unverified

### 4. CausalMix: Data Mixture as Causal Inference for Language Model Training
- **arXiv**: https://arxiv.org/abs/2607.01104
- **作者**: Zinan Tang, Yukun Zhang
- **年份**: 2026
- **摘要**: 将 LLM 训练的数据混合优化建模为因果推断问题, 将数据池的统计特征作为协变量、领域混合作为处理. 在 512 次 Qwen2.5-0.5B 运行上拟合因果模型估计 CATE 后, 外推至 800K 数据池并应用于 7B 模型, 持续超越 RegMix 等基线.
- **验证**: unverified

### 5. Causal Discovery in the Era of Agents
- **arXiv**: https://arxiv.org/abs/2606.23608
- **作者**: Yujia Zheng, Vishal Verma
- **年份**: 2026
- **摘要**: 论证 agent 在因果发现中应辅助工作流 (检查数据、检索上下文、解释假设), 而因果声明须基于数据、显式假设和形式化算法. 提出 causal-learn+ 在线平台, 协调数据分析、预处理、方法推荐和形式化发现, 在 Big Five 人格数据上展示 agent 辅助因果发现.
- **验证**: unverified

### 6. Words as Difference Makers: How Large Language Models Determine Causal Structure in Text
- **arXiv**: https://arxiv.org/abs/2606.22430
- **作者**: Wolfgang Pietsch
- **年份**: 2026
- **摘要**: 论证 LLM 采用基于"差分逻辑" (difference-making logic / variational induction) 的归纳方法从文本学习因果结构. LLM 需要来自多样上下文的海量文本数据来识别词序列中的差分和非差分制造者, 分析 token 嵌入和自注意力如何实现该逻辑.
- **验证**: unverified

### 7. Pruning via Causal Attribution Preserves Reasoning Performance in Large Language Models
- **arXiv**: https://arxiv.org/abs/2606.19350
- **作者**: Amogh Sheth, Biruk Assefa
- **年份**: 2026
- **摘要**: 提出 Causal Attribution Pruning (CAP), 无训练方法通过测量注意力头对推理任务的因果影响来识别关键头, 再将头级重要性分数转化为权重级重要性进行剪枝. 在 ARC-Challenge 20% 稀疏度下相对 Wanda 准确率提升最高 61%.
- **验证**: unverified

### 8. From Prompts to Tokens: Internalizing Causal Supervision in Vision-Language Model for Multi-Image Causal Reasoning
- **arXiv**: https://arxiv.org/abs/2606.11745
- **作者**: Haoping Yu, Yuanxi Li
- **年份**: 2026
- **摘要**: 提出 BridgeVLM, 从多图像输入诱导因果图并转化为结构化 Causal Tokens, 由注入 LLM 解码器的 RAMP 层执行. 统一训练接口 M3S 提供局部和全局因果监督, 在 CausalVLBench 干预任务上达 54.4% 准确率 (prompt 级仅 33.2%).
- **验证**: unverified

### 9. Causal-Audit: Explicit and Auditable Graph-based Reasoning via Target-Aware Causal Chain Construction
- **arXiv**: https://arxiv.org/abs/2607.15281
- **作者**: Su Lan, Xuefei Yin
- **年份**: 2026
- **摘要**: 提出显式可审计的因果推理框架, 将因果推断建模为在显式因果图上的结构化推理. 目标感知图构建策略在扩展时将目标变量作为核心约束以抑制无关变量, 路径级因果证据聚合机制建模跨多路径的增强和抵消效应.
- **验证**: unverified

### 10. Optimizing Large Language Models for Causality Assessment in Pharmacovigilance: Developing a Performance Metric as Objective for Bayesian Hyperparameter Optimization
- **arXiv**: https://arxiv.org/abs/2607.03704
- **作者**: Nicole Sonne Heckmann, Arnault-Quentin Vermillet
- **年份**: 2026
- **摘要**: 开发与高斯过程兼容的优化目标, 研究温度优化是否改善 LLM 与专家在 Naranjo 因果评估 (FAERS 个案安全报告) 上的一致性, 使用 GPT-5.2. EWACS 引导的贝叶斯优化将分类一致性从 45.0% 提升至 72.0% (+27pp), 无通用温度最优值表明性能主要由 ICSR 内容驱动.
- **验证**: unverified

## 备注
- 论文 1 (CausalForge/2607.22511) 将因果推断研究与形式化证明 (Lean) 结合, 代表"LLM×因果"前沿的方法论创新, 已 verified.
- 论文 2 (Causal Ensemble Agent/2606.10607) 将 LLM 定位为因果发现的元裁判而非直接推断器, 是 LLM 在因果发现中角色定位的重要参考, 已 verified.
- arXiv 搜索查询: "causal inference large language model", sorted by newest first. 搜索返回 40 篇可见论文, 全部在 2025-09 ~ 2026-07 范围内.
- 选材偏向: LLM 辅助因果发现/推断、LLM 训练中的因果建模、因果可解释性/剪枝、视觉因果推理、领域应用 (金融/药物警戒).
