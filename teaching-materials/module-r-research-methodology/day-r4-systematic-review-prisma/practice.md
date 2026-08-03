---
unit: R4
title: 系统综述 PRISMA 2020 方法论 - 刻意练习
version: v6.0
algorithm: Ericsson deliberate practice + MIT CS229 diagnostic + CS230 progressive project + Stanford interleaving
---

# practice.md - R4 系统综述 PRISMA 刻意练习

> 质量契约：CQ-R4-1（protocol、双人独立筛选、偏倚/证据确定性、自动化披露）。

## skill_target

能用 `arxiv` + `pandas` + `scikit-learn` + `matplotlib` 独立实现 PRISMA 2020 四阶段方法论流程（Identification → Screening → Quality Assessment → Synthesis），产出符合 27 条 checklist 的 PRISMA flow diagram + Cohen's kappa 评分者一致性报告 + Kitchenham 五维质量评分 + ASReview 主动学习效率曲线，且能在 90 分钟内对一份全新 arXiv 检索结果（>=80 篇）跑通全流程并解释每一阶段的排除比例与偏倚来源。

## diagnostic (CS229 pset0 式先测, 探测先验缺口)

> 不查阅资料，15 分钟内作答。每题先写"我有把握 / 我猜的 / 不会"，再写答案。检测点决定从哪个 drill 起步。

**D1**：给定两位筛选者对 100 篇文献的标签（A: 60 篇纳入, B: 70 篇纳入, 两人都纳入 50 篇），手工计算 Cohen's kappa。若 kappa = 0.55，按 Landis-Koch 表对应哪个等级？PRISMA 2020 Item 8 要求说明选择过程、独立筛选者与自动化工具；kappa 在这里为该过程提供什么补充审计信号？

**D2**：Kitchenham & Charters (2007) 五维质量评估中，"方法适当性"与"分析恰当性"如何区分？一篇用 case study 方法回答"LLM 对营销转化率因果效应"研究问题的论文，在"方法适当性"维应打 0 还是 1？为什么？

**D3**：ASReview 主动学习停止规则"连续 N 篇均为负例即停"会在什么文献分布下产生**假停止**（premature stop）？若种子集只有 3 篇正例且偏向某一子主题，TF-IDF + LogisticRegression 排序会系统性漏掉哪类相关论文？用什么策略缓解？

> 评分：3 题全对 → 从 Drill 2 起步；D1 错 → 从 Drill 1 起步；D2/D3 错 → 从 Drill 1 起步并补做 worked example。

## subskills

- **S1 - PRISMA Phase 1+2 检索筛选链**：arxiv 多查询检索 + pandas 去重 + 双盲筛选 + scikit-learn Cohen's kappa 计算 + Landis-Koch 等级判定
- **S2 - PRISMA Phase 3 质量评估与偏倚分级**：Kitchenham 五维评分函数实现 + Risk of Bias 三级分级（Low ≥4 / Moderate 2-3 / High 0-1）+ 偏倚来源归因
- **S3 - PRISMA Phase 4 主动学习综合**：ASReview 机制模拟（种子集 → TF-IDF + LogisticRegression → 迭代查询 → 效率曲线）+ RAGAS evidence synthesis 质量评估

## drills

### drill_id: D1
**target subskill**: S1
**difficulty**: 2
**reps_required**: 3
**feedback_rule**: 用 `arxiv.Search("AI marketing")` 真实查询 → 学生用 `pandas.drop_duplicates(subset='title')` 去重 → 对照 `data/README.md` 的 fallback JSON 检查去重前后数量差。若去重后数量与 fallback 不符，反馈指向"标题大小写/空白未规范化"。Cohen's kappa 必须用 `sklearn.metrics.cohen_kappa_score`，禁止手算。
**worked_faded**:
- 阶段1 完整示范：solution.ipynb TODO1-2 的完整代码 + 注释每一行（arxiv.Search 查询构造 → DataFrame 转换 → drop_duplicates → 数量记录）
- 阶段2 部分填空：starter.ipynb TODO1-2 给出 arxiv.Search 调用骨架，学生填 query 列表 + drop_duplicates 参数 + 数量记录变量
- 阶段3 独立解：给一份新的查询主题（"LLM advertising"），学生独立完成检索→去重→数量报告

### drill_id: D2
**target subskill**: S2
**difficulty**: 3
**reps_required**: 4
**feedback_rule**: 学生实现 `kitchenham_score(paper)` 函数 → 对 `data/` 中至少 10 篇论文打 0-5 分 → 用 `pandas.cut` 分箱为 Low/Moderate/High RoB。反馈规则：若学生把"方法适当性"与"分析恰当性"混淆（如把 case study 回答因果问题判为方法适当），引用 Kitchenham 原文第 5 维定义纠正。RoB 分级边界必须 `>=4 / 2-3 / 0-1`，不允许 `>3` 这种模糊边界。
**worked_faded**:
- 阶段1 完整示范：对 2 篇论文（1 篇 RCT 高质量 + 1 篇 case study 低质量）逐维打分 + RoB 分级，写出每一维的判断依据
- 阶段2 部分填空：给 5 篇论文 + 评分函数骨架（五维变量名已给），学生填判断逻辑 + RoB 分箱条件
- 阶段3 独立解：学生对 `data/` 中 10 篇论文独立打分 + 分级，产出质量评分表

