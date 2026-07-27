# Constructive Alignment - Day 4 因果发现 (Biggs 建构对齐)

## ILO ↔ TLA ↔ AT 矩阵

| ILO (预期学习产出) | TLA (教学学习活动) | AT (评估任务) | mastery_threshold |
|---|---|---|---|
| ILO1: 能区分因果发现与因果推断，用 PC 算法在 sklearn 糖尿病真实数据上自动发现因果图结构并解读有向/无向边，指出 v-结构触发条件 | starter.ipynb TODO1-3 + tutorial.ipynb Socratic 追问 PC 假设 + practice.md D1 worked-faded + schedule.json C1 间隔复习 | solution.ipynb PC 结果解读 + tutorial 后测 + D1 独立解在 NSW 前 5 变量跑 PC 写 300 字 | >=80% 正确解读边含义 + 指出 v-结构 |
| ILO2: 能用 NOTEARS 连续优化做因果发现，对比 PC 结果，说明矩阵指数 trace 约束 tr(e^{W∘W})-d=0 的作用与收敛诊断 | starter.ipynb TODO4 + practice.md D2 worked-faded + schedule.json C2 间隔复习 + tutorial Socratic 追问 DAG 约束 | solution.ipynb NOTEARS 代码 + 阈值截断 + D2 独立解糖尿病 NOTEARS vs PC 对比报告 | >=70% + 能解释 tr(e^{W∘W})-d=0 |
| ILO3: 能用因果森林 CausalForestDML 在 NSW 真实数据上估计 CATE，解读特征重要性，并融合 LLM 因果图做交叉验证 | starter.ipynb TODO5-6 + practice.md D3 worked-faded + schedule.json C3+C4 间隔复习 + tutorial Socratic 追问 LLM 幻觉风险 | solution.ipynb CATE 分布 + 特征重要性 + D3 独立解 LLM+PC+NOTEARS 融合全流程 | 能独立解 + 交叉验证 LLM 边 |

## mastery_threshold (掌握阈值)
- ILO1: >=80% (PC 边解读 + v-结构识别 + 因果充分性假设说明)
- ILO2: >=70% (NOTEARS 收敛 + 阈值截断 + 与 PC 对比)
- ILO3: 能独立完成端到端融合流程 (LLM 候选图 → PC 验证 → NOTEARS 修正 → 因果森林 CATE)
- 整体: 3 个 ILO 全部达标 + 交叉练习 (interleaving A1B1C1...B2C2A2...C3A3B3) 通过

## 3 自检问题 (Biggs 建构对齐 Feed Up / Feed Back / Feed Forward)

1. **Feed Up** (TLA 是否训练 ILO?): practice.md 的 D1-D3 drills + tutorial Socratic 追问 + schedule.json 间隔复习，是否覆盖了 ILO1-ILO3 的所有核心能力？→ 是，每个 ILO 都有对应的 drill + tutorial 追问 + 复习卡。若学生跳过任一 TLA，对应 ILO 难以达标。

2. **Feed Back** (AT 是否测量 ILO?): solution.ipynb + D1-D3 独立解 + tutorial 后测，是否能检测学生是否真的掌握了 PC/NOTEARS/因果森林？→ 是，AT 要求在真实数据（sklearn 糖尿病 / NSW）上独立产出，而非选择题。D3 独立解要求端到端融合，无法靠 memorization 通过。

3. **Feed Forward** (不经 TLA 能过 AT 吗?): 若学生跳过 starter.ipynb 的 TODO 填空和 tutorial 的 Socratic 追问，直接抄 solution.ipynb，能否通过 D1-D3 独立解？→ 不能，独立解要求在新数据（NSW / 糖尿病+NSW 组合）上应用，抄答案无法迁移。若能 = 对齐失败，需强化 AT（如口试答辩）。
