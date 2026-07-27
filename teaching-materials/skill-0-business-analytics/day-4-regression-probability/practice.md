# 刻意练习 - 回归分析与概率分布 (v6.0)

> 本单元刻意练习脚本: 基于 Ericsson 刻意练习 5 要素 + MIT 6.5940 渐退示例(Worked/Faded) + 交叉练习(A1B1C1)
> 真实库: statsmodels (OLS/Logit/QuantReg) + scipy.stats (norm/binom/poisson)
> 真实数据: causaldata NSW 职业培训实验 (LaLonde 1986, 445条), treat 系数=1621, LTV uplift 39.4%

---

## skill_target

能独立用 **statsmodels** 对 causaldata NSW 真实 RCT 数据拟合 OLS / Logit / 分位数回归, 用 **scipy.stats** 拟合正态/二项/泊松分布建模不确定性, 解读 treat 系数(1621)与 LTV uplift(39.4%) 的商业含义, 并用 VIF / 倾向性评分 / 异质性分位系数判断模型可信度。

---

## subskills

- **S1 (OLS+VIF)**: 能用 `sm.OLS(y, sm.add_constant(X)).fit()` 拟合多元线性回归, 解读 R²/系数/p值/95%CI, 用 `variance_inflation_factor` 检测多重共线性 (VIF>10 = 严重共线)
- **S2 (Logit+倾向性评分)**: 能用 `sm.Logit(y, X).fit()` 拟合逻辑回归, 计算倾向性评分 propensity score, 理解它是连接技能3因果推断的桥梁
- **S3 (分布+LTV+分位)**: 能用 `scipy.stats.norm/binom/poisson` 拟合分布计算概率, 用 `sm.QuantReg` 拟合分位数回归 (NSW 75分位 treat coef=2502 p=0.004 vs 25分位 290 p=0.520), 用回归+分布组合计算 LTV 点估计与概率区间

---

## diagnostic (诊断性前测, 3 道)

> 开练前先做, 暴露先验弱点, 决定从哪个 drill 起步。

- **D0.1**: 给定一段 `sm.OLS` 输出, treat 系数=1621, p=0.046, 95%CI=[32, 3210], R²=0.037。请用 3 句话向营销总监解释: (a) 系数含义 (b) 是否显著 (c) R² 低说明了什么
- **D0.2**: NSW 数据中 treat 在 75 分位上系数=2502 (p=0.004), 在 25 分位上系数=290 (p=0.520)。这说明营销干预对哪类用户有效? OLS 均值回归为何看不到这个差异?
- **D0.3**: 客服每日来电次数 / 转化(0/1) / 订单金额(取对数后) 各应选哪种概率分布(scipy.stats)? 写出对应参数名。

---

## drills (>=3, 每个含 difficulty / reps_required / feedback_rule / worked_faded)

### drill_id: D1
- **目标子技能**: S1 (OLS + VIF)
- **difficulty**: 2
- **reps_required**: 3
- **feedback_rule**:
  - 若 VIF 未计算 -> 提示: "先 `from statsmodels.stats.outliers_influence import variance_inflation_factor`, 对每个 X 算 VIF, 任一 >10 即严重共线"
  - 若把 treat 系数 1621 解读为"每花1元多挣1621元" -> 纠偏: "treat 是 0/1 干预变量, 系数=1621 表示干预组平均比对照组多 1621 单位, 不是弹性"
  - 若 R²=0.037 被当作"模型无用" -> 补充: "真实 RCT 数据 R² 常低, 重点是 treat 系数显著性与因果解释, 不是预测力"
- **worked_faded**:
  - Stage 1 (完整示范): 给出完整 `sm.OLS(y, sm.add_constant(X)).fit()` + `summary()` + VIF 循环代码与解读
  - Stage 2 (部分填空): 给出框架代码, 留空 `add_constant` / `fit` / VIF 公式三处让学生填
  - Stage 3 (独立解): 只给数据加载, 学生独立写 OLS + VIF + 解读

### drill_id: D2
- **目标子技能**: S2 (Logit + 倾向性评分)
- **difficulty**: 3
- **reps_required**: 3
- **feedback_rule**:
  - 若用 `sm.OLS` 而非 `sm.Logit` 拟合 0/1 -> 提示: "二值因变量必须 Logit/Probit, OLS 会出 [0,1] 外预测; 用 `sm.Logit(y, X).fit()`"
  - 若未输出 propensity score -> 提示: "`fittedvalues` 经 sigmoid 即得 P(treat=1|X), 用 `1/(1+np.exp(-fittedvalues))`"
  - 若混淆"倾向性评分"与"处理效应" -> 纠偏: "倾向性评分是 P(被分到干预组|X), 不是干预效应; 它用于匹配/加权, 是技能3 的入口"
