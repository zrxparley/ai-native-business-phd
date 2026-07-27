# alignment.md - Constructive Alignment (Biggs) - skill-4-business-model/day-4-platform-strategy-ecosystem

> v6.0 学习科学层 · Biggs 建构对齐 (Constructive Alignment)
> 哲学：ILO (预期学习产出) ↔ TLA (教学学习活动) ↔ AT (评估任务) 三者对齐，才不会"教 A 考 B"。

---

## ILO ↔ TLA ↔ AT 矩阵

| ILO (Intended Learning Outcome 预期学习产出) | TLA (Teaching/Learning Activity 教学学习活动) | AT (Assessment Task 评估任务) | mastery_threshold |
|---|---|---|---|
| **ILO1**: 能用 networkx 构建真实平台生态网络（26节点40边，多边关系），计算度分布/聚类系数/核心-边缘结构，识别生态核心节点与边缘风险 | starter.ipynb TODO1+TODO2 drill D1 worked-faded + tutorial.ipynb Socratic 追问 + schedule.json C1/C2/C5 间隔复习 | solution.ipynb 解题（结构对应无 scaffold）+ D1 independent 阶段（独立构建 21 节点 MCP 生态）+ tutorial 后测 | >=80% 正确率 + 能口述"谁是核心、谁是边缘、为什么" |
| **ILO2**: 能用 pandas 量化多归属率/锁定度/网络效应强度/赢者通吃倾向，按参与者类型分组，并解释数据飞轮对锁定度的加权 | starter.ipynb TODO3+TODO5 drill D2 worked-faded + tutorial.ipynb 追问"为何乘飞轮强度" + schedule.json C3/C6 间隔复习 | D2 independent 阶段（独立计算 MCP 生态多归属率+A2A 迁移成本）+ 项目 P2 milestone | >=70% 正确率 + 能解释 4 类参与者多归属率差异原因 |
| **ILO3**: 能用 numpy 蒙特卡洛 + 贝叶斯先验实现天道推演，预判平台 tipping point，输出 2-3 时间线 + 风险预警 + 认知盲点 | starter.ipynb TODO6 drill D3 worked-faded + tutorial.ipynb Socratic "tipping 为何是概率分布" + schedule.json C4 间隔复习 + 项目 P3+P4 | D3 independent 阶段（独立推演 Hugging Face vs 新进入者 tipping）+ 项目 P3 final + P4 poster | 能独立解 + tipping 概率分布合理（非单点）+ 盲点 >=2 个 |

---

## mastery_threshold 说明

- **>=80% (ILO1)**：networkx 图构建零语法错误 + 核-边分析输出完整 + 能口述生态核心/边缘判断依据
- **>=70% (ILO2)**：pandas 多归属率分母正确 + WTA 倾向输出连续概率（非二元）+ 能解释锁定度乘飞轮强度的原因
- **能独立解 (ILO3)**：蒙特卡洛用贝叶斯先验（非纯频率主义）+ tipping 输出概率分布（非单点）+ 盲点 >=2 个 + 2-3 时间线

不达 mastery_threshold 的 drill 触发 practice.md `weak_loop`（连续 2 次失败回退到上一阶段 + 补充 worked example + 额外复习卡）。

---

## 3 自检问题 (Biggs 三问，对应 Hattie Feed Up / Feed Back / Feed Forward)

> 每次单元交付后用以下 3 问自检建构对齐是否成立。任一答"否"则需重设计。

1. **Feed Up (TLA 是否训练 ILO?)**：starter.ipynb 的 6 个 TODO + practice.md 的 3 个 drill 是否直接训练 ILO1/ILO2/ILO3 的可观察技能？
   - 自检答：是。TODO1/2 ↔ D1 ↔ ILO1；TODO3/5 ↔ D2 ↔ ILO2；TODO6 ↔ D3 ↔ ILO3。每个 TODO 都有对应 drill 和 ILO，无悬空训练。
2. **Feed Back (AT 是否测量 ILO?)**：solution.ipynb + D1/D2/D3 independent 阶段 + 项目 P2/P3/P4 是否测量 ILO1/ILO2/ILO3 的掌握度？
   - 自检答：是。D1 independent 测 ILO1（构建新生态）；D2 independent 测 ILO2（MCP 多归属率）；D3 independent 测 ILO3（HF vs 新进入者 tipping）。每个 AT 都对应 ILO，无"教 A 考 B"。
3. **Feed Forward (不经 TLA 能过 AT 吗?)**：如果学生跳过 starter.ipynb drill 和 tutorial Socratic 追问，直接交 solution.ipynb 抄答案，能过 AT 吗？若能 = 对齐失败。
   - 自检答：不能。D1/D2/D3 independent 阶段的题目（MCP 生态/HF vs 新进入者）与 starter.ipynb 的 worked/faded 题目不同，且 tutorial 后测口述"为什么"必须经过 Socratic 追问才能形成。抄 solution.ipynb 只能过 faded，无法过 independent + 口述。

---

## 跨文件对齐追踪

| 文件 | 对应 ILO | 对应 drill | 对应 card |
|---|---|---|---|
| notes.md §学习目标 1 | ILO1 | D1 | C1, C2, C5 |
| notes.md §学习目标 2-3 | ILO2 | D2 | C3, C6 |
| notes.md §学习目标 5 | ILO3 | D3 | C4 |
| starter.ipynb TODO1/2 | ILO1 | D1 worked-faded | C1, C2 |
| starter.ipynb TODO3/5 | ILO2 | D2 worked-faded | C3 |
| starter.ipynb TODO6 | ILO3 | D3 worked-faded | C4 |
| tutorial.ipynb Socratic | ILO1/2/3 | D1/D2/D3 independent | C1-C6 |
| practice.md weak_loop | ILO1/2/3 | D1/D2/D3 retry | C1-C6 weak 卡 |

---

*本文件配合 practice.md（刻意练习）、schedule.json（间隔重复）、tutorial.ipynb（牛津 Socratic）使用。Biggs 建构对齐确保"教-学-评"三者不脱节。*
*最后更新：2026-07-25*
