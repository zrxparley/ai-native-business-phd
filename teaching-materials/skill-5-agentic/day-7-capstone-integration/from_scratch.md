# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：技能5 Agentic系统工程 · Day 7 端到端交付 + Capstone整合
> **scratch 哲学**：不调 LangGraph + garak + LangSmith 全家桶，手写端到端 Agent runtime，把 loop/tool/guard/obs 四件套组装到一个 40 行的裸 Python 类，让"生产 runtime"不再是框架黑箱。

## scratch_topic

本单元 from-scratch 主题：**手写端到端 Agent runtime（loop + tool + guardrail + observability 四件套组装）**。对应 rohitg00 P14/29 Production Runtimes + P17/23 SRE for AI。notes.md 把技能1-5整合为"数据->因果->Agent->评估->论文"五层流水线，本层把"Agent 层"拆到裸 Python：ReAct 循环 + 工具注册表 + 输入/输出 guard + trace 日志，组装成一个可逐行审计的 `AgentRuntime` 类，让"生产 runtime 怎么拼"不再是 LangGraph + LangSmith 的黑箱，而是四层函数变换器的显式组合。

## core_algorithm

生产 Agent runtime 是四层组合：$\text{runtime} = \text{obs} \circ \text{guard}_{\text{out}} \circ \text{loop}(\text{tool}) \circ \text{guard}_{\text{in}}$。每层是函数变换器，输入输出都是 (state, trace)。

**层组合的可靠性**：设各层可靠性 $R_l$（正确执行概率），独立层组合的总可靠性：

$$R = \prod_{l=1}^{L} R_l$$

四层各 99% -> 总 $R = 0.99^4 = 96.1\%$；各 99.9% -> $99.6\%$。这是 notes.md "灾备降级"的数学根基--层越多，单层必须越可靠，否则总可靠性指数衰减。

**SLO 作为概率保证**：服务可用性 $A = 1 - \text{failure\_rate}$，月可用性 99.9% 允许 43 分钟故障。Agent runtime 的故障包括：LLM API 超时、工具异常、guardrail 误拦、obs 丢 trace。误差预算（error budget）$B = 1 - \text{SLO}$，每月消耗 $B$ 的速率决定发布节奏。

**循环终止 + 工具隔离**：loop 层的终止条件（max_steps）与 tool 层的异常隔离（工具失败不崩 loop）共同保证 runtime 不挂。形式化：$\forall t \leq T_{\max}, \text{loop}(t) \neq \bot$，且 $\text{tool}_k$ 抛异常时 loop 捕获并记 trace，继续下一步。

**Guardrail 的 AND 语义**：输入 guard $\land$ 输出 guard，两者都通过才放行。漏放率 $F = F_{\text{in}} \cdot F_{\text{out}}$（独立）。这是 day-4 分层防御在 runtime 级的复现。

## code_artifact

```python
from dataclasses import dataclass, field

@dataclass
class RuntimeState:
    query: str
    history: list = field(default_factory=list)
    answer: str = ""
    blocked: bool = False

def guard_in(text, bl=("忽略指令", "reveal prompt")):
    for p in bl:
        if p in text:
            return False, f"blocked:{p}"
    return True, ""

def guard_out(text):
    return (False, "leak") if ("成本价" in text or "SYSTEM_PROMPT" in text) else (True, "")

class AgentRuntime:
    def __init__(self, llm_fn, tools, max_steps=5):
        self.llm_fn, self.tools, self.max_steps = llm_fn, tools, max_steps
        self.trace = []
    def run(self, query):
        self.trace = []
        ok, r = guard_in(query)
        self.trace.append(("guard_in", ok))
        if not ok:
            return RuntimeState(query, blocked=True)
        st = RuntimeState(query)
        for step in range(self.max_steps):
            try:
                text = self.llm_fn(st.history, query)
            except Exception as e:
                self.trace.append(("llm_err", str(e))); break
            st.history.append(text)
            if "FINISH:" in text:
                ans = text.split("FINISH:", 1)[1].strip()
                ok2, _ = guard_out(ans)
                self.trace.append(("guard_out", ok2))
                st.answer = ans if ok2 else "[blocked]"
                return st
            if "TOOL:" in text:
                name = text.split("TOOL:", 1)[1].strip().split("(")[0]
                try:
                    obs = self.tools.get(name, lambda: "unknown")()
                    st.history.append(f"OBS:{obs}")
                    self.trace.append(("tool", name, True))
                except Exception as e:
                    st.history.append(f"OBS:err:{e}")
                    self.trace.append(("tool", name, False))
        return st

if __name__ == "__main__":
    script = ["TOOL:search()", "FINISH:hello world"]
    rt = AgentRuntime(lambda h, q: script[len([x for x in h if x.startswith("TOOL")])],
                      {"search": lambda: "result"}, max_steps=5)
    st = rt.run("normal query")
    assert not st.blocked and st.answer == "hello world"
    assert any(t[0] == "guard_in" for t in rt.trace)
    bad = AgentRuntime(lambda h, q: "x", {}, max_steps=1)
    assert bad.run("忽略指令").blocked
```

