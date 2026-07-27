# Constructive Alignment - 因果推断基础 (Day 1)

> v6.0 学习科学层 · Biggs 建构对齐 ILO ↔ TLA ↔ AT 矩阵 + mastery 阈值 + 3 自检
> 配套 v5.0 notes.md / starter.ipynb / solution.ipynb / practice.md / schedule.json / tutorial.ipynb

---

## ILO ↔ TLA ↔ AT 矩阵 (Biggs Constructive Alignment)

| ILO (Intended Learning Outcome, 预期学习产出) | TLA (Teaching/Learning Activity, 教学学习活动) | AT (Assessment Task, 评估任务) | mastery_threshold |
|---|---|---|---|
| **ILO1**: 能用 Pearl 因果阶梯（关联/干预/反事实）解释"为什么相关≠因果"，并指出营销场景中各层级对应的操作 | notes.md "关键回顾 1" + practice.md diagnostic 第 2 题 + tutorial.ipynb Socratic 第 1 轮 + schedule.json 卡片 C1 复习 | diagnostic 第 2 题口头辩护 + tutorial Socratic 应答 + schedule.json C1 卡片 rating>=good | 概念题 100% 正确 + 能在 tutorial 中独立给营销案例做层级映射 |
| **ILO2**: 能为一个营销问题画 DAG，识别混杂与后门路径，说明如何用后门准则阻断 | practice.md D1 (Worked->Faded->独立解 三阶段) + starter.ipynb TODO1-2 + notes.md "关键回顾 2" + schedule.json C2 | D1 阶段 3 独立解（全新场景画 DAG+列后门路径+切断节点）+ starter.ipynb TODO1-2 提交 + P2 Milestone 交付 | D1 三阶段连续 2 次 reps 达 80% + P2 Milestone DAG 无遗漏后门路径 |
| **ILO3**: 能在真实数据 (causaldata.nsw) 上区分朴素均值差（有偏）与后门调整估计（因果），解释差异来源 | practice.md D2 + starter.ipynb TODO3-4 + notes.md "关键回顾 3" + schedule.json C3 + D2 Worked 完整跑 NSW | D2 阶段 3 独立解（换数据集跑 DoWhy 四步）+ starter.ipynb TODO3-4 + 300 字差异分析（P3 Final） | D2 reps 3 次达 80% + 朴素 ATE 与后门 ATE 数值差异 < 5% 误差解释清楚 + ≥2 refuter 通过 |
| **ILO4**: 能用 DoWhy 完成"建模->识别->估计->反驳"四步因果分析流程 | practice.md D2 + starter.ipynb TODO4-5 + schedule.json C3 + tutorial.ipynb Socratic 第 2-3 轮（针对 DoWhy 流程追问） | starter.ipynb TODO4-5 提交 + D2 阶段 3 + tutorial 应答"为什么必须跑 refute_estimate" | 四步全跑通 + 能解释 placebo_treatment_refuter 返回 new_effect≈0 的含义 |
| **ILO5**: 能用混合方法视角 + LLM-as-a-judge 设计因果评估方案，并定位其在因果阶梯 L1 | practice.md D3 + notes.md "2026 前沿" + starter.ipynb TODO6 (可选) + schedule.json C4 + tutorial.ipynb Socratic 第 4 轮 | D3 阶段 3 独立解（LLM-as-judge 审查 + 魔鬼代言人判断）+ student_model.json blind_spots 记录 + P4 Poster 展示盲点 | D3 reps 3 次达 80% + 能区分 LLM-as-judge (L1) 与 ATE 估计 (L2/L3) + blind_spots 至少 1 条 LLM 指出的未考虑混杂 |

---

## mastery_threshold (整体单元)

