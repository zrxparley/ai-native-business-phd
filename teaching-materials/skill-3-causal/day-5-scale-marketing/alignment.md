# Constructive Alignment - U-skill3-day5 规模实验与营销因果

> Biggs 建构对齐 (Constructive Alignment): ILO (预期学习产出) ↔ TLA (教学学习活动) ↔ AT (评估任务) 三者一一对应. 若不经 TLA 能过 AT, 则对齐失败.

## ILO ↔ TLA ↔ AT 矩阵

| ILO (预期学习产出) | TLA (教学学习活动) | AT (评估任务) | mastery_threshold |
|---|---|---|---|
| ILO1: 能用 Thompson Sampling MAB 在 NSW 真实响应率上对比固定 A/B，定量解释探索-利用权衡与实验成本节省 | starter.ipynb TODO1-3 + practice.md D1 (Worked→Faded→Independent) + tutorial.ipynb cell3 Socratic loop Round 1-2 + schedule.json C1 复习 | solution.ipynb 解题 + D1 reps 3/3 + tutorial 后测"实验成本节省 X%"数字正确 | >=80% (D1 reps 3/3 通过, 实验成本节省数字误差 <10%) |
| ILO2: 能用 econml CausalForestDML 估计 CATE，识别响应最大用户群并做安慰剂反驳检验 | starter.ipynb TODO4-5 + practice.md D2 + schedule.json C2/C4 复习 + tutorial cell3 Round 3 | solution.ipynb TODO4-5 + D2 reps 3/3 + 100 字因果解释 | >=70% (CATE 方向正确, 安慰剂 p>0.05, 因果解释引用 top-3 调节变量) |
| ILO3: 能用 Uplift/Qini 把用户分四类，给出精准投放建议并规避三陷阱 | starter.ipynb TODO6 (可选 Uplift) + practice.md D3 + schedule.json C3 复习 + tutorial cell3 Round 4 | solution.ipynb TODO6 + D3 reps 3/3 + 300 字投放建议含 Qini 拐点 | 能独立解 (四类用户分类正确, 投放建议指向 persuadables, 引用至少 1 个陷阱规避) |
| ILO4: 能完成"数据→因果→决策"综合案例流程，迁移到自选营销场景 | practice.md M4 渐进项目 + tutorial.ipynb cell4 student_model 跨单元复用 + interleaving A1B1C1 交叉 | M4 自选场景迁移报告 (含 ATE/CATE/决策三段) | >=80% (三段齐全, 因果链自洽, 决策引用 ATE+CATE) |

## mastery_threshold 全局说明

- **D1 (Thompson MAB)**: >=80% - 三次 reps 全过，"实验成本节省"数字与 solution 误差 <10%
- **D2 (CATE)**: >=70% - CATE 方向正确，安慰剂不显著，因果解释含 top-3 调节变量
- **D3 (Uplift)**: 能独立解 - 四类用户分类正确，投放建议指向 persuadables 而非 sure things
- **M4 (迁移)**: >=80% - 三段齐全（数据/因果/决策），因果链自洽

## 3 自检问题 (Biggs Feed Up / Feed Back / Feed Forward)

1. **Feed Up (TLA 是否训练 ILO?)**: practice.md 的 D1/D2/D3 + tutorial Socratic 追问，是否真的训练了"Thompson MAB / CATE / Uplift"三项可观察技能？  
   *自检*: 每个 ILO 都能指到至少 1 个 drill + 1 个 tutorial round，否则补 TLA。

2. **Feed Back (AT 是否测量 ILO?)**: solution.ipynb + D1/D2/D3 reps + 100/300 字分析，是否真的测量了 ILO 而非仅"代码能跑"？  
   *自检*: AT 评分细则是否包含"解释/因果/陷阱规避"等高阶指标，而非仅"输出对"。

3. **Feed Forward (不经 TLA 能过 AT 吗?)**: 若学生跳过 tutorial 与 practice.md，直接抄 solution.ipynb 能过 AT 吗？若能 = 对齐失败。  
   *自检*: AT 必须含"口头辩护/因果解释/迁移场景"等 TLA 才能训练的能力，使抄答案不可行。

---

*本 alignment.md 实现 Biggs 建构对齐 (Constructive Alignment) + Hattie (2007 RER 77(1):81-112) 3 问 (Feed Up/Back/Forward) + MIT 6.5940 mastery 阈值. mastery_threshold 对齐 Ericsson 刻意练习的"可观察技能"标准.*
