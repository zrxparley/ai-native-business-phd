---
unit: U-E1-D2
title: Agent框架对比 · 刻意练习 (Deliberate Practice)
version: v6.0
algorithm: Ericsson deliberate practice + MIT worked-faded + Harvard/Stanford interleaving
skill_target: 能用LangGraph的StateGraph/create_react_agent与CrewAI/AutoGen API结构在同一营销任务(透肌精华竞品分析)上实现并对比ReAct vs Plan-Execute两种编排范式, 用天道推演因果链识别不可逆点并完成框架选型论证
---

# practice.md · 刻意练习 (Ericsson + MIT Worked-Faded + Harvard/Stanford Interleaving)

> 本文件落实 Ericsson 刻意练习三要素(精准子技能/即时反馈/重复到自动化) + MIT pset0-style worked-faded scaffold + Harvard/Stanford 交叉练习。所有 drill 的 feedback_rule 锚定本单元真实库(LangGraph StateGraph / create_react_agent / CrewAI Agent-Task-Crew / AutoGen ConversableAgent-GroupChat)与真实营销任务(透肌精华竞品分析+策略生成)。

---

## 一、Diagnostic (先测, CS229 pset0-style, 3题)

> 答题前不可翻 notes.md/solution.ipynb。目的: 探测先验缺口, 决定从哪个 drill 起步。

**D1 (先验-图论基础)**
LangGraph 的 `StateGraph` 中, `add_node("plan", plan_fn)` 与 `add_conditional_edges("plan", router_fn, {"need_tool": "execute", "done": "END"})` 分别定义了图的哪两类要素? 若漏写 `add_edge(START, "plan")` 会发生什么?

**D2 (先验-框架语义)**
给定 CrewAI 的 `Agent(role="竞品调研员", goal="...", backstory="...")` 与 `Task(description="...", expected_output="...", agent=调研员)`, 请用一句话说明 CrewAI 的"控制流"由谁决定, 与 LangGraph 的"开发者显式定义图结构"有何本质差异?

**D3 (先验-因果链)**
在 LangGraph Plan-Execute 范式中, "plan_node 一次性规划 4 步"是因果链上的哪一类节点? 为什么说它是**不可逆点**? 若 plan 阶段前提假设错误, execute 阶段能否动态纠偏?

> 评分: 每题 0/1/2 分(共 6 分)。<=2 分从 drill A1 起步; 3-4 分从 B1 起步; 5-6 分直接进 C1。

---

## 二、Subskills (3 个可观察子技能, subskills)

> subskills 拆解原则: 每个子技能必须可观察、可评估, 与 ILO 一一映射。

| ID | 子技能 | 可观察行为 | 关联 ILO |
|----|--------|-----------|---------|
| S-A | **图结构编排** | 能用 `StateGraph` + `add_node` + `add_conditional_edges` 显式定义 ReAct 与 Plan-Execute 两种工作流图, 节点/边/条件分支无遗漏 | ILO2, ILO3 |
| S-B | **角色化/对话式 API 静态分析** | 能徒手写出 CrewAI `Agent/Task/Crew` 与 AutoGen `ConversableAgent/GroupChat` 的 API 结构, 标注与 LangGraph 的语义差异 | ILO4, ILO5 |
| S-C | **因果链选型推演** | 能用天道推演沙盘在同一营销任务上模拟 4 框架的行为路径, 标注不可逆点/收敛风险/适用边界, 给出选型结论 | ILO1, ILO6 |

---

## 三、Drills (>=3, 每个 worked->faded->independent 三阶段)

### Drill A1 (S-A, difficulty=3, reps_required=3)
**目标**: 用 LangGraph `StateGraph` 实现 Plan-Execute 范式于透肌精华竞品分析任务。

