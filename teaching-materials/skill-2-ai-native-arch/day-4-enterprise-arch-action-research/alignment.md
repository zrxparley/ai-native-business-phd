# Constructive Alignment - 技能2 · Day 4 企业级架构+行动研究

> v6.0 学习科学层 · Biggs 建构对齐 (Constructive Alignment) -- ILO (Intended Learning Outcomes) ↔ TLA (Teaching/Learning Activities) ↔ AT (Assessment Tasks) 三者必须对齐, 否则"不经 TLA 能过 AT"即为对齐失败。
> 哲学: 科学即高效 · 反馈即成长 -- 用 Biggs 建构对齐确保"教什么 / 学什么 / 考什么"三者一致, 避免学生靠刷题或抄答案过关。

---

## ILO ↔ TLA ↔ AT 矩阵

| ILO (预期学习产出) | TLA (教学学习活动) | AT (评估任务) | mastery_threshold |
|---|---|---|---|
| **ILO1**: 能用 pydantic 设计 CDP 四层 schema (Identity/Event/Segment/Profile), 基于 Segment Spec, 字段类型严格匹配 | starter.ipynb TODO1-3 + practice.md drill D1 (worked-faded 三阶段) + tutorial.ipynb Socratic 追问 "为什么 timestamp 用 datetime 而非 str?" + schedule.json C1 间隔复习 | solution.ipynb CDP 模型可 `model_validate_json` 一段真实 Segment 事件 + tutorial 后测 (口头辩护 Segment Spec required fields) | CDP 四层 pydantic 模型字段类型 100% 正确, 可 json 实例化, validator 不缺; D1 连续 3 次达标 |
| **ILO2**: 能用 networkx 建模 TOGAF 四层依赖图 (业务/应用/数据/技术), 输出关键路径与单点故障分析 | starter.ipynb TODO4-5 + practice.md drill D2 (worked-faded) + tutorial Socratic "17 节点 27 边, CDP事件层故障下游因果链几跳?" + schedule.json C2 | solution.ipynb 架构依赖图 (>=17 节点 >=27 边) + 关键路径 `nx.topological_sort` 输出 + 单点故障因果链描述 | 节点数 >=17, 边数 >=27, 四层分区正确 (业务/应用/数据/技术), 关键路径识别无误; D2 连续 3 次达标 |
| **ILO3**: 能用 pandas 分析行动研究 4 轮 KPI, 计算改善幅度, 排除霍桑效应, 理解 Susman 五步螺旋 | starter.ipynb TODO6 + practice.md drill D3 (worked-faded) + tutorial Socratic "n=2 能下结论吗? 如何排除霍桑效应?" + schedule.json C3 | solution.ipynb pandas 趋势图 + 改善幅度 `(last-first)/first*100%` + 霍桑效应排除论证 (对照组/DML/合成控制) | 改善幅度计算误差 <5%, 反思阶段 KPI 识别正确, 霍桑效应排除论证逻辑自洽; D3 连续 3 次达标 |
| **ILO4**: 能用天道推演视角对架构选型做 3 层沙盘推演, 输出 2-3 个差异化方案 + 因果链描述 (项目 CLAUDE.md 同构) | tutorial.ipynb Socratic 第 4 轮 "3 年后 Agent 从 4 个增加到 40 个, 你的架构哪个组件先崩溃?" + 500 字反思 + schedule.json C4 | 500 字天道推演反思 (含 >=3 层 future 推演 + >=2 个差异化方案 + 因果链) + DSR artifact 定位 (schedule.json C5) | >=3 层 future 推演 (immediate/near/far) + >=2 个差异化方案对比 + 完整因果链描述; 反思逻辑自洽非套话 |

---

## mastery_threshold 总览

| 子技能 | drill | mastery_threshold | 验证方式 |
|---|---|---|---|
| S1 · CDP schema | D1 | 字段类型 100% 正确, validator 不缺, 可实例化 | `model_validate_json` 真实 Segment 事件通过 |
| S2 · TOGAF 依赖图 | D2 | >=17 节点 >=27 边, 四层分区正确, 关键路径无误 | `nx.topological_sort` 输出 + 因果链描述 |
| S3 · 行动研究 KPI | D3 | 改善幅度误差 <5%, 霍桑效应排除论证自洽 | pandas 趋势图 + 改善幅度 + 对照组论证 |
| S4 · 天道推演 (跨子技能) | 反思 | >=3 层推演 + >=2 方案 + 因果链 | 500 字反思 + tutorial 口头辩护 |

