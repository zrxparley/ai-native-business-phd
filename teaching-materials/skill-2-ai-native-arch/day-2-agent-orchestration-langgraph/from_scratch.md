# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：技能2 AI原生企业架构 · Day 2 Agent 编排架构 + LangGraph
> **scratch 哲学**：不调 LangGraph，手写 StateGraph 状态机 + 条件分支 + 修订循环，从有向图遍历直译到 numpy。

## scratch_topic

本单元 from-scratch 主题：**手写 StateGraph 有状态有向图 + 条件分支 + 修订循环退出**。对应 rohitg00 P14/13 LangGraph Stateful Graphs + P11/16 LangGraph State Machines。notes.md/starter.ipynb 用真实 LangGraph 1.x 的 `StateGraph`/`add_node`/`add_edge`/`add_conditional_edges`/`compile`/`invoke` API 装配营销 Agent 工作流，本层去 LangGraph 化：纯 numpy + typing 实现 StateGraph 类（节点函数 State->dict + 无条件边 + 条件路由 + 循环退出），让"有状态图遍历""条件分支""循环退出条件"三个概念在白板级代码中显形--不依赖 LangGraph 的 `TypedDict` + `Annotated[list, operator.add]` 抽象，手写 dict 合并让 State 的累积语义可见。

## core_algorithm

StateGraph 的核心是有状态有向图的遍历。给定图 $G = (V, E, E_c)$，其中 $V$ 是节点集（每个节点是 $\text{State} \to \text{dict}$ 的函数），$E: V \to V$ 是无条件边，$E_c: V \to (\text{State} \to \text{key}) \times (\text{key} \to V)$ 是条件边。状态转移：

$$s_{t+1} = s_t \uplus \delta_t, \quad \delta_t = v_t(s_t), \quad v_{t+1} = \begin{cases} E[v_t] & \text{if } v_t \in \text{dom}(E) \\ E_c[v_t].\text{map}(\text{router}(s_{t+1})) & \text{if } v_t \in \text{dom}(E_c) \\ \text{END} & \text{otherwise} \end{cases}$$

其中 $\uplus$ 是 dict 合并（后者覆盖前者），$\delta_t$ 是节点函数返回的增量。循环退出条件是条件路由返回终态键：

$$\text{exit}(s) \iff \text{router}(s) = \text{"publish"} \lor \text{rev}(s) \ge r_{\max}$$

执行迹 $\text{trace} = [v_0, v_1, \dots, v_T]$ 是图上的拓扑序遍历，条件边使迹可含重复节点（循环）。Checkpointing 把每步 $s_t$ 序列化使可恢复，from-scratch 版用 `state["__next__"]` 记录暂停点实现最简检查点。这是 LangGraph StateGraph 的数学本质：节点函数是纯函数（State -> delta），路由器是 State -> key 的分类器，合并+路由的交替就是图的遍历。修订循环 `copywriter -> approval -> copywriter` 的退出条件 `rev >= 3` 确保有界--若无退出条件，条件边回指形成死循环，这是 LangGraph 循环模式的第一陷阱。

## code_artifact

```python
import numpy as np
from typing import Callable

class StateGraph:
    def __init__(self):
        self.nodes = {}; self.edges = {}; self.cond = {}; self.entry = None
    def add_node(self, name, fn):
        self.nodes[name] = fn
        if self.entry is None: self.entry = name
    def add_edge(self, a, b): self.edges[a] = b
    def add_conditional_edges(self, node, router, mapping): self.cond[node] = (router, mapping)
    def compile(self, interrupt_before=None):
        self.interrupt = set(interrupt_before or []); return self
    def invoke(self, state, config=None):
        cur = state.pop("__next__", self.entry); trace = []
        while cur and cur != "END":
            if cur in getattr(self, "interrupt", set()):
                state["__next__"] = cur; return state, trace, "interrupted"
            delta = self.nodes[cur](state) or {}; state.update(delta); trace.append(cur)
            if cur in self.cond:
                r, m = self.cond[cur]; cur = m.get(r(state), "END")
            else: cur = self.edges.get(cur, "END")
        return state, trace, "done"

def research(s): return {"analysis": "audience", "scores": np.array([0.8, 0.6])}
def strategy(s): return {"plan": "pos"}
def copywriter(s):
    s["rev"] = s.get("rev", 0) + 1
    q = float(np.mean(s.get("scores", np.array([0.5]))))
    return {"copy": f"v{s['rev']}", "quality": q}
def approval(s): return {}
def route(s):
    if s.get("approved") or s.get("rev", 0) >= 3: return "publish"
    return "revise"

# verification_property: loop exits at rev>=3 or approved; quality is numpy mean of state vector
if __name__ == "__main__":
    g = StateGraph()
    for n, f in [("research", research), ("strategy", strategy), ("copywriter", copywriter), ("approval", approval), ("publish", lambda s: {"done": True})]:
        g.add_node(n, f)
    g.add_edge("research", "strategy"); g.add_edge("strategy", "copywriter"); g.add_edge("copywriter", "approval")
    g.add_conditional_edges("approval", route, {"publish": "publish", "revise": "copywriter"})
    g.compile()
    s, tr, st = g.invoke({})
    assert st == "done" and tr[-1] == "publish" and tr.count("copywriter") == 3
    assert 0.0 <= s["quality"] <= 1.0
```

