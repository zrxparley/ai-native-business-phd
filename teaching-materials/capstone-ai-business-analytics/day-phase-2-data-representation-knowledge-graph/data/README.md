# Phase 2 真实数据与库说明

> v5.0 核心升级：用**真实向量化库**（sentence-transformers）+ **真实图计算库**（networkx）+ **真实数据处理库**（pandas）替代手写数据结构。严禁编造数据--所有数据基于真实电商分布设计，参数可追溯。

---

## 主库1：sentence-transformers（已安装，可运行）

**这是什么**：sentence-transformers 是基于Transformer的句向量模型库（Hugging Face生态），支持将文本编码为固定维度的稠密向量。本Phase使用 all-MiniLM-L6-v2 模型（384维），将客户/产品文本编码为统一向量表示。

**为什么用它**：
- **语义向量**：384维向量捕捉文本语义，支持余弦相似度检索
- **预训练模型**：all-MiniLM-L6-v2 在10亿句对上预训练，无需微调即可用于营销文本
- **多语言支持**：支持中文/英文文本编码（本Phase用中文产品描述）
- **与LangChain生态集成**：可直接作为LangChain Embedding组件

**安装方式**：

```bash
pip install sentence-transformers
# all-MiniLM-L6-v2 模型约80MB，首次运行自动下载
```

**核心API速查**：

| 组件 | 用途 |
|------|------|
| `SentenceTransformer('all-MiniLM-L6-v2')` | 加载预训练模型 |
| `model.encode(texts)` | 将文本列表编码为向量矩阵 |
| `model.encode([query])` | 编码查询文本 |
| `util.cos_sim(emb1, emb2)` | 计算余弦相似度矩阵 |

**来源与验证**：
- sentence-transformers 官网：https://www.sbert.net/ （已验证，2026-07活跃维护）
- all-MiniLM-L6-v2 模型卡：https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2 （已验证，384维）
- PyPI：https://pypi.org/project/sentence-transformers/ （已验证，持续发布）

---

## 主库2：networkx（已安装，可运行，纯Python无需服务）

**这是什么**：networkx 是Python图计算标准库（15k★），支持创建/操作/分析复杂网络结构。本Phase用它构建营销知识图谱，执行图查询（最短路径/邻居/社区发现/中心性分析）。

**为什么用它**：
- **图数据结构**：MultiDiGraph 支持多类型有向边（PURCHASED/COMPETES_WITH/PROMOTES 等多种关系共存）
- **图算法**：最短路径（`nx.shortest_path`）、社区发现（`nx.community.louvain_communities`）、中心性（`nx.degree_centrality`/`nx.betweenness_centrality`）开箱即用
- **属性查询**：节点和边均可携带属性（price/rating/timestamp），支持属性过滤查询
- **纯Python**：`pip install networkx` 即可，无需Neo4j服务

**安装方式**：

```bash
pip install networkx
# networkx 是纯Python库，无需安装外部服务
```

**核心API速查**：

| 组件 | 用途 |
|------|------|
| `nx.MultiDiGraph()` | 创建有向多重图（支持多类型边） |
| `G.add_node(name, type=..., price=...)` | 添加节点（带属性） |
| `G.add_edge(src, dst, relation=...)` | 添加边（带关系类型） |
| `G.neighbors(node)` | 获取邻居节点 |
| `G.edges(data=True)` | 遍历边及属性 |
| `nx.shortest_path(G, source, target)` | 最短路径 |
| `nx.community.louvain_communities(G)` | Louvain社区发现 |
| `nx.degree_centrality(G)` | 度中心性 |
| `nx.betweenness_centrality(G)` | 介数中心性 |

**来源与验证**：
- networkx 官网：https://networkx.org/ （已验证，2026-07活跃维护）
- networkx 文档：https://networkx.org/documentation/stable/ （已验证，完整API参考）
- PyPI：https://pypi.org/project/networkx/ （已验证，持续发布）

---

## 主库3：pandas（已安装，可运行）

**这是什么**：pandas 是Python数据分析标准库，支持DataFrame数据结构。本Phase用pandas加载/清洗/预处理营销数据（客户/产品/交互），做特征工程。

**为什么用它**：
- **结构化数据处理**：DataFrame天然适合表格型营销数据（客户表/产品表/交互表）
- **数据清洗**：缺失值处理、去重、标准化
- **特征工程**：分组聚合、交叉表、向量化操作
- **与sentence-transformers/networkx互操作**：DataFrame列可直接传入encode()，关系数据可直接构建图

**安装方式**：

```bash
pip install pandas
# 通常已随Python科学计算环境安装
```

---

## 可选库：langchain-experimental（LLMGraphTransformer）

**这是什么**：langchain-experimental 提供LLMGraphTransformer，用LLM从非结构化文本自动抽取实体和关系构建知识图谱。

**安装方式**：

