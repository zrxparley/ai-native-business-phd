# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：Capstone AI和商业分析 · Phase 3 Agentic系统架构
> **scratch 哲学**：不调 LangGraph StateGraph、不调 langchain，手写 Plan-Execute-Verify 状态机 + 验证门控，从 DFA 转移函数 + 几何停止概率直译到 numpy。

## scratch_topic

本单元 from-scratch 主题：**手写 agent 编排状态机（Plan-Execute-Verify 三阶段 + 验证门控 + 修订循环）**。对应 rohitg00 P19/24 Plan Execute Control Flow + P19/29 End to End Coding Task Demo。notes.md/starter.ipynb 用 `langgraph.StateGraph` + `add_conditional_edges` + `interrupt_before` + `MemorySaver` 构建 researcher->strategist->writer->review->publish 工作流，本层把"状态图 -> 转移函数 -> 门控判定 -> 循环退出"拆开：从确定性有限自动机（DFA）转移函数与几何停止概率出发，手写 numpy/python 实现 Plan-Execute-Verify 状态机，让"为什么修订 3 次后退出""验证门控如何决定分支"不再是 LangGraph 的黑箱，而是可逐行审计的状态转移逻辑。

## core_algorithm

Agent 编排的本质是确定性有限自动机（DFA）$M = (Q, \Sigma, \delta, q_0, F)$，其中状态集 $Q = \{\text{PLAN}, \text{EXECUTE}, \text{VERIFY}, \text{REVISE}, \text{ACCEPT}, \text{REJECT}\}$，输入字母表 $\Sigma = \{\text{pass}, \text{fail}, \text{max\_reached}\}$，初始状态 $q_0 = \text{PLAN}$，接受态 $F = \{\text{ACCEPT}\}$。转移函数 $\delta: Q \times \Sigma \to Q$ 定义为：

$$\delta(\text{PLAN}, \cdot) = \text{EXECUTE}, \quad \delta(\text{EXECUTE}, \cdot) = \text{VERIFY}$$
$$\delta(\text{VERIFY}, \text{pass}) = \text{ACCEPT}, \quad \delta(\text{VERIFY}, \text{fail}) = \text{REVISE}, \quad \delta(\text{REVISE}, \cdot) = \text{EXECUTE}$$

修订循环的退出条件由"最大修订次数 $K$"控制：当修订次数 $r \geq K$ 时，$\delta(\text{VERIFY}, \text{fail}) = \text{REJECT}$（而非 REVISE）。**验证门控** $V: \mathcal{O} \to \{0, 1\}$ 是一个二元谓词（如安全合规检查、质量阈值），输出 $V(o) = 1$ 表示通过。

**停止概率分析**：若每次执行通过验证的概率为 $p$（独立假设），则在最多 $K$ 次修订内被接受（进入 ACCEPT 态）的概率为：

$$P(\text{ACCEPT}) = 1 - (1-p)^{K}$$

这是几何分布的累积分布函数。期望修订次数 $\mathbb{E}[R] = \min(\text{Geom}(p), K)$，当 $p$ 小时需大 $K$ 才能保证 $P(\text{ACCEPT}) \to 1$。这是 HITL 审批节点 `revision_count >= 3` 退出条件的数学根基--选择 $K=3$ 意味着若单次通过率 $p=0.5$，接受概率 $1-0.5^3 = 0.875$；若 $p=0.3$，接受概率仅 $1-0.7^3 = 0.657$，需调大 $K$。手写时用 `dataclasses` 定义状态，`abc.ABC` 定义验证门控抽象基类，转移函数用字典编码 $\delta$。

## code_artifact

```python
import numpy as np
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import Any, Callable

STATES = ["PLAN", "EXECUTE", "VERIFY", "REVISE", "ACCEPT", "REJECT"]

@dataclass
class AgentState:
    plan: Any = None
    output: Any = None
    revision_count: int = 0
    max_revisions: int = 3
    history: list = field(default_factory=list)

class VerificationGate(ABC):
    @abstractmethod
    def check(self, output: Any, state: AgentState) -> bool:
        ...

class SafetyGate(VerificationGate):
    def __init__(self, forbidden: list):
        self.forbidden = forbidden
    def check(self, output, state):
        if not isinstance(output, str):
            return True
        return not any(w in output.lower() for w in self.forbidden)

def transition(state: AgentState, gate: VerificationGate,
               planner: Callable, executor: Callable) -> str:
    q = "PLAN"
    while q not in ("ACCEPT", "REJECT"):
        if q == "PLAN":
            state.plan = planner(state)
            q = "EXECUTE"
        elif q == "EXECUTE":
            state.output = executor(state)
            q = "VERIFY"
        elif q == "VERIFY":
            if gate.check(state.output, state):
                q = "ACCEPT"
            elif state.revision_count >= state.max_revisions:
                q = "REJECT"
            else:
                state.revision_count += 1
                q = "REVISE"
        elif q == "REVISE":
            state.output = executor(state)  # re-execute with feedback
            q = "VERIFY"
        state.history.append(q)
    return q

# verification_property:
#   FSM always terminates in {ACCEPT, REJECT}; ACCEPT requires gate.check==True;
#   REJECT occurs iff revision_count >= max_revisions and gate still fails.
if __name__ == "__main__":
    gate = SafetyGate(["spam", "scam"])
    calls = {"n": 0}
    def planner(s): return "draft plan"
    def executor(s):
        calls["n"] += 1
        return "clean output" if s.revision_count >= 1 else "spam output"
    s = AgentState(max_revisions=3)
    result = transition(s, gate, planner, executor)
    assert result == "ACCEPT", f"must ACCEPT after revision, got {result}"
    assert s.revision_count == 1, "one revision before clean output"
    # reject case: always fail
    fail_gate = SafetyGate(["output"])  # bans word 'output'
    s2 = AgentState(max_revisions=2)
    r2 = transition(s2, fail_gate, planner, executor)
    assert r2 == "REJECT", "must REJECT when gate always fails within max_revisions"
    assert s2.revision_count == 2
    # geometric stopping: P(ACCEPT) = 1-(1-p)^K
    p, K = 0.5, 3
    assert abs((1 - (1-p)**K) - 0.875) < 1e-9
```

