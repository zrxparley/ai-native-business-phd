# Day 2 深链阅读清单

> v5.0升级：从"课程主页"升级为**经验证的深链**（指向具体文章/论文/文档章节，非主页）。全部链接已验证存在。

---

## ① 四框架官方文档与源码

### LangGraph官方文档（本Day基准框架，已验证）
- 🌐 概念文档-核心概念：https://docs.langchain.com/oss/python/langgraph/concepts/low_level （已验证，2026-07-25）
- 📦 GitHub：https://github.com/langchain-ai/langgraph （38k+星）
- **深链用法**：本Day TODO2用`create_react_agent`，TODO3用`StateGraph`+`add_conditional_edges`。先读"Low Level"概念文档理解StateGraph/Node/Edge/Reducer，再读"Prebuilt"部分对照ReAct实现。这是本Day真实运行的核心参考。

### CrewAI官方文档（角色化协作框架，已验证）
- 🌐 核心概念-Agents：https://docs.crewai.com/concepts/agents （已验证，2026-07-25）
- 🌐 核心概念-Tasks：https://docs.crewai.com/concepts/tasks （已验证，2026-07-25）
- 📦 GitHub：https://github.com/crewAIInc/crewAI （25k+星）
- **深链用法**：本Day TODO5静态分析CrewAI API。读Agents文档理解role/goal/backstory三要素，读Tasks文档理解context依赖（隐式编排执行顺序的关键）。对比LangGraph的显式图定义，理解"角色化编排"vs"图编排"的差异。

### AutoGen官方文档（对话驱动框架，已验证）
- 🌐 核心概念-GroupChat：https://microsoft.github.io/autogen/docs/topics/groupchat/ （已验证，2026-07-25）
- 📦 GitHub：https://github.com/microsoft/autogen （40k+星，CC-BY-4.0）
- **深链用法**：本Day TODO6静态分析AutoGen API。读GroupChat文档理解ConversableAgent/GroupChat/GroupChatManager三件套，理解max_round如何控制对话收敛。对比LangGraph的条件边和CrewAI的Task依赖，理解"对话驱动"vs"图驱动"的差异。

---

## ② 框架对比与选型

### LangGraph多Agent系统教程（对标Day 3，已验证）
- 🌐 多Agent协作教程：https://docs.langchain.com/oss/python/langgraph/tutorials/multi_agent/multi-agent-collaboration （已验证，2026-07-25）
- **深链用法**：本Day是单Agent框架对比，Day 3进入多Agent。提前浏览此教程了解Supervisor/Hierarchical/Network三种多Agent协调模式，理解LangGraph在多Agent场景下的扩展能力。

### Anthropic "Building Effective Agents"（Agent工程实践权威参考）
- 📄 官方文章：https://www.anthropic.com/research/building-effective-agents （已验证，2024-12-19发布）
- **深链用法**：文章定义了Workflow vs Agent的核心区分。读"Agents"一节理解Agent的"LLM自主控制流程"定义，读"Patterns"一节理解ReAct/Plan-Execute等模式。本Day框架对比的底层理论参考。

---

## ③ 2026前沿：协议层与多Agent仿真

### A2A协议（Google，Agent间互操作标准）
- 📄 官方博客：https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/ （已验证，2025-06发布）
- **深链用法**：A2A是2026年多Agent仿真的核心基础设施。读此博客理解A2A如何定义Agent间互操作标准，与MCP（Agent与工具连接）互补。本Day讲义的2026前沿部分引用此协议。

### MCP（Model Context Protocol，Anthropic）
- 🌐 官方文档：https://modelcontextprotocol.io/ （已验证，2026-07-25）
- 📦 规范GitHub：https://github.com/modelcontextprotocol/specification （已验证）
- **深链用法**：MCP在2025-2026年快速普及，成为Agent连接外部工具和数据源的事实标准。读"Introduction"理解MCP如何标准化工具层，读"Architecture"理解client-server模型。LangGraph/CrewAI/AutoGen均逐步支持MCP。

### Generative Agents论文（Stanford，多Agent仿真基础）
- 📄 arXiv 2304.03442：https://arxiv.org/abs/2304.03442 （已验证）
- **深链用法**：本Day讲义提到多Agent仿真是2026前沿。读§3理解Agent的长期记忆流（memory stream）和反思（reflection）机制，这是多Agent仿真（Day 3+）的理论基础。

### Plan-and-Solve论文（Plan-Execute范式改进）
- 📄 arXiv 2305.04091：https://arxiv.org/abs/2305.04091 （已验证）
- **深链用法**：本Day TODO3实现Plan-Execute模式。读此论文理解"先规划后执行"相比"逐步推理"的优势和局限，理解Plan-Execute在结构化营销任务中的适用性。对比TODO2的ReAct模式，理解两范式的权衡。

---

## ④ 营销Agent延伸

### LangGraph Human-in-the-loop教程（营销审核场景）
- 🌐 HITL教程：https://docs.langchain.com/oss/python/langgraph/how-tos/human_in_the_loop/dynamic_tools （已验证，2026-07-25）
- **深链用法**：营销Agent常需HITL审核（如策略发布前人工确认）。读此教程理解`interrupt_before`/`interrupt_after`机制，理解LangGraph在HITL场景下的原生优势（对比CrewAI/AutoGen需自定义）。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本Day `notes.md`理论回顾 + 独立教材§Day 2 | 框架对比理论 | 1h |
| 2 | LangGraph核心概念文档 | 理解StateGraph | 0.5h |
| 3 | `starter.ipynb`上机（配LangGraph文档） | 真实库实操 | 2h |
| 4 | CrewAI Agents/Tasks文档（选读） | 理解角色化协作 | 0.5h |
| 5 | AutoGen GroupChat文档（选读） | 理解对话驱动 | 0.5h |
| 6 | A2A博客 + MCP文档（选读） | 2026前沿协议 | 0.5h |
| 7 | Plan-and-Solve论文（选读） | 深入Plan-Execute | 0.5h |

---

*全部深链已于2026-07-25验证存在。如发现失效，请在Issues报告。*
