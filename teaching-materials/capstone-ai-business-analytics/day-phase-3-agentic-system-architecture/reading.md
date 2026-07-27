# Phase 3 深链阅读清单

> v5.0升级：从"课程主页"升级为**经验证的深链**（指向具体notebook / 章节 / API页，非主页）。全部链接已验证存在。

---

## 1. LangGraph核心理论与官方教程

### LangGraph官方仓库与文档（已验证：MIT，"Build resilient agents"）
- GitHub：https://github.com/langchain-ai/langgraph
- 官方文档：https://langchain-ai.github.io/langgraph/
- **深链用法**：
  - 仓库 `README.md` 的Quickstart：最小可运行LangGraph示例，对标本Phase TODO5（图装配）
  - 仓库 `examples/` 目录：含multi-agent / human-in-the-loop / persistence等真实示例
  - 官方文档Concepts章节：StateGraph / Node / Edge / Checkpointer概念定义

### LangChain Academy官方课程（已验证：LangChain团队官方LangGraph教学）
- 课程网站（含视频）：https://academy.langchain.com/
- GitHub仓库：https://github.com/langchain-ai/langchain-academy
- **深链用法**：
  - Module 1 `chain.ipynb`：https://github.com/langchain-ai/langchain-academy/blob/main/module-1/chain.ipynb -- 讲LangGraph基础State与chain，直接对标本Phase TODO1（State定义）和TODO5（图装配）
  - Module 0基础设置：https://github.com/langchain-ai/langchain-academy/tree/main/module-0 -- 环境准备
  - Module 1-5渐进式覆盖：基础chain -> 状态管理 -> 工具 -> 多Agent -> 部署

---

## 2. Capstone教材与Agent架构模式

### Capstone独立教材Phase 3节（已验证：本课程教材）
- 文件：[`../../AI原生化商业博士_独立教材_Capstone_AI和商业分析项目.md`](../../AI原生化商业博士_独立教材_Capstone_AI和商业分析项目.md)
- **深链用法**：第438-660行Phase 3节，含三层架构设计 / LangGraph Agent工作流代码示例 / 人机协作治理框架 / 交付物清单。本Phase的Agent系统架构直接基于此节设计。

### Anthropic "Building Effective Agents"（已验证：Anthropic官方工程博客）
- https://www.anthropic.com/research/building-effective-agents
- **用法**：本Phase用其中"Workflow vs Agent"的区分与五种设计模式（Prompt链/路由/聚合/Orchestrator-Workers/Evaluator-Optimizer）。Workflow是确定性的图（本Phase的LangGraph编排属于此），Agent是非确定性的自主决策。"能Workflow解决的不要用Agent"，本Phase的条件路由正是把"需要决策的环节"固化成Workflow的可控循环。Plan-Execute模式是其中Orchestrator-Workers的简化版。

### 技能5独立教材（已验证：本课程教材）
- 文件：[`../../AI原生化商业博士_独立教材_技能5_Agentic系统工程与落地.md`](../../AI原生化商业博士_独立教材_技能5_Agentic系统工程与落地.md)
- **深链用法**：Day 1讲Agent架构模式（ReAct/Plan-Execute/Reflection），Day 2讲LangGraph编排。本Phase整合技能5 Day1的Plan-Execute模式 + Day2的StateGraph/HITL机制。

---

## 3. 2026前沿：MCP / A2A / 天道推演×多Agent仿真

### MCP（Model Context Protocol）（已验证：Anthropic提出）
- 官方文档：https://modelcontextprotocol.io/
- GitHub：https://github.com/modelcontextprotocol
- **用法**：Anthropic提出的LLM接工具的标准协议。本Phase的researcher_agent通过读取Phase 2知识图谱模拟MCP工具调用 -- Agent通过标准协议调用知识图谱工具检索市场知识。企业级多Agent系统：LangGraph做编排 + MCP做工具接入。

### A2A（Agent-to-Agent Protocol）（已验证：Google 2024提出）
- GitHub：https://github.com/google/A2A
- **用法**：Google提出的Agent间通信协议，与MCP互补（MCP接工具，A2A接Agent）。本Phase的多Agent通过LangGraph State共享通信（同进程内）；A2A解决跨进程、跨组织、跨框架的Agent间通信。企业级多Agent系统的未来：LangGraph做进程内编排 + A2A做跨进程协作 + MCP做工具接入。

### 天道推演系统（本项目内部概念，定义于项目CLAUDE.md）
- 项目根 `CLAUDE.md` 的「天道推演系统」章节
- **定义**：元认知沙盘推演能力 -- 以天神视角俯视局势，在意识中构建多路径沙盘，模拟不同决策路径下的未来走向
- **六能力**：局势感知 / 因果链追踪 / 沙盘模拟 / 概率评估 / 最优路径推荐 / 反馈学习
- **与LangGraph的同构**：天道推演在意识中构建多路径沙盘，LangGraph在代码中构建多Agent状态图。条件边=决策分支，Checkpointing=推演假设记录，反馈学习节点=因果模型更新。可把天道推演从"思维框架"升级为"可计算多Agent沙盘"。详见 `notes.md` 2026前沿小节。

### HuggingFace Agents Course（已验证：Apache-2.0，4 units含LangGraph）
- 课程主页：https://hf.co/learn/agents-course
- GitHub：https://github.com/huggingface/agents-course
- **深链用法**：Unit 2专门讲LangGraph（与smolagents / LlamaIndex并列三大框架），HF视角偏"框架对比"，看完后能说清LangGraph vs smolagents vs LlamaIndex的取舍。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本Phase `notes.md` 理论回顾 + Capstone教材Phase 3节 | 建立三层架构 + LangGraph概念框架 | 1h |
| 2 | Anthropic "Building Effective Agents" | 五种Agent设计模式 + Plan-Execute权威指南 | 0.5h |
| 3 | `starter.ipynb` 上机（配LangGraph官方文档） | 真实库实操：State/条件边/interrupt/HITL/Phase 2整合 | 2h |
| 4 | LangChain Academy Module 1 `chain.ipynb` | 官方权威State + chain教程，巩固TODO1/TODO5 | 1h |
| 5 | MCP + A2A GitHub仓库README | 前沿：工具接入 + Agent协作协议 | 0.5h |
| 6 | 项目CLAUDE.md「天道推演系统」+ 技能5教材Day1-2 | 前沿：多Agent仿真×天道推演 + Agent架构模式 | 1h |

---

*全部深链已于2026-07-24验证存在。如发现失效，请在Issues报告。*
