---
unit: elective-e2-marketing-analytics/day-3-mmm-mta-incremental
topic: MMM/MTA增量测量 (Marketing Mix Modeling + Multi-Touch Attribution + Incremental, Bayesian, DoWhy)
version: v6.0
skill_target: 能独立用 statsmodels+sklearn+scipy+causaldata NSW 真实数据完成 MMM 全流程(Adstock+Ridge+R²+贡献分解)、MTA 马尔可夫移除法、合成控制+DML 增量测量、scipy.optimize 预算优化，并能解释每一步的因果与统计依据。
subskills: [S1_MMM_Adstock_Ridge, S2_Causal_Incremental_RCT_SyntheticControl_DML, S3_BudgetOptimization_KKT_IncrementalValidation]
---

# 刻意练习 · MMM/MTA 增量测量 (v6.0)

> 基于 Ericsson 刻意练习 + MIT 6.867 pset 风格 + Harvard/Stanford worked-faded 渐退示范。所有 drill 领域特定,引用本单元真实库 (statsmodels/sklearn/scipy/causaldata) 与真实数据 (NSW 445 样本 + 真实快消品 MMM 参数)。

---

## 一、Diagnostic 先测 (CS229 pset0 式, 3 题)

> 探测先验知识缺口。每题先独立答,再对照参考。若 3 题全错,先回退到 Day 1 描述性分析 + Day 2 CLV 的概念复习。

### D1 · MMM 模型方程与 Adstock 衰减
给定周度数据:渠道投入 `Spend_search,t`, `Spend_social,t`, `Spend_tv,t`,销量 `Sales_t`,控制变量 `Holiday_t`, `Price_t`。
- 写出 MMM 的 Ridge 回归模型方程 (含 Adstock 变换)
- 给定 Search λ=0.2, Social λ=0.5, TV λ=0.8,写出三者 Adstock 递推式
- 解释为什么用 Ridge 而非 OLS (Hint: 渠道共线性)

### D2 · MTA 马尔可夫移除法
给定 4 条用户路径:
```
[Search, Social, Email, Convert]
[Display, Social, No Convert]
[Search, Email, Convert]
[Social, Search, Convert]
```
- 画出状态集与一阶转移矩阵
- 解释 Removal Effect 的 5 步算法
- 反问:若完全移除 Social,基线转化率下降多少?

### D3 · NSW RCT 增量测量的偏差源
给定 NSW 数据描述:treat=1(收到培训) vs treat=0,结果 re78(1978 收入),协变量 re74/re75/age/educ。
- 朴素均值差 `E[re78|treat=1] - E[re78|treat=0]` 在 RCT 全样本上是否无偏?为什么?
- 若只看 treat=1 中 age<25 的子样本 vs treat=0 中 age>=25 的子样本,均值差有偏吗?偏差方向?
- 合成控制和 DML 各自如何修正这种偏差?

---

## 二、Subskills 拆解 (3 个子技能)

| Subskill | 描述 | 可观察行为 |
|:--------:|------|----------|
| **S1** MMM 拟合与诊断 | Adstock 变换 + Ridge 回归 + R² + 贡献分解 | 能在 starter TODO1 上独立写出 λ 经验值匹配 + Ridge 系数 + 贡献百分比 |
| **S2** 因果增量测量 | RCT 均值差 + 合成控制 ATT + DML 双重去偏 | 能在 TODO3-5 上对比四法估计,解释 ATT vs ATE 差距 |
| **S3** 预算优化与批判 | scipy.optimize + KKT 检验 + 增量验证 | 能在 TODO6 上求解预算分配,并用增量测试批判性检验 |

---

## 三、Drills (>=3, 每个 worked-faded 三阶段)

> 每个 drill 含 `worked`(完整示范) -> `faded`(部分填空) -> `independent`(独立解) 三阶段。重复至 reps_required 次全对。

### DRILL-01 · MMM-Adstock + Ridge 拟合

