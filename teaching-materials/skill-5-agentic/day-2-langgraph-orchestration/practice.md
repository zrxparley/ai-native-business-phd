---
unit: U5-D2
title: LangGraph 编排实战 - 刻意练习 (Deliberate Practice)
version: v6.0
algorithm: Ericsson deliberate practice + MIT CS229 pset0 diagnostic + CS230 progressive project + Worked-Faded scaffolding
---

# practice.md · LangGraph 编排刻意练习

## skill_target

能用 LangGraph 的 `StateGraph`/`Node`/`Edge` 三要素装配一个带**条件边**（`add_conditional_edges` + `should_approve`）与**循环退出条件**（`revision_count >= 3`）的多Agent营销状态图，并解释 `MemorySaver` 检查点与 `interrupt` 人机协作（HITL）在审核节点的恢复机制。可在 60 分钟内独立完成 `starter.ipynb` 的 6 个 TODO 并通过 `solution.ipynb` 结构对照。

---

## diagnostic (先测, CS229 pset0 式, 探测先验缺口)

> 限时 15 分钟闭卷作答。每题先写"我确信/我猜的/我不会"标记，再写答案。目的不是得分，是暴露缺口。

### D1. 概念辨析
LangGraph 的 `StateGraph` 与 LangChain 的 `Chain` 在**状态管理**与**控制流**上有何本质区别？请各用一句话定义，并指出 `MarketingState`（TypedDict）属于哪一层的对象。

### D2. 反事实推演
若把 `starter.ipynb` TODO4 中 `should_approve` 的循环退出条件 `revision_count >= 3` **完全删除**，画出审核不通过分支的状态图，并指出在什么输入下系统会进入死循环。给出你的判断依据。

### D3. 库 API 细节
写出下列 LangGraph 调用的真实签名（不要查文档）：
- `workflow.add_conditional_edges(...)` 的三个参数分别是什么？
- `interrupt(value)` 在节点函数内被调用后，图的执行状态如何变化？人工恢复时用什么对象传入结果？

> 自评：若 D1/D2/D3 中有 >=2 题标"我猜的/我不会"，先回 `notes.md` § 关键回顾 1-3 重读，再开始 drills。

---

## subskills (3 个子技能拆解)

| 子技能 | 描述 | 对应 starter TODO |
|--------|------|-------------------|
| S1. 状态建模 (State Modeling) | 用 TypedDict 定义多节点共享的 `MarketingState`，明确每个节点只写自己负责的字段（状态驱动设计） | TODO1 |
| S2. 条件路由 (Conditional Routing) | 写 `should_approve` 条件函数 + 用 `add_conditional_edges` 注册 publish/revise 分支，并设循环退出条件 | TODO2-4 |
| S3. 检查点与人机协作 (Checkpointing + HITL) | 用 `MemorySaver`/`SqliteSaver` 持久化 State，用 `interrupt`+`Command` 实现审核节点暂停-恢复 | TODO5-6 |

---

## drills (>=3, 每个 drill 含 difficulty/reps_required/feedback_rule/worked_faded)

### drill_id: D-STATE
- **difficulty**: 2
- **reps_required**: 3
- **目标**: 定义 `MarketingState` TypedDict，含 brief/analysis/strategy/content/review_feedback/revision_count/approved/messages 八字段
- **feedback_rule**: 用 `solution.ipynb` TODO1 的 TypedDict 字段集做 diff；缺任一字段反馈"你的 State 缺少 X，content_agent 写 content 后审核节点读不到 review_feedback 会导致 KeyError"——必须引用具体节点的读写依赖
- **worked_faded** (三阶段):
  - **Worked (完整示范)**: 给出完整 `class MarketingState(TypedDict): brief: str; analysis: str; ...` 八字段定义 + 注释每字段由哪个 agent 写
  - **Faded (部分填空)**: 给出 TypedDict 框架，挖空 review_feedback/revision_count/approved 三个字段名，学生填
  - **Independent (独立解)**: 仅给"定义一个营销多Agent共享状态，需含 brief/分析/策略/内容/审核反馈/修订次数/是否通过/消息历史"自然语言描述，学生独立写 TypedDict

### drill_id: D-ROUTE
- **difficulty**: 3
- **reps_required**: 4
- **目标**: 实现 `should_approve(state) -> Literal["publish","revise"]` + 用 `add_conditional_edges("review", should_approve, {"publish":"publish","revise":"content"})` 注册，并加 `revision_count >= 3` 强制 publish 退出
- **feedback_rule**: 用 LangGraph `compile()` 是否抛 `InvalidGraphError` 做硬反馈；若图能编译但条件函数漏掉退出条件，反馈"你的 should_approve 没有 revision_count 上限，运行 brief='不通过测试' 会死循环——用 `starter.ipynb` cell 6 的 stream 跑 5 步看是否卡在 review->content->review"
- **worked_faded**:
  - **Worked**: 完整 `def should_approve(state): if state["revision_count"] >= 3: return "publish"; return "revise" if not state["approved"] else "publish"` + `add_conditional_edges` 调用
  - **Faded**: 给出函数框架与 `add_conditional_edges` 调用，挖空 `revision_count >= 3` 的判断逻辑与 Literal 返回值
  - **Independent**: 仅给状态图 ASCII（review -> publish/revise -> content 循环），学生独立写条件函数 + 注册

