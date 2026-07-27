# U5D7 · Capstone整合 · 建构对齐 (v6.0 学习科学层)

> 依据：Biggs (1996) Constructive Alignment -- ILO↔TLA↔AT 三者对齐；mastery learning (Bloom 1968) 阈值；Hattie & Timperley (2007) 三级反馈 Feed Up / Feed Back / Feed Forward。
> 配套：[`notes.md`](./notes.md)（ILO 原文）· [`practice.md`](./practice.md)（drill 与 worked-faded）· [`tutorial.ipynb`](./tutorial.ipynb)（Socratic + Hattie 四级）· [`starter.ipynb`](./starter.ipynb) / [`solution.ipynb`](./solution.ipynb)

---

## ILO ↔ TLA ↔ AT 矩阵（Biggs 建构对齐）

> ILO = Intended Learning Outcome（预期学习产出，源自 `notes.md` 学习目标 1-4）
> TLA = Teaching/Learning Activity（教学学习活动，引用 starter/drill/tutorial）
> AT  = Assessment Task（评估任务，引用 solution/tutorial 后测）
> mastery_threshold = 通过阈值（Bloom mastery，>=80% 视为掌握）

| ILO | TLA（训练 ILO 的活动） | AT（测量 ILO 的任务） | mastery_threshold |
|-----|----------------------|---------------------|-------------------|
| **ILO1**：能用 DSR 六步框架（Hevner 2004 / Peffers 2007）规划 Capstone，把工程实践转化为可发表的设计科学贡献 | `starter.ipynb` TODO1（DSR 系统设计填空）+ `practice.md` Drill D1 worked-faded（worked->faded->independent 三阶段）+ `tutorial.ipynb` cell3 Socratic 追问"Step2 目标定义如何量化" | `solution.ipynb` TODO1 六步映射表逐行比对 + `tutorial.ipynb` 后测：口头复述六步并给出每步的 Capstone 落点 | >=80%（六步全列、顺序无误、Step6 含 ICIS/DSS/HICSS 三选一理由） |
| **ILO2**：能把技能1-5 整合为端到端流水线（causaldata NSW -> DoWhy ATE -> LangGraph 营销 Agent -> deepeval -> IMRaD） | `starter.ipynb` TODO2-5（数据/因果/Agent/评估填空）+ `practice.md` Drill D2 worked-faded（NSW->DoWhy->LangGraph 接线）+ Drill D4 worked-faded（天道推演×多Agent仿真同构） | `solution.ipynb` TODO2-5 端到端跑通 + `tutorial.ipynb` cell3 Socratic 追问"条件边为什么不能是无条件边" + deepeval 评估报告（BaseMetric 引用工具轨迹） | >=80%（ATE 估计正确 + 条件边分支显式 + Agent 输出 grounded 于因果证据） |
| **ILO3**：能用 IMRaD 结构写 3000-5000 字 Capstone 论文草稿，含 DSR artifact 描述，并制定学术发表路线图 | `starter.ipynb` TODO6（论文草稿填空）+ `practice.md` Drill D3 worked-faded（deepeval->IMRaD）+ `notes.md` 关键回顾 3（IMRaD+DSR 映射表） | `solution.ipynb` TODO6 IMRaD 草稿 + `tutorial.ipynb` Hattie 四级反馈对草稿打分 + 一页投稿计划（ICIS/DSS/HICSS 选一） | >=80%（IMRaD 四段齐全 + Methods↔Step3 / Results↔Step5 对齐 + 投稿目标有理由） |
| **ILO4**：能理解天道推演×多Agent仿真的同构关系，作为 Capstone 的特色理论视角 | `notes.md` 2026前沿章节（五对同构表）+ `practice.md` Drill D4 worked-faded + `tutorial.ipynb` cell3 Socratic 追问"沙盘模拟↔多Agent场景模拟的代码落点在哪" | `tutorial.ipynb` 后测：在 Discussion 段写五对同构 + DSR 互补句 + `solution.ipynb` Discussion 段评分 | >=80%（五对同构各有代码/数据落点 + 双框架互补句完整） |

---

## mastery_threshold（Bloom mastery learning）

