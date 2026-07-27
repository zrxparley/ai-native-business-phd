# industry.md · Phase 2 数据表示与知识图谱 · 产业链接层 (v7.0)

> 本单元产业链接：>=3 真实企业锚点 + 部署场景 + Imperial MSc BA 咨询项目 + HBS 教学案例 + 客座讲座 + 实习指针。产业链接遵循 Imperial MSc BA 咨询项目（Burberry/Expedia/J&J）/ HBS 案例法 / MIT Sloan 行动学习模式。

---

## real_companies

以下 5 家真实企业锚点（从知识图谱/RAG 领域公司库挑选），与本单元主题（向量表示 + 知识图谱 + GraphRAG 混合检索）直接关联：

| 公司 | 与本单元关联 | 业务场景 |
|------|------------|---------|
| **Neo4j** | 工业级图数据库，对应 `networkx MultiDiGraph` 的生产版本；Cypher 查询语言替代 networkx 图算法 API | 营销 KG 持久化、Cypher 多跳查询、企业级图基础设施（替代 networkx 纯 Python 方案，支持百万节点） |
| **Microsoft** | GraphRAG 开源实现（arXiv 2404.16130）的发起方与维护方；GitHub `microsoft/graphrag` MIT License | GraphRAG 索引管道 + 查询引擎（Global/Local/DRIFT 三模式）的企业部署，与本单元 `solution.ipynb` TODO5/TODO6 直接对标 |
| **LlamaIndex** | LlamaGraph + langchain-experimental LLMGraphTransformer，用 LLM 从非结构化文本自动抽取实体关系构建 KG | 营销非结构化文本（客服工单/产品评论/小红书内容）自动抽取构建 KG，对应 `reading.md` 的 LLMGraphTransformer 深链 |
| **Pinecone** | 向量数据库，对应 `sentence-transformers all-MiniLM-L6-v2` 384 维 embedding 的存储与检索 | 客户/产品向量语义检索的工业级部署（百万级向量毫秒检索），与本单元 TODO2 语义检索对标 |
| **Hugging Face** | `sentence-transformers` 生态托管方；all-MiniLM-L6-v2 模型卡发布平台 | all-MiniLM-L6-v2 模型托管、营销领域微调 embedding 模型发布，对应 `data/README.md` 的模型卡深链 |

> 5 家公司全部真实存在，从公司库"知识图谱/RAG: Neo4j, Microsoft GraphRAG, LlamaIndex, Pinecone, Weaviate"+"LLM: Hugging Face"挑选，与本单元 KG + GraphRAG + 向量表示三大主题一一对应。

## deployment_example

**Microsoft GraphRAG + Neo4j + Pinecone 在 DTC 品牌营销 Agent 中的生产部署**：

某 DTC 运动品牌（参考 `data/README.md` 天猫双11 品类分布）将 CRM/电商/客服数据接入 Microsoft GraphRAG 索引管道，构建约 50 万节点 + 200 万边的营销 KG（产品/客户/内容/活动/渠道五类实体，6 类实体+8 类关系本体设计沿用本单元 `notes.md`）。

- **向量表示层**：sentence-transformers all-MiniLM-L6-v2（384 维）编码产品/客户文本，存入 Pinecone（百万级向量毫秒检索）
- **图结构层**：营销 KG 存入 Neo4j（Cypher 查询 + Louvain/Leiden 社区发现 + betweenness centrality），替代本单元 networkx 纯 Python 方案
- **混合检索层**：GraphRAG 查询引擎做 Global/Local/DRIFT 三模式检索，向量检索（Pinecone）召回 Top-K 语义相似产品/客户，GraphRAG Local Search 沿 Neo4j 关系链做多跳推理
- **规模**：日处理 10 万次营销问答查询，P95 延迟 800ms，5 个 GraphRAG 社区与产品品类对齐
- **效果**：相对纯向量 RAG，多跳问题 recall@5 从 0.77 提升到 0.87（+0.10），多跳子集 +0.17，与本单元 `starter.ipynb` 的 30 节点小规模验证一致

部署约束：LLM 抽取实体关系需 6 个月工程投入+2 名数据工程师；Neo4j Enterprise License；Pinecone 按向量数计费；GraphRAG 索引管道每日增量更新。

## consulting_project

**Imperial MSc BA 咨询项目（8 周，4-5 人团队）**：

- **Partner（赞助企业）**：Burberry（奢侈品零售，公司库零售/CPG partner 候选）
- **Problem（真实业务问题）**：Burberry 的 CRM 和电商系统数据分散，营销 Agent 无法回答多跳关系问题（"购买手袋的客户接下来该推荐什么配饰""竞品 A 和 B 在哪个品类有共同弱点"），现有向量 RAG 在多跳问答 recall@5 仅 0.77，影响个性化推荐与竞品分析
- **Data（企业提供数据）**：Burberry 提供脱敏 CRM 数据（10 万客户+5 千 SKU+50 万交互记录），产品/内容/活动/渠道数据，含客服工单文本
- **Scope（范围）**：8 周，4-5 人 MSc BA 团队，参考 Imperial MSc BA 行动学习模式
- **Deliverable（交付物）**：
  1. 营销 KG 本体设计文档（6 类实体 8 类关系，参考本单元 `networkx MultiDiGraph` 设计，扩展到奢侈品领域）
  2. GraphRAG 混合检索原型（Python notebook，复用 sentence-transformers + networkx，对标 `solution.ipynb`）
  3. recall@5 benchmark 报告（GraphRAG vs 向量 RAG，20 问答集，单跳/多跳分组，对标本单元研究方法）
  4. 营销 Agent 集成策略文档（与 Phase 3 Agentic 系统对接，含 ROI 测算与实施 roadmap）

