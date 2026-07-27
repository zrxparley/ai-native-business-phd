# frontier.md (v9.0 学术前沿注入层)

> **所属**：skill-1-representation · day-2-marketing-representation
> **版本**：v9.0（学术前沿注入层）
> **本单元前沿课题**：工业级营销表示的持续学习 + 多路复用商品表示 + I2I 检索的对比 SFT+RL 两阶段范式 + 冷启动稀疏表示，如何更新本单元所教的四大表示类型 + Two-Tower + InfoNCE + CLIP 图文对齐。

---

## frontier_topic

本单元教授营销场景四大表示类型（客户/产品/内容/跨域对齐）+ Two-Tower InfoNCE + CLIP 图文对齐。2025-2026 前沿从四个工业级部署更新这些方法：① 京东 MMRM 用多路复用商品表示（MLLM + 协作信号）替代单一 Two-Tower；② 小红书 UniNote 用对比 SFT + RL 排序精炼两阶段范式替代纯 InfoNCE；③ AlphaWiSE 用权重空间插值实现持续多模态学习（新品上架不停机）；④ 稀疏嵌入在冷启动推荐上挑战密集向量。这些论文将本单元的"教学级 Two-Tower"推向"工业级多路复用 + 持续学习 + 稀疏冷启动"。

---

## recent_papers

### 1. MMRM: A Multiplex Multimodal Representation Model for Product Ranking in E-commerce Search
- **arXiv**: https://arxiv.org/abs/2607.11030
- **作者**: Zhen-Lin Chen, Maosen Sheng
- **年份**: 2026
- **摘要**: 统一框架将 MLLM 与多样协作信号对齐，在单次推理中生成多路复用商品表示。部署于京东电商搜索引擎，为数百万日活用户带来显著性能提升。
- **与本单元的关联**: 本单元 notes.md "关键回顾 2" 教 Two-Tower 单一架构（客户塔 + 产品塔 + InfoNCE）；此论文用 MLLM + 协作信号的多路复用表示替代单一双塔，是对 Two-Tower 的工业级扩展。

### 2. UniNote: A Unified Embedding Model for Multimodal Representation and Ranking
- **arXiv**: https://arxiv.org/abs/2605.29287
- **作者**: Jinghan Zhao, Wenwei Jin
- **年份**: 2026
- **摘要**: 工业级 I2I 检索统一嵌入模型，针对不同粒度的复杂多模态内容提供定制检索策略，采用对比 SFT + RL 排序精炼两阶段范式。部署于小红书并配合 MRL，在检索质量与成本效率上显著提升。
- **与本单元的关联**: 本单元 solution.ipynb TODO4 用纯 InfoNCE 训练 Two-Tower；此论文用"对比 SFT + RL 排序精炼"两阶段范式替代单阶段 InfoNCE，是对本单元训练范式的工业级升级。

### 3. AlphaWiSE: Adaptive Weight Interpolation for Continual Multimodal Representation Learning
- **arXiv**: https://arxiv.org/abs/2607.15094
- **作者**: Sarthak Jain, Qiran Hu
- **年份**: 2026
- **摘要**: 事后权重空间插值方法，组合两个冻结 checkpoint 实现持续多模态学习，在 exemplar memory 上拟合标量插值系数。在音频-图像-文本检索上持续优于强持续学习基线。
- **与本单元的关联**: 本单元教四大表示类型但未覆盖"新品持续上架"场景（模型需不停重训）；此论文的权重插值方法让营销表示模型支持持续学习，填补本单元的持续学习空白。

### 4. Learning Sparse Representations of Multimodal Content for Enhanced Cold Item Recommendation
- **arXiv**: https://arxiv.org/abs/2607.17184
- **作者**: Gregor Meehan, Johan Pauwels
- **年份**: 2026
- **摘要**: 论证稀疏嵌入在内容冷启动推荐中相较密集向量的优势，改造现有训练范式以适配稀疏表示学习。在四个多模态推荐系统数据集上，冷启动准确率显著提升且存储成本更低。
- **与本单元的关联**: 本单元 solution.ipynb TODO1-3 用 sentence-transformers 密集向量做客户/产品/内容 embedding；此论文证明稀疏嵌入在冷启动（新品/新客）场景更优，直接挑战本单元的密集向量默认选择。

---

## critical_synthesis

