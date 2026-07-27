# 刻意练习 (Deliberate Practice) · 价值创造+定价 · v6.0

> **本文件落地 Ericsson 刻意练习 5 要素 + MIT 提取/间隔/交叉/Worked-Faded**。所有 drill 的 `feedback_rule` 均回指 v5.0 既有真实库 (`statsmodels OLS R²=0.859` / `numpy-financial NPV` / `scipy.stats` 价格弹性 `-0.6169` / 天道推演 10k 蒙特卡洛)。

---

## skill_target

学生在 90 分钟内, 给定一组真实 AI API 定价数据 (OpenAI/Anthropic/Google/DeepSeek 官方页) + DeepSeek V3 训练成本 $5.576M, 能独立产出**一份定价决策备忘录**: (a) 用 `statsmodels.OLS` 量化定价驱动因素并解读 R²/系数/p值; (b) 用 `numpy-financial` 计算 NPV/IRR/payback 评估财务可行性; (c) 用 `scipy.stats` 估计价格弹性置信区间; (d) 用天道推演 10k 蒙特卡洛沙盘给出最优定价路径与风险预警。

## diagnostic (前测 3 道, 触发弱项循环判定)

- **D0-1**: 给定 `output_price ~ context_window + value_mechanism + has_reasoning + provider` 的 OLS 输出 R²=0.859, 解释"上下文窗口系数 p=0.003 但 provider 系数 p=0.42"对定价决策的含义。→ 诊断 OLS 解读能力
- **D0-2**: DeepSeek V3 训练成本 $5.576M, 若选择 10% 折现率、5 年现金流, 问"成本加成 vs 撇脂"哪种策略更可能在 NPV 上为正? 仅凭直觉选择并说明假设。→ 诊断 NPV 直觉
- **D0-3**: 弹性点估计 = -0.6169, 95% CI = [-1.02, -0.21], 问"是否应基于点估计直接涨价"? → 诊断小样本不确定性意识

> 诊断任一题答错或答"不知道"→ 该子技能进入 `weak_loop` (见文末)。

## subskills

- **S1. OLS 定价驱动建模**: 能用 `sm.OLS(y, sm.add_constant(X)).fit()` 拟合多元线性回归, 正确解读 R²/系数/p值/CI, 区分"显著"与"经济意义"。
- **S2. NPV/IRR/payback 财务评估**: 能用 `npf.npv(rate, cashflows)` / `npf.irr(cashflows)` / `npf.payback(cashflows)` 计算四种定价策略 (成本加成/价值定价/渗透/撇脂) 的财务可行性, 给定 DeepSeek V3 真实训练成本。
- **S3. 弹性估计 + 天道推演蒙特卡洛**: 能用 `scipy.stats` 估计弹性置信区间; 能用天道推演框架对竞品反应做 10k 蒙特卡洛沙盘, 输出最优路径的概率分布而非单一预测。

---

## drills (3 个, 每个 3 阶段 Worked → Faded → Independent)

### drill D1 · OLS 定价驱动建模 (subskill S1)

- **drill_id**: D1
- **difficulty**: 3 (1-5 量表)
- **reps_required**: 3
- **feedback_rule**:
  - 若学生漏写 `sm.add_constant(X)` → 反馈: "你忘了截距, OLS 默认无常数项。回看 `statsmodels` 文档 `sm.add_constant`, 重做。"
  - 若学生把 p>0.4 的 provider 系数当"显著" → 反馈: "p=0.42 不是 <0.05, 不能声称 provider 显著影响定价。回看 notes.md `关键回顾 1`。"
  - 若学生只报 R²=0.859 不报 CI → 反馈: "R² 高不等于系数可信。报每个系数的 95% CI。"
- **worked_faded**:
  1. **Worked (完整示范)**: 完整代码 `sm.OLS(y, sm.add_constant(X)).fit()`, 完整解读 R²=0.859 / context_window 系数 / p=0.003 / 95% CI, 学生只需阅读并复述。
  2. **Faded (部分填空)**: 给出框架代码, 留空 `__A__ = sm.add_constant(__B__)` 和 `model = sm.OLS(__C__, __D__).fit()`, 学生填空。
  3. **Independent (独立解)**: 给定新数据集 (只给 8 行), 学生从零写 OLS 拟合并产出解读段。

### drill D2 · NPV/IRR/payback 财务评估 (subskill S2)

- **drill_id**: D2
- **difficulty**: 4
- **reps_required**: 3
- **feedback_rule**:
  - 若学生用 `npf.npv(rate, cashflows)` 但 cashflows 第 0 期写成正数 → 反馈: "第 0 期是投资流出, 必须 ≤ 0 (DeepSeek V3 训练成本 -$5.576M)。重看 numpy-financial 约定。"
  - 若学生 IRR 算出 NaN 不报错 → 反馈: "IRR 在符号多次变化时可能无解或多解。检查现金流符号序列。"
  - 若学生比较 4 种策略只看 NPV 不看 payback → 反馈: "撇脂策略 NPV 可能最高但 payback 最长。决策必须并列 NPV + IRR + payback 三指标。"
