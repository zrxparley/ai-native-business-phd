---
unit: U-Capstone-P2
skill_target: 能用 sentence-transformers + networkx + pandas 构建企业营销知识图谱（六类实体+八类关系）并实现 GraphRAG 混合检索（向量+图谱多跳），在多跳营销问答上对比传统向量 RAG 的召回率差异
---

# 刻意练习 · Capstone Phase 2 · 数据表示与知识图谱

> 基础理论：Ericsson 刻意练习 + MIT OCW CS229 pset0 先测 + Harvard/Stanford Worked-Faded + CS230 渐进交付 + 交叉练习 (Interleaving)。所有 drill 的 feedback_rule 领域特定，引用本单元真实库（sentence-transformers all-MiniLM-L6-v2 / networkx MultiDiGraph / pandas / GraphRAG arXiv 2404.16130）。

---

## 1. Diagnostic 先测（CS229 pset0 式，3 题）

> 探测先验知识缺口。每题独立作答，不查资料。完成后对照 feedback_rule 自评。

### D1. 向量 vs 图谱（先验探测：表示选择）
"找相似产品"用向量余弦相似度即可；但"买跑鞋的客户还买什么"为何必须用知识图谱多跳推理，而非语义相似度 Top-K？

**判定要点**：能否指出 (a) 余弦相似度只看语义相似，不编码显式关系；(b) "还买什么"是沿 PURCHASED/COMPETES_WITH/CATEGORIZED_AS 等边的多跳可达性问题；(c) 向量空间中"跑鞋"与"护膝"语义距离可能远，但图谱中"跑鞋→运动装备→互补→护膝"是2-3跳可达。

### D2. GraphRAG 三模式（先验探测：前沿点）
GraphRAG（微软2024, arXiv 2404.16130）的 Global Search / Local Search / DRIFT Search 各自适合回答哪类营销问题？为什么传统向量 RAG 无法回答"竞品A和B的共同弱点是什么"这种全局问题？

**判定要点**：能否区分 Global=社区摘要回答全局主题、Local=实体邻居回答事实、DRIFT=混合多跳；能否指出传统向量 RAG 检索的是chunk，无法跨文档聚合"共同弱点"这种需要沿 COMPETES_WITH 边双向汇聚的关系型问题。

### D3. 本体设计（先验探测：实体关系建模）
若营销数据里有"客户、产品、内容、活动、渠道、指标"六类实体，请设计至少 4 类关系边，并指出哪条关系边最能支撑"交叉销售推荐"的图算法推理。

**判定要点**：能否给出 PURCHASED / INTERACTED_WITH / CATEGORIZED_AS / COMPETES_WITH / PROMOTES / TARGETS / DISTRIBUTES / MEASURES 中至少4条；能否指出 PURCHASED+COMPETES_WITH+互补关系（隐含 CATEGORIZED_AS 同品类）是交叉销售多跳推理的核心边。

---

## 2. subskills 拆解（3 个子技能）

| ID | 子技能 | 可观察行为 |
|----|--------|-----------|
| S1 | 文本向量化与语义检索 | 用 sentence-transformers all-MiniLM-L6-v2（384维）将客户/产品文本编码为向量，实现余弦相似度 Top-K 语义检索 |
| S2 | 知识图谱构建与图查询 | 用 networkx MultiDiGraph 构建六类实体+八类关系图谱，执行最短路径/邻居/社区发现/中心性分析 |
| S3 | GraphRAG 混合检索与对比 | 实现向量检索+图谱多跳检索的融合，在多跳营销问答上对比传统向量 RAG 的召回率/准确率 |

---

## 3. Drills（>=3 个，Worked-Faded 三阶段）

### Drill 1: 向量表示与语义检索（S1）
- **drill_id**: DRILL-VEC-SEMSEARCH
- **difficulty**: 2
- **reps_required**: 3
- **feedback_rule**: 检查 (a) 模型名是否为 `all-MiniLM-L6-v2`、维度是否为 384；(b) 余弦相似度是否正确归一化（不能用裸 dot product）；(c) Top-K 返回是否带 product_id 与相似度分数。若学生用欧氏距离，提示"营销语义检索标准是余弦相似度，因为文本向量长度差异不代表语义差异"。
- **worked_faded**:
  - **Worked（完整示范）**：给定 3 条产品文本（"轻量跑鞋 透气 减震" / "专业马拉松鞋 碳板" / "休闲运动鞋"），完整演示 `SentenceTransformer('all-MiniLM-L6-v2')` 编码 → cosine_similarity 矩阵 → Top-2 检索，输出 product_id 列表。
  - **Faded（部分填空）**：给定 5 条产品文本，学生填空：模型加载语句、相似度计算语句、Top-K 选取语句（3 处 TODO）。
  - **Independent（独立解）**：给定 10 条客户评论文本，独立实现"找相似评论"语义检索，输出 Top-3 相似评论对。

