---
unit: elective-e2-marketing-analytics/day-2-clv-churn-prediction
topic: CLV与流失预测 (BG/NBD + RFM + sklearn Logistic/RandomForest + AUC/PR)
version: v6.0 学习科学层
---

# practice.md · Day 2 刻意练习 (Ericsson + MIT CS229 + Harvard/Stanford Worked-Faded)

> 本文件配合 `starter.ipynb`（TODO1-6 脚手架）与 `solution.ipynb`（参考答案）。练习目标不是"看完会做"，而是"独立写出可跑代码并解释每一个参数选择"。

## skill_target

**核心可观察技能**：给定 NSW 真实 RCT 数据 (`causaldata.nsw`)，独立完成"RFM 分群 → BG/NBD 简化 CLV 预测 → sklearn 流失建模 (LogisticRegression vs RandomForest, stratify + class_weight='balanced' + StandardScaler) → AUC-ROC/Precision/Recall 评估 → CLV × 流失四象限行动矩阵"全链路，并能口头解释 `retention_rate`、`discount_factor`、`class_weight`、`stratify` 在 B2B/B2C 场景中的工程取舍。达成 = 6 个 TODO 全跑通 + 300 字分析报告通过同伴互评。

---

## diagnostic（CS229 pset0 式先测题，3 道，10 分钟）

> 先测目的：探测本 Day 的先验缺口。答不出 → 不要跳过 worked example；答对 → 直接进入 D2/D3。

### D1.1 概念辨析
某 B2B SaaS 客户合同年付 12 万元，过去 3 年留存率 0.85，折现率 0.1。请用「简单预测 CLV」公式估算该客户 5 年期望 CLV（写出 `expected_months = 1/churn_rate` 推导）。如果改用 BG/NBD，需要哪两类新假设？为什么 B2B 场景 BG/NBD 可能违背？

### D1.2 评估盲点
你训练 LogisticRegression 流失模型，accuracy=0.92。但流失客户只占 8%。这个 0.92 可信吗？请改用哪两个指标重新评估？如果改用 RandomForest 后 AUC=0.55，可能的原因是什么（从 NSW 数据特征维度思考）？

### D1.3 行动矩阵
Q1（高 CLV × 高流失风险）有 500 人，平均 CLV 3000 元。若挽留成功率 30%，营销预算 10 万元，单客挽留成本 200 元。该不该做？写出 `retained_value = 500 × 0.3 × 3000` vs `cost = 500 × 200` 的决策不等式。

---

## subskills（拆 3 个子技能）

- **S1 · 描述性 RFM 分群**：用 pandas 把 NSW `re74/re75/re78` 映射为 Recency/Frequency/Monetary，产出 R+F 组合分群（Champions / Recent / At Risk / Hibernating / Lost 五类）。关键技能 = `pd.cut` 分箱 + `pd.qcut` 等频分箱的选择。
- **S2 · 预测性 CLV 公式**：手写 BG/NBD 简化版 `pred_clv = F × retention^12 × AOV × 12 × discount`，理解 Poisson 购买率 + Beta 流失概率两大假设，能用 numpy 向量化计算 445 个客户的 CLV 分布与价值四分位。
- **S3 · 流失建模 + 业务行动**：用 sklearn `LogisticRegression(class_weight='balanced')` 与 `RandomForestClassifier` 建模，`train_test_split(stratify=y)` + `StandardScaler`，输出 AUC-ROC / classification_report，并把流失概率 × CLV 拼成四象限行动矩阵。

---

## drills（≥3 个，每个含 drill_id/difficulty/reps_required/feedback_rule/worked-faded 三阶段）

### drill_id: D2-RFM
- **difficulty**: 2
- **reps_required**: 3
- **feedback_rule**: 检查 R/F/M 三列是否用 `pd.qcut` 4 分位（不是 `pd.cut` 等距，除非用户故意）。Recency 越小越好（近），Frequency/Monetary 越大越好。Champions = R 高分位 + F 高分位。若学生直接 `pd.cut(re74, bins=4)` 等距分箱 → 反馈"零售场景 F/M 通常重尾分布，等距会被 0 大量占据，改 qcut 看分群均衡度"。
- **worked_faded**:
  - **Worked（完整示范）**：`df['R'] = pd.qcut(df['days_since_last'], 4, labels=[4,3,2,1]).astype(int)` 完整代码 + 注释解释 `labels=[4,3,2,1]` 为什么倒序。
  - **Faded（部分填空）**：给出 `df['F'] = pd.qcut(df['<填空>'], 4, labels=[?])` 学生填 frequency 列名与 label 顺序。
  - **Independent（独立解）**：学生独立写出 `df['M'] = pd.qcut(df['re78'], 4, labels=[1,2,3,4])` 并解释为什么 Monetary label 升序。

### drill_id: D3-BGNBD
- **difficulty**: 4
- **reps_required**: 2
- **feedback_rule**: BG/NBD 简化公式 `pred_clv = F × retention^12 × AOV × 12 × discount_factor`。常见错误：① 忘了 `discount_factor`（折现到现值）② 把 retention 写成 churn（二者互补）③ 没用 numpy 向量化而是 for 循环 445 次（性能惩罚）。若学生 `discount_factor=1.0` → 反馈"长期 CLV 不折现等于假设资金无成本，BG/NBD 论文默认 0.1-0.15，金融场景必须 <1"。
- **worked_faded**:
  - **Worked**：完整示范 `discount_factor = 1 / (1 + 0.1) ** np.arange(1, 13)` + CLV = Σ(discounted_monthly_profit)。
  - **Faded**：给出 `pred_clv = df['F'] * (df['<retention_or_churn>'] ** 12) * df['AOV'] * 12 * <?>` 学生补 retention 与 discount_factor。
  - **Independent**：学生独立用 numpy 向量化计算 445 客户 CLV，并用 `np.percentile(pred_clv, [25,50,75,90])` 看价值四分位。

