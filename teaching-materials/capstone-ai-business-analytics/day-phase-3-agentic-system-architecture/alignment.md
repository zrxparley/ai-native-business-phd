---
unit: capstone-phase-3-agentic-system-architecture
version: v6.0
layer: learning-science
framework: Biggs Constructive Alignment + Mastery Learning
---

# Capstone Phase 3 建构对齐 (Biggs ILO ↔ TLA ↔ AT)

> 本文件遵循 Biggs「建构对齐」原则: 预期学习产出 (ILO) -> 教学学习活动 (TLA) -> 评估任务 (AT) 三者对齐, 每行配 mastery_threshold。学生可用 3 个自检问题判断是否对齐 (Feed Up / Feed Back / Feed Forward)。

## ILO ↔ TLA ↔ AT 矩阵 (>=3 行)

| ILO (预期学习产出, Intended Learning Outcome) | TLA (教学学习活动, Teaching/Learning Activity) | AT (评估任务, Assessment Task) | mastery_threshold |
|----------------------------------------------|-----------------------------------------------|------------------------------|------------------|
| **ILO-1**: 能用 Capstone 三层架构 (用户交互/Agent编排/数据知识) 解释 Agent 系统如何从 Phase 2 知识图谱获取知识、经多Agent编排产出营销方案、通过 HITL 审批交付用户 | 读 notes.md「关键回顾1 三层架构」表 + 做 practice.md diagnostic Q1 (TypedDict 字段分层) + starter.ipynb TODO 1 (定义 AgentSystemState 含 knowledge_context) + tutorial.ipynb cell2 pre-tutorial essay (写三层映射) | diagnostic Q1 自动评分 + starter.ipynb TODO 1 单元测试 (`assert 'knowledge_context' in AgentSystemState.__annotations__`) + tutorial.ipynb cell5 Hattie [TASK] 反馈 | >=80% (diagnostic Q1 + TODO 1 测试 + essay 三项加权) |
| **ILO-2**: 能用 LangGraph `StateGraph`/`Node`/`Edge` 构建 researcher->strategist->writer->review->publish 多Agent营销系统, 识别条件边与循环退出, 说明 HITL 治理意义 | 做 practice.md drill_A1 (State 建模) + drill_B1 (节点+条件边装配, Worked-Faded 三阶段) + starter.ipynb TODO 2/3/4/5 + tutorial.ipynb cell3 Socratic 追问 (条件边 / 循环退出 / HITL) | drill_B1 reps_required=5 全部通过 + starter.ipynb TODO 2/3/4/5 单元测试 + tutorial.ipynb cell4 student_model.json 记录掌握度 | >=80% (drill_B1 + TODO 测试 + student_model 满足"无盲点") |
| **ILO-3**: 能在真实 LangGraph 库上完成"定义State -> 写节点 -> 装配图 (含 interrupt_before + MemorySaver) -> 编译 -> 三步 HITL 运行"全流程, 解释 Checkpointing 持久化作用 | 做 practice.md drill_C1 (HITL 三步运行 + 天道推演映射, Worked-Faded) + starter.ipynb TODO 6 + tutorial.ipynb cell3 Socratic 追问 (Checkpointing / 三步恢复) + reading.md 深链 LangGraph 官方文档 | drill_C1 reps_required=4 全部通过 + starter.ipynb TODO 6 端到端测试 (`run_capstone_hitl()` 返回 final_output 不为 None) + progressive_project final (系统架构文档 + HITL 演示截图) | >=80% (drill_C1 + TODO 6 端到端 + final 项目评审) |
| **ILO-4**: 能用 Plan-Execute 模式解释 strategist(Plan)/writer(Execute) 分工, 用 MCP 解释 researcher 工具调用, 用 A2A 解释多Agent通信 | 读 notes.md「2026前沿 LangGraph/MCP/A2A」+ schedule.json C2/C3 卡片间隔重复 + tutorial.ipynb cell3 Socratic 追问 (MCP/A2A/Plan-Execute 三概念区分) | schedule.json 卡片 EF 值 >= 2.5 维持 + progressive_project proposal (300 字方案含 5 节点输入输出) + tutorial.ipynb cell5 Hattie [PROCESS] 反馈 | >=80% (schedule 卡片 retention + proposal 评审 + Socratic 答对率) |
| **ILO-5**: 能用"天道推演 × 多Agent仿真"视角把 Capstone 营销沙盘映射为 LangGraph 多Agent博弈图, 为 Phase 4 因果评估提供可审计决策链 | 读 notes.md「天道推演 × 多Agent仿真」表 + practice.md drill_C1 *Independent* 阶段 (写映射段) + progressive_project poster (反事实分析) | drill_C1 Independent 阶段评分 + progressive_project poster 评审 (含三张反事实分析) + tutorial.ipynb cell6 exit artifact (盲点 + 复习单元) | >=80% (drill_C1 Independent + poster + exit artifact 三项加权) |

