---
unit: U5-D2
title: LangGraph 编排实战 - 建构对齐 (Constructive Alignment)
version: v6.0
framework: Biggs ILO ↔ TLA ↔ AT + mastery threshold
---

# alignment.md · LangGraph 编排建构对齐

## 核心命题

> Biggs 建构对齐 (Constructive Alignment): 预期学习产出 (ILO) ↔ 教学学习活动 (TLA) ↔ 评估任务 (AT) 三者必须对齐。学生不经 TLA 训练就无法过 AT = 对齐成功；若不经 TLA 也能过 AT，说明 AT 太浅 = 对齐失败。

本单元的 ILO 来自 `notes.md` § 学习目标（5 条），TLA 引用 `starter.ipynb` 的 TODO 填空脚手架 + `practice.md` 的 drill，AT 引用 `solution.ipynb` 后测 + `tutorial.ipynb` Socratic 追问。

---

## ILO ↔ TLA ↔ AT 矩阵

| ILO (预期学习产出) | TLA (教学学习活动) | AT (评估任务) | mastery_threshold |
|--------------------|--------------------|---------------|-------------------|
| **ILO1**: 能用 `StateGraph`/`Node`/`Edge` 三要素解释有状态有向图如何替代线性 Chain，指出营销多Agent场景中各要素对应的代码对象 | `starter.ipynb` TODO1 (定义 MarketingState TypedDict) + `practice.md` D-STATE drill (Worked->Faded->Independent) + `notes.md` § 关键回顾 1 三要素表 | `solution.ipynb` cell 2-3 结构对照 (TODO1 填对 8 字段) + `tutorial.ipynb` cell 3 Socratic 问"MarketingState 属于三要素哪一层" | >=80% (8 字段全对 + 三要素归类正确) |
| **ILO2**: 能为"分析->策略->内容->审核->发布"工作流画出状态图，识别条件边与循环退出条件，说明为何任何循环都必须有退出条件 | `starter.ipynb` TODO4 (should_approve 条件函数 + add_conditional_edges 注册) + `practice.md` D-ROUTE drill + `notes.md` § 关键回顾 2 状态图 ASCII | `solution.ipynb` cell 5 条件路由结构对照 + 作业"300 字分析 revision_count>=3 设成多少合理" + `tutorial.ipynb` cell 3 Socratic 问"删掉退出条件会怎样" | >=80% (条件函数 + 注册 + 退出条件三者齐全) |
| **ILO3**: 能在真实 LangGraph 库上完成"定义 State -> 写节点函数 -> 装配图 -> 编译 -> stream 运行"全流程，解释 MemorySaver 检查点作用 | `starter.ipynb` TODO2-3-5 (analysis/strategy/content agent + build_marketing_graph) + `practice.md` D-ASSEMBLE drill (Worked->Faded->Independent) + `data/README.md` langchain-academy 课程 | `solution.ipynb` cell 4-6 完整装配对照 + `verify_unit.py` 第 3 条 TODO 数检查 + `tutorial.ipynb` cell 3 Socratic 问"compile(checkpointer=MemorySaver()) 的作用" | >=80% (4 个 add_node + 3 条 add_edge + 1 条 conditional + compile 全对) |
| **ILO4**: 能用 `add_conditional_edges` + `interrupt` 实现"审核不通过回内容Agent重生成"的条件循环与人机协作 (HITL) | `starter.ipynb` TODO6 (interrupt 替换 review_node) + `practice.md` D-HITL drill (Worked->Faded->Independent) + `notes.md` § 关键回顾 3 interrupt/Command 代码片段 | `solution.ipynb` cell 6 HITL 演示对照 + 作业"用 interrupt 实现真人工审核"交付物 + `tutorial.ipynb` cell 3 Socratic 问"interrupt 在节点内还是节点外调用" | >=80% (interrupt 在节点内调用 + Command(resume=...) 恢复可复现) |
| **ILO5**: 能用"多Agent仿真 × 天道推演"视角，把项目 CLAUDE.md 天道推演沙盘映射为可计算的 LangGraph 多Agent博弈图 | `notes.md` § 2026 前沿补充 (节点-能力映射表) + `reading.md` 深链 + `practice.md` progressive_project poster 阶段 | 作业"(可选) 增加消费者Agent节点画新状态图"交付物 + `tutorial.ipynb` cell 3 Socratic 问"analysis_agent 对应天道推演哪一能力" | >=70% (poster 同伴互评 >=3 人能复述映射) |

---

## 3 自检问题 (Feed Up / Feed Back / Feed Forward)

