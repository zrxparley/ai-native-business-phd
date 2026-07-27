# Day 2 真实库与资源说明

> v5.0 核心升级：用**真实库 LangGraph**（非伪代码/模拟框架）替代"自己造的编排逻辑"。真实库的 API 细节、检查点机制、条件边注册方式，是伪代码学不到的。

---

## 主库：LangGraph（已验证，可运行）

**这是什么**：LangChain 团队官方推出的 Agent 编排框架，把 Agent 工作流建模为**有状态有向图**（StateGraph），原生支持条件路由、循环、状态持久化与人机交互（HITL）。生产级复杂 Agent 的事实标准。

**为什么用它**：
- 38k★ GitHub，MIT License，LangChain 团队官方维护（非社区实验项目）
- 原生支持条件边（`add_conditional_edges`）和循环--这是线性 Chain 框架做不到的
- 内置 Checkpointing（`MemorySaver` / `SqliteSaver` / `PostgresSaver`），支持暂停-恢复
- 原生 `interrupt` 功能实现人机协作（HITL），无需额外工程

**安装方式**（需先 `pip install langgraph langchain-anthropic`）：

```python
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import interrupt, Command
```

**核心 API 速查**（本 Day 上机会用到）：

| API | 作用 |
|-----|------|
| `StateGraph(State)` | 创建以 State 为全局状态的有向图 |
| `workflow.add_node(name, fn)` | 添加节点（函数：State -> dict） |
| `workflow.add_edge(a, b)` | 添加普通边（a 无条件到 b） |
| `workflow.add_conditional_edges(src, fn, mapping)` | 添加条件边（fn 读 State 返回键名，mapping 映射到目标节点） |
| `workflow.compile(checkpointer=...)` | 编译图为可执行图 |
| `graph.stream(state, config, stream_mode="values")` | 流式执行，逐节点输出 State |
| `interrupt(value)` | 节点内暂停图，把 value 抛给调用方等待人工 ressume |
| `graph.get_state(config)` | 获取当前检查点状态 |

**来源与验证**：
- GitHub 仓库：https://github.com/langchain-ai/langgraph （38.0k★，MIT，"Build resilient agents"，已验证 2026-07-24）
- 官方文档：https://langchain-ai.github.io/langgraph/ （已验证可活，SPA 单页应用）
- LangChain 文档站：https://docs.langchain.com/oss/python/langgraph/overview （官方文档跳转目标）

---

## 官方课程：LangChain Academy（已验证，2.8k★）

**这是什么**：LangChain 团队官方的 LangGraph 教学课程仓库，Module 0-6 渐进式讲 LangGraph，每个模块含 Jupyter notebook + studio 子目录（可用 LangGraph Studio 可视化探索图）。

**为什么用它**：这是 LangGraph 的**官方权威教程**，比第三方博客更准、更全、更跟版本。Module 1 讲基础 chain，Module 4 讲工具与搜索，Module 6 讲部署。

**深链用法**：
- Module 1 `chain.ipynb`：https://github.com/langchain-ai/langchain-academy/blob/main/module-1/chain.ipynb （已验证存在，705 行，30.6 KB，讲 LangGraph 基础 chain 与 state）
- Module 0 基础设置：https://github.com/langchain-ai/langchain-academy/tree/main/module-0
- 配套网站（含视频）：https://academy.langchain.com/

**来源与验证**：
- GitHub 仓库：https://github.com/langchain-ai/langchain-academy （2.8k★，1.8k forks，MIT，"Introduction to LangGraph!"，已验证 2026-07-24）

---

## 第三方课程：HuggingFace Agents Course（已验证，30.4k★）

**这是什么**：HuggingFace 官方的 Agent 课程，4 个 unit 覆盖 agent 基础 + 三大框架（smolagents / **LangGraph** / LlamaIndex）+ agentic RAG + 结业认证项目。

**为什么用它**：30.4k★ 的超高人气课程，Apache-2.0 开源，其中 LangGraph 单元可与 LangChain Academy 互补（HF 视角更偏"框架对比"，LangChain 视角更偏"自家框架深度"）。

**深链用法**：
- 课程主页：https://hf.co/learn/agents-course
- GitHub 仓库：https://github.com/huggingface/agents-course （30.4k★，2.2k forks，Apache-2.0，已验证 2026-07-24）

---

## 为什么不用伪代码 / 模拟框架（v4.0 做法）

| 维度 | 伪代码 / 模拟框架（v4.0） | 真实 LangGraph（v5.0） |
|------|--------------------------|----------------------|
| API 细节 | 跳过，只讲概念 | 真实 `add_conditional_edges` / `interrupt` 签名 |
| 检查点机制 | 无 | `MemorySaver` / `SqliteSaver` 真实可用 |
| 版本跟进 | 随作者写死 | 跟 LangGraph 官方 release |
| 可复用性 | 代码出了教室没用 | 学完直接上生产 |
| 社区支持 | 无 | 38k★ 仓库 + LangChain Academy 官方课 |

**真实即严谨**--这是 v5.0 的哲学增量，与技能3 Day1 用真实 Lalonde/NSW 数据同一逻辑。

---

## 环境准备提示

本 Day 上机需安装：

```bash
pip install langgraph langchain-anthropic langchain-core
```

需要 `ANTHROPIC_API_KEY` 环境变量（或把 `ChatAnthropic` 替换为 `ChatOpenAI` + `OPENAI_API_KEY`）。若暂无 API Key，starter.ipynb 的 TODO 仍可填写--图可以编译（`compile`），只是 `stream` 执行需要 LLM 调用。
