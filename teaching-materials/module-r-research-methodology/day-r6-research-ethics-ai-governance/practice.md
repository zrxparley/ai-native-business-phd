---
unit: R6
title: 研究伦理与AI治理 刻意练习
skill_target: 用 Belmont Report 三原则 + NIST AI RMF 四步循环 + garak/PyRIT 红队概念, 对真实 AI 研究案例实施 IRB 式伦理审查评分 (0-100) 并输出合规状态与天道推演风险路径
version: v6.0
frameworks: [Ericsson_deliberate_practice, MIT_CS229_pset0, CS230_progressive, Harvard_Worked-Faded, Stanford_interleaving]
---

# R6 刻意练习 (Deliberate Practice, v6.0)

> 基于 Ericsson 刻意练习理论 + MIT CS229 pset0 先测 + CS230 渐进交付 + Harvard Worked-Faded 三阶段 + Stanford 交叉练习。所有 drill 反馈规则**领域特定**: 引用 Belmont Report / NIST AI RMF / EU AI Act / garak / PyRIT / pydantic / OECD AI Incidents Monitor。

---

## diagnostic (CS229 pset0 式先测, 探测先验缺口)

> 开练前 8 分钟做完。不评分, 只定位盲点。每题选完后自查答案 (后附)。

- **D1**: Belmont Report (1979) 三原则英文与中文配对。下列哪一项**不属于** Belmont 三原则?
  - (a) Respect for Persons / 尊重个人
  - (b) Beneficence / 善行
  - (c) Autonomy / 自主权
  - (d) Justice / 公平正义
  - **目标盲点**: 学生常把"自主权"误当作独立原则 (实为 Respect for Persons 的子要求)

- **D2**: NIST AI RMF 四步循环 (Govern/Map/Measure/Manage) 中, "IRB 审批 + 伦理委员会监督 + 研究者问责"对应哪一步? 它与技能2 Day1 的企业治理视角有何区别?
  - **目标盲点**: 混淆"研究伦理视角"与"企业治理视角" (前者聚焦人类参与者保护, 后者聚焦组织合规流程)

- **D3**: 给定一个 AI 动态定价研究案例 (涉及敏感数据 + 无知情同意 + 弱势群体), 用 EU AI Act 判定风险等级, 并说出对应条款号 (Article 5 / Annex III / Article 50 / 其他)。
  - **目标盲点**: 把"高风险"与"禁止"混淆; 忘了 Article 5 是禁止性条款, 动态定价剥削弱势群体常落入 Article 5。

**自查答案**: D1 -> (c); D2 -> Govern (研究视角=IRB审批/伦理委员会/研究者问责; 企业视角=AI治理委员会/使用政策/问责机制, 区别在保护对象); D3 -> 禁止 (Article 5, 操控性营销/弱势群体剥削性广告)。

---

## subskills (3 个子技能, 拆解 skill_target)

- **S1 Belmont schema 化**: 用 pydantic 把 Belmont 三原则 6 审查项定义为可序列化的伦理审查清单 schema, 并实现 `assess_checklist_item` + `score_to_status` + `irb_ethics_review` 三个函数。
- **S2 多框架风险映射**: 对同一 AI 研究案例并行执行 Belmont 评分 + NIST AI RMF 研究伦理映射 + EU AI Act 合规判定, 三视角交叉印证。
- **S3 红队 + 天道推演验证**: 用 garak/PyRIT 概念设计红队 probe 集 (dan/promptinject/goodside), 用天道推演 3 层树 (immediate -> near -> far) 预判伦理风险路径, 识别高杠杆点。

---

## drills (>=3, 每个 Worked-Faded 三阶段)

### drill-1: Belmont pydantic schema + IRB 评分器 (子技能 S1)

