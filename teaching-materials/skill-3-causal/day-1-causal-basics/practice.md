# Day 1 因果推断基础 · 刻意练习 (v6.0 学习科学层)

> 配套 v5.0 notes.md / starter.ipynb / solution.ipynb，以 Ericsson 刻意练习五要素 + MIT 6.5940 渐退示例 + 交叉 interleaving 设计。

---

## skill_target (可观察核心技能)

给定一个营销/政策场景的真实观测数据集（含处理 T、结果 Y、协变量 X），能独立完成"画 DAG → 定义 estimand → 明示识别假设 → 识别后门路径 → 诊断 positivity/overlap → 用 DoWhy 做后门调整估计 → 用负对照、refuter 与 LLM-as-a-judge 审查论证"全流程，并解释朴素均值差与调整估计的差异来源。质量契约：CQ-S3-1。

## subskills

- **S1 画 DAG & 识别后门路径**：在 NSW/营销场景中正确标注处理/结果/混杂，列出所有后门路径并指出在哪个节点切断
- **S2 DoWhy 四步落地**：`modeling → identification → estimation → refutation`，正确声明 `common_causes`，调用 `backdoor` 识别，估计 ATE，并至少跑 `placebo_treatment_refuter` / `random_common_cause_refuter` / `data_subset_refuter` 三类 refuter 或敏感性分析中的两类
- **S3 论证审查 (LLM-as-judge + 反驳)**：用 LLM-as-a-judge 检查 DAG 完备性 / 识别策略 / 反驳充分性 / 结论是否过度外推，并解释它处于因果阶梯 L1（不能升 L2/L3）

---

## diagnostic (前测，pset0 式)

开课先测，定位起点。三题，每题 5 分钟，不计分但必答：

1. **DAG 题**：给定"用户活跃度 → 广告曝光 → 点击 → 转化"+"用户活跃度 → 历史购买 → 转化"，画出 DAG 并写出从 `广告曝光` 到 `转化` 的所有后门路径。
2. **概念题**：用一句话解释"为什么随机化能消除偏差，而观测数据不能"。再用 Pearl 阶梯说明 A/B 测试落在哪一层。
3. **代码题**：给定 `causaldata.nsw` 已加载为 `df`，写出"朴素 ATE 估计"的两行代码（处理组 `re78` 均值 - 对照组 `re78` 均值），并预测它比真实 ATE 偏高还是偏低，为什么。

> 评分规则：三题全对 = 直接进 D3；2 对 = 进 D2；≤1 对 = 从 D1 开始。这是 mastery-based 自定步调（SELENE 思路）。

---

## drills (>=3, 含 difficulty/reps_required/feedback_rule/worked-faded 三阶段)

### drill_id: D1
- **目标子技能**：S1 画 DAG & 识别后门路径
- **difficulty**: 2 (1-5 量表)
- **reps_required**: 3
- **feedback_rule**:
  - 若漏画后门路径 → 提示"从 T 指向 Y 的箭头之外，所有 T 的父节点中哪些同时指向 Y？逐条追踪"
  - 若误把中介变量当混杂（如把"点击"当混杂去控制）→ 提示"中介变量在 T→Y 的因果路径上，控制它会切断真实因果链，这叫 over-control bias；混杂必须同时是 T 和 Y 的共同原因"
  - 若切断节点选错（如切断 Y 的子节点）→ 提示"后门准则要求在混杂节点切断，不是在 Y 的下游切断；回到 NSW 案例，重新看 `用户活跃度` 的位置"
- **worked_faded 三阶段**:
  - **阶段 1 (Worked 完整示范)**：完整演示 NSW+CPS 观测比较场景 DAG——`age/educ/black/hisp/marr/nodegree/re74/re75` 共同指向 `treat` 与 `re78`，写出后门路径 `treat ← age → re78` 等 8 条，演示在协变量集合 `{age, educ, re74, re75, ...}` 上切断
  - **阶段 2 (Faded 部分填空)**：给出营销场景 DAG 框架，但留 3 处空白——"___ 是处理变量"、"___ 是混杂"、"应在 ___ 节点切断"，学生填空
  - **阶段 3 (独立解)**：给一个全新场景（邮件营销：`历史打开率 → 收到推送 → 点击 → 转化`，`历史打开率 → 会员等级 → 转化`），独立画 DAG + 写出全部后门路径 + 指出切断节点