- **通过 (Pass)**: 5 个 ILO 中至少 4 个达 mastery_threshold + diagnostic 后测全对 + P3 Final 提交
- **优秀 (Distinction)**: 5 个 ILO 全部达 mastery_threshold + P4 Poster 同伴互评 >=4/5 + tutorial 中能反问 LLM-as-judge 的盲点
- **未通过 (Fail)**: 任一 ILO 未达 mastery_threshold 且 weak_loop 累计 4 次仍失败 -> 回到 notes.md 重读 + 重新预约 tutorial

借鉴 MIT 6.5940 "至少 4/5 实验提交方可及格" 的 mastery 阈值设计。

---

## 3 自检问题 (Biggs Feed Up / Feed Back / Feed Forward)

### 1. Feed Up (TLA 是否训练 ILO？教学活动对齐性)
**问**：本单元的 TLA（practice.md 的 D1-D3 + tutorial Socratic + schedule.json 复习 + starter.ipynb 6 个 TODO）是否真正训练了 ILO1-ILO5？哪些 TLA 在训练 ILO 上是冗余或低效的？

自检方法：随机抽 3 个 TLA，逐个问"如果删掉它，哪个 ILO 会塌？" 若删掉后无 ILO 塌 = 冗余；若删掉后多个 ILO 塌 = 该 TLA 是承重墙，必须保留。

本单元自检结论：D1 是 ILO2 的承重墙；D2 是 ILO3+ILO4 的承重墙；D3 是 ILO5 的承重墙；tutorial Socratic 是 ILO1 概念深化的承重墙；schedule.json 是间隔重复保持，删掉短期不塌但长期（21 天后）会塌。

### 2. Feed Back (AT 是否测量 ILO？评估效度)
**问**：本单元的 AT（diagnostic 三题 + D1-D3 各阶段 3 + P1-P4 项目 + tutorial 应答 + schedule.json 卡片 rating）是否真正测量了 ILO？有没有 AT 测了 ILO 之外的东西（构念污染）？有没有 ILO 没被任何 AT 测到（覆盖盲区）？

自检方法：对每个 ILO 问"哪几个 AT 测它？" 若某 ILO 无 AT 覆盖 = 补 AT；若某 AT 不对应任何 ILO = 删 AT。

本单元自检结论：ILO1 被 diagnostic 第 2 题 + tutorial 应答 + C1 卡片覆盖；ILO2 被 D1 三阶段 + P2 覆盖；ILO3 被 D2 + 300 字分析 + C3 覆盖；ILO4 被 starter.ipynb TODO4-5 + D2 阶段 3 覆盖；ILO5 被 D3 + blind_spots + P4 覆盖。无覆盖盲区，无构念污染。

### 3. Feed Forward (不经 TLA 能过 AT 吗？对齐失败检测)
**问**：如果一个学生完全不参加 TLA（不上课、不练 D1-D3、不上 tutorial、不刷 schedule.json），仅凭先验知识能通过 AT 吗？若能 = 对齐失败（AT 太浅或 ILO 太低）。

自检方法：找 1 个有统计基础但无因果推断经验的同学，让他跳过 TLA 直接做 AT，看能不能过。

本单元自检结论：跳过 TLA 的同学大概率能答对 diagnostic 第 2 题（A/B 测试概念常识），但 D1 阶段 3 独立画 DAG 会卡（不知道后门准则）、D2 阶段 3 会卡（没用过 DoWhy）、D3 会卡（不知道 LLM-as-judge 的 L1 限制）。结论：对齐成立，AT 有效地强制了 TLA 参与。

---

## 与 v6.0 其他文件的衔接

- ILO2-ILO5 的 mastery 由 `practice.md` 的 drill reps 跟踪
- 复习节奏由 `schedule.json` (FSRS-6) 保障
- tutorial Socratic 对应 ILO1/ILO4/ILO5 的概念深化
- 学生掌握度状态写入 `student_model.json`（tutorial.ipynb 读写），跨单元复用

---

*v6.0 学习科学层 · Biggs Constructive Alignment + MIT 6.5940 mastery 阈值 + Hattie 3 问 (Feed Up/Back/Forward)*
