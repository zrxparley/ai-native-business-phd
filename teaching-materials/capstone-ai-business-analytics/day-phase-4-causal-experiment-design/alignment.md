# alignment.md - Capstone Phase 4 建构对齐 (Constructive Alignment, Biggs)

> 本文件遵循 Biggs 建构对齐原则：ILO（预期学习产出）↔ TLA（教学学习活动）↔ AT（评估任务）三者对齐，每行附 mastery_threshold。配 3 自检问题（Feed Up / Feed Back / Feed Forward）确保对齐有效。

---

## ILO ↔ TLA ↔ AT 矩阵

| ILO（预期学习产出） | TLA（教学学习活动） | AT（评估任务） | mastery_threshold |
|--------------------|--------------------|---------------|-------------------|
| **ILO1**：能用解释性序列设计规划营销 Agent 因果评估方案（先定量 A/B+因果推断，再定性访谈，最后整合） | 阅读 notes.md "解释性序列设计"节 + starter.ipynb TODO1 + practice.md Drill A1 Worked-Faded + tutorial.ipynb cell2 pre-tutorial essay | starter.ipynb TODO1 协变量均衡表 + tutorial.ipynb cell5 Hattie [TASK] 反馈 + practice.md Drill A1 Independent 阶段提交 | ≥80% 协变量 SMD 表正确 + 序列设计图 3 阶段无遗漏 |
| **ILO2**：能在 NSW 真实 RCT 上完成 DoWhy 四步因果分析（建模->识别->估计->反驳），估计 ATE 并跑反驳检验 | notes.md 关键回顾 2 + starter.ipynb TODO2/TODO3 + practice.md Drill A1/A2/A3 + reading.md DoWhy 条目 + tutorial.ipynb cell3 Socratic 追问 | starter.ipynb TODO2/TODO3 完成 + solution.ipynb 对照 + practice.md Drill A3 Independent 稳健性报告（3 种反驳 + 自选第 4 种） | ≥80% ATE 估计符号正确 + 3 种反驳偏离均 < 30% + student_model.json `robustness_pass: true` |
| **ILO3**：能用 DML（econml LinearDML）和因果森林估计异质因果效应 CATE，识别获益最大子群体 | notes.md 2026 前沿 DML/因果森林节 + starter.ipynb TODO5/TODO6 + practice.md Drill B2 + reading.md econml 条目 | starter.ipynb TODO5/TODO6 + practice.md Drill B2 Independent CATE 对比表（DML vs 因果森林）+ 300 字"哪个群体获益最大" | ≥80% DML ATE 与因果森林 CATE 在 nodegree 子群体符号一致 + 群体识别正确（如 nodegree=True 获益最大） |
| **ILO4**：能用 CUPED 利用前实验协变量（re75）降低实验方差，提升检测灵敏度 | notes.md 关键回顾 4 + starter.ipynb TODO4 + practice.md Drill B1 | starter.ipynb TODO4 方差对比 + practice.md Drill B1 Independent 协变量选择对比（re74 vs re75） | ≥80% 方差降低 > 5% + theta 公式正确 + Y_adj 计算无误 |
| **ILO5**：能用自定义 BaseMetric（deepeval fallback）评估 Phase 3 Agent 输出中因果证据使用质量 | notes.md 整合性节 + starter.ipynb TODO7 + practice.md Drill C1 + tutorial.ipynb cell4 student_model 读写 | starter.ipynb TODO7 BaseMetric 实现 + practice.md Drill C1 Independent 5 样本评估报告 + tutorial.ipynb cell5 [FEED-FORWARD] 改进建议 | ≥80% BaseMetric 返回 0-1 分数 + reason 字段 + 5 样本评估分数分布合理（非全 1 或全 0） |

---

## 3 自检问题（Feed Up / Feed Back / Feed Forward）

### 自检 1 - Feed Up：TLA 是否训练 ILO？

> 问：上述 5 个 ILO，每个 ILO 的 TLA 是否真的训练了该 ILO 所需的能力？

