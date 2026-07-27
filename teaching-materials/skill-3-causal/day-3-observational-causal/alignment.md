# Constructive Alignment - Day 3 观测因果 (NSW+CPS PSM + close_college IV + DML)

> v6.0 学习科学层 · Biggs 建构对齐 (ILO ↔ TLA ↔ AT) + mastery threshold + 3 自检
> 参考: Biggs (1996) "Enhancing teaching through constructive alignment"; Hattie & Timperley (2007 RER 77(1):81-112)

## ILO ↔ TLA ↔ AT 矩阵

| ILO (预期学习产出) | TLA (教学学习活动) | AT (评估任务) | mastery_threshold |
|---|---|---|---|
| **ILO1**: 能在 NSW+CPS 真实观测数据上用 PSM 消除自选择偏差, 并与朴素估计对比解释偏误来源 | starter.ipynb TODO1-4 + practice.md D1 (Worked→Faded→Independent) + tutorial.ipynb Socratic loop Round 1-2 + schedule.json C1 间隔复习 | solution.ipynb 解题 + practice.md D1 Independent 交付 + tutorial.ipynb exit 盲点表 | ATT 估计偏差 < $200 vs LaLonde 基准; 平衡检验 SMD<0.1 全部协变量通过; 自评 >=4/5 |
| **ILO2**: 能在 close_college 真实 IV 数据上用 2SLS 估计 LATE, 论证 IV 三假设, 对比 OLS 解释差异 | starter.ipynb TODO5-6 + practice.md D2 (Worked→Faded→Independent) + tutorial.ipynb Socratic loop Round 3 (devil's advocate 追问排他性) + schedule.json C2 复习 | D2 Independent 交付 + 300 字分析 (IV vs OLS 差异说明什么) + 第一阶段 F 统计量报告 | 2SLS 估计与 Card 1995 基准偏差 < 30%; 第一阶段 F>=10; 能口头辩护 nearc4 三假设 |
| **ILO3**: 能用 econml.dml / DoubleML 在 NSW+CPS 上对比 PSM vs DML, 理解"放松函数形式但不放松可忽略性" | practice.md D3 (Worked→Faded→Independent) + reading.md DML 条目 + schedule.json C3 复习 + tutorial.ipynb Hattie [PROCESS] 反馈 | D3 Independent 交付 + 200 字辩护 (DML vs PSM 哪个更可信) + poster 同伴评审 | DML 估计与 PSM 差异合理解释 (函数形式 vs 混杂结构); 不声称 DML 解决未观测混杂 (概念过关) |
| **ILO4**: 能用"何时用哪个"决策框架为营销观测场景设计观测因果方案, 并在 2 分钟内辩护方法选择 | practice.md interleaving A1B1C1 交叉练习 + progressive_project Week 1 proposal + tutorial.ipynb pre-task | progressive_project Week 4 poster + 2 分钟话术 + 同伴 devil's advocate 互质三问 | proposal 能正确分类混杂 (可观测/未观测); 2 分钟话术能挡住 3 轮 devil's advocate 追问 |

## mastery_threshold (整体单元过关)

- 4 个 drill 全部达 reps_required=3 且自评 >=4/5
- diagnostic 前测 3 道后测重做正确率 >=2/3 (检验前测盲点已补)
- progressive_project Week 3 final 报告 >=80% (rubric: 方法选择 30% / 代码正确 30% / 解读深度 20% / 稳健性检验 20%)
- schedule.json 5 卡片首次复习完成率 100% (第 1 天 + 第 3 天)
- tutorial.ipynb exit artifact 列出 >=2 个盲点 + >=1 个推荐复习单元

## 3 自检问题 (Biggs Feed Up / Feed Back / Feed Forward)

1. **Feed Up (TLA 是否训练 ILO?)**: practice.md 的 D1 (PSM) / D2 (IV) / D3 (DML) 三个 drill 是否真的训练了 ILO1/ILO2/ILO3? 还是只是"做了一遍"而没掌握? 检验: 学生能否在 Independent 阶段独立解, 不回看 Worked example? 若不能 = TLA 脚手架不够, 需加一轮 Faded.
2. **Feed Back (AT 是否测量 ILO?)**: solution.ipynb + D1/D2/D3 Independent 交付 + 300/200 字分析, 是否真的测量了"能对比 PSM vs 朴素 / IV vs OLS / PSM vs DML"的差异解读? 还是只测了"能跑通代码"? 检验: 拿掉解读任务, 学生还能过 AT 吗? 若能 = AT 没测 ILO 的认知层, 需加口头辩护.
3. **Feed Forward (不经 TLA 能过 AT 吗?)**: 若学生跳过 starter.ipynb TODO 填空、跳过 practice.md drill、跳过 tutorial.ipynb Socratic, 直接抄 solution.ipynb 能过 AT 吗? 若能 = 对齐失败, AT 太浅. 修复: AT 加随机子集变体 (如 NSW 男性子集 vs 全样本), solution.ipynb 抄不到答案.

## ILO 与前后 Day 对齐

- Day 1 (因果基础: DAG/后门调整) → ILO4 决策框架的根基
- Day 2 (实验设计: A/B + DiD/RDD) → ILO4 决策框架的 DiD/RDD 分支
- **Day 3 (本单元)**: 观测数据 PSM/IV/DML → ILO1/ILO2/ILO3
- Day 4 (因果发现 + ML 因果: DML 进阶/因果森林) → ILO3 DML 的延伸

---

*v6.0 学习科学层 · Biggs (1996) Constructive Alignment + Hattie & Timperley (2007) Feed Up/Back/Forward*
