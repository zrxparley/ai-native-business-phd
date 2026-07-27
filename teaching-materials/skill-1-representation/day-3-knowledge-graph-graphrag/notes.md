# 技能1 · Day 3：企业知识图谱 + GraphRAG · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 技能1 表示工程与营销智能 · Day 3
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：向量表示擅长"相似度匹配"，但不擅长"关系推理"--知识图谱 + GraphRAG 如何补上这一块？
> **v5.0 升级点**：① 新增真实库上机（networkx + numpy/scikit-learn）② 新增 TODO 填空式起始笔记本 ③ Notebook 化 ④ 深链阅读 ⑤ 2026 前沿（GraphRAG 微软2024 + KGE + LangGraph 图检索增强）

---

## 学习目标（学完你能做到）

1. 能解释企业知识图谱（EKG）的核心要素（实体/关系/属性/本体），并说明为什么向量表示无法替代关系推理--"买了跑鞋的客户还买什么"需要沿关系链做多跳推理，而非语义相似度
2. 能区分三种 KGE 方法（TransE / RotatE / ComplEx）的数学原理和适用场景：TransE 的 h+r≈t 平移模型及其一对多关系局限性、RotatE 的复数空间旋转、ComplEx 的对称/非对称关系建模
3. 能用 **networkx** 构建营销知识图谱（产品-品牌-品类-客户-评论-活动-渠道），执行图查询（最短路径/邻居/社区发现/中心性分析）
4. 能用 **numpy** 从零实现 TransE KGE（初始化嵌入/负采样/margin-based ranking loss/梯度更新），理解 h+r≈t 的训练过程
5. 能实现并对比**传统RAG**（TF-IDF 向量检索）与**GraphRAG**（知识图谱多跳检索）在营销多跳问答上的效果差异，理解 GraphRAG 的核心创新（实体关系抽取 + 社区检测 + 多策略检索）

---

## 理论部分：精炼索引（详见独立教材）

