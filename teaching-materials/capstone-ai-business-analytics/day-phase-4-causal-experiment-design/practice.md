---
unit: capstone-phase-4
title: 因果实验设计 - 刻意练习 (Deliberate Practice)
version: v6.0
algorithm: Ericsson deliberate practice + MIT pset0 + CS230 progressive project + Worked-Faded
---

# practice.md - Capstone Phase 4 因果实验设计 · 刻意练习

> 本文件遵循 Ericsson 刻意练习原则（拆子技能 + 即时反馈 + 重复到自动化），融合 MIT pset0 先测、CS230 渐进交付、Harvard Worked-Faded 示范-填空-独立解三阶段。所有 drill 反馈规则均**领域特定**，引用 NSW RCT / DoWhy / econml / CUPED / deepeval 真实库与数据。

---

## skill_target

**核心可观察技能**：能在真实 NSW RCT 数据（Dehejia & Wahba 1999）上独立完成 DoWhy 四步因果分析（建模→识别→估计→反驳），用 DML/CUPED/因果森林做异质效应与方差缩减，并用 deepeval 自定义 BaseMetric 评估 Agent 因果证据使用质量，输出可被反驳检验通过的 ATE/CATE 报告。

---

## diagnostic (CS229 pset0 式先测, 探测先验缺口)

> 答题时间 15 分钟。每题选最接近的选项。先测目的不是评分，是定位你的盲点，决定从哪个 drill 起步。

**D1. NSW 数据中 `treat` 与 `re78` 的朴素均值差为什么有偏？**
- (a) 因为样本量不够大
- (b) 因为 `age`/`educ`/`re75` 等协变量在处理组与对照组分布不均，产生混杂偏差
- (c) 因为 1978 年有通胀
- (d) 因为 DoWhy 算法不靠谱

**D2. CUPED 用 `re75` 调整 `re78` 后，方差大约能降低多少？**
- (a) 降低 50%
- (b) 降低 $\rho^2$（Y 与 X_pre 的相关系数平方）
- (c) 完全不变
- (d) 反而增大

**D3. DML 相对线性回归后门调整的核心优势是什么？**
- (a) 速度更快
- (b) 不需要协变量
- (c) 在高维非线性 nuisance functions 下提供 double/debiased 无偏估计
- (d) 可以省略反驳检验

> 评分规则：3/3 全对 → 跳过 Drill A1 直接进 A2；2/3 → 从 A1 起步；≤1/3 → 先重读 notes.md 关键回顾 2-4 再启动。

---

## subskills (3 个子技能拆解)

| Subskill | 描述 | 对应 drill |
|----------|------|-----------|
| **S1 因果识别与估计** | 在 NSW 真实 RCT 上声明 DAG、用后门准则识别、用 DoWhy 估计 ATE 并跑反驳检验 | Drill A1, A2, A3 |
| **S2 方差缩减与异质效应** | 用 CUPED 调整 `re78`、用 econml LinearDML 与因果森林估计 CATE、识别获益最大群体 | Drill B1, B2 |
| **S3 Agent 因果证据评估** | 用 deepeval 自定义 BaseMetric（fallback）评估 Phase 3 Agent 输出中因果证据使用质量 | Drill C1 |

---

## drills (>=3 个, 每个 drill 含 5 字段)

### drill_id: A1
- **difficulty**: 2
- **reps_required**: 3
- **feedback_rule**: 跑 `model.refute_estimate(method_name="random_common_cause")` 必须返回与新估计符号一致、偏差 < 20% 的结果；若符号翻转或偏差 > 20%，反馈指向 DAG 漏声明 `re75`/`educ` 等混杂。用 NSW `data/nsw.csv`，**禁用**模拟数据。
- **worked_faded**:
  - **Worked（完整示范）**：导师演示 `CausalModel(data, treatment="treat", outcome="re78", common_causes=["age","educ","re75"])` → `identify_effect()` → `estimate_effect(method_name="backdoor.linear_regression")` → `refute_estimate(method_name="placebo_treatment_refuter")` 全流程，输出 ATE + p 值。
  - **Faded（部分填空）**：学生填 `common_causes` 列表与 `method_name`，导师已写好反驳调用。
  - **Independent（独立解）**：学生从空 cell 起步，自选混杂集，跑 4 步，提交 ATE + 安慰剂检验 + 随机混杂检验三张图。