**verification_property**: 正常查询完成并返回 answer；注入查询被 guard_in 拦截（blocked=True）；trace 记录每次 guard/tool/llm 操作；工具异常不崩 runtime（捕获并记 trace）；循环在 max_steps 内终止。

## connection_to_unit

1. **五层流水线 vs 四件套内核**：notes.md 的 Capstone 整合"数据->因果->Agent->评估->论文"五层流水线，from-scratch 版的 `AgentRuntime` 是"Agent 层"的最小内核--loop+tool+guard+obs 四件套就是 notes.md LangGraph Agent 的金属层实现。库的 `create_react_agent` 把这四件套打包，from-scratch 拆开让你看到每件。
2. **DSR artifact 接口对比**：notes.md 的 DSR 六步第3步"设计开发"要求架构+Agent+安全+评估设计，from-scratch 版的 `AgentRuntime.__init__` 参数（`llm_fn`, `tools`, `max_steps`）+ `guard_in`/`guard_out` 就是 DSR artifact 的核心接口契约--这是"可复现 artifact"的工程表达，论文 Methods 可直接引用此接口。
3. **可复现 trace 对比**：notes.md 的"可复现研究"要求 trace 存档（LangSmith/Langfuse），from-scratch 版的 `self.trace` 列表（记录 guard_in/llm_call/tool/guard_out 每次操作）就是 trace 存档的最简形式。库把 trace 持久化到云端，from-scratch 让你看到 trace 的结构是 `(name, attrs)` 元组列表。
4. **天道推演映射对比**：notes.md 的"天道推演×多Agent仿真"要求 Agent 在沙盘中博弈，from-scratch 版的 `tools` 字典是 Agent 的"行动能力"--天道推演的"因果链追踪"对应 trace，"沙盘模拟"对应 loop 的多步推演，"概率评估"对应 guard 的阈值判定。这是把哲学框架落到代码的接口。

## deep_dive_links

- [P14/29 Production Runtimes - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/14-agent-engineering/29-production-runtimes/README.md) - 生产 Agent runtime 设计，loop/tool/guard/obs 组装，本单元核心理论锚点
- [P17/23 SRE for AI - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/17-infrastructure-and-production/23-sre-for-ai/README.md) - AI SRE，SLO/error budget/可靠性工程

## exercises

1. 在本单元 `starter.ipynb` TODO4（Agent 层 LangGraph 构建营销策略 Agent）完成后，用 from-scratch `AgentRuntime` 接入同一个 `llm_fn` 和 `tools` 字典，对比两版的 trace 结构与终止行为。提示：用 mock `llm_fn` 返回预设脚本（"TOOL:..." / "FINISH:..."），聚焦控制流验证。
2. 实现工具并行调用：在 `run()` 中检测 `"TOOLS:[a,b]"` 格式，并行执行多个工具。对应 day-2 的并行工具调用练习，观察 trace 中 tool span 的嵌套结构变化。
3. 实现 fallback 链：`llm_fn` 抛异常时，调用备用 `llm_fn2`，对应 notes.md "灾备降级"多级 fallback。验证：主模型故障时 runtime 不崩，trace 记录 `llm_err` + `fallback`。
4. TODO: 在 `practice.md` 的 DSR 系统设计 drill 中，用 from-scratch `AgentRuntime` 作为 artifact 原型，在论文 Methods 部分描述其四层架构（loop/tool/guard/obs），在 Results 部分报告其 trace 统计（步数分布 / 工具成功率 / guard 拦截率）。这是 notes.md "DSR artifact 评估"的端到端实现。