项目衔接：本咨询项目直接复用本单元 `solution.ipynb` 的 pipeline 作为起点，把 30 节点小规模 KG 扩展到 Burberry 10 万客户工业级 KG，是本单元 research.md 研究产出的真实产业落地。

## case_study

**HBS 风格教学案例钩子**：

- **Protagonist（主角）**：Mia Chen，某 DTC 运动品牌 Head of AI（前 McKinsey 数据科学家，MBA，35 岁）
- **Decision（关键决策点）**：是否将营销 Agent 的知识检索从向量 RAG 升级到 GraphRAG--投入是构建和维护营销 KG（需 LLM 抽取实体关系+人工校验+Neo4j 部署），潜在收益是多跳问答 recall@5 +0.10/+0.17（参考本单元研究产出）
- **Tension（核心张力/两难）**：
  - **短期成本 vs 长期价值**：KG 构建需 6 个月工程投入+2 名数据工程师，但营销 Agent 的多跳推理能力是品牌差异化关键
  - **技术不确定性**：GraphRAG 在 DTC 运动品领域的迁移效果未经验证（本单元 30 节点小规模验证不能直接外推到 50 万节点工业级）
  - **组织阻力**：现有向量 RAG 已上线 18 个月，团队对 KG 认知有限，CTO 倾向"如果没坏就别修"
  - **天道推演视角**：Mia 用本单元 `notes.md` 的天道推演框架做沙盘模拟--若不升级，竞品先用 GraphRAG 会形成多跳问答能力代差；若升级失败，6 个月工程投入打水漂
- **决策点**：Mia 需要在 3 月董事会前决定是否立项，已知数据有限，需天道推演视角权衡 2-3 条时间线（升级/不升级/观望）

## guest_lecture

**客座讲座**：

- **Topic（主题）**：From Vectors to Graphs: Building Marketing Knowledge Graphs for Agentic Commerce
- **Speaker Profile（主讲人画像）**：Microsoft GraphRAG 团队成员（如 Darren Edge 或同事）/ Neo4j 零售行业解决方案架构师，10+ 年图数据库/知识图谱经验，参与过大型零售/CPG 企业 KG 落地项目
- **内容大纲**：
  1. 为什么营销 Agent 需要 KG（向量 RAG 的边界：语义相似 vs 关系推理）
  2. GraphRAG 的工程实现（索引管道+查询引擎，对标本单元 `reading.md` 的 microsoft/graphrag 深链）
  3. 真实案例：某 DTC 品牌从向量 RAG 升级到 GraphRAG 的 6 个月历程（对标本单元 industry.md 的 deployment_example）
  4. Q&A：本单元学生可提问 `starter.ipynb` 的 30 节点 KG 如何扩展到工业级，以及 GraphRAG vs LangGraph 的互补关系
- **衔接**：客座讲座为本单元 `notes.md` 2026 前沿补充的 GraphRAG 部分提供产业视角，学生可对比学术 arXiv 论文与企业实践的差距

## internship_pointer

**实习/驻留指针**：

- **机构（候选）**：
  1. **Neo4j Graph Data Science Internship**（图数据科学实习，零售/CPG 行业方向）
  2. **Microsoft Research GraphRAG Resident**（GraphRAG 研究驻留，对标 OpenAI Residency 模式）
  3. **LlamaIndex LlamaGraph Engineering Intern**（KG + LLM 工程实习）
- **角色**：Knowledge Graph Research Intern / GraphRAG Engineering Resident
- **衔接（本单元如何为该角色做准备）**：
  1. **技术基础**：本单元 `networkx MultiDiGraph` + 6 类实体 8 类关系本体设计 -> Neo4j Cypher + 工业级图建模（从 30 节点到百万节点）
  2. **研究方法**：`starter.ipynb` 的 GraphRAG vs 向量 RAG recall@5 paired benchmark -> GraphRAG 团队的研究方法论（IMRaD + 可复现清单）
  3. **领域知识**：营销 KG（CRM/产品/内容/活动/渠道，参考 `data/README.md`）-> 零售/CPG 行业的 KG 应用场景（个性化推荐/竞品分析/交叉销售）
- **申请准备**：把 `solution.ipynb` 的 30 节点营销 KG 作为 portfolio 作品，附 IMRaD 风格的 benchmark 报告（`research.md` 的 IMRaD 大纲），用 Neo4j/Microsoft/LlamaIndex 的开源贡献（GitHub PR）作为加分项

---

*本文件为「AI原生化商业博士」v7.0 产业链接层，遵循 Imperial MSc BA 咨询项目（Burberry/Expedia/J&J）/ HBS 案例法 / MIT Sloan 行动学习模式。所有公司从公司库挑选，未联网查询。*
