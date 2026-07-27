---
unit: R6
title: 研究伦理与AI治理 建构对齐 (Biggs ILO ↔ TLA ↔ AT)
version: v6.0
framework: Biggs constructive alignment + mastery threshold
---

# R6 建构对齐 (Constructive Alignment, v6.0)

> 基于 Biggs 建构对齐理论: ILO (Intended Learning Outcome) ↔ TLA (Teaching-Learning Activity) ↔ AT (Assessment Task) 三者必须对齐。所有 TLA 引用本单元 starter/solution/drill/tutorial 真实活动, 所有 AT 引用 solution/tutorial 后测, mastery_threshold >=80%。

---

## ILO ↔ TLA ↔ AT 对齐矩阵 (>=3 行)

| ILO (预期学习产出) | TLA (教学学习活动) | AT (评估任务) | mastery_threshold |
|:------------------|:-------------------|:--------------|:-----------------:|
| **ILO1**: 能解释 Belmont Report (1979) 三原则 (Respect/Beneficence/Justice) 并说明每条在 AI+营销研究中的体现 | ① 读 `notes.md` § 关键回顾 1 表格 + `data/README.md` Belmont Report 原文 6 审查项; ② 做 `practice.md` diagnostic D1 自查; ③ 完成 `tutorial.ipynb` cell2 pre-tutorial essay (用英文写三原则配对); ④ `practice.md` drill-1 阶段1 Worked (对照 `solution.ipynb` TODO1 完整 schema) | ① `solution.ipynb` TODO1 自动评分 (pydantic schema 字段完整=80%); ② `tutorial.ipynb` cell5 Hattie [TASK] 反馈: 三原则英文术语写对; ③ `practice.md` drill-1 阶段3 Independent 新增第 7 审查项 "data_deidentification" (正确扩展 schema=100%) | >=80% |
| **ILO2**: 能用 pydantic 定义 IRB 伦理审查清单 schema (3原则6审查项) 并实现评分器, 输出合规状态与风险等级 | ① 读 `notes.md` § 上机任务 TODO1/TODO3; ② `starter.ipynb` TODO1+TODO3 填空 (assess_checklist_item + score_to_status + irb_ethics_review); ③ `practice.md` drill-1 三阶段 Worked->Faded->Independent; ④ `tutorial.ipynb` cell3 Socratic loop 第 2 轮追问 score_to_status 阈值边界 | ① `solution.ipynb` TODO3 单元测试: 8 案例 score 与 status 全对 (compliant>=80, conditional 60-79, non_compliant<60); ② `practice.md` drill-1 feedback_rule 命中 (weakest_principle 与 pandas 热力图短板一致) | >=80% |
| **ILO3**: 能从研究伦理视角映射 NIST AI RMF 四步循环, 并区别于技能2 Day1 企业治理视角 | ① 读 `notes.md` § 关键回顾 2 双视角对比表; ② `practice.md` drill-2 阶段1 Worked (AI个性化推荐示范) + diagnostic D2; ③ `tutorial.ipynb` cell3 Socratic loop 第 3 轮反例追问 ("如果用企业视角会怎样?"); ④ `practice.md` interleaving B1/B2/B3 交叉练习 | ① `solution.ipynb` TODO4 NIST 映射正确 (Govern=IRB审批, 非企业治理委员会); ② `practice.md` drill-2 阶段3 Independent 三元组 `(belmont_score, nist_step=研究视角, eu_risk_level)` 全对; ③ `tutorial.ipynb` cell4 student_model.json 记录 "nist_step_confusion" 盲点消除 | >=80% |
| **ILO4**: 能用 EU AI Act 真实条款 (Article 5/Annex III/Article 50) 判定 AI 研究案例风险等级 | ① 读 `notes.md` § 关键回顾 3 风险分级表; ② `practice.md` drill-2 阶段2 Faded (AI自动文案A/B测试) + diagnostic D3; ③ `data/README.md` EU AI Act 链接深读; ④ `tutorial.ipynb` cell3 Socratic loop 第 4 轮 "凭什么" 追问条款号 | ① `solution.ipynb` TODO4 EU AI Act 判定 8 案例全对 (含动态定价=Article 5 禁止); ② `practice.md` drill-2 阶段3 Independent 动态定价案例解释为何落入 Article 5; ③ `tutorial.ipynb` cell5 [FEED-FORWARD] 推荐复习 R6 + 模块S (合规) | >=80% |
| **ILO5**: 能用 garak/PyRIT 红队概念 + 天道推演 3 层树预判 AI 研究伦理风险路径, 识别高杠杆点 | ① 读 `notes.md` § 2026 前沿 (红队伦理验证 + 天道推演预判); ② `practice.md` drill-3 三阶段 Worked (动态定价示范) -> Faded -> Independent; ③ `starter.ipynb` TODO6 红队+天道推演填空; ④ `tutorial.ipynb` cell3 Socratic loop 第 5 轮 "如何" 追问高杠杆点可执行性 | ① `solution.ipynb` TODO6 输出含 probe 列表 (>=2 个, dan/promptinject/goodside) + 3 层树 (immediate/near/far 因果相连, far 含罚款/禁令/声誉) + 高杠杆点 (>=1); ② `practice.md` drill-3 阶段3 Independent 独立完成 AI 个性化推荐案例 (有知情同意 -> far 层因果链被截断); ③ progressive_project final 阶段提交完整 IRB 报告 | >=80% |

