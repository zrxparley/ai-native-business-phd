# industry.md · Day 3 企业知识图谱 + GraphRAG · 产业链接层 (v7.0)

> 本单元产出产业链接：≥3 真实企业锚点 + 部署场景 + Imperial MSc BA 风格咨询项目 + HBS 教学案例 + 客座讲座 + 实习指针。产业链接遵循 Imperial MSc BA 咨询项目 (Burberry/Expedia/J&J) / HBS 案例法 / MIT Sloan 行动学习模式。

---

## real_companies

与本单元主题（企业知识图谱 + GraphRAG + KGE）匹配的真实企业锚点（从公司库挑选）：

| 公司 | 与本单元关联 | 业务场景 |
|------|-------------|---------|
| **Neo4j** | 图数据库行业标准，本单元 `notes.md` 的 Neo4j fallback 选项即指其产品；其原生图查询语言 Cypher 是生产级 KG 部署的首选 | 零售/金融企业的客户-产品-渠道知识图谱存储与多跳查询；Neo4j GraphRAG toolkit 把 GraphRAG 检索与图数据库整合 |
| **Microsoft** | GraphRAG 论文 (arXiv 2404.16130) 与开源实现 (github.com/microsoft/graphrag, MIT License) 的出品方；本单元 TODO5/TODO6 直接复现其方法骨架 | Microsoft 365 Copilot 的企业文档图谱化检索；Azure AI Foundry 提供 GraphRAG 托管服务，企业可一站式部署 Global/Local/DRIFT 三种搜索模式 |
| **LlamaIndex** | LangChain 生态外的另一 RAG 框架主流方，其 `KnowledgeGraphIndex` 与 `GraphRAG` 集成支持从文档自动构建 KG 并做图检索；与 `langchain-experimental.LLMGraphTransformer`（本单元 TODO5 参考展示）形成竞品 | 企业知识库的 GraphRAG 管道搭建；LlamaIndex PropertyGraph + Neo4j 后端是 2026 年生产级 GraphRAG 的常见组合 |
| **Pinecone** | 向量数据库主流方，传统 RAG 的生产级后端；本单元 TODO4 的 TF-IDF 基线在工业上通常替换为 Pinecone 语义向量检索，是 GraphRAG 的对照基线 | 大规模语义检索场景下的传统 RAG 后端；与 GraphRAG 形成成本/能力对照（低构建成本 vs 多跳推理能力） |
| **Weaviate** | 同时支持向量检索与图结构的混合数据库，本单元"GraphRAG vs 传统 RAG"对比在工业上的折中方案 | 企业级混合检索（向量 + 图），适合需要语义相似度 + 关系推理但不愿承担完整 GraphRAG LLM 抽取成本的场景 |

> 5 家企业全部从公司库挑选，全部真实存在，覆盖知识图谱/RAG 全栈：图数据库 (Neo4j) + GraphRAG 出品方 (Microsoft) + RAG 框架 (LlamaIndex) + 向量数据库 (Pinecone/Weaviate)。

---

## deployment_example

**部署场景：某全国性零售企业的"客户-产品-渠道"营销知识图谱 + GraphRAG 智能问答系统**

- **企业画像**：年 GMV 百亿级零售企业，SKU 10万+，会员客户千万级，线上线下全渠道（门店/APP/小程序/第三方平台）。
- **痛点**：传统向量 RAG 能回答"找相似产品"，但答不了"购买产品 X 的客户通常还会买什么""竞品 A 和 B 的共同弱点是什么""某品类 Top 客户的跨品类迁移路径"等多跳关系问题。
- **部署架构**：
  1. **KG 构建**：用 `langchain-experimental.LLMGraphTransformer` 从产品文档/客户反馈/竞品分析/市场报告自动抽取实体关系；存量结构化数据（CRM/订单/库存）用 ETL 直接写入；存储用 **Neo4j**（亿边规模）。
  2. **GraphRAG 索引**：跑 Microsoft GraphRAG 索引管道，Leiden 算法做社区检测，为每个社区生成 LLM 摘要。
  3. **查询路由**：简单事实性问答走 Pinecone 向量 RAG（低成本）；多跳关系/全局性问题走 GraphRAG（Global/Local/DRIFT 三模式按问题类型路由）。
  4. **评估闭环**：RAGAS 框架量化忠实度/答案相关性/上下文精度，A/B 测试验证 GraphRAG vs 向量 RAG 的业务效果（L2 因果验证，非仅 L1 关联）。
