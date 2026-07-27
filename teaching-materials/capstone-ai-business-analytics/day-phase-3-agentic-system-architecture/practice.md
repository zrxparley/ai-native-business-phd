---
unit: capstone-phase-3-agentic-system-architecture
version: v6.0
layer: learning-science
skill_target: 能独立用 LangGraph StateGraph 装配一个含 researcher→strategist→writer→review→publish 多Agent、条件边、循环退出与 interrupt_before HITL 审批的Capstone营销系统,并解释每个图对象对应的Capstone三层架构映射
---

# Capstone Phase 3 刻意练习 (Deliberate Practice, Ericsson + MIT/Stanford)

> 本文件遵循 Ericsson「刻意练习」原则: 任务拆解到子技能 → 每子技能配带反馈的重复训练 → Worked-Faded 渐退 → 交叉练习促迁移。所有 drill 领域特定, 引用本单元真实库 (LangGraph/MCP/A2A/Phase 2 知识图谱/OfflineMockLLM), 不使用通用模板。

## diagnostic (CS229 pset0 式先测, 探测先验缺口)

> 限时 15 分钟, 不查资料, 不跑代码。三题全错者从 drill A1 起步; 错 1 题从 B1 起步; 全对从 C1 起步。

**Q1 (先验: Python TypedDict 与 Annotated)** 给出下面代码片段, 写出 `AgentSystemState` 中 `messages: Annotated[list, operator.add]` 字段在两次节点 `add_message` 后的最终值, 并解释为什么不能用 `messages: list`:

```python
class AgentSystemState(TypedDict):
    messages: Annotated[list, operator.add]
    revision_count: int
```

**Q2 (先验: 状态机与图论)** 用 `add_conditional_edges` 写出"审核通过 → publish; 审核不通过 → writer; 修订次数 ≥3 → publish"的路由函数 `route_after_review(state)`。说明若忘记加 `revision_count >= 3` 退出条件, 图会发生什么 (LangGraph 默认递归上限是多少?)。

**Q3 (先验: HITL 与中断恢复)** LangGraph 的 `compile(interrupt_before=["review_node"], checkpointer=MemorySaver())` 编译后的图, 三步 HITL (`invoke → update_state → None/resume`) 各自做什么? 如果漏掉 `checkpointer=`, 第二步 `update_state` 会发生什么?

---

## subskills (3 子技能, 对应 notes.md 5 个学习目标)

- **subskill_A (State 建模)**: 能定义 `AgentSystemState` 含 `knowledge_context`(Phase 2 桥接)、`Annotated[list, operator.add]` 追加模式字段、循环计数器 (`revision_count`), 并说明各字段在哪一层 (用户交互/Agent编排/数据知识)
- **subskill_B (节点 + 条件边装配)**: 能实现 researcher(MCP工具读知识图谱)/strategist(Plan)/writer(Execute+循环)/review(HITL+安全)/route_after_review(条件路由) 五个节点, 用 `add_conditional_edges` 装配图并设置 `interrupt_before`
- **subskill_C (HITL 三步运行 + Checkpointing)**: 能跑通 `invoke → update_state → resume` 全流程, 解释 MemorySaver 的状态持久化作用, 并把"天道推演 × 多Agent仿真"的"记录假设/追踪偏差/更新因果模型"映射到 Checkpointing + 反馈学习节点

---

## drills (>=3, 每个 drill_id / difficulty(1-5) / reps_required / feedback_rule / worked_faded 三阶段)

### drill_A1
- **drill_id**: A1
- **difficulty**: 2
- **reps_required**: 3
- **target subskill**: A (State 建模)
- **task**: 在 starter.ipynb 的 TODO 1 处定义 `AgentSystemState`, 含 10 字段: `brief`/`knowledge_context`/`research_findings`/`strategy`/`draft`/`review_feedback`/`revision_count`/`messages`/`final_output`/`safety_flag`, 其中 `messages` 必须是 `Annotated[list, operator.add]`
- **feedback_rule**: 跑 `python3 -c "from solution import AgentSystemState; import operator, typing; assert typing.get_type_hints(AgentSystemState)['messages'].__metadata__[0] is operator.add"`。若失败, 提示"打开 starter.ipynb 看 TODO 1 提示行: 字段类型注解的第二个参数 `operator.add` 是追加规约, 不是默认值"。引用 notes.md 表格"Capstone三层架构"中"`knowledge_context` Phase 2 知识图谱字段"作为字段对齐证据
- **worked_faded**:
  - *Worked (完整示范)*: 给出 `insight_state` 的完整定义 (5 字段, 含 Annotated), 学生照抄一遍跑通
  - *Faded (部分填空)*: 给出 `AgentSystemState` 的 10 字段名, 学生填类型注解 (`Annotated[list, operator.add]` / `str` / `int`)
  - *Independent (独立解)*: 学生从零定义, 并口述每个字段属于哪一层 (用户交互/Agent编排/数据知识)