- **drill_id**: D1-BELMONT-SCHEMA
- **difficulty**: 2
- **reps_required**: 3
- **feedback_rule**: 运行 `irb_ethics_review(case)` 必须返回 `{score: 0-100, status: compliant/conditional/non_compliant, risk_level: low/medium/high, weakest_principle: respect|beneficence|justice}`。若 `weakest_principle` 缺失或与 pandas 热力图短板分析不一致 -> 判错。引用 `data/README.md` 中 Belmont Report 原文 6 审查项。
- **worked_faded**:
  - **阶段1 Worked (完整示范)**: 给出完整的 `BelmontChecklist` pydantic 模型 + `assess_checklist_item` + `score_to_status` + `irb_ethics_review` 完整实现 (对照 `solution.ipynb` TODO1/TODO3)。
  - **阶段2 Faded (部分填空)**: 留空 `score_to_status` 阈值分支 (compliant>=80, conditional 60-79, non_compliant<60) 和 `weakest_principle` argmin 逻辑, 学生填。
  - **阶段3 Independent (独立解)**: 学生独立新增第 7 审查项 "data_deidentification" (数据脱敏), 修改 schema 并扩展评分器, 用 OECD AI Incidents 中"AI个性化推荐"案例自测。

### drill-2: 三框架并行映射 (子技能 S2)

- **drill_id**: D2-THREE-FRAMEWORK-MAP
- **difficulty**: 3
- **reps_required**: 3
- **feedback_rule**: 输出必须是三元组 `(belmont_score, nist_step, eu_risk_level)`, 其中 `nist_step ∈ {Govern, Map, Measure, Manage}` 且必须与"研究伦理视角"映射一致 (非企业视角), `eu_risk_level ∈ {prohibited, high, limited, minimal}` 必须带条款号 (Article 5 / Annex III / Article 50 / -)。引用 `notes.md` § 关键回顾 2/3 表格校对。
- **worked_faded**:
  - **阶段1 Worked**: 给出"AI个性化推荐研究 (有知情同意)"的完整三元组示范 -> `(85, Measure, limited-Article50)`。
  - **阶段2 Faded**: 留空"AI自动文案A/B测试 (无知情同意)"的 belmont_score 与 eu_risk_level, 学生填; NIST 步骤已给 (Measure)。
  - **阶段3 Independent**: 学生独立处理"AI客服交互研究 (有知情同意)"与"AI动态定价研究 (敏感+无同意+弱势)"两案例, 输出三元组并解释动态定价为何落入 Article 5 (禁止)。

### drill-3: 红队 probe + 天道推演 3 层树 (子技能 S3)

- **drill_id**: D3-REDTEAM-TIANDAO
- **difficulty**: 4
- **reps_required**: 2
- **feedback_rule**: 输出必须包含 (a) garak/PyRIT probe 列表 (>=2 个, 从 dan/promptinject/goodside 中选, 说明对应 Belmont 原则), (b) 天道推演 3 层树 (immediate/near/far 各 >=1 条, 必须因果相连, far 层必须含"罚款/禁令/声誉"之一), (c) 高杠杆点 (>=1 个, 小投入改变大局)。若 far 层缺因果连接或高杠杆点不可执行 -> 判错。
- **worked_faded**:
  - **阶段1 Worked**: 给出"AI动态定价研究"完整示范 -- probes=[dan, promptinject, goodside], 三层树 [immediate: 敏感数据无授权使用 -> near: 用户投诉/GDPR调查 -> far: 巨额罚款+研究禁令+声誉受损], 高杠杆点=[部署前补全知情同意+差分隐私] (对照 `notes.md` § 天道推演预演示例)。
  - **阶段2 Faded**: 留空"AI自动文案A/B测试 (无知情同意)"的三层树 far 层和高杠杆点, 学生填; probes 已给。
  - **阶段3 Independent**: 学生独立为"AI个性化推荐研究 (有知情同意)"构造完整三层树 + probe 集 + 高杠杆点, 并解释为何此案例风险等级较低 (有知情同意 -> Belmont Respect 得分高 -> far 层因果链被截断)。

---

## progressive_project (CS230 式渐进交付)

> 一个贯穿 R6 单元的真实研究伦理审查项目, 四阶段交付。每阶段独立评分, mastery_threshold >=80%。