- **规模/约束/效果**：KG 节点百万级/边千万级；GraphRAG 构建成本（LLM 抽取）约为向量 RAG 的 5-10 倍，但多跳问答召回率显著提升（具体数字见 `solution.ipynb` TODO6）；Neo4j 查询 P95 < 200ms。
- **关键约束**：① LLM 抽取实体关系的成本与延迟；② KG 增量更新（新品/新客户/新评论的实时入库）；③ 多跳推理的可解释性要求（路径可追溯是 KG 相对向量黑盒的核心优势）。

---

## consulting_project

**Imperial MSc Business Analytics 风格咨询项目**

- **Partner（赞助企业）**：Neo4j（或 Microsoft GraphRAG 团队，或某零售企业如 Burberry/Sephora 的数据团队）
- **Problem（真实业务问题）**：partner 当前用传统向量 RAG 服务营销/客服问答，但多跳关系问题（"购买产品 X 的客户还买什么""竞品共同弱点"）召回率低，希望通过 GraphRAG 提升多跳问答能力，同时控制 LLM 抽取成本。
- **Data（企业提供数据）**：① 脱敏后的产品文档/客户反馈/竞品分析文本（约 10万文档）；② 现有 CRM/订单结构化数据（产品-客户-订单关系）；③ 现有向量 RAG 的问答日志与人工标注答案（用于 RAGAS 评估）。
- **Scope（8 周，4-5 人团队）**：
  - W1-2：用 `LLMGraphTransformer` 从文档抽取实体关系构建 KG（Neo4j 后端），与现有结构化数据对齐。
  - W3-4：跑 Microsoft GraphRAG 索引管道，Leiden 社区检测，生成社区摘要；搭建 Global/Local/DRIFT 三模式查询。
  - W5-6：在同一问题集上对照 GraphRAG vs 现有向量 RAG，用 RAGAS 量化忠实度/答案相关性/上下文精度。
  - W7-8：成本-收益分析（LLM 抽取成本 vs 召回率提升），查询路由策略（简单问题走向量、多跳走 GraphRAG），最终交付。
- **Deliverable（交付物）**：① 可运行原型（Python + Neo4j + GraphRAG）；② RAGAS 评估报告（GraphRAG vs 向量 RAG 定量对比）；③ 成本-收益模型与查询路由策略；④ 8 周咨询报告 + 高管简报。

---

## case_study

**HBS 风格教学案例钩子**

- **Protagonist（主角）**：某全国性零售企业 Head of AI（背景：前大厂资深算法工程师，2 年前入职主导 AI 中台建设）
- **Decision（关键决策点）**：是否将客服/营销问答系统从现有 Pinecone 向量 RAG 迁移到 Microsoft GraphRAG + Neo4j 的图检索架构？投入约 200 万元（LLM 抽取 + Neo4j 部署 + 团队重构），预计 6 个月上线。
- **Tension（核心张力/两难）**：
  - **能力 vs 成本**：GraphRAG 在多跳关系问题上显著优于向量 RAG（沿图边多跳推理 vs 单一向量搜索），但 LLM 抽取实体关系的构建成本是向量 RAG 的 5-10 倍，且增量更新复杂。
  - **可解释 vs 黑盒**：KG 路径可追溯是监管/合规优势（能解释"为什么推荐这个产品"），但向量 RAG 的黑盒相似度匹配在简单问答上够用且成本低。
  - **技术债 vs 竞争压力**：现有向量 RAG 已上线 18 个月，技术债累积；竞争对手已公开宣传"知识图谱驱动的智能客服"，迁移是否窗口期？
  - **团队 vs 路径**：团队擅长向量检索，KG/GraphRAG 需要新技能（Cypher/图算法/Leiden 社区检测），招人还是培训？