- **Worked (完整示范)**: 给出 `plan_node`(一次性产出 4 步: search_product_info -> analyze_competitor -> write_strategy -> END) + `execute_node`(按 plan 顺序调工具) + `add_conditional_edges("execute", lambda s: "plan" if s["step"]<len(s["plan"]) else "END")` 的完整代码, 学生逐行注释每行的图论语义。
- **Faded (部分填空)**: 抽空 `add_conditional_edges` 的 router_fn 与 `add_edge(START, "plan")`, 学生补全。
- **Independent**: 仅给任务描述"用 Plan-Execute 模式让 Agent 完成 search_product_info -> analyze_competitor -> write_strategy", 学生独立写完 StateGraph。
- **feedback_rule (领域特定)**: 运行后检查 (a) `END` 是否可达 (b) `StateGraph` 是否 compile 通过 (c) 营销工具调用顺序是否符合 plan。若 (a) 失败 -> 提示"条件边 router 缺 `END` 分支"; 若 (c) 顺序错 -> 提示"plan_node 产出的 list 顺序决定 execute 顺序, 这是 Plan-Execute 的不可逆点"。
- **weak-loop 触发**: 若连续 2 次 compile 失败 -> 回退到 Worked 阶段 + 补充 `MemorySaver` 持久化示例。

### Drill B1 (S-B, difficulty=2, reps_required=2)
**目标**: 徒手写出 CrewAI 与 AutoGen 的等价 API 结构(含 import guard), 不依赖真实安装。

- **Worked**: 给出 CrewAI 四角色(调研员/分析师/策略师/撰写人) + 四 Task + `Crew(agents, tasks, process="sequential")` 完整结构, 及 AutoGen `GroupChat(agents=[调研员, 分析师, 策略师, 撰写人], messages=[], max_round=6)` + `GroupChatManager` 完整结构。
- **Faded**: 抽空 `Task(..., agent=..., context=...)` 的 context 依赖与 `GroupChat` 的 `max_round`。
- **Independent**: 给定"为透肌精华任务设计一个 CrewAI 方案 + 一个 AutoGen 方案", 学生独立写两段 API 结构并标注语义差异。
- **feedback_rule (领域特定)**: 检查 (a) CrewAI 的 `context` 依赖链是否构成有向无环图(无循环 Task 依赖); (b) AutoGen 的 `max_round` 是否设置(防止无限讨论); (c) 两个方案是否都引用了 `search_product_info`/`analyze_competitor`/`write_strategy` 三个营销工具。若 (b) 漏 -> 提示"AutoGen 的因果风险: max_round 耗尽仍未共识是关键不可逆点"。
- **weak-loop 触发**: 若连续 2 次 context 依赖成环 -> 回退 Worked + 补充 CrewAI `process="hierarchical"` 示例。

### Drill C1 (S-C, difficulty=4, reps_required=2)
**目标**: 用天道推演沙盘在同一透肌精华任务上模拟 4 框架行为路径, 产出选型论证(300字)。

- **Worked**: 给出 notes.md 中四框架因果链推演模板(感知->因果节点->不可逆点->风险->适用边界), 学生套用模板填 ReAct 与 Plan-Execute 两条时间线。
- **Faded**: 抽空 CrewAI 与 AutoGen 两条时间线的"不可逆点"与"适用边界"。
- **Independent**: 仅给任务"同一个营销任务, 你在 4 框架中选哪个? 用天道推演因果链视角说明", 学生独立产出 300 字论证 + 2-3 个认知盲点。
- **feedback_rule (领域特定)**: 检查 (a) 是否标注每条时间线的不可逆点(如 Plan-Execute 的 plan_node / AutoGen 的 max_round 耗尽 / CrewAI 的角色定义错误); (b) 是否给出 2-3 个差异化策略选项(而非单一结论); (c) 是否承认不确定性(如 StubLLM 无法真实模拟 LLM 推理质量)。若 (a) 漏 -> 提示"回看 notes.md 天道推演节, 每条路径必含不可逆点"。
- **weak-loop 触发**: 若连续 2 次只给单一结论 -> 回退 Worked + 补充"反事实"思维提示("如果不选这个框架, 会怎样?")。

---

## 四、Progressive Project (CS230 式, proposal->milestone->final->poster)

**PP-Proposal (Day 2 当天交, 1页)**: 选定一个营销任务(透肌精华/竞品分析/策略生成三选一或自定), 写明 (a) 用哪 2 个框架对比 (b) 评估指标(步数/工具调用次数/输出质量/不可逆点数) (c) 预期选型结论。

**PP-Milestone (Day 2 +3 天)**: 提交 LangGraph ReAct 与 Plan-Execute 两版真实可运行代码(可用 StubChatModel), 跑通同一营销任务, 记录步数/调用次数对比表。

