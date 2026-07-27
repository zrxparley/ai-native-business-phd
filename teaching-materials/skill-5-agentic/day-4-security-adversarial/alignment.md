---
unit: U5D4
title: Agent 安全与对抗 - 建构对齐 (Constructive Alignment, Biggs 1996)
version: v6.0
references:
  - Biggs, J. "Enhancing teaching through constructive alignment" (1996)
  - Hattie & Timperley "The Power of Feedback" (2007) - Feed Up / Feed Back / Feed Forward
  - Bloom mastery learning threshold >=80%
  - 本单元 notes.md / starter.ipynb / solution.ipynb / practice.md / tutorial.ipynb
---

# 建构对齐 (Biggs ILO ↔ TLA ↔ AT)

> Biggs 建构对齐核心: **ILO (Intended Learning Outcome, 预期学习产出)** 决定 **TLA (Teaching/Learning Activity, 教学学习活动)**, TLA 训练的能力由 **AT (Assessment Task, 评估任务)** 测量。三者必须一一对应, 否则对齐失败 (学生能过 AT 但未经 TLA, 或 TLA 训练的能力 AT 没测)。

## ILO ↔ TLA ↔ AT 矩阵 (>=3 行, 每行 mastery_threshold)

| ILO (预期学习产出) | TLA (教学学习活动) | AT (评估任务) | mastery_threshold |
|------------------|------------------|--------------|------------------|
| **ILO1**: 能解释 Prompt Injection 直接 vs 间接两种形态, 说明 OWASP 为何列十大风险之首 | 读 notes.md "关键回顾 1" + 跑 starter.ipynb TODO2 复现攻击 + practice.md D1 diagnostic 自测 | solution.ipynb TODO2 的攻击复现输出 + 300 字分析"间接注入为何更危险" | >=80% (3 题中答对 2 题 + 分析无关键错漏) |
| **ILO2**: 能用 garak 跑 dan/promptinject/encoding/goodside probes, 读懂 fail 率报告 | practice.md drill D1-garak-scan (Worked->Faded->Independent 三阶段) + tutorial.ipynb 苏格拉底追问"probe/detector/generator 三层抽象" | starter.ipynb TODO1 完成的 garak 报告 + practice.md D1 Independent 选新 probe (leakreplay) 跑通 | >=80% (garak 报告结构化 + fail 率正确解析 + 新 probe 跑通) |
| **ILO3**: 能用 PyRIT PromptSendingOrchestrator + Scorer 批量红队, 用 RedTeamingOrchestrator 编排多轮 | practice.md drill D2-pyrit-orchestrator (三阶段) + tutorial.ipynb 追问"四件套职责" + 限频复习 | starter.ipynb TODO4 的 pyrit_results.jsonl + 攻破率断言 < 30% | >=80% (>=20 条对抗提示 + scorer 评分 + 断言通过) |
| **ILO4**: 能为营销 Agent 设计 >=4 层分层防御 (输入/提示/输出/人工), 加固后 garak fail 率降 >=50% | practice.md drill D3-layered-defense (三阶段) + tutorial.ipynb HBS devil's advocate 追问"防御层被绕过怎么办" | starter.ipynb TODO5 防御代码 + TODO6 IMRaD 报告 + 加固前后 garak 重扫对比 | >=80% (>=4 层防御可独立验证 + fail 率降幅达标 + IMRaD 四节齐全) |
| **ILO5**: 能对照 NIST AI RMF 四步循环 + HarmBench 基准给安全治理建议 | practice.md drill D4-imrad-report Independent 阶段 + schedule.json C6 卡间隔重复 | TODO6 IMRaD 报告的 Discussion 节映射 NIST 四步 + HarmBench 分类 | >=80% (四步映射无遗漏 + HarmBench standard/contextual 分类正确) |

---

## 3 自检问题 (Feed Up / Feed Back / Feed Forward, Hattie & Timperley 2007)

> 三个问题用来检验 ILO↔TLA↔AT 是否真的对齐。任何一个答 No 就是对齐失败, 必须改 TLA 或 AT。

### Q1. Feed Up (TLA 是否训练 ILO?)
**问**: 每条 ILO 是否都有对应的 TLA 在训练它? 学生做完 TLA 后能力是否真的向 ILO 靠拢?

