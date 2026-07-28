# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：选修E1 Agentic AI · Day 2 Agent框架对比
> **scratch 哲学**：不调 LangGraph/CrewAI/AutoGen，手写三框架最小内核（StateGraph/Actor/Crew），同一营销任务跑三套抽象，让"框架选型"从 API 记忆变成计算模型对比。

## scratch_topic

本单元 from-scratch 主题：**手写三框架最小内核对比**（StateGraph 内核 / Actor 消息模型内核 / Role-based Crew 内核）。对应 rohitg00 P14/13 LangGraph Stateful Graphs + P14/14 AutoGen Actor Model + P14/15 CrewAI Role Based Crews。notes.md 用 LangGraph `StateGraph`/`create_react_agent` 真实运行 + CrewAI/AutoGen 静态 API 对比，本层把三大框架的"设计哲学"拆到三段各 10 行的裸 Python 内核：状态图 = 节点函数 + 路由器，Actor = 消息处理器 + 邮箱，Crew = 任务 DAG + 角色分配。同一营销任务（透肌精华竞品分析）跑过三套内核后，"Agent 即图 / Agent 即对话者 / Agent 即角色"不再是 API 文档的描述，而是可逐行审计的控制流差异。

## core_algorithm

三大 Agent 框架本质上是同一计算问题（多步状态转移）的三种抽象。将每个框架形式化为一个计算模型：

**1. StateGraph（LangGraph）**：Agent 工作流建模为有状态有向图 $G = (V, E, \delta, r)$，其中 $V$ 是节点集（处理函数），$E$ 是边集（控制流），$\delta: S \times V \to S$ 是状态转移函数（节点函数返回状态补丁），$r: S \times V \to V$ 是条件路由器。执行规则：

$$s_{t+1} = \delta(s_t, v_t), \quad v_{t+1} = r(s_{t+1}, v_t)$$

开发者显式定义图结构，路由器 $r$ 根据当前状态选择下一节点。LangGraph 的 `add_conditional_edges` 是 $r$ 的 API 封装，`compile()` 将 $G$ 编译为可执行 IR。

**2. Actor Model（AutoGen）**：Agent 建模为消息处理器 $\sigma_i: \text{msg} \to [\text{msg}]$。GroupChat 中，每条消息广播给所有 Actor，每个 Actor 产生回复列表。消息队列的演化为：

$$M' = M \setminus \{\text{msg}\} \cup \bigcup_{i=1}^{N} \sigma_i(\text{msg})$$

计算展开为一棵消息树，`max_round` 限制树的深度。AutoGen 的 `ConversableAgent` 是 $\sigma_i$ 的封装，`GroupChatManager` 管理消息队列 $M$ 的分发和终止。

**3. Role-based Crew（CrewAI）**：Agent 建模为角色 $R$ + 任务集 $T$ + 依赖 DAG $\prec$。任务 $t$ 在所有前驱完成时变为就绪：$\text{ready}(T) = \{t \in T \setminus \text{Done} \mid \text{prereq}(t) \subseteq \text{Done}\}$。每个任务绑定一个角色 $r(t)$，执行时上下文为前驱结果：$\text{ctx}(t) = \{d \mapsto \text{result}(d) \mid d \prec t\}$。CrewAI 的 `Task(context=[...])` 隐式定义 $\prec$，from-scratch 用 `deps` dict 显式表达。

三者的表达力等价（均可模拟图灵机），但认知负荷不同：StateGraph 要求开发者预先设计完整流程图（高控制力），Actor 要求设计消息协议（高灵活性），Crew 要求设计角色和依赖（高直觉性）。这就是 notes.md "选型不是哪个最好而是哪个最匹配"的数学根源。

## code_artifact

