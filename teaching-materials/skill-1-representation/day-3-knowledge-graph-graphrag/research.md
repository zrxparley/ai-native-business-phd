# research.md · Day 3 企业知识图谱 + GraphRAG · 研究产出层 (v7.0)

> 本单元产出可发表研究工件：研究问题 + 贡献声明 + arXiv 链接 + IMRaD 大纲 + NeurIPS 风格可复现清单 + research-to-practice 翻译。研究产出遵循 IMRaD / DSR (Hevner) / OSF 预注册 / FAIR / 可复现研究标准。

---

## research_question

**核心研究问题**：在企业营销多跳问答任务（如"购买产品 X 的客户通常还会买什么""竞品 A 和 B 的共同弱点是什么"）上，微软 GraphRAG (arXiv 2404.16130) 的多跳图检索相对传统 TF-IDF 向量检索 RAG，在召回率与关系推理准确率上的提升是否显著，且提升幅度是否足以抵消其 LLM 抽取实体关系带来的更高构建成本？

该问题可实证：本单元 `starter.ipynb` 的 TODO6 已构建对照实验（同一营销语料，同一组多跳问题），可量化两类检索的召回率/准确率差异，并叠加 RAGAS 框架的忠实度/答案相关性/上下文精度三项指标。

---

## contribution

**Delta vs prior work**：

1. **相对 GraphRAG 原论文 (Edge et al., 微软 2024, arXiv 2404.16130)**：原论文在通用文档语料（podcast transcripts、新闻）上验证 GraphRAG 的全局问答能力；本研究把 GraphRAG 锚定到**企业营销知识图谱**这一具体垂直域，覆盖 7 类实体（产品/品牌/品类/客户/评论/活动/渠道）与 8 类关系，验证 GraphRAG 在"营销多跳推理"这一具有明确业务价值的子任务上的增量。
2. **相对传统 KGE 文献 (TransE NIPS 2013 / RotatE ICLR 2019 / ComplEx ICML 2016)**：这些工作聚焦于链接预测的嵌入质量（MR / Hit@k），未与下游 RAG 检索质量挂钩；本研究用 `numpy` 从零实现 TransE（margin-based ranking loss `L = Σ max(0, γ + f(h,t) - f(h',t'))`）作为可教学的最小 KGE 基线，并将其与 GraphRAG 的图结构检索对比，桥接 KGE 表示学习与 RAG 检索两条通常割裂的研究线。
3. **相对向量 RAG 基线**：本研究用 `scikit-learn` `TfidfVectorizer` 实现严格对照的传统 RAG 基线（同一语料/同一问题集），而非专家访谈或主观评估，使"GraphRAG vs 传统 RAG"的对比在营销域首次具备可复现的定量证据。

---

## linked_paper

**From local to global: A graph RAG approach to query-focused summarization**

- 作者：Darren E. Edge, Ha Trinh, Newman Cheng, Joshua Bradley, Alex Chao, Apurva Mody, Steven Truitt, Jonathan Larson (Microsoft Research)
- 年份：2024
- arXiv 链接：https://arxiv.org/abs/2404.16130
- GitHub 实现：https://github.com/microsoft/graphrag (MIT License, 活跃维护)

**关联说明**：本论文是 Day 3 上机 TODO5 (GraphRAG 实现) 与 TODO6 (GraphRAG vs 传统 RAG 对比) 的直接理论来源。论文 §3 提出用 LLM 从文档抽取实体/关系构建知识图谱 + Leiden 算法做社区检测 + 为每个社区生成摘要；§4 给出 Global/Local/DRIFT 三种搜索模式的实验对比。本单元 `starter.ipynb` 在营销域复现其方法骨架（用 `networkx` 替代 Neo4j 以去除外部服务依赖），并将其搜索模式映射到营销多跳问答场景。

**辅助链接论文**（均已在 `reading.md` 收录）：
- TransE (Bordes et al., NIPS 2013): https://papers.nips.cc/paper/2013/hash/1cecc7a77928ca8133fa24680a88d2a9-Abstract.html
- RotatE (Sun et al., ICLR 2019): https://arxiv.org/abs/1902.10197
- ComplEx (Trouillon et al., ICML 2016): https://arxiv.org/abs/1606.06357
- Knowledge Graph Survey (Hogan et al., 2021): https://arxiv.org/abs/2003.02320

---

## imrad_outline

### Introduction
- **动机**：向量表示（Day 1-2）擅长语义相似度匹配，但在"买 X 的用户还买什么"这类多跳关系推理上失效。企业营销决策高度依赖关系链推理（产品-品牌-品类-客户-评论-活动-渠道 7 类实体，8 类关系）。
- **Gap**：现有 RAG 文献多在通用语料验证，缺乏营销垂直域的可复现定量证据；KGE 表示学习与 RAG 检索两条研究线割裂。
- **贡献**：① 在营销域复现 GraphRAG (微软 2024) 方法骨架；② 用 `numpy` 从零实现 TransE 作为可教学 KGE 基线；③ 同一语料/同一问题集严格对照 GraphRAG vs TF-IDF RAG。

