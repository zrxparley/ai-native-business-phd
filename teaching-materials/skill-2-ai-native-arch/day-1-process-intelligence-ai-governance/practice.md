# 刻意练习设计 (Ericsson + MIT 6.5940) · Day 1 流程智能驱动 + AI治理框架

> v6.0 学习科学层。配合 `starter.ipynb` / `solution.ipynb` / `tutorial.ipynb` / `schedule.json` / `alignment.md` 使用。

---

## skill_target

**可观察技能**：给定一个真实AI用例（如营销个性化推荐 / 动态定价 / AI客服），能在 30 分钟内独立完成 (1) 用 pydantic 定义 NIST AI RMF 控制项 schema；(2) 实现合规扫描器输出 0-100 评分；(3) 实现 EU AI Act 风险分级器判定 Article 5 / Annex III / Article 50 / 最小风险；(4) 用 pandas 生成"用例×功能"风险热力图并定位最弱控制项；(5) 用天道推演沙盘输出 2-3 条风险路径与高杠杆干预点。

## subskills

- **S1 - Schema 建模**：用 pydantic 定义 `ComplianceStatus` 枚举 + `ControlItem` / `AIUseCase` 模型，覆盖 NIST 18 个真实控制项与 OECD 真实事件类型
- **S2 - 双框架合规判定**：实现 `scan_nist_rmf` + `classify_eu_ai_act`，能区分"有限风险需透明度"与"高风险需合格评定"的法律边界
- **S3 - 风险可视化与推演**：用 pandas 构建热力图定位短板，用天道推演因果链输出风险路径与高杠杆点（连接 NIST Map -> Manage）

---

## diagnostic (pre-test, pset0 式)

开课 15 分钟内完成，不计分但用来标定起点：

- **Q1**：NIST AI RMF 的四个核心功能是什么？`Govern` 与其他三个功能的关系是"串行"还是"贯穿"？用一句话回答。
- **Q2**：给定一个"AI 客服在用户不知情情况下记录对话用于训练"的用例，它在 EU AI Act 下属于哪个风险等级？引用具体条款。
- **Q3**：以下哪条是 NIST AI RMF 的真实控制项编号？(a) `GOVERN-2` (b) `MAP-3.4` (c) `MEASURE-1` (d) `MANAGE-4` (e) 以上都是。若答 (e)，说明每个控制项的语义。

> Q1 答错 -> 回到 `notes.md` 关键回顾 2；Q2 答错 -> 回到关键回顾 3 + Article 50；Q3 答错 -> 打开 `data/README.md` 看真实控制项清单。

---

## drills (>=3, 每个 difficulty 1-5 + reps_required + feedback_rule + worked-faded 三阶段)

### drill_id: D1
**skill**：S1 - pydantic schema 建模
**difficulty**: 2
**reps_required**: 3
**feedback_rule**: 若 `ControlItem` 缺少 `id` / `function` / `description` / `status` 任一字段 -> 反馈"对照 NIST AI RMF 1.0 真实控制项清单（ Govern-1~5 / Map-1~5 / Measure-1~4 / Manage-1~4 ），你的 schema 漏掉了哪一个维度？打开 `data/README.md` 链接核对"。若 `ComplianceStatus` 枚举不全（缺 `COMPLIANT` / `PARTIAL` / `NON_COMPLIANT` / `NOT_APPLICABLE`） -> 反馈"真实合规评估至少需要这 4 个状态，想想 PARTIAL 和 NOT_APPLICABLE 的区别"。
**worked_faded**:
- 阶段 1 (Worked) - 完整示范：教师演示 `Govern-1: AI Governance Policy` 的 pydantic 模型定义，含字段、validator、docstring
- 阶段 2 (Faded) - 部分填空：给出 `Map-1: Context Established` 的模型骨架，学生填 `function` 字段和 1 个 validator
- 阶段 3 (Independent) - 独立解：学生独立完成剩余 16 个控制项的模型定义

### drill_id: D2
**skill**：S2 - 双框架合规判定
**difficulty**: 4
**reps_required**: 3
**feedback_rule**: 若 EU AI Act 分级顺序错误（应按 Article 5 禁止 -> Annex III 高风险 -> Article 50 有限 -> 最小风险，从严到宽） -> 反馈"记住 EU AI Act 是从最严到最宽的瀑布式判定，先判禁止再判高风险，错了会导致保险定价被误判为最小风险"。若 NIST 评分逻辑混淆"控制项通过率"与"风险等级" -> 反馈"NIST 是治理成熟度（0-100），EU Act 是法律分级，两者不可互相替代，回到 notes.md 关键回顾 2+3 对照表"。若 `classify_eu_ai_act` 没有处理 Annex III 中的保险/信贷例外 -> 反馈"动态定价在涉及保险时升为高风险，你的代码有没有 if 分支处理这个例外？"
**worked_faded**:
- 阶段 1 (Worked) - 完整示范：教师演示 `assess_control(use_case, control)` 函数，含评分逻辑、阈值映射、status 返回
- 阶段 2 (Faded) - 部分填空：给出 `score_to_status(score)` 函数骨架，学生填阈值边界（>=80 COMPLIANT / 50-79 PARTIAL / <50 NON_COMPLIANT）
- 阶段 3 (Independent) - 独立解：学生独立实现 `classify_eu_ai_act(use_case)`，处理 Article 5 / Annex III / Article 50 / 最小风险四级

