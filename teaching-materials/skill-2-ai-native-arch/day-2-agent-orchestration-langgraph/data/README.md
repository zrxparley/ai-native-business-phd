# Day 2 真实库与资源说明

> v5.0 核心：用**真实库 LangGraph + langchain-core + pydantic**（非伪代码/模拟框架）。真实库的 API 细节、检查点机制、条件边注册、interrupt 暂停-恢复，是伪代码学不到的。

---

## 主库 1：LangGraph（已验证，可运行）

**这是什么**：LangChain 团队官方推出的 Agent 编排框架，把 Agent 工作流建模为**有状态有向图**（StateGraph），原生支持条件路由、循环、状态持久化与人机交互（HITL）。生产级复杂 Agent 的事实标准。

**为什么用它**（企业架构视角）：
- 原生支持条件边（`add_conditional_edges`）和循环 -- 线性 Chain 框架做不到
- 内置 Checkpointing（`MemorySaver` / `SqliteSaver` / `PostgresSaver`），支持暂停-恢复与故障恢复
- 原生 `interrupt_before` 实现人机协同（HITL），企业 AI 治理的工程基础
- 图结构可视化 + 逐步执行 + 状态检查，生产级可调试性

**安装方式**（`pip install langgraph langchain-openai langchain-core`）：

```python
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
# interrupt_before 在 compile() 参数中使用，无需单独 import
```

**核心 API 速查**（本 Day 上机会用到）：

| API | 作用 | 本 Day 对应 |
|-----|------|------------|
| `StateGraph(State)` | 创建以 State 为全局状态的有向图 | `StateGraph(CampaignState)` |
| `workflow.add_node(name, fn)` | 添加节点（函数：State -> dict） | research/strategy/copywriter/approval/publish |
| `workflow.add_edge(a, b)` | 添加普通边（a 无条件到 b） | START->research->strategy->copywriter->approval |
| `workflow.add_conditional_edges(src, fn, mapping)` | 条件边（fn 读 State 返回键名） | approval -> route_after_approval -> {publish, revise} |
| `workflow.compile(checkpointer=, interrupt_before=)` | 编译为可执行图 | MemorySaver + interrupt_before=["approval"] |
| `graph.invoke(state, config)` | 执行图（到暂停点或终点） | Step 1: 执行到 approval 前暂停 |
| `graph.update_state(config, values)` | 更新检查点状态 | Step 2: 注入 approved=True |
| `graph.invoke(None, config)` | 从暂停点恢复执行 | Step 3: 恢复至完成 |
| `graph.get_state(config)` | 获取当前检查点状态 | 查看 .next（暂停位置）和 .values |

**来源与验证**：
- GitHub 仓库：https://github.com/langchain-ai/langgraph （MIT，"Build resilient agents"，已验证 2026-07-24）
- 官方文档：https://langchain-ai.github.io/langgraph/
- 已安装版本：langgraph 1.2.9（`pip install langgraph` 安装，2026-07-24 验证通过）

---

## 主库 2：langchain-core（消息类型）

**这是什么**：LangChain 的核心抽象层，提供 `HumanMessage` / `AIMessage` / `SystemMessage` 等消息类型，是所有 LangChain 生态框架（含 LangGraph）的基础。

**为什么用它**：LangGraph 节点调用 LLM 时，用消息类型构造 Prompt。即使使用离线模拟 LLM，消息类型的接口也与真实 LLM 一致，学完直接迁移到生产环境。

```python
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
# 调用 LLM：llm.invoke([SystemMessage(content="..."), HumanMessage(content="...")])
```

**来源与验证**：
- PyPI：https://pypi.org/project/langchain-core/
- 已安装版本：langchain-core 1.5.1（2026-07-24 验证通过）

---

## 主库 3：pydantic（状态 schema 验证）

**这是什么**：Python 最流行的数据验证库，用 Python 类型注解定义数据 schema，自动生成验证逻辑。

**为什么用它**：LangGraph 的 State 可以用 `TypedDict`（轻量，本 Day 用此）或 Pydantic Model（带运行时验证）定义。企业级系统中，Pydantic Model 提供更强的类型保证和错误提示。

```python
# 方式1：TypedDict（本 Day 用此，LangGraph 推荐）
from typing import TypedDict, Annotated
import operator
class CampaignState(TypedDict):
    brief: str
    messages: Annotated[list, operator.add]  # 追加模式

# 方式2：Pydantic Model（更强验证，企业级备选）
from pydantic import BaseModel
class CampaignStatePydantic(BaseModel):
    brief: str
    revision_count: int = 0
```

**来源与验证**：
- GitHub：https://github.com/pydantic/pydantic
- 已安装版本：pydantic 2.12.5（2026-07-24 验证通过）

---

## 官方课程：LangChain Academy（已验证）

LangChain 团队官方的 LangGraph 教学课程仓库，Module 0-6 渐进式讲 LangGraph，每个模块含 Jupyter notebook + studio 子目录。

- 课程网站：https://academy.langchain.com/
- GitHub 仓库：https://github.com/langchain-ai/langchain-academy
- Module 1 `chain.ipynb`：https://github.com/langchain-ai/langchain-academy/blob/main/module-1/chain.ipynb （讲 State 与 chain 基础，直接对标本 Day TODO1 和 TODO5）

---

## 为什么不用伪代码 / 模拟框架（v4.0 做法）

| 维度 | 伪代码 / 模拟框架（v4.0） | 真实 LangGraph（v5.0） |
|------|--------------------------|----------------------|
| API 细节 | 跳过，只讲概念 | 真实 `add_conditional_edges` / `interrupt_before` / `update_state` 签名 |
| 检查点机制 | 无 | `MemorySaver` 真实可用，支持暂停-恢复 |
| HITL | 纸上谈兵 | `interrupt_before` + 三步模式真实可跑 |
| 版本跟进 | 随作者写死 | 跟 LangGraph 官方 release（1.2.9） |
| 可复用性 | 代码出了教室没用 | 学完直接上生产 |
| 社区支持 | 无 | 38k+ Star 仓库 + LangChain Academy 官方课 |

**真实即严谨** -- 这是 v5.0 的哲学增量。本 Day 的编排逻辑（StateGraph / 条件边 / interrupt / Checkpointing）全部是真实 LangGraph API；离线模拟 LLM 只固定了 LLM 返回值，聚焦编排学习。

---

## 环境准备提示

```bash
pip install langgraph langchain-openai langchain-core pydantic
```

- 有 `OPENAI_API_KEY`：使用真实 ChatOpenAI，LLM 返回真实营销文案
- 无 API key：自动降级为 `OfflineMockLLM`，返回固定营销文案，图端到端跑通
- 两种模式下，LangGraph 编排逻辑（StateGraph/条件边/interrupt/Checkpointing）完全相同
