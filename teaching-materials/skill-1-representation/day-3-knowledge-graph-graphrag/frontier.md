# frontier.md (v9.0 学术前沿注入层)

> **所属**：skill-1-representation · day-3-knowledge-graph-graphrag
> **版本**：v9.0（学术前沿注入层）
> **本单元前沿课题**：上下文多模态文档检索 + 无推理稀疏检索替代密集 + 命题式符号表示对标 KG 三元组 + 对比学习几何保持对 KGE 嵌入的启示，如何更新本单元所教的企业知识图谱 + TransE/RotatE/ComplEx KGE + GraphRAG vs 传统 RAG 多跳检索。

---

## frontier_topic

本单元教授企业知识图谱（EKG）+ TransE h+r≈t KGE + GraphRAG 三种搜索模式（Global/Local/DRIFT）+ 传统 RAG TF-IDF 基线对比。2025-2026 前沿从四个方向更新这些方法：① CMDR 提出上下文多页文档检索（CMDR-Bench + CMDR-Embed），扩展 GraphRAG 的单页/社区摘要局限；② 无推理稀疏检索在 1870 万文档上 NDCG@5 较密集基线提升 +13.8pp，为"传统 RAG vs GraphRAG"二分法引入第三选项；③ 命题袋框架用原子命题替代 KG 三元组的显式图结构；④ Jacobian 条件数的几何分析为 KGE 嵌入质量提供新度量。

---

## recent_papers

### 1. CMDR: Contextual Multimodal Document Retrieval
- **arXiv**: https://arxiv.org/abs/2607.05927
- **作者**: Ryota Tanaka, Taku Hasegawa
- **年份**: 2026
- **摘要**: 提出多模态文档检索新任务与基准 CMDR-Bench，要求文档上下文建模；以及 CMDR-Embed 框架，联合编码多页以导出上下文页面级嵌入。实验表明显著优于非上下文嵌入。
- **与本单元的关联**: 本单元 notes.md 教 GraphRAG 的 Global Search（社区摘要）处理全局问题；CMDR 提出多页上下文建模作为替代方案--当文档间存在跨页引用（营销多页报告/产品手册）时，社区摘要可能丢失页面级上下文。

### 2. Inference-Free Multimodal Learned Sparse Retrieval for Production-Scale Visual Document Search
- **arXiv**: https://arxiv.org/abs/2605.30917
- **作者**: Gyu-Hwung Cho, Youngjune Lee
- **年份**: 2026
- **摘要**: 提出用于视觉文档检索的无推理稀疏检索器，使用 caption-gated token 监督激活检索相关词汇维度。在 1870 万文档语料上 NDCG@5 较密集基线平均提升 +13.8pp，R@5 翻倍以上。
- **与本单元的关联**: 本单元 solution.ipynb TODO4 用 scikit-learn TfidfVectorizer（char n-gram 2-3）做传统 RAG 基线；此论文的 learned sparse retrieval（caption-gated token）是 TF-IDF 的学习增强版，为"传统 RAG vs GraphRAG"二分法引入"学习稀疏检索"第三选项。

### 3. From Modalities To Propositions: A Language-Centric Framework for Multimodal Intelligence
- **arXiv**: https://arxiv.org/abs/2607.16560
- **作者**: Nadine Chang, Maying Shen
- **年份**: 2026
- **摘要**: 提出以语言表示多模态数据的框架，任何观测（图像/视频/文本）表达为由全局语义码本统一的原子命题袋。支持跨模态理解、检索与组合性，在自动驾驶和开放世界数据上验证。
- **与本单元的关联**: 本单元 notes.md 教 KG 三元组（h, r, t）作为显式关系表示；命题袋框架用原子命题（来自全局语义码本）替代三元组--每个命题是可组合的符号原子，与 KG 实体/关系对标但无需显式图结构。

### 4. Beyond Objective Expressivity: Geometry Preservation in Multimodal Contrastive Learning
- **arXiv**: https://arxiv.org/abs/2607.17673
- **作者**: Tillmann Rheude, Roland Eils
- **年份**: 2026
- **摘要**: 识别编码器 Jacobian 条件数为三模态对比学习的关键因素，条件不良的编码器会退化多模态对齐。提出几何保持编码器（GPE），在多个对比目标和数据集上提升检索与线性探测性能。
- **与本单元的关联**: 本单元 solution.ipynb TODO2 用 numpy 实现 TransE（h+r≈t 是几何平移约束），dim=50，margin=1.0；Jacobian 条件数为 KGE 嵌入质量提供几何度量--TransE 的 h+r≈t 平移假设是否在条件不良的嵌入空间中退化，此论文的几何分析框架可迁移到 KGE。

---

## critical_synthesis