---

## 3 自检问题 (Feed Up / Feed Back / Feed Forward)

### Q1: Feed Up -- TLA 是否训练 ILO?

逐行检查: 每个 ILO 是否都有 >=1 个 TLA 直接训练该产出?

- ILO1 (Belmont 三原则): TLA 含 `notes.md` 表格 + diagnostic D1 + tutorial essay + drill-1 Worked -> **是, 4 个 TLA 直接训练**
- ILO2 (pydantic schema + 评分器): TLA 含 `starter.ipynb` TODO1/TODO3 填空 + drill-1 三阶段 + Socratic 追问 -> **是, 3 个 TLA 直接训练**
- ILO3 (NIST 研究伦理视角): TLA 含双视角对比表 + drill-2 Worked + Socratic 反例 + interleaving B1/B2/B3 -> **是, 4 个 TLA 直接训练**
- ILO4 (EU AI Act 条款): TLA 含风险分级表 + drill-2 Faded + 深读 + Socratic "凭什么" -> **是, 4 个 TLA 直接训练**
- ILO5 (红队+天道推演): TLA 含 2026 前沿节 + drill-3 三阶段 + TODO6 + Socratic "如何" -> **是, 4 个 TLA 直接训练**

**结论**: 全部 ILO 有 TLA 训练, Feed Up 对齐通过。

### Q2: Feed Back -- AT 是否测量 ILO?

逐行检查: 每个 ILO 是否都有 >=1 个 AT 直接测量该产出?

- ILO1: AT=`solution.ipynb` TODO1 (schema 字段完整) + tutorial [TASK] + drill-1 Independent -> **是**
- ILO2: AT=`solution.ipynb` TODO3 (8 案例评分) + drill-1 feedback_rule (weakest_principle 一致) -> **是**
- ILO3: AT=`solution.ipynb` TODO4 (NIST 研究视角, 非企业) + drill-2 Independent 三元组 + student_model 盲点消除 -> **是**
- ILO4: AT=`solution.ipynb` TODO4 (8 案例 EU 判定) + drill-2 Independent (动态定价 Article 5 解释) -> **是**
- ILO5: AT=`solution.ipynb` TODO6 (probe+3层树+高杠杆点) + drill-3 Independent (AI 个性化推荐) + progressive_project final -> **是**

**结论**: 全部 ILO 有 AT 测量, Feed Back 对齐通过。

### Q3: Feed Forward -- 不经 TLA 能过 AT 吗? 若能 = 对齐失败

逐行检查: 是否存在"跳过 TLA 也能过 AT"的捷径?

- ILO1: 跳过 Belmont 表格 + diagnostic, 能直接写出 pydantic 三原则 schema 吗? 不能 -- schema 字段名 (Respect/Beneficence/Justice) 必须来自 TLA 的 `notes.md`/`data/README.md` 原文 -> **对齐成功**
- ILO2: 跳过 `starter.ipynb` 填空 + drill-1 三阶段, 能直接过 `solution.ipynb` TODO3 测试吗? 不能 -- 8 案例评分阈值 (80/60) 与 weakest_principle argmin 逻辑必须通过 drill-1 反复修正 -> **对齐成功**
- ILO3: 跳过双视角对比表 + drill-2, 能直接过 NIST 研究视角判定吗? **风险点**: 学生可能背"Govern=IRB审批"通过 AT, 但不理解与企业视角区别 -> **缓解**: tutorial Socratic 第 3 轮反例追问 + drill-2 Independent 必须输出三元组 (强制三视角交叉) -> **对齐成功 (有缓解)**
- ILO4: 跳过风险分级表 + drill-2, 能直接判 Article 5 吗? **风险点**: 学生可能记"动态定价=禁止"通过 AT, 但说不出条款号 -> **缓解**: drill-2 feedback_rule 强制带条款号 + Socratic "凭什么" 追问 -> **对齐成功 (有缓解)**
- ILO5: 跳过 2026 前沿 + drill-3, 能直接写 3 层树吗? 不能 -- 3 层因果相连 + far 含罚款/禁令/声誉 + 高杠杆点可执行性, 必须通过 drill-3 Worked->Faded->Independent 三阶段训练 -> **对齐成功**

**结论**: 无"不经 TLA 可过 AT"的捷径, Feed Forward 对齐通过 (ILO3/ILO4 有缓解措施)。

---

## mastery_threshold 总览

| 维度 | 阈值 | 验证方式 |
|:----:|:----:|:--------|
| 单 ILO | >=80% | 该 ILO 所有 AT 全部 >=80% |
| 单 drill | >=80% | feedback_rule 全部命中 |
| 单元总评 | 5 ILO 全部 >=80% + diagnostic 自查全对 | `verify_unit.py` 7/7 + `verify_v6_unit.py` 5/5 |
| progressive_project 各阶段 | >=80% | proposal/milestone/final/poster 各阶段评分 |

---

*本 alignment.md 基于 Biggs 建构对齐理论 (ILO ↔ TLA ↔ AT) + Feed Up/Feed Back/Feed Forward 三自检 + mastery threshold。所有 TLA/AT 引用本单元真实文件 (notes/starter/solution/practice/tutorial/data/README)。*
