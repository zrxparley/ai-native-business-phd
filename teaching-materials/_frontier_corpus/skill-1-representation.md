# 前沿语料库: skill-1-representation - 多模态表示学习与检索对齐

> v9.0 前沿注入层共享语料库. 论文来自 arXiv 搜索 (2025-09 ~ 2026-07, post 2025-08 cutoff). 标注 verified 的论文经 abstract 页抽查. wave agent 仅可引用本文档列出的论文, 禁止编造.

## 论文

### 1. Beyond Objective Expressivity: Geometry Preservation in Multimodal Contrastive Learning
- **arXiv**: https://arxiv.org/abs/2607.17673
- **作者**: Tillmann Rheude, Roland Eils
- **年份**: 2026
- **摘要**: 识别编码器 Jacobian 条件数为三模态对比学习的关键因素, 条件不良的编码器会退化多模态对齐. 提出几何保持编码器 (GPE), 在多个对比目标和数据集上提升检索与线性探测性能.
- **验证**: verified

### 2. Gemini Embedding 2: A Native Multimodal Embedding Model from Gemini
- **arXiv**: https://arxiv.org/abs/2605.27295
- **作者**: Madhuri Shanbhogue, Zhe Li
- **年份**: 2026
- **摘要**: 原生多模态嵌入模型, 通过大规模对比学习将视频、音频、图像、文本统一到单一表示空间. 达到 SOTA: MSCOCO R@1 62.9, Vatex NDCG@10 68.8, MTEB 多语言 69.9.
- **验证**: verified

### 3. Learning Sparse Representations of Multimodal Content for Enhanced Cold Item Recommendation
- **arXiv**: https://arxiv.org/abs/2607.17184
- **作者**: Gregor Meehan, Johan Pauwels
- **年份**: 2026
- **摘要**: 论证稀疏嵌入在内容冷启动推荐中相较密集向量的优势, 改造现有训练范式以适配稀疏表示学习. 在四个多模态推荐系统数据集上, 冷启动准确率显著提升且存储成本更低.
- **验证**: unverified

### 4. From Modalities To Propositions: A Language-Centric Framework for Multimodal Intelligence
- **arXiv**: https://arxiv.org/abs/2607.16560
- **作者**: Nadine Chang, Maying Shen
- **年份**: 2026
- **摘要**: 提出以语言表示多模态数据的框架, 任何观测 (图像/视频/文本) 表达为由全局语义码本统一的原子命题袋. 支持跨模态理解、检索与组合性, 在自动驾驶和开放世界数据上验证.
- **验证**: unverified

### 5. AlphaWiSE: Adaptive Weight Interpolation for Continual Multimodal Representation Learning
- **arXiv**: https://arxiv.org/abs/2607.15094
- **作者**: Sarthak Jain, Qiran Hu
- **年份**: 2026
- **摘要**: 事后权重空间插值方法, 组合两个冻结 checkpoint 实现持续多模态学习, 在 exemplar memory 上拟合标量插值系数. 在音频-图像-文本检索上持续优于强持续学习基线.
- **验证**: unverified

### 6. MMRM: A Multiplex Multimodal Representation Model for Product Ranking in E-commerce Search
- **arXiv**: https://arxiv.org/abs/2607.11030
- **作者**: Zhen-Lin Chen, Maosen Sheng
- **年份**: 2026
- **摘要**: 统一框架将 MLLM 与多样协作信号对齐, 在单次推理中生成多路复用商品表示. 部署于京东电商搜索引擎, 为数百万日活用户带来显著性能提升.
- **验证**: unverified

### 7. DREAM: Extending Vision-Language Models with Dual-Objective Encoding for Cross-Modal Retrieval
- **arXiv**: https://arxiv.org/abs/2606.19062
- **作者**: Kaleem Ullah, Altaf Hussain
- **年份**: 2026
- **摘要**: 多模态框架, 结合 masked 和 permuted 目标的混合语言建模策略, 配合级联组注意力的分层视觉编码器. 在 MSRVTT、MSVD、LSMDC 基准上达到新 SOTA R1 分数 49.4%、49.7%、27.3%.
- **验证**: unverified

### 8. Inference-Free Multimodal Learned Sparse Retrieval for Production-Scale Visual Document Search
- **arXiv**: https://arxiv.org/abs/2605.30917
- **作者**: Gyu-Hwung Cho, Youngjune Lee
- **年份**: 2026
- **摘要**: 提出用于视觉文档检索的无推理稀疏检索器, 使用 caption-gated token 监督激活检索相关词汇维度. 在 1870 万文档语料上 NDCG@5 较密集基线平均提升 +13.8pp, R@5 翻倍以上.
- **验证**: unverified

### 9. UniNote: A Unified Embedding Model for Multimodal Representation and Ranking
- **arXiv**: https://arxiv.org/abs/2605.29287
- **作者**: Jinghan Zhao, Wenwei Jin
- **年份**: 2026
- **摘要**: 工业级 I2I 检索统一嵌入模型, 针对不同粒度的复杂多模态内容提供定制检索策略, 采用对比 SFT + RL 排序精炼两阶段范式. 部署于小红书并配合 MRL, 在检索质量与成本效率上显著提升.
- **验证**: unverified

### 10. CMDR: Contextual Multimodal Document Retrieval
- **arXiv**: https://arxiv.org/abs/2607.05927
- **作者**: Ryota Tanaka, Taku Hasegawa
- **年份**: 2026
- **摘要**: 提出多模态文档检索新任务与基准 CMDR-Bench, 要求文档上下文建模; 以及 CMDR-Embed 框架, 联合编码多页以导出上下文页面级嵌入. 实验表明显著优于非上下文嵌入.
- **验证**: unverified

## 备注
- 论文 1 (2607.17673) 从几何角度分析多模态对比学习的表示对齐, 理论贡献突出, 已 verified.
- 论文 2 (Gemini Embedding 2/2605.27295) 是 Google 原生多模态嵌入工业级模型, 直接覆盖"表示学习+检索对齐"双主题, 已 verified.
- arXiv 搜索查询: "multimodal representation learning retrieval", sorted by newest first. 搜索返回 39 篇可见论文 (页面显示共 547 结果), 全部在 2025-09 ~ 2026-07 范围内.
- 选材偏向: 对比学习理论、稀疏 vs 密集表示、跨模态检索、工业级部署 (JD/小红书/Gemini).
