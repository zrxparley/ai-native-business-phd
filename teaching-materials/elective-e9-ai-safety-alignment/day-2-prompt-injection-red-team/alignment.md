# alignment.md · Day 2 提示注入+红队 · 建构对齐 (v6.0)

> 依据: Biggs 建构对齐 (Constructive Alignment) — ILO (Intended Learning Outcomes, 预期学习产出) ↔ TLA (Teaching/Learning Activities, 教学学习活动) ↔ AT (Assessment Tasks, 评估任务) 三者一致; 配合 Bloom 修订版 + mastery threshold。
> 配套: `notes.md` (5 学习目标) / `starter.ipynb` (6 TODO) / `solution.ipynb` (gated) / `practice.md` (3 drills) / `tutorial.ipynb` (苏格拉底).

---

## ILO ↔ TLA ↔ AT 矩阵 (Biggs, >=3 行)

> ILO 编号对应 `notes.md` 的 5 个学习目标 (1-5); TLA 引用具体 drill/starter TODO/tutorial; AT 引用具体 solution/tutorial 后测; mastery_threshold 是过关线。

| ILO (预期学习产出) | TLA (教学学习活动) | AT (评估任务) | mastery_threshold |
|-------------------|-------------------|--------------|------------------|
| **ILO-1** 解释 OWASP LLM01 Prompt Injection 两种形态 (直接 vs 间接) 及对营销 Agent 的威胁 (泄露竞品机密/越权打折/发布违规文案) | • `notes.md` § 关键回顾 1-2 表格精读<br>• `practice.md` Drill D1 Worked+Faded (PI-01/05 拆解)<br>• `tutorial.ipynb` 苏格拉底追问 "为什么间接注入更危险" | • `practice.md` Diagnostic Q1 (LLM01-L5 映射)<br>• `tutorial.ipynb` pre-tutorial essay (提交一段攻击面拆解)<br>• `solution.ipynb` TODO1 12 攻击向量集 | ≥80% (12 向量分类全对, L1 漏检原因说清) |
| **ILO-2** 手写 Python 5 层纵深防御 (L1 regex / L2 系统提示加固 / L3 规则式安全检查 Agent / L4 输出脱敏 / L5 权限隔离) | • `starter.ipynb` TODO2 (L1+L2) / TODO3 (L3+L4) / TODO4 (L5)<br>• `practice.md` Drill D2 Worked (L1 完整) + Faded (L3 三规则) + Independent (L4+L5)<br>• `tutorial.ipynb` 苏格拉底 "L1 漏检 Base64 时 L2-L5 如何兜底" | • `solution.ipynb` 5 层代码跑通 12 攻击向量<br>• `practice.md` Drill D2 reps 4 次达标<br>• `tutorial.ipynb` 后测: 写出 L3 三规则签名 + L4 三脱敏模式 | ≥80% (5 层接口一致 `layer()->(prompt,blocked,name)`, 12 向量拦截 ≥9/12) |
| **ILO-3** 用 deepeval 自定义 BaseMetric (SafetyMetric) 量化防御前后安全分, 理解 LLM-as-a-judge 在安全评估中的应用 | • `notes.md` § 2026 前沿 (deepeval SafetyMetric)<br>• `starter.ipynb` TODO6 (SafetyMetric)<br>• `practice.md` Drill D3 Worked (防御前 0.18 / 防御后 0.92 演示) + Faded (measure 三维度填空)<br>• `tutorial.ipynb` 苏格拉底 "为什么不能只看脏话" | • `solution.ipynb` TODO6 防御前后对比分数<br>• `practice.md` Drill D3 Independent (SafetyMetric.measure 三维度)<br>• `tutorial.ipynb` Hattie [TASK] 反馈 | ≥80% (防御后 SafetyMetric ≥0.85, 三维度说清) |
| **ILO-4** 执行红队仿真: 手写 12+ Prompt Injection 攻击向量 (jailbreak/leak/instruction-injection/data_poisoning/encoding/action), 跑 5 层防御, 统计各层拦截率 | • `starter.ipynb` TODO1 (12 向量) + TODO5 (红队仿真)<br>• `practice.md` Drill D1 (12 向量分类) + Drill D3 Worked (拦截率表)<br>• `tutorial.ipynb` 苏格拉底 "若攻击者用 Base64+小写+多轮组合" | • `solution.ipynb` TODO5 各层拦截率表<br>• `practice.md` Drill D3 Independent (1 条间接注入 + 300 字根因)<br>• `tutorial.ipynb` Hattie [PROCESS] 反馈 | ≥80% (12 向量覆盖六分类, 拦截率表 5 层全填) |
| **ILO-5** 区分 garak (NVIDIA LLM 漏洞扫描器) 与 PyRIT (微软自动化红队框架) 的定位差异, 理解生产环境互补关系 | • `notes.md` § 2026 前沿 (garak/PyRIT 工具表)<br>• `reading.md` garak/PyRIT/OWASP 深链<br>• `practice.md` Drill D3 feedback_rule (garak vs PyRIT 定位)<br>• `tutorial.ipynb` 苏格拉底 "garak 全过 ≠ 安全, 对应因果阶梯哪层" | • `practice.md` Drill D3 Independent 根因分析<br>• `tutorial.ipynb` Hattie [FEED-FORWARD] 反馈<br>• `practice.md` 元认知自检 Q3 | ≥80% (定位写对, 因果阶梯 L1 自知说清) |

---

