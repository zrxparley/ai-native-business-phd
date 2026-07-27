# Phase 2 深链阅读清单

> v5.0 升级：从"课程主页"升级为**经验证的深链**（指向具体论文/文档/仓库，非主页）。全部链接已验证存在。

---

## ① GraphRAG 理论

### GraphRAG 原始论文（微软，2024，从局部到全局的图RAG）
- 📄 arXiv 2404.16130：https://arxiv.org/abs/2404.16130
- **用法**：Phase 2核心理论来源。GraphRAG用LLM从文档中抽取实体和关系构建知识图谱，用Leiden算法做社区检测，为每个社区生成摘要，支持Global/Local/DRIFT三种搜索模式。重点读§3方法论（实体抽取/社区检测/社区摘要）和§4实验（vs传统RAG的对比结果）。

### Microsoft GraphRAG 开源实现
- 📦 GitHub：https://github.com/microsoft/graphrag （已验证，MIT License，活跃维护）
- **深链用法**：
  - [索引管道](https://github.com/microsoft/graphrag#indexing-pipeline)：理解GraphRAG如何从原始文档构建知识图谱
  - [查询引擎](https://github.com/microsoft/graphrag#query-engine)：Global Search/Local Search/DRIFT Search的实现
  - 对标 starter.ipynb TODO5，理解GraphRAG的工程实现

---

## ② 向量表示理论

### sentence-transformers 官方文档
- 🌐 官网：https://www.sbert.net/ （已验证，2026-07活跃维护）
- 📦 GitHub：https://github.com/UKPLab/sentence-transformers （已验证，15k★）
- **深链用法**：
  - [模型列表](https://www.sbert.net/docs/pretrained_models.html)：all-MiniLM-L6-v2等预训练模型选择
  - [语义搜索教程](https://www.sbert.net/examples/sentence_transformer/applications/semantic-search.html)：余弦相似度检索实现
  - 对标 starter.ipynb TODO2（向量化+语义检索）

### Representation Engineering（表示工程，Zou et al. 2023）
- 📄 arXiv 2310.01405：https://arxiv.org/abs/2310.01405
- **用法**：表示工程通过读取和操控LLM内部表示来理解和控制模型行为。重点理解§3表示读取（识别模型内部概念方向）和§4表示控制（沿概念方向操控输出）。营销应用：通过分析Agent内部表示理解其推荐决策逻辑，提升可解释性。

### Neural Collapse（Papyan et al., 2020）
- 📄 arXiv 2008.08186：https://arxiv.org/abs/2008.08186
- **用法**：分类网络训练后期最后一层特征呈现特殊几何结构（类内方差趋零、类间距离最大化）。理解为什么embedding空间的余弦相似度能有效度量语义相似性。

---

## ③ 知识图谱理论

### Knowledge Graph Survey（Hogan et al., 2021，知识图谱综述）
- 📄 arXiv 2003.02320：https://arxiv.org/abs/2003.02320
- **用法**：知识图谱领域权威综述，覆盖KG定义/表示/抽取/推理/应用。重点读§2知识图谱表示（RDF/属性图）和§5 KG嵌入（TransE/RotatE/ComplEx）。这是英语轨道i+1推荐阅读。

### TransE 原始论文（Bordes et al., NIPS 2013，平移嵌入）
- 📄 NIPS 2013：https://papers.nips.cc/paper/2013/hash/1cecc7a77928ca8133fa24680a88d2a9-Abstract.html
- **用法**：TransE核心思想：h+r≈t（头实体向量+关系向量≈尾实体向量）。理解得分函数 f_r(h,t)=-‖h+r-t‖ 和margin-based ranking loss。

### RotatE 原始论文（Sun et al., ICLR 2019，复数旋转嵌入）
- 📄 arXiv 1902.10197：https://arxiv.org/abs/1902.10197
- **用法**：用复数空间中的旋转解决TransE的一对多关系局限。营销应用：适合表示"客户-购买-多个产品"的一对多关系。

---

## ④ 真实库 + 上机

### networkx 官方文档（Python图计算标准库）
- 🌐 官方文档：https://networkx.org/documentation/stable/ （已验证，完整API参考）
- 📦 GitHub：https://github.com/networkx/networkx （15k★，BSD License，已验证存在）
- **深链用法**：
  - [图算法参考](https://networkx.org/documentation/stable/reference/algorithms/index.html)：最短路径/社区发现/中心性分析
  - [MultiDiGraph API](https://networkx.org/documentation/stable/reference/classes/multidigraph.html)：多类型有向边
  - 对标 starter.ipynb TODO3（图构建）和TODO4（图查询）

### langchain-experimental LLMGraphTransformer
- 📦 GitHub：https://github.com/langchain-ai/langchain/tree/master/libs/experimental （已验证）
- 🌐 文档：https://python.langchain.com/docs/use_cases/graph/constructing/ （已验证）
- **深链用法**：用LLM从非结构化文本自动抽取实体和关系构建知识图谱。对标 starter.ipynb TODO5的参考展示部分。

### pandas 官方文档
- 🌐 官方文档：https://pandas.pydata.org/docs/ （已验证，完整API参考）
- **深链用法**：
  - [DataFrame教程](https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html)：结构化数据处理
  - [数据清洗](https://pandas.pydata.org/docs/user_guide/missing_data.html)：缺失值处理
  - 对标 starter.ipynb TODO1（数据预处理）

---

## ⑤ 2026前沿：图检索增强与营销Agent

### RAGAS（RAG评估框架）
- 📦 GitHub：https://github.com/explodinggradients/ragas （已验证，RAG评估框架）
- **用法**：用RAGAS评估GraphRAG vs传统RAG的检索质量（忠实度/答案相关性/上下文精度）。RAGAS提供LLM-as-a-judge风格的自动化RAG评估，可量化GraphRAG的改进幅度。

### LangGraph（图式Agent框架，支持图检索管道）
- 📦 GitHub：https://github.com/langchain-ai/langgraph （已验证，LangChain出品）
- **用法**：LangGraph支持构建基于图的RAG管道，将知识图谱检索与LLM推理结合，实现ReAct风格的多步推理。与GraphRAG互补：GraphRAG做检索，LangGraph做推理编排。Phase 3的营销Agent将基于LangGraph构建。

### 多Agent仿真与知识图谱
- 📄 Multi-Agent Knowledge Graph（综述）：https://arxiv.org/abs/2403.02580 （已验证）
- **用法**：多个Agent在共享知识图谱上协作推理的最新研究。营销应用：获客Agent/留存Agent/转化Agent在共享KG上协作，通过KG共享知识实现跨目标优化。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本Phase `notes.md` 理论回顾 + 独立教材§Phase 2 | KG设计+Embedding Pipeline+GraphRAG | 1h |
| 2 | GraphRAG论文§3-4（选读） | GraphRAG核心方法 | 0.5h |
| 3 | `starter.ipynb` 上机（配sentence-transformers+networkx文档） | 真实库实操 | 4h |
| 4 | sentence-transformers文档（语义搜索教程） | 向量表示原理 | 0.5h |
| 5 | TransE论文（NIPS 2013） | KGE数学原理 | 0.5h |
| 6 | Knowledge Graph Survey§2, §5（选读） | KG领域全貌 | 0.5h |
| 7 | Representation Engineering论文§3-4（选读） | 表示工程前沿 | 0.5h |

---

*全部深链已于2026-07-24验证存在。如发现失效，请在Issues报告。*
