# Day 2 LLM 应用工程 · 产业链接层 (v7.0)

> **本文件性质**：产业链接 (industry linkage)，遵循 Imperial MSc BA 咨询项目模式 (Burberry / Expedia / J&J)、HBS 案例法、MIT Sloan 行动学习模式。锚定本单元 `notes.md` 的真实库 (tiktoken + langchain_core + langsmith + numpy)、真实定价 (gpt-4o $2.50/M vs DeepSeek V3 $0.27/M)、真实场景 (营销知识库 RAG)。

---

## real_companies

| 公司 | 与本单元关联 | 业务场景 |
|------|------------|---------|
| LangChain | RAG / Prompt 工程 / 可观测性框架提供方 | `langchain_core` ChatPromptTemplate + `langsmith` @traceable 是本单元 TODO2/TODO3/TODO5 的核心库；LangChain 是 LLM 应用工程的事实标准抽象层，2026 年其 LangGraph / LangSmith 已成为生产标配。 |
| OpenAI | LLM API 与分词器提供方 | `tiktoken` (o200k_base) 是 TODO1 的 token 计数器；gpt-4o 是本单元定价基线 ($2.50/M input)，其 Function Calling / Structured Output 是 TODO2 五种 Prompt 技术的工业实现。 |
| DeepSeek | 低成本推理革命推动方 | DeepSeek V3 (arXiv 2412.19437) 用 MoE 671B/37B 实现 gpt-4o 接近质量, input $0.27/M (10× 成本下降), 是本单元 TODO1 成本对比与 Pareto 前沿研究的扰动变量。 |
| McKinsey | 咨询 partner (AI 转型) | McKinsey 为零售 / CPG 客户设计 LLM 应用工程落地路线 (Prompt -> RAG -> Agent), 是本单元 consulting_project 与 internship_pointer 的潜在 sponsor。 |
| Burberry | 零售 / CPG 咨询项目 partner | Burberry 的营销文案生成场景 (产品描述 / 邮件营销 / 社媒文案) 是 RAG + Prompt 工程的典型应用, 适合 Imperial MSc BA 8 周咨询项目。 |
| Perplexity | AI 原生 RAG 产品 | Perplexity 的核心产品即 RAG (检索 + 生成 + 引用), 是本单元 RAG pipeline 的工业级参照; 其推理成本管理策略直接对应 TODO1 的成本-质量权衡。 |
| Neo4j / Pinecone / Weaviate | RAG 向量库提供方 | 这三家是 RAG 生产部署的向量库标配, 对应 `notes.md` "RAG 质量优化六维度"中的"Embedding 模型"与"检索策略"维度。 |

## deployment_example

**部署场景：Perplexity 风格的营销知识库 RAG Agent 在零售企业的生产部署**

- **规模**：日均 10,000 次营销文案生成请求 (产品描述 / 邮件营销 / 社媒文案), 峰值 100 QPS。
- **架构**：用户提问 -> Query 处理 -> 向量库 (Pinecone, all-MiniLM-L6-v2 embedding) 检索 + BM25 混合检索 -> 重排序 (Cohere Rerank) -> ChatPromptTemplate (System + Human) -> LLM 生成 (DeepSeek V3 主, gpt-4o 兜底) -> langsmith @traceable 全链路追踪 -> RAGAS faithfulness/context_recall 实时评估。
- **约束**：(1) P95 延迟 ≤ 2s (用户体验阈值)；(2) 单次推理成本 ≤ $0.001 (财务约束)；(3) faithfulness ≥ 90% (品牌安全约束, 防幻觉)。
- **效果**：用 DeepSeek V3 替代 gpt-4o 后, 月推理成本从 ~$300 降至 ~$30 (10× 降幅), faithfulness 在营销垂直域保持 ≥90% (因为营销术语集中、词表规模有限, sparse TF-IDF 与 dense retrieval 质量差距小于通用域)。RAGAS 评估集成到 CI/CD, 每次产品文档更新或 Prompt 调整自动跑回归, 质量退化即阻断部署。
- **关键工程决策**：先用 Prompt Engineering (成本极低) 上线, 不够再上 RAG (成本中), 最后才考虑 Fine-tuning (成本高、灵活性低、可能灾难性遗忘)--这是本单元 `notes.md` 的"四种模式决策框架"工程原则在生产中的体现。

## consulting_project

**Imperial MSc BA 风格咨询项目 (8 周, 4-5 人团队)**

