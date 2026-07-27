# practice.md - 刻意练习 (Ericsson + MIT 4C/ID) · Day 4 企业级架构+行动研究

> v6.0 学习科学层 · 配合 `starter.ipynb` / `solution.ipynb` / `tutorial.ipynb` / `schedule.json` / `alignment.md`
> 哲学: 科学即高效 · 反馈即成长 -- 用 Ericsson 刻意练习 5 要素 + MIT 提取练习/交叉/渐退示例 把"上机"升级为"刻意练习"

---

## skill_target (本单元核心可观察技能)

能用 **pydantic + networkx + pandas** 独立设计企业级 AI 原生参考架构（CDP 四层 schema + TOGAF 四层依赖图 17 节点 27 边 + 行动研究 4 轮 KPI 闭环），并能用**天道推演**视角对架构选型做 3 层沙盘推演与口头辩护。

---

## diagnostic (前测 · 3 道 · 不计分但强制提交, 用于定位起点)

> 提取练习 (retrieval practice) -- Butler (2010): 推断题 68% vs 重学 44%。前测不是为了打分, 是为了激活先验知识 + 诊断概念缺口。

- **Q1 (CDP)**: 给定一段 Segment Identify 事件 JSON `{"userId":"u123","traits":{"email":"a@b.com"},"context":{"ip":"1.2.3.4"}}`, 请用 pydantic 写出对应的 `Identity` 模型, 字段类型必须严格匹配 Segment Spec (https://segment.com/docs/spec/identify/)。
- **Q2 (TOGAF 依赖图)**: 给定三节点架构图 `CDP事件层 → Agent编排 → 营销报表`, 问有几条依赖路径? 若 `CDP事件层` 故障, 下游因果链有几跳? 最大瓶颈在哪?
- **Q3 (行动研究 KPI)**: 给定 4 轮行动研究 KPI 数据 (决策时间/决策质量/团队满意度/AI使用率), 问 Plan→Act→Observe→Reflect 各阶段的改善幅度分别是多少? 哪一轮改善最大?

> 诊断结果写入 `student_model.json` 的 `diagnostic_scores` 字段, 决定 drill 起点难度。

---

## subskills (3 项子技能, 对应 ILO1/ILO2/ILO3)

- **S1 · CDP schema 设计**: 用 pydantic 建模 Identity/Event/Segment/Profile 四层, 基于真实 Segment Spec, 理解 CDP 作为"AI 数据基础设施"的角色
- **S2 · 企业架构依赖图建模**: 用 networkx DAG 建模 TOGAF 四层 (业务/应用/数据/技术), 17 节点 27 边, 识别关键依赖路径与单点故障
- **S3 · 行动研究 KPI 分析**: 用 pandas 分析 Susman & Evered (1978) 五步螺旋 (诊断/规划/行动/评估/反思) 的 4 轮 KPI, 计算改善幅度, 排除霍桑效应

---

## drills (3 个刻意练习, 每 drill 含 difficulty / reps_required / feedback_rule / worked_faded)

### drill_id: D1 · CDP 四层 schema (pydantic + Segment Spec)
- **difficulty**: 3
- **reps_required**: 3
- **feedback_rule**: 若 pydantic 模型字段类型错误或缺失 validator, 引用 Segment Spec (https://segment.com/docs/spec/identify/ 与 https://segment.com/docs/spec/track/) 让学生重读 required fields; 若 CDP 四层关系混淆 (Identity/Event/Segment/Profile 层级颠倒), 引用独立教材 § Day 4 "CDP 在 AI 原生架构中的角色" 四点 (向量化/实时流/知识图谱/AI 激活), 追问"你这个 schema 缺 Profile 向量化字段, Agent 怎么做语义匹配?"
- **worked_faded** (三阶段渐退示例, Worked-Faded):
  - Stage 1 (完整示范): 给出 `Identity` 模型完整 pydantic 代码, 含 `user_id: str`, `traits: dict`, `context: dict`, `timestamp: datetime`, `@field_validator` 校验 user_id 非空
  - Stage 2 (部分填空): 给出 `Event` 模型骨架, 抽掉 `context.ip` 字段和 `event_type` 的 validator, 学生填空
  - Stage 3 (独立解): 学生独立写 `Segment` (含 `conditions: list[dict]`) 和 `Profile` (含 `embedding: list[float]`) 模型

### drill_id: D2 · TOGAF 四层依赖图 (networkx DAG 17 节点 27 边)
- **difficulty**: 4
- **reps_required**: 3
- **feedback_rule**: 若 networkx 图节点少于 12 或层级混淆 (如把"伦理审查委员会"放应用层), 引用 TOGAF ADM (https://pubs.opengroup.org/architecture/togaf9-doc/arch/chap28.html) 让学生重画业务/应用/数据/技术四层分区; 若未识别关键路径, 追问"用 nx.topological_sort 找一条从'CDP事件层'到'营销报表'的最长路径, 这条路径上任何一个节点故障, 整个架构会怎样? 画出因果链"; 若与天道推演脱节, 追问"你这 17 节点图里, 哪个节点是高杠杆点 (小投入改变大局)?"
- **worked_faded**:
  - Stage 1 (完整示范): 给出 17 节点 27 边完整 networkx DAG 代码, 含四层 partition dict, `nx.draw` with layer colors, `nx.topological_sort` 输出关键路径
  - Stage 2 (部分填空): 抽掉 5 条关键边 (如 `CDP事件层→Agent编排`), 给节点列表让学生补边并标注依赖类型 (数据流/控制流/治理流)
  - Stage 3 (独立解): 学生独立设计自己的营销中心架构依赖图, 要求 >=12 节点, 四层分区正确, 输出关键路径与单点故障分析

### drill_id: D3 · 行动研究 KPI 分析 (pandas + Susman 五步螺旋)
- **difficulty**: 3
- **reps_required**: 3
- **feedback_rule**: 若学生只用均值不画趋势线或漏掉 Reflect 阶段改善幅度, 引用 Susman & Evered (1978) 五步螺旋 (诊断/规划/行动/评估/反思) 追问"第 3 轮 Observe 到第 4 轮 Reflect 的 KPI 变化说明了什么干预效果? 是真实改善还是霍桑效应?"; 若未排除混淆变量, 追问"你这 4 轮 KPI 提升, 凭什么是 AI 系统的贡献而不是同期市场环境变好? 怎么用 DML (双重机器学习) 或合成控制法归因?"; 若未与 DSR artifact 衔接, 追问"你的行动研究结论如何反哺架构 artifact 的下一轮设计?"
- **worked_faded**:
  - Stage 1 (完整示范): 给出 pandas 完整分析 4 轮 KPI 代码, 含 `df.groupby('phase')['kpi'].agg(['mean','std'])`, 趋势图 matplotlib, 改善幅度 `(last-first)/first*100%`
  - Stage 2 (部分填空): 给 2 轮 KPI 数据 + 代码骨架, 学生算剩余 2 轮改善幅度并画趋势线
  - Stage 3 (独立解): 学生独立设计自己的行动研究 KPI 追踪表 (>=4 轮, >=4 个 KPI), 输出改善幅度 + 霍桑效应排除论证

---

## progressive_project (渐进式项目脚手架, MIT Sloan 行动学习风格)

营销中心 AI 原生参考架构完整设计 -- 三阶段递进交付, 每阶段对应一个 drill 产出:

- **Stage 1 (D1 产出)**: CDP 四层 schema 可实例化 -- pydantic 模型能 `model_validate_json` 一段真实 Segment 事件
- **Stage 2 (D2 产出)**: 加上 TOGAF 四层依赖图 17 节点 27 边 -- networkx DAG 能输出关键路径与单点故障
- **Stage 3 (D3 产出)**: 加上 4 轮行动研究 KPI 闭环分析 -- pandas 趋势图 + 改善幅度 + 霍桑效应排除

**最终交付** = 完整参考架构 (ASCII + networkx 图) + 行动研究计划 (Susman 五步) + 天道推演 500 字反思 (含 3 层沙盘推演 + 2-3 方案对比 + 因果链描述)

> 与 starter.ipynb 的 6 个 TODO 对应: TODO1-3=Stage1, TODO4-5=Stage2, TODO6=Stage3

---

## interleaving (交叉练习 A1B1C1...A2B2C2...A3B3C3, 不块状)

> MIT Open Learning: 交叉练习 (interleaving) A1B1C1...B2C2A2...C3A3B3 模式比块状练习提升 40% 迁移表现。本单元强制交叉, 不允许"先练完所有 CDP 再练架构图"。

- **A = CDP schema (S1)**, **B = TOGAF 依赖图 (S2)**, **C = 行动研究 KPI (S3)**
- **A1** = CDP-Identity 简单 (单模型 5 字段) / **B1** = networkx 三节点图 (CDP→Agent→报表) / **C1** = pandas 单轮 KPI (4 个指标)
- **A2** = CDP-Event + Segment (含 validator) / **B2** = TOGAF 四层 12 节点 / **C2** = pandas 4 轮 KPI + 改善幅度
- **A3** = CDP-Profile + 完整四层 schema / **B3** = 17 节点 27 边完整图 / **C3** = 行动研究五步螺旋反思 + 霍桑效应排除

**强制顺序**: A1 → B1 → C1 → A2 → B2 → C2 → A3 → B3 → C3 (每两次 drill 之间间隔 >=1 小时, 利用间隔重复 + 提取练习效应)

> 不允许块状: A1→A2→A3→B1→B2→B3→C1→C2→C3 是**错误**练法, 会造成短期记忆假象, 迁移测试时崩盘。

---

## retry_policy (重试策略, Stanford CS230 风格)

- **单次 drill 失败**: 24 小时后重试 (间隔效应, 避免短期记忆假象; 不允许立即重试)
- **任一 drill 连续 2 次失败**: 触发 `weak_loop` (见下)
- **全单元 3 次 drill 失败累计**: 回退到 `diagnostic` 重测, 定位概念缺口, 必要时回看 Day 1 (架构基础) / Day 2 (Agent 编排) / Day 3 (人机协作治理)
- **late penalty**: 借鉴 CS230 的 10 late days + 20%/天罚分, 但本单元以"掌握"而非"按时"为目标, 不罚分但触发 weak_loop

---

## weak_loop (弱项循环, 连续 2 次失败触发)

> Ericsson: 刻意练习的核心是"在弱项上反复刻意练习, 而非在强项上重复舒适区"。

触发条件: 任一 drill 连续 2 次未达 mastery_threshold (见 alignment.md)

执行步骤:
1. **回退**: 回退到上一难度 drill (D3→D2, D2→D1, D1→回看 Day 1 starter.ipynb)
2. **重做 worked example**: 重做该 drill 的 Stage 1 (完整示范), 不是 Stage 2 (faded), 更不是 Stage 3 (独立解) -- 重新建立正确心理模型
3. **天道推演反思问**: 补充 1 个因果链反思问, 例如:
   - "你的 CDP schema 在数据层缺一个 Profile.embedding 字段, 会导致应用层 Agent 的什么决策失败? 画出从 Profile 缺失 → 向量检索失败 → Agent 推荐不准 → 营销效果下降 → 团队失去信心的完整因果链"
   - "你的 TOGAF 依赖图把'伦理审查委员会'放错层, 3 年后公司扩张 3 倍, 这个错误会导致什么连锁反应?"
4. **再 faded → 独立解**: 通过 worked example 后, 回到 Stage 2 → Stage 3, 直到 mastery_threshold 达标

> weak_loop 不计入 reps_required, 但 reps_required 必须在 weak_loop 之后再独立完成 3 次才算掌握。

---

## 反馈来源引用 (feedback_rule 真实依据)

- **CDP schema**: Segment Spec (https://segment.com/docs/spec/) -- Identify/Track/Page/Screen 标准事件
- **pydantic**: https://docs.pydantic.dev/latest/ -- field_validator / model_validator
- **TOGAF**: https://pubs.opengroup.org/architecture/togaf9-doc/arch/ -- ADM 四层架构域
- **networkx**: https://networkx.org/documentation/stable/reference/algorithms/dag.html -- topological_sort / longest_path
- **行动研究**: Susman & Evered (1978) "An Assessment of the Scientific Merits of Action Research" Administrative Science Quarterly 23(4):582-603
- **天道推演**: 项目 CLAUDE.md 「天道推演系统」-- 局势感知/因果链追踪/沙盘模拟/概率评估/最优路径推荐

---

*v6.0 学习科学层 · Ericsson 刻意练习 + MIT 4C/ID 认知负荷 + Butler 提取练习 + Stanford CS230 retry · 2026-07-25*
