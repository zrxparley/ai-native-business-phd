# 刻意练习 - Day 3 描述统计与推断统计 (v6.0)

> **学习科学依据**：Ericsson 刻意练习五要素（明确目标/专注/反馈/重复/渐增难度）+ MIT 6.5940 提取练习 + Worked-Faded 渐退示例 + A1B1C1 交叉练习（不块状）+ 弱项循环回退。

---

## skill_target

在 90 分钟内独立完成一份营销 A/B 测试统计推断报告：用 `scipy.stats` 执行 t 检验、用 `chi2_contingency` 执行卡方检验、用 `scipy.stats.beta` 实现 Beta-Binomial 贝叶斯推断，并按 ASA p 值六原则报告效应量 + 95% CI + 后验分布，区分"统计显著性"与"商业显著性"。

---

## diagnostic（前测诊断 3 道，检索练习）

1. **D-1 概念检索**：写出 t 检验原假设 H₀ 与备择假设 H₁ 的营销语义；A/B 两组转化率差为 +0.8%、p=0.04，结论是"方案有效"吗？请用法庭审判类比解释第一类错误 α 与第二类错误 β。
2. **D-2 真实库调用**：写出 `scipy.stats.chi2_contingency` 的输入数据结构（用户分群 × 品类列联表），并解释返回元组四个元素的含义（chi2 / p / dof / expected）。
3. **D-3 贝叶斯对比**：Beta(1,1) 先验 + 观察到 30 次转化 / 200 次试验，写出后验参数与后验均值；对比频率派 p 值与贝叶斯后验分布在"直接回答业务问题"上的根本差异。

> 诊断结果决定起始 drill：D-1 答错先做 D1；D-2 答错先做 D2；D-3 答错先做 D3。三道全对从 D2 起步。

---

## subskills

- **S1 描述统计稳健性**：能解释为何右偏营销客单价（AOV）分布下中位数比均值更稳健，能用 numpy/pandas 计算 mean/median/var/std/quantile/skew 并可视化对比。
- **S2 假设检验流程**：能用 `scipy.stats.ttest_ind` 执行 t 检验、用 `chi2_contingency` 执行卡方检验，正确解读 p 值、效应量、95% CI，并遵守 ASA 2016 p 值六原则（p≠P(H₀真)、不抹杀研究、不只看 p、p 需透明、p+CI+效应量、科学推论不归一指标）。
- **S3 贝叶斯推断更新**：能用 Beta-Binomial 模型实现先验→似然→后验的更新，对比频率派与贝叶斯派在"小样本/持续更新"场景下的差异，了解 PyMC 前沿扩展。

---

## drills（>=3，每含 difficulty/reps_required/feedback_rule/worked_faded）

### drill_id: D1
- **技能指向**：S1 描述统计稳健性
- **difficulty**：2
- **reps_required**：3
- **feedback_rule**：若学生答"均值更能代表典型客单价"，反馈"右偏分布下少数大额订单拉高均值；用 numpy 同时算 mean 与 median，若 mean > median 即右偏，请用 skewness 验证（>0 即右偏）"；若学生混淆方差与标准差，反馈"std 是 var 的平方根，单位与原始数据一致，营销场景用 std 更可解释"。
- **worked_faded**：
  - **Worked（完整示范）**：给定 `aov = np.array([38, 42, 55, 60, 80, 120, 450])`，演示 `np.mean(aov)=120.7` vs `np.median(aov)=60` vs `scipy.stats.skew(aov)=1.87`，结论"右偏，中位数更稳健"。
  - **Faded（部分填空）**：给定另一组数据，让学生填 `np.median(?)` 与 `scipy.stats.skew(?)` 两行，结论由学生写。
  - **Independent（独立解）**：给一组 1000 条 `df['aov']`，学生独立写 describe + skew 并判断分布形态。

### drill_id: D2
- **技能指向**：S2 假设检验流程（t 检验 + ASA p 值）
- **difficulty**：3
- **reps_required**：3
- **feedback_rule**：若学生写 `ttest_ind(groupA, groupB)` 漏掉 `equal_var=False`（Welch），反馈"营销数据两组方差常不等，默认 Student t 会膨胀 α；用 Welch t = `ttest_ind(a, b, equal_var=False)` 更稳健"；若学生只报 p 值不报效应量，反馈"ASA 2016 第三条：p 值不是效应量；必须同时报告 Cohen's d 或 Hedges' g + 95% CI"；若学生写"p=0.06 所以无效"，反馈"二分阈值 0.05 是惯例不是真理；ASA 第六条：科学推论不该归一指标，请结合 CI 宽度与业务成本判断"。
- **worked_faded**：
  - **Worked**：A 组 n=500 转化率 12%，B 组 n=500 转化率 14.5%；演示 `stats.ttest_ind(a_converted, b_converted, equal_var=False)` 得 t=1.96, p=0.05；效应量 Cohen's d ≈ 0.12（小）；95% CI = [−0.001, 0.051]；结论"统计边际显著，但 CI 跨 0，效应量小，需更大样本或更长观察期"。
  - **Faded**：给学生 A/B 两组数据，学生填 `ttest_ind(?, ?, equal_var=?)` 一行 + 写效应量公式 + 解释 CI 是否跨 0。
  - **Independent**：给学生 1000 条营销数据 DataFrame，独立完成 t 检验 + 效应量 + CI + ASA 六原则解读。

