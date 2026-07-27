# Day 3 深链阅读清单

> v5.0升级：从"课程主页"升级为**经验证的深链**（指向具体文章/论文/文档章节，非主页）。全部链接已验证存在。

---

## ① LangGraph多Agent系统（本Day基准框架）

### LangGraph多Agent协作教程（已验证）
- 🌐 多Agent协作教程：https://docs.langchain.com/oss/python/langgraph/tutorials/multi_agent/multi-agent-collaboration （已验证，2026-07-25）
- **深链用法**：本Day TODO3用supervisor拓扑，TODO4用team拓扑。读此教程的"Supervisor"章节理解`add_conditional_edges`如何实现中心化路由，读"Network"章节理解去中心化Agent间直接通信。这是本Day真实运行的核心参考。

### LangGraph核心概念文档（已验证）
- 🌐 概念文档-低层级API：https://docs.langchain.com/oss/python/langgraph/concepts/low_level （已验证，2026-07-25）
- **深链用法**：本Day TODO1定义`MultiAgentState`（TypedDict + Annotated reducer）。读此文档理解State/Node/Edge/Reducer四要素，特别是`Annotated[list, operator.add]`如何实现Agent间消息累积。

### LangGraph多Agent系统架构指南（已验证）
- 🌐 多Agent系统架构：https://docs.langchain.com/oss/python/langgraph/concepts/multi_agent/ （已验证，2026-07-25）
- **深链用法**：读"Multi-agent architectures"章节，理解supervisor/hierarchical/network三种拓扑的适用场景。本DayTODO3/TODO4分别实现supervisor和team两种拓扑，此文档是选型依据。

---

## ② networkx网络科学（本Day拓扑分析工具）

### networkx官方教程（已验证）
- 🌐 教程-图基础：https://networkx.org/documentation/stable/tutorial.html （已验证，2026-07-25）
- **深链用法**：本Day TODO5用networkx构建Agent通信图。读"Creating a graph"和"Adding attributes"章节，理解DiGraph/节点属性/边属性。Agent=节点，消息流=有向边。

### networkx中心性算法（已验证）
- 🌐 中心性算法参考：https://networkx.org/documentation/stable/reference/algorithms/centrality.html （已验证，2026-07-25）
- **深链用法**：本Day TODO5计算度中心性/介数中心性。读`degree_centrality`和`betweenness_centrality`文档，理解哪个Agent是通信枢纽（度中心性高），哪个Agent是信息瓶颈（介数中心性高）。

### networkx连通性分析（已验证）
- 🌐 连通性算法参考：https://networkx.org/documentation/stable/reference/algorithms/component.html （已验证，2026-07-25）
- **深链用法**：本Day TODO5评估拓扑鲁棒性。读`is_strongly_connected`和`strongly_connected_components`文档，理解多Agent系统的消息可达性--移除某Agent后是否仍能全员通信。

---

## ③ 2026前沿：A2A/MCP协议与多Agent仿真

### A2A协议（Google，Agent间互操作标准）
- 📄 官方博客：https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/ （已验证，2025-06发布）
- 📦 协议规范GitHub：https://github.com/google/A2A （已验证）
- **深链用法**：A2A是2026年多Agent仿真的核心基础设施。读此博客理解A2A如何定义Agent Card（发现）、Task（委托）、State（查询）机制。本Day讲义的通信协议设计引用A2A的"Agent间互操作"理念。

### MCP（Model Context Protocol，Anthropic）
- 🌐 官方文档：https://modelcontextprotocol.io/ （已验证，2026-07-25）
- 📦 规范GitHub：https://github.com/modelcontextprotocol/specification （已验证）
- **深链用法**：MCP解决Agent与工具连接，与A2A（Agent间连接）互补。读"Architecture"理解client-server模型。本Day的Agent工具函数（产品库/竞品库查询）可视为MCP工具的简化版。

### Generative Agents论文（Stanford，多Agent仿真基础）
- 📄 arXiv 2304.03442：https://arxiv.org/abs/2304.03442 （已验证）
- **深链用法**：本Day天道推演×多Agent仿真的理论基础。读§3理解Agent的memory stream和reflection机制，理解多Agent如何涌现出群体智能。本Day的涌现行为分析借鉴此论文的"emergence"概念。

### AutoGen论文（微软，对话驱动多Agent）
- 📄 arXiv 2308.08155：https://arxiv.org/abs/2308.08155 （已验证）
- **深链用法**：AutoGen的GroupChat是team去中心化拓扑的代表。读§3理解ConversableAgent如何通过对话消息驱动协作，对比本DayTODO4的team拓扑实现，理解"对话驱动"vs"图驱动"的差异。

### MetaGPT论文（SOP驱动的多Agent）
- 📄 arXiv 2308.00352：https://arxiv.org/abs/2308.00352 （已验证）
- **深链用法**：MetaGPT的SOP是hierarchical层级拓扑的代表。读§3理解Standard Operating Procedure如何预定义Agent协作流程，对比本Day的supervisor拓扑，理解"流程驱动"vs"路由驱动"的差异。

---

## ④ 营销多Agent系统延伸

### Anthropic "Building Effective Agents"（多Agent模式参考）
- 📄 官方文章：https://www.anthropic.com/research/building-effective-agents （已验证，2024-12-19发布）
- **深链用法**：文章后半部分讨论多Agent模式（Multi-agent collaboration）。读"Patterns"一节理解Evaluator-Optimizer和Orchestrator-Worker模式，这是本Daysupervisor拓扑的工程实践参考。

### LangGraph Human-in-the-loop教程（营销审核场景）
- 🌐 HITL教程：https://docs.langchain.com/oss/python/langgraph/how-tos/human_in_the_loop/dynamic_tools （已验证，2026-07-25）
- **深链用法**：营销多Agent系统的reviewer审核节点常需HITL。读此教程理解`interrupt`机制，当reviewer和writer冲突无法解决时升级人工审核。本DayTODO6的涌现分析可扩展到HITL场景。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本Day `notes.md`理论回顾 + 独立教材§Day 3 | 多Agent理论 | 1h |
| 2 | LangGraph多Agent协作教程 | 理解supervisor/team拓扑 | 0.5h |
| 3 | `starter.ipynb`上机（配LangGraph+networkx文档） | 真实库实操 | 2h |
| 4 | networkx中心性算法文档（选读） | 理解拓扑指标 | 0.5h |
| 5 | A2A博客 + MCP文档（选读） | 2026前沿协议 | 0.5h |
| 6 | Generative Agents论文§3（选读） | 多Agent仿真理论 | 0.5h |
| 7 | AutoGen/MetaGPT论文摘要（选读） | 对比拓扑设计 | 0.5h |

---

*全部深链已于2026-07-25验证存在。如发现失效，请在Issues报告。*