- **ILO1**：starter.ipynb TODO1 + Drill A1 + tutorial cell2 -> 训练"规划评估方案"。**是**，TODO1 要求画协变量均衡表（规划第一步），tutorial cell2 essay 强制 retrieval 设计思路。
- **ILO2**：TODO2/3 + Drill A1/A2/A3 + reading DoWhy -> 训练"DoWhy 四步"。**是**，三 drill 覆盖建模/识别/估计/反驳四步。
- **ILO3**：TODO5/6 + Drill B2 + reading econml -> 训练"DML+因果森林 CATE"。**是**，Drill B2 Worked-Faded-Independent 全流程。
- **ILO4**：TODO4 + Drill B1 -> 训练"CUPED 方差缩减"。**是**，但 TLA 单一（仅 1 drill），若学生失败触发 weak_loop 回退 B1 + 补 Worked。
- **ILO5**：TODO7 + Drill C1 + tutorial cell4 -> 训练"BaseMetric 评估"。**是**，但依赖 Phase 3 Agent 输出（跨 Phase 整合）。

**结论**：5 ILO 均有 TLA 支撑。ILO4 TLA 较薄，已用 weak_loop 补偿。

### 自检 2 - Feed Back：AT 是否测量 ILO？

> 问：每个 ILO 的 AT 是否真的测量了该 ILO 所声明的产出，而非相邻 ILO？

- **ILO1 AT**：TODO1 协变量 SMD 表 + tutorial [TASK] 反馈 -> 测"规划能力"。**是**，SMD 表是规划第一步的具体产物。
- **ILO2 AT**：TODO2/3 + Drill A3 稳健性报告 -> 测"DoWhy 四步 + 反驳"。**是**，三种反驳 + 自选第 4 种直接对应反驳能力。
- **ILO3 AT**：TODO5/6 + Drill B2 CATE 对比表 -> 测"DML+因果森林 CATE"。**是**，CATE 对比表是异质效应的直接测量。
- **ILO4 AT**：TODO4 方差对比 + Drill B1 协变量对比 -> 测"CUPED"。**是**，方差降低比例是 CUPED 的直接指标。
- **ILO5 AT**：TODO7 BaseMetric + Drill C1 5 样本报告 -> 测"Agent 因果证据评估"。**是**，5 样本评估直接测能力。

**结论**：5 AT 均直接测量对应 ILO，无错位。

### 自检 3 - Feed Forward：不经 TLA 能过 AT 吗？（若能 = 对齐失败）

> 问：学生若不参与 TLA（不做 drill、不读 notes、不上 tutorial），仅凭先验知识能否通过 AT？

- **ILO1 AT**：SMD 表需知道 `pd.crosstab` + 标准化均值差公式。先验充足的统计学生**可能跳过** notes 直接做。**风险中等**。补救：tutorial cell2 essay 强制写"为什么用解释性序列而非纯定量"，无 TLA 难答。
- **ILO2 AT**：DoWhy 四步 API 调用需具体库知识。**不参与 TLA 难过**（DoWhy API 非通用知识）。
- **ILO3 AT**：econml LinearDML/CausalForestDML 参数（`discrete_treatment`/`model_y`/`model_t`）非通用。**不参与 TLA 难过**。
- **ILO4 AT**：CUPED theta 公式 + NSW `re75` 选择需 notes 上下文。**不参与 TLA 难过**（学生可能误用 `re74`）。
- **ILO5 AT**：deepeval BaseMetric `measure()` 签名 + 因果证据三检测项需 TODO7 + Drill C1。**不参与 TLA 难过**。

**结论**：5 AT 中 4 个不参与 TLA 难过，1 个（ILO1）有中等风险已用 tutorial essay 补救。**对齐有效**。

---

## mastery 总览

- **Phase 4 通过条件**：5 个 ILO 的 AT 均达 mastery_threshold + Poster ≥ 80%
- **未达 mastery 的回路**：触发 practice.md weak_loop -> 回退上一 drill + 补 Worked Example + schedule.json 间隔缩短
- **mastery 记录位置**：tutorial.ipynb cell4 `student_model.json`，字段 `ilo_mastery: {ILO1: float, ILO2: float, ..., ILO5: float}`

---

## 与 v5.0 基线的衔接

本对齐矩阵不修改 v5.0 的 notes.md/starter.ipynb/solution.ipynb/reading.md/data/README.md。新增的 practice.md/schedule.json/tutorial.ipynb 是 v6.0 学习科学层，与 v5.0 上机任务（7 个 TODO）一一对应：每个 TODO 映射到至少一个 ILO 的 AT。
