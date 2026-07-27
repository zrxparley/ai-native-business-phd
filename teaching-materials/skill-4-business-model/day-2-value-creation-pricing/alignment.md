# Constructive Alignment - 价值创造+定价 (Skill 4 · Day 2)

> **Biggs 建构对齐 (Constructive Alignment)**: ILO (Intended Learning Outcomes) ↔ TLA (Teaching/Learning Activities) ↔ AT (Assessment Tasks) 三者必须对齐。本单元 v6.0 在 v5.0 既有的 starter/solution/reading 之上, 新增 practice.md / schedule.json / tutorial.ipynb 三个学习科学层文件, 目标是让"练什么 = 教什么 = 考什么"。

---

## ILO ↔ TLA ↔ AT 矩阵

| ILO (预期学习产出) | TLA (教学学习活动) | AT (评估任务) | mastery_threshold |
|---|---|---|---|
| **ILO1**: 能用 `statsmodels.OLS` 对真实 AI API 定价数据拟合多元线性回归 (`sm.OLS(y, sm.add_constant(X)).fit()`), 量化"什么驱动了 AI 产品定价" (R²=0.859), 正确解读 R²/系数/p值/95% CI | starter.ipynb TODO2 drill + practice.md D1 (Worked→Faded→Independent) + tutorial.ipynb Socratic loop 追问"p=0.42 vs p=0.003 含义" + schedule.json C1 间隔复习 | solution.ipynb OLS 单元 + 300 字解读段 (context_window 系数显著 vs provider 不显著) + tutorial 后测问"为何报 CI 而非点估计" | ≥80% (D1 Independent 阶段 3 reps 中至少 2 次正确解读 R²+p+CI 三要素) |
| **ILO2**: 能用 `numpy-financial` 计算 NPV/IRR/payback (`npf.npv()`/`npf.irr()`/`npf.payback()`), 基于 DeepSeek V3 真实训练成本 $5.576M, 评估四种定价策略 (成本加成/价值定价/渗透/撇脂) 的财务可行性 | starter.ipynb TODO3 drill + practice.md D2 (Worked→Faded→Independent) + tutorial.ipynb Socratic 追问"第 0 期符号为何必须为负" + schedule.json C2 间隔复习 | solution.ipynb NPV/IRR/payback 表 + 4 策略排名 + 蒙特卡洛敏感性 | ≥70% (D2 Independent 阶段 3 reps 中至少 2 次三指标全对 + 符号约定正确) |
| **ILO3**: 能用 `scipy.stats` 估计价格弹性置信区间 (点估计 -0.6169, 95% CI [-1.02, -0.21]), 理解小样本不确定性; 能用天道推演 10k 蒙特卡洛沙盘对竞品反应做 3 层推演树 (immediate/near/far) | starter.ipynb TODO4+TODO6 drill + practice.md D3 (Worked→Faded→Independent) + tutorial.ipynb Socratic 追问"为何 100 次采样不够" + schedule.json C3+C4 间隔复习 | solution.ipynb 弹性 CI + 10k 蒙特卡洛概率分布图 + 3 层推演树 + 风险预警 | 能独立解 (D3 Independent 阶段 3 reps 中至少 2 次产出完整概率分布 + 3 层推演树 + 风险预警三要素齐全) |

---

## mastery_threshold (总单元过关条件)

学生必须同时满足:
1. **三 ILO 各自阈值**: ILO1 ≥80% / ILO2 ≥70% / ILO3 能独立解。
2. **跨 ILO 整合**: 完成 300 字定价决策备忘录, 同时引用 OLS 结论 + NPV 排名 + 弹性 CI + 蒙特卡洛概率分布。
3. **间隔复习首日完成**: schedule.json 5 张卡片的首日复习 (due[0]=1) 全部完成, 自评 q≥3。
4. **tutorial 限频内完成**: 每日 1 次 tutorial 会话, 产出 exit artifact (2-3 盲点 + 推荐复习单元)。

未达标 → 进入 practice.md `weak_loop` (回退 Faded + 补充 worked + 24h 间隔重测)。

---

## 3 自检问题 (Biggs 三问, 对应 Hattie 三级反馈)

> Biggs (1996) 建构对齐的核心是"不经 TLA 不能过 AT"。本单元用以下 3 自检验证对齐性。

### 1. Feed Up - TLA 是否训练 ILO?
- ILO1 要求"解读 R²/系数/p/CI"——TLA 中 practice.md D1 是否训练了**解读**而非仅**计算**?
  - 自检: D1 的 feedback_rule 明确惩罚"只报 R² 不报 CI"——是。✓
  - 自检: tutorial.ipynb Socratic loop 用追问"p=0.42 含义"而非直接给答案——是。✓
- ILO2 要求"评估四种策略"——TLA 中 D2 是否训练了**比较**而非仅**计算单一策略**?
  - 自检: D2 feedback_rule 惩罚"只看 NPV 不看 payback"——是。✓
- ILO3 要求"3 层推演树"——TLA 中 D3 是否训练了**多层**?
  - 自检: D3 feedback_rule 惩罚"只展开 immediate 层"——是。✓

### 2. Feed Back - AT 是否测量 ILO?
- ILO1 的 AT (300 字解读段) 是否**测量解读能力**而非**抄写代码**?
  - 自检: 解读段必须包含"显著 vs 不显著"的判断 + CI 引用——是。✓
- ILO2 的 AT (4 策略排名表) 是否**测量比较能力**?
  - 自检: 排名必须并列 NPV+IRR+payback 三指标——是。✓
- ILO3 的 AT (概率分布图 + 3 层推演树) 是否**测量多层推演**?
  - 自检: 必须 immediate/near/far 三层齐全 + 风险预警——是。✓

### 3. Feed Forward - 不经 TLA 能过 AT 吗? 若能 = 对齐失败
- **临界检验**: 若学生跳过 practice.md D1-D3, 直接抄 solution.ipynb, 能过 AT 吗?
  - 自检: tutorial.ipynb 的 Socratic loop 会用追问"为什么 p=0.42 不显著"验证理解——抄 solution 的学生答不出→对齐成立。✓
- **临界检验**: 若学生跳过 schedule.json 间隔复习, 长期能保持吗?
  - 自检: schedule.json 的 due=[1,3,8,21,60,180] 强制 6 次复习——跳过则长期保留率 <50% (Butler 2010)→对齐成立。✓
- **临界检验**: 若学生跳过 tutorial.ipynb 的 student_model.json 更新, 跨单元 (Day 3) 能复用吗?
  - 自检: Day 3 Agent 经济会调用本单元的定价模型, student_model.json 记录盲点——跳过则 Day 3 无法个性化→对齐成立。✓

---

## 跨单元对齐 (Feed Forward 纵向)

本单元 ILO3 的天道推演 3 层推演树, 在 Day 3 (Agent 经济) 中被复用为"Agent 定价博弈的多智能体沙盘"。alignment.md 的 student_model.json 字段 `blind_spots` 会跨单元传递, 确保 Day 3 知道该学生在"小样本不确定性"或"多层推演"上的弱项, 自动调整 Day 3 的 tutorial 起点脚手架层级。

---

*本文件 v6.0 新增。所有 ILO 均回指 v5.0 既有真实库: statsmodels OLS R²=0.859 / numpy-financial NPV (DeepSeek V3 $5.576M) / scipy.stats 弹性 -0.6169 / 天道推演 10k 蒙特卡洛。*
