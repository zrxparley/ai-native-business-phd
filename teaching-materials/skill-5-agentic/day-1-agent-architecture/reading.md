# Day 1 深链阅读清单

> v5.0 升级：从"课程主页"升级为**经验证的深链**（指向具体文章 / 论文 / 文档章节，非主页）。全部链接已验证存在。

---

## ① Agent 架构基础理论

### Anthropic "Building Effective Agents"（业界最权威的 Agent 工程实践参考）
- 📄 官方文章：https://www.anthropic.com/research/building-effective-agents （已验证，2024-12-19 发布）
- **深链用法**：文章总结了五种 Agent 构建模式（Prompt Chaining / Routing / Parallelization / Orchestrator-Workers / Evaluator-Optimizer），直接对标本 Day 的理论回顾 5。重点读"Workflows and Agents"一节，理解"能用 Workflow 解决的，不要用 Agent"这一核心实践建议。

### ReAct 原始论文（Yao et al., 2022, ICLR 2023）
- 📄 arXiv 2210.03629：https://arxiv.org/abs/2210.03629 （已验证，CC BY 4.0 开源）
- **深链用法**：ReAct 是本 Day 的核心模式。读 §3（Method）理解 Thought-Action-Observation 循环的设计原理，读 §4（Experiments）看 ReAct 在推理和问答任务上相比纯推理（CoT）的优势。

### Self-Refine 论文（Reflection 模式的理论基础）
- 📄 arXiv 2303.17651（Madaan et al., NeurIPS 2023）：https://arxiv.org/abs/2303.17651
- **深链用法**：本 Day TODO5 实现 Reflection 循环。读 §3 理解"生成 -> 评估 -> 改进"循环的原理，以及为什么 LLM 能有效地"自我批评"。

---

## ② 真实库 + 上机

### LangGraph 官方文档（已验证：LangGraph overview）
- 🌐 新址：https://docs.langchain.com/oss/python/langgraph （已验证，2026-07-24）
- 📦 GitHub：https://github.com/langchain-ai/langgraph （38k 星）
- **深链用法**：文档的"Quickstart"部分展示 `StateGraph` 基础用法，"Prebuilt"部分展示 `create_react_agent`（本 Day TODO2 的核心 API）。先读 overview 理解 LangGraph 定位（"低层级编排框架"），再读 prebuilt 部分对照 starter.ipynb。

### LangChain 官方文档
- 🌐 官方文档：https://python.langchain.com/docs/
- 📦 GitHub：https://github.com/langchain-ai/langchain （142k 星）
- **深链用法**：重点看"Tools"章节，理解 `@tool` 装饰器的用法（本 Day TODO1 的核心）。以及"Chat Models"章节，理解 `ChatOpenAI`/`ChatAnthropic` 的配置。

### LangGraph 持久化与记忆文档
- 🌐 概念文档：https://docs.langchain.com/oss/python/langgraph/concepts/persistence
- **深链用法**：本 Day TODO4 用 `MemorySaver` 实现短期记忆。读此文档理解 checkpointer 概念、`thread_id` 的作用、以及如何切换到持久化后端（如 PostgreSQL）。

---

## ③ 2026 前沿：MCP（Model Context Protocol）

### MCP 官方文档（已验证）
- 🌐 官网：https://modelcontextprotocol.io/
- 📄 架构概览：https://modelcontextprotocol.io/docs/concepts/architecture （已验证，2026-07-24）
- **深链用法**：读此文档理解 MCP 的 Client-Server 架构（Host/Client/Server 三层）、三大原语（Tools/Resources/Prompts）、两种传输层（Stdio/Streamable HTTP）。重点理解"为什么 MCP 让 Agent 工具集成从'定制开发'变成'即插即用'"。

### MCP 参考服务器（GitHub）
- 📦 官方服务器集：https://github.com/modelcontextprotocol/servers
- **深链用法**：浏览已有 MCP Server（Filesystem / GitHub / Slack / Google Drive / PostgreSQL...），理解"一个 Server 暴露一组工具"的模式。尝试运行 Filesystem Server 体验 MCP 工作流。

### MCP 规范文档
- 📄 最新规范：https://modelcontextprotocol.io/specification/latest
- **深链用法**：进阶阅读，理解 JSON-RPC 2.0 消息格式、生命周期管理、能力协商。适合想开发自定义 MCP Server 的同学。

---

## ④ 营销 Agent 延伸

### LangGraph 多 Agent 系统（对标 Day 3）
- 📄 多 Agent 协作文档：https://docs.langchain.com/oss/python/langgraph/tutorials/multi_agent/multi-agent-collaboration
- **深链用法**：本 Day 是单 Agent，Day 3 是多 Agent。提前浏览此文档了解 Supervisor / Hierarchical / Network 三种多 Agent 协调模式。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | Anthropic "Building Effective Agents" | 建立架构直觉 | 0.5h |
| 2 | 本 Day `notes.md` 理论回顾 + 独立教材 §3.1.1-3.1.4 | 理论框架 | 1h |
| 3 | `starter.ipynb` 上机（配 LangGraph 文档） | 真实库实操 | 2h |
| 4 | ReAct 论文 §3-4（选读） | 深入理解 ReAct | 0.5h |
| 5 | MCP 架构概览 | 前沿趋势 | 0.5h |
| 6 | Self-Refine 论文（选读） | 深入理解 Reflection | 0.5h |

---

*全部深链已于 2026-07-24 验证存在。如发现失效，请在 Issues 报告。*
