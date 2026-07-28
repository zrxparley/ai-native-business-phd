# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：选修E1 Agentic AI · Day 1 Agent理论基础
> **scratch 哲学**：不调 LangChain/LangGraph/pydantic，手写 BDI（信念-愿望-意图）状态机，从 Bratman 的认知架构直译到纯 Python dataclass。

## scratch_topic

本单元 from-scratch 主题：**手写 BDI（Belief-Desire-Intention）推理循环状态机**。对应 rohitg00 P14/01 The Agent Loop。notes.md 用 LangChain `create_react_agent` + pydantic BDI Schema 构建 ReAct Agent，本层把 Bratman(1987)/Rao & Georgeff(1995) 的 BDI 认知架构拆到裸 Python：信念修订 -> 愿望生成 -> 意图承诺 -> 行动执行的四函数循环。与 skill-5 day-1 的 ReAct 手写不同，e1 day-1 聚焦 BDI 的"意图持续性"（intention persistence）--这是 ReAct 每步重规划所不具备的认知特性，让 Agent 不会因微小信念变化就放弃已承诺的计划。

## core_algorithm

BDI（Belief-Desire-Intention）是经典 Agent 认知架构（Bratman 1987，Rao & Georgeff 1995 形式化）。Agent 状态为三元组 $S_t = (B_t, D_t, I_t)$，其中 $B_t$ 是信念集（对世界的认知），$D_t$ 是愿望集（目标），$I_t$ 是意图队列（已承诺执行的计划）。推理循环由四个函数组成：

1. **信念修订**（Belief Revision）：$B_t = \text{BR}(B_{t-1}, \text{obs}_t)$ -- 将新观测 $\text{obs}_t$ 融入信念集
2. **愿望生成**（Option Generation）：$D_t = \text{options}(B_t, I_{t-1})$ -- 基于当前信念和已有意图生成候选愿望
3. **意图承诺**（Intention Commitment）：$I_t = \text{filter}(B_t, D_t, I_{t-1})$ -- 从愿望中选择并承诺执行
4. **行动执行**（Action Execution）：$a_t = \text{execute}(I_t)$ -- 从意图队列弹出下一个行动

循环往复：$\text{obs}_{t+1} = \text{env}(a_t)$，反馈到信念修订。BDI 的核心特性是**意图持续性**（intention persistence）--意图不会在每步被放弃，Agent 持续执行 $I_t$ 直到队列耗尽或信念修订使意图前提不满足。形式化：

$$I_t = \begin{cases} I_{t-1} \setminus \{\text{completed}\} & \text{if } B_t \models \text{precondition}(I_{t-1}) \\ \text{filter}(B_t, D_t, \emptyset) & \text{otherwise (replan)} \end{cases}$$

意图持续性防止"thrashing"--没有它，Agent 每步重新规划，永远无法完成多步任务。在营销 Agent 语境下，$B_t$ 包含产品/竞品知识，$D_t$ 是"生成营销策略"，$I_t$ 是 [search\_product, analyze\_competitor, write\_strategy, done] 步骤序列。ReAct 每步重规划（$I_t$ 每步由 LLM 重新生成），BDI 则承诺计划后持续执行--这是两种范式的本质差异。

## code_artifact

```python
from dataclasses import dataclass, field

@dataclass
class BDIState:
    belief: dict = field(default_factory=dict)
    desire: str = ""
    intention: list = field(default_factory=list)
    cursor: int = 0

def revise(belief, obs):
    """Belief revision: B_t = BR(B_{t-1}, obs_t)."""
    belief.update(obs)
    return belief

def bdi_loop(state, perceive, plan, execute, max_iter=6):
    """BDI cycle: perceive -> revise belief -> (re)plan -> execute."""
    trace = []
    for t in range(max_iter):
        obs = perceive(state)
        state.belief = revise(state.belief, obs)
        if state.cursor >= len(state.intention):
            state.intention = plan(state.belief, state.desire)
            state.cursor = 0
        if state.cursor >= len(state.intention):
            break
        action = state.intention[state.cursor]
        result = execute(action, state)
        state.cursor += 1
        trace.append({"t": t, "B": dict(state.belief), "a": action, "obs": result})
        if action == "done" or "done" in str(result).lower():
            break
    return state, trace

if __name__ == "__main__":
    db = {"product": "透肌精华299元", "competitor": "雅诗兰黛760元", "write": "策略已写入", "done": "done"}
    def perceive(s):
        for k in ["product", "competitor"]:
            if k not in s.belief:
                return {k: db[k]}
        return {"done": True}
    plan = lambda b, d: ["query_product", "query_competitor", "write", "done"]
    def execute(a, s):
        key = a.replace("query_", "") if a.startswith("query_") else a
        return db.get(key, "done")
    s = BDIState(desire="营销策略")
    final, trace = bdi_loop(s, perceive, plan, execute)
    assert len(trace) <= 6, "terminate within max_iter"
    assert "product" in trace[0]["B"], "belief revised after first perception"
    assert trace[-1]["a"] == "done", "reached terminal action"
```