### drill_id: D3
**target subskill**: S3
**difficulty**: 4
**reps_required**: 5
**feedback_rule**: 学生模拟 ASReview 主动学习（种子集 5 篇正例 + 5 篇负例 → `TfidfVectorizer` + `LogisticRegression` → 迭代查询 Top-10 → 重新训练）。反馈规则：若学生未设随机种子（`random_state=42`），导致两次运行效率曲线不一致，引用 PRISMA 2020 Item 7 "可重复性"要求纠正。效率提升必须对比"人工全筛基线"（读 100% 才覆盖 90% 相关），而非只报 ASReview 的绝对数。
**worked_faded**:
- 阶段1 完整示范：solution.ipynb TODO5 的完整 ASReview 模拟代码 + 效率曲线图 + 与人工基线对比
- 阶段2 部分填空：starter.ipynb TODO5 给出 TfidfVectorizer + LogisticRegression 调用骨架，学生填种子集标注 + 迭代查询循环 + 效率计算
- 阶段3 独立解：学生换一个主题（"LLM advertising"）独立跑 ASReview 模拟，产出"读前 N 篇覆盖 90% 相关"曲线

### drill_id: D4
**target subskill**: S1+S2+S3 串联
**difficulty**: 5
**reps_required**: 2
**feedback_rule**: 学生从 `data/` 起步，90 分钟内独立产出 PRISMA 2020 flow diagram（matplotlib）+ Cohen's kappa 报告 + Kitchenham 质量表 + ASReview 效率曲线。反馈规则：flow diagram 必须包含 27 条 checklist 中 Item 16a-17 要求的"识别/筛选/纳入各阶段真实数字"，缺一阶段即退回重做。kappa 报告必须含 Landis-Koch 等级判定，不能只给数值。
**worked_faded**:
- 阶段1 完整示范：solution.ipynb TODO6 的完整 PRISMA flow diagram 代码 + 四阶段数字标注
- 阶段2 部分填空：给 matplotlib 框架代码（box 位置已定），学生填各阶段数字 + 箭头 + 排除理由标注
- 阶段3 独立解：学生对全新 arXiv 检索结果独立产出完整 PRISMA flow diagram + 三份报告

## progressive_project (CS230 式渐进交付)

- **proposal (Day 3)**：提交 1 页 PRISMA 综述提案 + `protocol.md` 摘要——研究问题 + 6 条 arXiv 查询式 + 纳排标准 + 双人独立筛选计划 + 预期种子集大小 + 预期 kappa 范围。导师否决"研究问题过宽/查询式无同义词/未声明 protocol amendment 规则"三类问题。
- **milestone (Day 7)**：完成 Phase 1+2——提交去重后的 DataFrame + 双人独立筛选结果或教学模拟披露 + Cohen's kappa 值 + Landis-Koch 等级 + 冲突裁决记录。kappa < 0.41 触发"筛选者培训"补充 drill。
- **final (Day 14)**：完成全四阶段——PRISMA flow diagram + Kitchenham/RoB proxy 质量表 + 报告偏倚与证据确定性表 + ASReview 效率曲线 + 300 字方法论反思（哪个阶段排除比例最高？为什么？自动化工具带来什么偏倚？）。
- **poster (Day 17)**：1 页 A3 poster 展示 PRISMA 流程图 + 核心数字 + 方法论学习点，用于模块 R 跨单元 gallery walk。

## interleaving (交叉排布, 不块状)

> 不按 D1→D2→D3→D4 块状刷，按下列交叉顺序练习，促进迁移：

```
A1(S1 基础) → B1(S2 基础) → C1(S3 基础) →
A2(S1 进阶) → B2(S2 进阶) → C2(S3 进阶) →
C3(S3 串联) → A3(S1 串联) → B3(S2 串联) →
D4(全串联)
```

明文交叉顺序：
- 第1轮：D1 阶段1 → D2 阶段1 → D3 阶段1（三子技能 worked example 各看一遍）
- 第2轮：D1 阶段2 → D2 阶段2 → D3 阶段2（三子技能部分填空交叉）
- 第3轮：D3 阶段3 → D1 阶段3 → D2 阶段3（独立解，顺序倒置强化提取）
- 第4轮：D4 全串联（合练）

## retry_policy (CS230 式)

- 每位学生有 **10 free late days**（可分配给任意 drill / project 阶段，不罚分）
- Drill 失败可**无限重试不罚分**，但每次重试必须附 50 字"上次错在哪"反思
- progressive_project 的 milestone 若 kappa < 0.41，触发弱项循环后可重交，不扣 late day

## weak_loop (连续 2 次失败触发)

> 触发条件：同一 drill 连续 2 次未达 reps_required 的反馈标准。

触发后：
1. **回退上一 drill**：D2 失败 → 回退 D1 重做阶段2；D3 失败 → 回退 D2 重做阶段2
2. **补充 worked example**：重看 solution.ipynb 对应 TODO 的完整代码 + 导师 5 分钟口述讲解
3. **诊断盲点**：用 `tutorial.ipynb` 的 Socratic loop 针对失败点追问 3 轮，更新 `student_model.json` 的 `blind_spots` 字段
4. **重新进入**：补做 1 次后重新进入原 drill，从阶段2 起步（不重做阶段1）

典型弱项循环场景：
- kappa 计算错 → 回退 D1 → 补 worked example（`cohen_kappa_score` 调用）→ 重做 D2 阶段2
- RoB 分级边界错 → 回退 D2 → 补 worked example（`pandas.cut` 分箱）→ 重做 D2 阶段3
- ASReview 效率曲线无基线对比 → 回退 D2 → 补 worked example（人工全筛基线构造）→ 重做 D3 阶段3

---

*practice.md 由 v6.0 学习科学层生成。领域特定反馈规则引用 arxiv/pandas/scikit-learn/matplotlib + Kitchenham/Cohen/ASReview 真实概念，非通用模板。*