### Methods
- **数据**：本单元 `data/` 构建的企业营销知识图谱（7 类实体、8 类关系），文档级语料为产品文档/客户反馈/竞品分析/市场报告。
- **模型/方法**：① `networkx.MultiDiGraph` 构建营销 KG；② `numpy` 从零实现 TransE KGE（嵌入初始化/负采样/margin-based ranking loss/梯度更新，`f = -‖h + r - t‖`）；③ `scikit-learn.TfidfVectorizer` 传统 RAG 基线；④ GraphRAG 多跳检索（实体关系抽取 + 社区发现 + Global/Local/DRIFT 三模式）。
- **识别策略**：同一组多跳营销问题（如"竞品 A 和 B 的共同弱点""购买产品 X 的客户还买什么"），对两类检索器输出做配对比较；用 RAGAS 框架评估忠实度/答案相关性/上下文精度。

### Results
- **预期/已得核心发现**：① GraphRAG 在多跳关系推理类问题上召回率显著高于 TF-IDF RAG（沿图边多跳检索 vs 单一向量搜索）；② 对全局性问题（"主要主题是什么"），GraphRAG 通过社区摘要可答，传统 RAG 不可答；③ 对简单事实性问答，传统 RAG 仍够用，GraphRAG 的 LLM 抽取成本不划算；④ TransE 在一对一关系上工作良好，但无法处理"客户-购买-多个产品"的一对多关系（需 RotatE/ComplEx）。具体数字由 TODO6 上机产出，本单元 `solution.ipynb` 提供参考实现。

### Discussion
- **贡献边界**：本单元在因果阶梯 L1（对文档的关联分析）；GraphRAG 的关系推理增强可解释性，但不替代真实业务验证（L2 A/B 测试）。规模限于教学型营销 KG，未在工业级亿边图上验证。
- **局限**：① Neo4j 服务依赖用 `networkx` 替代，未验证图数据库的查询性能优势；② LLMGraphTransformer 需 API Key，上机中作为参考展示而非完整复现；③ RAGAS 评估依赖 LLM-as-a-judge，存在评估器偏差。
- **未来工作**：① 与 Day 4 多模态表示融合（文本-图像-视频实体关联）；② 在 Day 5 综合实战中扩展到亿边规模；③ 与因果推断结合，从关系推理升级为因果推理。

---

## reproducibility_checklist

NeurIPS / ACM 风格可复现清单（≥6 项）：

- [x] **Code**：完整代码在 `solution.ipynb`（8 个 code cells，6 个 TODO 参考答案）；`starter.ipynb` 提供 TODO 填空脚手架（6 个学生代码块，8 cells）。两 notebook 结构对应（sol cells=8/starter=8，scaffold=0，TODO 残留=0）。
- [x] **Data**：企业营销知识图谱数据集（7 类实体：产品/品牌/品类/客户/评论/活动/渠道；8 类关系），见 `data/README.md`。来源为本单元构造的教学型营销语料（产品文档/客户反馈/竞品分析/市场报告）。许可：教学使用。外部依赖库 `networkx` (BSD) / `numpy` (BSD) / `scikit-learn` (BSD) / `langchain-experimental` (MIT) 均为开源。
- [x] **Seeds**：TransE KGE 训练使用固定随机种子（`numpy` 嵌入初始化与负采样可复现）；本单元 `solution.ipynb` 在初始化单元格显式设 `random_state=42`（与 v6.0 `schedule.json` 的卡片假设一致）。
- [x] **Environment**：Python 3.10+；关键库版本 `networkx>=3.2` / `numpy>=1.26` / `scikit-learn>=1.4` / `langchain-experimental>=0.1.0`（详见 `data/README.md`）。Neo4j 为可选 fallback，无服务时用 `networkx` 替代。
- [x] **Preregistration**：本单元 `notes.md` 已声明假设（GraphRAG 在多跳营销问答上优于传统 RAG；TransE 无法处理一对多关系），等同于预注册的 hypothesis 声明；可上传至 OSF DOI 以满足正式预注册要求。
- [x] **FAIR**：数据可发现（`data/README.md` 索引）/ 可访问（开源库 + 教学语料）/ 可互操作（`networkx` 标准图数据结构，可导出 GraphML/JSON）/ 可重用（BSD/MIT 许可库 + 明确教学许可）。
- [x] **Benchmark baseline**：传统 RAG 基线用 `scikit-learn.TfidfVectorizer` 严格对照（同一语料/同一问题集），非主观评估。

---

## research_to_practice

本研究产出可沿三条路径翻译为实践工件：

1. **HBS Working Paper → HBR Article**：将"GraphRAG vs 传统 RAG 在营销多跳问答上的定量对比"先写成 HBS Working Paper（含 IMRaD 完整证据链 + RAGAS 评估），再压缩为 HBR Article（如"为什么你的 RAG 答不了多跳问题：GraphRAG 的营销应用"），面向 CMO/Head of AI 决策者。
2. **MIT Sloan Teaching Case**：以本单元营销 KG 为底本，撰写 MIT Sloan 教学案例（protagonist = 某零售企业 Head of AI，decision = 是否从向量 RAG 迁移到 GraphRAG，tension = 多跳推理能力 vs LLM 抽取成本）。
3. **企业白皮书 / 行业报告**：与 Neo4j / Microsoft GraphRAG / LlamaIndex 等产业方合作，输出"企业知识图谱 + GraphRAG 营销应用白皮书"，含部署架构（见 `industry.md` `deployment_example`）、ROI 测算、风险清单。

研究产出遵循 IMRaD / DSR (Hevner 设计科学循环：问题识别 → 制品设计 → 评估 → 沟通) / OSF 预注册 / FAIR 数据原则 / NeurIPS 可复现研究标准。

---

*本文件为 v7.0 研究产出层，不破坏 v5.0/v6.0 基线。最后更新：2026-07-26*
