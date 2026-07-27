---
unit: E1-D3
title: 多Agent系统设计 · 建构对齐 (Constructive Alignment, Biggs 1996)
version: v6.0
based_on: Biggs ILO↔TLA↔AT + mastery learning (Bloom 1968, Block 1971)
---

# 多Agent系统设计 · 建构对齐矩阵

> 把「预期学习产出 (ILO)」↔「教学学习活动 (TLA)」↔「评估任务 (AT)」三者对齐, 并设 mastery 阈值。
> 不对齐 = TLA 没训练 ILO, 或 AT 没测量 ILO, 或学生不经 TLA 也能过 AT (对齐失败)。

## ILO ↔ TLA ↔ AT 矩阵

> ILO 编号对应 [`notes.md`](./notes.md) 「学习目标（学完你能做到）」1-6。
> TLA 引用 [`starter.ipynb`](./starter.ipynb) TODO / [`practice.md`](./practice.md) drill / [`tutorial.ipynb`](./tutorial.ipynb) 苏格拉底回合。
> AT 引用 [`solution.ipynb`](./solution.ipynb) 后测 / [`tutorial.ipynb`](./tutorial.ipynb) 退出盲点 / [`practice.md`](./practice.md) 渐进交付。

| ILO (预期学习产出) | TLA (教学学习活动) | AT (评估任务) | mastery_threshold |
|--------------------|-------------------|---------------|-------------------|
| **ILO1** 解释单Agent三瓶颈 (Context Window/角色冲突/专业化) 及多Agent分工如何解决 | 读 `notes.md` 关键回顾1表 + 做 `practice.md` diagnostic D1 先测 + `tutorial.ipynb` 苏格拉底回合1 (追问「为什么 Context Window 是结构性而非工程性瓶颈?」) | `solution.ipynb` 后测题1: 用 200 字解释三瓶颈并各举一营销子案例; `tutorial.ipynb` 退出盲点1 | >=80% (后测题1三瓶颈各至少 60 字且各配一例) |
| **ILO2** 用五种协作模式拓扑图分析营销场景选型 | 读 `notes.md` 关键回顾2五种模式图 + 做 `practice.md` drill D-TOPO-02 阶段1 Worked (教师画 supervisor 有向图) + `tutorial.ipynb` 苏格拉底回合2 (反例追问「若辩论模式用于流水线任务会付出什么代价?」) | `practice.md` progressive_project proposal 阶段 (1页 PDF 描述场景与选型理由) | >=70% (proposal 必须引用 notes.md 五种模式决策树) |
| **ILO3** 用 LangGraph `StateGraph` 构建 supervisor 中心化多Agent拓扑 (4 营销Agent + 条件边) | 做 `starter.ipynb` TODO1 (协议) + TODO2 (4 Agent 节点) + TODO3 (supervisor 拓扑) + `practice.md` drill D-PROTO-01 + D-TOPO-02 阶段2 Faded | `solution.ipynb` 检查 TODO1-3 代码可跑通; `practice.md` milestone 阶段 (Day3+3天交 TODO1-3) | >=80% (milestone 跑通且 supervisor 死循环被修复) |
| **ILO4** 用 networkx 分析 Agent 通信拓扑, 识别瓶颈Agent与单点故障 | 做 `starter.ipynb` TODO5 (networkx 分析) + `practice.md` drill D-EMERGE-03 阶段1 Worked + `tutorial.ipynb` 苏格拉底回合3 (假设变追问「若移除 supervisor 节点连通性如何变化?」) | `solution.ipynb` 检查 TODO5 输出 degree_centrality dict; `practice.md` final 阶段 (含 networkx 指标 + 天道推演映射) | >=80% (degree_centrality 输出正确 + 300字涌现分析含「单点故障」术语) |
| **ILO5** 设计三层通信协议 (传输/格式/语义) + pydantic AgentMessage, 解释 A2A/MCP 互补 | 读 `notes.md` 关键回顾3三层表 + 做 `practice.md` drill D-PROTO-01 三阶段 + `tutorial.ipynb` 苏格拉底回合4 (凭什么追问「pydantic 强类型凭什么比 dict 更适合 A2A 互操作?」) | `solution.ipynb` 检查 TODO1 AgentMessage + MessageType 枚举; `schedule.json` card C1+C5 间隔重复召回 | >=80% (AgentMessage 字段完整 + MessageType 5 值 + 三层归属正确) |
| **ILO6** 用天道推演框架分析多Agent涌现行为 (沙盘↔仿真同构) | 读 `notes.md` 「天道推演视角」对照表 + 做 `practice.md` drill D-EMERGE-03 阶段3 Independent + `tutorial.ipynb` 苏格拉底回合5 (如何追问「如何用沙盘方法在部署前预判拓扑涌现质量?」) | `practice.md` final 阶段 300 字涌现分析 + poster 阶段 (A3 海报含同构说明); `schedule.json` card C7 | >=70% (final 分析含「沙盘」「因果链」「关键节点」天道推演术语) |

