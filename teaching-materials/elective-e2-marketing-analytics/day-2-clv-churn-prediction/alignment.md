# alignment.md · Day 2 建构对齐矩阵 (Biggs ILO ↔ TLA ↔ AT)

> 本文件验证"教-学-评"一致性 (Biggs constructive alignment)。每行：ILO (预期学习产出) ↔ TLA (教学学习活动) ↔ AT (评估任务) ↔ mastery_threshold。底部 3 自检问题 (Feed Up / Feed Back / Feed Forward)。

## ILO ↔ TLA ↔ AT 矩阵

| ILO (预期学习产出) | TLA (教学学习活动) | AT (评估任务) | mastery_threshold |
|---|---|---|---|
| **ILO1**: 能阐述 CLV 三种计算方法 (历史 CLV / 简单预测 CLV / BG/NBD + Gamma-Gamma 概率模型) 的数据需求与适用场景，并说明 CLV 如何将营销决策从短期 ROI 转向长期客户价值 | 讲义 §CLV 三方法回顾 + `practice.md` D3-BGNBD Worked example (BG/NBD 简化公式 `pred_clv = F × retention^12 × AOV × 12 × discount_factor`) + `tutorial.ipynb` 苏格拉底追问 (B2B 场景假设违背) + `schedule.json` C1/C5 间隔重复 | `solution.ipynb` TODO1 (历史 CLV + 简单预测 CLV) + TODO3 (BG/NBD 简化 CLV) 跑通 + `practice.md` D1.1 先测题 + `tutorial.ipynb` exit artifact 列出 BG/NBD 假设盲点 | TODO1+TODO3 单元测试通过 (CLV 均值落在合理区间) **>=80%**；D1.1 答出 Poisson 购买率 + Beta 流失两大假设 |
| **ILO2**: 能用 pandas + numpy 实现 RFM 客户分群 (Recency/Frequency/Monetary -> Champions/Recent/At Risk/Hibernating/Lost)，将 NSW 真实 RCT 数据转化为 RFM 评分矩阵 | `starter.ipynb` TODO2 脚手架 + `practice.md` D2-RFM Worked-Faded 三阶段 (`pd.qcut` vs `pd.cut` 选择) + `tutorial.ipynb` Hattie [TASK] 级反馈 + `schedule.json` C2 间隔重复 | TODO2 单元测试 (五类分群非空 + 每类样本量均衡) + `practice.md` D2-RFM Independent 阶段独立产出 `df['R']`/`df['F']`/`df['M']` 三列 + 互评 | 五类分群每类 **>=5%** 样本量 (避免某类=0)；qcut 分箱逻辑正确率 **>=80%** |
| **ILO3**: 能用 sklearn 构建流失预测模型 (LogisticRegression + RandomForestClassifier)，理解 `train_test_split(stratify=y)` + `class_weight='balanced'` + `StandardScaler` 三个工程陷阱，并用 AUC-ROC / Precision / Recall 评估 | `starter.ipynb` TODO4+TODO5 脚手架 + `practice.md` D5-SKLEARN Worked-Faded (stratify/scaler/class_weight 三大陷阱) + `tutorial.ipynb` Hattie [PROCESS] 级反馈 + `schedule.json` C3 间隔重复 + 讲义 §"为什么 NSW 上 AUC≈0.54 是预期的" | TODO4+TODO5 跑通 + `practice.md` D1.2 先测题 (8% 流失率下 accuracy 不可信) + `practice.md` D5 Independent 阶段独立写 `roc_auc_score` + `classification_report` | LogisticRegression AUC **>=0.50** (NSW 基线场景允许 ≈0.54)；能口头解释为什么 AUC<0.80 是预期的（缺行为特征） |
| **ILO4**: 能将 CLV 预测与流失概率组合为"高/低 CLV × 高/低流失风险"四象限行动矩阵，为每象限设计差异化营销行动，并用特征重要性识别关键流失驱动因子 | `starter.ipynb` TODO6 脚手架 + `practice.md` D6-MATRIX Worked-Faded + `tutorial.ipynb` 苏格拉底追问 (Q1 挽留 ROI 不等式) + `schedule.json` C4 间隔重复 + 讲义 §四象限行动矩阵 | TODO6 跑通 + `practice.md` D1.3 先测题 (Q1 挽留决策不等式) + `practice.md` progressive_project final 300 字分析 (Q1 客户数 × 平均 CLV × 挽留成功率 = 可挽回价值) | Q1 客户数 **>0 且 <全量** (分箱逻辑正确)；300 字分析能算出可挽回价值并给出 go/no-go 决策 |

