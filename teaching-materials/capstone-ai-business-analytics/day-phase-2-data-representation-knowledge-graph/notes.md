# Capstone · Phase 2：数据表示与知识图谱 · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · Capstone AI和商业分析项目 · Phase 2
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：3-4h 讲义 + 4-5h 上机练习
> **核心命题**：如何将分散在CRM/电商/客服系统中的客户、产品、内容数据转化为统一的向量表示+知识图谱，为Phase 3的营销Agent提供结构化的知识基础？
> **v5.0 升级点**：① 整合技能1(表示工程Day1-3)+技能0(数据处理) ② 真实库上机（sentence-transformers + networkx + pandas） ③ TODO填空式起始笔记本 ④ Notebook化 ⑤ 深链阅读 ⑥ 2026前沿（GraphRAG + 表示工程 + 天道推演×知识图谱推演）

---

## 学习目标（学完你能做到）

1. 能设计企业营销知识图谱本体（Customer/Product/Content/Campaign/Channel/Metric六类实体+八类关系），并说明为什么向量表示无法替代关系推理——"买了跑鞋的客户还买什么"需要沿关系链做多跳推理，而非语义相似度匹配
2. 能用 **sentence-transformers**（all-MiniLM-L6-v2，384维）将客户/产品文本数据编码为统一向量表示，用余弦相似度实现语义检索，并用 **pandas** 做数据预处理与特征工程
3. 能用 **networkx** 构建营销知识图谱（MultiDiGraph，产品-品牌-品类-客户-评论-活动-渠道），执行图查询（最短路径/邻居/社区发现/中心性分析），并理解图结构对营销推理的增量价值
4. 能设计并实现 **GraphRAG混合检索**（向量检索+图谱多跳检索），对比传统向量RAG在多跳营销问答上的效果差异，理解GraphRAG的核心创新（实体关系抽取+社区检测+多策略检索）
5. 能将Phase 2的数据表示层+知识图谱作为Phase 3 Agent的知识基础设施，用**天道推演**视角预判知识图谱在营销Agent推理链中的角色（知识基础→多跳推理→个性化推荐→因果反馈）

---

## 理论部分：精炼索引（详见独立教材）

> Phase 2 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_Capstone_AI和商业分析项目.md` § Phase 2](../../AI原生化商业博士_独立教材_Capstone_AI和商业分析项目.md)（2.1-2.4节，已包含知识图谱本体设计/Embedding Pipeline/GraphRAG集成/交付物清单）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：Phase 2在Capstone中的位置

| Phase | 核心任务 | 交付物 | 依赖 |
|-------|---------|--------|------|
| Phase 1 | 研究问题定义与文献综述 | 研究问题文档 | - |
| **Phase 2** | **数据表示与知识图谱** | **KG设计+Embedding Pipeline+GraphRAG方案** | **Phase 1** |
| Phase 3 | Agentic系统架构设计 | Agent架构文档 | Phase 2 |
| Phase 4 | 实验设计与因果推断 | 实验方案 | Phase 2-3 |

**核心定位**：Phase 2是Capstone项目的**数据基础设施层**。Phase 1定义了"要回答什么问题"，Phase 2解决"用什么数据结构表示这些问题"。Phase 3的Agent将基于Phase 2的知识图谱和向量表示做推理决策，Phase 4的因果推断将基于Phase 2的数据管道做实验设计。

### 关键回顾 2：企业知识图谱本体设计

独立教材定义的营销领域本体：

```
实体类型（Nodes）：
├─ Customer（客户）: customer_id, demographics, lifecycle_stage, value_segment
├─ Product（产品）: product_id, category, features, price, lifecycle_stage
├─ Content（内容）: content_id, type, topic, channel, performance_metrics
├─ Campaign（营销活动）: campaign_id, objective, budget, timeline, roi
├─ Channel（渠道）: channel_id, type, reach, cost
└─ Metric（指标）: metric_id, type, value, timestamp

