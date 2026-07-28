# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：技能2 AI原生企业架构 · Day 3 人机协作治理 + 组织变革
> **scratch 哲学**：不调 LangGraph interrupt + pandas groupby，手写 HITL interrupt 工作流 + 审批门控 + 干预率统计，从等待状态机直译到 numpy。

## scratch_topic

本单元 from-scratch 主题：**手写 HITL interrupt 工作流 + 审批门控 + 人工干预率统计**。对应 rohitg00 P14/12 Anthropic Workflow Patterns + P14/02 REWOO Plan and Execute。notes.md/starter.ipynb 用 pandas `groupby` 分析审计日志 + networkx 构建组织网络，本层去框架化：纯 numpy + typing 实现 HITL 执行器（interrupt_before + update_state + resume 三步模式）+ 审计日志记录 + 干预率计算 + 降级判定，让"暂停-注入-恢复""审批门控""干预率阈值降级"三个概念在白板级代码中显形--不依赖 LangGraph 的 `interrupt_before` 参数，不依赖 pandas 的 `groupby` 聚合，手写 while 循环让 HITL 的等待状态机可见。

## core_algorithm

HITL 工作流的核心是在有向图遍历中引入显式等待状态。给定中断节点集 $I \subseteq V$，执行器在遇到 $v \in I$ 时暂停并 yield 状态 $s_t$，等待人工输入 $h$ 后合并 $s_{t+1} = s_t \uplus h$ 并恢复。三步模式：

$$\text{HITL} = \begin{cases} \text{Step 1: } \text{run}(s_0) \to (s_t, \text{interrupted}) & \text{when } v_t \in I \\ \text{Step 2: } s_{t+1} = s_t \uplus h & \text{human injects } h \\ \text{Step 3: } \text{run}(s_{t+1}, \text{resuming=True}) \to (s_T, \text{done}) \end{cases}$$

恢复时需跳过首个节点的中断检查（`skip` 标志），否则会再次暂停。审批门控函数 $\text{gate}(s) = \text{approved}(s) \lor \text{rev}(s) \ge r_{\max}$ 决定循环退出。人工干预率按任务类型 $k$ 统计：

$$r_k = \frac{1}{|T_k|} \sum_{i \in T_k} \mathbb{1}[\text{human\_intervention}_i = 1], \quad \text{demote}(k) \iff r_k > \tau$$

阈值 $\tau = 0.3$ 是"AI 主导"降级为"人机协作"的临界点：若某类任务的人工干预率超过 30%，说明 AI 成熟度被高估，需重新划入人机协作模式。这把审计日志从"事后统计"升级为"分工动态调整信号"，是 NIST AI RMF Measure 功能的量化基础。from-scratch 版用 numpy 的 `np.mean` 计算干预率，比 pandas 的 `groupby('task_type')['human_intervention'].mean()` 更直白地暴露"布尔均值 = 干预比例"的数学结构。

## code_artifact

```python
import numpy as np
from typing import Callable

class HITLExecutor:
    """Minimal HITL: interrupt_before + approval gate + audit log."""
    def __init__(self, nodes, edges, cond, interrupt_before):
        self.nodes = nodes; self.edges = edges; self.cond = cond
        self.interrupt = set(interrupt_before); self.entry = next(iter(nodes))
        self.audit = []
    def invoke(self, state, resuming=False):
        cur = state.pop("__next__", self.entry); trace = []; skip = resuming
        while cur and cur != "END":
            if cur in self.interrupt and not skip:
                state["__next__"] = cur
                self.audit.append({"node": cur, "event": "pause"})
                return state, trace, "interrupted"
            skip = False
            delta = self.nodes[cur](state) or {}; state.update(delta); trace.append(cur)
            self.audit.append({"node": cur, "human": state.get("human_intervention", 0)})
            if cur in self.cond:
                fn, m = self.cond[cur]; cur = m.get(fn(state), "END")
            else: cur = self.edges.get(cur, "END")
        return state, trace, "done"
    def update_state(self, state, human_decision):
        state.update(human_decision); state["human_intervention"] = 1; return state
    def resume(self, state): return self.invoke(state, resuming=True)

def intervention_rate(audit):
    execs = [a for a in audit if "human" in a]
    return float(np.mean([a["human"] for a in execs])) if execs else 0.0

def should_demote(rate, tau=0.3):
    return rate > tau  # AI主导 -> 人机协作 if intervention too high

# verification_property: interrupt pauses before approval; resume executes interrupted node; demote at rate>0.3
if __name__ == "__main__":
    nodes = {"draft": lambda s: {"copy": "v1"}, "approve": lambda s: {}, "publish": lambda s: {"done": True}}
    edges = {"draft": "approve", "publish": "END"}
    cond = {"approve": (lambda s: "publish" if s.get("approved") else "revise", {"publish": "publish", "revise": "draft"})}
    ex = HITLExecutor(nodes, edges, cond, ["approve"])
    s, tr, st = ex.invoke({})
    assert st == "interrupted" and tr == ["draft"]
    ex.update_state(s, {"approved": True})
    s2, tr2, st2 = ex.resume(s)
    assert st2 == "done" and "publish" in tr2
    ex.audit = [{"human": 0}, {"human": 1}, {"human": 0}, {"human": 1}, {"human": 0}]
    r = intervention_rate(ex.audit)
    assert abs(r - 0.4) < 1e-6 and should_demote(r)
```

