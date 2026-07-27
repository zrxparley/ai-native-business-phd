# U-R1 建构对齐矩阵（Biggs Constructive Alignment + Mastery Learning）

> Biggs (1996) 建构对齐原则：ILO（Intended Learning Outcomes）↔ TLA（Teaching/Learning Activities）↔ AT（Assessment Tasks）三者必须对齐。
> 每一行 AT 必须测量对应 ILO，TLA 必须训练对应 ILO。若学生不经过 TLA 也能过 AT，则对齐失败（Feed Forward 诊断）。
> 本矩阵锚定本单元真实数据集 causaldata NSW（445 样本, ATE=1794.34）与真实库 pydantic/pandas/LangGraph。

## ILO ↔ TLA ↔ AT 矩阵

| ILO（预期学习产出） | TLA（教学学习活动） | AT（评估任务） | mastery_threshold |
|---------------------|---------------------|----------------|-------------------|
| **ILO-1** 能解释 DSR 核心概念：March & Smith 四型 artifact、Hevner 七准则、Peffers 六步，并说明 DSR 与传统实证研究的根本区别（"如何构建" vs "是什么"） | 阅读 `notes.md` 理论部分 + 完成 `practice.md` 的 diagnostic 3 题先测 + `schedule.json` 5 张卡间隔重复（C1/C2/C3） + `tutorial.ipynb` 苏格拉底追问 | `tutorial.ipynb` cell2 pre-tutorial essay（提交一段 DSR 核心概念辨析）+ `schedule.json` 卡集 C1/C2/C3 答对率 | >=80% 卡片答对率 + essay 含四型/七准则/六步全部正确术语 |
| **ILO-2** 能用 pydantic 将 DSR 六步框架建模为结构化 artifact 规格 schema，把真实营销 Agent 系统实例化为 DSR artifact | `starter.ipynb` TODO1（schema 定义）+ TODO2（实例化）+ `practice.md` drill D1（worked-faded 三阶段）+ `tutorial.ipynb` cell3 苏格拉底反例追问 | `solution.ipynb` 对应 TODO1/TODO2 自动评分 + `practice.md` drill D1 independent 阶段通过（pydantic.validate 跑通） | >=80% TODO 通过 + pydantic schema 含 ArtifactType 枚举四型 + 营销 Agent 实例化引用 NSW 数据 |
| **ILO-3** 能用 pandas 结构化评估 artifact 是否满足 Hevner 七准则，理解 rigor vs design 核心张力 | `starter.ipynb` TODO3/TODO4（DataFrame + 评分）+ `practice.md` drill D2（worked-faded）+ `tutorial.ipynb` cell5 Hattie [TASK]/[PROCESS] 反馈 | `solution.ipynb` TODO3/TODO4 自动评分 + drill D2 independent 阶段 + 300 字分析"我的 artifact 哪条准则最弱" | >=80% TODO 通过 + DataFrame 7 行 4 列完整 + rigor/design 平衡分绝对值 < 1.5 |
| **ILO-4** 能区分"做一个系统"与"产出设计原则"，从 DSR Step 6 Communication 抽取可复用设计原则（principle/rationale/generalizability 三件套） | `starter.ipynb` TODO5（设计原则）+ TODO6（天道推演同构）+ `practice.md` drill D3（worked-faded）+ `tutorial.ipynb` cell5 [FEED-FORWARD] 反馈 | `solution.ipynb` TODO5/TODO6 自动评分 + drill D3 independent 阶段（>=4 条原则，至少 1 条可跨领域迁移） + poster 提交 | >=80% TODO 通过 + >=4 条原则三件套完整 + 至少 1 条迁移到非营销领域（如采购/R&D ClawBot） |

## 三自检问题（Feed Up / Feed Back / Feed Forward）

### 1. Feed Up: TLA 是否训练 ILO？
- ILO-1 的 TLA 是否覆盖"四型/七准则/六步"全部概念？答：是。`notes.md` 理论 + `practice.md` diagnostic + `schedule.json` C1/C2/C3 + `tutorial.ipynb` 苏格拉底追问四路并进。
- ILO-2 的 TLA 是否真的训练"pydantic schema 建模"？答：是。`starter.ipynb` TODO1/TODO2 + `practice.md` D1 worked-faded 三阶段，从完整示范到独立解。
- ILO-3 的 TLA 是否训练"pandas 七准则评估"？答：是。`starter.ipynb` TODO3/TODO4 + `practice.md` D2，feedback_rule 强制引用 NSW ATE=1794.34。
- ILO-4 的 TLA 是否训练"设计原则抽取"？答：是。`starter.ipynb` TODO5/TODO6 + `practice.md` D3，三件套强制 + 跨领域迁移。

### 2. Feed Back: AT 是否测量 ILO？
- AT-1 的 essay + 卡集答对率是否测量"概念解释"？答：是。essay 要求正确术语，卡集要求 recall。
- AT-2 的 `solution.ipynb` TODO1/TODO2 是否测量"schema 建模"？答：是。pydantic.validate 是客观判据。
- AT-3 的 DataFrame 7 行 4 列 + 平衡分是否测量"七准则评估"？答：是。结构化评分是直接测量。
- AT-4 的 >=4 条原则三件套是否测量"设计原则抽取"？答：是。三件套 + 跨领域迁移是 DSR Step 6 的本质。

### 3. Feed Forward: 不经 TLA 能过 AT 吗？若能 = 对齐失败
- 不经 `practice.md` D1 worked-faded，学生能否直接过 AT-2？理论上能（如果学生已熟 pydantic），但 D1 的 feedback_rule 要求 artifact_name 含"营销Agent"或"GraphRAG"，不经练习很难命中领域锚定。**对齐成立**。
- 不经 `tutorial.ipynb` 苏格拉底追问，学生能否过 AT-4 的"跨领域迁移"？这是高风险点 -- 学生可能凭直觉写一条原则应付。**对齐部分成立，需加强**：在 AT-4 增加"原则迁移到 R&D ClawBot 的具体步骤"子项。
- 不经 `schedule.json` 间隔重复，学生能否过 AT-1 卡集？不能 -- 间隔重复本身就是 AT-1。**对齐成立**。

## mastery 阈值汇总

| ILO | mastery_threshold | 不达标处理 |
|-----|-------------------|-----------|
| ILO-1 | >=80% 卡片答对率 + essay 术语全对 | 回退 `schedule.json` 卡集重练 + `practice.md` weak_loop |
| ILO-2 | >=80% TODO 通过 + pydantic.validate 跑通 | `practice.md` D1 weak_loop（回退到 worked 阶段） |
| ILO-3 | >=80% TODO 通过 + 平衡分 < 1.5 | `practice.md` D2 weak_loop + 补 worked example |
| ILO-4 | >=4 条原则三件套 + 跨领域迁移 | `practice.md` D3 weak_loop + `tutorial.ipynb` 重做 [FEED-FORWARD] |

---

*本文件遵循 Biggs (1996) 建构对齐 + Bloom mastery learning。mastery_threshold 全部锚定本单元 `starter.ipynb`/`solution.ipynb`/`practice.md`/`tutorial.ipynb`/`schedule.json` 的真实任务。*
