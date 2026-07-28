# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：选修E1 Agentic AI · Day 3 多Agent系统设计
> **scratch 哲学**：不调 LangGraph/networkx，手写三种多Agent协调协议（supervisor/blackboard/contract net），让"协作拓扑"从 networkx 图论指标回到控制流本身。

## scratch_topic

本单元 from-scratch 主题：**手写三种多Agent协调协议**（supervisor 中心化路由 / blackboard 共享内存 / contract net 招标分配）。对应 rohitg00 P16/05 Supervisor Orchestrator Pattern + P16/07 Society of Mind Debate。notes.md 用 LangGraph `StateGraph` 构建 supervisor 中心化与 team 去中心化双拓扑 + networkx 分析度中心性，本层把多Agent协调拆到三种经典协议的裸 Python 实现：supervisor 是顺序分派 + 结果累积，blackboard 是共享内存 + 不动点收敛，contract net 是招标投标 + $\arg\max$ 分配。与 skill-5 day-1 的单 Agent ReAct 不同，e1 day-3 聚焦多 Agent 间的协调机制 --消息如何路由、状态如何共享、任务如何分配，这是多Agent系统设计的核心。

## core_algorithm

多Agent协调形式化 $N$ 个 Agent 如何 collectively 解决超出单 Agent 能力的任务。三种经典协调协议对应三种计算模型：

**1. Supervisor（中心化路由）**：supervisor $S$ 维护路由函数，按顺序将任务分派给专业 Agent。每步 agent $i$ 接收上下文 $c_t = \{\text{task}, R_t\}$（$R_t$ 为已累积结果），产出 $o_t = \text{fn}_i(c_t)$，结果累积 $R_{t+1} = R_t \cup \{i \mapsto o_t\}$。supervisor 是单点故障 --其度中心性 $C_D(S) = 1.0$，移除后拓扑崩溃。

**2. Blackboard（共享内存）**：所有 Agent 读写同一黑板 $BB$。Agent $i$ 在触发条件满足时写入 $BB_{t+1} = BB_t \cup \text{post}_i(BB_t)$。收敛需要不动点：

$$\exists T \geq 0: BB_T = BB_{T+1} \quad (\text{fixed point / no agent has new posts})$$

blackboard 拓扑是共享总线（所有 Agent 连接到 $BB$ 而非彼此），消除了 supervisor 瓶颈但引入收敛风险（若 Agent 持续触发则永不收敛）。

**3. Contract Net（招标分配）**：manager 宣布任务 $\tau$，每个 Agent $a_i$ 计算标 $b_i = \text{score}(a_i, \tau)$，中标者执行：

$$w = \arg\max_{i \in \{1,\ldots,N\}} \text{score}(a_i, \tau), \quad \text{result} = \text{exec}_w(\tau)$$

contract net 的拓扑在招标阶段是星型（所有 Agent 向 manager 投标），执行阶段是点对点（manager-winner），总通信开销 $O(N)$ 优于 supervisor 的 $O(N)$ 但无固定路由 --每次任务重新招标。

三种协议在控制力与自主性间权衡：supervisor 最大控制力但 $S$ 是瓶颈，blackboard 最大自主性但有非收敛风险，contract net 优化任务匹配但 $O(N)$ 招标开销。notes.md 的"拓扑选择决策树"本质上是这三种权衡的定性版本，from-scratch 让权衡在代码中显形。

## code_artifact

