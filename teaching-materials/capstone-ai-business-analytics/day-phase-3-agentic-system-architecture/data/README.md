# Phase 3 真实库与资源说明

> v5.0核心：用**真实库LangGraph + langchain-core + pydantic**（非伪代码/模拟框架）。真实库的API细节、检查点机制、条件边注册、interrupt暂停-恢复，是伪代码学不到的。

---

## 主库 1：LangGraph（已验证，可运行）

**这是什么**：LangChain团队官方推出的Agent编排框架，把Agent工作流建模为**有状态有向图**（StateGraph），原生支持条件路由、循环、状态持久化与人机交互（HITL）。生产级复杂Agent的事实标准。

**为什么用它**（Capstone三层架构视角）：
- 原生支持条件边（`add_conditional_edges`）和循环 -- 线性Chain框架做不到
- 内置Checkpointing（`MemorySaver` / `SqliteSaver` / `PostgresSaver`），支持暂停-恢复与故障恢复
- 原生 `interrupt_before` 实现人机协同（HITL），Capstone治理的工程基础
- 图结构可视化 + 逐步执行 + 状态检查，生产级可调试性

**安装方式**（`pip install langgraph langchain-openai langchain-core`）：

```python
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
# interrupt_before 在 compile() 参数中使用，无需单独 import
```

**核心API速查**（本Phase上机会用到）：

| API | 作用 | 本Phase对应 |
|-----|------|------------|
| `StateGraph(State)` | 创建以State为全局状态的有向图 | `StateGraph(AgentSystemState)` |
| `workflow.add_node(name, fn)` | 添加节点（函数：State -> dict） | researcher/strategist/writer/review/publish |
| `workflow.add_edge(a, b)` | 添加普通边（a无条件到b） | START->researcher->strategist->writer->review |
| `workflow.add_conditional_edges(src, fn, mapping)` | 条件边（fn读State返回键名） | review -> route_after_review -> {publish, revise} |
| `workflow.compile(checkpointer=, interrupt_before=)` | 编译为可执行图 | MemorySaver + interrupt_before=["review"] |
| `graph.invoke(state, config)` | 执行图（到暂停点或终点） | Step 1: 执行到review前暂停 |
| `graph.update_state(config, values)` | 更新检查点状态 | Step 2: 注入approved=True |
| `graph.invoke(None, config)` | 从暂停点恢复执行 | Step 3: 恢复至完成 |
| `graph.get_state(config)` | 获取当前检查点状态 | 查看.next（暂停位置）和.values |

**来源与验证**：
- GitHub仓库：https://github.com/langchain-ai/langgraph （MIT，"Build resilient agents"，已验证2026-07-24）
- 官方文档：https://langchain-ai.github.io/langgraph/
- 已安装版本：langgraph（`pip install langgraph` 安装，2026-07-24验证通过）

---

## 主库 2：langchain-core（消息类型）

**这是什么**：LangChain的核心抽象层，提供 `HumanMessage` / `AIMessage` / `SystemMessage` 等消息类型，是所有LangChain生态框架（含LangGraph）的基础。

**为什么用它**：LangGraph节点调用LLM时，用消息类型构造Prompt。即使使用离线模拟LLM，消息类型的接口也与真实LLM一致，学完直接迁移到生产环境。

```python
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
# 调用LLM：llm.invoke([SystemMessage(content="..."), HumanMessage(content="...")])
```

**来源与验证**：
- PyPI：https://pypi.org/project/langchain-core/
- 已安装版本：langchain-core（2026-07-24验证通过）

---

## 主库 3：pydantic（状态schema验证）

**这是什么**：Python最流行的数据验证库，用Python类型注解定义数据schema，自动生成验证逻辑。

**为什么用它**：LangGraph的State可以用 `TypedDict`（轻量，本Phase用此）或Pydantic Model（带运行时验证）定义。企业级系统中，Pydantic Model提供更强的类型保证和错误提示。

```python
# 方式1：TypedDict（本Phase用此，LangGraph推荐）
from typing import TypedDict, Annotated
import operator
class AgentSystemState(TypedDict):
    brief: str
    messages: Annotated[list, operator.add]  # 追加模式

# 方式2：Pydantic Model（更强验证，企业级备选）
from pydantic import BaseModel
class AgentSystemStatePydantic(BaseModel):
    brief: str
    revision_count: int = 0
```

