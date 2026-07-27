# U5D7 · Capstone整合 · 刻意练习 (v6.0 学习科学层)

> 所属：AI原生化商业博士 · 技能5 Agentic系统工程与落地 · Day 7（收官）
> 学习科学依据：Ericsson deliberate practice / MIT CS229 pset0 diagnostic / CS230 progressive project / Harvard STP worked-faded / Stanford interleaving
> 配套：[`notes.md`](./notes.md) · [`starter.ipynb`](./starter.ipynb) · [`solution.ipynb`](./solution.ipynb) · [`tutorial.ipynb`](./tutorial.ipynb) · [`alignment.md`](./alignment.md) · [`schedule.json`](./schedule.json)

---

## skill_target

**一句话可评估的核心技能**：能在 4 小时内，独立用 **DSR 六步框架**（Hevner 2004 / Peffers 2007）把技能1-5 整合为端到端 Capstone——`causaldata NSW RCT → DoWhy ATE → LangGraph 营销策略 Agent → deepeval (BaseMetric + GEval) → IMRaD 草稿`——并产出可复现的 DSR artifact 描述与天道推演×多Agent仿真 Discussion 锚点。

---

## diagnostic（先测，CS229 pset0 式，探测先验缺口）

> 3 道题，每题 ≤90 秒。做完先不查答案，对照 `solution.ipynb` 自评。错题即为你本次 Capstone 的弱项起点。

**DQ1（DSR 框架序）**：把以下 6 项按 Peffers et al. (2007) DSR 六步的正确顺序排列：评估 / 演示 / 问题识别 / 设计开发 / 目标定义 / 传播。

**DQ2（因果层定义）**：给定 NSW 数据集，`treat`/`re75`/`re78` 三个字段在 Capstone 营销映射中分别对应什么角色？DoWhy 估计的 ATE 在数学上回答了哪个反事实问题？

**DQ3（Agent 层接线）**：一个 LangGraph `StateGraph` 至少需要哪几类节点才能把 DoWhy 因果证据"喂"给营销策略 Agent？相邻节点之间的边为什么必须是条件边（conditional edge）而非无条件边？

---

## subskills（3 个子技能，对齐 ILO1-3）

- **S1 · DSR 框架应用**：把工程项目（6 个 TODO）翻译为可发表的 DSR artifact 贡献（问题→目标→设计→演示→评估→传播）。
- **S2 · 端到端流水线整合**：把 causaldata/DoWhy/LangGraph/deepeval 四层用真实数据接通，而非孤立练习。
- **S3 · 论文写作与发表**：用 IMRaD 结构 + DSR artifact 描述写 3000-5000 字草稿，并选定 ICIS / Decision Support Systems / HICSS 投稿路线。

---

## drills（4 个，每个含 drill_id / difficulty / reps_required / feedback_rule / worked_faded）

> Worked-Faded 三阶段（Harvard STP）：完整示范（worked）→ 部分填空（faded）→ 独立解（independent）。每个 drill 的 feedback_rule 引用本单元真实库/数据集，禁用通用模板话术。

drill_id: D1
title: DSR 六步映射 Capstone
difficulty: 3
reps_required: 4
subskill: S1
feedback_rule: 用 `solution.ipynb` TODO1 的六步映射表逐行比对；任一步骤与"营销场景映射表"冲突即标红；传播步必须同时给出 ICIS/DSS/HICSS 三选一及其理由，否则反馈"传播步缺投稿锚点"。
worked_faded:
  - worked: 完整示范——把 starter TODO1 的"NSW 营销 Agent"映射到 DSR 六步，每步配一句 artifact 描述。
  - faded: 部分填空——给出 Step1/Step3/Step5 的答案，学生补 Step2/Step4/Step6。
  - independent: 独立解——换一个数据集（如 causaldata 的 `lmbdata`），重做六步映射。

drill_id: D2
title: 因果层 + Agent 层接线（NSW → DoWhy → LangGraph）
difficulty: 4
reps_required: 5
subskill: S2
feedback_rule: DoWhy 输出的 ATE 必须作为 LangGraph Agent 的工具返回值被下一个节点读取，否则反馈"因果证据未进入 Agent 决策"；条件边 `should_generate_strategy` 必须显式分支（`|ate| > 0`），否则反馈"无条件边=硬编码策略，违背 Agent 性"；Agent 输出必须含对 ATE 的文字引用，否则反馈"Agent 未 grounded 在因果证据上"。
worked_faded:
  - worked: 完整示范——`estimate_ate(treat, re78, covariates)` → `build_marketing_agent(ate)` 全链打通。
  - faded: 部分填空——给出 DoWhy 估计代码，学生补 LangGraph 的 `add_node` / `add_conditional_edges`。
  - independent: 独立解——把 outcome 从 `re78` 换成自定义转化率字段，重跑端到端。

drill_id: D3
title: 评估层 + 论文草稿（deepeval → IMRaD）
difficulty: 4
reps_required: 5
subskill: S3
feedback_rule: 自定义 `BaseMetric` 必须在 `measure()` 里引用 Agent 的工具调用轨迹，否则反馈"评估的不是 Agent 而是 LLM 文本"；GEval 的 criteria 必须含"因果 grounded 度"，否则反馈"评估器无法区分 grounded 策略与幻觉"；IMRaD 草稿的 Methods 必须映射 DSR Step3、Results 映射 Step5，否则反馈"论文未做 DSR 对齐"。
worked_faded:
  - worked: 完整示范——`class CausalGroundedMetric(BaseMetric)` + GEval criteria + IMRaD Methods 段。
  - faded: 部分填空——给出 BaseMetric 骨架与 IMRaD Methods，学生补 GEval criteria 与 Results。
  - independent: 独立解——新增一个"天道推演对齐度"自定义 Metric，并写进 Discussion。

