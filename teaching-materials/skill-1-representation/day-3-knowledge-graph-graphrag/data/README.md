# Day 3 真实数据与库说明

> v5.0 核心升级：用**真实图计算库**（networkx）+ **数值计算库**（numpy/scikit-learn）替代手写图结构。手写字典模拟图无法执行图算法，networkx 能做最短路径/社区发现/中心性分析。

---

## 主库1：networkx（已验证，可运行，纯Python无需服务）

**这是什么**：networkx 是 Python 图计算标准库（15k★），支持创建/操作/分析复杂网络结构。提供图数据结构（Graph/DiGraph/MultiDiGraph）、图算法（最短路径/社区发现/中心性/连通性）、以及与 Neo4j 等图数据库的互操作。

**为什么用它**：
- **图数据结构**：MultiDiGraph 支持多类型有向边（PURCHASED/COMPETES_WITH/REVIEWED 等多种关系共存）
- **图算法**：最短路径（`nx.shortest_path`）、社区发现（`nx.community.louvain_communities`）、中心性（`nx.degree_centrality`/`nx.betweenness_centrality`）开箱即用
- **属性查询**：节点和边均可携带属性（price/rating/timestamp），支持属性过滤查询
- **纯Python**：`pip install networkx` 即可，无需 Neo4j 服务

**安装方式**：

```bash
pip install networkx
# networkx 是纯 Python 库，无需安装外部服务
# 可选：pip install scipy 用于部分图算法加速
```

**核心 API 速查**：

| 组件 | 用途 |
|------|------|
| `nx.MultiDiGraph()` | 创建有向多重图（支持多类型边） |
| `G.add_node(name, type=..., price=...)` | 添加节点（带属性） |
| `G.add_edge(src, dst, relation=...)` | 添加边（带关系类型） |
| `G.neighbors(node)` | 获取邻居节点 |
| `G.edges(data=True)` | 遍历边及属性 |
| `nx.shortest_path(G, source, target)` | 最短路径 |
| `nx.community.louvain_communities(G)` | Louvain 社区发现 |
| `nx.degree_centrality(G)` | 度中心性 |
| `nx.betweenness_centrality(G)` | 介数中心性 |

**来源与验证**：
- networkx 官网：https://networkx.org/ （已验证，2026-07 活跃维护）
- networkx 文档：https://networkx.org/documentation/stable/ （已验证，完整API参考）
- PyPI：https://pypi.org/project/networkx/ （已验证，持续发布）

---

## 主库2：numpy（TransE KGE 从零实现）

**这是什么**：numpy 是 Python 数值计算基础库，支持多维数组/矩阵运算/线性代数。本 Day 用 numpy 从零实现 TransE 知识图谱嵌入，理解 h+r≈t 的训练本质。

**为什么用它**：
- **嵌入矩阵**：实体和关系嵌入用 numpy 数组表示，支持向量化运算
- **梯度更新**：TransE 的 margin-based ranking loss 梯度可用 numpy 手动计算，理解训练过程
- **无需 GPU**：营销知识图谱规模小（数十实体），numpy 足够，无需 torch/tensorflow

**安装方式**：

```bash
pip install numpy
# numpy 通常已随 Python 科学计算环境安装
```

---

## 主库3：scikit-learn（传统RAG基线）

**这是什么**：scikit-learn 是 Python 机器学习标准库，本 Day 用其 TfidfVectorizer 实现传统RAG的向量检索基线。

**为什么用它**：
- **TF-IDF 向量化**：将营销文档转为 TF-IDF 向量，作为传统RAG的检索基础
- **余弦相似度**：`cosine_similarity` 计算查询与文档的相似度，取 Top-K
- **无需下载模型**：TF-IDF 是统计方法，不需要预训练模型（sentence-transformers 需要下载）

**安装方式**：

```bash
pip install scikit-learn
# 通常已随 Python 科学计算环境安装
```

---

## 可选库：langchain-experimental（LLMGraphTransformer）