## 3 自检问题 (Feed Up / Feed Back / Feed Forward, Hattie & Timperley 2007)

> 教师每周末用这 3 题自检本单元建构对齐是否成立。任一题答「否」即对齐失败, 需修 TLA 或 AT。

### 自检1 (Feed Up): TLA 是否训练 ILO?

- 具体问: `practice.md` drill D-TOPO-02 (supervisor 拓扑构建) 是否真的训练 ILO3 (用 LangGraph 构建 supervisor 中心化拓扑)?
- 验证: drill D-TOPO-02 阶段3 Independent 要求学员独立实现 team 去中心化拓扑, 这预设学员已掌握 supervisor 中心化 (ILO3 核心), 故 TLA→ILO 训练链成立。
- 若否的修法: 若学员在 Independent 阶段大面积卡在 `add_conditional_edges` API, 说明 Faded 阶段练习不足, 需补 1 个 2-Agent 极简 worked example (见 weak_loop 流程)。

### 自检2 (Feed Back): AT 是否测量 ILO?

- 具体问: `solution.ipynb` 后测题1 (200字解释三瓶颈) 是否真的测量 ILO1 (解释单Agent三瓶颈及多Agent分工)?
- 验证: 后测题1 评分细则要求三瓶颈各 60 字且各配一营销子案例, 直接对应 ILO1 的「解释 + 多Agent分工如何解决」, AT→ILO 测量链成立。
- 若否的修法: 若学员能背三瓶颈名但举不出营销子例, 说明 AT 测的是记忆而非理解, 需把后测改为「给定一营销 Brief, 指出单Agent会在哪个瓶颈失败 + 为什么」。

### 自检3 (Feed Forward): 不经 TLA 能过 AT 吗? 若能 = 对齐失败

- 具体问: 学员若不读 `notes.md` 关键回顾2、不做 `starter.ipynb` TODO3、不练 drill D-TOPO-02, 能直接过 `solution.ipynb` 后测题 (构建 supervisor 拓扑) 吗?
- 验证: 后测题要求用 `StateGraph` + `add_conditional_edges` 真实写代码并跑通, 不经 TLA 无法凭空写出 API 调用 (LangGraph API 非通用知识), 对齐成立。
- 若否的修法: 若 AT 改为「画一张 supervisor 拓扑示意图」(无需代码), 则不经 TLA 也能凭直觉画图过 AT, 此时对齐失败, 需把 AT 改回真实代码实现或 networkx 指标计算。

## mastery 学习原则 (Bloom 1968, Block 1971)

- **不进位原则**: ILO3 未达 >=80% mastery, 不进入 ILO4 (networkx 分析依赖拓扑已构建); ILO5 未达 80% 不进入 ILO6 (天道推演映射依赖协议+拓扑+涌现三维已稳)。
- **补救而非加速**: 未达 mastery 的学员走 `practice.md` weak_loop (回退 + 补 worked example), 而非跳到下一 ILO。
- **进步而非排名**: AT 评分用绝对阈值 (>=80%) 而非相对排名 (前 30%), 与天道推演「谦虚承认不确定性」一致--mastery 是个人达成的, 不是与他人比较的。

---

*本建构对齐矩阵为 v6.0 学习科学层新增, 不修改 v5.0 的 notes.md/starter.ipynb/solution.ipynb/reading.md/data。*
*最后更新: 2026-07-26*
