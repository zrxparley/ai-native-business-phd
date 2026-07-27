---
unit: U-E1-D2
title: Agent框架对比 · 建构对齐 (Constructive Alignment)
version: v6.0
framework: Biggs constructive alignment (ILO <-> TLA <-> AT) + mastery learning
---

# alignment.md · 建构对齐 (Biggs ILO <-> TLA <-> AT + Mastery)

> 本文件落实 Biggs 建构对齐: 预期学习产出(ILO) -> 教学学习活动(TLA) -> 评估任务(AT) 三者闭环, 每行附 mastery 阈值。所有 TLA 引用本单元真实库(LangGraph/CrewAI/AutoGen)与真实营销任务(透肌精华竞品分析)。

---

## 一、ILO <-> TLA <-> AT 矩阵 (>=3 行)

| ILO (预期学习产出) | TLA (教学学习活动) | AT (评估任务) | mastery_threshold |
|--------------------|--------------------|---------------|-------------------|
| **ILO1**: 能解释四大框架(LangGraph/CrewAI/AutoGen/MetaGPT)设计哲学差异(Agent即图/角色/对话者/流程), 在营销场景准确选型 | 读 notes.md §四框架设计哲学对比表 + practice.md Drill C1 worked/faded (天道推演沙盘推演 4 框架时间线) + tutorial.ipynb 苏格拉底追问"凭什么选这个框架?" | PP-Final 300 字选型论证(透肌精华任务) + tutorial.ipynb 后测盲点列表 | >=80% 论证含 >=2 策略选项 + >=2 认知盲点 + 引用不可逆点 |
| **ILO2**: 能用 LangGraph `StateGraph` 显式定义 Agent 工作流图(节点+边+条件分支), 用 `create_react_agent` 构建 ReAct Agent | starter.ipynb TODO2/TODO3 填空 + practice.md Drill A1 worked->faded->independent (StateGraph 实现 Plan-Execute) + tutorial.ipynb 苏格拉底追问"漏写 add_edge(START,plan) 会怎样?" | PP-Milestone: ReAct 与 Plan-Execute 两版可运行代码 + 步数/调用次数对比表 | >=80% 两版代码 compile 通过 + END 可达 + 对比表无遗漏 |
| **ILO3**: 能用 LangGraph 实现 Plan-Execute 模式(plan_node+execute_node+条件边), 与 ReAct 在同一营销任务对比 | starter.ipynb TODO3/TODO4 + practice.md Drill A1 (Plan-Execute 不可逆点识别) + tutorial.ipynb 苏格拉底追问"plan 阶段前提错误, execute 能纠偏吗?" | PP-Final: 4 框架对比表(含步数/调用次数/不可逆点数) | >=80% 对比表含 4 框架 + 不可逆点标注 + Plan-Execute 复兴前沿点 |
| **ILO4**: 能读写 CrewAI Agent/Task/Crew API 结构(角色化协作), 即便未安装也能静态分析设计哲学 | starter.ipynb TODO5 (CrewAI API 结构, 含 import guard) + practice.md Drill B1 worked (四角色+四Task+Crew) + tutorial.ipynb 苏格拉底追问"CrewAI 控制流由谁决定?" | PP-Final: CrewAI 静态 API 结构 + 与 LangGraph 语义差异标注 | >=80% API 结构完整 + context 依赖成 DAG + 语义差异标注 |
| **ILO5**: 能读写 AutoGen ConversableAgent/GroupChat API 结构(对话驱动), 理解多 Agent 讨论适用边界 | starter.ipynb TODO6 (AutoGen API 结构) + practice.md Drill B1 faded (max_round 设置) + tutorial.ipynb 苏格拉底追问"max_round 耗尽未共识怎么办?" | PP-Final: AutoGen 静态 API 结构 + 适用边界论证 | >=80% API 结构完整 + max_round 设置 + 适用边界标注 |
| **ILO6**: 能用天道推演框架分析"同一营销任务、不同框架实现"因果链差异, 识别高杠杆点和不可逆节点 | notes.md §天道推演视角 + practice.md Drill C1 (沙盘模拟 4 框架时间线) + tutorial.ipynb 苏格拉底追问"如果不选这个框架, 会怎样?"(反事实) | PP-Final: 3 条时间线推演 + 高杠杆点/不可逆点标注 | >=80% 含 3 条时间线 + 不可逆点 + 反事实分析 |