- **drill_id**: DRILL-01
- **difficulty**: 3
- **reps_required**: 5
- **feedback_rule**: 检查 Adstock 公式 λ 设定是否匹配渠道类型(Search 0.1-0.3 / Social 0.3-0.5 / Display 0.5-0.7 / Email 0.1-0.2 / TV 0.7-0.9);用 statsmodels OLS 与 Ridge 对比系数稳定性,VIF>10 必须用 Ridge;R² 报告必须同时报告 adjusted R²;贡献分解 = β_i × Adstock_i_mean / Σ(β_i × Adstock_i_mean),归一化。
- **worked_faded**:
  - **worked**(完整示范): 给定 Social 渠道 4 周 Spend=[10,20,15,5], λ=0.5,完整推导 Adstock=[10, 25, 27.5, 18.75];用 statsmodels Ridge 拟合 Sales,展示系数与 R²。
  - **faded**(部分填空): 给定 Search 渠道 4 周 Spend=[8,12,10,6], λ=0.2,你填 Adstock 第 3-4 项;用 sklearn Ridge(alpha=1.0) 拟合,你填 β_search 系数。
  - **independent**(独立解): 给定 TV 渠道 6 周 Spend, λ=0.8,独立写 Adstock 变换 + Ridge 拟合 + 贡献分解;并解释 TV 的衰减率为何高。

### DRILL-02 · MTA 马尔可夫移除法

- **drill_id**: DRILL-02
- **difficulty**: 4
- **reps_required**: 5
- **feedback_rule**: 用 numpy 构建一阶转移矩阵,验证行和=1;移除效应必须归一化(Σ=1);对比 Shapley 值法,讨论计算复杂度 O(n!) vs O(n²);识别"移除后转化率下降最多"的关键触点。
- **worked_faded**:
  - **worked**: 给定 3 条路径,完整构建 4 状态(Search/Social/Convert/Null)转移矩阵,计算基线转化率 0.5,移除 Social 后转化率 0.3,Removal Effect=0.4,归一化得 Social 功劳 40%。
  - **faded**: 给定 5 条路径,你填转移矩阵的 Search→Social 概率 + Social→Convert 概率。
  - **independent**: 给定 10 条真实风格路径(含 Display/Social/Search/Email/Convert/Null),独立完成移除法 + 归一化 + Shapley 对比。

### DRILL-03 · NSW 增量测量四法对比

- **drill_id**: DRILL-03
- **difficulty**: 4
- **reps_required**: 6
- **feedback_rule**: 用 causaldata NSW 445 真实样本;朴素均值差仅在全 RCT 样本无偏,观测子样本必偏;合成控制必须报告 pre-period 匹配 RMSE;DML 必须用 2-fold 或 5-fold 交叉拟合;报告 ATT vs ATE 差距,解释业务含义(增量率 2% vs 30% 的"收割 vs 创造")。
- **worked_faded**:
  - **worked**: 完整示范 NSW 全样本 RCT 朴素均值差 = $1794 (含标准误 + 95% CI);增量率与 ROI 公式推导。
  - **faded**: 你填合成控制权重 w 的约束条件 + pre-period RMSE;你填 DML 的 m(x)=E[T|X] 与 g(x)=E[Y|X] 残差化步骤。
  - **independent**: 独立完成四法对比表(朴素/合成控制/DML/RCT 真值),报告 ATT 与 ATE 偏差,讨论何时该用哪法。

### DRILL-04 · 预算优化 + 增量验证

- **drill_id**: DRILL-04
- **difficulty**: 5
- **reps_required**: 4
- **feedback_rule**: 用 scipy.optimize.minimize SLSQP;约束 Σx_i = B, x_i>=0;检验 KKT 条件(拉格朗日乘子符号);用增量测试批判:MMM 是历史外推,市场环境变化时优化结果可能失效,需用 Geo 实验 + CUPED 验证。
- **worked_faded**:
  - **worked**: 给定 3 渠道 MMM 系数 + B=$100k,完整示范 SLSQP 求解 + KKT 检验。
  - **faded**: 你填拉格朗日乘子 + 影子价格解释。
  - **independent**: 给定 5 渠道,独立求解 + 写 300 字增量验证方案(用 NSW 思路设计 Geo 实验 + CUPED 方差缩减)。