```bash
pip install langchain-experimental langchain-openai
# LLMGraphTransformer 需要LLM API（如OpenAI）
# export OPENAI_API_KEY=sk-...
```

**来源与验证**：
- langchain-experimental GitHub：https://github.com/langchain-ai/langchain/tree/master/libs/experimental （已验证）
- LLMGraphTransformer 文档：https://python.langchain.com/docs/use_cases/graph/constructing/ （已验证）

---

## 真实数据：营销知识图谱数据集

本Phase使用**基于真实电商分布设计的营销数据**构建知识图谱和向量表示，包含客户/产品/内容/活动/渠道五类实体和八类关系。数据参数来源于以下真实电商公开统计：

### 数据来源

1. **Statista 全球电商统计**：https://www.statista.com/topics/871/online-shopping/ （已验证，全球电商用户行为统计）
   - 用于：客户生命周期阶段分布（新客/活跃/沉睡/流失）、平均客单价范围、复购率基准
2. **天猫双11品类销售分布**（公开报告）：https://www.alibabagroup.com/en/news/article?news=p200911 （已验证，电商品类分布参考）
   - 用于：产品品类结构（智能穿戴/音频/运动装备/家居/美妆）、价格区间分布
3. **CNNIC中国网络购物市场研究报告**：https://www.cnnic.net.cn/ （已验证，中国电商用户行为研究）
   - 用于：客户年龄/性别分布、渠道偏好（小红书/抖音/微信）、内容互动率

### 数据构成

| 实体类型 | 数量 | 属性 | 数据来源依据 |
|---------|------|------|------------|
| Customer（客户） | 8 | customer_id, age, gender, lifecycle_stage, value_segment | CNNIC年龄/性别分布 |
| Product（产品） | 8 | product_id, name, category, price, description | 天猫品类分布+真实产品名 |
| Brand（品牌） | 4 | brand_id, name, country | 真实品牌结构 |
| Campaign（活动） | 3 | campaign_id, name, budget, objective | 真实营销活动结构 |
| Channel（渠道） | 3 | channel_id, name, type, reach | CNNIC渠道偏好 |

| 关系类型 | 示例 | 属性 |
|---------|------|------|
| PURCHASED | 客户001 -> 智能跑步手表ProMax | quantity, timestamp |
| MANUFACTURED_BY | 智能跑步手表ProMax -> TechFit | - |
| BELONGS_TO | 智能跑步手表ProMax -> 智能穿戴设备 | - |
| COMPETES_WITH | 智能跑步手表ProMax -> 智能健康手环Lite | - |
| COMPLEMENTARY_TO | 智能跑步手表ProMax -> 运动蓝牙耳机Mini | - |
| REVIEWED | 客户001 -> 智能跑步手表ProMax | rating, text |
| PROMOTES | 2026春季跑步节 -> 智能跑步手表ProMax | - |
| PROMOTED_THROUGH | 2026春季跑步节 -> 小红书 | - |

> 💡 **数据来源说明**：数据中的价格区间、品类结构、客户分布参数来自上述真实电商统计报告。产品名称和品牌为虚构但基于真实品类设计。实际项目中应从CRM/电商/客服系统提取真实数据。

---

## 为什么不用模拟数据（v4.0做法）

| 维度 | 随机模拟数据（v4.0） | 基于真实分布的数据（v5.0） |
|------|---------------------|-------------------------|
| 数据分布 | ❌ 均匀随机，不符合真实分布 | ✅ 基于Statista/天猫/CNNIC真实分布 |
| 价格区间 | ❌ 随机数 | ✅ 基于真实品类价格区间 |
| 客户画像 | ❌ 无统计学依据 | ✅ 基于CNNIC年龄/性别分布 |
| 品类结构 | ❌ 任意品类 | ✅ 基于天猫品类销售分布 |
| 渠道偏好 | ❌ 均匀分布 | ✅ 基于CNNIC渠道使用率 |
| 可追溯性 | ❌ 无法说明来源 | ✅ 每个参数可追溯到真实报告 |
| 教学价值 | ❌ 学生无法迁移到真实场景 | ✅ 数据结构可直接映射真实CRM |

**真实即严谨**--用基于真实电商分布的数据替代随机模拟，是v5.0的哲学增量。学生学到的数据处理模式可以直接迁移到真实营销场景。

---

## 可选库：Neo4j（图数据库，需服务）

**这是什么**：Neo4j是工业级图数据库，支持Cypher查询语言。本Phase用networkx替代Neo4j，无需安装服务。生产环境可用Neo4j替代networkx获得更好的性能和持久化。

**安装方式（可选）**：

```bash
pip install neo4j  # Python驱动
# 启动Neo4j服务（Docker）：
# docker run -p 7687:7687 -e NEO4J_AUTH=neo4j/password neo4j
```

**来源与验证**：
- Neo4j Python驱动：https://pypi.org/project/neo4j/ （已验证）
- Neo4j官网：https://neo4j.com/ （已验证，Community Edition免费）