### drill_id: D3
- **技能指向**：S2 卡方 + S3 贝叶斯 Beta-Binomial
- **difficulty**：4
- **reps_required**：3
- **feedback_rule**：若学生卡方列联表行列颠倒，反馈"`chi2_contingency` 要求行=用户分群、列=购买品类，列联表 shape 应为 (3,4) 不是 (4,3)；用 `pd.crosstab(df['segment'], df['category'])`"；若学生贝叶斯后验写错参数，反馈"先验 Beta(α,β) + s 成功 / n 试验 → 后验 Beta(α+s, β+n−s)，不是 Beta(α+s, β+s)；后验均值 = (α+s)/(α+β+n)"；若学生混淆可信区间与置信区间，反馈"贝叶斯 credible interval 直接说'转化率有 95% 概率落在此区间'；频率派 CI 说'重复实验 95% 次包含真值'——语义根本不同"。
- **worked_faded**：
  - **Worked**：用户分群（新客/回客/VIP）× 品类（美妆/电子/健身/家居）列联表，演示 `chi2_contingency(table)` 得 chi2=18.3, p=0.003, dof=6；同时用 Beta(1,1)+30/200 → 后验 Beta(31,171)，后验均值 0.153，95% credible interval [0.107, 0.205]。
  - **Faded**：给列联表，学生填 `chi2_contingency(?)` 与 `stats.beta(1+?, 1+?-) ` 两行。
  - **Independent**：独立完成卡方 + 贝叶斯，对比频率派 p 值与贝叶斯后验，写 300 字对比分析。

---

## progressive_project（渐进项目脚手架，CS230 风格）

- **阶段 1（Day 3 当堂）**：完成 starter.ipynb 6 个 TODO，得到 t 检验 / 卡方 / 贝叶斯初步结果。
- **阶段 2（Day 3 +1 周）**：用 PyMC 为同一 A/B 测试构建层次贝叶斯模型，对比 scipy.stats.beta 手动后验，500 字反思频率派与贝叶斯派在小样本场景的差异。
- **阶段 3（Day 3 +2 周，对接技能3 因果推断）**：补做功效分析（`statsmodels.stats.power`）计算所需样本量，并预注册（OSF 模板）下次 A/B 测试的分析计划，避免 p-hacking。

---

## interleaving（A1B1C1 交叉练习，不块状）

不按 D1→D2→D3 块状刷题，而按以下交叉序列：

```
A1(t检验-均值差) → B1(卡方-独立性) → C1(贝叶斯-后验)
→ B2(卡方-拟合度) → C2(贝叶斯-先验选择) → A2(t检验-配对)
→ C3(贝叶斯-credible interval) → A3(t检验-Welch) → B3(卡方-expected freq)
```

**为什么交叉**：Butler 2010 与 MIT 6.5940 证据表明，块状练习短期流畅但长期保持差；A1B1C1 交叉强制每次重新选择检验工具，训练"何时用何检验"的元认知，这正是营销分析师的核心能力。

---

## retry_policy

- 每个 drill **reps_required=3**，3 次中至少 2 次达成 80% 标准（效应量解释正确 + CI 解读正确 + ASA 原则引用对）方为通过。
- 未通过：可重做同一 drill 的 Independent 变体（数据不同、结构相同），最多 3 次。
- 累计 3 次未通过：触发 `weak_loop`。

---

## weak_loop（连续 2 次失败触发弱项循环）

若同一 drill 连续 2 次失败：
1. **回退一级**：从 Independent 退回 Faded，再退回 Worked，重新做一遍示范-填空-独立解三阶段。
2. **补充 worked example**：从 `solution.ipynb` 提取对应 TODO 的完整解，在 `tutorial.ipynb` 的 Socratic loop 中触发该 subskill 的脚手架降级。
3. **`student_model.json` 标记弱项**：把该 subskill 的 `mastery` 降到 0.3 以下，下次跨单元复习时 `schedule.json` 会优先安排该卡。
4. **限频放宽**：tutorial 当天再加 1 次（但仅限该弱项 subskill），通过后恢复 1 次/天限制。

---

## 学习科学关键词映射

- Ericsson 刻意练习 → drills + reps_required + feedback_rule
- MIT Worked-Faded → 每个 drill 三阶段
- MIT A1B1C1 interleaving → interleaving 节
- Biggs 建构对齐 → alignment.md ILO↔TLA↔AT
- Hattie 4 级反馈 → tutorial.ipynb [TASK]/[PROCESS]/[SELF-REG]/[FEED-FORWARD]
- FSRS-6 间隔重复 → schedule.json
- Oxford tutorial Socratic → tutorial.ipynb persona