### drill_id: D3
**skill**：S3 - 风险热力图 + 天道推演
**difficulty**: 5
**reps_required**: 3
**feedback_rule**: 若 pandas 热力图没有用 `pivot_table` 或 `groupby` 聚合 -> 反馈"用 `pd.DataFrame(...).pivot_table(index='use_case', columns='function', values='score')` 才能得到用例×功能矩阵，回去改"。若没有定位"最弱控制项"（最低分 function） -> 反馈"NIST AI RMF 的 Manage 维度若得分最低，意味着企业'知道风险但不会应对'，这是最危险的状态；你的代码 `idxmin()` 找到了吗？"。若天道推演只列 1 条路径 -> 反馈"天道推演要求至少 3 层走向（immediate -> near -> far）和 2-3 条平行时间线，回到 notes.md 2026前沿补充章节看营销AI推演示例"。
**worked_faded**:
- 阶段 1 (Worked) - 完整示范：教师演示对 1 个营销用例（AI个性化推荐）构建热力图 + 推演路径 A（无治理）+ 路径 B（有 NIST Measure 治理）
- 阶段 2 (Faded) - 部分填空：给出 AI 动态定价用例的 DataFrame 骨架和推演模板，学生填 `pivot_table` 参数和路径 B 的因果节点
- 阶段 3 (Independent) - 独立解：学生独立完成 AI 客服 / AI 自动文案两个用例的热力图 + 推演路径

---

## progressive_project (CS230 式脚手架: proposal -> milestone -> final -> poster)

- **Proposal (Day 1 课前提交)**：选定 1 个企业真实 AI 用例（非课上 8 个 OECD 案例），提交 1 页 proposal：用例描述 / 数据流 / 已知风险 / 你打算用 NIST 哪个功能重点治理
- **Milestone (Day 1 课中)**：提交 `starter.ipynb` 完成 TODO1-TODO4（schema + 扫描器 + 分级器），未完成 TODO5/TODO6 可拿 milestone 分
- **Final (Day 1 课后 48h)**：提交完整 `solution.ipynb`（6 个 TODO 全完成）+ 300 字风险路径分析（用天道推演输出）
- **Poster (Day 2 课前 5 分钟)**：1 页 slide 展示你的用例在 NIST 哪个功能得分最低 + 对应 EU AI Act 等级 + 1 条高杠杆干预

---

## interleaving (A1B1C1...B2C2A2...C3A3B3, 不块状)

**禁止块状练习**（A1A2A3 B1B2B3 C1C2C3），按下表交叉排布：

| 时间槽 | 练习内容 | 子技能 |
|:----:|---------|:----:|
| Slot 1 | A1: D1 阶段 1 (Worked pydantic schema) | S1 |
| Slot 2 | B1: D2 阶段 1 (Worked 双框架判定) | S2 |
| Slot 3 | C1: D3 阶段 1 (Worked 热力图+推演) | S3 |
| Slot 4 | A2: D1 阶段 2 (Faded pydantic schema) | S1 |
| Slot 5 | B2: D2 阶段 2 (Faded 双框架判定) | S2 |
| Slot 6 | C2: D3 阶段 2 (Faded 热力图+推演) | S3 |
| Slot 7 | A3: D1 阶段 3 (Independent pydantic schema) | S1 |
| Slot 8 | B3: D2 阶段 3 (Independent 双框架判定) | S2 |
| Slot 9 | C3: D3 阶段 3 (Independent 热力图+推演) | S3 |

> **依据**：MIT Open Learning 明文原则——交叉练习 (A1B1C1...B2C2A2...C3A3B3) 比块状练习提升长期保留率。Butler (2010) 检索练习证据：交叉 + 检索 > 块状 + 重学。

---

## retry_policy (CS229 / CS230 式)

- **迟交**：10 late days / 学期，每迟 1 天扣 20% 分（与 CS230 一致）
- **重做**：milestone 未过（<70%）可在 final 前重做 1 次，新分 = 0.7 × 重做分
- **drill 重做**：单 drill 连续 2 次失败（feedback_rule 触发）-> 进入 weak_loop

---

## weak_loop (连续 2 次失败触发)

若学生在某 drill 连续 2 次未达 reps_required 阈值：

1. **回退**：回到上一个 drill 的阶段 1 (Worked) 重新观看示范
2. **补充 worked example**：教师提供 1 个额外 worked example（非课上案例，如 AI 简历筛选或 AI 招聘评分）
3. **限频**：每天最多进入 weak_loop 1 次，避免学生依赖教师补充
4. **退出条件**：在补充 worked example 后能独立完成阶段 3 (Independent) 1 次，方可回到原 drill

> **依据**：Ericsson 刻意练习 5 要素之"即时反馈" + "难度匹配"。weak_loop 防止学生在挫败中放弃，也防止在简单重复中停滞。

---

## 交叉引用

- `schedule.json`：FSRS-6 间隔重复，3 张核心卡 (NIST 四功能 / EU Act 四级 / 天道推演三时间线) 按 due [1,3,8,21,60,180] 复习
- `alignment.md`：Biggs ILO↔TLA↔AT 矩阵，本 practice.md 的 drills 对应 TLA
- `tutorial.ipynb`：牛津 tutorial 仿真，Socratic 追问 + Hattie 四级反馈
- `notes.md`：v5.0 原文（理论 + 真实框架 + 前沿点），末尾追加 v6.0 学习科学层说明
