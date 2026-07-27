# Constructive Alignment - 回归分析与概率分布 (Day 4)

> Biggs 建构对齐 (Constructive Alignment): ILO (Intended Learning Outcomes) ↔ TLA (Teaching/Learning Activities) ↔ AT (Assessment Tasks) 三者必须对齐, 否则学生可以通过不对齐的 TLA 通过 AT, 即对齐失败。
> v6.0 学习科学层: 在 v5.0 (notes.md/starter.ipynb/solution.ipynb/reading.md/data) 之上, 新增 practice.md/schedule.json/tutorial.ipynb 三件套, 形成 4 阶段闭环。

---

## ILO ↔ TLA ↔ AT 矩阵

| ILO (预期学习产出) | TLA (教学学习活动) | AT (评估任务) | mastery_threshold |
|---|---|---|---|
| ILO1: 能用 statsmodels OLS 拟合多元线性回归, 解读 R²/系数/p值/CI, 用 VIF 检测多重共线性 | notes.md 关键回顾1-2 + starter.ipynb TODO1-2 + practice.md D1 worked-faded + tutorial.ipynb Socratic 第1-2轮 + schedule.json C1 间隔复习 | solution.ipynb OLS cell + practice.md D1 Stage3 独立解 + tutorial 后测第1题 | treat 系数解读正确 + VIF>10 识别 + >=80% |
| ILO2: 能用 statsmodels Logit 拟合二值回归并计算倾向性评分, 理解其作为因果推断桥梁 | notes.md 营销映射表 + starter.ipynb TODO3 + practice.md D2 worked-faded + tutorial.ipynb Socratic 第3轮 + schedule.json C2 间隔复习 | solution.ipynb Logit cell + practice.md D2 Stage3 + tutorial 后测第2题 | propensity score 公式正确 + 与处理效应区分 + >=70% |
| ILO3: 能用 scipy.stats 拟合 norm/binom/poisson 分布, 用 QuantReg 做分位数回归, 计算 LTV 概率区间 (复现 uplift 39.4%) | notes.md 关键回顾3 + 2026前沿分位数 + starter.ipynb TODO4-6 + practice.md D3 worked-faded + tutorial.ipynb Socratic 第4轮 + schedule.json C3/C4 间隔复习 | solution.ipynb 分布+QuantReg+LTV cells + practice.md D3 Stage3 + 300字商业解读 | 三分布选型全对 + LTV 概率区间含95% + 75分位 vs 25分位差异解读 + 能独立解 |
| ILO4: 能区分相关关系与因果关系, 知道从相关到因果的额外假设 (引向技能3) | notes.md 关键回顾4 + tutorial.ipynb devil's advocate 角色 + schedule.json C1/C4 复习 | practice.md diagnostic D0.2 + 300字分析中"R²低说明什么" | 能举出混杂因素例子 + 知道 RCT 随机化为何能识别因果 + 能独立解 |

---

## mastery_threshold (掌握阈值)

- **单元通过**: 4 个 ILO 全部达到对应 mastery_threshold, 且 practice.md 3 个 drill 各完成 reps_required=3
- **高分 (A)**: 4 个 ILO 全部 >=85% + LTV uplift 39.4% 复现误差 <5% + 分位数回归 75分位 vs 25分位差异解读正确
- **底线 (及格)**: ILO1>=80% + ILO2>=70% + ILO3 能独立解 + ILO4 能独立解, 任一未达即触发 weak_loop
- **leech 检测**: schedule.json 同卡连续 4 次评分 <=3 -> 转入 practice.md 弱项循环

---

## 3 自检问题 (Biggs Feed Up / Feed Back / Feed Forward)

1. **Feed Up (TLA 是否训练 ILO?)**: practice.md 的 D1/D2/D3 三个 drill 是否覆盖 ILO1/ILO2/ILO3? tutorial.ipynb 的 4 轮 Socratic 是否对应 4 个 ILO? 若有 ILO 无对应 TLA = 训练缺口, 必须补 drill。
   - 自检: 数 ILO 数量 == 数 drill 数量 == 数 Socratic 轮数? 是 -> 通过
2. **Feed Back (AT 是否测量 ILO?)**: solution.ipynb 的 8 个 code cells 是否覆盖 6 个 TODO 对应的 4 个 ILO? practice.md D1/D2/D3 Stage3 独立解的评分标准是否映射 mastery_threshold? 若 AT 测的不是 ILO = 评估失焦。
   - 自检: starter.ipynb TODO1-6 -> ILO1/2/3/4 映射表完整? solution.ipynb 无 scaffold 残留 (verify_unit.py 4 通过)? 是 -> 通过
3. **Feed Forward (不经 TLA 能过 AT 吗?)**: 若学生跳过 practice.md worked-faded 与 tutorial Socratic, 仅看 solution.ipynb 抄答案能否过 AT? 若能 = 对齐失败, 必须 AT 含独立解题环节 (D1/D2/D3 Stage3 + tutorial 后测)。
   - 自检: practice.md Stage3 是否独立解 (无填空)? tutorial 后测是否禁直接答案? schedule.json leech 是否触发 weak_loop? 是 -> 通过

---

## v6.0 升级对齐增量

| v5.0 文件 | v6.0 增量 | 对齐作用 |
|---|---|---|
| notes.md | 末尾追加"学习科学层 v6.0"一节 | 命中 FSRS/刻意练习/建构对齐/Socratic/Hattie/间隔重复/交叉/mastery/Worked-Faded >=4 关键词 |
| starter.ipynb | 不动 (v5.0 基线 7/7) | TODO 填空脚手架保留 |
| solution.ipynb | 不动 | 参考答案保留 |
| practice.md (新) | D1/D2/D3 + worked-faded + interleaving A1B1C1 + weak_loop | 刻意练习 + 交叉 + 弱项循环 |
| schedule.json (新) | 4 cards FSRS-6 due [1,3,8,21,60,180] | 间隔重复 + 提取练习 |
| alignment.md (新) | ILO↔TLA↔AT 4 行 + mastery + 3 自检 | 建构对齐 |
| tutorial.ipynb (新) | 6 cells: persona + pre-task + Socratic + student_model + Hattie + 限频 | 牛津 tutorial 仿真 |

---

*本 alignment.md 由 v6.0 学习科学层升级生成, 不破坏 v5.0 基线。*
*最后更新: 2026-07-25*