- **Partner (赞助企业)**：Burberry (零售 / CPG, 营销文案生成场景)。
- **Problem (真实业务问题)**：Burberry 的全球营销团队日均生成 5,000+ 条产品描述 / 邮件营销 / 社媒文案, 当前用 gpt-4o + 纯 Prompt Engineering, 月推理成本 ~$15,000, 且文案时常出现幻觉 (产品规格错误 / 品牌调性偏离)。需要 (a) 用 RAG 注入产品知识库降低幻觉, (b) 用 RAGAS 量化评估质量, (c) 评估 DeepSeek V3 替代 gpt-4o 的成本-质量 Pareto 改进。
- **Data (企业提供数据)**：(1) 营销知识库语料 (产品文档 / FAQ / 品牌调性指南, 约 10,000 条文档)；(2) 历史营销文案 50,000 条 (含人工标注的"幻觉 / 调性偏离"标签)；(3) gpt-4o 与 DeepSeek V3 的 API 访问 (有 key 时的真实 ablation)。
- **Scope (范围)**：8 周, 4-5 人团队。Week 1-2: 现状诊断与数据探索；Week 3-4: RAG pipeline 原型 (numpy TF-IDF -> all-MiniLM-L6-v2 dense retrieval ablation)；Week 5-6: RAGAS 评估集成与 Pareto 前沿构造；Week 7: 成本-质量策略报告；Week 8: 高管汇报与移交。
- **Deliverable (交付物)**：(1) RAG pipeline 原型 (Python, 可复现, 基于 `solution.ipynb` 扩展)；(2) RAGAS 评估仪表板 (faithfulness / context_recall / answer_relevance 实时监控)；(3) 成本-质量 Pareto 策略报告 (gpt-4o vs DeepSeek V3 决策矩阵)；(4) 8 周咨询报告 + 高管 deck。

## case_study

**HBS 风格教学案例钩子**

- **Protagonist (主角)**：Sarah Chen, Burberry 新任 Head of AI Marketing, 前 Meta Ads 工程师, 上任 90 天。
- **Decision (关键决策点)**：Sarah 需在 30 天内向 CMO 提交"营销 Agent 推理成本优化方案"--在三个选项中抉择：(a) 全量切换 gpt-4o -> DeepSeek V3 (省 90% 成本, 但质量风险未知)；(b) 保留 gpt-4o 但加 RAG 注入产品知识 (成本不变, 但幻觉降低)；(c) 双模型路由 (简单文案用 DeepSeek V3, 高价值文案用 gpt-4o + RAG, 需构建路由分类器)。
- **Tension (核心张力)**：(1) **质量 vs 成本**--CMO 要求"品牌调性零妥协", 但 CFO 要求年降本 50%, 两个约束在 gpt-4o-only 方案下不可同时满足；(2) **速度 vs 可观测性**--竞品已上线 RAG Agent, Sarah 若再用 8 周做 RAGAS 评估可能丢市场, 但若跳过评估直接上线, 幻觉事件可能上社交媒体头条 (品牌风险)；(3) **工程原则 vs 业务紧迫**--`notes.md` 的"先 Prompt Engineering, 不够再 RAG, 最后才 Fine-tuning"原则要求渐进式上线, 但业务方要求"一步到位的 Agent 化"。

教学目标：让学生用本单元的 6-TODO pipeline + RAGAS 评估 + Pareto 前沿方法, 为 Sarah 设计决策矩阵并给出推荐路径。

## guest_lecture

**客座讲座**

- **Topic (主题)**：《从 LangChain 到 LangGraph: LLM 应用工程的生产化之路--RAG / Prompt / Agent 的工程决策框架》
- **Speaker Profile (主讲人画像)**：LangChain Head of Developer Relations (前 McKinsey Digital 高级顾问, 曾主导 3 个财富 500 强企业的 LLM 应用落地项目)。主讲人深度参与 `langchain_core` / `langsmith` 的产品方向, 对 RAG 生产化痛点 (分块策略 / 检索质量 / 评估自动化 / 推理成本) 有第一手经验。
- **讲座大纲**：(1) LLM 应用四种模式决策框架的工业实践；(2) RAG 质量优化六维度的真实案例 (分块 / Embedding / 混合检索 / 重排序 / Prompt / 评估)；(3) LangSmith 可观测性与 RAGAS CI/CD 集成；(4) DeepSeek V3 / MCP 工具协议对 2026 年 LLM 应用架构的影响；(5) Q&A: 学生用本单元 6-TODO pipeline 的实战问题对话主讲人。

## internship_pointer

**实习 / 驻留指针**

- **机构 1：OpenAI Residency (或 Anthropic Residency)**--角色：AI Residency (6-12 个月)。衔接：本单元的 Prompt 工程 / Function Calling / RAG 评估为 Residency 的 LLM 应用研究做直接准备；RAGAS 评估经验是 Residency 项目的核心技能。
- **机构 2：LangChain Capstone Sponsor**--角色：Solutions Engineer Intern (3-6 个月)。衔接：本单元的 `langchain_core` / `langsmith` 实战 + Pareto 前沿研究为 LangChain 企业客户落地项目做直接准备；`solution.ipynb` 可作为申请作品集。
- **机构 3：McKinsey QuantumBlack AI Capstone**--角色：Data Scientist Intern (8-12 周)。衔接：本单元的 consulting_project (Burberry 风格) + 成本-质量策略报告为 McKinsey AI 转型项目做直接准备；HBS 风格 case_study 训练咨询思维。
- **机构 4：DeepSeek / Together AI 推理优化驻留**--角色：Inference Optimization Resident (3-6 个月)。衔接：本单元的 DeepSeek V3 成本扰动 + Pareto 前沿研究为推理成本优化项目做直接准备；`tiktoken` 计数与定价建模是核心技能。