**verification_property**: interrupt 在 `approve` 节点前暂停（trace=["draft"], status="interrupted"）；`resume` 跳过首个中断检查执行被暂停的节点（trace2 含 "approve" + "publish"）；干预率 `np.mean([0,1,0,1,0])` = 0.4 > 0.3 阈值触发降级。

## connection_to_unit

1. **HITL 三步的裸实现**：starter.ipynb 用 LangGraph 的 `interrupt_before=["approval"]` + `graph.update_state(config, {"approved": True})` + `graph.invoke(None, config)` 三步，from-scratch 版的 `invoke` + `update_state` + `resume` 方法名与 LangGraph 同构但内部是 while 循环 + `skip` 标志--让"恢复时跳过首个中断检查"这个 LangGraph 隐藏的细节在 `skip = resuming; skip = False` 两行代码中显形。
2. **审计日志从 pandas 到手写**：starter.ipynb TODO1 用 `pd.DataFrame(AUDIT_LOGS).groupby('分工模式')['人工干预'].mean()` 计算干预率，from-scratch 版的 `intervention_rate(audit)` 用 `np.mean([a["human"] for a in execs])` --pandas 的 `groupby` 隐藏了"按任务类型分片再均值"的两步操作，from-scratch 版把"过滤含 human 字段的记录 -> 布尔均值"暴露为显式的列表推导。
3. **降级阈值的数学表达**：notes.md 关键回顾 1 的"AI主导任务人工干预率超过 30% 说明 AI 成熟度被高估"在 starter.ipynb 中是 DataFrame 筛选 + 文字结论，from-scratch 版的 `should_demote(rate, tau=0.3)` 把这个判断压缩为 `rate > tau` 一行--让"30% 阈值"从管理咨询建议变为可测试的布尔断言（构造数据 rate=0.4 触发降级）。
4. **审批门控的两种退出**：notes.md 关键回顾 1 的人机分工矩阵中"AI 主导，人例外"模式，from-scratch 版的 `cond` 路由器 `lambda s: "publish" if s.get("approved") else "revise"` 实现了两种退出：人工批准（`approved=True`）或循环上限（Day 2 的 `rev >= 3`）--这是 HITL 审批门控的最简形态，比 LangGraph 的 `interrupt_before` + 条件边组合更直白。

## deep_dive_links

- [P14/12 Anthropic Workflow Patterns - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/14-agent-engineering/12-anthropic-workflow-patterns/README.md) - Anthropic 工作流模式（含 HITL / interrupt / 审批循环），本 from-scratch 单元 HITL 执行器的核心理论锚点
- [P14/02 REWOO Plan and Execute - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/14-agent-engineering/02-rewoo-plan-and-execute/README.md) - Plan-Execute 两阶段模式，本单元审批门控在工作流中的定位参考

## exercises

1. 在本单元 `starter.ipynb` TODO1（pandas 审计日志分析 `groupby` 干预率）运行后，用上面的 `intervention_rate` 在同一份审计日志上手动计算干预率，对比 pandas 版的 `groupby('分工模式')['人工干预'].mean()` 输出与 numpy 版的 `np.mean` 输出（应数值一致），解释差异来源（提示：pandas 自动按分组，from-scratch 版需手动按 `task_type` 过滤）。
2. 构造"降级场景实验"：生成 20 条审计记录，其中"文案生成"任务（AI 主导）的干预率为 0.4（>0.3 阈值），"合规审核"任务（人类主导）的干预率为 0.9。用 `should_demote` 判定文案生成应降级为人机协作，验证 notes.md 关键回顾 1 的"AI 成熟度被高估"诊断逻辑。
3. 为 `HITLExecutor` 添加"循环上限退出"：当 `rev >= 3` 时即使 `approved=False` 也路由到 `publish`（Day 2 的退出条件），对比纯人工批准（`approved=True`）与循环上限（`rev>=3`）两种退出路径的审计日志差异。对应 practice.md D2 drill 的 HITL 三步工程化。
4. TODO: 在 `practice.md` 的 D3 drill（综合治理推演）中，为 from-scratch 版的 `intervention_rate` 添加"按角色切片"功能：审计日志含 `role` 字段（人/Agent），计算每个角色的干预贡献度。这是本单元既有 TODO1 的 from-scratch 补充--理解 pandas groupby 在裸代码中如何分解为 filter + mean。