- **worked_faded**:
  1. **Worked**: 完整 4 策略 NPV/IRR/payback 表格 + 解读"为什么价值定价 IRR=38% 而渗透 IRR=22%"。
  2. **Faded**: 给出 `npf.npv(0.10, [-5.576, __A__, __B__, ...])` 留空现金流, 学生填。
  3. **Independent**: 给定新折现率 8% 和新 5 年现金流, 学生独立算 4 策略三指标并排名。

### drill D3 · 弹性 CI + 天道推演 10k 蒙特卡洛 (subskill S3)

- **drill_id**: D3
- **difficulty**: 5
- **reps_required**: 3
- **feedback_rule**:
  - 若学生基于点估计 -0.6169 直接做定价决策 → 反馈: "点估计不是决策依据。报 95% CI [-1.02, -0.21], 问自己'若真值是 -1.02 涨价会损失多少需求'。"
  - 若学生蒙特卡洛只跑 100 次就下结论 → 反馈: "100 次采样误差过大。天道推演约定 ≥10k 次。重跑 `np.random.seed(42); samples = np.random.choice(..., size=10000)`。"
  - 若学生沙盘只展开 immediate 层 → 反馈: "天道推演要求 3 层 (immediate/near/far)。补 near (3-6月) 和 far (1-2年) 两层。"
- **worked_faded**:
  1. **Worked**: 完整 `scipy.stats.linregress` 弹性估计 + 完整 10k 蒙特卡洛 + 3 层推演树解读。
  2. **Faded**: 给出蒙特卡洛框架 `for _ in range(10000): ...`, 留空采样分布和聚合步骤。
  3. **Independent**: 给定新弹性先验和新竞品反应矩阵, 学生独立产出最优定价路径概率分布 + 风险预警。

---

## progressive_project (渐进式项目, MIT 4C/ID 脚手架)

参照 MIT 6.5940 / CS230 渐进交付节奏:

- **M1 (Day 2 课中)**: 完成 D1+D2+D3 的 Worked 阶段, 提交解读段 (200 字)。
- **M2 (Day 2 课后 3 天)**: 完成 D1+D2+D3 的 Faded 阶段, 提交填空代码 + 解读。
- **M3 (Day 2 课后 7 天)**: 完成 D1+D2+D3 的 Independent 阶段, 提交完整定价决策备忘录 (含 OLS 表 + NPV 表 + 弹性 CI + 蒙特卡洛概率分布图 + 3 层推演树)。
- **M4 (Day 2 课后 14 天)**: 同伴互评 (参照 Harvard CS229 Ed Discussion 模式), 接受 2 份同伴反馈并修订, 提交终版。

> 每里程碑返回 `student_model.json` (见 tutorial.ipynb cell 4) 更新掌握度。

---

## interleaving (交叉练习, A1B1C1...B2C2A2...C3A3B3 模式)

**明文排布** (不块状): 学生在 90 分钟训练中按以下顺序练习, 强制交叉, 不允许"先做完所有 D1 再做 D2":

```
A1 = D1 Worked   →  B1 = D2 Worked   →  C1 = D3 Worked
→  B2 = D2 Faded  →  C2 = D3 Faded   →  A2 = D1 Faded
→  C3 = D3 Indep  →  A3 = D1 Indep   →  B3 = D2 Indep
```

理由 (Butler 2010 + MIT Open Learning): 交叉练习迫使大脑反复检索不同子技能的入口, 比块状练习提升长期保留 ~30%。本单元交叉 S1 (OLS) / S2 (NPV) / S3 (弹性+蒙特卡洛) 三个子技能, 模拟真实定价决策中"建模→财务→博弈"的交错思维。

---

## retry_policy

- 每份 drill 提交后, 若 `feedback_rule` 触发任一条 → 必须修订并重交, **不扣分** (参照 Stanford CS230 10 late days + 20%/天罚分, 但本单元学习期不罚分)。
- Independent 阶段最多重试 2 次; 第 3 次仍失败 → 触发 `weak_loop`。
- 蒙特卡洛若 100 次以下采样被判失败, 必须重跑 10k 次 (硬约束, 不可豁免)。

---

## weak_loop (连续 2 次失败触发)

若学生在同一 drill 的 Independent 阶段连续 2 次未达标:
1. **回退**: 退到该 drill 的 Faded 阶段重做 2 reps。
2. **补充 worked example**: 触发 tutorial.ipynb 的 Socratic loop, 牛津 fellow 用追问引导学生自己发现错误 (不直接给答案)。
3. **诊断盲点**: 写入 `student_model.json` 的 `blind_spots` 字段, 跨单元复用 (Day 3 Agent 经济会调用本单元的定价模型)。
4. **重测**: 24 小时间隔后 (利用 FSRS-6 间隔效应), 重做 Independent 阶段一次。若仍失败 → 进入 1v1 真人答疑通道 (超出 agent 能力范围)。

---

*本文件 v6.0 新增。所有 feedback_rule 回指 v5.0 既有真实库与数据: statsmodels OLS R²=0.859 / numpy-financial NPV (DeepSeek V3 $5.576M) / scipy.stats 弹性 -0.6169 / 天道推演 10k 蒙特卡洛。*