```python
from dataclasses import dataclass, field
from typing import Callable

def run_graph(nodes, router, state, max_steps=6):
    """Kernel 1: StateGraph - LangGraph-style nodes + conditional router."""
    cur, trace = "start", []
    for _ in range(max_steps):
        if cur == "END" or cur not in nodes: break
        patch = nodes[cur](state); state.update(patch)
        trace.append({"node": cur, "state": dict(state)})
        cur = router(state, cur)
    return state, trace

@dataclass
class Actor:
    """Kernel 2: Actor - AutoGen-style message handler."""
    name: str; handler: Callable; mailbox: list = field(default_factory=list)

def run_actors(actors, init_msg, max_round=3):
    log, pending = [], [(None, init_msg)]
    for r in range(max_round):
        if not pending: break
        _, msg = pending.pop(0)
        for a in actors:
            reps = a.handler(msg, a.name)
            log.append({"r": r, "actor": a.name, "out": reps})
            pending.extend([(a.name, x) for x in reps])
    return log

def run_crew(tasks, deps, roles, exec_fn, max_iter=6):
    """Kernel 3: Crew - CrewAI-style role-based task DAG scheduling."""
    done, trace = {}, []
    for _ in range(max_iter):
        ready = [t for t in tasks if t not in done and all(d in done for d in deps.get(t, []))]
        if not ready: break
        for t in ready:
            ctx = {d: done[d] for d in deps.get(t, [])}
            done[t] = exec_fn(t, roles[t], ctx); trace.append({"task": t, "role": roles[t]})
    return done, trace

if __name__ == "__main__":
    gn = {"start": lambda s: {"p": "299"}, "a": lambda s: {"c": "760"}, "w": lambda s: {"ok": 1}}
    gr = lambda s, c: "a" if c == "start" else "w" if c == "a" else "END"
    _, gt = run_graph(gn, gr, {"task": "透肌精华"})
    acts = [Actor("r", lambda m, n: ["299"] if "research" in m else []),
            Actor("s", lambda m, n: ["done"] if "299" in m else [])]
    al = run_actors(acts, "research")
    c_t, c_d, c_r = ["r", "a", "w"], {"a": ["r"], "w": ["a"]}, {"r": "调研", "a": "分析", "w": "撰写"}
    _, ctr = run_crew(c_t, c_d, c_r, lambda t, r, c: f"{r}完成{t}")
    assert len(gt) == 3 and al[0]["actor"] == "r" and len(ctr) == 3
```

**verification_property**: 三个内核在同一营销任务上跑通后各产出可审计的 trace -- `run_graph` 的 trace 长度 = 节点数（每步一个节点补丁），`run_actors` 的 log 按 round 分组（每轮广播给所有 actor），`run_crew` 的 trace 按 DAG 拓扑序排列（前驱任务先于后继出现）。三内核均在 max\_steps/max\_round/max\_iter 内终止。

## connection_to_unit