这四篇论文 + 语料库整体揭示了 2025-2026 检索增强与知识表示前沿的三个张力。**共识**：单页/单实体的非上下文嵌入不足以支撑复杂文档检索--CMDR 的多页上下文建模与 GraphRAG 的社区摘要同属"上下文聚合"阵营，但前者保持页面级粒度、后者聚合到社区级，共识是"孤立嵌入不够，需上下文"。**争议**：稀疏 vs 密集 vs 图结构三路径未达成共识。Cho & Lee 的无推理稀疏检索在 1870 万文档上 NDCG@5 较密集基线 +13.8pp（显著优势），但 CMDR-Embed 用密集上下文嵌入也取得"显著优于非上下文"的结果--稀疏优势是否在上下文建模后仍保持未明。命题袋框架（Chang 等）更进一步，用符号命题替代向量/图结构，提供第三条路径。**趋势**：从"单一检索模式"向"多模式融合"迁移--GraphRAG 的 Global/Local/DRIFT 三模式、CMDR 的上下文页面嵌入、稀疏检索的 caption-gated token 都表明单一检索范式不足以覆盖复杂文档查询。**局限**：CMDR-Bench 是新提出基准，其任务设计（多页上下文）可能偏向论文方法，尚未被第三方独立验证；Cho & Lee 的稀疏检索仅在视觉文档（非纯文本营销场景）验证，caption-gated token 依赖 caption 质量在营销多跳问答中可能失效；Chang 等的命题框架在自动驾驶封闭本体上验证，营销场景的长尾实体（数万 SKU）组合性未明；Rheude & Eils 的 GPE 限于三模态对比学习，未覆盖 TransE 的平移几何。整体而言，前沿论文扩展了本单元的"GraphRAG vs 传统 RAG"二分法为"图结构 + 稀疏学习 + 上下文嵌入 + 命题符号"四路径，但 TransE h+r≈t 的基础几何仍是理解这些扩展的前提。

---

## delta_to_unit

1. **上下文多页建模扩展 GraphRAG 社区摘要**：本单元 notes.md "关键回顾 3" 教 GraphRAG 的 Global Search 通过社区摘要回答全局问题；solution.ipynb TODO5 的 `graphrag_query` 函数做多跳检索（co_purchase/brand_products/competitors）。CMDR 2026 提出多页上下文建模（CMDR-Embed 联合编码多页）--本单元的 GraphRAG 检索是单实体/单社区粒度，未覆盖多页文档间的跨页引用上下文，需补充 CMDR-Embed 作为文档级检索的扩展。

2. **学习稀疏检索引入第三选项**：本单元 solution.ipynb TODO4 用 `TfidfVectorizer(analyzer='char', ngram_range=(2, 3))` 做 TF-IDF 基线，TODO6 对比"传统 RAG（TF-IDF）vs GraphRAG"召回率（0% vs 100%）。Cho & Lee 2026 的 caption-gated learned sparse retrieval 在 1870 万文档上 NDCG@5 较密集基线 +13.8pp--本单元的二分法（TF-IDF vs GraphRAG）缺少"学习稀疏检索"第三选项，需补充 caption-gated sparse 作为 TF-IDF 的学习增强版。

3. **命题袋框架对标 KG 三元组**：本单元 notes.md 教 KG 三元组（h, r, t）+ TransE h+r≈t 作为显式关系表示；solution.ipynb TODO1 构建 MultiDiGraph 含 7 类实体 8 类关系。Chang 等 2026 的命题袋框架用原子命题（全局语义码本）替代三元组--无需显式图结构即可支持跨模态理解/检索/组合性。本单元的 KG 构建成本高（需 LLMGraphTransformer 抽取实体关系），命题袋框架可能提供更低成本的符号表示替代。

4. **Jacobian 条件数为 KGE 嵌入质量提供度量**：本单元 solution.ipynb TODO2 的 numpy TransE（dim=50, margin=1.0, 200 epochs）仅用 margin-based ranking loss 训练，未监控嵌入空间几何质量。Rheude & Eils 2026 的 Jacobian 条件数分析为 KGE 提供几何度量--TransE 的 h+r≈t 平移假设在条件不良的嵌入空间中可能退化，本单元应补充条件数监控作为 KGE 训练诊断工具。

---

## open_questions

1. CMDR-Embed 的多页上下文建模在营销多跳问答（本单元 "买X的用户还买什么"）上，相比 GraphRAG 的社区摘要是否有显著优势--还是上下文粒度（页面级 vs 社区级）的取舍依赖查询类型？
2. caption-gated learned sparse retrieval 的 caption 质量依赖在营销场景（产品描述短文本/歧义词如"精华"）下是否稳定，还是 caption 噪声会导致稀疏维度激活错误？
3. 命题袋框架的全局语义码本在营销长尾实体（数万 SKU × 动态价格 × 促销活动）上能否保持组合性，还是码本会爆炸性增长导致检索效率下降？
4. TransE 的 h+r≈t 平移几何在 Jacobian 条件数不良时如何退化--是否需要将 GPE（几何保持编码器）思想迁移到 KGE 训练，用条件数正则化 TransE 嵌入矩阵？

---

## methodological_critique

CMDR 论文提出新基准 CMDR-Bench 并在自身方法上验证"显著优于非上下文嵌入"--这种"自造基准 + 自验证"模式存在 benchmark-gaming 风险，博后读者应警惕任务设计偏向论文方法的可能。Cho & Lee 的稀疏检索论文标注 unverified，且 1870 万文档的实验规模远超学术复现能力；其"R@5 翻倍以上"的声明需警惕--翻倍可能源于密集基线在视觉文档上的低起点（低基数下的倍数易膨胀）。Chang 等的命题框架虽在自动驾驶和开放世界数据验证，但自动驾驶的封闭本体（有限实体类型）与营销场景的长尾性差异巨大--组合性声明在开放营销域可能不成立，且全局语义码本的学习成本未披露。Rheude & Eils 的 GPE 论文虽 verified，但限于三模态对比学习，将 Jacobian 条件数迁移到 TransE KGE 缺乏直接证据--KGE 的平移几何（h+r≈t）与对比学习的对齐几何机制不同，条件数的适用性需独立验证。整体而言，四篇论文的 benchmark 多为英文/视觉/封闭域，博后读者应警惕直接迁移到中文营销知识图谱的外部效度风险。

---

*本文件由 v9.0 学术前沿注入层生成。所有论文链接来自 `_frontier_corpus/skill-1-representation.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证）。*