drill_id: D4
title: 天道推演 × 多Agent仿真 同构映射（特色 Discussion）
difficulty: 5
reps_required: 3
subskill: S1+S3
feedback_rule: 五对同构（局势感知/因果链追踪/沙盘模拟/概率评估/最优路径）必须每一对都给出 Capstone 中的具体代码或数据落点（如"沙盘模拟↔多Agent场景模拟"对应 LangGraph 的并行 branch），否则反馈"同构悬空=哲学贴标签"；Discussion 必须说清 DSR 评估"系统好不好"与天道推演评估"策略路径优不优"的互补关系，否则反馈"双框架未叠加"。
worked_faded:
  - worked: 完整示范——五对同构表 + Discussion 段落（含 DSR 互补句）。
  - faded: 部分填空——给出三对同构，学生补两对 + 互补句。
  - independent: 独立解——把同构视角从营销迁移到采购/运营场景，重写 Discussion。

---

## progressive_project（CS230 式 proposal → milestone → final → poster）

> 把 6 个 TODO 升级为四阶段渐进交付，每阶段有明确 artifact 与 rubric。

| 阶段 | 对应 TODO | 交付物 | rubric 要点 |
|------|----------|--------|------------|
| **Proposal** | TODO1 (DSR) | 1 页 DSR 六步 + 研究问题 + 投稿目标 | Step1/2 完整、投稿目标有理由 |
| **Milestone** | TODO2-3 (数据+因果) | NSW 数据加载 + DoWhy ATE 估计 + 反事实 | ATE 显著性 + 反事实解读 |
| **Final** | TODO4-5 (Agent+评估) | LangGraph Agent + deepeval 评估报告 | 条件边正确 + BaseMetric 引用工具轨迹 |
| **Poster** | TODO6 (论文) | IMRaD 草稿 3000-5000 字 + 1 页海报 | Methods↔Step3 / Results↔Step5 对齐 |

---

## interleaving（交叉排布，非块状）

> 三类子技能 A=DSR / B=流水线 / C=论文，按 A1B1C1 → B2C2A2 → C3A3B3 交叉，避免块状死练。

```
Day 7 上午 block1:  A1(D1-worked) → B1(D2-worked) → C1(D3-worked)
Day 7 下午 block2:  B2(D2-faded)  → C2(D3-faded)  → A2(D1-faded)
Day 7 晚间 block3:  C3(D3-independent) → A3(D1-independent) → B3(D2-independent)
加餐（可选）:        D4-worked → D4-faded → D4-independent（天道推演同构，贯穿三 block）
```

明文交叉顺序：`A1 → B1 → C1 → B2 → C2 → A2 → C3 → A3 → B3`（A/B/C 各出现 3 次，相邻不同类，杜绝块状）。

---

## retry_policy（CS230 式，降低试错心理代价）

- **10 free late days**：全 Capstone 周期可用，不罚分；鼓励"先跑通再优化"。
- **失败重试不罚分**：任一 drill 的 independent 阶段未达 mastery（<80%），可重做；重做通过即记满分，不累计扣分。
- **Milestone 可回退**：Milestone 未过可回退到 Proposal 修订，不算"挂科"。

---

## weak_loop（连续 2 次失败触发弱项循环）

> 监测信号：任一 drill 的 independent 阶段连续 2 次未达 80%。

**触发后**：
1. 回退到该 drill 的 `worked` 阶段重看完整示范（不是重做 faded）。
2. 补充一份 worked example：导师在 `solution.ipynb` 里对该 drill 做一次"出声思考"（think-aloud），录制 3-5 分钟解说。
3. 学生复述 worked example 的关键决策点（口头 retrieval，不是重读）。
4. 重新进入 `faded` 阶段，faded 的填空比例从 50% 降到 30%（更接近 worked）。
5. 通过后再回 `independent`；若再失败 2 次，触发 1-on-1 tutorial（见 `tutorial.ipynb`）。

**典型弱项映射**：
- D1 连败 → DSR 框架不熟 → 复习 `notes.md` 关键回顾 2 + reading.md 的 Hevner 2004 条目。
- D2 连败 → DoWhy/LangGraph 接线断层 → 回退到 Day 2（LangGraph）+ Day 3（DoWhy）的 schedule.json 卡片重排。
- D3 连败 → deepeval/IMRaD 写作 → 回退到 Day 6（IMRaD）+ Day 3（deepeval）。
- D4 连败 → 天道推演同构悬空 → 重读 `notes.md` 2026前沿章节 + 项目 CLAUDE.md 天道推演矩阵。

---

*本文件遵循 Ericsson 刻意练习四原则：特定子技能 / 即时反馈 / 重复 / 难度递进。所有 feedback_rule 均引用本单元真实库（causaldata NSW / DoWhy / LangGraph StateGraph / deepeval BaseMetric+GEval / IMRaD+DSR）。*