> 借鉴 MIT 6.5940 mastery 阈值: "至少 4/5 实验提交方可及格"。本单元要求 D1/D2/D3 三 drill 各连续 3 次达标 (reps_required=3), 加天道推演反思达标, 方算 v6.0 收敛。

---

## 3 自检问题 (Biggs + Hattie Feed Up/Back/Forward)

> Biggs 建构对齐的核心三问 + Hattie (2007 RER 77(1):81-112) formative feedback 三级 (Feed Up 目标 / Feed Back 进展 / Feed Forward 下一步)。

### 1. Feed Up (目标清晰度) -- TLA 是否训练 ILO?
- **问**: practice.md drill D1 是否真的训练"CDP schema 设计"能力, 还是只是让学生抄 pydantic 模板?
- **自检**: 检查 D1 的 Stage 3 (独立解) 是否要求学生独立写 Segment + Profile 模型, 而非填空。若是填空, 则 TLA 未充分训练 ILO1, 需升级 Stage 3 难度。
- **改进**: 若发现 Stage 3 仍是填空, 改为"给定一段真实 Segment Track 事件 JSON, 从零写 Event 模型"。

### 2. Feed Back (进展反馈) -- AT 是否测量 ILO?
- **问**: solution.ipynb 的"CDP 可实例化"是否真的能区分学生会不会设计 CDP schema, 还是只要抄了 solution 就能过?
- **自检**: 检查 AT1 是否包含口头辩护环节 (tutorial 后测), 若只看 solution.ipynb 代码, 则学生可抄答案过关, AT 未真正测量 ILO1。
- **改进**: 在 AT1 加"用天道推演视角解释你为什么选 Segment Spec 而非自定义 schema"口头问, 强制学生辩护。

### 3. Feed Forward (下一步) -- 不经 TLA 能过 AT 吗? 若能 = 对齐失败!
- **问**: 如果学生跳过 tutorial.ipynb Socratic 追问, 直接抄 solution.ipynb, 能通过 AT 吗? 若能, 则对齐失败, ILO4 (天道推演) 形同虚设。
- **自检**: 模拟一个"只抄 solution 不上 tutorial"的学生, 看他能否通过 AT4 (天道推演反思)。若能写出 500 字套话反思过关, 则 AT4 需加"在 tutorial 中口头辩护 3 轮以上"硬性门槛。
- **改进**: 在 AT4 加"tutorial Socratic loop >=4 轮参与记录"作为前置条件, 无该记录则 AT4 不评分, 强制对齐。

---

## 与 v5.0 基线的衔接 (不破坏)

- v5.0 的 7 条验收 (notes.md 学习目标 / data README / starter TODO / solution 无 scaffold / notebook 化 / reading 深链 / 2026 前沿) **全部保留**, 本文件仅在其上加建构对齐层。
- ILO1-3 对应 v5.0 的学习目标 1-3 (CDP / TOGAF / 行动研究), ILO4 对应学习目标 5 (天道推演×企业架构)。
- mastery_threshold 不替代 v5.0 的 5 分制量表, 而是补充"达标/未达标"二元判断 (CS230 retry 风格)。

---

## 反馈来源 (feedback_rule 真实依据)

- **Biggs 建构对齐**: Biggs, J. (1996) "Enhancing teaching through constructive alignment" Higher Education 32(3):347-364
- **Hattie 四级 formative feedback**: Hattie, J. & Timperley, H. (2007) "The Power of Feedback" Review of Educational Research 77(1):81-112
- **MIT 6.5940 mastery**: "至少 4/5 实验提交方可及格" -- 阈值化评估
- **天道推演**: 项目 CLAUDE.md 「天道推演系统」-- 局势感知/因果链/沙盘模拟/概率评估/最优路径
- **Segment Spec**: https://segment.com/docs/spec/ -- CDP 数据模型行业事实标准
- **TOGAF**: https://pubs.opengroup.org/architecture/togaf9-doc/ -- ADM 四层架构域
- **Susman & Evered (1978)**: Administrative Science Quarterly 23(4):582-603 -- 行动研究五步螺旋

---

*v6.0 学习科学层 · Biggs Constructive Alignment + Hattie 4-Level Feedback + MIT mastery threshold · 2026-07-25*