**PP-Final (Day 2 +7 天)**: 提交 (a) 4 框架对比表(含 CrewAI/AutoGen 静态 API 结构) (b) 天道推演沙盘推演 3 条时间线 (c) 300 字选型论证 + 认知盲点。

**PP-Poster (Day 2 +10 天, 1 页 A3)**: 可视化呈现 (a) 4 框架设计哲学雷达图 (b) 同一营销任务的 4 条因果链对比图 (c) 选型决策树。poster 须能让未学本单元的同学 5 分钟内理解。

---

## 五、Interleaving (交叉排布, 非块状)

> 块状练习(A1A1A1-B1B1-C1C1)迁移效果差。本单元采用 A1-B1-C1-A2-B2-C2-A3-B3-C3 交叉排布, 每次切换强制 retrieval:

| 顺序 | 任务 | 切换提示(retrieval 触发) |
|------|------|--------------------------|
| 1 | A1 Worked | (起点) 回想 D1: StateGraph 的节点与边分别是什么? |
| 2 | B1 Worked | 切换: 刚写完图结构, 现在用 CrewAI 的"角色+任务"语义重写同一任务, 两者控制流谁决定? |
| 3 | C1 Worked | 切换: 推演 A1 与 B1 两条路径的不可逆点分别在哪? |
| 4 | A1 Faded | 切换回 A1: 不看 Worked, 默写 `add_conditional_edges` 的 router_fn。 |
| 5 | B1 Faded | 切换回 B1: 默写 `Task.context` 依赖, 与 A1 的条件边有何异同? |
| 6 | C1 Faded | 切换回 C1: 推演 CrewAI 与 AutoGen 两条时间线的不可逆点。 |
| 7 | A1 Independent | 切换回 A1: 独立写完 Plan-Execute StateGraph。 |
| 8 | B1 Independent | 切换回 B1: 独立写 CrewAI + AutoGen 两套 API 结构。 |
| 9 | C1 Independent | 切换回 C1: 独立产出 300 字选型论证。 |

> 每次切换 = 一次 retrieval practice(提取练习), 迁移效果优于重读。

---

## 六、Retry Policy (CS230 式)

- **10 free late days**: 整个选修 E1 共 10 天迟到额度, 自由分配, 不罚分。
- **失败重试不罚分**: Drill 未通过(worked/faded/independent 任一阶段失败)可无限重试, 取最高分。
- **weak-loop 触发后**: 不计迟到, 额外给 3 天补 worked example 后再重试。
- **PP 阶段不可 retry**: Proposal/Milestone/Final/Poster 一旦提交即锁定, 防止"无限重试导致不收敛"。仅 Final 可用 1 次 retry(扣 10% 分)。

---

## 七、Weak-Loop (连续 2 次失败触发, weak_loop / 弱项循环)

触发条件: 同一 drill 的同一阶段(independent)连续 2 次未通过 feedback_rule。

处理流程:
1. **回退上一阶段**: independent -> faded -> worked。
2. **补充 worked example**: 针对失败点补充 1 个 worked example(如 A1 失败 -> 补充 `MemorySaver` 持久化示例; B1 失败 -> 补充 `process="hierarchical"` 示例; C1 失败 -> 补充"反事实"思维示例)。
3. **重做 independent**: 用**新变体**(不同营销任务, 如把透肌精华换成另一个竞品), 防止"记住答案而非理解"。
4. **记录 student_model.json**: 在 tutorial.ipynb 的 student_model 中标记该子技能为 weak, 下次 tutorial 优先追问。

---

## 八、Mastery Threshold

| 子技能 | mastery 条件 |
|--------|-------------|
| S-A | A1 Independent 一次通过 + PP-Milestone 两版代码可运行 + 步数对比表无遗漏 |
| S-B | B1 Independent 一次通过 + PP-Final 含 CrewAI/AutoGen 静态 API 结构 |
| S-C | C1 Independent 一次通过 + PP-Final 300 字论证含 >=2 策略选项 + >=2 认知盲点 |

未达 mastery 不可进入 Day 3(多 Agent 系统设计)。

---

*本文件遵循 Ericsson 刻意练习 + MIT worked-faded + Harvard/Stanford interleaving。mastery 阈值与建构对齐见 alignment.md。*