```python
from dataclasses import dataclass, field

# Protocol 1: Supervisor - centralized routing to specialist agents
def supervisor_route(agents, task, max_round=5):
    results, log = {}, []
    for i, a in enumerate(agents[:max_round]):
        out = a["fn"]({"task": task, "results": results})
        results[a["name"]] = out
        log.append({"agent": a["name"], "out": out})
        if out.get("done"): break
    return results, log

# Protocol 2: Blackboard - shared memory, agents react to state changes
@dataclass
class Blackboard:
    data: dict = field(default_factory=dict)
    def post(self, k, v): self.data[k] = v
    def read(self, k): return self.data.get(k)

def blackboard_loop(agents, bb, task, max_iter=5):
    bb.post("task", task); log = []
    for i in range(max_iter):
        prev = dict(bb.data); [a["fn"](bb) for a in agents]
        if bb.data == prev: break
        log.append({"i": i, "keys": list(bb.data.keys())})
    return bb.data, log

# Protocol 3: Contract Net - bidding-based task allocation
def contract_net(task, agents, bid_fn):
    bids = sorted([(a["name"], bid_fn(a, task)) for a in agents], key=lambda x: -x[1])
    w = bids[0][0]
    result = next(a["fn"]({"task": task}) for a in agents if a["name"] == w)
    return {"winner": w, "bids": bids, "result": result}

if __name__ == "__main__":
    mk = lambda n, f: {"name": n, "fn": f}
    ags = [mk("r", lambda c: {"info": "299"}), mk("s", lambda c: {"plan": "x"}), mk("w", lambda c: {"done": 1})]
    res, _ = supervisor_route(ags, "营销")
    bb = Blackboard()
    bags = [mk("r", lambda b: b.post("p", "299") if "p" not in b.data else None),
            mk("s", lambda b: b.post("st", "ok") if "p" in b.data else None)]
    _, blog = blackboard_loop(bags, bb, "透肌精华")
    cags = [mk("f", lambda c: {"t": 1}), mk("q", lambda c: {"t": 3})]
    cn = contract_net("写文案", cags, lambda a, t: 0.9 if a["name"] == "q" else 0.5)
    assert "w" in res and "st" in bb.data and cn["winner"] == "q"
```

**verification_property**: 三协议在同一营销任务上跑通 -- `supervisor_route` 顺序分派直到 `done`，结果累积在 `results` dict；`blackboard_loop` 迭代直到不动点（$BB_T = BB_{T+1}$），收敛后 `bb.data` 不再变化；`contract_net` 招标后 $\arg\max$ 中标者执行，`winner` 为最高分 Agent。三协议均在 max\_round/max\_iter 内终止。

## connection_to_unit

1. **supervisor 拓扑对比**：solution.ipynb TODO3 用 LangGraph `StateGraph(MultiAgentState)` + `add_node("supervisor", supervisor_node)` + `add_conditional_edges("supervisor", route_from_supervisor, {...})` 构建 supervisor 中心化拓扑，from-scratch `supervisor_route` 用列表枚举 + `out.get("done")` 终止。LangGraph 的 `route_from_supervisor` 函数根据 `current_agent` 状态字段路由（researcher->strategist->writer->reviewer->END），from-scratch 用列表顺序隐含路由 --但核心抽象一致：supervisor 按序分派，结果累积。notes.md "supervisor=因果链追踪（集中调度），星型拓扑可控但supervisor是单点故障"在 from-scratch 中显形为 `enumerate(agents[:max_round])` 这一行顺序分派。
2. **team 拓扑 vs blackboard 对比**：solution.ipynb TODO4 用 LangGraph `add_edge("researcher", "strategist")` 等直接边构建 team 去中心化拓扑（流水线式 Agent 间直接传递），from-scratch `blackboard_loop` 提供了另一种去中心化方案 --Agent 不直接通信而是通过共享 `Blackboard` 对象读写。notes.md 的"五种协作模式"未显式覆盖 blackboard 架构（它是经典 AI 架构但不在流水线/中心化/辩论/层级/自由协作五模式中），from-scratch 补充了这一模式。blackboard 的不动点收敛 $BB_T = BB_{T+1}$ 是 team 拓扑不具备的特性 --team 的流水线有固定终点，blackboard 靠状态不变检测收敛。
3. **共识机制 vs contract net 对比**：notes.md 讲三种共识机制（投票/权威/协商），solution.ipynb 的 supervisor 用固定顺序路由（权威机制的隐式版本 --supervisor 有终决权），from-scratch `contract_net` 实现了第四种协调机制 --市场招标。$w = \arg\max_i \text{score}(a_i, \tau)$ 让任务分配基于能力评分而非固定角色，这是 notes.md 五模式和三共识机制都未覆盖的协调范式。contract net 在 Agent 能力异构时优于固定路由（notes.md "researcher/strategist/writer/reviewer"角色固定，contract net 允许动态选最优执行者）。
4. **networkx 拓扑指标对比**：solution.ipynb TODO5 用 networkx `degree_centrality`/`betweenness_centrality`/`is_strongly_connected` 分析拓扑，from-scratch 三协议有结构不同的拓扑：supervisor 是星型（$C_D(\text{supervisor})=1.0$，其他 Agent $\approx 0.2$），blackboard 是共享总线（所有 Agent 连 $BB$ 不连彼此，$C_D(BB)=1.0$ 但 Agent 间 $C_D=0$），contract_net 是动态星型（招标阶段星型，执行阶段点对点）。notes.md "networkx 量化因果链追踪--哪个Agent是关键因果节点"在 from-scratch 中直接映射为 supervisor 的单点故障风险和 blackboard 的 $BB$ 瓶颈。