### drill_id: A2
- **difficulty**: 3
- **reps_required**: 3
- **feedback_rule**: 朴素 ATE（$\bar Y_{treated} - \bar Y_{control}$）与 DoWhy 后门 ATE 差值应 > 200 美元（NSW 真实混杂存在）；若差值 < 50 美元，反馈检查是否误用了 RCT 子集（NSW 处理组是真随机，但对照组含 observational 补充样本，混杂来自此处）。
- **worked_faded**:
  - **Worked**：演示 `df.groupby("treat")["re78"].mean().diff()` 算朴素 ATE，对比 DoWhy 后门调整 ATE，画出协变量均衡表。
  - **Faded**：学生填均衡表 `pd.crosstab` 与 SMD（标准化均值差）计算，导师已写好 ATE 对比。
  - **Independent**：学生独立产出"朴素 vs PSM vs 后门线性"三 ATE 对比表 + 一段 300 字解释偏差来源。

### drill_id: A3
- **difficulty**: 4
- **reps_required**: 2
- **feedback_rule**: 必须跑 3 种反驳（placebo/random_common_cause/data_subset），任一反驳使估计偏离 > 30% 即判"不稳健"，反馈指向 DAG 隐藏混杂或样本子集偏差；要求学生在 `student_model.json` 写入 `robustness_pass: bool`。
- **worked_faded**:
  - **Worked**：演示完整 3 种反驳的调用与结果判读。
  - **Faded**：学生填 `method_name` 参数与判读阈值。
  - **Independent**：学生自选第 4 种反驳（如 bootstrap），写稳健性报告。

### drill_id: B1
- **difficulty**: 3
- **reps_required**: 3
- **feedback_rule**: CUPED 调整后方差比原始方差降低比例应 > 5%（NSW `re75`-`re78` 相关性约 0.3-0.5）；若降低 < 1%，反馈检查 $\theta = \text{Cov}(Y, X_{pre})/\text{Var}(X_{pre})$ 是否算错或用了 `re74` 而非 `re75`。
- **worked_faded**:
  - **Worked**：演示 `Y_adj = Y - theta * (X_pre - X_pre.mean())` 全代码 + 方差对比 print。
  - **Faded**：学生填 `theta` 计算与 `Y_adj` 公式。
  - **Independent**：学生自选前实验协变量（`re74` 或 `age+educ`），对比哪个方差缩减更优。

### drill_id: B2
- **difficulty**: 5
- **reps_required**: 2
- **feedback_rule**: econml `LinearDML` 与因果森林 CATE 必须在 `nodegree=True` 子群体上符号一致；若符号不一致，反馈指向 `model_t`/`model_y` 没用 RandomForestRegressor 或 `discrete_treatment=True` 未设。CATE 异质性方差比 ATE 大 2-5 倍属正常。
- **worked_faded**:
  - **Worked**：演示 `LinearDML(model_y=RandomForestRegressor(), model_t=RandomForestClassifier(), discrete_treatment=True).fit(X, T, Y)` → `ate_`/`effect_` 全流程。
  - **Faded**：学生填 `effect(X)` 调用与 CATE 排序。
  - **Independent**：学生跑因果森林 `CausalForestDML`，对比 DML 与森林在 `nodegree`/`marr` 子群体的 CATE，写"哪个群体获益最大"。