> Day 3 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_技能1_表示工程与营销智能.md` § Day 3](../../AI原生化商业博士_独立教材_技能1_表示工程与营销智能.md)（3.3.1–3.3.5 节，已包含EKG设计/KGE数学原理/GraphRAG对比/营销应用/Neo4j+LangChain代码）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：为什么需要知识图谱

| 维度 | 向量表示（Day 1-2） | 知识图谱（Day 3） |
|------|-------------------|------------------|
| 擅长 | 语义相似度匹配 | 关系推理 / 多跳推理 |
| 表示方式 | 高维稠密向量 | 显式图结构（节点+边） |
| 典型任务 | "找相似产品" | "买X的用户还买什么" |
| 可解释性 | 低（黑盒向量） | 高（路径可追溯） |
| 构建成本 | 低（自动嵌入） | 高（需实体关系抽取） |

**核心洞察**：向量推荐只能找到"和跑鞋相似的产品"，但知识图谱可以沿关系链推理："跑鞋 → 属于 → 运动装备 → 互补 → 运动护具 → 推荐护膝"。这种基于关系的推理是向量空间无法直接实现的。

### 关键回顾 2：KGE 三大方法

| 方法 | 核心思想 | 得分函数 | 适用关系 | 局限性 |
|:----:|---------|---------|---------|--------|
| **TransE** | h + r ≈ t（平移） | f = -‖h + r - t‖ | 一对一 | 无法处理一对多/多对多 |
| **RotatE** | h ∘ r ≈ t（复数旋转） | f = -‖h ∘ r - t‖ | 一对多/多对多 | 实现较复杂 |
| **ComplEx** | Re(h̄ · diag(r) · t) | 复数内积取实部 | 对称+非对称 | 需复数运算 |

**TransE 的 margin-based ranking loss**：L = Σ max(0, γ + f(h,t) - f(h',t'))，其中 (h',r,t') 是负采样生成的错误三元组，γ 是间隔。训练目标是让正确三元组的得分比错误三元组至少高出 γ。

### 关键回顾 3：GraphRAG vs 传统RAG

| 维度 | 传统RAG（向量检索） | GraphRAG（微软2024） |
|------|-------------------|---------------------|
| 检索方式 | 语义相似度 | 实体关系图 + 社区层级摘要 |
| 全局问题 | 无法回答"主要主题是什么" | 通过社区摘要回答全局问题 |
| 关系推理 | 不支持 | 支持（沿图边多跳推理） |
| 搜索模式 | 单一向量搜索 | Global Search + Local Search + DRIFT Search |
| 构建成本 | 低（只需向量化） | 高（需LLM抽取实体关系） |
| 适用场景 | 事实性问答 | 需要推理和综合的复杂问题 |

**GraphRAG 的三种搜索模式**：Global Search（全局推理/社区摘要）、Local Search（实体中心查询/邻居检索）、DRIFT Search（混合/先全局定位再局部精确检索）。

---

## 上机部分：用 networkx + numpy 构建营销知识图谱 + GraphRAG

> 📓 **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO 填空版，你来做）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，gated，做完再看）
> 📊 **真实数据/库**：[`data/README.md`](./data/README.md)（networkx + numpy + scikit-learn + langchain-experimental 库说明）

### 为什么用真实库而非手写图结构

v4.0 的代码用"手写字典模拟图"--手写图无法执行图算法（最短路径/社区发现/中心性），无法体现知识图谱的真正价值。v5.0 改用 **networkx**（Python 图计算标准库）+ **numpy**（TransE KGE 从零实现）+ **scikit-learn**（传统RAG基线）：

- **networkx**：构建/分析知识图谱，图算法（路径/社区/中心性）开箱即用
- **numpy**（教学）/ **torch**（生产）：TransE KGE 从零实现（嵌入初始化/负采样/margin loss/梯度更新），理解 h+r≈t 的训练本质；生产环境可用 torch 加速 GPU 训练
- **scikit-learn** / **sentence-transformers**：TF-IDF 向量检索作为传统RAG基线（教学用 scikit-learn），生产环境可用 sentence-transformers 做语义向量检索
- **langchain-experimental**：LLMGraphTransformer 用 LLM 从文本自动抽取实体关系构建 KG（需 API Key，上机中作为参考展示）

> **Neo4j fallback**：Neo4j 需安装服务（Docker），无服务时用 networkx 替代。上机代码完全基于 networkx，无需外部服务。

### 营销映射（关键桥接）

本 Day 构建一个**企业营销知识图谱**，覆盖产品/品牌/品类/客户/评论/活动/渠道七类实体和八类关系，并用它回答营销多跳问题：

| 知识图谱能力 | 营销场景 | 实现方式 |
|-------------|---------|---------|
| 图构建 | 产品-品牌-品类-客户-评论-活动-渠道 | networkx MultiDiGraph |
| KGE 嵌入 | 学习实体/关系向量，支持链接预测 | numpy TransE |
| 图查询 | 最短路径/邻居/社区发现/中心性 | networkx 图算法 |
| 传统RAG | 基于文本相似度检索营销文档 | scikit-learn TF-IDF |
| GraphRAG | 多跳推理回答"买X的用户还买什么" | networkx 多跳检索 |
| 效果对比 | 多跳问答召回率/准确率 | GraphRAG vs 传统RAG |

### 上机任务（6 个 TODO，见 starter.ipynb）

1. **TODO1**：用 networkx 构建营销知识图谱（产品-属性-用户-评论-品牌-活动-渠道，节点+边）
2. **TODO2**：TransE KGE 实现（numpy，学习实体/关系向量，理解 h+r≈t）
3. **TODO3**：知识图谱查询（最短路径/邻居/社区发现/中心性分析）
4. **TODO4**：传统RAG实现（scikit-learn TF-IDF 向量检索），作为对比基线
5. **TODO5**：GraphRAG实现（networkx 多跳检索 + LLMGraphTransformer 参考展示）
6. **TODO6**：GraphRAG vs 传统RAG 效果对比（多跳问答召回率/准确率）

---

## 2026 前沿补充：GraphRAG + KGE + 图检索增强

> v5.0 新增前沿点。GraphRAG（微软2024, arXiv 2404.16130）是 RAG 技术的重大演进，解决了传统向量检索 RAG 无法回答全局性问题和多跳推理的痛点。

**核心技术栈**：
- **GraphRAG**（微软2024）：用 LLM 从文档中自动抽取实体和关系构建知识图谱，用 Leiden 算法做社区检测，为每个社区生成摘要，支持 Global/Local/DRIFT 三种搜索模式。GitHub: microsoft/graphrag
- **KGE（知识图谱嵌入）**：TransE/RotatE/ComplEx 将实体和关系映射到低维向量空间，支持链接预测（"客户A可能购买产品B"）和关系补全
- **LangGraph + 图检索**：LangChain 生态的 LangGraph 框架支持构建基于图的 RAG 管道，将知识图谱检索与 LLM 推理结合，实现 ReAct 风格的多步推理
- **RAGAS（RAG评估）**：用 RAGAS 框架评估 GraphRAG vs 传统RAG 的检索质量（忠实度/答案相关性/上下文精度）

**怎么用**：把企业营销数据（产品文档/客户反馈/竞品分析/市场报告）用 LLMGraphTransformer 抽取为知识图谱，用 GraphRAG 的多跳检索回答"竞品A和B的共同弱点是什么""购买产品X的客户通常还会买什么"等关系型问题--这是传统向量RAG做不到的。

**注意**：GraphRAG 的构建成本高于传统RAG（需 LLM 抽取实体关系），适合需要推理和综合的复杂问题。对于简单事实性问答，传统RAG仍然够用。对应因果阶梯 L1（对文档的关联分析），GraphRAG 的关系推理增强了可解释性但不能替代真实业务验证（L2 A/B测试）。

> 🔗 深入阅读见 [`reading.md`](./reading.md) 的 GraphRAG / TransE / RotatE 条目。

---

## 与后续 Day 的衔接

- **Day 4**：多模态融合与跨域对齐--今天的知识图谱是跨模态对齐的结构化基础（文本-图像-视频的实体关联）。KGE 的 margin-based 对比学习训练范式与多模态领域的对比学习（CLIP、BLIP）共享相同的数学直觉--都是通过对比正负样本学习嵌入空间。LLaVA 等多模态 LLM 也在探索将知识图谱作为结构化先验注入多模态推理，实现图文对齐 + 关系推理的融合。多模态表示 + 知识图谱的结合是 2026 年表示工程的前沿方向。
- **Day 5**：表示工程综合实战--今天的知识图谱 + GraphRAG 将与多模态表示融合，构建完整的企业营销智能系统

---

## 作业与评估

作业、5 分制量表、费曼演练、2 分钟话术、复盘自诊表--沿用独立教材 § Day 3 既有设计。本学习材料包不重复，仅新增上机交付物：

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6 个 TODO 全部填好，能跑通）
- [ ] 一段 300 字分析：GraphRAG 在哪个营销场景下显著优于传统RAG？为什么？（提示：多跳关系推理 vs 语义相似度匹配）
- [ ] （可选）用 LLMGraphTransformer 从一段真实营销文本抽取实体关系，对比手动构建的 KG 差异

---

*本讲义由 v5.0 学习材料包升级生成。理论部分引用独立教材，上机部分用真实库（networkx + numpy + scikit-learn）+ TODO 脚手架。*
*最后更新：2026-07-24*

---

## 学习科学层 (v6.0)

> v6.0 在 v5.0 基线上加**学习科学层**（4 个新文件 + 本节），不破坏 v5.0。哲学增量：**科学即高效 · 反馈即成长**--用学习科学把"练习"升级为"刻意练习 + 间隔重复 + 建构对齐 + 牛津 tutorial 仿真"。

### 4 个新增文件

1. **`practice.md`** - 刻意练习（Ericsson + MIT 6.5940 Worked-Faded）：`skill_target` + 3 subskills + 3 drills（D1 networkx 图构建 / D2 TransE KGE / D3 GraphRAG 对比），每 drill 含 `difficulty` / `reps_required` / `feedback_rule` / `worked_faded` 三阶段。`interleaving` 采用 A1B1C1...B2C2A2...C3A3B3 交叉排布（Butler 2010 交叉练习证据），非块状。`weak_loop` 连续 2 次失败触发回退+补充 worked example。
2. **`schedule.json`** - 间隔重复（FSRS-6 / SM-2 备份，`request_retention=0.9`）：5 张卡片覆盖 TransE margin loss / GraphRAG 三搜索模式 / KGE 三方法对比 / networkx 图查询 API / GraphRAG vs TF-IDF 召回率差异。每卡 `due=[1,3,8,21,60,180]`，`ef0=2.5`。
3. **`alignment.md`** - 建构对齐（Biggs 1996 Constructive Alignment）：4 行 ILO↔TLA↔AT 矩阵 + `mastery_threshold`（D1≥80% / D2≥70% / D3 能独立解）+ 3 自检问题（Feed Up / Feed Back / Feed Forward）。
4. **`tutorial.ipynb`** - 牛津 Tutorial LLM 仿真（Oxford tutorial + arxiv 2024-2025 Socratic LLM 论文 + Hattie 2007 四级 formative feedback）：persona 严格 Socratic + 禁直接答案 + devil's advocate；5 轮静态 if/else 追问覆盖本体设计 / networkx API / TransE 对称矛盾 / GraphRAG 成本反例 / 反事实；`student_model.json` 跨单元复用；Hattie 四级 `[TASK]` / `[PROCESS]` / `[SELF-REG]` / `[FEED-FORWARD]` 全标（避免 Self 级表扬，Hattie 实证表扬效应量仅 0.14）；限频 1 次/天防依赖。

### 学习科学关键词索引

- **刻意练习 (deliberate practice)**：Ericsson 5 要素 - specific goal / feedback / repetition / difficulty / motivation
- **间隔重复 (spaced retrieval)**：FSRS-6 算法 + SM-2 备份，21 weights，`request_retention=0.9`
- **建构对齐 (constructive alignment)**：Biggs ILO↔TLA↔AT 三者对齐，不经 TLA 能过 AT 即对齐失败
- **牛津 tutorial (Oxford tutorial)**：1对1-3 / 每周 / 强制 / 口头辩护 / Socratic 追问
- **Hattie 四级 formative feedback**：TASK / PROCESS / SELF-REG / FEED-FORWARD，避免 Self 级表扬
- **Worked-Faded 示例**：MIT 6.5940 完整示范 -> 部分填空 -> 独立解 三阶段
- **交叉练习 (interleaving)**：A1B1C1...B2C2A2...C3A3B3 而非块状，Butler 2010 证据
- **mastery threshold**：MIT 6.5940 "至少 4/5 实验提交方可及格"
- **提取练习 (retrieval practice)**：Butler 2010 - 检索练习 68% vs 重学 44%

### 与 v5.0 的关系

- v5.0 的 notes.md / data/README.md / starter.ipynb / solution.ipynb / reading.md **不变**
- v6.0 仅在 starter.ipynb 的 TODO 之上加 drill/feedback/mastery 层
- v5.0 的 7 条验收仍由 `verify_unit.py` 检查；v6.0 的 5 条新标准由 `verify_v6_unit.py` 检查
- 两者全通过 = 该单元 v6.0 收敛（12/12）

### v6.0 学习科学依据

- Ericsson, K. A. (1993). *The Role of Deliberate Practice*. Psychological Review, 100(3).
- Biggs, J. (1996). *Enhancing teaching through constructive alignment*. Higher Education, 32(3).
- Hattie, J. (2007). *The Power of Feedback*. Review of Educational Research, 77(1), 81-112.
- Butler, A. C. (2010). *Repeated testing produces superior transfer of learning*. JEP:HPP.
- FSRS-6: Open Spaced Repetition Scheduler, `request_retention=0.9`, 21 weights.
- arxiv 2409.05511 / 2507.05795 / 2508.21204 - Socratic LLM tutoring 仿真设计

*最后更新：2026-07-25 (v6.0 学习科学层追加)*

---

## 研究产出与产业链接层 (v7.0)

本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+arXiv链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。详见 research.md 与 industry.md。

### v7.0 新增文件

1. **`research.md`** - 研究产出层：6 段领域特定 (research_question 营销多跳问答 GraphRAG vs TF-IDF RAG / contribution 相对 GraphRAG 原论文+TransE+向量RAG基线的 delta / linked_paper arXiv 2404.16130 + TransE/RotatE/ComplEx/KG Survey 辅助 / imrad_outline 引用 starter.ipynb TODO6 与 solution.ipynb 真实方法 / reproducibility_checklist 7 项 NeurIPS 风格 / research_to_practice HBR+MIT Sloan+企业白皮书三路径)。
2. **`industry.md`** - 产业链接层：6 段领域特定 (real_companies Neo4j/Microsoft/LlamaIndex/Pinecone/Weaviate 5 家 / deployment_example 零售企业 GraphRAG+Neo4j 部署 / consulting_project Neo4j 赞助 8 周咨询 / case_study Head of AI 迁移决策 / guest_lecture Microsoft GraphRAG 团队 / internship_pointer Microsoft Research+Neo4j+LlamaIndex 实习指针)。

### v7.0 关键词索引

- **研究产出 / research output**：可发表研究工件，遵循 IMRaD / DSR (Hevner 设计科学循环) / OSF 预注册 / FAIR 数据原则 / NeurIPS 可复现研究标准
- **可复现 / reproducibility**：code (solution.ipynb) + data (营销 KG 7 实体 8 关系) + seeds (random_state=42) + environment (Python 3.10+/networkx/numpy/scikit-learn) + preregistration (notes.md hypothesis 声明) + FAIR (可发现/可访问/可互操作/可重用)
- **linked_paper**：GraphRAG (Edge et al., 微软 2024, arXiv 2404.16130) + TransE (NIPS 2013) + RotatE (arXiv 1902.10197) + ComplEx (arXiv 1606.06357) + KG Survey (arXiv 2003.02320)
- **产业链接 / industry linkage**：Neo4j (图数据库) + Microsoft (GraphRAG 出品方) + LlamaIndex (RAG 框架) + Pinecone/Weaviate (向量数据库)
- **consulting / 咨询**：Imperial MSc BA 风格 8 周咨询项目，partner=Neo4j，problem=多跳问答召回率，deliverable=原型+RAGAS 评估+成本收益模型
- **case study / 案例**：HBS 风格教学案例，protagonist=零售企业 Head of AI，decision=向量 RAG -> GraphRAG 迁移，tension=能力 vs 成本 vs 可解释 vs 团队
- **guest lecture / 客座**：Microsoft GraphRAG 团队 Senior Applied Scientist，主题"From Vector RAG to GraphRAG: Production Lessons"
- **internship / 实习**：Microsoft Research / Neo4j / LlamaIndex 三候选，角色 Research Intern / Open Source Resident
- **deployment / 部署**：零售企业 GraphRAG + Neo4j + Pinecone 混合架构，节点百万/边千万，查询路由策略
- **contribution / 贡献**：营销域复现 GraphRAG + numpy 从零 TransE + 同语料同问题集严格对照

### 与 v5.0/v6.0 的关系

- v5.0 的 notes.md / data/README.md / starter.ipynb / solution.ipynb / reading.md **不变**
- v6.0 的 practice.md / schedule.json / alignment.md / tutorial.ipynb **不变**
- v7.0 仅在 notes.md 末尾追加本节 + 新增 research.md / industry.md 两文件
- v5.0 的 7 条验收仍由 `verify_unit.py` 检查；v6.0 的 5 条新标准由 `verify_v6_unit.py` 检查；v7.0 的 3 条新标准由 `verify_v7_unit.py` 检查
- 三者全通过 = 该单元 v7.0 收敛（15/15）

*最后更新：2026-07-26 (v7.0 研究产出与产业链接层追加)*