- **proposal (第 1 周末提交)**: 选定一个真实 AI 研究 (从 OECD AI Incidents Monitor 取一个真实事件), 写 1 页 proposal: 研究摘要 + 涉及人类参与者识别 + 初步 Belmont 三原则风险预判。
- **milestone (第 3 周末提交)**: 提交 pydantic BelmontChecklist schema + 8 案例评分结果 + pandas 透视热力图 (案例×原则), 标注短板。
- **final (第 5 周末提交)**: 完整 IRB 伦理审查报告 (含 Belmont 评分 + NIST AI RMF 研究伦理映射 + EU AI Act 合规判定 + garak/PyRIT 红队 probe 集 + 天道推演 3 层风险路径 + 高杠杆点), 全部代码在 `solution.ipynb` 基础上扩展。
- **poster (第 6 周末提交)**: 1 页 A3 海报 (中文+英文 i+1), 标题"From Belmont to Red-Team: A Research Ethics Pipeline for AI+Marketing Studies", 包含三框架互补图 + 一个最关键高杠杆点 + 反思 (哪里推演对了/失误了)。

---

## interleaving (交叉排布, 非块状)

> 按 A1B1C1...B2C2A2...C3A3B3 顺序交叉, 促进迁移。A=drill-1 (S1), B=drill-2 (S2), C=drill-3 (S3)。

| 顺序 | 任务 | 子技能 | 阶段 | 预计时长 |
|:----:|------|:------:|:----:|:--------:|
| 1 | A1: drill-1 阶段1 Worked | S1 | Worked | 25 min |
| 2 | B1: drill-2 阶段1 Worked | S2 | Worked | 25 min |
| 3 | C1: drill-3 阶段1 Worked | S3 | Worked | 30 min |
| 4 | A2: drill-1 阶段2 Faded | S1 | Faded | 20 min |
| 5 | B2: drill-2 阶段2 Faded | S2 | Faded | 25 min |
| 6 | C2: drill-3 阶段2 Faded | S3 | Faded | 30 min |
| 7 | C3: drill-3 阶段3 Independent | S3 | Independent | 35 min |
| 8 | A3: drill-1 阶段3 Independent | S1 | Independent | 30 min |
| 9 | B3: drill-2 阶段3 Independent | S2 | Independent | 30 min |

**理由**: S3 (drill-3) 最难且依赖 S1/S2, 所以 C3 放最前 ( cognitive load 高时先攻最难); S1 (drill-1) 基础且独立, A3 放后 (巩固); S2 (drill-2) 中等, B3 收尾 (验证迁移)。每两个相邻任务来自不同子技能, 强制 context switch, 提升远迁移 (Far Transfer)。

---

## retry_policy (CS230 式)

- **10 free late days**: 整个 R6 单元享有 10 个免费迟交日, 用于 proposal/milestone/final/poster 任一阶段, 不扣分。
- **失败重试不罚分**: 任一 drill 阶段未达 mastery_threshold (>=80%) 可无限重试, 取最高分。重试时 feedback_rule 不变, 但案例可换 (从 OECD AI Incidents 取新事件)。
- **Worked 重看允许**: 重试时可重看阶段1 Worked 示范, 不视为作弊 (Ericsson: 反馈+修正循环)。

---

## weak_loop (连续 2 次失败触发弱项循环)

- **触发条件**: 同一 drill 连续 2 次未达 mastery_threshold (>=80%)。
- **回退动作**:
  1. 退回上一阶段 (Independent -> Faded, Faded -> Worked)
  2. 补充 1 个 worked example (从 `solution.ipynb` 取对应 TODO 的完整解答, 学生手抄一遍并加注释)
  3. 重做 diagnostic 中对应题目 (D1->S1, D2->S2, D3->S3) 验证盲点是否补上
  4. 重新进入原阶段, 若再失败 -> 触发 1:1 助教 review (引用 Hattie [TASK] 反馈: 具体到哪一步错)

---

## mastery_threshold

- 单 drill: >=80% (各 feedback_rule 全部命中)
- progressive_project 各阶段: >=80%
- 单元总评: 4 阶段均 >=80% + diagnostic 自查全对 = mastery 通过

---

*本 practice.md 基于 Ericsson 刻意练习 + MIT CS229 pset0 + CS230 渐进交付 + Harvard Worked-Faded + Stanford interleaving 设计。所有 feedback_rule 领域特定, 引用 Belmont Report / NIST AI RMF / EU AI Act / garak / PyRIT / pydantic / OECD AI Incidents Monitor 真实框架与数据。*