### drill_id: D5-SKLEARN
- **difficulty**: 5
- **reps_required**: 2
- **feedback_rule**: 三大陷阱必查：① 是否 `stratify=y`（NSW 流失仅 ~20%，不 stratify 则 test 集分布漂移）② LogisticRegression 是否 `StandardScaler.fit_transform(X_train)` 后再 `transform(X_test)`（数据泄露检查）③ RandomForest 是否 `class_weight='balanced'`（否则多数类压倒）。若学生 AUC < 0.55 → 反馈"NSW 只有基线人口学特征（age/educ/marr），行为特征缺失，这正是教学价值点：理解为什么真实营销需要登录频率/会话时长/客服投诉才能 AUC>0.80"。
- **worked_faded**:
  - **Worked**：完整示范 `X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)` + `scaler = StandardScaler().fit(X_train)` + `LogisticRegression(class_weight='balanced').fit(scaler.transform(X_train), y_train)`。
  - **Faded**：给出 RandomForest 对比骨架但 `class_weight=<??>`、`scaler.transform(X_???)` 留空。
  - **Independent**：学生独立写 `roc_auc_score(y_test, rf.predict_proba(X_test)[:,1])` 与 `classification_report`，并能解释为什么 Precision 比 Accuracy 更重要。

### drill_id: D6-MATRIX（进阶，可选）
- **difficulty**: 4
- **reps_required**: 1
- **feedback_rule**: 四象限必须用 `pd.cut(clv, 2) × pd.cut(churn_prob, 2)` 交叉分箱。Q1（高 CLV 高风险）必须有具体行动（专属客户经理/深度折扣），不能写"加强关注"这种空话。若学生 Q1 人数 = 0 → 反馈"检查 clv/churn 分箱中位数是否合理，NSW 数据 re78=0 占比高，流失概率普遍高，可能需要 70 分位而非中位数切"。
- **worked_faded**:
  - **Worked**：完整 `df['quadrant'] = np.where((df.clv_high & df.churn_high), 'Q1-优先挽留', ...)`。
  - **Faded**：Q2/Q3/Q4 留空。
  - **Independent**：学生独立产出 Q1 客户数 × 平均 CLV × 挽留成功率 = 可挽回价值，对应到 `solution.ipynb` TODO6 输出。

---

## progressive_project（CS230 式渐进交付）

- **proposal（D2 当天提交）**：300 字方案——你将如何把 NSW re78=0 定义为流失标签？为什么这个定义在 B2B 场景可能不合适？BG/NBD 两大假设哪个在 NSW 上更可能被违背？
- **milestone（D2+3 天）**：跑通 TODO1-3，输出历史 CLV 均值 + BG/NBD 简化 CLV 均值 + 二者差异的解释。
- **final（D2+7 天）**：跑通 TODO4-6，输出 LogisticRegression AUC / RandomForest AUC / Q1 客户数 + 300 字分析。
- **poster（D2+10 天，可选）**：一页 slide——「NSW 数据上流失预测为何 AUC≈0.54？真实营销场景需要补什么特征？」给同学 2 分钟讲解。

---

## interleaving（交叉练习，A1B1C1...B2C2A2...C3A3B3 排布，禁止块状）

> 理由：CLV/RFM/流失建模 三者相互引用（RFM 输出是流失特征，CLV 是行动矩阵的另一轴），块状练习会让学生忘记前一个。交叉排布促进近迁移。

**推荐顺序（一次 session 约 90 分钟）**：
- A = D2-RFM（S1），B = D3-BGNBD（S2），C = D5-SKLEARN（S3）
- Round 1: **A1** 做完 Worked+Faded → **B1** Worked → **C1** Worked（每个 15 min）
- Round 2: **B2** Faded → **C2** Faded → **A2** Independent（每个 15 min）
- Round 3: **C3** Independent → **A3** Independent → **B3** Independent（每个 15 min）

> 反例（**禁止**）：先把 A1/A2/A3 全做完再开始 B——这是块状练习，符合直觉但迁移效果差（Roediger & Karpicke 2006）。

---

## retry_policy（CS230 式）

- 10 free late days 全学期（本 Day 最多用 3 天）
- D2/D3/D5 任意 drill 失败可重做，**重做不扣分**，只记最后一次通过版本
- 失败定义：`verify_unit.py` 跑不通 / AUC < 0.55（NSW 基线场景）/ 四象限 Q1 人数逻辑错（如 0 或全量）

---

## weak_loop（连续 2 次失败触发弱项循环）

判定：同一 drill 连续 2 次未通过 → 触发：
1. 回退到上一难度 drill（D5 失败 → 回 D3；D3 失败 → 回 D2）
2. 重做对应 Worked example（不允许跳 Worked 直奔 Faded）
3. 补充 worked example：导师用 `solution.ipynb` 对应 TODO 段落，逐行注释 `class_weight='balanced'` / `stratify=y` / `discount_factor` 三个工程取舍
4. 重新进 Faded 前，学生口头解释"为什么 NSW 上 AUC≈0.54 是预期的"——若解释不出，回 Worked 再来一轮

> 弱项循环不计入 retry 次数，但触发 3 次以上需导师介入诊断先验知识缺口（通常是 OLS / 逻辑回归 / 评估指标三者之一）。
