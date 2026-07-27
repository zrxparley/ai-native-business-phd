# 选修E3 · Day 2：LLM 应用工程 · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 选修E3 LLM导论 · Day 2
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：LLM 应用工程是营销 Agent 的"应用层"--用 Prompt 工程控制输出、用 RAG 注入产品知识、用评估度量质量、用 LangSmith 追踪全链路
> **v5.0 升级点**：① 新增真实库上机（tiktoken + langchain_core + langsmith + numpy RAG）② 新增 TODO 填空式起始笔记本 ③ Notebook 化 ④ 深链阅读 ⑤ 2026 前沿（RAGAS / LangSmith / DeepSeek V3 推理成本 / MCP 工具协议）

---

## 学习目标（学完你能做到）

1. 能阐述 LLM 应用的四种核心模式（Prompt Engineering / RAG / Fine-tuning / Function Calling）的决策框架，并说明"先 Prompt Engineering，不够再 RAG，最后才 Fine-tuning"的工程原则背后的成本与灵活性权衡
2. 能用 **tiktoken**（OpenAI BPE 分词器）精确计算营销文案的 token 数，结合 2026 年主流模型定价（gpt-4o vs DeepSeek V3）计算推理成本，识别成本瓶颈并给出模型选型建议
3. 能用 **langchain_core ChatPromptTemplate**（System + Human 消息模板）+ **StrOutputParser** 构建营销文案生成 Prompt 管道，理解 Few-shot / CoT / Structured Output 五种 Prompt 技术
4. 能用 **numpy TF-IDF + 余弦相似度**实现 RAG 检索（营销知识库召回），理解分块策略、Embedding 模型、混合检索等 RAG 质量优化维度，并能说明 sentence-transformers all-MiniLM-L6-v2 在生产环境的作用
5. 能用 **langsmith @traceable** 装饰器为 LLM 调用配置端到端追踪，用 **RAGAS** 简化实现（faithfulness / context_recall 规则近似）评估 RAG 系统质量，理解 2026 年 LLM 应用可观测性与评估的前沿趋势

---

## 理论部分：精炼索引（详见独立教材）

> Day 2 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_选修E3_LLM导论.md` § Day 2](../../AI原生化商业博士_独立教材_选修E3_LLM导论.md)（一至五节，已包含 LLM 应用四种模式 / Prompt Engineering 进阶 / RAG 系统详解 / Fine-tuning / Function Calling）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：LLM 应用四种模式决策框架

```
问题是否需要最新知识或私有知识？
├── 是 -> 用 RAG
│   └── 还需要特定输出格式/风格？
│       └── 是 -> RAG + Fine-tuning
└── 否 -> 用 Prompt Engineering
    └── 需要调用外部工具/API？
        ├── 是 -> Function Calling
        └── 否 -> 纯 Prompt Engineering