- **教学目标**：让学员在真实约束下权衡 GraphRAG vs 向量 RAG，理解技术选型不仅是能力对比，更是成本/可解释性/团队/时机的系统决策。

---

## guest_lecture

**客座讲座**

- **Topic（主题）**：From Vector RAG to GraphRAG: Production Lessons from Deploying Knowledge Graphs at Enterprise Scale（从向量 RAG 到 GraphRAG：企业级知识图谱部署的生产经验）
- **Speaker Profile（主讲人画像）**：Microsoft GraphRAG 团队 Senior Applied Scientist，或 Neo4j Graph Data Science 团队 Head of Solutions。背景：PhD in CS/NLP，主导过 3+ 个 Fortune 500 企业的 GraphRAG/KG 部署项目，在 arXiv 2404.16130 上有贡献。
- **讲座大纲（建议 60 分钟 + 30 分钟 Q&A）**：
  1. GraphRAG 的三个生产真相（vs 论文理想）：增量更新成本、社区摘要质量漂移、查询路由策略
  2. Leiden 社区检测在企业数据上的调参经验（resolution parameter / 层级深度）
  3. Global/Local/DRIFT 三模式的真实业务匹配（哪些问题该走哪条路径）
  4. RAGAS 评估的陷阱：LLM-as-a-judge 的偏差与缓解
  5. 从 L1 关联到 L2 因果：GraphRAG 的关系推理如何与 A/B 测试闭环
- **与本单元衔接**：讲座内容直接对标 `notes.md` 的 GraphRAG 三搜索模式与 `solution.ipynb` TODO6 的对比实验，学员可在讲座前完成上机，带着具体问题参与 Q&A。

---

## internship_pointer

**实习/驻留指针**

- **机构（3 个候选，全部真实）**：
  1. **Microsoft Research** - GraphRAG 团队 Research Intern（Redmond/Remote）：直接参与 arXiv 2404.16130 后续工作，研究 GraphRAG 的增量更新/社区摘要质量/多模态扩展。
  2. **Neo4j** - Graph Data Science Intern（London/San Mateo/Remote）：参与 Neo4j GraphRAG toolkit 与 Graph Data Science 库的开发，接触生产级亿边图。
  3. **LlamaIndex** - Open Source Resident / Applied ML Intern（Remote）：参与 `KnowledgeGraphIndex` 与 `GraphRAG` 集成的开源开发，与 LangChain 生态竞合。
- **角色**：Research Intern / Applied Scientist Intern / Open Source Resident
- **衔接（本单元如何为该角色做准备）**：
  1. **技术上**：本单元 `starter.ipynb` 的 6 个 TODO 覆盖了 GraphRAG 全栈（KG 构建 / TransE KGE / 图查询 / 传统 RAG 基线 / GraphRAG 多跳检索 / 对比评估），是面试时的"上机作品集"。
  2. **理论上**：`reading.md` 的 GraphRAG / TransE / RotatE / ComplEx / KG Survey 5 篇深链论文是实习面试的必备前置阅读。
  3. **研究产出**：本单元 `research.md` 的 IMRaD 大纲与可复现清单可作为实习申请的研究陈述（research statement）草稿。
  4. **产业认知**：本单元 `industry.md` 的部署场景与咨询项目让学员在面试中能谈"生产约束"而非仅"论文方法"。
- **申请建议**：在申请前完成 `solution.ipynb` 全部 TODO + 用 RAGAS 跑一次 GraphRAG vs 向量 RAG 的对比实验，把结果作为 writing sample 附申请。

---

*本文件为 v7.0 产业链接层，不破坏 v5.0/v6.0 基线。最后更新：2026-07-26*