**verification_property**: 修订循环在 `rev >= 3` 时退出（trace 含 3 次 `copywriter`，最后一次 approval 路由到 `publish`）；条件路由 `route(s)` 是 State -> key 的纯函数；`quality` 是 numpy 向量均值的标量化（`np.mean(scores)` 在 [0,1] 内）。

## connection_to_unit

1. **API 映射对比**：starter.ipynb 用 LangGraph 的 `StateGraph(CampaignState)` + `add_node` + `add_edge` + `add_conditional_edges` + `compile(checkpointer=MemorySaver())` 装配图，from-scratch 版用同名的 `StateGraph` 类但内部是纯 dict + while 循环遍历--LangGraph 的 `TypedDict` State + `Annotated[list, operator.add]` 追加模式被简化为 `state.update(delta)` 的 dict 合并，让"State 累积语义"（覆盖 vs 追加）在裸代码中可见。
2. **条件路由的裸实现**：starter.ipynb 的 `route_after_approval` 返回 `"publish"` 或 `"revise"` 字符串，LangGraph 的 `add_conditional_edges` 内部做 key->node 映射，from-scratch 版的 `self.cond[node] = (router, mapping)` + `m.get(r(state), "END")` 把这个映射暴露为查表操作--研究者能看到"条件边 = 路由函数 + 字典查表"的数学结构。
3. **循环退出的有界性**：notes.md 关键回顾 2 的"循环模式必须有退出条件（`revision_count >= 3`）"在 starter.ipynb 中是 `route_after_approval` 的一个 if 分支，from-scratch 版的 `route(s)` 函数把 `s.get("rev", 0) >= 3` 作为退出条件的唯一来源--去掉这行会死循环，这是 from-scratch 让"有界循环"的必要性可验证的方式。
4. **Checkpointing 的最简形态**：starter.ipynb 用 `MemorySaver` + `config={"configurable": {"thread_id": "1"}}` 实现检查点，from-scratch 版用 `state["__next__"]` 记录暂停节点--这是检查点的最简形态（单字段），让"Checkpointing = 序列化当前状态 + 记住下一个节点"的本质不被 LangGraph 的 thread_id/config 配置抽象遮蔽。

## deep_dive_links

- [P14/13 LangGraph Stateful Graphs - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/14-agent-engineering/13-langgraph-stateful-graphs/README.md) - LangGraph 状态图，本 from-scratch 单元 StateGraph 类的核心理论锚点
- [P11/16 LangGraph State Machines - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/16-langgraph-state-machines/README.md) - LLM 工程中的状态机，本单元条件分支 + 循环退出的状态机模型参考

## exercises

1. 在本单元 `starter.ipynb` TODO5（`build_campaign_graph` 装配 StateGraph）运行后，用上面的 from-scratch `StateGraph` 类重新装配同一营销工作流（research -> strategy -> copywriter -> approval -> publish/revise），对比 LangGraph 版与 numpy 版的执行迹 `trace`（应拓扑序一致，差异仅在 LLM 返回值）。提示：固定 `np.random.default_rng(0)` 使 `scores` 可复现。
2. 将 `route(s)` 的退出条件从 `rev >= 3` 改为 `rev >= 5`，观察 trace 中 `copywriter` 出现次数的变化。然后去掉退出条件（只留 `approved` 判断），验证死循环发生（加 `max_steps=100` 安全阀）。这与 notes.md 作业"修订循环退出条件设成多少合理"直接相关。
3. 为 from-scratch `StateGraph` 添加 `interrupt_before` 支持：在 `invoke` 中检查 `cur in self.interrupt` 时返回 `"interrupted"` 状态并把 `cur` 存入 `state["__next__"]`，实现 Day 3 HITL 的基础。对应 notes.md 关键回顾 2 的"人机协同（HITL）"编排模式。
4. TODO: 在 `practice.md` 的 D1 drill（StateGraph 装配）中，用 from-scratch 版替代 LangGraph 版完成 Worked 阶段示范，对比两者代码行数与可读性。这是本单元既有 TODO5 的 from-scratch 补充--理解 LangGraph 封装了什么、暴露了什么。