---

## 3 自检问题 (Feed Up / Feed Back / Feed Forward)

> 学生完成本单元后, 自检三个问题。任一答"否"即对齐失败, 需回退到对应 TLA 重做。

### 自检 1 (Feed Up): TLA 是否训练 ILO?

> 问: 我做过的 TLA (starter.ipynb 6 TODO + practice.md 3 drill + tutorial.ipynb Socratic + schedule.json 4 卡片) 是否实际训练了 5 个 ILO?
>
> 自检方法: 对每个 ILO, 找到至少 1 个 TLA 直接训练它。
> - ILO-1 <- starter TODO 1 + diagnostic Q1 + tutorial essay
> - ILO-2 <- starter TODO 2/3/4/5 + drill_A1/B1 + Socratic 追问
> - ILO-3 <- starter TODO 6 + drill_C1 + reading.md LangGraph 文档
> - ILO-4 <- schedule.json C2/C3 + notes.md 前沿节 + Socratic 追问
> - ILO-5 <- drill_C1 Independent + poster + notes.md 天道推演表
>
> 若某 ILO 找不到 TLA -> 对齐失败, 补做对应 TLA。

### 自检 2 (Feed Back): AT 是否测量 ILO?

> 问: 我参加的 AT (diagnostic + drill 评分 + TODO 单元测试 + progressive_project + tutorial student_model) 是否实际测量了 5 个 ILO?
>
> 自检方法: 对每个 ILO, 找到至少 1 个 AT 测量它, 且 AT 评分标准与 ILO 表述对应 (不是"参加了就行", 而是"做到了 ILO 描述的能力")。
> - ILO-1 测量 <- diagnostic Q1 + TODO 1 测试 (能定义三层字段)
> - ILO-2 测量 <- drill_B1 reps + TODO 2/3/4/5 测试 (能装配条件边)
> - ILO-3 测量 <- drill_C1 reps + TODO 6 端到端 (能跑通三步 HITL)
> - ILO-4 测量 <- schedule.json retention + proposal (能解释 MCP/A2A)
> - ILO-5 测量 <- drill_C1 Independent + poster (能做天道推演映射)
>
> 若某 ILO 找不到 AT 或 AT 评分不对应 ILO -> 对齐失败, 重设 AT。

### 自检 3 (Feed Forward): 不经 TLA 能过 AT 吗? 若能 = 对齐失败

> 问: 如果我不做 TLA (不写 starter.ipynb, 不做 drill, 不上 tutorial), 仅靠 prior knowledge 能直接过 AT 吗?
>
> 自检方法:
> - **diagnostic Q1 (TypedDict + Annotated)**: 没学过 LangGraph AgentState 的人能写对吗? 若能 (因为只是 Python typing 通用知识) -> diagnostic 不够领域特定, 但仍可作为先验探测
> - **drill_B1 (条件边装配)**: 没读过 notes.md「Agent工作流表」和「Plan-Execute 模式」的人能正确实现 `route_after_review` 返回值与条件边字典键匹配吗? 若不能 -> 对齐成功 (TLA 必要)
> - **drill_C1 (HITL 三步 + 天道推演映射)**: 没学过 LangGraph `interrupt_before` + `update_state` + `MemorySaver` 的人能跑通三步吗? 没读过 notes.md「天道推演表」的人能写映射段吗? 若不能 -> 对齐成功
> - **proposal (Plan-Execute + 三层架构)**: 没学过 notes.md 的人能写出含 5 节点输入输出的 300 字方案吗? 若不能 -> 对齐成功
>
> 若全部 AT 都能不经 TLA 通过 -> 对齐彻底失败, 需重设 AT 使其真正依赖本单元领域知识 (LangGraph/MCP/A2A/Phase 2 知识图谱/天道推演)。

---

## mastery 阈值汇总

- 全部 5 个 ILO 的 AT 加权 >= 80% 视为本单元 mastery
- 任一 ILO 的最高 AT 分 < 70% 视为该 ILO 未掌握, 即使总分达标也需回退 TLA + AT 重做 (见 practice.md weak_loop)
- progressive_project final 必须 >= 75% (CS230 风格 capstone 最低门槛), 否则触发 weak_loop 回退到 milestone
- tutorial.ipynb student_model.json 中记录的盲点必须 < 2 个, 否则视为 ILO-2/ILO-3 未掌握

---

*本文件由 v6.0 学习科学层升级生成。ILO/TLA/AT 全部引用本单元真实对象 (LangGraph StateGraph / interrupt_before / MemorySaver / Phase 2 知识图谱 / 天道推演 × 多Agent仿真 / MCP / A2A / Plan-Execute), 不使用通用模板。*