---

## 二、3 自检问题 (Feed Up / Feed Back / Feed Forward)

> Biggs 建构对齐的三阶反馈。若任一问题答"否", 对齐失败, 需回到 TLA 修订。

### Q1 (Feed Up): TLA 是否训练 ILO?
- **检查**: practice.md Drill A1 是否真的让学生用 `StateGraph` 写图? 是(worked/faded/independent 三阶段都写真实 LangGraph API)。Drill B1 是否真让学生写 CrewAI/AutoGen API? 是(worked 给完整结构, faded 抽空 context/max_round, independent 独立写)。
- **结论**: TLA 与 ILO1-6 一一对应, **是**。

### Q2 (Feed Back): AT 是否测量 ILO?
- **检查**: PP-Milestone(两版可运行代码+对比表)是否测量 ILO2/ILO3? 是(代码可运行=能用 StateGraph; 对比表=能对比 ReAct/Plan-Execute)。PP-Final(4 框架对比表+300字论证+3 时间线)是否测量 ILO1/ILO4/ILO5/ILO6? 是(4 框架=ILO1/4/5; 论证=ILO1; 时间线=ILO6)。
- **结论**: AT 与 ILO 一一映射, **是**。

### Q3 (Feed Forward): 不经 TLA 能过 AT 吗? (若能 = 对齐失败)
- **检查**: 学生若不读 notes.md 四框架对比表、不做 starter.ipynb TODO2/3/5/6、不练 practice.md Drill A1/B1/C1, 能直接产出 PP-Final 的 4 框架对比表+300字论证+3 时间线吗?
  - 不经 Drill A1 -> 不会写真实 StateGraph, PP-Milestone 代码跑不通。
  - 不经 Drill B1 -> 不知 CrewAI `context` 依赖与 AutoGen `max_round`, PP-Final API 结构残缺。
  - 不经 Drill C1 -> 不知天道推演沙盘模板, PP-Final 3 时间线无法产出。
- **结论**: 不经 TLA **不能**过 AT, 对齐**成立**。

---

## 三、Mastery 阈值总览 (防"未达 mastery 进入 Day 3")

| 子技能 | mastery 条件 | 未达后果 |
|--------|-------------|---------|
| S-A (图结构编排) | A1 Independent 一次通过 + PP-Milestone 两版代码可运行 | 不可进 Day 3 (Day 3 多 Agent 系统需 StateGraph 基础) |
| S-B (角色化/对话式 API) | B1 Independent 一次通过 + PP-Final 含 CrewAI/AutoGen 静态 API | 不可进 Day 3 (Day 3 需 AutoGen GroupChat 基础) |
| S-C (因果链选型推演) | C1 Independent 一次通过 + PP-Final 300 字论证含 >=2 策略 + >=2 盲点 | 不可进 Day 3 (Day 3 需天道推演冲突解决能力) |

> mastery 未达 -> 触发 practice.md weak-loop (回退 worked + 补充 example + 重做 independent 用新变体)。

---

## 四、与 v5.0 starter/solution 的对齐验证

| starter.ipynb TODO | 对应 ILO | 对应 Drill | solution.ipynb 验证 |
|--------------------|---------|-----------|---------------------|
| TODO1 (营销工具+StubChatModel) | ILO2 前置 | A1 worked 前置 | solution TODO1 提供工具定义 |
| TODO2 (create_react_agent ReAct) | ILO2 | A1 | solution TODO2 提供 ReAct 实现 |
| TODO3 (StateGraph Plan-Execute) | ILO3 | A1 | solution TODO3 提供 plan/execute/条件边 |
| TODO4 (ReAct vs Plan-Execute 对比) | ILO3 | A1+C1 | solution TODO4 提供对比表 |
| TODO5 (CrewAI API 结构) | ILO4 | B1 | solution TODO5 提供四角色+四Task+Crew |
| TODO6 (AutoGen API 结构+四框架对比表) | ILO5/ILO1 | B1+C1 | solution TODO6 提供 GroupChat+对比表 |

> 验证: 6 个 TODO 全部映射到 ILO/Drill, 无"孤立 TODO"(对齐无遗漏)。

---

*本文件遵循 Biggs 建构对齐 + Bloom mastery learning。mastery 阈值与 worked-faded 见 practice.md, 间隔重复见 schedule.json, 苏格拉底追问见 tutorial.ipynb。*
