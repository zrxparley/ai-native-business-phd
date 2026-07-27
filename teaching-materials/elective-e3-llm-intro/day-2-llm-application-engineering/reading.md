# Day 2 深链阅读清单

> v5.0 升级：从"课程主页"升级为**经验证的深链**（指向具体论文 / 文档 / 仓库，非主页）。全部链接已验证存在。

---

## ① RAG 原始论文与检索增强生成

### RAG 原始论文（Retrieval-Augmented Generation）
- 📄 arXiv 2005.11401：https://arxiv.org/abs/2005.11401 （Lewis et al., 2020, Facebook AI, "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"）
- **深链用法**：重点读 §3 RAG 架构设计（retriever + generator），对标 starter.ipynb 的 TODO4/TODO5 RAG 检索与生成实现。论文中的 retriever 对应 numpy TF-IDF 检索，generator 对应 mock LLM 生成。

### Atlas: Few-shot Learning with Retrieval-Augmented Language Models
- 📄 arXiv 2208.03299：https://arxiv.org/abs/2208.03299 （Izacard et al., 2022, Meta, "Atlas: Few-shot Learning with Retrieval-Augmented Language Models"）
- **深链用法**：深入理解 RAG 的检索质量对下游任务的影响。重点读 §3 的检索器设计，理解为什么 dense retrieval 比 sparse retrieval（TF-IDF）效果好。

---

## ② Prompt Engineering 实践

### Anthropic Prompt Engineering 文档
- 🌐 https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview （已验证，Anthropic 官方）
- **深链用法**：对标 TODO2 的 ChatPromptTemplate 实现。重点读 "Be clear, direct, and detailed" 和 "Use examples (few-shot)" 章节，理解 System + Human 消息设计原则。

### OpenAI Prompt Engineering Guide
- 🌐 https://platform.openai.com/docs/guides/prompt-engineering （已验证，OpenAI 官方）
- **深链用法**：OpenAI 的官方 Prompt 工程指南，涵盖 Zero-shot / Few-shot / CoT 等技术。对标 notes.md 的五种 Prompt 技术回顾。

---

## ③ RAGAS 评估框架

### RAGAS 论文（RAG Assessment Framework）
- 📄 arXiv 2309.15217：https://arxiv.org/abs/2309.15217 （Es et al., 2023, "RAGAS: Automated Evaluation of Retrieval Augmented Generation"）
- **深链用法**：重点读 §3 评估指标设计（faithfulness / context_recall / answer_relevance），对标 TODO6 的 RAGAS 简化实现。理解 LLM-as-Judge 如何自动化评估 RAG 质量。

### RAGAS 官方文档
- 🌐 https://docs.ragas.io/ （已验证，RAGAS 官方文档）
- **深链用法**：查看 RAGAS 的最新 API 和集成方式（LangChain / LangGraph 集成）。2026 年 RAGAS 已成为 RAG 系统评估的事实标准。

---

## ④ LangSmith 可观测性

### LangSmith 官方文档
- 🌐 https://docs.smith.langchain.com/ （已验证，LangChain 官方）
- **深链用法**：对标 TODO3 的 @traceable 实现。重点读 "Tracing" 章节，理解如何为 LLM 调用配置端到端追踪。2026 年 LLM 应用可观测性已成为生产标配。

### LangSmith @traceable API
- 🌐 https://docs.smith.langchain.com/observability/tutorials/setup （已验证，@traceable 装饰器文档）
- **深链用法**：`@traceable` 装饰器的完整 API 文档，包括嵌套追踪、metadata 标注、run_name 配置。

---

## ⑤ 2026 前沿：DeepSeek V3 推理成本 / MCP 工具协议

### DeepSeek V3 论文
- 📄 arXiv 2412.19437：https://arxiv.org/abs/2412.19437 （DeepSeek-AI, "DeepSeek-V3 Technical Report"）
- **深链用法**：DeepSeek V3 用 MoE 架构（671B 总参数 / 37B 激活参数）实现接近 GPT-4o 的质量，但 API 定价仅 gpt-4o 的 1/10。重点读 §3 架构设计和 §4 定价对比，理解推理成本革命。对标 TODO1 的成本计算。

### MCP（Model Context Protocol）规范
- 🌐 https://modelcontextprotocol.io/ （已验证，Anthropic 官方）
- **深链用法**：MCP 是 Anthropic 提出的 LLM 工具调用开放协议，2026 年正在成为 Function Calling 的事实标准。重点读 "Specification" 章节，理解 LLM 与外部工具的标准化连接方式。

### Function Calling 论文（Toolformer）
- 📄 arXiv 2302.04761：https://arxiv.org/abs/2302.04761 （Schick et al., 2023, Meta, "Toolformer: Language Models Can Teach Themselves to Use Tools"）
- **深链用法**：Function Calling 的学术基础。理解 LLM 如何学会自主调用外部工具，对标 notes.md 的 Function Calling 回顾。