### Drill 2: 知识图谱构建与图查询（S2）
- **drill_id**: DRILL-KG-NETWORKX
- **difficulty**: 3
- **reps_required**: 3
- **feedback_rule**: 检查 (a) 是否用 `nx.MultiDiGraph()`（不是 Graph/DiGraph，因为营销关系允许多重边，如同一客户多次 PURCHASED 同一产品）；(b) 六类实体节点是否齐全（Customer/Product/Content/Campaign/Channel/Metric）；(c) 八类关系边是否齐全；(d) 图查询是否覆盖最短路径+邻居+社区发现+中心性四类。若学生用 `nx.Graph()`，提示"营销数据有多重边和方向（PURCHASED 有向、COMPETES_WITH 无向），必须用 MultiDiGraph"。
- **worked_faded**:
  - **Worked（完整示范）**：用 3 个产品+2 个客户+1 个品类节点，完整演示 `G.add_node()` / `G.add_edge()` 构图 → `nx.shortest_path()` 查"客户A到产品C的购买路径" → `nx.betweenness_centrality()` 找桥接节点。
  - **Faded（部分填空）**：给定完整 6 类实体数据，学生填空：节点添加循环、边添加循环、社区发现算法调用（3 处 TODO）。
  - **Independent（独立解）**：独立用 networkx 构建 8 类关系完整图谱，执行 `nx.community.louvain_communities()` 或 Leiden 社区发现，输出"哪个品类社区聚合度最高"。

### Drill 3: GraphRAG 混合检索与对比（S3）
- **drill_id**: DRILL-GRAPHRAG-HYBRID
- **difficulty**: 4
- **reps_required**: 2
- **feedback_rule**: 检查 (a) 混合检索是否真正融合两条路径（向量检索 + 图谱多跳），而非只跑一条；(b) 多跳查询是否沿 KG 边走 2-3 跳（如 PURCHASED→COMPETES_WITH→PURCHASED），而非只看 1 跳邻居；(c) 对比实验是否在多跳问题（"买跑鞋的客户还买什么"）和单跳问题（"找相似产品"）上分别跑，并报告召回率差异。若学生只用向量检索冒充 GraphRAG，提示"GraphRAG 的核心创新是实体关系抽取+社区检测+多策略检索（Global/Local/DRIFT），不是单纯向量检索"。
- **worked_faded**:
  - **Worked（完整示范）**：给定"购买跑鞋的客户还买什么"问题，完整演示向量检索（找相似产品）→ 图谱多跳检索（PURCHASED→CATEGORIZED_AS→COMPETES_WITH→PURCHASED 2-3跳）→ 结果融合排序 → 输出推荐列表。
  - **Faded（部分填空）**：给定混合检索框架代码，学生填空：向量检索函数、图谱多跳检索函数、结果融合权重（3 处 TODO）。
  - **Independent（独立解）**：独立设计 5 个多跳营销问题 + 5 个单跳营销问题，分别用传统向量 RAG 和 GraphRAG 检索，报告召回率@5 对比表，写一段300字分析"GraphRAG 在哪类问题显著优于向量 RAG"。

---

## 4. Progressive Project（CS230 式渐进交付）

> 一个贯穿 Phase 2 的项目，分 4 阶段交付，每阶段独立评分。

### Stage 1: Proposal（提案，1页）
- 选定一个真实营销场景（如"某运动品牌电商交叉销售推荐"）
- 定义研究问题：该场景下 GraphRAG 相对传统向量 RAG 在哪类多跳问题上提升最大？
- 列出数据来源（CRM/电商/客服系统）+ 六类实体+八类关系的初步本体
- **交付**：proposal.md（1页）+ 本体草图

### Stage 2: Milestone（中期，向量+图谱就绪）
- 完成 starter.ipynb 的 TODO1-4（pandas 预处理 + sentence-transformers 向量化 + networkx 图谱构建 + 图查询）
- 交付可运行的 milestone.ipynb，输出：(a) 向量Top-K检索demo；(b) 图谱统计（节点数/边数/平均度）；(c) 至少2个图查询结果（最短路径+社区发现）
- **mastery_threshold**: TODO1-4 全部正确，向量维度=384，图谱节点>=6类实体