**verification_property**: bdi\_loop 在 max\_iter 内终止；每步先修订信念再执行意图（$B_t$ 在 action 前更新）；意图持续性体现在 cursor 推进而非每步 replan（$I_t$ 仅在耗尽时重新生成）；trace 记录每步的 $(B_t, a_t, \text{obs}_t)$ 三元组。

## connection_to_unit

1. **BDI Schema 对比**：notes.md TODO1 用 pydantic `BaseModel` 定义 Belief/Desire/Intention 三模型（带 `Field` 校验和 `description`），from-scratch 用 `@dataclass` 定义 `BDIState` -- pydantic 提供运行时类型校验和 JSON schema 导出，dataclass 轻量但无校验。BDI 的语义结构（belief=世界认知/desire=目标/intention=计划）在两版中完全一致，但 from-scratch 把信念修订 `revise()` 和意图推进 `cursor++` 显式化为独立函数，而 pydantic 版只定义静态 Schema 不含推理循环。
2. **推理循环对比**：solution.ipynb TODO3 用 LangGraph `create_react_agent` 构建 ReAct Agent（每步由 LLM 重新生成 thought-action），from-scratch 的 `bdi_loop` 实现 BDI 的"先承诺计划再持续执行"--这是 ReAct 与 BDI 的本质差异：ReAct 的 $I_t$ 每步由 LLM 生成（无持续性），BDI 的 $I_t$ 在 `cursor >= len(intention)` 时才重新规划（有持续性）。notes.md 的"关键回顾 2"讲 BDI 的"Intention 的坚持性"，from-scratch 让这个抽象概念在 `cursor` 变量上显形。
3. **Plan-Execute 对比**：solution.ipynb TODO6 用 `StateGraph` 实现 Plan-Execute（plan\_node 一次性规划 + execute\_node 顺序执行），结构上类似 BDI 的 deliberate-then-execute，但 Plan-Execute 执行阶段不检查信念变化（盲执行整个 plan），BDI 每步先 `revise(belief, obs)` 再执行--如果观测使意图前提不满足，BDI 会触发 replan。这是 notes.md 天道推演节"Plan-Execute 的 Plan 错误传播到所有 Execute 步骤"的 from-scratch 修复方案。
4. **记忆机制对比**：solution.ipynb TODO5 用 LangGraph `MemorySaver` 按 `thread_id` 隔离会话（checkpointer 持久化），from-scratch 的 `belief` dict 就是短期记忆的最简形式--每个会话对应一个 `BDIState` 实例，信念集随感知更新。MemorySaver 的 `thread_id` 对应 from-scratch 中维护多个 `BDIState` 实例的字典 key，长期记忆需外接向量库（本 from-scratch 不实现）。

## deep_dive_links

- [P14/01 The Agent Loop - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/14-agent-engineering/01-the-agent-loop/README.md) - agent loop from scratch，BDI 推理循环的理论锚点（perceive-revise-plan-execute 四阶段）
- [P14/03 Reflexion Verbal RL - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/14-agent-engineering/03-reflexion-verbal-rl/README.md) - Reflexion 自我反思，BDI intention revision 的扩展（执行后自我批评触发 replan）

## exercises

1. 在本单元 `starter.ipynb` TODO1（pydantic BDI Schema）运行后，用上面的 `bdi_loop` 接入同一个营销任务（透肌精华竞品分析），对比 pydantic BDI Schema 与 dataclass BDIState 的状态管理差异。提示：用 mock `perceive`/`plan`/`execute` 替代真实 LLM，聚焦信念修订与意图推进的验证。
2. 扩展 `bdi_loop` 实现"intention reconsideration"：在每步执行前检查信念是否仍支持当前 intention 的前提（`precondition_fn(belief, intention[cursor]) -> bool`），若不支持则触发 re-deliberate。对应 Rao & Georgeff (1995) 的 intention persistence vs reconsideration 平衡。观察 reconsideration 频率对总步数的影响。
3. 实现"Reflexion"变体：在 BDI cycle 的 `done` 前，加一个 `critic` 步骤对整个 trace 进行自我批评，若评分低于阈值则清空 intention 重新规划。对应 rohitg00 P14/03 Reflexion Verbal RL 和 notes.md 讲的"评估者-优化者"循环。这是 from-scratch 实现 solution.ipynb TODO4 中"天道推演因果链分析"的代码化。
4. TODO: 在 `practice.md` Drill 1（BDI Schema 刻意练习）中，为本 from-scratch 实现添加"信念版本化"：每次 `revise` 时保留旧信念快照（`belief_history` 列表），支持回溯到任意历史信念状态。这是 solution.ipynb 的 pydantic BDI 未实现的功能，from-scratch 让你显式实现信念历史轨迹--对应天道推演的"反馈学习"能力。