---

## 3 自检问题 (Feed Up / Feed Back / Feed Forward)

### 自检 1 · Feed Up: TLA 是否训练 ILO？
- ILO1 的 TLA 是否覆盖"CLV 三方法的对比"训练？**是**--D3-BGNBD Worked 显式对比历史/简单/BG/NBD 三者公式与数据需求，`tutorial.ipynb` 苏格拉底追问"B2B 合同周期违背哪个假设"训练 ILO1 的"适用场景"理解。
- ILO3 的 TLA 是否训练"`stratify` + `class_weight` + `StandardScaler` 三陷阱"？**是**--D5-SKLEARN feedback_rule 显式列出三陷阱，`solution.ipynb` TODO4 给出完整示范。
- ILO4 的 TLA 是否训练"差异化营销行动设计"？**部分**--D6-MATRIX feedback_rule 检查 Q1 行动是否具体（不能写"加强关注"），但 Q2/Q3/Q4 的差异化训练强度较弱，需在 `tutorial.ipynb` 追问中补强。

### 自检 2 · Feed Back: AT 是否测量 ILO？
- ILO1 的 AT (TODO1+TODO3 单元测试 + D1.1 先测题) 是否测量"三方法对比 + 数据需求"？**是**--单元测试检查 CLV 均值合理性，D1.1 检查 BG/NBD 假设阐述。
- ILO2 的 AT (TODO2 单元测试 + D2 Independent) 是否测量"RFM 五类分群"？**是**--五类非空 + 样本均衡 = 直接测量 ILO2。
- ILO3 的 AT 是否测量"三陷阱理解"？**部分**--AUC>=0.50 只测结果不测过程。**改进**：在 `tutorial.ipynb` exit artifact 要求学生口头解释"如果不用 stratify 会怎样"，作为 ILO3 的过程性 AT 补充。
- ILO4 的 AT 是否测量"行动差异化 + ROI 决策"？**是**--D1.3 决策不等式 + final 300 字分析直接测量。

### 自检 3 · Feed Forward: 不经 TLA 能过 AT 吗？若能 = 对齐失败
- ILO1 不经 D3-BGNBD Worked 能过 TODO3 吗？**不能**--BG/NBD 简化公式涉及 `discount_factor` 折现概念，不看不写 Worked 的学生大概率用 `discount_factor=1.0` (未折现)，TODO3 单元测试会捕获此错误。**对齐成功**。
- ILO2 不经 D2-RFM Worked 能过 TODO2 吗？**能**（部分）--学生可能直接 `pd.cut` 等距分箱也能跑通 TODO2，但分群不均衡。**对齐脆弱点**：TODO2 单元测试需补"每类样本量 >=5%"门槛才能堵住捷径。已在 mastery_threshold 中体现。
- ILO3 不经 D5-SKLEARN Worked 能过 TODO4+TODO5 吗？**不能**--不写 `class_weight='balanced'` 则 RandomForest 多数类压倒，AUC 表面高但 Recall 极低；不写 `StandardScaler` 则 LogisticRegression 不收敛。`solution.ipynb` 与 D5 Worked 是必经路径。**对齐成功**。
- ILO4 不经 D6-MATRIX 能过 TODO6 吗？**能**（部分）--学生可能机械拼 `pd.cut(clv) × pd.cut(churn_prob)` 但 Q1 行动写空话。**对齐脆弱点**：D1.3 先测题与 final 300 字分析的"决策不等式 + 具体行动"是关键 AT，必须严格执行同伴互评，否则 ILO4 流于形式。

---

## 整体结论

- 4 ILO 中 2 个对齐稳健 (ILO1/ILO3)，2 个对齐脆弱 (ILO2/ILO4 需依赖先测题 + 互评堵捷径)
- mastery_threshold 已在每个 ILO 标注具体可测量门槛 (AUC 数值 / 分群样本量 / Q1 决策不等式)
- `tutorial.ipynb` 的 Hattie [FEED-FORWARD] 级反馈将针对 ILO2/ILO4 的脆弱点补强 (例: "你的 pd.cut 分群跑通了，但 Lost 类样本量=2，重新用 qcut 看分布均衡度")
