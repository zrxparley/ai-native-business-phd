---
unit: capstone-phase-1
unit_topic: "Capstone阶段1: 问题定义+文献综述 (DSR框架 + PRISMA + arxiv/pydantic/pandas/matplotlib + 天道推演路径选择)"
skill_target: "能用DSR框架+pydantic Schema把模糊研究想法转化为可验证的artifact定义，并用arxiv/pandas执行PRISMA四步流程，从真实arXiv文献中识别2-3个研究空白"
version: v6.0
---

# 刻意练习 · Capstone Phase 1：问题定义与文献综述

> 基于 Ericsson deliberate practice + MIT/Harvard/Stanford 工程博士训练范式。本单元 drills 引用真实 arXiv API + pydantic Schema + pandas 文献计量 + matplotlib PRISMA 流程图 + 天道推演沙盘。

## diagnostic（先测 · CS229 pset0 式 · 探测先验缺口）

回答以下 3 题（不查资料，5 分钟内作答）：

1. **PRISMA 流程排序**：给定 4 个步骤「Quality Assessment / Identification / Synthesis / Screening」，按 PRISMA 国际标准正确顺序排列。并解释为什么 Screening 必须在 Quality Assessment 之前。
2. **DSR artifact 类型识别**：给定三段描述（a）一个 Agent 框架（b）一个评估方法论（c）一个实证 case study，哪几个属于 DSR 意义上的 artifact？为什么？请引用 Hevner et al. 2004 的 7 条指南中至少 2 条。
3. **贝叶斯路径选择**：天道推演给出 3 条研究路径沙盘，先验成功概率分别为 0.4/0.3/0.3。你在 arXiv 检索后观察到第 1 条路径有 8 篇相关论文、第 2 条 3 篇、第 3 条 1 篇。若把"相关论文数"视为弱证据（似然比 2:1:0.5），写出后验分布并说明你选哪条路径。

> 评分：3/3=可跳过 drill-1 的 worked 阶段直接进 faded；2/3=按正常节奏走；<=2/3=必须完整做 worked 阶段 + 补充阅读 reading.md 中 DSR/PRISMA 条目。

## subskills（拆 3 个子技能）

- **S1 DSR 问题定义**：用 pydantic 把模糊营销问题转化为有结构化 Schema 的研究问题定义书（problem_identification / solution_objectives / artifact_description / expected_contribution 四字段类型约束）。
- **S2 PRISMA 文献综述**：用 arxiv 包查询真实 arXiv API + pandas 去/筛/纳入 + matplotlib 画带真实数字的 PRISMA 流程图。
- **S3 研究空白识别 + 天道推演路径选择**：用 pandas 文献计量统计按年份/研究维度，识别 2-3 个 gap；用天道推演沙盘展开 3 条研究路径 × 3 层（immediate/near/far），用贝叶斯更新选最优路径。

## drills（>=3 个 · 每个 worked_faded 三阶段）

### drill-1: pydantic DSR Schema 构造
- drill_id: D1
- difficulty: 3
- reps_required: 3
- skill: S1
- feedback_rule: 验证 Schema 必含 4 字段 (problem_identification / solution_objectives / artifact_description / expected_contribution) 且每字段有 pydantic Field(min_length=10) 约束；实例化 Capstone 研究问题（"AI 营销 Agent 系统因果评估"）必须通过 model_validate。失败提示"哪个字段类型约束没生效？回看 Hevner 2004 第 1-2 条指南"。
- worked_faded:
  - **Worked（完整示范）**：教师演示完整 ResearchQuestionSchema pydantic 类 + 实例化 Capstone 主题 + model_validate 通过。
  - **Faded（部分填空）**：给出 ResearchQuestionSchema 骨架，4 个字段类型留空，学生填 `Field(...)` 约束并实例化。
  - **Independent（独立解）**：学生从零写 Schema + 实例化另一个研究主题（如"表示工程×营销知识图谱"）。

### drill-2: arxiv + pandas PRISMA 四步
- drill_id: D2
- difficulty: 4
- reps_required: 4
- skill: S2
- feedback_rule: 检查 PRISMA 四步数字链 identification→screening→quality→synthesis 必须单调递减且每步记录前后数；arxiv.Search(query="AI marketing agent") 必须真实返回 >=10 条；pandas 去重按 title hash；matplotlib 流程图框中数字必须等于 DataFrame len()。失败提示"你的筛选标准是年份>=2023 + AI+营销相关性，回看 PRISMA 2020 Statement 第 2 阶段定义"。
- worked_faded:
  - **Worked**：教师演示 arxiv.Search + pandas.DataFrame 构建 + 去重 + 筛选 + matplotlib 4 框流程图（带真实数字）。
  - **Faded**：给出 arxiv 查询代码与 DataFrame 构建骨架，学生填去重逻辑（drop_duplicates subset=['title_hash']）+ 筛选条件 + PRISMA 流程图绘制。
  - **Independent**：学生换 query（如 "causal inference marketing"）独立完成 PRISMA 四步 + 流程图。

