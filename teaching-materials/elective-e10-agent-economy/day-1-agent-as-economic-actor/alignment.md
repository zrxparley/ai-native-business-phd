# alignment.md · 建构对齐 (Biggs ILO ↔ TLA ↔ AT + mastery)

> 本文件落实 Biggs 建构对齐 (Constructive Alignment): 预期学习产出 (ILO) ↔ 教学学习活动 (TLA) ↔ 评估任务 (AT) 三者对齐。每行 ILO 必须有 TLA 训练 + AT 测量 + mastery 阈值。若学生不经 TLA 即可过 AT, 视为对齐失败。

---

## ILO ↔ TLA ↔ AT 矩阵 (>=3 行)

| ILO (预期学习产出, Intended Learning Outcome) | TLA (教学学习活动, Teaching/Learning Activity) | AT (评估任务, Assessment Task) | mastery_threshold |
|---|---|---|---|
| **ILO1**: 能用 mesa 构建买方/卖方 Agent 经济仿真, 含贝叶斯价格信念、A2A 协商、预算约束、破产机制, 20 步后涌现 gini 0.3-0.6 | ① starter.ipynb TODO1/TODO2/TODO4 (TODO 填空脚手架)<br>② practice.md drill D-S1-ABM (Worked->Faded->Independent 三阶段)<br>③ tutorial.ipynb 苏格拉底追问贝叶斯更新公式 | ① solution.ipynb 对照 (TODO1/2/4 无 scaffold 残留)<br>② practice.md drill D-S1-ABM feedback_rule: gini 0.3-0.6 + 9 个 model_reporters 齐<br>③ tutorial.ipynb 后测: 手算后验 μ'/σ'² | >=80% (gini 合理 + 9 reporters 齐 + 后测正确) |
| **ILO2**: 能用 networkx 分析 Agent 交易网络拓扑 (密度/聚类系数/PageRank), 解释三指标的宏观经济意义 (活跃度/多边协作可能性/资金流向影响力) | ① starter.ipynb TODO3 (networkx DiGraph 填空)<br>② practice.md drill D-S2-NET (Worked->Faded->Independent)<br>③ tutorial.ipynb 苏格拉底追问 "为何 PageRank 用在有向图才有经济意义" | ① solution.ipynb 对照 (TODO3 无 scaffold 残留)<br>② practice.md drill D-S2-NET feedback_rule: 三指标非 NaN + top-1 PageRank 经济解读<br>③ progressive_project Milestone: 三拓扑指标可计算 | >=80% (三指标非 NaN + 经济解读正确) |
| **ILO3**: 能用 numpy-financial 计算 Agent-as-Worker 的 NPV/IRR, 含推理成本敏感性 (GPT-4o vs DeepSeek V3 vs 临界点), 4 子图齐全 | ① starter.ipynb TODO5/TODO6 (DataCollector 提取 + NPV/IRR + matplotlib)<br>② practice.md drill D-S3-NPV (Worked->Faded->Independent)<br>③ tutorial.ipynb 苏格拉底追问 "推理成本下降到何处 Agent 经济盈亏平衡" | ① solution.ipynb 对照 (TODO5/6 无 scaffold 残留)<br>② practice.md drill D-S3-NPV feedback_rule: NPV 符号正确 + IRR 合理 + 4 子图齐<br>③ progressive_project Final: 4 子图有数据 + 推理成本敏感性结论 | >=80% (NPV 符号 + 4 子图 + 敏感性) |
| **ILO4**: 能解释 Agent 经济三层模型 (Tool/Worker/Actor) + 推理成本硬约束 + 天道推演×多Agent仿真同构, 联系营销场景 | ① notes.md 理论部分 + reading.md 深链阅读<br>② practice.md diagnostic D1/D2 (pset0 先测)<br>③ tutorial.ipynb 苏格拉底追问 "Agent-as-Actor 与 Agent-as-Worker 的本质区别" + schedule.json FSRS-6 间隔重复 | ① notes.md 作业: 300 字分析 (涌现现象/推理成本影响/网络拓扑意义)<br>② schedule.json C1/C2/C5 卡片复习 (FSRS-6 间隔, request_retention=0.9)<br>③ progressive_project Poster: 天道推演同构反思 | >=80% (300字分析 + FSRS 卡片 recall + Poster) |

---

