# 建构对齐 · MMM/MTA 增量测量 (v6.0)

> 基于 Biggs (1996) Constructive Alignment: ILO ↔ TLA ↔ AT 三者对齐。mastery_threshold 来自 Bloom 掌握学习。所有 TLA 引用本单元 starter/solution/drill/tutorial 真实活动,所有 AT 引用 solution 后测 + practice 渐进项目。

---

## 一、ILO ↔ TLA ↔ AT 对齐矩阵 (5 行,覆盖 notes.md 6 个学习目标)

| ILO (预期学习产出) | TLA (教学学习活动) | AT (评估任务) | mastery_threshold |
|:------------------|:------------------|:-------------|:-----------------|
| **ILO1** 能阐述 MMM/MTA/增量测试三大方法的核心原理、数据需求、优势与局限,并能根据业务场景(年度预算/月度优化/关键决策/新渠道评估/隐私合规)推荐合适方法或组合 | ① 读 notes.md § 关键回顾 1 三方法对比表 + § 2026 前沿 ② starter TODO1+TODO2+TODO3 起步 ③ practice.md DRILL-01 worked + DRILL-02 worked + DRILL-03 worked ④ tutorial.ipynb cell3 苏格拉底追问"何时该用哪法" ⑤ schedule.json C1+C2+C3 间隔复习 | ① solution TODO1+TODO2+TODO3 结构对应 ② practice.md D1+D2+D3 diagnostic 先测 ③ 300 字分析报告(哪个渠道贡献最高/MTA 移除效应最高渠道/NSW 增量率) ④ tutorial.ipynb cell5 Hattie [TASK] 反馈 | >=80% 三方法场景推荐正确率;D1+D2+D3 全对 |
| **ILO2** 能用 statsmodels+sklearn 实现 MMM 全流程:Adstock 衰减变换 + Ridge 回归 + R² + 渠道贡献分解,并解释为什么 MMM 用聚合数据反而在隐私时代有优势 | ① starter TODO1 填空脚手架 ② practice.md DRILL-01 (worked->faded->independent 三阶段) ③ schedule.json C1 (Adstock 公式+λ 经验值) 间隔复习 ④ tutorial.ipynb cell3 追问"为什么 Ridge 而非 OLS" | ① solution TODO1 完整 Ridge 拟合 + Adstock + R² + 贡献分解 ② practice.md progressive_project milestone (R²>0.7) ③ DRILL-01 reps_required=5 全对 | R² > 0.7 + adjusted R² 报告 + λ 匹配渠道类型 + VIF<10 + 贡献分解归一化 |
| **ILO3** 能用 numpy+pandas 实现 MTA 马尔可夫链移除法:构建一阶转移矩阵 + 计算移除效应 + 识别关键触点 | ① starter TODO2 ② practice.md DRILL-02 (worked->faded->independent) ③ tutorial.ipynb cell3 反例追问"若完全移除 Social 转化率下降多少" ④ schedule.json C2 (5 步算法) | ① solution TODO2 完整移除效应 + 归一化 ② practice.md 300 字分析"MTA 移除效应最高渠道" ③ DRILL-02 reps_required=5 全对 | 移除效应归一化 Σ=1 + 转移矩阵行和=1 + 关键触点识别正确 + Shapley 对比 |
| **ILO4** 能用 causaldata NSW 真实 RCT 数据做增量测量:朴素均值差(有偏观测) vs RCT 真值 vs 合成控制 ATT vs DML 处理效应,并用增量率/增量 ROI 评估渠道真实因果价值 | ① starter TODO3+TODO4+TODO5 ② practice.md DRILL-03 (worked->faded->independent) ③ schedule.json C3+C4 (四法对比 + DML 算法) ④ tutorial.ipynb cell3 追问"ATT vs ATE 业务场景" + cell4 student_model 记录 DML 盲点 | ① solution TODO3+TODO4+TODO5 四法对比 ② practice.md progressive_project final (含 DML) ③ DRILL-03 reps_required=6 全对 ④ poster (Week 6) 标注 ATT vs ATE | ATT 估计与 RCT 真值偏差 < 15% + 合成控制 pre-period RMSE 报告 + DML 交叉拟合 2-fold 或 5-fold + 增量率业务解释 |
| **ILO5** 能用 scipy.optimize 基于 MMM 系数做预算优化:总预算约束下最大化预测销量,并用增量测试思想批判性检验优化结果可信度 | ① starter TODO6 ② practice.md DRILL-04 (worked->faded->independent) ③ schedule.json C6 (预算优化+CUPED) ④ tutorial.ipynb cell5 [FEED-FORWARD] 推荐复习增量验证 | ① solution TODO6 SLSQP 求解 ② practice.md progressive_project final (预算分配报告) ③ DRILL-04 reps_required=4 全对 | KKT 条件满足(拉格朗日乘子非负) + 影子价格解释 + 增量验证方案(Geo 实验 + CUPED) |

