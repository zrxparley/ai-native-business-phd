# Day 3 建构对齐 (Biggs ILO ↔ TLA ↔ AT) (v6.0 学习科学层)

> 配套 v5.0 `notes.md` 学习目标 / `starter.ipynb` TODO 脚手架 / `solution.ipynb` 参考答案 / `practice.md` drills / `tutorial.ipynb` Socratic tutorial。本文件用 Biggs 建构对齐 (Constructive Alignment) 框架确保 ILO (Intended Learning Outcome) ↔ TLA (Teaching/Learning Activity) ↔ AT (Assessment Task) 三者对齐，每行附 mastery_threshold。所有 TLA/AT 引用本单元真实文件，不引入外部未交付物。

---

## ILO ↔ TLA ↔ AT 矩阵

> ILO 来源：`notes.md` 学习目标 1-5。TLA 引用 `starter.ipynb` 的 TODO / `practice.md` 的 drill / `tutorial.ipynb` 的 Socratic。AT 引用 `solution.ipynb` 后测 / `practice.md` 阶段3 独立解 / `tutorial.ipynb` exit artifact。
>
> **CQ-S5-1 对齐约束**：本单元新增评估可靠性协议后，所有 ILO 的 AT 必须覆盖数据真实性分级、人工黄金集、judge 校准、置信区间、成本、延迟和安全失败率；否则“能跑 deepeval”不等于“能做可信 Agent 评估”。

| ILO (预期学习产出) | TLA (教学学习活动) | AT (评估任务) | mastery_threshold |
|---|---|---|---|
| **ILO-1** 能解释 Agent 评估与传统软件测试的根本差异（非确定性/多步推理/工具调用/长尾效应），说明为什么传统断言式测试在 Agent 上失效 | (1) 读 `notes.md` 关键回顾1（四大挑战表）<br>(2) `practice.md` diagnostic D1 先测<br>(3) `tutorial.ipynb` cell2 pre-tutorial 提交一段"为什么断言失效"essay<br>(4) `practice.md` drill D3-Faithfulness 阶段3 设计对抗性用例 | (1) `solution.ipynb` TODO1 评测用例设计题（含"知识库不存在的问题"用例）<br>(2) `practice.md` D3 阶段3 独立解：对抗性用例 + 因果阶梯 L1/L2 定位<br>(3) `tutorial.ipynb` cell5 Hattie [TASK] 反馈判定 | >=80% (四大挑战能说出3个 + 断言失效根因 + 因果阶梯定位正确) |
| **ILO-2** 能区分轨迹评估 vs 端到端评估，指出各自适合的营销 Agent 场景 | (1) 读 `notes.md` 关键回顾2（轨迹 vs 端到端对比表 + ASCII 图）<br>(2) `practice.md` diagnostic D2 先测<br>(3) `practice.md` drill D2-Trajectory 阶段1 Worked（参考 solution.ipynb TODO3）<br>(4) `tutorial.ipynb` cell3 Socratic 追问"反例：端到端 0.82 但轨迹有错" | (1) `solution.ipynb` TODO3 自定义 BaseMetric 评估轨迹<br>(2) `practice.md` D2 阶段3 独立解：扩展参数准确性子分 + 解释 AgentBench OS/DB 场景为何更严<br>(3) `tutorial.ipynb` cell5 Hattie [PROCESS] 反馈 | >=80% (能指出端到端漏检幻觉 + 轨迹在哪步报警 + 两层都要的实践建议) |
| **ILO-3** 能用 deepeval 框架为营销 Agent 搭建可运行评测套件（LLMTestCase + GEval + FaithfulnessMetric + BaseMetric + evaluate） | (1) 读 `notes.md` 上机部分 6 个 TODO + `data/README.md` deepeval API 速查表<br>(2) `starter.ipynb` TODO1-6 填空脚手架<br>(3) `practice.md` drill D1-GEval / D2-Trajectory / D3-Faithfulness / D4-EvalBatch 全套<br>(4) `tutorial.ipynb` cell4 student_model 读写追踪掌握度 | (1) `solution.ipynb` 全 6 TODO 完整版（scaffold=0, TODO 残留=0）<br>(2) `practice.md` progressive_project Milestone：3 条 LLMTestCase + 3 metric 跑通最小版本<br>(3) `practice.md` D4 阶段3 独立解：evaluate() 批量 + 300 字根因<br>(4) `tutorial.ipynb` cell6 exit artifact | >=80% (6 TODO 全通 + 三大指标数字合理非0/100 + 根因定位到工具/参数/推理/幻觉之一) |
| **ILO-4** 能设计营销 Agent 核心评估指标（任务完成率/工具调用准确率/幻觉率），用 deepeval evaluate() 批量运行汇总 | (1) 读 `notes.md` 关键回顾4 六大指标表<br>(2) `practice.md` drill D4-EvalBatch 阶段1 Worked（参考 solution.ipynb TODO6）<br>(3) `tutorial.ipynb` cell3 Socratic 追问"指标能直接相加吗"<br>(4) 读 `reading.md` AgentBench/SWE-bench 条目定位自己 Agent 水平 | (1) `solution.ipynb` TODO6 evaluate() 批量结果<br>(2) `practice.md` D4 阶段3 独立解：三大指标 + 改进建议 + 改进前后对比<br>(3) `practice.md` progressive_project Final + Poster<br>(4) `tutorial.ipynb` cell5 Hattie [FEED-FORWARD] 反馈 | >=80% (三大指标计算正确 + 不直接相加的解释 + 改进建议有因果链预测) |
| **ILO-5** 能用自定义 BaseMetric 实现轨迹级评估，把"人工抽检"变成"CI 可运行的自动测试" | (1) 读 `notes.md` 上机部分 TODO3 + `data/README.md` BaseMetric API<br>(2) `practice.md` drill D2-Trajectory 三阶段 Worked-Faded<br>(3) `tutorial.ipynb` cell3 Socratic 追问"凭什么 reason 不是空洞词"<br>(4) 读 `reading.md` LLM-as-a-judge 条目理解 CI 集成 | (1) `solution.ipynb` TODO3 `ToolCallCorrectnessMetric` 完整实现<br>(2) `practice.md` D2 阶段3 独立解：参数准确性子分扩展<br>(3) `practice.md` D4-EvalBatch feedback_rule：reason 空洞词自检<br>(4) `tutorial.ipynb` cell5 Hattie [SELF-REG] 反馈 | >=80% (BaseMetric 跑通 + score 非0/100 + reason 含具体步骤定位 + CI 集成命令正确) |