### drill_id: D2
- **目标子技能**：S2 DoWhy 四步落地
- **difficulty**: 3 (1-5 量表)
- **reps_required**: 3
- **feedback_rule**:
  - 若 `common_causes` 声明遗漏关键混杂 → 提示"回看 D1 的 DAG，所有指向 T 且指向 Y 的节点都必须进 `common_causes`；NSW 案例中至少 8 个协变量"
  - 若识别阶段选错方法（如对有未观测混杂的图选 `backdoor`）→ 提示"后门准则要求所有后门路径上的混杂都可观测；检查你的 DAG 是否有双向虚线或未观测节点"
  - 若跳过 `refutation` → 提示"估计出来的 ATE 没有 refuter 验证就等于没交作业；CQ-S3-1 要求至少跑 placebo_treatment_refuter / random_common_cause_refuter / data_subset_refuter 三类中的两类，并解释负对照或未观测混杂敏感性"
- **worked_faded 三阶段**:
  - **阶段 1 (Worked)**：完整跑一遍 NSW——先写 estimand `ATE=E[Y(1)-Y(0)]` 与识别假设（consistency / exchangeability / positivity / SUTVA），再执行 `CausalModel(data, treatment="treat", outcome="re78", common_causes=[...8个])` → `identify_effect(estimator_type="backdoor")` → `estimate_effect()` → `refute_estimate(refuter="placebo_treatment_refuter")` → `refute_estimate(refuter="random_common_cause_refuter")`，每行注释意图
  - **阶段 2 (Faded)**：给出框架代码但留 4 个 TODO——`common_causes=[___]`、`identified_estimand = model.___()`、`estimate = identified_estimand.___()`、`ref = estimate.___()`，学生填方法名
  - **阶段 3 (独立解)**：换数据集（`causaldata.lalonde` 或 `causaldata.marginal_tax`），独立从零写四步，并解释 `placebo_treatment_refuter` 返回的 `new_effect` 接近 0、`random_common_cause_refuter` 不改变主估计、`data_subset_refuter` 方向稳定分别意味着什么

### drill_id: D3
- **目标子技能**：S3 论证审查 (LLM-as-a-judge + 反驳)
- **difficulty**: 4 (1-5 量表)
- **reps_required**: 3
- **feedback_rule**:
  - 若把 LLM-as-a-judge 当成"因果效应估计器" → 提示"LLM-as-a-judge 处于因果阶梯 L1（对论证文本的关联分析），不能升 L2/L3；它审的是论证质量，不是估计 ATE"
  - 若 LLM-as-judge 的 prompt 缺失结构化检查项 → 提示"参考 NeurIPS 2023 LLM-as-a-judge 范式，prompt 必须包含 4 个检查维度：(a) DAG 是否遗漏混杂 (b) 识别策略是否满足后门准则 (c) 反驳是否充分 (d) 结论是否过度外推"
  - 若不记录 LLM 指出的盲点 → 提示"LLM-as-judge 的价值是暴露你没想到的潜在混杂；必须把它的指摘写进 `student_model.json` 的 `blind_spots` 字段，跨单元复用"
- **worked_faded 三阶段**:
  - **阶段 1 (Worked)**：完整示范——把 D2 的 DoWhy 结果（DAG + identified_estimand + estimate + refute）整理成结构化文本，喂给 LLM（静态模拟响应），记录其指出的 1 个未考虑混杂（如"NSW/CPS 中 `nodegree` 与 `educ` 高度相关，可能存在共线性"），写进 `student_model.json`
  - **阶段 2 (Faded)**：给 LLM prompt 模板留 2 处空白——"检查 DAG 是否遗漏 ___" 和 "结论是否 ___"，学生补全；再给 LLM 响应留 1 处空白让学生预测 LLM 会指出什么
  - **阶段 3 (独立解)**：把 D2 独立解的结果喂给 LLM-as-judge（可用静态模拟分支占位），独立判断其反馈是否合理（魔鬼代言人视角：LLM 是否在胡说？），把盲点写进 `student_model.json`

---

## progressive_project (proposal → milestone → final → poster, CS230 式脚手架)

本 Day 的项目是 `starter.ipynb` 的延伸，分四阶段交付：

- **P1 Proposal (Day 1 上午交)**：选一个营销/政策场景（不限 NSW），写 200 字提案——研究问题、处理 T、结果 Y、候选混杂 X、数据来源。不评分但必须交，否则后续不收。
- **P2 Milestone (Day 1 下午交)**：交付完整 DAG（手绘或代码）+ NSW 实验基准 + NSW处理组/CPS对照的观测朴素估计 + 一段话解释样本选择。反馈给“是否混淆实验与观测对照、是否漏后门路径”的建议。
- **P3 Final (Day 1 + 2 天)**：交付完整 `starter.ipynb`——DoWhy 四步全跑通 + estimand 与识别假设段落 + overlap/positivity 诊断 + ≥2 个 refuter 或敏感性分析 + 负对照设计 + LLM-as-judge 审查记录 + `student_model.json` 更新。
- **P4 Poster (Day 2 课前)**：1 页 PDF poster——DAG 图 + 三种估计对比表（朴素/后门调整/PSM）+ 1 个 LLM-as-judge 指出的盲点。用于同伴互评（CS229 Ed Discussion 模式）。