这四篇论文共同揭示了 2025-2026 营销表示工程从"教学级双塔"向"工业级多路复用 + 持续学习"的范式迁移。**共识**：纯 InfoNCE 对比学习的单一阶段训练不足以支撑工业级营销检索--UniNote（对比 SFT + RL 排序精炼）和 MMRM（MLLM + 协作信号多路复用）都采用多阶段/多信号融合，表明"对比学习是基础但非终点"已成为工业界共识。**争议**：持续学习的路径存在分歧。AlphaWiSE 用权重空间插值（组合冻结 checkpoint）实现持续学习，不需重训；而 MMRM/UniNote 隐含的路径是定期重训 + 在线更新。前者低成本但可能损失新模态信息，后者高成本但表示更准确--哪种路径在营销场景（新品高频上架）更优未达成共识。**趋势**：稀疏表示从检索（Meehan & Pauwels）到工业部署（UniNote 配合 MRL）正在渗透营销推荐全链路，密集向量的垄断地位正在松动。**局限**：四篇论文均为工业部署（JD/小红书/音频-图像-文本），其"显著提升"声明依赖内部 A/B 数据，学术界难以独立验证；AlphaWiSE 的 exemplar memory 假设在营销场景（客户行为持续漂移）下是否成立未讨论；Meehan & Pauwels 的稀疏优势仅在冷启动验证，热启动（已有行为数据的成熟品）是否仍优未明。整体而言，前沿论文将本单元的 Two-Tower + InfoNCE 基础推向多阶段 + 多路复用 + 持续学习 + 稀疏冷启动，但教学级基础仍是理解这些工业扩展的前提。

---

## delta_to_unit

1. **多阶段训练范式替代纯 InfoNCE**：本单元 solution.ipynb TODO4 的 `info_nce_loss` 函数用单阶段对比损失（temperature=0.1）训练 TwoTowerModel 100 步。UniNote 2026 用"对比 SFT + RL 排序精炼"两阶段范式--第一阶段对比学习初始化表示空间，第二阶段 RL 精炼排序质量。本单元的 TODO4 缺少第二阶段 RL 精炼，这是工业级营销检索的关键缺失。

2. **多路复用表示替代单一双塔**：本单元 notes.md "关键回顾 2" 的 Two-Tower 架构（Tower A 客户 + Tower B 产品 + cos(u,v)）是单一表示路径。MMRM 2026 在单次推理中生成多路复用商品表示（MLLM + 协作信号），部署于京东搜索引擎--本单元的单一双塔未覆盖协作信号融合，需补充多路复用架构作为 Two-Tower 的工业级扩展。

3. **持续学习填补新品上架空白**：本单元 solution.ipynb 的 8 个客户 + 8 个产品是静态数据集，未讨论"新品持续上架"场景。AlphaWiSE 2026 的权重空间插值方法（组合两个冻结 checkpoint + 标量系数）让模型支持持续学习而无需全量重训--本单元应补充持续学习作为营销表示工程的必备能力（新品每周上架是营销常态）。

4. **稀疏嵌入挑战密集向量默认**：本单元 solution.ipynb TODO1-3 用 `SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')` 生成 384 维密集向量做客户/产品/内容 embedding。Meehan & Pauwels 2026 在四个多模态推荐数据集上证明稀疏嵌入在冷启动（新客/新品）场景准确率更高且存储更低--本单元将密集向量作为默认选择，未覆盖稀疏替代方案，需补充稀疏嵌入作为冷启动场景的备选。

---

## open_questions

1. UniNote 的对比 SFT + RL 排序精炼两阶段范式，在中文美妆电商（本单元 8 产品场景）的 I2I 检索上，RL 精炼阶段的 reward 设计应如何适配营销 KPI（CTR/转化率而非纯检索召回）？
2. AlphaWiSE 的权重插值方法假设两个冻结 checkpoint 可线性组合--营销场景中客户行为分布持续漂移（季节性/促销期），这一线性组合假设是否成立？
3. MMRM 的多路复用表示（MLLM + 协作信号）在中小企业（非京东规模）是否可行，还是协作信号的获取成本使其仅适用于头部平台？
4. 稀疏嵌入在冷启动场景优于密集向量，但本单元的热启动场景（8 个已知客户 × 8 个已知产品）是否会出现稀疏劣势--稀疏/密集的 crossover 点在哪？

---

## methodological_critique

MMRM 和 UniNote 均为工业部署论文（京东/小红书），其"显著性能提升"声明依赖内部 A/B 测试数据，未开源完整训练细节和数据集--学术复现几乎不可能，博后读者应将其视为"工业证据"而非"科学验证"。AlphaWiSE 标注 unverified，且其 exemplar memory 假设在营销场景（客户行为持续漂移、非平稳分布）下的有效性未讨论；权重插值的标量系数拟合可能在小样本（本单元 8 客户）上过拟合。Meehan & Pauwels 的稀疏表示论文虽在四个数据集验证，但均偏英文推荐基准，中文营销场景（短文本/歧义词如"精华"=护肤品还是食品）的稀疏优势未经验证；其"存储成本更低"的声明需警惕--稀疏表示的索引开销在亿级 SKU 上可能反超密集向量。整体而言，四篇论文的工业部署规模（京东数百万 DAU/小红书亿级 I2I）远超本单元的教学场景（8 客户 × 8 产品），直接迁移需谨慎评估规模差异带来的外部效度损失。

---

*本文件由 v9.0 学术前沿注入层生成。所有论文链接来自 `_frontier_corpus/skill-1-representation.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证）。*
