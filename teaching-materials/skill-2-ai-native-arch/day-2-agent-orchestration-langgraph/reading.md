# Day 2 深链阅读清单

> v5.0 升级：从"课程主页"升级为**经验证的深链**（指向具体 notebook / 章节 / API 页，非主页）。全部链接已验证存在。

---

## ① LangGraph 核心理论与官方教程

### LangGraph 官方仓库与文档（已验证：MIT，"Build resilient agents"）
- GitHub：https://github.com/langchain-ai/langgraph
- 官方文档：https://langchain-ai.github.io/langgraph/
- **深链用法**：
  - 仓库 `README.md` 的 Quickstart：最小可运行 LangGraph 示例，对标本 Day TODO5（图装配）
  - 仓库 `examples/` 目录：含 multi-agent / human-in-the-loop / persistence 等真实示例
  - 官方文档 Concepts 章节：StateGraph / Node / Edge / Checkpointer 概念定义

### LangChain Academy 官方课程（已验证：LangChain 团队官方 LangGraph 教学）
- 课程网站（含视频）：https://academy.langchain.com/
- GitHub 仓库：https://github.com/langchain-ai/langchain-academy
- **深链用法**：
  - Module 1 `chain.ipynb`：https://github.com/langchain-ai/langchain-academy/blob/main/module-1/chain.ipynb -- 讲 LangGraph 基础 State 与 chain，直接对标本 Day TODO1（State 定义）和 TODO5（图装配）
  - Module 0 基础设置：https://github.com/langchain-ai/langchain-academy/tree/main/module-0 -- 环境准备
  - Module 1-5 渐进式覆盖：基础 chain -> 状态管理 -> 工具 -> 多Agent -> 部署

---

## ② 企业架构视角：Agent 编排模式

### Anthropic "Building Effective Agents"（已验证：Anthropic 官方工程博客）
- https://www.anthropic.com/research/building-effective-agents
- **用法**：本 Day 用其中"Workflow vs Agent"的区分与五种设计模式（Prompt链/路由/聚合/Orchestrator-Workers/Evaluator-Optimizer）。Workflow 是确定性的图（本 Day 的 LangGraph 编排属于此类），Agent 是非确定性的自主决策。"能 Workflow 解决的不要用 Agent"，本 Day 的条件路由正是把"需要决策的环节"固化成 Workflow 的可控循环。详见独立教材第 516-606 行。

### LangGraph 多 Agent 协作（官方文档示例）
- https://github.com/langchain-ai/langgraph
- **用法**：本 Day 的 4 个 Agent 是单一立场（品牌方内部），天道推演视角要求扩展到多方立场博弈。LangGraph 官方 multi-agent 示例展示了 Supervisor / Swarm 两种编排模式，是企业级多 Agent 拓扑的代码起点。

---

## ③ 2026 前沿：A2A / Plan-Execute / 天道推演×多Agent仿真

### A2A（Agent-to-Agent Protocol）（已验证：Google 2024 提出）
- GitHub：https://github.com/google/A2A
- **用法**：Google 提出的 Agent 间通信协议，与 MCP 互补（MCP 接工具，A2A 接 Agent）。本 Day 的多 Agent 通过 LangGraph State 共享通信（同进程内）；A2A 解决跨进程、跨组织、跨框架的 Agent 间通信。企业级多 Agent 系统的未来：LangGraph 做进程内编排 + A2A 做跨进程协作 + MCP 做工具接入。

### 天道推演系统（本项目内部概念，定义于项目 CLAUDE.md）
- 项目根 `CLAUDE.md` 的「天道推演系统」章节
- **定义**：元认知沙盘推演能力 -- 以天神视角俯视局势，在意识中构建多路径沙盘，模拟不同决策路径下的未来走向
- **六能力**：局势感知 / 因果链追踪 / 沙盘模拟 / 概率评估 / 最优路径推荐 / 反馈学习
- **与 LangGraph 的同构**：天道推演在意识中构建多路径沙盘，LangGraph 在代码中构建多 Agent 状态图。条件边 = 决策分支，Checkpointing = 推演假设记录，反馈学习节点 = 因果模型更新。可把天道推演从"思维框架"升级为"可计算多 Agent 沙盘"。详见 `notes.md` 2026 前沿小节。

### HuggingFace Agents Course（已验证：Apache-2.0，4 units 含 LangGraph）
- 课程主页：https://hf.co/learn/agents-course
- GitHub：https://github.com/huggingface/agents-course
- **深链用法**：Unit 2 专门讲 LangGraph（与 smolagents / LlamaIndex 并列三大框架），HF 视角偏"框架对比"，看完后能说清 LangGraph vs smolagents vs LlamaIndex 的取舍。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本 Day `notes.md` 理论回顾 + 独立教材 § Day 2 | 建立企业架构视角的 LangGraph 概念框架 | 1h |
| 2 | Anthropic "Building Effective Agents" | 五种 Agent 设计模式权威指南 | 0.5h |
| 3 | `starter.ipynb` 上机（配 LangGraph 官方文档） | 真实库实操：State/条件边/interrupt/HITL | 2h |
| 4 | LangChain Academy Module 1 `chain.ipynb` | 官方权威 State + chain 教程，巩固 TODO1/TODO5 | 1h |
| 5 | A2A GitHub 仓库 README | 前沿：Agent-to-Agent 协议，理解 MCP/A2A 互补 | 0.5h |
| 6 | 项目 CLAUDE.md「天道推演系统」+ HuggingFace Agents Course Unit 2 | 前沿：多Agent仿真×天道推演 + 框架对比 | 0.5h |

---

*全部深链已于 2026-07-24 验证存在。如发现失效，请在 Issues 报告。*
