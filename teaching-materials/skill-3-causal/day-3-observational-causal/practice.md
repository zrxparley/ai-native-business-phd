# 刻意练习 - Day 3 观测因果 (NSW+CPS PSM + close_college IV + DML)

> v6.0 学习科学层 · Ericsson 刻意练习 5 要素 + MIT 渐退示例 (Worked-Faded) + 交叉 interleaving

## skill_target

能在**真实观测数据** (NSW+CPS 观测对照 / close_college IV 数据) 上独立完成一条完整观测因果推断链路：识别混杂 → 选 PSM/IV/DML → 估计 → 稳健性检验 → 解释 LATE/ATE 差异，并为一个营销观测场景辩护方法选择。

## subskills

- **S1 混杂诊断**：在 NSW+CPS 数据上识别自选择偏差来源（可观测 vs 未观测混杂），量化朴素估计的偏误大小
- **S2 PSM 链路**：倾向得分估计 → 匹配 → 平衡检验（SMD<0.1）→ ATT 估计 → 安慰剂反驳，全程 DoWhy/statsmodels
- **S3 IV 链路**：用 close_college (Card 1995) 验证工具变量三假设（相关性/独立性/排他性），2SLS 估计 LATE，对比 OLS 解释差异
- **S4 DML 前沿**：用 econml.dml 或 DoubleML 在 NSW+CPS 上对比 PSM vs DML 估计，理解"放松函数形式但不放松可忽略性"

## diagnostic (前测 3 道，定位起点)

1. NSW 实验对照 vs CPS 观测对照：朴素估计（均值差）哪个更偏？偏向哪一边？写出你的推断与依据。
2. 给定 Z=nearc4（住近大学），T=educ（受教育年限），Y=lwage（对数工资）：请逐一论证 Z 是否满足 IV 三假设，并指出哪个假设最可能在营销"门店→促销→转化"映射中破裂。
3. PSM 估计的 ATT = $1,600，DML 估计的 ATT = $1,200，朴素估计 = $2,500。这三个数告诉你关于混杂结构的什么信息？哪个最可信？为什么？

## drills (>=3, 每 drill 含 difficulty/reps_required/feedback_rule/worked_faded)

### drill_id: D1
- **difficulty**: 2
- **reps_required**: 3
- **目标子技能**: S2 PSM 链路 (NSW+CPS)
- **feedback_rule**: 若学生在 TODO4 (DoWhy+PSM) 估计的 ATT 与朴素估计差 < $200，反馈"请检查公共支撑限制与协变量平衡 SMD<0.1；NSW+CPS 是观测对照，自选择偏差应使朴素估计偏大 $600-$1000，参考 LaLonde 1986 经典结论"。若平衡检验未通过，反馈"matched sample 仍失衡 = PSM 假设破裂，需换 IV 或加交互项"。
- **worked_faded**:
  - *Worked (完整示范)*：教师演示 `causaldata.nsw_mixtape` + `cps_mixtape` 合并 → Logistic 估计 e(X) → 1:1 nearest neighbor 匹配 → SMD 表 → ATT
  - *Faded (部分填空)*：starter.ipynb TODO4 给出 DoWhy 框架，学生填 propensity score model + matching method
  - *Independent*：学生独立换协变量集（去掉 `re74`），重估 ATT，解释变化

### drill_id: D2
- **difficulty**: 3
- **reps_required**: 3
- **目标子技能**: S3 IV 链路 (close_college)
- **feedback_rule**: 若学生 2SLS 估计的教育回报 > OLS 估计 50% 以上，反馈"经典 IV vs OLS 差异通常在 10%-40%，超出说明你混淆了 LATE 与 ATE--IV 估计的是 compliers（因近大学而多读书的人）的效应，不是全局 ATE，参考 Card 1995"。若学生未检查第一阶段 F 统计量，反馈"弱工具变量检验缺失：第一阶段 F<10 = 弱工具，2SLS 估计有偏，需 Hausman 检验"。
- **worked_faded**:
  - *Worked*：教师演示 `causaldata.card` 加载 → first stage `educ ~ nearc4 + controls` → second stage `lwage ~ \hat{educ} + controls` → LATE 解释
  - *Faded*：starter.ipynb TODO6 给 2SLS 框架，学生填工具变量列名与控制变量集
  - *Independent*：学生换一个"可疑工具"（如 `nearc2`），重估并对比 LATE 稳定性