**verification_property**: FSM 必然终止于 {ACCEPT, REJECT}（无死循环）；ACCEPT 当且仅当 gate.check 返回 True；REJECT 当且仅当 revision_count 达到 max_revisions 且验证仍失败；几何停止概率 $P(\text{ACCEPT}) = 1-(1-p)^K$ 数值验证（$p=0.5, K=3 \Rightarrow 0.875$）。

## connection_to_unit

1. **库 vs 手写的状态图**：notes.md 用 `langgraph.StateGraph` + `add_node` + `add_conditional_edges` + `compile(interrupt_before=...)` 装配图，from-scratch 版用 `transition()` 函数 + `while` 循环 + 字典状态编码--LangGraph 的 `StateGraph` 底层正是这样的转移函数，但暴露了 checkpoint persistence / streaming / parallel branches 等生产特性；from-scratch 版剥离这些，让"PLAN->EXECUTE->VERIFY->(ACCEPT|REVISE)"控制流可见。
2. **HITL interrupt 的本质**：starter.ipynb TODO5 用 `compile(interrupt_before=["review_node"])` 实现人机协作暂停，from-scratch 版没有 interrupt 原语--HITL 在状态机视角下是"VERIFY 态切换为人工 gate.check"，即把 `SafetyGate` 替换为 `HumanGate(input("approve? y/n"))`。这暴露了 HITL 的本质：验证门控的判定者从函数变为人。
3. **MemorySaver checkpointing 的简化**：notes.md 用 `MemorySaver` 持久化状态，from-scratch 版用 `AgentState` dataclass + `history` 列表--前者是序列化到存储（崩溃恢复），后者是内存轨迹（审计）。两者都服务于 Phase 4 因果评估的"可审计决策链"，但 from-scratch 版让"哪些字段需要 checkpoint"显式化（plan/output/revision_count 三字段即足够重放）。
4. **修订循环退出条件的数学化**：starter.ipynb TODO4 的 `route_after_review` 用 `if revision_count >= 3: return "publish"` 硬编码退出，from-scratch 版用几何分布 $P(\text{ACCEPT}) = 1-(1-p)^K$ 解释"为什么是 3 次"--让 $K$ 的选择从工程直觉变为可计算的接受概率权衡，这是 notes.md 作业"修订循环退出条件设成多少合理"的 from-scratch 回答。

## deep_dive_links

- [P19/24 Plan Execute Control Flow - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/19-capstone-projects/24-plan-execute-control-flow/README.md) - Plan-Execute 控制流，本单元 from-scratch 的架构锚点（DFA 转移函数 + 验证门控）
- [P19/29 End to End Coding Task Demo - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/19-capstone-projects/29-end-to-end-coding-task-demo/README.md) - 端到端演示，Plan-Execute-Verify 闭环的工程参考

## exercises

1. 在本单元 `starter.ipynb` TODO5（build_agent_system StateGraph 装配）运行后，用上面的 `transition()` 函数实现等价的 Plan-Execute-Verify 闭环，对比 LangGraph 版与 from-scratch 版的状态转移轨迹（`state.history` vs LangGraph 的 `graph.get_state_history()`）。提示：两者应走相同的 PLAN->EXECUTE->VERIFY->REVISE->EXECUTE->VERIFY->ACCEPT 序列。
2. 扩展 `VerificationGate`：实现一个 `QualityGate(threshold=0.7)` 用"输出长度/关键词覆盖度"作为质量分，当分数 < threshold 时 fail。对比 `SafetyGate`（硬规则）与 `QualityGate`（软阈值）对修订次数分布的影响。这对应 notes.md HITL 治理框架中"安全审查 vs 创意审核"的差异化门控。
3. 实现"并行 Execute"：把 EXECUTE 态拆为 EXECUTE_RESEARCH + EXECUTE_WRITE 并行（用 numpy 无法真并行，但可模拟 fork-join），观察总执行步数是否减少。这与 notes.md 的 A2A Agent 协作（多 Agent 通过 State 共享通信）对应。
4. TODO: 在 `practice.md` 的 drill 中，用本 from-scratch 的 `transition()` 替代 LangGraph 版本，把 feedback_rule 中的"HITL 三步（invoke->update_state->resume）"升级为"FSM 状态转移轨迹审计（history 列表完整记录 PLAN/EXECUTE/VERIFY/REVISE 序列）"。这是 starter.ipynb TODO6 run_capstone_hitl 的 from-scratch 版本。
