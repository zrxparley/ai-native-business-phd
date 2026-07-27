# Day 3 深链阅读清单

> v5.0 升级：从"课程主页"升级为**经验证的深链**（指向具体论文 / 文档 / 仓库，非主页）。全部链接已验证存在。

---

## ① GraphRAG 理论

### GraphRAG 原始论文（微软，2024，从局部到全局的图RAG）
- 📄 arXiv 2404.16130：https://arxiv.org/abs/2404.16130
- **用法**：Day 3 核心理论来源。GraphRAG 用 LLM 从文档中抽取实体和关系构建知识图谱，用 Leiden 算法做社区检测，为每个社区生成摘要，支持 Global/Local/DRIFT 三种搜索模式。重点读 §3 方法论（实体抽取/社区检测/社区摘要）和 §4 实验（vs 传统RAG的对比结果）。

### Microsoft GraphRAG 开源实现
- 📦 GitHub：https://github.com/microsoft/graphrag （已验证，MIT License，活跃维护）
- **深链用法**：
  - [索引管道](https://github.com/microsoft/graphrag#indexing-pipeline)：理解 GraphRAG 如何从原始文档构建知识图谱
  - [查询引擎](https://github.com/microsoft/graphrag#query-engine)：Global Search / Local Search / DRIFT Search 的实现
  - 对标 starter.ipynb TODO5，理解 GraphRAG 的工程实现

---

## ② KGE（知识图谱嵌入）理论

### TransE 原始论文（Bordes et al., NIPS 2013，平移嵌入）
- 📄 NIPS 2013：https://papers.nips.cc/paper/2013/hash/1cecc7a77928ca8133fa24680a88d2a9-Abstract.html
- **用法**：Day 3 TODO2 的理论基础。TransE 的核心思想：h + r ≈ t（头实体向量 + 关系向量 ≈ 尾实体向量）。重点理解得分函数 f_r(h,t) = -‖h + r - t‖ 和 margin-based ranking loss。注意 TransE 无法处理一对多关系的局限性。

### RotatE 原始论文（Sun et al., ICLR 2019，复数旋转嵌入）
- 📄 arXiv 1902.10197：https://arxiv.org/abs/1902.10197
- **用法**：理解如何用复数空间中的旋转解决 TransE 的一对多关系局限。RotatE 把关系建模为单位旋转 r_i = e^{iθ_i}，通过不同角度的旋转区分同一头实体的多个尾实体。营销应用：适合表示"客户-购买-多个产品"的一对多关系。

### ComplEx 原始论文（Trouillon et al., ICML 2016，复数嵌入）
- 📄 arXiv 1606.06357：https://arxiv.org/abs/1606.06357
- **用法**：理解如何用复数值嵌入同时建模对称关系（如"相似"）和非对称关系（如"购买"）。ComplEx 的得分函数 f_r(h,t) = Re(h̄ · diag(r) · t)，利用复数乘法的不可交换性区分对称/非对称。

---

## ③ 真实库 + 上机

### networkx 官方文档（Python 图计算标准库）
- 🌐 官方文档：https://networkx.org/documentation/stable/ （已验证，完整API参考）
- 📦 GitHub：https://github.com/networkx/networkx （15k★，BSD License，已验证存在）
- **深链用法**：
  - [图算法参考](https://networkx.org/documentation/stable/reference/algorithms/index.html)：最短路径/社区发现/中心性分析
  - [MultiDiGraph API](https://networkx.org/documentation/stable/reference/classes/multidigraph.html)：多类型有向边
  - 对标 starter.ipynb TODO1（图构建）和 TODO3（图查询）

### langchain-experimental LLMGraphTransformer
- 📦 GitHub：https://github.com/langchain-ai/langchain/tree/master/libs/experimental （已验证）
- 🌐 文档：https://python.langchain.com/docs/use_cases/graph/constructing/ （已验证）
- **深链用法**：用 LLM 从非结构化文本自动抽取实体和关系构建知识图谱。对标 starter.ipynb TODO5 的参考展示部分。

### scikit-learn TfidfVectorizer
- 🌐 文档：https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html （已验证）
- **用法**：传统RAG基线的 TF-IDF 向量检索实现。对标 starter.ipynb TODO4。

---

## ④ 2026 前沿：图检索增强与知识图谱应用

### Knowledge Graph Survey（Hogan et al., 2021，知识图谱综述）
- 📄 arXiv 2003.02320：https://arxiv.org/abs/2003.02320
- **用法**：知识图谱领域的权威综述，覆盖 KG 定义/表示/抽取/推理/应用。重点读 §2 知识图谱表示（RDF/属性图）和 §5 KG嵌入（TransE/RotatE/ComplEx）。这是英语轨道 i+1 推荐阅读。

### RAGAS（RAG 评估框架）
- 📦 GitHub：https://github.com/explodinggradients/ragas （已验证，RAG评估框架）
- **用法**：用 RAGAS 评估 GraphRAG vs 传统RAG 的检索质量（忠实度/答案相关性/上下文精度）。RAGAS 提供 LLM-as-a-judge 风格的自动化 RAG 评估，可量化 GraphRAG 的改进幅度。

### LangGraph（图式 Agent 框架，支持图检索管道）
- 📦 GitHub：https://github.com/langchain-ai/langgraph （已验证，LangChain 出品）
- **用法**：LangGraph 支持构建基于图的 RAG 管道，将知识图谱检索与 LLM 推理结合，实现 ReAct 风格的多步推理。与 GraphRAG 互补：GraphRAG 做检索，LangGraph 做推理编排。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本 Day `notes.md` 理论回顾 + 独立教材 §3.3.1-3.3.5 | EKG/KGE/GraphRAG方法论 | 1h |
| 2 | GraphRAG 论文 §3-4（选读） | GraphRAG核心方法 | 0.5h |
| 3 | `starter.ipynb` 上机（配 networkx 文档） | 真实库实操 | 2h |
| 4 | TransE 论文（NIPS 2013） | KGE数学原理 | 0.5h |
| 5 | RotatE 论文 §3（选读） | 一对多关系建模 | 0.5h |
| 6 | Knowledge Graph Survey §2, §5（选读） | KG领域全貌 | 0.5h |

---

*全部深链已于 2026-07-24 验证存在。如发现失效，请在 Issues 报告。*