---

## 二、3 自检问题 (Feed Up / Feed Back / Feed Forward)

### Q1 · Feed Up: TLA 是否训练 ILO?

逐行检查:每个 ILO 是否有对应的 starter TODO + practice drill + tutorial 追问 + schedule card?

- ILO1 -> TODO1+2+3, DRILL-01/02/03, tutorial cell3 三方法追问, C1+C2+C3 ✓
- ILO2 -> TODO1, DRILL-01 三阶段, tutorial Ridge 追问, C1 ✓
- ILO3 -> TODO2, DRILL-02 三阶段, tutorial 反例追问, C2 ✓
- ILO4 -> TODO3+4+5, DRILL-03 三阶段, tutorial ATT/ATE 追问, C3+C4 ✓
- ILO5 -> TODO6, DRILL-04 三阶段, tutorial Feed-Forward, C6 ✓

**结论**: 5 个 ILO 全部有 TLA 覆盖,无遗漏。

### Q2 · Feed Back: AT 是否测量 ILO?

逐行检查:每个 ILO 的 AT 是否能区分"真正掌握"vs"看似会了"?

- ILO1: 三方法场景推荐 + D1+D2+D3 先测 -> 能区分(场景判断错 = 没掌握)
- ILO2: R²>0.7 + λ 匹配 + VIF<10 + 贡献归一化 -> 能区分(只跑通代码 ≠ 理解 λ)
- ILO3: 移除效应归一化 + 关键触点识别 -> 能区分(只建矩阵 ≠ 理解移除效应)
- ILO4: ATT 偏差<15% + pre-period RMSE + DML 交叉拟合 -> 能区分(只调包 ≠ 理解交叉拟合)
- ILO5: KKT 满足 + 增量验证方案 -> 能区分(只求最优解 ≠ 理解可信度边界)

**结论**: 5 个 AT 全部有可观察的客观标准,不是主观打分。

### Q3 · Feed Forward: 不经 TLA 能过 AT 吗? (若能 = 对齐失败)

**反事实检验**: 若学生跳过 practice drill 和 tutorial,只看 notes.md + 直接抄 solution.ipynb,能过 AT 吗?

- ILO2 AT (R²>0.7 + λ 匹配): 抄 solution 能跑通代码,但 λ 匹配渠道类型的解释无法抄 -> **不过** ✓
- ILO3 AT (移除效应归一化 + Shapley 对比): 抄 solution 能得数值,但 Shapley 对比讨论无答案 -> **不过** ✓
- ILO4 AT (ATT 偏差<15% + DML 交叉拟合): 抄 solution 能得 ATT,但交叉拟合步骤跳过 -> tutorial cell5 [PROCESS] 反馈会捕获 -> **不过** ✓
- ILO5 AT (KKT + 增量验证方案): 抄 solution 能得最优解,但增量验证方案(Geo+CUPED)需独立设计 -> **不过** ✓

**结论**: 所有 AT 均需经 TLA 才能过,对齐成立。tutorial.ipynb 的 Hattie [PROCESS] 与 [FEED-FORWARD] 反馈专门捕获"跳过 worked-faded 直接抄答案"的学生。

---

## 三、Mastery Threshold 汇总

| ILO | mastery_threshold | 检测点 |
|:---:|:-----------------|:-------|
| ILO1 | >=80% 场景推荐正确率 + D1+D2+D3 全对 | diagnostic 先测 + tutorial 后测 |
| ILO2 | R²>0.7 + λ 匹配 + VIF<10 + 贡献归一化 | solution TODO1 + milestone |
| ILO3 | 移除效应归一化=1 + 关键触点正确 | solution TODO2 + DRILL-02 |
| ILO4 | ATT 偏差<15% + pre-period RMSE + DML 交叉拟合 | solution TODO3-5 + final |
| ILO5 | KKT 满足 + 增量验证方案 | solution TODO6 + final |

未达 mastery -> 触发 practice.md § 七 Weak Loop 弱项循环(回退上一 drill + worked 示范 + schedule.json 间隔复习)。

---

*本 alignment.md 基于 Biggs (1996) Constructive Alignment + Bloom 掌握学习。ILO 来自 notes.md 6 个学习目标,TLA 引用 starter/drill/tutorial 真实活动,AT 引用 solution 后测 + practice 渐进项目。*