| **ILO-6 / CQ-S5-1** 能判断 Agent eval 分数是否可信：区分 synthetic/curated/recorded 数据，构建人工黄金集，校准 LLM judge，报告 Wilson 置信区间、成本、延迟和安全失败率 | (1) 读 `notes.md` 评估可靠性协议<br>(2) 读 `data/README.md` 数据真实性分级与泄漏控制<br>(3) 完成 `practice.md` CQ-S5-1 校准/轨迹/安全/工程加练<br>(4) 在 `solution.ipynb` 对比 deterministic trajectory metric 与 LLM judge metric | (1) 提交 >=10 条 curated case 的 provenance 表<br>(2) 提交人工黄金集 vs judge 标签一致性表<br>(3) 提交重复评估均值/方差 + 位置偏差/长度偏差说明<br>(4) 提交成本、延迟、安全失败率摘要 | >=80% (能说明 3 条 synthetic 样例不能支撑生产结论 + judge 校准通过 + 安全失败不被平均分掩盖) |

---

## 3 自检问题 (Biggs constructive alignment 三层反馈)

### Q1 Feed Up：TLA 是否训练 ILO？（教学活动是否对准预期产出）

逐行检查矩阵：每个 ILO 至少有 2 个 TLA 支撑（读 notes + 做 drill/tutorial），且 TLA 类型多元（读/做/答）。若某 ILO 只有 1 个 TLA 或全为"读"型 -> 对齐不足，需补 1 个"做"型 TLA。

**本单元自检**：5 个 ILO 各有 >=3 TLA（读 notes + starter TODO + practice drill + tutorial Socratic），类型多元，对齐充分。

### Q2 Feed Back：AT 是否测量 ILO？（评估任务是否真的测预期产出）

逐行检查：每个 AT 必须能区分"会 ILO"与"不会 ILO"的学生。若 AT 只测"是否抄了 solution.ipynb" -> 测量失效，需改为"用自己的话写 criteria / 独立设计对抗性用例"。

**本单元自检**：5 个 AT 中 4 个含"独立解"或"300 字根因"（不能靠抄），D4 AT 含"改进前后对比数字"（必须真跑 evaluate）。measurement 有效。

### Q3 Feed Forward：不经 TLA 能过 AT 吗？（若能=对齐失败）

对每个 AT 反问：学生若跳过所有 TLA（不读 notes / 不做 starter TODO / 不做 drill / 不上 tutorial），能否直接过 AT？

- **AT-1** (solution TODO1 评测用例设计)：跳过 TLA -> 不知 deepeval API，无法设计 -> 对齐 OK
- **AT-2** (D2 阶段3 独立解扩展参数子分)：跳过 TLA -> 不知 BaseMetric 继承机制 -> 对齐 OK
- **AT-3** (D4 阶段3 evaluate 批量 + 300 字根因)：跳过 TLA -> 不知 evaluate API + 不懂因果链 -> 对齐 OK
- **AT-4** (progressive_project Final + Poster)：跳过 TLA -> 无改进前后对比数字 -> 对齐 OK
- **AT-5** (tutorial exit artifact 2-3 盲点)：跳过 TLA -> 不知 LLM-as-judge 偏差 -> 对齐 OK

**结论**：5 个 AT 均无法绕过 TLA 直接通过 -> 建构对齐成立。

---

## mastery 阈值汇总

| ILO | mastery_threshold | 测量来源 |
|---|---|---|
| ILO-1 | >=80% (四大挑战3个 + 断言失效根因 + 因果阶梯) | D3 阶段3 + tutorial [TASK] |
| ILO-2 | >=80% (端到端漏检 + 轨迹报警 + 两层都要) | D2 阶段3 + tutorial [PROCESS] |
| ILO-3 | >=80% (6 TODO + 三大指标合理 + 根因) | progressive_project Milestone + tutorial exit |
| ILO-4 | >=80% (三大指标 + 不相加 + 改进因果链) | D4 阶段3 + Poster + tutorial [FEED-FORWARD] |
| ILO-5 | >=80% (BaseMetric + reason 具体定位 + CI 命令) | D2 阶段3 + tutorial [SELF-REG] |
| ILO-6 / CQ-S5-1 | >=80% (provenance + 人工黄金集 + judge 校准 + 置信区间 + 成本/延迟/安全) | practice CQ-S5-1 加练 + solution 后测 |

**整体 mastery**：6 个 ILO 全部达标 = Day 3 mastery 通过，可进入 Day 4 安全防护。任一 ILO 未达标 -> 进入 `practice.md` weak_loop 回退阶段1。

---

*v6.0 学习科学层：Biggs 建构对齐 (ILO ↔ TLA ↔ AT) + mastery threshold + 三层反馈 (Feed Up / Feed Back / Feed Forward)。所有 TLA/AT 引用本单元真实文件 (notes.md / starter.ipynb / solution.ipynb / practice.md / tutorial.ipynb / reading.md / data/README.md)，不引入外部未交付物。*