### Stage 3: Final（最终，GraphRAG混合检索+对比）
- 完成 starter.ipynb 的 TODO5-6（GraphRAG混合检索+对比实验）
- 交付 final.ipynb，输出：(a) GraphRAG 混合检索demo（Global/Local/DRIFT 至少1个）；(b) 多跳问题 vs 单跳问题的召回率对比表；(c) 300字分析"GraphRAG 优势场景"
- **mastery_threshold**: 混合检索真正融合两路；多跳问题召回率@5 > 传统向量 RAG 至少 20%

### Stage 4: Poster（海报，2分钟话术）
- 1页 A4 海报：左=本体图（六类实体+八类关系）、中=GraphRAG 架构图（向量+图谱+融合）、右=对比表（召回率/准确率/可解释性）
- 2分钟口头话术：解释"为什么向量推荐只能找相似，而 GraphRAG 能沿关系链多跳推理"
- **mastery_threshold**: 海报三栏齐全 + 话术能在 2 分钟内向非技术听众讲清 GraphRAG 创新点

---

## 5. Interleaving 交叉排布（A1B1C1...B2C2A2...C3A3B3）

> 不块状练习。3 个子技能（A=S1向量 / B=S2图谱 / C=S3 GraphRAG）按以下顺序交叉，每次只做该子技能的1个 rep，下一轮换子技能。

| 轮次 | 顺序 | 内容 |
|------|------|------|
| 第1轮 | A1 → B1 → C1 | A1=Drill1.Worked / B1=Drill2.Worked / C1=Drill3.Worked |
| 第2轮 | B2 → C2 → A2 | B2=Drill2.Faded / C2=Drill3.Faded / A2=Drill1.Faded |
| 第3轮 | C3 → A3 → B3 | C3=Drill3.Independent / A3=Drill1.Independent / B3=Drill2.Independent |

**交叉理由**：S1（向量）和 S2（图谱）是 GraphRAG（S3）的子模块，块状练习会导致"学完图谱忘了向量"。交叉排布强制每次切换表示空间（稠密向量 → 显式图 → 混合），训练学生在三种表示间灵活切换的迁移能力。

---

## 6. Retry Policy（CS230 式）

- **10 free late days**：整个 Phase 2 共 10 个迟到日，自由分配到 4 个 Stage，不扣分。
- **失败重试不罚分**：任一 Stage 未达 mastery_threshold，可重交，重交通过即满分，不扣分。
- **Drill 重做**：Drill 未达 reps_required，可重做，feedback_rule 每次重新触发。

---

## 7. Weak Loop（连续2次失败触发弱项循环）

> 监测：同一 drill 连续 2 次未达 mastery_threshold。

**触发后**：
1. 回退到上一阶段（如 Drill3 失败 → 回退到 Drill2 的 Faded 阶段重做 1 次）
2. 补充 1 个 Worked Example（教师完整示范该 drill 的一个变体）
3. 重新进入失败 drill 的 Faded 阶段（而非 Independent）
4. 通过后再进入 Independent

**典型场景**：
- Drill3（GraphRAG）连续2次失败 → 多半是 S2 图谱多跳查询基础不牢 → 回退 Drill2.Faded 重做 + 补充 Worked Example（演示 PURCHASED→CATEGORIZED_AS→COMPETES_WITH 2-3跳查询）
- Drill1（向量）连续2次失败 → 多半是余弦相似度归一化或模型加载问题 → 回退到 Worked 阶段重看完整示范

---

## 8. 评估量表（5分制，沿用 v5.0 notes.md）

| 维度 | 1分 | 3分 | 5分 |
|------|-----|-----|-----|
| 向量表示 | 模型加载错误 | 正确加载 all-MiniLM-L6-v2 + 余弦相似度 | 正确+维度校验+Top-K带分数 |
| 知识图谱 | 节点边不全 | 六类实体+八类关系齐全 | 齐全+四类图查询+社区发现 |
| GraphRAG | 只跑向量检索 | 混合检索但未对比 | 混合+对比+多跳优势分析 |
| 天道推演 | 无推演 | 单路径推演 | 多路径推演+因果链标注 |

---

*本 practice.md 基于 Ericsson 刻意练习 + CS229/CS230 渐进交付 + Worked-Faded 三阶段 + Interleaving 交叉练习设计。所有 feedback_rule 领域特定，引用 sentence-transformers / networkx MultiDiGraph / GraphRAG arXiv 2404.16130。*