### drill_B1
- **drill_id**: B1
- **difficulty**: 4
- **reps_required**: 5
- **target subskill**: B (节点 + 条件边装配)
- **task**: 在 starter.ipynb 的 TODO 2/3/4/5 处实现 5 个节点 (`researcher_agent`/`strategist_agent`/`writer_agent`/`review_node`/`route_after_review`) + `build_agent_system` 装配。条件边规则: `safety_flag=True → publish_node`; `revision_count >= 3 → publish_node`; 否则 → `writer_agent`
- **feedback_rule**: 跑 `python3 -c "from solution import build_agent_system; g = build_agent_system(); assert 'review_node' in g.nodes; assert 'writer_agent' in g.nodes"`。若失败, 提示"检查 `add_conditional_edges('review_node', route_after_review, {True:'publish_node', False:'writer_agent', 'exit':'publish_node'})` 的字典键是否与 `route_after_review` 返回值匹配"。引用 notes.md "Plan-Execute模式" 与 "Agent工作流" 表格作为节点职责校验
- **worked_faded**:
  - *Worked*: 给出 `researcher_agent` + `strategist_agent` 完整实现, 学生照抄跑通
  - *Faded*: 给出 `writer_agent` 的函数签名 + docstring + 5 个 TODO 占位 (`# TODO: 调 LLM / TODO: 处理 review_feedback / TODO: revision_count+1 / TODO: 返回 state / TODO: 异常处理`), 学生填空
  - *Independent*: 学生独立实现 `review_node` + `route_after_review` + `build_agent_system` 装配 (含 `interrupt_before=["review_node"]`)

### drill_C1
- **drill_id**: C1
- **difficulty**: 5
- **reps_required**: 4
- **target subskill**: C (HITL 三步运行 + Checkpointing + 天道推演映射)
- **task**: 在 starter.ipynb TODO 6 处实现 `run_capstone_hitl`, 跑通三步: (1) `graph.invoke(initial_state, config={"configurable":{"thread_id":"1"}})` 到 `interrupt_before` 暂停; (2) 人工审批后 `graph.update_state(config, {"review_feedback":"approve", "safety_flag":True})`; (3) `graph.invoke(None, config)` resume 到 publish。最后写一段话: 把 Checkpointing 映射到天道推演的"记录前提假设/追踪偏差/更新因果模型"
- **feedback_rule**: 跑 `python3 -c "from solution import run_capstone_hitl; out = run_capstone_hitl(); assert out['final_output'] is not None; assert out['revision_count'] <= 3"`。若失败, 提示"第一步 invoke 必须传 `thread_id` 否则 checkpointer 找不到状态; 第二步 update_state 不是 invoke, 不要传 input; 第三步 resume 用 `graph.invoke(None, config)` 不是 `graph.invoke({}, config)`"。引用 notes.md "天道推演 × 多Agent仿真" 表格作为映射校验
- **worked_faded**:
  - *Worked*: 给出 `run_capstone_hitl` 完整代码 (含三步 + 打印 + 注释), 学生跑通
  - *Faded*: 给出三步的函数签名 + 每步一个 TODO (第一步 TODO: 怎么传 config; 第二步 TODO: update_state 的参数; 第三步 TODO: resume 的特殊入参), 学生填空
  - *Independent*: 学生独立实现, 并额外加一个"取消审核"分支 (`update_state` 设 `safety_flag=False`, 验证 publish_node 仍能跑通, 解释为什么)

---

## progressive_project (CS230 式 proposal → milestone → final → poster)