关系类型（Edges）：
├─ PURCHASED: Customer -> Product
├─ INTERACTED_WITH: Customer -> Content
├─ CATEGORIZED_AS: Product -> Category
├─ COMPETES_WITH: Product -> Product
├─ PROMOTES: Content -> Product
├─ TARGETS: Campaign -> Customer/Segment
├─ DISTRIBUTES: Channel -> Content
└─ MEASURES: Metric -> Campaign/Product/Content
```

### 关键回顾 3：向量表示 vs 知识图谱

| 维度 | 向量表示（Embedding） | 知识图谱（KG） |
|------|---------------------|---------------|
| 擅长 | 语义相似度匹配 | 关系推理/多跳推理 |
| 表示方式 | 高维稠密向量 | 显式图结构（节点+边） |
| 典型任务 | "找相似产品""找相似客户" | "买X的用户还买什么" |
| 可解释性 | 低（黑盒向量） | 高（路径可追溯） |
| 构建成本 | 低（自动嵌入） | 高（需实体关系抽取） |
| 新增节点 | 需重新编码 | 直接添加节点+边 |

**核心洞察**：向量推荐只能找到"和跑鞋相似的产品"，但知识图谱可以沿关系链推理："跑鞋 -> 属于 -> 运动装备 -> 互补 -> 运动护具 -> 推荐护膝"。GraphRAG将两者融合：向量检索做语义匹配，图谱检索做关系推理。

### 关键回顾 4：GraphRAG（微软2024, arXiv 2404.16130）

| 维度 | 传统RAG（向量检索） | GraphRAG |
|------|-------------------|----------|
| 检索方式 | 语义相似度 | 实体关系图+社区层级摘要 |
| 全局问题 | 无法回答"主要主题是什么" | 通过社区摘要回答全局问题 |
| 关系推理 | 不支持 | 支持（沿图边多跳推理） |
| 搜索模式 | 单一向量搜索 | Global Search+Local Search+DRIFT Search |
| 构建成本 | 低（只需向量化） | 高（需LLM抽取实体关系） |
| 适用场景 | 事实性问答 | 需要推理和综合的复杂问题 |

---

## 上机部分：用 sentence-transformers + networkx + pandas 构建营销数据表示与知识图谱

> 📓 **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO 填空版，你来做）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，做完再看）
> 📊 **真实数据/库**：[`data/README.md`](./data/README.md)（sentence-transformers + networkx + pandas 库说明+真实数据来源）

### 为什么用真实库而非手写数据结构

v4.0 的代码用"手写字典模拟图"和"手写余弦相似度"——手写结构无法执行图算法（最短路径/社区发现/中心性），无法体现知识图谱和向量表示的真正价值。v5.0 改用三大真实库：

- **sentence-transformers**（all-MiniLM-L6-v2，384维）：客户/产品文本向量化，语义检索开箱即用
- **networkx**（Python图计算标准库）：构建/分析营销知识图谱，图算法开箱即用
- **pandas**：数据预处理与特征工程，处理结构化营销数据

> **整合技能0+技能1**：技能0的数据处理（pandas清洗/特征工程）+ 技能1的表示工程（sentence-transformers向量化 + networkx知识图谱）= Phase 2完整数据表示层。

### 营销映射（关键桥接）

本Phase为营销Agent构建**产品/客户知识图谱+向量化表示**，支撑个性化推荐：

| Phase 2能力 | 营销场景 | 实现方式 | Agent用途 |
|------------|---------|---------|----------|
| 数据预处理 | CRM/电商数据清洗与特征工程 | pandas DataFrame | 数据基础 |
| 向量表示 | 客户/产品文本向量化 | sentence-transformers 384维 | 语义检索 |
| 语义检索 | "找相似产品""找相似客户" | 余弦相似度Top-K | 推荐召回 |
| 知识图谱 | 产品-品牌-品类-客户-评论-活动-渠道 | networkx MultiDiGraph | 关系推理 |
| 图查询 | 最短路径/邻居/社区发现/中心性 | networkx 图算法 | 多跳推理 |
| GraphRAG | 混合检索（向量+图谱） | 混合检索策略 | Agent知识检索 |

### 上机任务（6个TODO，见starter.ipynb）

1. **TODO1**：用 pandas 加载和预处理营销数据（客户/产品/交互数据清洗、特征工程）
2. **TODO2**：用 sentence-transformers 将产品/客户文本编码为384维向量，实现语义检索
3. **TODO3**：用 networkx 构建营销知识图谱（六类实体+八类关系，节点+边+属性）
4. **TODO4**：知识图谱查询（最短路径/邻居/社区发现/中心性分析）
5. **TODO5**：GraphRAG混合检索实现（向量检索+图谱多跳检索+结果融合）
6. **TODO6**：GraphRAG vs 传统向量RAG效果对比（多跳问答召回率/准确率）

---

## 2026前沿补充：GraphRAG + 表示工程 + 天道推演×知识图谱

> v5.0 新增前沿点。GraphRAG（微软2024, arXiv 2404.16130）是RAG技术的重大演进，表示工程（Representation Engineering）是可解释AI的前沿方向，天道推演×知识图谱为营销Agent提供推演基础。

**核心技术栈**：
- **GraphRAG**（微软2024）：用LLM从文档中自动抽取实体和关系构建知识图谱，用Leiden算法做社区检测，为每个社区生成摘要，支持Global/Local/DRIFT三种搜索模式。GitHub: microsoft/graphrag
- **表示工程**（Representation Engineering, Zou et al. 2023）：通过读取和操控LLM内部表示来理解和控制模型行为。营销应用：通过分析Agent内部表示理解其推荐决策逻辑，提升可解释性
- **天道推演×知识图谱**：将知识图谱作为天道推演的"因果链骨架"——图谱中的关系边定义了推演的因果路径，节点属性注入初始条件，图算法（最短路径/社区发现）辅助识别推演中的关键节点和路径。营销Agent可以基于KG做多路径推演："如果推荐产品A -> 客户可能购买 -> 触发交叉销售 -> 影响LTV"
- **多Agent仿真**：基于知识图谱的多Agent仿真——多个营销Agent在共享KG上协作推理，每个Agent负责一个营销子目标（获客/留存/转化），通过KG共享知识实现协作

**怎么用**：把企业营销数据（CRM/产品/内容/交互）用sentence-transformers向量化，用networkx构建知识图谱，用GraphRAG的混合检索为营销Agent提供知识基础。Agent可以沿KG关系链做多跳推理回答"竞品A和B的共同弱点是什么""购买产品X的客户通常还会买什么"等关系型问题——这是传统向量RAG做不到的。

**天道推演视角**：Phase 2构建的知识图谱不仅是数据结构，更是天道推演的沙盘基础。图谱中的每条边是一条因果链，每个节点是一个决策变量。营销Agent在KG上做多跳推理，本质上就是在沙盘上推演不同推荐策略的连锁反应。

> 🔗 深入阅读见 [`reading.md`](./reading.md) 的GraphRAG / sentence-transformers / networkx条目。

---

## 与后续Phase的衔接

- **Phase 3**：Agentic系统架构设计——今天的知识图谱+向量表示将成为Agent的知识检索基础设施。Agent的推理链将基于KG的多跳检索，Agent的决策将基于向量表示的语义匹配。GraphRAG的混合检索（向量+图谱）将直接集成到Agent的知识检索模块中。
- **Phase 4**：实验设计与因果推断——Phase 2的数据管道和向量表示将支撑Phase 4的A/B测试和因果推断。知识图谱中的关系边可以作为因果图的先验结构，向量表示可以用于匹配实验组/对照组。
- **天道推演**：Phase 2的KG是天道推演的"因果链骨架"。Phase 3的Agent在KG上做多跳推理，本质上是天道推演的"沙盘模拟"在营销领域的实例化。

---

## 作业与评估

作业、5分制量表、费曼演练、2分钟话术、复盘自诊表——沿用独立教材§Phase 2既有设计。本学习材料包不重复，仅新增上机交付物：

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6个TODO全部填好，能跑通）
- [ ] 一段300字分析：GraphRAG在哪个营销场景下显著优于传统向量RAG？为什么？（提示：多跳关系推理 vs 语义相似度匹配）
- [ ] 知识图谱设计文档（六类实体+八类关系的本体定义，附networkx图结构验证）
- [ ] （可选）用天道推演框架分析：知识图谱中的哪条关系链可以支撑营销Agent的推荐推演？

---

*本讲义由v5.0学习材料包升级生成。理论部分引用独立教材，上机部分用真实库（sentence-transformers + networkx + pandas）+ TODO脚手架。整合技能1(表示工程)+技能0(数据处理)。*
*最后更新：2026-07-24*

---

## 学习科学层 (v6.0)

本单元采用**刻意练习** (Ericsson deliberate practice) / **间隔重复** (FSRS-6, SM-2 spaced retrieval) / **建构对齐** (Biggs ILO↔TLA↔AT constructive alignment) / **牛津tutorial LLM仿真** (Socratic questioning, Hattie四级反馈)。

**mastery 阈值** 与 **Worked-Faded 示例**见 `practice.md` 与 `alignment.md`：
- ILO1（本体设计）：六类实体+八类关系100%齐全，Drill2.Worked->Faded->Independent 三阶段
- ILO2（向量表示）：all-MiniLM-L6-v2 维度=384 + 余弦归一化 + Top-K带分数
- ILO3（图查询）：四类图查询齐全（最短路径+邻居+社区发现+中心性）
- ILO4（GraphRAG）：多跳召回率@5 > 传统向量RAG 至少20%
- ILO5（天道推演）：推演链>=2条因果边标注 + 2分钟话术

**交叉练习 (interleaving)** 促进迁移：S1向量 / S2图谱 / S3 GraphRAG 按 A1B1C1->B2C2A2->C3A3B3 交叉排布，强制每次切换表示空间（稠密向量 -> 显式图 -> 混合）。

**提取练习 (retrieval practice)** 优于重读：tutorial.ipynb cell2 强制 pre-tutorial essay，tutorial 期间不得查阅 notes.md/starter/solution。

**间隔重复卡片 (FSRS-6)**：见 `schedule.json`，6张卡片覆盖向量vs图谱/六类实体八类关系/GraphRAG三模式/all-MiniLM-L6-v2/图查询四类/天道推演×KG，due 间隔 [1,3,8,21,60,180] 天。

**Hattie 四级反馈**：tutorial.ipynb cell5 含 [TASK]/[PROCESS]/[SELF-REG]/[FEED-FORWARD] 四级，避免 Self 级表扬。

**限频**：每单元 tutorial 1次/天，mastery<0.7 间隔24小时重试，防 LLM 依赖。

> "天道推演不是预言，而是通过穷尽可能的未来，来选择最好的现在。" -- v6.0 学习科学层让每一次刻意练习、每一次间隔提取、每一次 Socratic 追问，都是向未来投资。

---

## 研究产出与产业链接层 (v7.0)

本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+arXiv链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。详见 research.md 与 industry.md。