### drill-3: 研究空白 + 天道推演沙盘路径选择
- drill_id: D3
- difficulty: 5
- reps_required: 3
- skill: S3
- feedback_rule: gap analysis 必须基于 pandas groupby 统计（按年份/研究维度），识别 2-3 个 gap 必须有数字支撑（如"2023-2025 年 Agent×因果 0 篇 vs Agent 12 篇"）；天道推演沙盘必须展开 3 条路径 × 3 层（immediate Phase 2-3 / near Phase 4-5 / far Phase 6+发表），贝叶斯后验必须有数字（先验+似然比→后验）。失败提示"你的 gap 是定性陈述还是数字支撑？天道推演不是占卜，请补数字"。
- worked_faded:
  - **Worked**：教师演示 pandas groupby 识别 gap + 天道推演 3 路径沙盘 + 贝叶斯更新（先验 0.4/0.3/0.3 → 后验数字）。
  - **Faded**：给出 groupby 骨架与沙盘模板，学生填 gap 数字证据 + 贝叶斯似然比 + 后验计算。
  - **Independent**：学生换数据子集（如只看 2024 年论文）独立做 gap + 沙盘 + 贝叶斯路径选择。

## progressive_project（CS230 式渐进交付）

- **Proposal（Day 3）**：提交研究问题定义书（DSR Schema pydantic 实例，1 页 Markdown）→ tutor 给 [TASK] 反馈。
- **Milestone（Day 7）**：提交 PRISMA 文献综述 draft（>=15 篇真实 arXiv 论文 + 4 步流程图 + DataFrame 统计表）→ tutor 给 [PROCESS] 反馈。
- **Final（Day 14）**：提交完整文献综述报告（20-30 篇 + gap analysis + 天道推演 3 路径沙盘 + 贝叶斯后验）→ tutor 给 [FEED-FORWARD] 反馈。
- **Poster（Day 21）**：2 页 poster 展示研究问题 + PRISMA 流程图 + 3 条研究路径沙盘 + 最优路径选择 → 同伴互评（rubric 见 alignment.md AT-3）。

## interleaving（A1B1C1...B2C2A2...C3A3B3 交叉排布 · 不块状）

按以下顺序练习（每个数字=1 次 rep，1 天 1 次）：
- Day 1: D1-rep1 (S1 pydantic Schema)
- Day 2: D2-rep1 (S2 arxiv PRISMA)
- Day 3: D3-rep1 (S3 gap + 天道推演)
- Day 4: D1-rep2
- Day 5: D2-rep2
- Day 6: D3-rep2
- Day 7: D1-rep3
- Day 8: D2-rep3
- Day 9: D3-rep3
- Day 10: D2-rep4 (S2 难度最高，多 1 rep)

> 不块状：不在同一天连做 D1×3，避免"短期熟练度假象"。交叉促进迁移（interleaving enhances transfer, Rohrer 2012）。

## retry_policy（CS230 式）

- 10 free late days（全程 Phase 1 用完即止，不滚入 Phase 2）。
- 任何 drill 失败（未过 feedback_rule 验证）可重试，重试不扣分，仅记录尝试次数。
- Final 交付物未达 mastery（>=80%）可重交 1 次，取两次最高分。

## weak_loop（连续 2 次失败触发弱项循环）

- 触发条件：同一 drill 连续 2 次未过 feedback_rule。
- 动作：
  1. 回退到上一个 drill（如 D3 失败 → 回 D2 重做 1 rep）。
  2. 补充 1 个 worked example（教师重新演示该 drill 的 Worked 阶段，学生口述每行代码意图）。
  3. 重新尝试原 drill，直到过 feedback_rule。
- 记录：weak_loop 触发次数写入 tutorial.ipynb 的 student_model.json 的 `blind_spots` 字段。

---

*本 practice.md 基于 Ericsson deliberate practice + CS229/CS230 工程训练范式。drills 引用本单元真实库（arxiv/pydantic/pandas/matplotlib）与真实数据源（arXiv API），feedback_rule 域特定。*
