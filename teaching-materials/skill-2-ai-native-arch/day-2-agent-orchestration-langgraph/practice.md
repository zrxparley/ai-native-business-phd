# practice.md - 刻意练习 (Ericsson + MIT)

> v6.0 学习科学层, 不破坏 v5.0 基线。本文件定义本 Day 的刻意练习 (deliberate practice) 规格。
> 研究依据: Ericsson 刻意练习 5 要素 + MIT OpenLearning (worked-faded + 交叉 interleaving + 渐进项目)。

---

## skill_target
能在真实 **LangGraph 1.x** 上独立装配一个含 **条件分支 (Conditional Edge) + 修订循环 (revision loop) + HITL `interrupt_before`** 的企业级多 Agent 营销编排图, 并能用 **A2A / Plan-Execute / Supervisor** 三种拓扑解释自己的设计选择 (口头辩护 + 代码可跑)。

## diagnostic (前测, 3 道, 检测先备)
1. 给定一段 LangGraph 代码, 识别其中哪些是 `Node` / `Edge` / `Conditional Edge` / `Checkpoint`? 各起什么作用?
2. 若把 `interrupt_before=["approval"]` 去掉, HITL 三步模式会塌缩成几步? 为什么? `update_state` 在没有暂停点时是什么行为?
3. A2A 与 MCP 在多 Agent 协作中各负责什么? 给一个"既要 MCP 又要 A2A"的企业场景, 解释为什么缺一不可。

## subskills
- **S1: StateGraph 装配** — `State` 定义 (TypedDict + `Annotated[list, operator.add]`) + `add_node` + `add_edge` + `add_conditional_edges` + `compile`
- **S2: HITL 三步工程化** — `interrupt_before` + `update_state` + `invoke(None)` resume + `MemorySaver` / `SqliteSaver` Checkpointing
- **S3: 多 Agent 拓扑选型** — Supervisor (条件路由=主管) / 层级式 / A2A (Agent-to-Agent) / Plan-Execute (strategy=Plan, copywriter=Execute) + 循环退出条件设计

## drills

### drill D1 (StateGraph 装配)
- **drill_id**: D1
- **difficulty**: 3
- **reps_required**: 3
- **feedback_rule**: 若学员把 Conditional Edge 写成普通 `add_edge`, 追问"如果 `revision_count` 已经 =3, 你的图怎么知道该停? `add_edge` 能读 State 吗?" 引导重读 LangGraph `add_conditional_edges` 文档; 若循环退出条件缺失, 让学员现场跑 `revision_count>=3` 看 State 演化, 自己发现死循环。**反馈锚点: LangGraph StateGraph + 条件分支**。
- **worked_faded**:
  - *Worked* (完整示范): 给出 `research -> strategy -> copywriter` 顺序图完整代码, 含 `CampaignState` TypedDict 与 `Annotated[list, operator.add]` 追加模式
  - *Faded* (部分填空): 给出 `approval_node` 函数框架, 留空 `route_after_approval` 条件函数 (返回 "publish" 或 "revise")
  - *Independent* (独立解): 学员独立加一个"消费者 Agent"节点 + 对应条件分支, 自行设计退出条件

### drill D2 (HITL 三步 + Checkpointing)
- **drill_id**: D2
- **difficulty**: 4
- **reps_required**: 3
- **feedback_rule**: 若学员漏掉 `update_state` 或 `invoke(None)`, 让其用 `print(state)` 打印每步后的 State, 自己发现"`approved` 字段没变 / 图没继续跑"; 若 `MemorySaver` 没装在 `compile()` 里, 提示"重启进程后你的图还能从 approval 恢复吗? Checkpoint 存哪?"。**反馈锚点: HITL 三步 + `interrupt_before` + MemorySaver/SqliteSaver**。
- **worked_faded**:
  - *Worked*: 完整 HITL 三步示范代码 (`invoke` 暂停 -> `update_state` 注入 `{"approved": True}` -> `invoke(None)` resume)
  - *Faded*: 留空 `update_state` 的第二个参数 (人工决策注入字段名与值)
  - *Independent*: 学员独立把 `MemorySaver` 换成 `SqliteSaver`, 验证跨进程恢复 (关掉 Python 重启, 图仍能从 approval 恢复)

