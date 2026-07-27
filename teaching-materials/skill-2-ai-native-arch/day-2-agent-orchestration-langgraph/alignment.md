# Constructive Alignment - 技能2 Day 2 (Agent编排架构+LangGraph)

> **Biggs 建构对齐 (Constructive Alignment)**: ILO (Intended Learning Outcomes 预期学习产出) ↔ TLA (Teaching/Learning Activities 教学学习活动) ↔ AT (Assessment Tasks 评估任务) 三者必须对齐。
> v6.0 学习科学层, 不破坏 v5.0 基线。

---

## ILO ↔ TLA ↔ AT 矩阵

| ILO (预期学习产出) | TLA (教学学习活动) | AT (评估任务) | mastery_threshold |
|---|---|---|---|
| **ILO1**: 能用 `StateGraph`/`Node`/`Edge` 三要素解释"有状态有向图"如何替代线性 Chain, 识别四种编排模式 (顺序/并行/循环/条件) 与多 Agent 协作拓扑 (Supervisor/层级式) | notes.md §关键回顾1-2 + starter.ipynb TODO 1-3 (State+顺序节点) + tutorial.ipynb Socratic 追问 + practice.md D1 (worked->faded->independent) + schedule.json C1 复习 | starter.ipynb TODO 1-3 填空 + tutorial.ipynb pre-task Q1 + D1 independent 通过 | >=80% TODO 正确 + 能口头辩护"为什么用图不用链" (tutorial Socratic 不被问穿) |
| **ILO2**: 能在真实 LangGraph 上完成 `State -> 节点函数 -> 装配(interrupt_before+MemorySaver) -> compile -> 三步HITL(invoke->update_state->resume)` 全流程, 解释 Checkpointing 持久化作用 | notes.md §关键回顾5 + starter.ipynb TODO 4-6 (approval+route+build+run_with_hitl) + practice.md D2 (HITL worked->faded->independent) + tutorial.ipynb Hattie [PROCESS] + schedule.json C2 | starter.ipynb TODO 4-6 + solution.ipynb 对照 + D2 faded->independent 通过 + 300字退出条件分析 (`revision_count>=3` 合理性) | >=70% TODO 正确 + 能独立解 D2 independent (SqliteSaver 跨进程恢复) |
| **ILO3**: 能区分 A2A/MCP 互补定位 (MCP 接工具, A2A 接 Agent), 用 Supervisor/层级式/Plan-Execute/A2A 解释多 Agent 协作拓扑, 用"天道推演×多Agent仿真"视角映射企业沙盘 | notes.md §关键回顾3-4 + §2026前沿 + practice.md D3 (拓扑选型 worked->faded->independent) + tutorial.ipynb devil's advocate + schedule.json C3/C4 | D3 independent (加消费者/竞品 Agent + 条件分支 + A2A 通信设计) + 选做 M4 poster (天道推演六能力映射 300字) | 能独立解 D3 + 口头辩护"为什么选 Supervisor 而非层级式"+"为什么既要 MCP 又要 A2A" |

---

## mastery_threshold (整体)

- 6 个 starter.ipynb TODO 全部填对 (>=80% 代码正确率)
- 3 个 drill (D1/D2/D3) 各完成 3 reps (worked->faded->independent 三阶段全通)
- tutorial.ipynb Hattie [FEED-FORWARD] 无红色 flag (无未解决 blind_spot)
- schedule.json 4 张卡片 first review 全部 ef >= 2.5 (FSRS-6 stable)
- weak_loop 触发 <= 1 次 (连续 2 次失败才触发, 触发后能恢复)

---

## 3 自检问题 (Biggs Feed Up / Feed Back / Feed Forward)

### 1. Feed Up (TLA 是否训练 ILO?)
**问**: starter.ipynb 的 6 个 TODO 是否覆盖了 ILO1/2/3? 哪个 ILO 训练不足?

**自检答案**: TODO 1-3 训练 ILO1 (StateGraph + 顺序/条件), TODO 4-6 训练 ILO2 (HITL + compile), D3 + 选做 M4 训练 ILO3 (拓扑选型 + 天道推演)。若学员只交 starter.ipynb 不做 D3, **ILO3 训练不足**, 需强制 tutorial.ipynb Socratic 追问 ("Supervisor 与 Plan-Execute 能兼任吗?") 补齐。

### 2. Feed Back (AT 是否测量 ILO?)
**问**: solution.ipynb 对照能测 ILO1/2 的什么? 不能测什么?

**自检答案**: solution.ipynb 能测 ILO1/2 的**代码正确性** (机械层: TODO 填对没有), 但测不了 ILO3 的**拓扑选型辩护** (需口头/文字辩护"为什么选 Supervisor 而非层级式")。因此加 tutorial.ipynb Hattie [PROCESS] 级反馈 + 300 字退出条件分析作 AT 补充, 把评估从"代码对错"升级为"代码+辩护"。

### 3. Feed Forward (不经 TLA 能过 AT 吗? 若能 = 对齐失败)
**问**: 学员能否不练 D2 直接过 HITL TODO (TODO 4-6)?

**自检答案**: **不能**。D2 的 faded->independent 强制学员自己写 `update_state` 的第二个参数, 若只抄 solution.ipynb 会被 tutorial.ipynb Socratic 追问"去掉 `interrupt_before` 会塌缩成几步? `update_state` 在没有暂停点时是什么行为?"问穿。**对齐成立**。若发现学员能跳过 D2 过 TODO 4-6, 说明 starter.ipynb 脚手架过宽, 需收紧 (留空更多)。

---

## v6.0 升级说明

- **v5.0 只有** notes.md / starter.ipynb / solution.ipynb / reading.md / data, 评估依赖 solution.ipynb 对照 (机械层, 测不出辩护与长期保持)
- **v6.0 加** practice.md (D1/D2/D3 刻意练习 + 交叉 interleaving + weak_loop) + tutorial.ipynb (Socratic 口头辩护 + Hattie 四级反馈) + schedule.json (FSRS-6 间隔复习) + alignment.md (Biggs 对齐自检), 把评估从"代码对错"升级为"**代码 + 辩护 + 长期保持**"
- 对齐校验: 每 ILO 都有 >=1 TLA (notes + starter + drill + tutorial) 与 >=1 AT (TODO + drill independent + tutorial辩护), 无孤儿 ILO