- **单 drill mastery**：independent 阶段 >=80% 视为掌握，未达则触发 `practice.md` weak_loop。
- **单 ILO mastery**：该 ILO 的所有 AT 均 >=80%。
- **单元 mastery（过关）**：4 个 ILO 全部 master + Capstone 论文草稿 IMRaD 四段齐全 + 端到端流水线跑通（`solution.ipynb` 6 个 TODO 全过）。
- **未达 mastery 的后果**：不挂科，触发弱项循环（见 `practice.md` weak_loop），可重做；连续 2 次失败回退 worked 阶段 + 补充 worked example。

---

## 3 自检问题（Hattie Feed Up / Feed Back / Feed Forward）

> 建构对齐的三级自检。任一答"否"即对齐失败，需回炉 TLA 或 AT。

### 自检 1 · Feed Up（TLA 是否训练 ILO？--活动与产出是否对齐）

**问题**：`starter.ipynb` 的 TODO1-6 + `practice.md` 的 Drill D1-D4 + `tutorial.ipynb` 的 Socratic 追问，是否真的训练了 ILO1-4 所声明的产出？

- TODO1/D1 -> ILO1（DSR 六步）：是。填空+worked-faded 直接训练"用 DSR 规划 Capstone"。
- TODO2-5/D2 -> ILO2（端到端流水线）：是。NSW->DoWhy->LangGraph->deepeval 逐层接线。
- TODO6/D3 -> ILO3（IMRaD 论文）：是。drill 的 independent 阶段即草稿写作。
- D4 + 2026前沿 -> ILO4（天道推演同构）：是。五对同构映射训练 Discussion 写作。

**结论**：是。所有 TLA 均有对应 ILO，无"训练了但没考"或"考了但没训练"。

### 自检 2 · Feed Back（AT 是否测量 ILO？--评估与产出是否对齐）

**问题**：`solution.ipynb` 的 TODO1-6 + `tutorial.ipynb` 后测 + deepeval 评估报告，是否真的测量了 ILO1-4 所声明的产出，而非测量别的东西？

- solution TODO1 比对六步映射表：测量 ILO1（DSR 规划能力），非测量"背书"。
- solution TODO2-5 端到端跑通 + deepeval：测量 ILO2（流水线整合），非测量"单层代码"。
- solution TODO6 IMRaD 草稿 + 投稿计划：测量 ILO3（论文写作+发表），非测量"格式排版"。
- tutorial 后测 Discussion 五对同构：测量 ILO4（同构视角），非测量"哲学名词"。

**结论**：是。所有 AT 均直测 ILO，mastery_threshold >=80% 可操作。

### 自检 3 · Feed Forward（不经 TLA 能过 AT 吗？--若能，对齐失败）

**问题**：假设一个学生完全跳过 TLA（不做 starter TODO、不做 drill、不上 tutorial），他能通过 AT 吗？如果能，说明 AT 没有真正依赖 TLA 的训练，对齐失败。

- 跳过 TODO1/D1 能过 solution TODO1 吗？--不能。DSR 六步映射需要 Hevner 2004 / Peffers 2007 的框架知识，不读 notes/practice 无法正确排序。
- 跳过 TODO2-5/D2 能过端到端跑通吗？--不能。DoWhy API + LangGraph 条件边需要上机练习，无练习无法写出能跑的代码。
- 跳过 TODO6/D3 能过 IMRaD 草稿吗？--勉强能写"格式像"的草稿，但 Methods↔Step3 / Results↔Step5 的 DSR 对齐会缺失，达不到 >=80% mastery。
- 跳过 D4/2026前沿能过 Discussion 五对同构吗？--不能。五对同构表在 notes.md，不读无法写出代码落点。

**结论**：不能。不经 TLA 无法过 AT，对齐成立。Feed Forward 行动：保持 TLA 的 worked-faded 三阶段强制顺序，禁止学生直接跳到 independent。

---

*本文件遵循 Biggs (1996) 建构对齐原则：ILO 决定 TLA，TLA 决定 AT，AT 回测 ILO。所有 TLA/AT 引用均指向本单元真实文件（starter/solution/practice/tutorial/notes）。*