## 3 自检问题 (Feed Up / Feed Back / Feed Forward)

> 每学期末, 教师用以下 3 问自检本单元建构对齐是否成立。任一答 "否" 即对齐失败, 需修订 TLA 或 AT。

### Q1. Feed Up: TLA 是否训练 ILO? (目标对齐)

- **问**: 本单元的 TLA (starter TODO 填空 + practice drill + tutorial 苏格拉底) 是否真正训练 ILO1-4 描述的可观察技能?
- **自检信号**:
  - ILO1 (mesa ABM) -> TODO1/2/4 + D-S1-ABM drill 是否覆盖贝叶斯更新 + A2A 协商 + 破产机制? 是。
  - ILO2 (networkx) -> TODO3 + D-S2-NET 是否覆盖三指标计算 + 经济解读? 是。
  - ILO3 (NPV/IRR) -> TODO5/6 + D-S3-NPV 是否覆盖推理成本敏感性? 是。
  - ILO4 (理论) -> notes/reading + diagnostic + tutorial + FSRS 卡片是否覆盖三层模型/推理成本/天道推演? 是。
- **若否**: 修订方向 -- 补 TLA (e.g., ILO3 若缺敏感性, 加 D-S3-NPV 的 GPT-4o vs DeepSeek 对比子任务)。

### Q2. Feed Back: AT 是否测量 ILO? (评估效度)

- **问**: AT (solution 对照 + drill feedback_rule + tutorial 后测 + 300 字分析 + FSRS recall + Poster) 是否真正测量 ILO, 而非测量无关技能 (如纯编程熟练度)?
- **自检信号**:
  - D-S1-ABM 的 feedback_rule 测量 gini 合理 + 9 reporters 齐 -> 测量的是 ABM 涌现理解, 不是 Python 语法。
  - D-S2-NET 的 feedback_rule 测量 PageRank 经济解读 -> 测量的是拓扑-经济映射, 不是 networkx API 调用。
  - D-S3-NPV 的 feedback_rule 测量 NPV 符号 + 推理成本敏感性 -> 测量的是 Agent 经济价值判断, 不是 numpy-financial 函数签名。
  - 300 字分析 + Poster 测量涌现解读 + 天道推演同构 -> 测量高阶认知, 不是复述。
- **若否**: 修订方向 -- 改 AT (e.g., 若发现 drill 只测 API 调用, 加 "用 1-2 句话解释该指标经济意义" 的口头答辩环节)。

### Q3. Feed Forward: 不经 TLA 能过 AT 吗? (对齐失败检测)

- **问**: 一个学生若不参与 TLA (不做 starter TODO、不练 drill、不与 tutorial 对话), 仅靠刷 solution.ipynb 或 ChatGPT 抄答案, 能过 AT 吗?
- **自检信号**:
  - D-S1-ABM Faded 阶段: 删 4 行核心代码 (后验均值/方差更新), 抄 solution 可过, 但 Independent 阶段 (LogNormal prior) 无 solution 可抄 -> 不能过。
  - D-S2-NET Independent: 时间切片图无 solution -> 不能过。
  - D-S3-NPV Independent: Agent 寿命敏感性无 solution -> 不能过。
  - tutorial.ipynb 后测: 手算 μ'/σ'², 抄不了 -> 不能过。
  - 300 字分析 + Poster: 高阶认知, 抄不了 -> 不能过。
- **结论**: 本单元 Independent 阶段 + 后测 + Poster 构成 "不经 TLA 不能过 AT" 的防线, 对齐成立。
- **若否 (e.g., 发现某 drill 抄 solution 可过)**: 修订方向 -- 加 Independent 变体 (改 prior 分布/改图结构/改现金流), 让 solution 失效。

---

## mastery 阈值统一标准

- 单 drill mastery: feedback_rule 全部检查项通过
- 单元 mastery: ILO1-4 全部 AT >=80% (与 practice.md progressive_project Final 评分一致)
- mastery 未达: 触发 practice.md weak_loop (回退上一 drill + Worked 重读 + tutorial 对话)

---

*本文件基于 Biggs 建构对齐理论 (Constructive Alignment) + Bloom 可观察 ILO + Hattie 可见学习 (visible learning) 的 Feed Up/Back/Forward 三级反馈设计。所有 TLA/AT 引用本单元真实文件 (starter/solution/practice/tutorial/schedule).*
