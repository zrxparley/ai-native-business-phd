# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：技能5 Agentic系统工程 · Day 2 LangGraph编排实战
> **scratch 哲学**：不调 LangGraph，手写 StateGraph 状态机 + 条件路由，从有向图状态转移到金属层。

## scratch_topic

本单元 from-scratch 主题：**手写 StateGraph 状态机 + 条件分支路由**。对应 rohitg00 P14/13 LangGraph Stateful Graphs + P14/12 Anthropic Workflow Patterns。notes.md 用 LangGraph `StateGraph`/`add_conditional_edges`/`MemorySaver` 装配"分析→策略→内容→审核→发布"工作流，本层把"有状态有向图"拆到裸 Python：节点函数表 + 邻接表 + 条件路由 + 状态合并 + 终止判定，让"图怎么走"不再是 LangGraph 的黑箱，而是 30 行可逐行审计的图执行引擎。

## core_algorithm

StateGraph 把 Agent 工作流建模为有状态有向图 $G=(V,E)$。节点是函数 $n_v: S \to \Delta S$（返回对状态的偏更新），边分两种：无条件边 $e=(u,v)$ 与条件边 $e=(u,v,r)$，其中 $r: S \to \text{Label}$ 是路由函数。执行是一步状态转移：

$$s_{t+1} = s_t \oplus n_{v_t}(s_t), \quad v_{t+1} = \text{route}(s_{t+1}, \text{edges}(v_t))$$

其中 $\oplus$ 是字段级 merge（`state.update(update)`），$v_t$ 是当前节点。条件路由从 $v_t$ 的出边中选第一条满足 $r(s)=\text{label}$ 的边。终止条件是路由到 $\text{END}$。

**终止性定理**：若图中每个环路 $C$ 都存在一个节点 $v \in C$，其更新使某单调不减字段 $f$ 严格递增，且路由函数在 $f \geq N$ 时强制返回 $\text{END}$，则执行在有限步内终止，上界为：

$$T_{\max} = \sum_{C \in \text{cycles}(G)} |C| \cdot N_C$$

这是 notes.md "任何循环都必须有退出条件"的数学根基--`revision_count` 就是这个单调字段 $f$，`should_approve` 在 $f \geq 3$ 时返回 `"publish"`（即 END 路径）。没有这个字段，图可能陷入无限循环。这也是 LangGraph `MemorySaver` 检查点的必要性：执行到第 $t$ 步崩溃，可从 $s_t$ 恢复而非从 $s_0$ 重算，代价是 $O(|s_t|)$ 的序列化开销。

## code_artifact

```python
class StateGraph:
    def __init__(self):
        self.nodes = {}
        self.edges = []  # (src, dst, cond_fn, rv)
    def add_node(self, name, fn):
        self.nodes[name] = fn
    def add_edge(self, src, dst):
        self.edges.append((src, dst, None, None))
    def add_conditional_edges(self, src, cond_fn, mapping):
        for rv, dst in mapping.items():
            self.edges.append((src, dst, cond_fn, rv))
    def run(self, init, max_steps=20):
        state = dict(init)
        cur = "START"
        hist = []
        adj = {}
        for src, dst, cf, rv in self.edges:
            adj.setdefault(src, []).append((dst, cf, rv))
        for _ in range(max_steps):
            if cur == "END" or cur not in adj:
                return state, hist
            if cur in self.nodes:
                upd = self.nodes[cur](state)
                if upd:
                    state.update(upd)
                hist.append((cur, dict(state)))
            nxt = None
            for dst, cf, rv in adj[cur]:
                if cf is None or cf(state) == rv:
                    nxt = dst
                    break
            if nxt is None:
                return state, hist
            cur = nxt
        return state, hist

if __name__ == "__main__":
    g = StateGraph()
    g.add_node("content", lambda s: {"rev": s.get("rev", 0) + 1})
    g.add_node("review", lambda s: {})
    g.add_edge("START", "content")
    g.add_edge("content", "review")
    g.add_conditional_edges("review",
        lambda s: "publish" if s.get("rev", 0) >= 3 else "revise",
        {"publish": "END", "revise": "content"})
    final, hist = g.run({"rev": 0}, max_steps=15)
    assert final["rev"] == 3, "exit when rev>=3"
    assert len(hist) == 6, "3 content+3 review visits"
```

