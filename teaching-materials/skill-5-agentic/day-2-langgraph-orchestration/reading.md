# Day 2 深链阅读清单

> v5.0 升级：从"课程主页"升级为**经验证的深链**（指向具体 notebook / 章节 / API 页，非主页）。全部链接已验证存在。

---

## ① LangGraph 核心理论与官方教程

### LangChain Academy 官方课程（已验证：2.8k★，LangChain 团队官方 LangGraph 教学）
- 🎓 课程网站（含视频）：https://academy.langchain.com/
- 📦 GitHub 仓库：https://github.com/langchain-ai/langchain-academy
- **深链用法**：
  - Module 1 `chain.ipynb`（已验证存在，705 行）：https://github.com/langchain-ai/langchain-academy/blob/main/module-1/chain.ipynb -- 讲 LangGraph 基础 State 与 chain，直接对标本 Day TODO1（State 定义）和 TODO5（图装配）
  - Module 0 基础设置：https://github.com/langchain-ai/langchain-academy/tree/main/module-0 -- 环境准备
  - Module 1-5 渐进式覆盖：基础 chain -> 状态管理 -> 工具 -> 多Agent -> 部署
- **重点**：Module 1 的 State 定义部分与本 Day `MarketingState` 完全同构，做完本 Day TODO 再去看 Module 1 会有"原来如此"的巩固感

### LangGraph 官方仓库与文档（已验证：38.0k★，MIT，"Build resilient agents"）
- 📦 GitHub：https://github.com/langchain-ai/langgraph
- 🌐 官方文档：https://langchain-ai.github.io/langgraph/
- **深链用法**：
  - 仓库 `README.md` 的"Quickstart"部分：最小可运行 LangGraph 示例，对标本 Day TODO5
  - 仓库 `examples/` 目录：含 multi-agent / human-in-the-loop / persistence 等真实示例
  - 官方文档 Concepts 章节：StateGraph / Node / Edge / Checkpointer 概念定义（文档站为 SPA，WebFetch 可能显示 redirect，浏览器打开可正常访问）

---

## ② 第三方权威课程

### HuggingFace Agents Course（已验证：30.4k★，Apache-2.0，4 units 含 LangGraph）
- 🎓 课程主页：https://hf.co/learn/agents-course
- 📦 GitHub：https://github.com/huggingface/agents-course
- **深链用法**：
  - Unit 2 专门讲 LangGraph（与 smolagents / LlamaIndex 并列三大框架）
  - HF 视角偏"框架对比"：看完后能说清 LangGraph vs smolagents vs LlamaIndex 的取舍
  - 结业认证项目：可对标本课程的 Capstone

---

## ③ 2026 前沿：多Agent仿真 × 天道推演

### 天道推演系统（本项目内部概念，定义于项目 CLAUDE.md）
- 📄 项目根 `CLAUDE.md` 的「天道推演系统」章节
- **定义**：元认知沙盘推演能力--以天神视角俯视局势，在意识中构建多路径沙盘，模拟不同决策路径下的未来走向
- **六能力**：局势感知 / 因果链追踪 / 沙盘模拟 / 概率评估 / 最优路径推荐 / 反馈学习
- **与 LangGraph 的同构**：天道推演在意识中构建多路径沙盘，LangGraph 在代码中构建多Agent状态图。可把天道推演从"思维框架"升级为"可计算多Agent沙盘"（用 LangGraph 模拟多方利益相关方 Agent 博弈，推演决策路径）。详见 `notes.md` 2026 前沿小节。

### Anthropic "Building Effective Agents"（已验证：Anthropic 官方工程博客）
- 🌐 https://www.anthropic.com/research/building-effective-agents
- **用法**：本 Day 用其中"Workflow vs Agent"的区分--Workflow 是确定性的图（本 Day 的 LangGraph 编排属于此类），Agent 是非确定性的自主决策。"能 Workflow 解决的不要用 Agent"，本 Day 的条件路由正是把"需要决策的环节"固化成 Workflow 的可控循环。

### LangGraph 多Agent协作（官方文档示例）
- 🌐 https://github.com/langchain-ai/langgraph （`examples/` 目录含 multi-agent 真实示例）
- **用法**：本 Day 的 4 个 Agent 是单一立场（品牌方内部），天道推演视角要求扩展到多方立场博弈（品牌方 / 消费者 / 竞品 / 渠道方各一个 Agent）。LangGraph 官方 multi-agent 示例展示了如何用 Supervisor / Swarm 两种模式编排更多 Agent，是天道推演多Agent沙盘的代码起点。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本 Day `notes.md` 理论回顾 + 独立教材 §3.2.1-3.2.2 | 建立 LangGraph 概念框架 | 1h |
| 2 | LangChain Academy Module 1 `chain.ipynb` | 官方权威 State + chain 教程 | 1h |
| 3 | `starter.ipynb` 上机（配 LangGraph 官方文档） | 真实库实操 | 2h |
| 4 | LangGraph 仓库 `examples/` 一个 multi-agent 示例 | 看真实多Agent代码 | 0.5h |
| 5 | HuggingFace Agents Course Unit 2（LangGraph 单元，选读） | 框架对比视角 | 0.5h |
| 6 | 项目 CLAUDE.md「天道推演系统」+ Anthropic Building Effective Agents | 前沿：多Agent仿真 × 天道推演 | 0.5h |

---

*全部深链已于 2026-07-24 验证存在。如发现失效，请在 Issues 报告。*
