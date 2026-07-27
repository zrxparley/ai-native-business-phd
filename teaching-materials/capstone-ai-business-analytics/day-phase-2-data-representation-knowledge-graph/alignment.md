# 建构对齐 · Capstone Phase 2 · 数据表示与知识图谱

> 理论基础：Biggs 建构对齐（Constructive Alignment, ILO↔TLA↔AT）+ Bloom mastery threshold。每个 AT 必须有明确掌握阈值，每个 TLA 必须能在 starter/drill/tutorial 中找到对应训练活动。

---

## 1. ILO ↔ TLA ↔ AT 对齐矩阵

| ILO（预期学习产出） | TLA（教学学习活动） | AT（评估任务） | mastery_threshold |
|--------------------|--------------------|---------------|-------------------|
| ILO1: 能设计企业营销知识图谱本体（六类实体 Customer/Product/Content/Campaign/Channel/Metric + 八类关系 PURCHASED/INTERACTED_WITH/CATEGORED_AS/COMPETES_WITH/PROMOTES/TARGETS/DISTRIBUTES/MEASURES），并说明向量表示无法替代关系推理 | (a) notes.md §关键回顾2 本体设计精读<br>(b) starter.ipynb TODO3 用 networkx 构建图谱<br>(c) practice.md Drill2.KG-NETWORKX Worked->Faded->Independent<br>(d) tutorial.ipynb cell2 pre-tutorial 本体设计 essay | (a) solution.ipynb TODO3 完整图谱构建<br>(b) practice.md Drill2.Independent 输出8类关系图谱+社区发现<br>(c) Progressive Project Stage1 proposal.md 本体草图 | 六类实体+八类关系齐全100%；能口头解释"向量相似度不编码 PURCHASED 关系链" |
| ILO2: 能用 sentence-transformers（all-MiniLM-L6-v2, 384维）将客户/产品文本编码为统一向量，用余弦相似度实现语义检索，用 pandas 做预处理 | (a) notes.md §关键回顾3 向量vs图谱对比表<br>(b) starter.ipynb TODO1 pandas预处理 + TODO2 sentence-transformers编码<br>(c) practice.md Drill1.VEC-SEMSEARCH 三阶段<br>(d) tutorial.ipynb cell3 Socratic 追问"为何余弦而非欧氏" | (a) solution.ipynb TODO1-2 完整向量管道<br>(b) practice.md Drill1.Independent Top-3相似评论对<br>(c) Progressive Project Stage2 milestone.ipynb 向量Top-K demo | 维度=384校验通过；余弦相似度正确归一化；Top-K带分数输出 |
| ILO3: 能用 networkx MultiDiGraph 构建营销知识图谱，执行图查询（最短路径/邻居/社区发现/中心性） | (a) notes.md §上机任务 TODO3-4<br>(b) starter.ipynb TODO3-4 构图+查询<br>(c) practice.md Drill2 四类图查询 worked<br>(d) tutorial.ipynb cell3 追问"为何 MultiDiGraph 而非 Graph" | (a) solution.ipynb TODO3-4<br>(b) practice.md Drill2.Independent 社区发现输出<br>(c) Stage2 milestone.ipynb 2个图查询结果 | 四类图查询齐全（最短路径+邻居+社区发现+中心性）；节点>=6类实体 |
| ILO4: 能设计并实现 GraphRAG 混合检索（向量+图谱多跳），对比传统向量RAG在多跳营销问答上的效果 | (a) notes.md §关键回顾4 GraphRAG三模式（Global/Local/DRIFT）<br>(b) starter.ipynb TODO5-6 混合检索+对比<br>(c) practice.md Drill3.GRAPHRAG-HYBRID 三阶段<br>(d) tutorial.ipynb cell3 追问"若只用向量冒充GraphRAG会怎样" | (a) solution.ipynb TODO5-6<br>(b) practice.md Drill3.Independent 多跳vs单跳召回率对比表<br>(c) Stage3 final.ipynb 300字分析 | 混合检索真正融合两路；多跳问题召回率@5 > 传统向量RAG 至少20% |
| ILO5: 能用天道推演视角预判知识图谱在营销Agent推理链中的角色（知识基础->多跳推理->个性化推荐->因果反馈） | (a) notes.md §2026前沿 天道推演×知识图谱<br>(b) reading.md GraphRAG/representation engineering 深链<br>(c) tutorial.ipynb cell5 Hattie Feed-Forward 追问推演链<br>(d) practice.md Drill3.Worked 演示 PURCHASED->CATEGORIZED_AS->COMPETES_WITH 推演 | (a) Stage4 poster 推演链标注<br>(b) Stage4 2分钟话术向非技术听众讲清 GraphRAG 创新点<br>(c) tutorial.ipynb cell6 exit artifact 含推演盲点 | 海报三栏齐全+推演链>=2条因果边标注；话术2分钟内讲清"向量相似 vs 关系多跳"差异 |