### drill_id: C1
- **difficulty**: 4
- **reps_required**: 2
- **feedback_rule**: 自定义 `BaseMetric`（deepeval fallback）必须返回 0-1 分数 + 因果证据使用理由（"Agent 引用了 ATE 数值但未提置信区间"等具体反馈）；若返回只有分数无理由，反馈判为"未实现 `measure()` 的 reason 字段"。
- **worked_faded**:
  - **Worked**：演示 `class CausalEvidenceMetric(BaseMetric): def measure(self, ...)` 全实现，含 ATE 引用检测、置信区间检测、反驳检验提及检测。
  - **Faded**：学生填 `reason` 字段构造逻辑。
  - **Independent**：学生用 Phase 3 Agent 输出做 5 条样本评估，写改进建议。

---

## progressive_project (CS230 式渐进交付)

| 阶段 | 交付物 | 字数/代码量 | 占分 |
|------|--------|------------|------|
| **Proposal**（Day 1） | 选定 NSW 子群体或营销映射场景，写因果问题陈述 + DAG 草图 | 300 字 + 1 张 DAG | 10% |
| **Milestone**（Day 3） | TODO1-4 跑通（数据加载 + 朴素估计 + DoWhy 四步 + CUPED） | starter.ipynb 4 格 | 30% |
| **Final**（Day 5） | TODO5-7 跑通（DML + 因果森林 + Agent BaseMetric） | starter.ipynb 全 7 格 | 40% |
| **Poster**（Day 7） | 1 页 poster：ATE/CATE/稳健性/Agent 评估四象限 + 300 字结论 | 1 页 PDF | 20% |

---

## interleaving (A1B1C1...B2C2A2...C3A3B3 交叉排布)

> 不块状练完 A 再练 B。按以下顺序交叉，促进迁移：

```
Day 1: A1(DoWhy四步) → B1(CUPED方差) → C1(Agent BaseMetric 草稿)
Day 2: B1(CUPED 复盘) → A2(朴素 vs 后门) → C1(Agent BaseMetric 测 1 样本)
Day 3: A2(PSM 补) → B2(DML CATE) → A3(反驳检验)
Day 4: B2(因果森林) → C1(Agent 5 样本) → A3(第4种反驳)
Day 5: C3(poster 草稿) → A3(独立) → B2(独立)
```

明文写出：A1B1C1B1A2C1A2B2A3B2C1A3C3A3B2（14 段，每段 30-45 分钟）。

---

## retry_policy (CS230 式)

- **10 free late days**：全 Phase 共享，用完即开始扣分（每天 -5%）
- **失败重试不罚分**：Drill 跑 `verify` 失败可在 24h 内重提交，不扣分；超过 24h 按 late day 算
- **mastery 重试**：Poster 评分 < 80% 可重做 1 次，取两次最高分

---

## weak_loop (连续 2 次失败触发)

若学生在同一 drill 连续 2 次 `verify` 失败：
1. **回退上一 drill**：A2 失败回 A1，B2 失败回 B1，C1 失败回 B2（先理解因果估计再评估 Agent）
2. **补充 Worked Example**：导师播放对应 drill 的 Worked 阶段完整代码 walkthrough
3. **简化 reps**：`reps_required` 临时降为 1，先跑通 1 次再补到 3
4. **`student_model.json` 标记 `weak_drill: <drill_id>`**，触发 schedule.json 该 drill 相关卡片间隔缩短为 [1,2,4,8]

---

## 反馈与 mastery 总览

- **mastery 阈值**：所有 drill 的 Independent 阶段 ≥ 80% + Poster ≥ 80% = Phase 4 通过
- **反馈来源**：DoWhy 反驳检验（自动）+ CUPED 方差数值（自动）+ deepeval BaseMetric（自动）+ 导师对 300 字分析的语义反馈（人工）
- **Worked-Faded 比例**：Drill A1 = 1:1:1，B2 = 1:1:2（Independent 加重，因 CATE 难度高），C1 = 1:2:2