- **proposal (Week 1)**: 300 字方案 — 选一个真实营销场景 (例: 新茶饮品牌上市), 列出 5 个节点的输入/输出, 标出 HITL 审批在哪个节点、为什么。提交 PDF
- **milestone (Week 2)**: 在 starter.ipynb 上跑通 6 个 TODO, 给出 `researcher_agent` 读 Phase 2 知识图谱的真实输出截图, 解释 `knowledge_context` 如何提升研究质量
- **final (Week 3)**: 完整 `solution.ipynb` + 系统架构文档 (三层架构图 + 节点职责表 + 条件边规则表) + 人机协作治理框架 (人类决策/Agent决策/混合决策矩阵) + Agent 安全检查方案
- **poster**: A1 海报, 含 LangGraph 状态图截图 + 天道推演映射表 + 三个最关键的"如果我改 X, 系统会怎样"反事实分析

---

## interleaving (A1B1C1 → B2C2A2 → C3A3B3 交叉排布, 不块状)

> 研究显示 interleaving (交叉练习) 促迁移, 优于 block practice (块状重复)。本表刻意打乱顺序。

| 顺序 | 练习 | 间隔 (上次同子技能后) |
|------|------|--------------------|
| 1 | A1 (rep 1/3) | — |
| 2 | B1 (rep 1/5) | — |
| 3 | C1 (rep 1/4) | — |
| 4 | B1 (rep 2/5) | 1 步 |
| 5 | C1 (rep 2/4) | 1 步 |
| 6 | A1 (rep 2/3) | 4 步 |
| 7 | C1 (rep 3/4) | 2 步 |
| 8 | A1 (rep 3/3) | 2 步 |
| 9 | B1 (rep 3/5) | 5 步 |
| 10 | B1 (rep 4/5) | 1 步 |
| 11 | C1 (rep 4/4) | 4 步 |
| 12 | B1 (rep 5/5) | 2 步 |

> 顺序明文: A1B1C1 B2C2A2 C3A3B3 B4B5 (B 在末尾加强因为难度最高 4-5)。每次练习间至少间隔一次其他子技能或一次睡眠。

---

## retry_policy (CS230 式 retry)

- 10 个 free late days, 每个 drill 可申请延后, 用完为止, 不额外扣分
- 任一 drill 评分 < 60% 视为"失败", **失败可重试, 不罚分** (CS230 风格), 取最高分入册
- 同一 drill 最多重试 2 次; 第 3 次仍失败触发 weak_loop
- 重试时必须附"我上次错在哪"的 50 字反思, 否则不受理

---

## weak_loop (连续 2 次失败触发弱项循环)

> 触发条件: 同一 drill 连续 2 次评分 < 60%。

**弱项循环流程**:
1. **回退一级**: 若失败 drill 是 B1, 回退到 A1 (子技能 A 是 B 的前置); 若是 C1, 回退到 B1
2. **补做 Worked Example**: 重做该 drill 的 *Worked* 阶段 (完整示范), 抄写一遍并写"为什么这行这么写"的注释
3. **再 Faded**: 重做 *Faded* 阶段, 但要求每个 TODO 旁写"这一行调用的是 LangGraph 哪个 API"
4. **盲点记录到 student_model.json** (见 tutorial.ipynb): 写入 `{"drill_id": "B1", "fail_count": 2, "blind_spot": "条件边字典键与 route 函数返回值不匹配"}`
5. **解锁重试**: 完成 1-4 后, 可重新提交该 drill, 不计入 retry 次数

**示例**: 学生在 B1 连续 2 次失败 → 回退 A1 (Worked 阶段重抄 `insight_state` 定义) → 再做 A1 Faded → 记录盲点 "Annotated 第二参数语义混淆" → 解锁 B1 重试

---

## mastery_threshold (整体掌握)

- diagnostic + 3 drill + progressive_project 总分 ≥ 80% 视为 mastery
- 任一 subskill (A/B/C) 的最高分 < 70% 视为该子技能未掌握, 即使总分达标也需补做该子技能的 Worked→Faded→Independent
- progressive_project 的 final 必须 ≥ 75%, 否则触发 weak_loop (回退到 milestone 重做)

---

*本文件由 v6.0 学习科学层升级生成。drill 的 feedback_rule 全部引用本单元真实库 (LangGraph StateGraph / interrupt_before / MemorySaver / Phase 2 知识图谱 / OfflineMockLLM), 不使用通用模板。*