```

**工程原则**：先尝试 Prompt Engineering（成本极低），不够再上 RAG（成本中），最后才考虑 Fine-tuning（成本高、灵活性低、可能灾难性遗忘）。

### 关键回顾 2：五种核心 Prompt 技术

| 技术 | 核心思想 | 适用场景 |
|------|---------|---------|
| Zero-shot | 直接给任务描述 | LLM 已有能力 |
| Few-shot | 提供示例引导格式/风格 | 需要特定输出格式 |
| Chain-of-Thought | 要求展示推理过程 | 复杂推理任务 |
| Self-Consistency | 多次生成取多数 | 减少随机性 |
| Structured Output | JSON/XML 格式输出 | 程序解析 |

### 关键回顾 3：RAG 工作流程

```
用户提问 -> Query 处理 -> 检索(向量库) -> 重排序 -> 生成(LLM+上下文) -> 回答
```

**RAG 质量优化六维度**：分块策略、Embedding 模型、检索策略（向量+BM25 混合）、重排序、Prompt 设计、评估（RAGAS）。

### 关键回顾 4：Function Calling 与 Agent

Function Calling 让 LLM 调用外部工具（API/数据库/计算器），是 Agent 系统的基础。RAG 提供"知识"，Function Calling 提供"操作能力"，两者互补。

### 关键回顾 5：RAGAS 评估框架

RAGAS（Retrieval-Augmented Generation Assessment）是 RAG 专用评估框架，核心指标：
- **Faithfulness（忠实度）**：回答中的信息是否都能在检索上下文中找到（防幻觉）
- **Context Recall（上下文召回率）**：ground truth 中的信息是否被检索到
- **Answer Relevance（回答相关性）**：回答是否切题

---

## 上机部分：用真实库构建 LLM 应用工程

> 📓 **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO 填空版，你来做）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，gated，做完再看）
> 📊 **真实数据/库**：[`data/README.md`](./data/README.md)（tiktoken + langchain_core + langsmith + numpy + 营销知识库语料）

### 为什么用真实库而非手写脚本

v4.0 的代码用"伪代码图解"演示概念。v5.0 改用工业级真实库：

- **tiktoken**（OpenAI，MIT）：精确计算营销文案 token 数，结合模型定价计算推理成本。gpt-4o 用 `o200k_base`，DeepSeek V3 用 `cl100k_base`
- **langchain_core**（LangChain，MIT）：`ChatPromptTemplate` 构建 Prompt 模板，`StrOutputParser` 解析输出。是 LLM 应用工程的标准抽象层
- **langsmith**（LangChain，MIT）：`@traceable` 装饰器为 LLM 调用配置端到端追踪，查看 Prompt/检索/生成的全链路
- **numpy**（BSD）：手写 TF-IDF 向量化 + 余弦相似度做 RAG 检索，理解检索原理而非黑箱调用。生产环境可用 sentence-transformers all-MiniLM-L6-v2 替代
- **RAGAS 简化实现**：用规则近似 faithfulness / context_recall，理解评估指标设计原理

### 营销映射（关键桥接）

LLM 应用工程的核心场景：用 RAG 让 LLM 基于产品知识库生成营销文案，Prompt 工程控制输出格式，评估质量。

| 上机任务 | 营销场景 | 真实库实现 |
|---------|---------|-----------|
| Token 计数 + 推理成本 | 营销文案的中英文 token 消耗差异 + gpt-4o/DeepSeek V3 定价对比 | tiktoken |
| Prompt 模板 | 营销文案生成 Prompt（System + Human 消息） | langchain_core ChatPromptTemplate |
| LLM 追踪 | 营销文案生成全链路追踪 | langsmith @traceable |
| RAG 检索 | 营销知识库召回（产品文档/FAQ） | numpy TF-IDF + 余弦相似度 |
| RAG 生成 | 检索 + Prompt + mock LLM 生成营销文案 | langchain_core + langsmith |
| RAGAS 评估 | faithfulness / context_recall 规则近似 | numpy 规则实现 |

### 上机任务（6 个 TODO，见 starter.ipynb）

1. **TODO1**：用 tiktoken 对营销文案做 tokenization，结合 gpt-4o / DeepSeek V3 定价计算推理成本
2. **TODO2**：用 langchain_core ChatPromptTemplate 构建营销文案生成 Prompt 模板
3. **TODO3**：用 langsmith @traceable 追踪 LLM 调用（无 API key 用 mock LLM）
4. **TODO4**：用 numpy TF-IDF + 余弦相似度实现 RAG 检索（营销知识库召回）
5. **TODO5**：用 RAG 检索 + Prompt 模板 + mock LLM 生成基于知识库的营销文案
6. **TODO6**：用 RAGAS 简化实现评估 RAG 质量（faithfulness / context_recall）

---

## 2026 前沿补充：RAGAS / LangSmith / DeepSeek V3 推理成本 / MCP

> v5.0 新增前沿点。LLM 应用工程在 2026 年的核心趋势是**可观测性 + 评估自动化 + 推理成本优化 + 工具协议标准化**。

### RAGAS：RAG 系统的自动化评估框架

RAGAS（arXiv 2309.15217）是 RAG 专用评估框架，用 LLM-as-Judge 自动评估 faithfulness / context_recall / answer_relevance。2026 年的趋势是将 RAGAS 集成到 CI/CD 流水线，每次 RAG 系统更新（分块策略/Embedding/Prompt 变更）都自动跑评估，质量回归即阻断部署。

**对营销 Agent 的启示**：营销知识库 RAG 上线后，每次更新产品文档或调整检索策略，都用 RAGAS 跑回归评估，确保文案生成质量不退化。

### LangSmith：LLM 应用的可观测性

LangSmith 是 LangChain 出品的 LLM 应用追踪平台，`@traceable` 装饰器记录每次 LLM 调用的 Prompt/响应/token/延迟/工具调用链。2026 年 LLM 应用的可观测性已成为生产标配--没有追踪的 LLM 应用等于黑箱。

### DeepSeek V3：推理成本革命

DeepSeek V3（arXiv 2412.19437）用 MoE 架构（671B 总参数 / 37B 激活参数）实现接近 GPT-4o 的质量，但 API 定价仅 gpt-4o 的 1/10（input $0.27/M vs $2.50/M）。对日均万次营销文案生成请求的场景，月成本从 ~$300（gpt-4o）降到 ~$30（DeepSeek V3），降幅 10 倍。

### MCP（Model Context Protocol）：工具协议标准化

MCP 是 Anthropic 提出的 LLM 工具调用开放协议，标准化 LLM 与外部工具/数据源的连接方式。2026 年 MCP 正在成为 Function Calling 的事实标准，替代各厂商私有的 tool calling 格式。理解 MCP 对构建可移植的营销 Agent 至关重要。

> 🔗 深入阅读见 [`reading.md`](./reading.md) 的 RAGAS / LangSmith / DeepSeek V3 / MCP 条目。

---

## 与后续 Day 的衔接

- **Day 1**（已学）：Transformer 架构与训练流程--今天用真实库构建应用层
- **Day 3**：LLM 评估与部署--今天的 RAGAS 评估概念将延伸到 MMLU/LLM-as-Judge 等完整评估体系

---

## 作业与评估

作业、5 分制量表、费曼演练、2 分钟话术、复盘自诊表--沿用独立教材 § Day 2 既有设计。本学习材料包不重复，仅新增上机交付物：

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6 个 TODO 全部填好，能跑通）
- [ ] 一段 300 字分析：gpt-4o vs DeepSeek V3 在营销文案生成场景的推理成本差异有多大？对模型选型有什么启示？
- [ ] （可选）用 RAGAS 简化实现评估自己构建的 RAG 系统，faithfulness 和 context_recall 各是多少？

---

*本讲义由 v5.0 学习材料包升级生成。理论部分引用独立教材，上机部分用真实库（tiktoken + langchain_core + langsmith + numpy）+ TODO 脚手架。*
*最后更新：2026-07-25*

---

## 学习科学层 (v6.0)

本单元在 v5.0 工程基础上叠加**学习科学层**，采用四种经实证的教学法以提升迁移与保持：

1. **刻意练习 (Ericsson 1993, deliberate practice)**：见 `practice.md`。本单元的核心可观察技能 (skill_target) 拆为 3 子技能 (Prompt+Token 经济 / RAG 检索+追踪 / RAGAS+MCP)，每个子技能配 >=3 个 drill，三阶段 Worked-Faded 示例 (完整示范 -> 部分填空 -> 独立解)。连续 2 次失败触发 weak_loop (弱项循环)，回退上一 drill + 补充 worked example。
2. **间隔重复 (FSRS-6, SM-2 backup)**：见 `schedule.json`。本单元 6 张卡片 (LLM 四模式决策框架 / tiktoken o200k_base vs cl100k_base / 五种 Prompt 技术 / RAG TF-IDF 六维优化 / RAGAS 三指标 / MCP+LangSmith) 按 FSRS-6 间隔 [1,3,8,21,60,180] 天 spaced retrieval，request_retention=0.9。
3. **建构对齐 (Biggs 1996, constructive alignment)**：见 `alignment.md`。ILO↔TLA↔AT 矩阵 5 行对齐，每行附 mastery 阈值 (>=80%)，附 Feed Up / Feed Back / Feed Forward 三级自检。
4. **牛津 Tutorial LLM 仿真 (Oxford tutorial + Socratic + Hattie 四级反馈)**：见 `tutorial.ipynb`。Oxford fellow persona 不直接给答案，4 轮 Socratic 追问 (凭什么/为什么/反例/若前提变/如何)，Hattie 四级形成性反馈 [TASK]/[PROCESS]/[SELF-REG]/[FEED-FORWARD]，限频 1 次/天防依赖。
5. **交叉练习 (interleaving, Rohrer 2012)**：drill 按 A1B1C1...B2C2A2...C3A3B3 交叉排布，反块状，促进 RAG "检索-生成-评估"循环的近迁移与远迁移。
6. **提取练习 (retrieval practice)**：优于重读。tutorial 前强制 mini-essay、Day 3 课前 2 分钟 poster lightning talk、schedule.json 卡片自测均为 retrieval practice 触发器。

> mastery 阈值与 Worked-Faded 示例见 `practice.md` 与 `alignment.md`；间隔重复卡片见 `schedule.json`；Socratic tutorial 见 `tutorial.ipynb`。本层不替换 v5.0 工程内容，仅在其上叠加学习科学增强。

*v6.0 学习科学层追加于 2026-07-26。*

## 研究产出与产业链接层 (v7.0)

本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+arXiv链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。本单元的研究问题锚定 DeepSeek V3 (arXiv 2412.19437, 671B/37B MoE, $0.27/M) 相对 gpt-4o ($2.50/M) 在 RAGAS faithfulness/context_recall 上的质量-成本 Pareto 前沿; linked_paper 用 reading.md 已有的 RAG (arXiv 2005.11401) / Atlas (arXiv 2208.03299) / RAGAS (arXiv 2309.15217) / DeepSeek V3 / Toolformer (arXiv 2302.04761) 五篇; 产业链接覆盖 LangChain/OpenAI/DeepSeek/McKinsey/Burberry/Perplexity 等真实企业的 deployment 与 consulting 场景。详见 research.md 与 industry.md。

*v7.0 研究产出与产业链接层追加于 2026-07-26。*

---

## 学术前沿层 (v9.0)

本单元新增 `frontier.md`：注入 2025-2026 最新学术前沿（N 篇真实 arXiv 论文 + 批判性综述 + delta_to_unit + ≥3 开放研究问题 + 方法论批评）。论文来自 `_frontier_corpus/elective-e3-llm-intro.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证），覆盖前沿课题：LLM推理经济 × 推理模型 × 高效推理。面向博后/教授级读者：批判性综述非罗列，delta_to_unit 显式指出前沿如何更新本单元所教，开放问题为可发表研究方向。详见 `frontier.md`。