## 3 自检问题 (Biggs 三级反馈: Feed Up / Feed Back / Feed Forward)

> 教师在交付前对每个 ILO 行做以下三问, 任一问答 "否" 即对齐失败, 需修改 TLA 或 AT。

### 自检 1: Feed Up — TLA 是否训练 ILO? (向上对齐预期产出)

- **ILO-1**: D1 Worked+Faded 是否训练"两种形态 + 营销威胁"? **是** — D1 直接拆 PI-01/05, 用 OWASP LLM01 术语。
- **ILO-2**: starter TODO2-4 + D2 是否训练"手写 5 层"? **是** — TODO2-4 覆盖 L1-L5 全部接口, D2 三阶段 (Worked L1 -> Faded L3 -> Independent L4+L5)。
- **ILO-3**: TODO6 + D3 是否训练"deepeval SafetyMetric + LLM-as-a-judge"? **是** — D3 Faded 直接补 measure() 三维度。
- **ILO-4**: TODO1+5 + D1+D3 是否训练"12 向量红队 + 拦截率"? **是** — D1 分类, D3 跑仿真。
- **ILO-5**: notes § 前沿 + D3 feedback_rule 是否训练"garak vs PyRIT 定位"? **是** — D3 根因分析强制引用两工具。

### 自检 2: Feed Back — AT 是否测量 ILO? (回测是否真测到产出)

- **ILO-1 AT**: Diagnostic Q1 + TODO1 是否真测"两种形态 + L1 漏检原因"? **是** — Q1 强制写 L1 漏检 LLM03 原因, TODO1 强制 12 向量分类。
- **ILO-2 AT**: solution 5 层代码 + D2 reps 是否真测"5 层实现 + 接口一致"? **是** — 接口三元组 `(prompt, blocked, name)` 自动校验。
- **ILO-3 AT**: solution TODO6 + D3 Independent 是否真测"SafetyMetric 三维度"? **是** — measure() 三维度必须显式。
- **ILO-4 AT**: solution TODO5 拦截率表 + D3 间接注入是否真测"红队仿真"? **是** — 拦截率表 5 层全覆盖才达标。
- **ILO-5 AT**: D3 根因 + 元认知 Q3 是否真测"garak vs PyRIT + 因果阶梯"? **是** — 必须说清 L1 自知。

### 自检 3: Feed Forward — 不经 TLA 能过 AT 吗? 若能 = 对齐失败 (前馈检验)

> 这是 Biggs 对齐的最严苛检验: 如果学生不参与 TLA (不来上课/不做 drill/不上 tutorial), 仅靠刷 AT 能过吗?

- **ILO-1**: 不读 notes 表格不做 D1, 仅刷 Diagnostic Q1 — **不能过**。Q1 要求 L1 漏检 LLM03 的具体原因, 不读 notes § 关键回顾 1 或不做 D1 Worked 无法答。
- **ILO-2**: 不做 starter TODO2-4 不做 D2, 仅抄 solution — **能跑通但 D2 reps 4 次不达标** (接口一致 + 单测覆盖正例负例, 抄的代码过不了 reps 反馈)。**对齐成立**。
- **ILO-3**: 不做 D3 Filled, 仅看 solution TODO6 — **不能过**。D3 Independent 要求设计 1 条新间接注入 (solution 没有), 必须自己写。
- **ILO-4**: 不做 D1+D3, 仅抄 solution 12 向量 — **能跑通拦截率表但 D3 根因 300 字不达标** (根因需区分 L1 编码漏检 vs L3 语义漏检, 抄的代码无根因)。**对齐成立**。
- **ILO-5**: 不读 notes § 前沿不做 D3 feedback_rule — **不能过**。元认知 Q3 强制说清 garak/PyRIT 定位 + 因果阶梯 L1, 不读前沿无法答。

**结论**: 5 个 ILO 全部通过三级自检, 建构对齐成立。若任一 ILO 在 Feed Forward 检验中"不经 TLA 能过 AT", 则该 ILO 对齐失败, 需升级 AT (加随机化/新场景/口头答辩) 或加 TLA (补 worked example)。

---

## mastery threshold 总表

| ILO | AT 主体 | 阈值 | 不达标触发 |
|----|--------|------|----------|
| ILO-1 | Diagnostic Q1 + TODO1 + tutorial essay | ≥80% (12 向量分类全对 + L1 漏检原因说清) | weak_loop 回 D1 Worked |
| ILO-2 | solution 5 层代码 + D2 reps 4 次 | ≥80% (5 层接口一致 + 12 向量拦截 ≥9/12) | weak_loop 回 D1 Faded |
| ILO-3 | solution TODO6 + D3 Independent | 防御后 SafetyMetric ≥0.85 + 三维度说清 | weak_loop 回 D3 Worked |
| ILO-4 | solution TODO5 拦截率表 + D3 间接注入 | ≥80% (六分类覆盖 + 5 层拦截率全填) | weak_loop 回 D1 + D3 Worked |
| ILO-5 | D3 根因 + 元认知 Q3 | ≥80% (garak/PyRIT 定位 + L1 自知说清) | weak_loop 回 D1 (攻击面术语) |

> mastery 阈值依据 Bloom 修订版: ILO-1/5 = Understand 层 (解释), ILO-2/3/4 = Apply/Analyze 层 (实现/度量/仿真)。Understand 层阈值 80%, Apply/Analyze 层阈值 80% 但 AT 含随机化新场景防抄。
