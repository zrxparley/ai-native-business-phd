# 建构对齐 (Constructive Alignment, Biggs) · Day 1 价值对齐与Constitutional AI

> 基于 Biggs 建构对齐 (ILO↔TLA↔AT) + mastery learning。每个预期学习产出(ILO)都有对应的教学学习活动(TLA)和评估任务(AT), 附mastery阈值。三个自检问题保证对齐闭环。

## ILO↔TLA↔AT 矩阵

| ILO (预期学习产出) | TLA (教学学习活动) | AT (评估任务) | mastery_threshold |
|---|---|---|---|
| **ILO1**: 能解释AI对齐三层结构(意图/行为/价值), 说明"最大化转化率"为何导致对齐失败 | starter.ipynb TODO1 (HHH用例设计) + practice.md drill D1 (HHH标注 Worked-Faded) + tutorial.ipynb Socratic loop 第1-2轮 | solution.ipynb TODO1 完整用例集 + tutorial.ipynb 后测第1题 + practice.md diagnostic Q1 | >=80% (3题对2题+) |
| **ILO2**: 能区分RLHF/CAI/DPO三种对齐方法的技术差异、优劣势、演进逻辑 | starter.ipynb TODO2-4 (deepeval BaseMetric实现) + practice.md drill D2 (HarmlessMetric Worked-Faded) + schedule.json C2卡片间隔重复 | solution.ipynb TODO2-4 三维度metric实现 + practice.md diagnostic Q2 | >=80% |
| **ILO3**: 能用deepeval自定义BaseMetric按HHH原则评估营销Agent对齐质量 | starter.ipynb TODO2-4 + practice.md drill D2 (Worked-Faded 三阶段) + tutorial.ipynb Socratic loop 第3轮 (HarmlessMetric追问) | solution.ipynb 三维度BaseMetric完整实现 + tutorial.ipynb 后测第2题 (实现一个metric) | >=80% (metric与oracle偏差<=0.3) |
| **ILO4**: 能用garak alignment probes扫描价值偏差并读懂报告 | starter.ipynb TODO5 (garak静态扫描fallback) + practice.md drill D3 (报告解读 Worked-Faded) + schedule.json C5卡片 | solution.ipynb TODO5 garak报告 + practice.md D3 Stage3独立解读 + tutorial.ipynb Socratic第4轮 | >=80% (fail率排序+弱点定位正确) |
| **ILO5**: 能为营销Agent设计企业宪法原则集(5-10条, 覆盖5维度) | starter.ipynb TODO6 (企业宪法+LLM-as-a-judge) + practice.md drill D4 (宪法设计 Worked-Faded) + tutorial.ipynb Socratic第5轮 | solution.ipynb TODO6 完整宪法+评审报告 + practice.md D4 Stage3独立设计 + tutorial.ipynb exit artifact | >=80% (5维度全覆盖+每条可测试) |

## 三个自检问题 (Feed Up / Feed Back / Feed Forward)

### Q1 (Feed Up): TLA 是否训练 ILO?

- ILO1 (对齐三层) -> TLA: TODO1用例设计 + D1标注 + Socratic追问 = ✅ 训练"识别对齐层次"能力
- ILO2 (方法差异) -> TLA: TODO2-4 + D2 metric + C2卡片 = ✅ 训练"理解方法演进"
- ILO3 (deepeval) -> TLA: TODO2-4 + D2 Worked-Faded + Socratic = ✅ 训练"实现BaseMetric"
- ILO4 (garak) -> TLA: TODO5 + D3报告解读 + C5卡片 = ✅ 训练"运行探针+读报告"
- ILO5 (企业宪法) -> TLA: TODO6 + D4 + Socratic = ✅ 训练"设计宪法原则"

**结论**: 每个 ILO 至少有 2-3 个 TLA 支撑, 训练充分。

### Q2 (Feed Back): AT 是否测量 ILO?

- ILO1 -> AT: TODO1完整用例集 + 后测Q1 + diagnostic Q1 = ✅ 直接测量"识别对齐层次"
- ILO2 -> AT: TODO2-4 + diagnostic Q2 = ✅ 测量"方法区分"
- ILO3 -> AT: TODO2-4 + 后测Q2 + metric偏差阈值 = ✅ 测量"BaseMetric实现质量"
- ILO4 -> AT: TODO5 + D3 Stage3 + Socratic第4轮 = ✅ 测量"报告解读+弱点定位"
- ILO5 -> AT: TODO6 + D4 Stage3 + exit artifact = ✅ 测量"宪法设计可执行性"

**结论**: 每个 ILO 至少有 2 个 AT 测量, 含代码实现+概念问答双通道。mastery 阈值明确(>=80%)。

### Q3 (Feed Forward): 不经 TLA 能过 AT 吗? 若能 = 对齐失败

- ILO1: 不做D1标注练习, 直接做后测Q1 -> 大概率凭直觉猜对一层, 但无法解释"价值对齐"为何不是意图对齐 -> ✅ 需TLA
- ILO2: 不做D2 metric实现, 直接做diagnostic Q2 -> 可能记住"CAI不需人类标注"但说不清RLAIF流程 -> ✅ 需TLA
- ILO3: 不做D2 Worked-Faded, 直接写metric -> 大概率写成if-else关键词匹配(notes.md明确批评的反模式) -> ✅ 需TLA
- ILO4: 不做D3报告解读, 直接做garak TODO5 -> 可能跑通但无法定位"最弱维度" -> ✅ 需TLA
- ILO5: 不做D4宪法设计, 直接写5条原则 -> 大概率写成"不要欺骗"等不可测试口号 -> ✅ 需TLA

**结论**: 所有 ILO 都需要经过 TLA 才能通过 AT, 对齐闭环成立。若学生不经 TLA 直接过 AT, 触发 weak_loop 回退到对应 drill 的 Stage1 worked example。

## mastery 渐进门槛

| 阶段 | 门槛 | 触发动作 |
|---|---|---|
| 单个 drill | >=80% (与 oracle/参考答案一致) | 未达->重试(不罚分) |
| 连续2次失败 | weak_loop | 回退Stage1+补充worked example+密集复习 |
| progressive_project proposal | 导师feedback通过(无评分) | 24h内反馈, 不通过迭代 |
| progressive_project milestone | HHH三维度metric跑通>=3用例 | 未达->重试1次 |
| progressive_project final | >=80% (HHH评分+garak报告+宪法5维度) | 未达->重试1次 |
| 单元总评 | 5个ILO全部>=80% | 任一未达->延长1周+1对1tutorial |

---

*本建构对齐矩阵引用 Biggs & Tang constructive alignment (ILO↔TLA↔AT) + Bloom mastery learning。TLA引用本单元真实文件 (starter.ipynb/solution.ipynb TODO编号 + practice.md drill编号 + tutorial.ipynb Socratic轮次 + schedule.json 卡片)。AT引用 TODO完整答案 + diagnostic + 后测 + exit artifact。*
