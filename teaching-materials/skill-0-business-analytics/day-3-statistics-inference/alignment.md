# Constructive Alignment - Day 3 描述统计与推断统计 (v6.0)

> **Biggs 建构对齐原则**：ILO（预期学习产出）↔ TLA（教学学习活动）↔ AT（评估任务）三者必须对齐，否则"对齐失败"——学生不经 TLA 也能过 AT，说明 AT 没测到 ILO。
> **mastery_threshold**：每项 ILO 有明确掌握阈值，未达阈值触发 `weak_loop`（见 practice.md）。

---

## ILO ↔ TLA ↔ AT 矩阵

| ILO (预期学习产出) | TLA (教学学习活动) | AT (评估任务) | mastery_threshold |
|---|---|---|---|
| ILO1: 能用 numpy/pandas 计算描述统计并解释为何右偏营销客单价(AOV)下中位数比均值更稳健 | starter.ipynb TODO1 + practice.md drill D1 (Worked-Faded 三阶段) + tutorial.ipynb Socratic loop Q1-Q2 | solution.ipynb TODO1 解题 + diagnostic D-1 + 300 字分析 | >=80% (描述统计 5 指标全对 + 右偏解释正确) |
| ILO2: 能用 scipy.stats.ttest_ind 执行 Welch t 检验、用 chi2_contingency 执行卡方检验，按 ASA p 值六原则报告 p+效应量+95% CI | starter.ipynb TODO3/TODO5 + practice.md drill D2/D3 + schedule.json C1/C2/C4 间隔复习 + tutorial.ipynb Socratic Q3-Q4 | solution.ipynb TODO3/5 解题 + diagnostic D-2 + drill D2/D3 三次 reps | >=70% (检验调用正确 + ASA 六原则引用 >=4 条 + CI 解读不跨 0) |
| ILO3: 能用 Beta-Binomial 模型实现先验->后验更新，对比频率派与贝叶斯派在小样本/持续更新场景的差异 | starter.ipynb TODO6 + practice.md drill D3 + schedule.json C3 间隔复习 + tutorial.ipynb Socratic Q5 + PyMC 选做 | solution.ipynb TODO6 解题 + diagnostic D-3 + 300 字对比分析 + (选做) PyMC 模型 | 能独立解 (后验参数对 + 均值对 + credible vs CI 语义区分) |
| ILO4: 能区分"统计显著性"(p 值)与"商业显著性"(效应量+CI 宽度)，避免大样本"微小差异显著"陷阱 | starter.ipynb TODO4 + practice.md drill D2 feedback_rule + tutorial.ipynb Hattie [FEED-FORWARD] | 300 字分析 + ASA 六原则解读 + 复盘自诊表 | >=80% (效应量 + CI 宽度 + 业务成本三维判断) |

---

## mastery_threshold 说明

- **>=80%**：5 指标/4 维度中至少 4 个正确，且核心概念（右偏/独立性/后验）零容忍。
- **>=70%**：检验调用必须正确（零容忍），ASA 六原则引用至少 4 条。
- **能独立解**：无脚手架情况下 90 分钟内完成，且 credible interval 与 CI 语义区分正确（这是贝叶斯派与频率派最易混淆点）。
- **未达阈值**：触发 `practice.md` 的 `weak_loop`——回退到 Worked-Faded 上一阶段 + tutorial 加 1 次（限该弱项 subskill）+ student_model.json 标记 mastery<0.3。

---

## 3 自检问题（Biggs 建构对齐自检，Feed Up / Feed Back / Feed Forward）

### 1. TLA 是否训练 ILO？（Feed Up - 向上看目标）

- ILO1 要求"解释右偏为何中位数更稳健"——TLA 中 drill D1 Worked-Faded 是否真的让学生练习"解释"而非只算数字？
- ILO2 要求"按 ASA 六原则报告"——TLA 中 drill D2 feedback_rule 是否每次都追问 ASA 引用？
- ILO3 要求"对比频率派与贝叶斯派"——TLA 中 drill D3 是否强制学生写对比分析而非只算后验？
- ILO4 要求"区分统计显著性与商业显著性"——TLA 中 drill D2 feedback_rule 是否在学生只报 p 时触发纠正？

**自检结论**：是。每个 TLA 活动都直接训练对应 ILO 的核心动作（解释/报告/对比/区分），而非泛泛练习。

### 2. AT 是否测量 ILO？（Feed Back - 向回看评估）

- AT1（solution.ipynb TODO1）是否真的测量"解释右偏"而非只测"算 mean/median"？——是，300 字分析强制解释。
- AT2（diagnostic D-2）是否测量"调用 chi2_contingency + 解读返回元组"？——是，四元素全要求。
- AT3（diagnostic D-3）是否测量"对比频率派与贝叶斯派"？——是，对比分析是核心交付物。
- AT4（ASA 六原则解读）是否测量"区分显著性与意义"？——是，效应量+CI+业务成本三维判断。

**自检结论**：是。每个 AT 都直接测量对应 ILO，无"代用指标"（proxy）。

### 3. 不经 TLA 能过 AT 吗？（Feed Forward - 向前看迁移）

若能，则对齐失败。

- 不做 drill D1 的 Worked-Faded，能直接在 AT1 写出"右偏分布少数大额订单拉高均值"吗？——多数学生不能，需 D1 训练。
- 不做 drill D2 的 feedback_rule 追问 ASA，能在 AT2 主动引用六原则吗？——多数学生只报 p，需 D2 feedback 训练。
- 不做 drill D3 的 Beta-Binomial 三阶段，能在 AT3 区分 credible interval 与 CI 语义吗？——这是最易混淆点，必须 D3 训练。
- 不做 tutorial Socratic loop 的反诘，能在 AT4 主动区分统计显著性与商业显著性吗？——多数学生不会主动区分，需 Socratic 训练。

**自检结论**：否。每个 AT 都依赖对应 TLA 训练，对齐成立。若学生不经 TLA 也能过 AT，说明 AT 阈值过低，需上调 mastery_threshold。

---

## 与跨单元学习科学的衔接

- `practice.md` 的 drills 对齐本表 ILO/TLA/AT。
- `schedule.json` 的 5 张卡片覆盖 ILO1-ILO4 的核心概念，FSRS-6 间隔重复。
- `tutorial.ipynb` 的 Socratic loop 5 问对应 ILO1-ILO4 的诊断与脚手架降级。
- `student_model.json`（tutorial.ipynb 读写）记录每项 ILO 的 mastery 值，跨单元复用。
- Hattie 4 级反馈（[TASK]/[PROCESS]/[SELF-REG]/[FEED-FORWARD]）直接映射 ILO 的掌握与迁移。