### drill D3 (A2A / Plan-Execute / Supervisor 拓扑选型)
- **drill_id**: D3
- **difficulty**: 5
- **reps_required**: 3
- **feedback_rule**: 若学员把 Supervisor 与 Plan-Execute 混为一谈, 追问"你的 `strategy_agent` 是 Supervisor 还是 Plan? 证据是什么? Supervisor 有全局路由权, Plan 只规划自己阶段, 两者能兼任吗?"; 若 A2A 与 MCP 混淆, 用"MCP 接工具, A2A 接 Agent"口诀校验, 让其给反例 (单 Agent + 多工具需不需要 A2A?); 若循环退出条件设为 1 (无修订机会) 或 ∞ (死循环), 让其推演"现实企业里 3 次修订合理吗? 为什么不是 1 或 10?"。**反馈锚点: A2A / Plan-Execute / Supervisor 拓扑选型 + 循环退出**。
- **worked_faded**:
  - *Worked*: 给出 `strategy`(Plan) + `copywriter`(Execute) 的 Plan-Execute 两阶段完整代码, 含 `route_after_approval` Supervisor 路由
  - *Faded*: 留空 Supervisor 的 `route_after_approval` 条件分支 (学员填 `revision_count >= 3` 退出条件)
  - *Independent*: 学员独立加一个"竞品 Agent"节点, 设计其与 `strategy_agent` 的 A2A 通信 (用 State 共享模拟跨进程), 并辩护"为什么用 A2A 而非直接 import"

## progressive_project (脚手架渐退, 参考 MIT CS230 proposal->milestone->final->poster)
- **M1 (proposal)**: 画出本 Day 营销系统的状态图 (纸笔 / mermaid), 标注 4 种编排模式 (顺序/条件/循环/HITL) 各出现在哪里
- **M2 (milestone)**: 在 `starter.ipynb` 上完成 6 个 TODO, 跑通基础版 (无 HITL)
- **M3 (final)**: 加 HITL 三步 + `MemorySaver`, 跑通完整版, 提交 `solution.ipynb` 对照
- **M4 (poster, 选做)**: 加"消费者 Agent"节点 + 用"天道推演 × 多 Agent 仿真"视角写 300 字分析 (六能力映射到 LangGraph 组件)

## interleaving (A1B1C1...B2C2A2...C3A3B3 交叉排布, 不块状)
- A = D1 (StateGraph 装配)
- B = D2 (HITL)
- C = D3 (拓扑选型)
- **排布**: `A1 -> B1 -> C1 -> B2 -> C2 -> A2 -> C3 -> A3 -> B3`
  - 第 1 轮 (A1/B1/C1): 各 drill 的 worked 阶段 (看示范, 抄一遍)
  - 第 2 轮 (B2/C2/A2): 各 drill 的 faded 阶段 (填空)
  - 第 3 轮 (C3/A3/B3): 各 drill 的 independent 阶段 (独立解)
- **不连续做同一 drill 超过 1 次**, 强制大脑在 StateGraph / HITL / 拓扑 三个子技能间切换 (提取练习 + 交叉 interleaving, Butler 2010 证据: 交叉+检索 >> 块状重学)。

## retry_policy
- 每个 drill 失败可重试, 但每次重试前必须先看一遍 worked example (强制 retrieval, 防止"瞎试")
- 累计 3 次失败触发 `weak_loop`
- late submission 参考 Stanford CS230: 10 late days 容忍, 之后每天 20% 罚分 (不罚到 0, 保 motivation)

## weak_loop (连续 2 次失败触发弱项循环)
1. **回退**: 回退到上一 drill (D3 退到 D2, D2 退到 D1, D1 退到 worked example 重看)
2. **补充 worked example**: 重看一遍对应 drill 的完整示范代码, 用 why-what-how 三问反思 (为什么错 / 正确的是什么 / 下次怎么避免)
3. **重做 faded**: 通过 faded 阶段后再回原 drill
4. **不计入 reps_required**: weak_loop 是补强, 不是进度, 但需记录到 `student_model.json` 供 `tutorial.ipynb` 读取 (Hattie [SELF-REG] 级反馈触发点)
5. **跨单元回溯**: 若 weak_loop 仍不能通过, 触发 `recommended_review` 指向技能5 Day2 (LangGraph mechanics) 复习 StateGraph 基础
