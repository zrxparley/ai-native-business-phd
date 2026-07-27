# Constructive Alignment · Day 3 人机协作治理 + 组织变革

> v6.0 学习科学层：Biggs 建构对齐 (Constructive Alignment) — ILO ↔ TLA ↔ AT 三者一致，避免"教了不考、考了没教"。
> 研究依据：Biggs & Tang (2011) *Teaching for Quality Learning at University* 4th ed.; Hattie & Timperley (2007) *Review of Educational Research* 77(1):81-112 三问 (Feed Up / Feed Back / Feed Forward)。

---

## ILO ↔ TLA ↔ AT 矩阵

| ILO (预期学习产出 Intended Learning Outcome) | TLA (教学学习活动 Teaching/Learning Activity) | AT (评估任务 Assessment Task) | mastery_threshold |
|---|---|---|---|
| **ILO1**：能用 **pandas** 加载人机协作审计日志，按分工模式多维聚合，计算人工干预率/Agent自主完成率/人工修正率，定位"AI成熟度被高估"的任务 | starter.ipynb TODO1 + practice.md D1 Worked→Faded→Independent + schedule.json C1/C2 间隔复习 + tutorial.ipynb Socratic 第 1-2 轮 | solution.ipynb TODO1 输出 + practice.md D1 Independent 阶段"哪类任务 AI 成熟度被高估"一句话结论 + 300 字分析 | >=80% 干预率计算正确 + 结论有数据支撑 |
| **ILO2**：能用 **networkx** 构建组织协作网络（含 Agent 节点），计算 degree_centrality 与 betweenness_centrality，识别枢纽与桥接节点（信息瓶颈） | starter.ipynb TODO3 + practice.md D2 Worked→Faded→Independent + schedule.json C3 间隔复习 + tutorial.ipynb Socratic 第 3 轮 | solution.ipynb TODO3 网络图 + practice.md D2 Independent 阶段"哪个节点是信息瓶颈 + 移除后连通性变化" | >=70% 中心性计算正确 + 桥接节点识别正确 |
| **ILO3**：能用 **McKinsey 7S** 评估组织 AI 就绪度 + **ADKAR** 诊断变革阻力阶段 + **天道推演**做 3 层沙盘推演（immediate→near→far），输出高杠杆干预点 + 2-3 条时间线 + 黑天鹅预警 | starter.ipynb TODO4/5/6 + practice.md D3 Worked→Faded→Independent + schedule.json C4/C5/C6 间隔复习 + tutorial.ipynb Socratic 第 4 轮 + progressive_project Final 阶段 | solution.ipynb TODO4/5/6 + practice.md D3 Independent 阶段完整沙盘 + progressive_project Poster（1 页 A3 + 3 分钟话术） | >=70% 7S+ADKAR 评分合理 + 天道推演 >=3 条时间线 + 1 个高杠杆点 |
| **ILO4**：能解释人机分工矩阵二维框架（任务复杂度 × AI成熟度）+ AI 治理四要素（数据/模型/流程/人员）+ 审计日志作为"黑匣子"的治理角色 | notes.md 关键回顾 1-3 + reading.md 深链 + schedule.json C1 间隔复习 + tutorial.ipynb pre-task | tutorial.ipynb 后测 + 2 分钟话术（向 AI 伦理委员会汇报） | 能口头辩护 >=3 个追问 |

---

## mastery_threshold 说明

- **>=80%**（ILO1）：pandas 是事实标准工具，干预率计算是治理决策的基础，阈值高
- **>=70%**（ILO2/ILO3）：networkx + 7S/ADKAR/天道推演 综合度高，允许部分推理瑕疵
- **口头辩护**（ILO4）：参考 Oxford tutorial 标准，能在 >=3 个 Socratic 追问下不自相矛盾

未达 threshold 触发 practice.md 的 weak_loop（回退 + worked example + 24h 间隔 retry）。

---

## 3 自检问题 (Biggs 三问 × Hattie 4 级)

### 1. Feed Up — TLA 是否训练 ILO？（学生知道"在练什么"吗？）

- [ ] practice.md 每个 drill 是否明确标注训练的 subskill（S1/S2/S3）？
- [ ] starter.ipynb 每个 TODO 是否在 notes.md 关键回顾中有理论锚点？
- [ ] tutorial.ipynb 每轮 Socratic 追问是否对应一个 ILO？

### 2. Feed Back — AT 是否测量 ILO？（学生知道"做得怎么样"吗？）

- [ ] solution.ipynb 是否提供可对照的参考答案（非唯一解）？
- [ ] practice.md 的 feedback_rule 是否引用具体框架（pandas审计日志/McKinsey 7S/ADKAR/networkx/天道推演）而非泛泛"再想想"？
- [ ] tutorial.ipynb 的 Hattie 四级反馈是否覆盖 [TASK]/[PROCESS]/[SELF-REG]/[FEED-FORWARD]？

### 3. Feed Forward — 不经 TLA 能过 AT 吗？（若能 = 对齐失败）

- [ ] 学生不练 pandas groupby 能直接过 TODO1 吗？若能 = TODO1 太简单，加难
- [ ] 学生不做天道推演沙盘能过 TODO6 吗？若能 = TODO6 只要套模板，要求独立设计 3 层
- [ ] 学生不看 reading.md 能过 2 分钟话术吗？若能 = 话术题目太浅，要求引用 >=1 个 2026 前沿点（Agentic Organization / computer use 审计 / 多Agent仿真）

---

## 跨单元对齐（与 Day 1-2 / Day 4 / 技能5 衔接）

| 本单元 ILO | 上游（Day 1-2）| 下游（Day 4 / 技能5）|
|---|---|---|
| ILO1 pandas 审计日志 | Day 1-2 Agent 能力分析 | Day 4 架构参考设计的治理层 |
| ILO2 networkx 协作网络 | Day 1-2 Agent 编排架构 | 技能5 生产化可观测性的业务层 |
| ILO3 天道推演×组织变革 | Day 1-2 流程驱动→智能驱动 | Day 4 行动研究的推演工具 |
| ILO4 分工矩阵 + 治理四要素 | Day 1-2 Agent 能力边界 | Day 4 治理体系基础 |

---

## v6.0 升级说明

本 alignment.md 是 v5.0 之上新增的建构对齐层。v5.0 的"学习目标 + 上机任务 + 作业评估"已有对齐雏形，v6.0 显式化为 ILO↔TLA↔AT 矩阵 + mastery_threshold + 3 自检，并用 Hattie 三问（Feed Up/Back/Forward）做形成性反馈锚点。