late policy: 借鉴 CS230，每单元 2 late days 免费，之后每天 -20%；超过 4 天不收。

---

## interleaving (A1B1C1...B2C2A2...C3A3B3 明文交叉，禁止块状)

不要按 D1→D2→D3 块状刷题。按以下交叉序列练习（A=DAG 画图, B=DoWhy 代码, C=LLM-as-judge 审查）：

```
Round 1: A1 → B1 → C1     (三个子技能各 1 次，浅层交叉)
Round 2: B2 → C2 → A2     (轮换起始，避免 A 总先做)
Round 3: C3 → A3 → B3     (再次轮换，C 起步)
Round 4 (巩固): A4 → C4 → B4 → A5 → B5 → C5
```

明文：每轮三个子技能都要碰到，顺序轮换。MIT 6.5940 实证——交叉练习比块状长期保留高 38%。每次 drill 从上一轮的 `student_model.json` 盲点出发，针对性选题。

---

## retry_policy

- 单次 drill 未达 mastery（80% 正确）→ 隔 1 小时重试（不是立刻，触发间隔重复效应）
- 连续 2 次失败 → 触发 weak_loop（见下）
- 累计 4 次仍失败 → 退出 drill，回到 notes.md 重读"关键回顾 2/3"，并预约 tutorial（见 tutorial.ipynb）

## weak_loop (连续 2 次失败触发)

当学生在同一 drill 连续 2 次未达 mastery：

1. **回退一级**：D3 失败 → 退到 D2；D2 失败 → 退到 D1；D1 失败 → 回到 notes.md "关键回顾"段
2. **补 Worked Example**：在回退后的 drill 重新跑阶段 1（Worked 完整示范），不要直接进 Faded
3. **写一句话诊断**：在 `student_model.json` 的 `weak_loop_log` 追加——"YYYY-MM-DD D3 失败 2 次，退回 D2 阶段 1，原因是 ___"
4. **24h 后重试**：不是立刻重试 D3，而是隔天（让间隔重复生效），从 D2 阶段 3 重新爬坡

weak_loop 是安全网不是惩罚——目的不是让学生羞耻，而是把"卡住"转化为"明确知道卡在哪"。

---

## 与 schedule.json / alignment.md / tutorial.ipynb 的衔接

- 本文件的 drill 完成情况 → 写入 `student_model.json`（tutorial.ipynb 读写）
- 间隔重复卡片 → 见 `schedule.json`（FSRS-6, 1/3/8/21/60/180 天）
- ILO ↔ TLA ↔ AT 对齐 → 见 `alignment.md`
- 卡在 D2/D3 超过 2 次 → 预约 `tutorial.ipynb` 的 Socratic 仿真（限频 1 次/天）

---

## CQ-S3-1 可判分 rubric

| 维度 | 权重 | 通过标准 | 常见扣分 |
|---|---:|---|---|
| estimand 与识别假设 | 20% | 明确定义 ATE、T、Y、X；逐条说明一致性（consistency）、可交换性（exchangeability）、正值性（positivity）/ overlap、SUTVA | 只给 DoWhy 代码；没说明“无未观测混杂”只是不可检验假设 |
| DAG 与后门路径 | 20% | 正确列出至少 5 条 NSW 后门路径；说明控制哪些变量、为什么不控制中介或碰撞变量 | 把点击/购买路径上的中介当混杂控制；漏掉 `re74/re75` |
| 数据与估计诊断 | 20% | 报告样本量、协变量 SMD、倾向得分 overlap、朴素 ATE、后门 ATE、PSM 或替代估计 | 只报告均值差；没有共同支撑检查；把单一估计量当真值 |
| refuter / 敏感性 / 负对照 | 25% | 至少完成 placebo、random common cause、data subset/bootstrap 三类中的两类；提出 1 个负对照；写出未观测混杂敏感性判断 | 只跑 placebo；把 refuter 通过解释为“因果已证明”；没有负对照 |
| 表达与迁移 | 15% | 300 字因果结论包含限制条件、营销映射、不可外推边界；能说明 LLM-as-a-judge 只审论证质量 | 过度外推到所有营销场景；让 LLM 直接估 ATE |

通过阈值：总分 ≥80 且 refuter / 敏感性 / 负对照维度不得低于 15/25；否则即使 notebook 跑通也不算 CQ-S3-1 达标。

---

*v6.0 学习科学层 · Ericsson 刻意练习 + MIT 6.5940 渐退示例 + 交叉 interleaving + CS230 渐进项目 + CS229 诊断前测*