- **worked_faded**:
  - Stage 1 (完整示范): 完整 Logit 拟合 + propensity 计算 + 直方图可视化代码
  - Stage 2 (部分填空): 给出 Logit 拟合, 留空 sigmoid 变换与绘图两处
  - Stage 3 (独立解): 给数据, 学生独立完成 Logit + propensity + 分布可视化

### drill_id: D3
- **目标子肤能**: S3 (分布 + LTV + 分位数回归)
- **difficulty**: 4
- **reps_required**: 3
- **feedback_rule**:
  - 若 LTV 点估计未给概率区间 -> 提示: "LTV = E[re78|treat=1] - E[re78|treat=0], 用 norm 拟合 re78 分布后做差, 给 95% 概率区间而非单点"
  - 若未用 QuantReg -> 提示: "`sm.QuantReg(y, X).fit(q=0.75)`, 对比 q=0.25/0.5/0.75 三个分位的 treat 系数"
  - 若把 75 分位系数 2502 当成均值效应 -> 纠偏: "分位系数是条件分位效应, 75 分位 treat=2502 只对高收入分位成立, 不能外推到全体; NSW LTV uplift 39.4% 是均值口径"
  - 若选错分布 -> 提示: "订单金额用 norm(对数后), 转化用 binom, 来电次数用 poisson; 选错会得负概率或方差不符"
- **worked_faded**:
  - Stage 1 (完整示范): norm/binom/poisson 三分布拟合 + QuantReg 三分位 + LTV 概率区间完整代码
  - Stage 2 (部分填空): 给分布拟合, 留空 QuantReg 调用与 LTV 区间计算
  - Stage 3 (独立解): 给数据, 学生独立完成分布选型 + 分位回归 + LTV uplift 39.4% 复现

---

## progressive_project (渐进式项目脚手架)

> 仿 MIT CS230 proposal->milestone->final->poster 四阶段, 本单元三阶段:

- **Stage P1 (proposal)**: 写 200 字方案 -- 用 NSW 数据回答"营销干预对哪类用户有效", 选 OLS/Logit/QuantReg 中的哪种, 为什么
- **Stage P2 (milestone)**: 提交 OLS + Logit 代码, 至少得到 treat 系数与 propensity score, VIF 通过
- **Stage P3 (final)**: 提交完整 notebook, 含分位数回归 + LTV 概率区间 + 300 字商业解读, 复现 LTV uplift 39.4%

---

## interleaving (交叉练习, A1B1C1 模式, 不块状)

> 仿 MIT Open Learning 明文原则: 三个子技能交叉排布, 不块状刷题。
> A=S1(OLS+VIF), B=S2(Logit+propensity), C=S3(分布+LTV+QuantReg)

排布序列 (每字母后数字代表第几次出现):
- **A1** D1 Stage1 (worked) -> **B1** D2 Stage1 (worked) -> **C1** D3 Stage1 (worked)
- **B2** D2 Stage2 (faded) -> **C2** D3 Stage2 (faded) -> **A2** D1 Stage2 (faded)
- **C3** D3 Stage3 (independent) -> **A3** D1 Stage3 (independent) -> **B3** D2 Stage3 (independent)

每轮穿插 diagnostic 复盘 1 道, 强制提取练习 (retrieval practice) 与交叉 (interleaving), 避免块状刷题的假性掌握。

---

## retry_policy

- 每个 drill 单次 reps 未达 reps_required(3) 不算通过
- Stage3 独立解错误率 >30% -> 回退到 Stage2 (faded) 重做
- 仿 CS229 pset0: diagnostic D0 全错者, 先做 D1 Stage1 worked 再开练
- 仿 CS230: 允许 2 次 late retry, 每次 -10% 分数 (上限 -20%)

---

## weak_loop (弱项循环)

> 连续 2 次失败触发弱项循环: 回退到上一 drill + 补充 worked example

- D1 连续 2 次未过 -> 回退到 diagnostic D0.1 重做 + 看 D1 Stage1 完整示范
- D2 连续 2 次未过 -> 回退到 D1 Stage3 通过版 + 看 D2 Stage1 完整示范
- D3 连续 2 次未过 -> 回退到 D2 Stage3 通过版 + 看 D3 Stage1 完整示范 + 复习 scipy.stats 三分布选型表
- 弱项循环通过后, 原 drill 重置 reps_required +1 (即需多练 1 次)

---

*本 practice.md 由 v6.0 学习科学层升级生成, 不破坏 v5.0 基线 (notes.md/data/README/starter.ipynb/solution.ipynb/reading.md)。*
*最后更新: 2026-07-25*