---

## 四、Progressive Project (CS230 式 4 阶段)

| 阶段 | 交付物 | 评分权重 | 关键标准 |
|:----:|--------|:--------:|---------|
| **proposal** (Week 1) | 选一个真实营销场景(快消/电商/B2B),定义业务问题 + 数据需求 + MMM/MTA/增量三方法组合方案 | 15% | 业务问题可测,数据可行,方法匹配场景 |
| **milestone** (Week 3) | MMM 拟合通过,R²>0.7,贡献分解可解释,Adstock λ 与渠道类型匹配 | 25% | R²>0.7 + λ 合理 + 系数稳定(VIF<10) |
| **final** (Week 5) | 加 MTA 移除效应 + NSW 增量测量 + DML,输出预算优化报告 | 40% | 四法对比可信 + 预算分配可解释 + 增量验证 |
| **poster** (Week 6) | 2 页海报,对比三方法优劣,标注数据需求与隐私合规 | 20% | 视觉清晰 + 批判性反思 + 业务可执行 |

---

## 五、Interleaving 交叉排布 (A1B1C1...B2C2A2...C3A3B3)

> 不块状练习,促进迁移。A=MMM, B=MTA, C=Incremental。

| 顺序 | 任务 | 子技能 | 时长 |
|:----:|------|:------:|:----:|
| A1 | DRILL-01 worked (Social Adstock + Ridge) | S1 | 20min |
| B1 | DRILL-02 worked (3 路径转移矩阵) | S2 | 20min |
| C1 | DRILL-03 worked (NSW 朴素均值差) | S2 | 20min |
| B2 | DRILL-02 faded (5 路径填空) | S2 | 25min |
| C2 | DRILL-03 faded (合成控制权重) | S2 | 25min |
| A2 | DRILL-01 faded (Search λ=0.2) | S1 | 25min |
| C3 | DRILL-03 independent (DML 交叉拟合) | S2 | 30min |
| A3 | DRILL-04 worked (3 渠道 SLSQP) | S3 | 30min |
| B3 | DRILL-02 independent (10 路径 + Shapley) | S2 | 35min |
| A4 | DRILL-04 independent (5 渠道 + 增量验证) | S3 | 40min |

---

## 六、Retry Policy (CS230 式)

- **10 free late days**: 整学期 10 天迟交免罚,鼓励试错
- **失败重试不罚分**: drill 未达 reps_required 可重做,取最高分
- **mastery 导向**: 不累计扣分,只看最终是否达到 mastery_threshold(见 alignment.md)

---

## 七、Weak Loop 弱项循环

> 连续 2 次失败触发弱项循环:

1. **检测**: 同一 drill 连续 2 次 reps 不达标
2. **回退**: 退到上一难度(如 DRILL-03 失败 -> 回到 DRILL-01 + DRILL-02 复习)
3. **补充 worked example**: 重看 worked 阶段完整示范,手抄一遍
4. **概念检索**: 查 schedule.json 对应 card(如 C3 合成控制),用 FSRS-6 间隔复习
5. **重做**: 用 faded 阶段重新进入,3 次连续正确才升级

**典型弱链**:
- MMM 系数不稳定 -> 回退到 Adstock 变换 + VIF 诊断 worked 示范
- DML 偏差大 -> 回退到合成控制 + RCT 朴素均值差 worked 示范
- 预算优化 KKT 不满足 -> 回退到 scipy.optimize 约束设定 worked 示范

---

*本 practice.md 基于 Ericsson 刻意练习 + MIT/Stanford worked-faded 渐退示范。领域特定反馈规则引用 statsmodels/sklearn/scipy/causaldata 真实库与 NSW 真实 RCT 数据。*