### drill_id: D3
- **difficulty**: 4
- **reps_required**: 3
- **目标子技能**: S4 DML 前沿对比 (NSW+CPS 上 PSM vs DML)
- **feedback_rule**: 若学生 DML 估计与 PSM 差异 < 5%，反馈"差异小说明函数形式不是主要瓶颈，混杂结构线性可分；但请仍报告 cross-fitting 折数与 nuisance learner 选择，参考 Chernozhukov 2018 (arXiv 1705.07626)"。若学生声称 DML 解决了未观测混杂，反馈"致命误解：DML 用 ML 放松函数形式假设，但不放松可忽略性--NSW+CPS 的未观测混杂（如上进心）DML 仍无能为力，需 IV。请重读 notes.md DML 段落"。
- **worked_faded**:
  - *Worked*：教师演示 `econml.dml.LinearDML` → first stage ML (RandomForest) 估 E[T|X], E[Y|X] → 残差回归 → 对比 PSM
  - *Faded*：给框架，学生填 `model_t` / `model_y` 的 learner 选择与 cross-fitting 折数
  - *Independent*：学生换 `DoubleML` 包重估，对比两个 DML 实现的估计差异，写一段 200 字辩护哪个更可信

## progressive_project (渐进式项目脚手架)

参考 MIT Sloan 行动学习 + CS230 翻转课堂四组件，按周渐进：

1. **Week 1 (proposal)**：选一个营销观测场景（优惠券/广告/促销），写 1 页 proposal：识别 T/Y/X/潜在未观测混杂，初判该用 PSM/IV/DML
2. **Week 2 (milestone)**：在 NSW+CPS 或 close_college 上跑通 baseline PSM 或 IV，提交代码 + 200 字解读
3. **Week 3 (final)**：加入 DML 对比 + 反驳检验（安慰剂处理/子集），提交 1500 字报告 + 5 分钟话术
4. **Week 4 (poster)**：2 分钟同伴评审，devil's advocate 互质三问（参考哈佛 HBS case method）

## interleaving (A1B1C1 交叉，禁块状)

**明文交叉排布**（参考 MIT 6.5940 提取练习 + 交叉练习）：

- A = PSM (NSW+CPS) / B = IV (close_college) / C = DML (NSW+CPS)
- **Round 1**：A1 (D1 Worked) → B1 (D2 Worked) → C1 (D3 Worked) —— 三链路各看一次完整示范
- **Round 2**：B2 (D2 Faded) → C2 (D3 Faded) → A2 (D1 Faded) —— 故意打乱顺序，强制切换方法心智模型
- **Round 3**：C3 (D3 Independent) → A3 (D1 Independent) → B3 (D2 Independent) —— 独立解时顺序再倒，检验迁移
- **禁忌**：不要 A1→A2→A3 块状练完再换 B，块状练习短期流畅度高但 1 周后遗忘率 +40% (Butler 2010)

## retry_policy

参考 CS229 pset0 + CS230 late-day 政策：

- 每个 drill 首次未达 reps_required=3 的熟练标准（自评 <4/5 或反馈规则触发）→ 允许重做，不扣分
- 全单元 10 个 "late points" 额度，每次重做扣 1 点，鼓励试错但不纵容拖延
- 连续 2 次失败 → 触发 weak_loop（见下）
- 重做时禁用 solution.ipynb，只能回看 worked example

## weak_loop (连续 2 次失败触发)

若学生在同一 drill 连续 2 次未达熟练标准：

1. **回退一级**：从 Independent 退到 Faded，从 Faded 退到 Worked
2. **补 worked example**：教师补一个变体 worked example（如换数据子集、换协变量），学生先看完再练
3. **诊断盲点**：跑 tutorial.ipynb Socratic loop，让 LLM tutor 追问 3 轮定位是概念盲点（如混淆 LATE/ATE）还是代码盲点（如 DoWhy API 不熟）
4. **重新出题**：换一个等价 but 不同的真实数据子集（如 NSW 男性子集 vs 全样本），重测
5. **过关条件**：连续 2 次自评 >=4/5 且反馈规则未触发，方可返回原 drill 序列

---

*v6.0 学习科学层 · Ericsson 刻意练习 + MIT Worked-Faded + Butler 2010 交叉练习证据*