**来源与验证**：
- GitHub：https://github.com/pydantic/pydantic
- 已安装版本：pydantic 2.12.5（2026-07-24验证通过）

---

## 真实数据：Phase 2知识图谱（复用Capstone Phase 2产出）

**这是什么**：Capstone Phase 2（数据表示与知识图谱）产出的营销领域知识图谱，包含实体-关系-实体三元组，是本Phase researcher_agent的知识基础。

**为什么用它**：Capstone的整合性要求Phase 3调用Phase 2的数据层产出。researcher_agent通过读取知识图谱（模拟MCP工具调用），获得结构化的市场知识（人群/竞品/趋势/需求场景），而非凭空生成。

**知识图谱内容**（starter.ipynb / solution.ipynb中的 `knowledge_context` 变量）：

```
Phase 2知识图谱产出（实体->关系->实体）：
(智能运动手环)-[属于]->(可穿戴设备)
(智能运动手环)-[功能]->(心率监测)
(智能运动手环)-[功能]->(血氧检测)
(智能运动手环)-[功能]->(睡眠分析)
(心率监测)-[需求场景]->(运动健康管理)
(睡眠分析)-[需求场景]->(都市白领健康焦虑)
(竞品A)-[定位]->(极致性价比)
(竞品B)-[定位]->(专业运动)
(目标人群)-[特征]->(25-35岁都市白领)
(目标人群)-[痛点]->(亚健康焦虑)
(目标人群)-[渠道偏好]->(小红书种草)
```

**Capstone整合链路**：
- Phase 2产出知识图谱 -> Phase 3的researcher_agent读取 -> 产出市场研究 -> strategist制定策略 -> writer生成文案 -> Phase 4因果验证

**来源**：
- Capstone Phase 2目录：[`../day-phase-2-data-representation-knowledge-graph/`](../day-phase-2-data-representation-knowledge-graph/)
- 知识图谱构建参考（NetworkX）：https://networkx.org/documentation/stable/reference/generated/networkx.Graph.html

---

## 官方课程：LangChain Academy（已验证）

LangChain团队官方的LangGraph教学课程仓库，Module 0-6渐进式讲LangGraph，每个模块含Jupyter notebook + studio子目录。

- 课程网站：https://academy.langchain.com/
- GitHub仓库：https://github.com/langchain-ai/langchain-academy
- Module 1 `chain.ipynb`：https://github.com/langchain-ai/langchain-academy/blob/main/module-1/chain.ipynb （讲State与chain基础，直接对标本Phase TODO1和TODO5）

---

## 为什么不用伪代码 / 模拟框架（v4.0做法）

| 维度 | 伪代码 / 模拟框架（v4.0） | 真实LangGraph（v5.0） |
|------|--------------------------|----------------------|
| API细节 | 跳过，只讲概念 | 真实 `add_conditional_edges` / `interrupt_before` / `update_state` 签名 |
| 检查点机制 | 无 | `MemorySaver` 真实可用，支持暂停-恢复 |
| HITL | 纸上谈兵 | `interrupt_before` + 三步模式真实可跑 |
| Phase 2整合 | 无 | researcher_agent真实读取知识图谱上下文 |
| 版本跟进 | 随作者写死 | 跟LangGraph官方release |
| 可复用性 | 代码出了教室没用 | 学完直接上生产 |
| 社区支持 | 无 | 38k+ Star仓库 + LangChain Academy官方课 |

**真实即严谨** -- 这是v5.0的哲学增量。本Phase的编排逻辑（StateGraph/条件边/interrupt/Checkpointing）全部是真实LangGraph API；离线模拟LLM只固定了LLM返回值，聚焦编排学习。Phase 2知识图谱是真实结构化数据（实体-关系-实体三元组），非编造。

---

## 环境准备提示

```bash
pip install langgraph langchain-openai langchain-core pydantic
```

- 有 `OPENAI_API_KEY`：使用真实ChatOpenAI，LLM返回真实营销文案
- 无API key：自动降级为 `OfflineMockLLM`，返回固定营销文案，图端到端跑通
- 两种模式下，LangGraph编排逻辑（StateGraph/条件边/interrupt/Checkpointing）完全相同