**自检**:
- ILO1 (Prompt Injection 形态): TLA 含读 notes.md + 跑 TODO2 复现 + D1 diagnostic -- **Yes**, 三种活动都训练"区分两种形态"
- ILO2 (garak 扫描): TLA 含 D1 drill 三阶段 + tutorial 追问 -- **Yes**, Worked 示范+Faded 填空+Independent 新 probe 训练"独立跑通"
- ILO3 (PyRIT 红队): TLA 含 D2 drill + tutorial 追问四件套 -- **Yes**, 但需确认学生真跑了 >=20 条对抗提示而非抄 solution
- ILO4 (分层防御): TLA 含 D3 drill + tutorial devil's advocate -- **Yes**, 但需确认加固后 garak 重扫对比是真跑而非编数字
- ILO5 (NIST/HarmBench): TLA 含 D4 Independent + schedule.json C6 间隔重复 -- **Yes**, 但 C6 只是记忆卡, 需补一个"映射练习"活动

**结论**: 5 条 ILO 都有 TLA 训练, 但 ILO5 的 TLA 偏记忆, 需在 tutorial 里加一个"把你的 IMRaD 报告 Discussion 映射到 NIST 四步"的追问。

### Q2. Feed Back (AT 是否测量 ILO?)
**问**: 每个 AT 是否真的在测量对应的 ILO? AT 的评分标准是否与 ILO 的可观察行为对应?

**自检**:
- ILO1 的 AT (TODO2 攻击复现 + 300 字分析): 测的是"能复现 + 能解释", 与 ILO1 "能解释两种形态"对应 -- **Yes**
- ILO2 的 AT (garak 报告 + 新 probe 跑通): 测的是"能跑 + 能读懂 fail 率", 与 ILO2 对应 -- **Yes**
- ILO3 的 AT (pyrit_results.jsonl + 断言 < 30%): 测的是"能批量发 + 能用 Scorer 评分 + 能下断言", 与 ILO3 对应 -- **Yes**
- ILO4 的 AT (防御代码 + 加固前后对比 + IMRaD): 测的是"能设计防御 + 能验证有效 + 能写报告", 与 ILO4 对应 -- **Yes**
- ILO5 的 AT (Discussion 映射 NIST + HarmBench 分类): 测的是"能映射治理框架", 与 ILO5 对应 -- **Yes**

**结论**: 5 条 AT 都测量对应 ILO, mastery_threshold >=80% 量化清晰。

### Q3. Feed Forward (不经 TLA 能过 AT 吗? 若能 = 对齐失败)
**问**: 一个学生如果**不参与任何 TLA** (不读 notes.md / 不跑 drill / 不上 tutorial), 只靠抄 solution.ipynb 或背答案, 能过 AT 吗? 如果能, 说明 AT 没真测 ILO, 对齐失败。

**自检**:
- ILO2 AT "新 probe leakreplay 跑通": 抄 solution 跑的是 dan, leakreplay 需独立选 probe + 解析新报告格式 -- **不能轻松抄**, 对齐 OK
- ILO3 AT "攻破率断言 < 30%": 抄 solution 的 orchestrator 可以, 但断言阈值需自己根据 scorer 输出调 -- **部分能抄**, 需在 AT 加"解释为什么选 30% 阈值"的口头答辩
- ILO4 AT "加固前后 garak 重扫 fail 率降 >=50%": 抄 solution 的防御代码可以, 但重扫需真跑 garak, 编数字会被交叉验证 -- **不能轻松抄**, 对齐 OK
- ILO5 AT "NIST 四步映射": 抄概念可以, 但映射需结合自己 IMRaD 的 Discussion -- **部分能抄**, 需在 AT 加"指出你的报告里哪段对应 NIST 的 Measure 步"的指认题

**结论**: ILO3 和 ILO5 的 AT 存在"部分能抄"风险, 已在自检里补充口头答辩 / 指认题作为 Feed Forward 修补。整体对齐 PASS, 但需在 tutorial 追问环节落实这两个补救问。

---

## mastery_threshold 兑现机制

- 每条 ILO 的 AT 都设 >=80% 阈值 (Bloom mastery learning)
- 未达 80% 的 ILO 触发 practice.md 的 weak_loop (回退上一 drill + 补 Worked example + 降 reps_required)
- 全部 5 条 ILO 达 80% 才算本 unit mastery, 才能进入 Day 5 (生产部署与运维)
- mastery 状态写入 tutorial.ipynb 的 student_model.json 的 `mastery` 字段, 供后续 Day 复用

---

*本 alignment.md 遵循 Biggs 建构对齐原则: ILO 决定 TLA, TLA 训练的能力由 AT 测量, AT 不经 TLA 难以通过 (Feed Forward 自检)。Hattie 四级反馈在 tutorial.ipynb 落地。*