## deep_dive_links

- [P16/05 Supervisor Orchestrator Pattern - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/16-multi-agent-and-swarms/05-supervisor-orchestrator-pattern/README.md) - supervisor 编排模式 from scratch，`supervisor_route` 协议的理论锚点
- [P16/07 Society of Mind Debate - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/16-multi-agent-and-swarms/07-society-of-mind-debate/README.md) - Society of Mind 辩论拓扑，多Agent辩论收敛与 `blackboard_loop` 不动点的关系

## exercises

1. 在本单元 `starter.ipynb` TODO3（supervisor 中心化拓扑）运行后，用上面的 `supervisor_route` 接入同样的 4 个营销 Agent（researcher/strategist/writer/reviewer），对比 LangGraph `StateGraph` + `add_conditional_edges` 与 from-scratch 列表枚举的路由逻辑差异。提示：将 LangGraph 的 `route_from_supervisor` 映射为 from-scratch 的列表顺序，用 mock agent 函数替代真实 LLM。
2. 扩展 `blackboard_loop` 实现"优先级触发"：为每个 agent 添加 `trigger_fn(bb) -> bool` 条件，只有 trigger 满足时 agent 才执行 `fn(bb)`。对应 notes.md "条件路由"概念和天道推演"关键因果节点"识别。观察优先级顺序对收敛步数的影响 --若低优先级 agent 的输出是高优先级 agent 的 trigger 前提，顺序错误会导致假收敛。
3. 实现"合同网+supervisor 混合"协议：supervisor 用 `contract_net` 协议动态分配任务给最优 agent（每次分派前招标），而非固定顺序路由。对应 rohitg00 P16/05 Supervisor Orchestrator Pattern 的动态路由扩展。对比固定路由 vs 动态招标的总执行质量和通信开销 --这是 solution.ipynb 固定路由的 from-scratch 升级。
4. TODO: 在 `practice.md` Drill D-EMERGE-03（networkx 涌现分析）中，为 from-scratch 三协议添加"拓扑度量"：手写计算 supervisor/blackboard/contract\_net 三种协议的 Agent 间平均消息跳数（不调 networkx），对应 solution.ipynb TODO5 的 `nx.degree_centrality`。提示：supervisor 星型的平均跳数为 2（agent->supervisor->agent），blackboard 共享总线为 2（agent->BB->agent），contract\_net 招标阶段为 2（agent->manager->agent）但执行阶段为 1（manager->winner）。这是 solution.ipynb networkx 分析的 from-scratch 版本。
