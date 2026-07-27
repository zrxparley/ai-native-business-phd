# Constructive Alignment - Day 5 数据治理与 SQL (v6.0)

> Biggs 建构对齐: ILO (预期学习产出 Intended Learning Outcomes) ↔ TLA (教学学习活动 Teaching/Learning Activities) ↔ AT (评估任务 Assessment Tasks). 三者必须对齐 - TLA 训练 ILO, AT 测量 ILO, 不经 TLA 不能过 AT.

## ILO ↔ TLA ↔ AT 矩阵

| ILO (预期学习产出) | TLA (教学学习活动) | AT (评估任务) | mastery_threshold |
|---|---|---|---|
| ILO1: 能用 sqlite3 设计电商营销数据库 Schema (6 表 + 主外键 + 约束 + 范式化 3NF) | starter.ipynb TODO1 + drill D1 worked-faded + tutorial Socratic 追问约束缺失 | solution.ipynb 完整 DDL + tutorial 后测 - 给定业务场景独立写 6 表 DDL | >=80% 约束正确 + 3NF 无冗余 |
| ILO2: 能用 SQL DQL (JOIN/GROUP BY/窗口函数/CTE/子查询) + pandas.read_sql 完成营销分析与 RFM 52/49/31/45 分群 | starter.ipynb TODO2-5 + drill D2 worked-faded + schedule.json 间隔复习 C2/C3 + tutorial Socratic 追问 JOIN 缺 ON | solution.ipynb 6 个查询 + 项目里程碑 M2 (6 个分析查询) | >=70% 查询正确 + RFM 阈值有依据 |
| ILO3: 能执行六维数据治理审计 (准确性/完整性/一致性/及时性/唯一性/有效性) 并写修复建议 | starter.ipynb TODO6 + drill D3 worked-faded + schedule.json C1 复习 + tutorial Hattie [TASK] 反馈 | solution.ipynb 六维检测 + 项目里程碑 M3 (审计报告 + 修复建议) | 能独立解 + 修复建议可执行 |
| ILO4: 能解释 GDPR/数据安全法/个保法对营销数据的影响 + Privacy by Design | notes.md 理论部分 + reading.md 深链 + tutorial Socratic "若数据泄露谁担责" | 300 字分析 (作业) + 费曼演练 | 能口头辩护 >=3 个合规点 |

## mastery_threshold (掌握阈值)
- ILO1: >=80% (5 类约束中至少 4 类正确 + 3NF 评估无遗漏)
- ILO2: >=70% (6 个查询中至少 4 个正确 + RFM 阈值有业务/统计依据)
- ILO3: 能独立解 (六维审计无遗漏 + 修复建议可执行)
- ILO4: 能口头辩护 (费曼演练 >=3 个合规点)

## 3 自检问题 (Biggs Feed Up / Feed Back / Feed Forward)
1. **Feed Up (TLA 是否训练 ILO?)** - drill D1/D2/D3 是否覆盖了 ILO1/ILO2/ILO3? worked-faded 三阶段是否真的训练了 Schema/DQL/审计能力? tutorial Socratic 追问是否在强化 ILO?
2. **Feed Back (AT 是否测量 ILO?)** - solution.ipynb + 项目里程碑 M1/M2/M3 是否真的测量了 ILO1/ILO2/ILO3? mastery_threshold 是否可观察可判定?
3. **Feed Forward (不经 TLA 能过 AT 吗?)** - 若学生跳过 drill D1 直接做 M1, 能过吗? 若能 = 对齐失败. 检查: 没做 worked-faded 的学生 AT 通过率应显著低于做过的学生 (Butler 2010 检索效应预测 30%+ 差距).