### drill_id: D-ASSEMBLE
- **difficulty**: 4
- **reps_required**: 3
- **目标**: 实现 `build_marketing_graph()`：`StateGraph(MarketingState)` -> `add_node` 4 个 -> `add_edge` 串行段 -> `add_conditional_edges` 审核分支 -> `set_entry_point` -> `compile(checkpointer=MemorySaver())`
- **feedback_rule**: 用 `verify_unit.py` 第 3 条（starter.ipynb TODO 数）做结构对照；若 `add_node` 漏节点，反馈"你的图缺 analysis_agent 节点，add_edge('analysis','strategy') 会抛 KeyError——对照 notes.md § 关键回顾 1 的三要素表"
- **worked_faded**:
  - **Worked**: 完整装配函数（含 4 个 add_node + 3 条 add_edge + 1 条 conditional + compile with MemorySaver）
  - **Faded**: 给出函数骨架与 add_edge 调用，挖空 add_node 的 4 个节点名 + add_conditional_edges 的参数
  - **Independent**: 仅给"装配一个营销多Agent图，4 节点 + 条件审核分支 + MemorySaver 检查点"，学生独立写整个函数

### drill_id: D-HITL
- **difficulty**: 5
- **reps_required**: 2
- **目标**: 把 `review_node` 的 LLM 自动审核替换为 `interrupt` 真人工审核：图在审核节点暂停，State 被 `MemorySaver` 持久化；人工 Command(resume=...) 恢复
- **feedback_rule**: 用 `langgraph.types.interrupt` 是否在节点函数内被调用做硬检查；若学生把 interrupt 写在节点外，反馈"interrupt 必须在节点函数内调用才会触发图暂停——参见 notes.md § 关键回顾 3 的代码片段"
- **worked_faded**:
  - **Worked**: 完整 `def review_node(state): feedback = interrupt({"content": state["content"], "msg":"请审核"}); return {"approved": feedback["approved"], "review_feedback": feedback.get("comment","")}`
  - **Faded**: 给出函数框架，挖空 interrupt 的调用 + return 的 State 更新字段
  - **Independent**: 仅给"用 interrupt 实现人工审核节点，暂停等待 approved 与 comment"，学生独立写

---

## progressive_project (CS230 式渐进交付)

| 阶段 | 交付物 | 评分权重 | 退出条件 |
|------|--------|----------|----------|
| Proposal (Day 2 课前) | 一段 300 字方案：你要为哪个营销场景（如新品发布/危机公关/投放优化）建多Agent图，画出预期状态图拓扑（含条件分支） | 15% | TA 确认拓扑含 >=1 条件边 + >=1 循环退出 |
| Milestone (Day 2 课中) | `starter.ipynb` TODO1-4 完成（State + 2 agent + 条件路由），图能 compile 不报错 | 30% | `compile()` 成功 + stream 跑通前 3 步 |
| Final (Day 2 课后 48h) | TODO1-6 全完成 + `interrupt` HITL + `MemorySaver` 检查点恢复演示 | 40% | `verify_unit.py` 7/7 + HITL 暂停-恢复可复现 |
| Poster (Day 3 课前) | 一页 poster：你的状态图 + 条件边决策树 + 一段"多Agent仿真 × 天道推演"映射（局势感知/沙盘模拟/反馈学习对应哪些节点） | 15% | 同伴互评 >=3 人能复述你的条件路由逻辑 |

---

## interleaving (交叉排布, 不块状)

> 不按 S1->S2->S3 块状练，按以下交叉顺序练（A=STATE, B=ROUTE, C=ASSEMBLE, D=HITL）：

```
Day 2 上午:  A1 -> B1 -> C1 -> A2 -> B2 -> (milestone 提交)
Day 2 下午:  C2 -> D1 -> A3 -> B3 -> C3 -> D2 -> (final 提交)
Day 2 晚间:  C3 -> A3 -> B3 -> (poster 准备, 回顾弱项)
```

理论依据：交叉练习（interleaving）促进迁移，比块状练习更利于在期末/poster 时区分何时用哪个子技能（LangGraph 装配时该用 add_edge 还是 add_conditional_edges）。

---

## retry_policy (CS230 式)

- **10 free late days**: 全学期 10 天免费迟交额度，跨单元共享，无需理由
- **失败重试不罚分**: drill 连续 2 次不过，重做至 reps_required 满足，最终分取最高分（不取平均）
- **milestone 不占 late days**: milestone 是形成性评估，迟交只触发弱项循环，不扣分

---

## weak_loop (连续 2 次失败触发弱项循环)

若同一 drill 连续 2 次 `feedback_rule` 判失败：
1. **回退**: 自动回退到上一难度 drill（如 D-ROUTE 失败 -> 回 D-STATE 重练 1 rep）
2. **补充 worked example**: 强制重看该 drill 的 Worked 阶段完整示范一遍
3. **诊断对话**: 触发 `tutorial.ipynb` 的 Socratic loop，针对失败 drill 的子技能追问"你的 should_approve 里 revision_count 是从哪个字段读的？为什么"
4. **退出条件**: 弱项循环连续 1 次通过后，回到原 drill 继续累计 reps

---

## 与 notes.md 的映射

| practice.md 元素 | notes.md 对应 |
|------------------|---------------|
| skill_target | 学习目标 1-4 |
| D-STATE drill | 关键回顾 1 (StateGraph) + TODO1 |
| D-ROUTE drill | 关键回顾 2 (条件路由) + TODO2-4 |
| D-ASSEMBLE drill | 关键回顾 1 + TODO5 |
| D-HITL drill | 关键回顾 3 (HITL/interrupt) + TODO6 |
| progressive_project poster | 2026 前沿补充 (多Agent仿真 × 天道推演) |

---

*本练习设计引用 Ericsson 刻意练习理论 + MIT CS229 pset0 诊断 + CS230 渐进项目 + Worked-Faded 示范渐退。领域对象全部来自 LangGraph 真实库与 MarketingState 营销场景。*