### 自检 1: Feed Up (TLA 是否训练 ILO?)
- **问题**: `starter.ipynb` 的 6 个 TODO + `practice.md` 的 4 个 drill，是否真的训练了 ILO1-5？
- **自答**:
  - TODO1/Drill D-STATE 训练 ILO1 (三要素) ✓
  - TODO2-3/Drill D-ASSEMBLE 训练 ILO3 (全流程装配) ✓
  - TODO4/Drill D-ROUTE 训练 ILO2 (条件边+退出) ✓
  - TODO5/Drill D-ASSEMBLE 训练 ILO3 (compile) ✓
  - TODO6/Drill D-HITL 训练 ILO4 (interrupt HITL) ✓
  - poster + 2026 前沿补充训练 ILO5 (天道推演映射) ✓
- **判定**: 5/5 ILO 均有 TLA 覆盖，无遗漏。Feed Up 通过。

### 自检 2: Feed Back (AT 是否测量 ILO?)
- **问题**: `solution.ipynb` 结构对照 + `tutorial.ipynb` Socratic 追问 + 作业交付物，是否真的测量了 ILO1-5，而非只测记忆？
- **自答**:
  - ILO1 测量: solution cell 2-3 字段对照（测识别）+ tutorial Socratic"三要素哪一层"（测归类推理）-- 超越记忆 ✓
  - ILO2 测量: 作业"revision_count>=3 设多少合理"（测反事实推理）+ tutorial"删掉退出条件会怎样"（测系统行为预测）-- 高阶 ✓
  - ILO3 测量: verify_unit.py TODO 数检查（测结构完整）+ tutorial"compile 作用"（测机制理解）-- 双层 ✓
  - ILO4 测量: HITL 暂停-恢复可复现（测可运行性）+ tutorial"interrupt 在节点内还是外"（测 API 细节）-- 实操+细节 ✓
  - ILO5 测量: poster 同伴互评（测可复述性）+ tutorial"analysis_agent 对应天道推演哪能力"（测映射）-- 迁移 ✓
- **判定**: 5/5 ILO 均有 AT 测量，且 AT 含推理/反事实/可运行性，非纯记忆。Feed Back 通过。

### 自检 3: Feed Forward (不经 TLA 能过 AT 吗? 若能 = 对齐失败)
- **问题**: 一个学生**不写** `starter.ipynb` TODO、**不做** `practice.md` drill、**不读** `notes.md` 关键回顾，能直接过 AT 吗？
- **自答**:
  - ILO1 AT: 不读三要素表，无法说出 MarketingState 属于"State"层而非"StateGraph"-- 不过 ✓
  - ILO2 AT: 不写 TODO4，无法反事实推理"删退出条件死循环"的具体机制（review->content->review 无限）-- 不过 ✓
  - ILO3 AT: 不写 TODO5，无法解释 compile(checkpointer=MemorySaver()) 为何要传 checkpointer-- 不过 ✓
  - ILO4 AT: 不写 TODO6，无法演示 interrupt 在节点内调用的暂停-恢复，会被 tutorial Socratic"节点内还是节点外"问穿 -- 不过 ✓
  - ILO5 AT: 不读 2026 前沿补充，无法说出 analysis_agent 对应局势感知-- 不过 ✓
- **判定**: 5/5 ILO 的 AT 均需经 TLA 训练才能通过，无"裸过"通道。Feed Forward 通过，对齐成功。

---

## mastery_threshold 说明

- **>=80%**: ILO1-4 的 AT 全对 80% 以上 = mastery 达标，可进入 Day 3 评估与 Benchmarking
- **70-79%**: 触发 `practice.md` weak_loop，回退上一 drill + 补 Worked example
- **<70%**: 重做 `practice.md` 全部 drill，并预约 `tutorial.ipynb` Socratic session
- **ILO5 特例**: 天道推演映射为高阶迁移目标，阈值放宽到 70%（poster 同伴互评 >=3 人复述即可），不阻塞 Day 3

---

## 与 v6.0 其他文件的对齐

| alignment.md 元素 | 对应文件 |
|-------------------|----------|
| ILO1-5 | `notes.md` § 学习目标 (5 条) |
| TLA (TODO1-6) | `starter.ipynb` (6 个 TODO 填空) |
| TLA (drill D-STATE/ROUTE/ASSEMBLE/HITL) | `practice.md` (4 个 drill) |
| AT (结构对照) | `solution.ipynb` (10 cells) |
| AT (Socratic 追问) | `tutorial.ipynb` (cell 3) |
| AT (间隔重复保持) | `schedule.json` (6 cards, FSRS-6) |
| mastery_threshold | `practice.md` retry_policy + weak_loop |

---

*本对齐矩阵基于 Biggs 建构对齐理论 + Bloom 可观察动词 + mastery learning 阈值。所有 ILO/TLA/AT 对象均引用本单元真实文件 (notes.md/starter.ipynb/solution.ipynb/practice.md/tutorial.ipynb/schedule.json)，非通用模板。*