1. **StateGraph 对比**：solution.ipynb TODO3 用 LangGraph `StateGraph(PlanExecuteState)` + `add_node("plan", plan_fn)` + `add_conditional_edges("execute", should_continue, {...})` + `compile()` 构建 Plan-Execute 图，from-scratch `run_graph` 用 `nodes` dict + `router` lambda 实现等价控制流。LangGraph 的 `compile()` 将图编译为内部 IR（支持 checkpointing、streaming、human-in-the-loop），from-scratch 是裸 for 循环 -- 但核心抽象完全一致：节点函数返回状态补丁，路由器决定下一节点。notes.md "Agent 即图"的设计哲学在 from-scratch 中退去 API 外壳，显形为 $s_{t+1} = \delta(s_t, v_t), v_{t+1} = r(s_{t+1}, v_t)$ 这两行数学。
2. **Actor/GroupChat 对比**：notes.md 讲 AutoGen 用 `ConversableAgent(name, system_message)` + `GroupChat(agents, messages, max_round)` + `GroupChatManager(group_chat)` + `agent.initiate_chat(manager, message)`，from-scratch `Actor` 有 `name` + `handler`（消息 -> 回复列表），`run_actors` 用 FIFO 队列广播消息。关键差异：AutoGen 的 `GroupChatManager` 管理轮次和终止条件（可自定义 speaker selection），from-scratch 用简单的 `pending` 队列 + `max_round` 截断。notes.md 说 AutoGen"对话驱动可能导致执行效率低（Agent 间可能无限讨论）"，from-scratch 的 `max_round` 就是这一风险的直接代码体现。
3. **Crew/Task 对比**：solution.ipynb TODO5 用 CrewAI `Agent(role, goal, backstory)` + `Task(description, expected_output, agent, context=[...])` + `Crew(agents, tasks, process=Process.sequential)` 静态对比，from-scratch `run_crew` 用 `tasks` 列表 + `deps` dict + `roles` dict + `exec_fn`。CrewAI 的 `Task(context=[...])` 隐式定义依赖（context 列表中的 task 是前驱），from-scratch 用 `deps` dict 显式表达 DAG。notes.md "CrewAI 根据Task的context依赖自动编排执行顺序"在 from-scratch 中显形为 `all(d in done for d in deps.get(t, []))` 这一行拓扑就绪检查。
4. **同任务三内核的统一性**：solution.ipynb 用同一营销任务（透肌精华竞品分析）跑 LangGraph ReAct 和 Plan-Execute 两种模式，from-scratch 用同一任务跑三个内核。这揭示了 notes.md 四框架对比表未点明的深层事实：三大框架是同一计算原语（状态转移 + 控制流路由）的不同语法包装，"框架选型"本质上是选择与开发者心智模型匹配的抽象层，而非计算能力的差异。

## deep_dive_links

- [P14/13 LangGraph Stateful Graphs - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/14-agent-engineering/13-langgraph-stateful-graphs/README.md) - LangGraph 状态图 from scratch，`run_graph` 内核的理论锚点
- [P14/14 Autogen Actor Model - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/14-agent-engineering/14-autogen-actor-model/README.md) - AutoGen Actor 模型 from scratch，`Actor`/`run_actors` 内核的理论锚点
- [P14/15 CrewAI Role Based Crews - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/14-agent-engineering/15-crewai-role-based-crews/README.md) - CrewAI 角色化 Crew from scratch，`run_crew` 内核的理论锚点

## exercises

1. 在本单元 `starter.ipynb` TODO2（`create_react_agent`）和 TODO3（`StateGraph` Plan-Execute）运行后，用上面的 `run_graph` 接入同一个营销任务（透肌精华竞品分析），对比 LangGraph `StateGraph` 与 from-scratch `run_graph` 的节点/路由映射。提示：将 LangGraph 的 `plan_node`/`execute_node`/`should_continue` 映射为 `run_graph` 的 `nodes` dict + `router` lambda，用 mock 函数替代真实 LLM。
2. 扩展 `run_actors` 实现"定向消息"：当前所有 actor 收到同一条消息（广播），扩展为支持 `msg["to"]` 字段定向投递（只有匹配的 actor 处理）。对应 AutoGen `ConversableAgent.send()` 的点对点通信 vs `GroupChat` 的广播通信。观察定向消息对 `max_round` 和总消息数的影响。
3. 为 `run_crew` 添加"并行任务执行"：当 `ready` 列表有多个无依赖任务时，用 `itertools` 或手动并行执行（模拟，不调 threading）。对应 notes.md 讲的 CrewAI `process="hierarchical"` 的并行编排能力。对比并行 vs 顺序的总迭代数差异。
4. TODO: 在 `practice.md` Drill A1（StateGraph Plan-Execute 刻意练习）中，用 from-scratch `run_graph` 替代 LangGraph `StateGraph`，手动实现 `plan_node` + `execute_node` + `should_continue` 的三函数版本。这是 solution.ipynb TODO3 的 from-scratch 对照，让你看到 LangGraph `compile()` 背后的裸控制流 -- 对应 notes.md 天道推演节"Plan-Execute 的 Plan 错误传播到所有 Execute 步骤"在 from-scratch 中的因果链显形。