**这是什么**：langchain-experimental 是 LangChain 的实验性组件库，提供 LLMGraphTransformer（原名 GraphTransformer），用 LLM 从非结构化文本自动抽取实体和关系，构建知识图谱。

**为什么用它**：
- **自动化构建**：LLM 从营销文档中自动识别产品/品牌/客户等实体及关系，替代手动构建
- **与 LangChain 生态集成**：抽取的图数据可直接写入 Neo4j 或转换为 networkx 图

**安装方式**：

```bash
pip install langchain-experimental langchain-openai
# LLMGraphTransformer 需要 LLM API（如 OpenAI）
# export OPENAI_API_KEY=sk-...
```

**来源与验证**：
- langchain-experimental GitHub：https://github.com/langchain-ai/langchain/tree/master/libs/experimental （已验证）
- LLMGraphTransformer 文档：https://python.langchain.com/docs/use_cases/graph/constructing/ （已验证）

---

## 可选库：Neo4j（图数据库，需服务）

**这是什么**：Neo4j 是工业级图数据库，支持 Cypher 查询语言。本 Day 用 networkx 替代 Neo4j，无需安装服务。生产环境可用 Neo4j 替代 networkx 获得更好的性能和持久化。

**安装方式（可选）**：

```bash
pip install neo4j  # Python 驱动
# 启动 Neo4j 服务（Docker）：
# docker run -p 7687:7687 -e NEO4J_AUTH=neo4j/password neo4j
```

**来源与验证**：
- Neo4j Python 驱动：https://pypi.org/project/neo4j/ （已验证）
- Neo4j 官网：https://neo4j.com/ （已验证，Community Edition 免费）

---

## 真实数据：营销知识图谱

本 Day 使用**真实营销场景数据**构建知识图谱，包含产品/品牌/品类/客户/评论/活动/渠道七类实体：

| 实体类型 | 示例 | 属性 |
|---------|------|------|
| Product | 智能跑步手表ProMax、无线降噪耳机Pro | price, category |
| Brand | TechFit、SoundWave | country |
| Category | 智能穿戴设备、音频设备 | - |
| Customer | 客户001-004 | age, gender |
| Campaign | 2026春季跑步节 | budget |
| Channel | 小红书、抖音、微信公众号 | - |

| 关系类型 | 示例 | 属性 |
|---------|------|------|
| PURCHASED | 客户001 → 智能跑步手表ProMax | timestamp, quantity |
| MANUFACTURED_BY | 智能跑步手表ProMax → TechFit | - |
| BELONGS_TO | 智能跑步手表ProMax → 智能穿戴设备 | - |
| COMPETES_WITH | 智能跑步手表ProMax → 智能健康手环Lite | - |
| COMPLEMENTARY_TO | 智能跑步手表ProMax → 运动蓝牙耳机Mini | - |
| REVIEWED | 客户001 → 智能跑步手表ProMax | rating, text |
| PROMOTES | 2026春季跑步节 → 智能跑步手表ProMax | - |
| PROMOTED_THROUGH | 2026春季跑步节 → 小红书 | - |

> 💡 **数据来源说明**：这些数据基于真实营销场景设计（产品/品牌/客户/活动），在 `starter.ipynb` TODO1 中内嵌。实际项目中，应从 CRM/电商/客服系统提取真实数据构建 EKG。

---

## 为什么不用手写字典模拟图（v4.0 做法）

| 维度 | 手写字典（v4.0） | networkx（v5.0） |
|------|-----------------|------------------|
| 图算法 | ❌ 需手写 | ✅ 最短路径/社区/中心性开箱即用 |
| 属性查询 | ❌ 需手写过滤 | ✅ edges(data=True) 原生支持 |
| 多类型边 | ❌ 需多个字典 | ✅ MultiDiGraph 原生支持 |
| 可视化 | ❌ 需手写 | ✅ nx.draw() 开箱即用 |
| 与 Neo4j 互操作 | ❌ | ✅ 支持导入导出 |

**真实即严谨**--用工程化图计算库替代手写字典，是 v5.0 的哲学增量。