**verification_property**: StateGraph.run 在 max_steps 内终止；revision_count 单调递增且到 3 时路由到 END；history 记录每次节点访问的 state 快照（可回放，等价于最简 checkpoint）。

## connection_to_unit

1. **图装配 vs 裸装配**：notes.md 用 `workflow.add_node`/`add_edge`/`add_conditional_edges`/`compile` 四步装配 LangGraph 图，from-scratch 版把这四步直译为 `StateGraph` 类的四个方法--`compile` 在 LangGraph 里做图校验（拓扑排序、悬空边检测），from-scratch 版省略校验直接在 `run` 里按邻接表走，暴露了"compile 实际在做什么"。
2. **状态合并语义**：notes.md 强调 `Annotated[list, operator.add]` 让 messages 字段累加而非覆盖，from-scratch 版的 `state.update(upd)` 是默认覆盖语义--要复现 `operator.add` 累加需在 merge 时按字段类型分发（本 from-scratch 留作练习）。这暴露了 LangGraph 的 reducer 机制：每个字段可定义自己的合并函数。
3. **条件路由对比**：notes.md 的 `should_approve(state) -> Literal["publish","revise"]` 配合 `add_conditional_edges("review", should_approve, {...})`，from-scratch 版把这两步合一：条件函数返回值与 mapping 中的 label 匹配即选边。库隐藏了"label 匹配是顺序扫描"这一事实--from-scratch 让你看到路由是 $O(\text{out-degree})$ 的线性扫描。
4. **检查点对比**：notes.md 的 `MemorySaver` 把 State 序列化到内存/SQLite，from-scratch 版的 `hist` 列表是检查点的最简形式（每次访问存 `dict(state)` 深拷贝）。LangGraph 的 `thread_id` 隔离对应这里 `run` 的局部 `state` 变量--每个 thread 是一次独立 `run` 调用。

## deep_dive_links

- [P14/13 LangGraph Stateful Graphs - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/14-agent-engineering/13-langgraph-stateful-graphs/README.md) - 状态图从零构建，本单元核心理论锚点
- [P14/12 Anthropic Workflow Patterns - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/14-agent-engineering/12-anthropic-workflow-patterns/README.md) - 工作流模式（prompt chaining / routing / evaluator-optimizer）

## exercises

1. 在本单元 `starter.ipynb` TODO5（`build_marketing_graph` 装配）完成后，用上面的 `StateGraph` 重新装配同一个"分析→策略→内容→审核→发布"图，对比两版的节点函数签名与条件路由逻辑。提示：notes.md 的 `should_approve` 可直接复用为 `add_conditional_edges` 的 cond_fn。
2. 为 `StateGraph` 添加 `compile` 方法做图校验：检测悬空边（指向不存在节点）、不可达节点（从 START BFS 不到）、无退出条件的环（DFS 找环且环内无单调字段）。这是 LangGraph compile 的核心职责，from-scratch 让你显式实现。
3. 实现 reducer 机制：`add_node` 时允许声明字段的合并函数（覆盖 vs 累加），对应 notes.md 的 `Annotated[list, operator.add]`。验证：连续两个节点都写 `messages` 列表时，默认覆盖会丢消息，reducer=append 则保留。
4. TODO: 在 `practice.md` 的条件路由 drill 中，把 `revision_count >= 3` 改为动态阈值（根据审核评分置信度调整），用 from-scratch `StateGraph` 观察终止步数分布。这是 notes.md "退出条件设成多少合理"的可量化回答。