---

## 2. 三自检问题（Feed Up / Feed Back / Feed Forward）

### Q1. Feed Up（TLA 是否训练 ILO？）
**问**：每个 ILO 是否都有对应的 TLA 活动在 starter.ipynb / practice.md / tutorial.ipynb 中可执行？

**自检**：
- ILO1 -> starter TODO3 + Drill2 + tutorial cell2 ✓（本体设计有训练载体）
- ILO2 -> starter TODO1-2 + Drill1 + tutorial cell3 ✓（向量管道有训练载体）
- ILO3 -> starter TODO3-4 + Drill2 worked ✓（图查询有训练载体）
- ILO4 -> starter TODO5-6 + Drill3 + tutorial cell3 ✓（GraphRAG有训练载体）
- ILO5 -> notes.md前沿 + tutorial cell5 + Stage4 poster ✓（天道推演有训练载体）

**结论**：5 个 ILO 全部有对应 TLA，无悬空 ILO。

### Q2. Feed Back（AT 是否测量 ILO？）
**问**：每个 AT 是否直接测量对应 ILO 的可观察行为，而非泛泛打分？

**自检**：
- ILO1 的 AT = "8类关系齐全100%" -> 直接测量本体设计能力，可观察 ✓
- ILO2 的 AT = "维度=384+余弦归一化+Top-K带分数" -> 直接测量向量管道，可观察 ✓
- ILO3 的 AT = "四类图查询齐全+节点>=6类" -> 直接测量图查询能力，可观察 ✓
- ILO4 的 AT = "多跳召回率@5 > 向量RAG 20%" -> 直接测量GraphRAG效果，可观察 ✓
- ILO5 的 AT = "推演链>=2条因果边+2分钟话术" -> 直接测量推演能力，可观察 ✓

**结论**：5 个 AT 全部有可观察的 mastery_threshold，无主观打分。

### Q3. Feed Forward（不经 TLA 能过 AT 吗？若能=对齐失败）
**问**：是否存在"学生不参加任何 TLA（不做 starter/practice/tutorial），仅靠考前突击就能过 AT"的路径？

**自检**：
- AT1（8类关系图谱）-> 必须做过 Drill2.Worked 才知道为何用 MultiDiGraph 而非 Graph，突击无法补 ✓（无绕过路径）
- AT2（向量Top-K带分数）-> 必须做过 Drill1.Worked 才知道余弦归一化 vs 裸dot product 的差异，突击容易写错 ✓（无绕过路径）
- AT3（四类图查询）-> 必须做过 starter TODO3-4 才知道 networkx API 细节（nx.community.louvain_communities 调用方式），突击查文档耗时大 ✓（无绕过路径）
- AT4（多跳召回率对比）-> 必须做过 Drill3.Faded 才知道混合检索融合权重设计，突击只会单路检索 ✓（无绕过路径）
- AT5（推演链标注）-> 必须读过 notes.md前沿+ tutorial cell5 Hattie Feed-Forward 才能讲清"向量相似 vs 关系多跳"，突击只能背术语 ✓（无绕过路径）

**结论**：5 个 AT 均无法绕过 TLA 通过，对齐成立。若发现某 AT 可绕过，则该 AT 需升级为"必须引用本单元 drill 输出"的硬约束。

---

## 3. Mastery 阈值汇总

| ILO | mastery_threshold | 不达标处理 |
|-----|-------------------|-----------|
| ILO1 | 六类实体+八类关系100%齐全 | weak_loop 回退 Drill2.Faded |
| ILO2 | 维度384+余弦归一化+Top-K带分数 | weak_loop 回退 Drill1.Faded |
| ILO3 | 四类图查询齐全+节点>=6类 | weak_loop 回退 Drill2.Worked |
| ILO4 | 多跳召回率@5 > 向量RAG 20% | weak_loop 回退 Drill3.Faded+Worked Example |
| ILO5 | 推演链>=2条+2分钟话术 | 补充 tutorial cell5 Feed-Forward 重做 |

---

*本 alignment.md 基于 Biggs 建构对齐（ILO↔TLA↔AT 三向对齐）+ Bloom mastery threshold + Hattie 三级反馈（Feed Up/Back/Forward）设计。所有 TLA 引用 starter.ipynb/practice.md/tutorial.ipynb 具体单元，所有 AT 引用 solution.ipynb/Stage 交付物具体输出。*
