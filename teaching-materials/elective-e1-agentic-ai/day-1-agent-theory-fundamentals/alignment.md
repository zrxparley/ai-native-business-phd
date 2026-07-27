# Day 1 Agent理论基础 · 建构对齐 (Constructive Alignment, Biggs 1996)

> 设计依据: Biggs(1996) ILO↔TLA↔AT 三元对齐 + Bloom 可观察动词 + mastery threshold(>=80%)。所有 TLA 引用本单元真实文件(starter.ipynb TODO / practice.md drill / tutorial.ipynb Socratic),所有 AT 引用 solution.ipynb / tutorial 后测 / practice diagnostic。

---

## 一、ILO ↔ TLA ↔ AT 对齐矩阵 (>=3 行)

| ILO (预期学习产出, Intended Learning Outcome) | TLA (教学学习活动, Teaching/Learning Activity) | AT (评估任务, Assessment Task) | mastery_threshold |
|---|---|---|---|
| **ILO1** 能解释Agent的自主性谱系(L0-L4),区分Workflow与Agent本质差异,在售前场景判断客户真实自主性需求层级 | ① 读 `notes.md` § 关键回顾1 自主性谱系表<br>② 完成 `practice.md` Diagnostic D1 先测<br>③ `tutorial.ipynb` Socratic 追问"L2条件路由为何仍是Workflow" | ① `practice.md` D1 自评<br>② `tutorial.ipynb` 后测:学生口头复述 L0-L4 + 营销示例<br>③ `schedule.json` C1 间隔重复卡 recall | >=80% (L0-L4 五级名称+营销示例各对1个) |
| **ILO2** 能用BDI(Belief-Desire-Intention)模型分析营销Agent认知结构,并用pydantic将BDI形式化为Agent状态Schema | ① `starter.ipynb` TODO1 填空 BDI Schema<br>② `practice.md` Drill1 (D1-BDI-Schema) Worked-Faded 三阶段<br>③ `tutorial.ipynb` Socratic 追问"Intention 的坚持性若缺失会怎样" | ① `solution.ipynb` TODO1 对照自评<br>② `practice.md` Drill1 阶段3 独立解 AgentState 模型<br>③ `schedule.json` C2 BDI 卡 recall | >=80% (三模型字段齐全+营销语义正确) |
| **ILO3** 能用LangGraph的`create_react_agent`和LangChain的`@tool`构建带工具调用的ReAct Agent,在营销任务上观察Thought-Action-Observation循环 | ① `starter.ipynb` TODO2 定义三个@tool工具<br>② `starter.ipynb` TODO3 用`create_react_agent`构建Agent<br>③ `practice.md` Drill2(D2-Tool-Contract)+Drill3(D3-ReAct-Trace)<br>④ `tutorial.ipynb` Socratic 追问"接口契约四要素" | ① `solution.ipynb` TODO2-3 对照<br>② `practice.md` Drill3 阶段3 独立提取 ReAct 轨迹+因果标注<br>③ `schedule.json` C3/C6 卡 recall | >=80% (轨迹含>=2轮Thought-Action-Obs+docstring四要素) |
| **ILO4** 能用`MemorySaver`实现Agent短期记忆,支持多轮对话,理解checkpointer机制 | ① `starter.ipynb` TODO5 添加 MemorySaver<br>② `tutorial.ipynb` Socratic 追问"thread_id 错误会怎样"<br>③ `schedule.json` C7 卡 recall | ① `solution.ipynb` TODO5 对照<br>② `practice.md` Drill3 阶段3 多轮续接验证 | >=80% (多轮对话能续接上一轮 Belief) |
| **ILO5** 能实现Plan-Execute模式并与ReAct对比,理解两种Agent范式在营销决策中的适用边界 | ① `starter.ipynb` TODO6 用 StateGraph 实现 Plan-Execute<br>② `practice.md` Drill4(D4-Plan-Execute-VS-ReAct)<br>③ `tutorial.ipynb` Socratic 追问"信息不足时为何 Plan-Execute 失效" | ① `solution.ipynb` TODO6 对照<br>② `practice.md` Drill4 阶段3 300字对比分析<br>③ `schedule.json` C5 卡 recall | >=80% (步数对比+适用边界判断正确) |
| **ILO6** 能用天道推演框架分析Agent因果链路,识别关键因果节点和不可逆后果 | ① 读 `notes.md` § 天道推演视角<br>② `practice.md` Drill3/4 阶段3 因果标注<br>③ `tutorial.ipynb` Socratic 追问"write_strategy 的不可逆点在哪" | ① `practice.md` Poster 阶段:因果链对比图+>=2不可逆点<br>② `tutorial.ipynb` exit artifact:2-3盲点 | >=80% (>=2个不可逆点+因果节点标注) |

---

## 二、3 自检问题 (Biggs constructive alignment 三阶反馈)

### 自检 1: TLA 是否训练 ILO? (Feed Up, 向上对齐)

- **ILO1↔TLA1**: `notes.md` 自主性谱系表 + D1 先测 + Socratic 追问 → 是否训练"解释+区分+判断"? **是**。三活动分别覆盖"读-测-辩",动词层级递进。
- **ILO2↔TLA2**: TODO1 填空 + Drill1 Worked-Faded + Socratic → 是否训练"分析+形式化"? **是**。Worked-Faded 从示范到独立解,逐步释放脚手架。
- **ILO3↔TLA3**: TODO2-3 + Drill2-3 + Socratic → 是否训练"构建+观察"? **是**。真实库上机 + 轨迹提取,可观察。
- **ILO4↔TLA4**: TODO5 + Socratic + C7 → 是否训练"实现+理解"? **是**。代码实现 + 概念 recall 双轨。
- **ILO5↔TLA5**: TODO6 + Drill4 + Socratic → 是否训练"实现+对比+理解边界"? **是**。同一任务双范式对比。
- **ILO6↔TLA6**: notes.md 天道推演 + Drill3/4 因果标注 + Socratic → 是否训练"分析+识别"? **是**。因果链标注可观察。

**Feed Up 结论**: 所有 ILO 都有 >=1 个 TLA 直接训练,无悬空 ILO。

### 自检 2: AT 是否测量 ILO? (Feed Back, 向下对齐)

- **ILO1↔AT1**: D1 自评 + Socratic 后测 + C1 recall → 是否测量"解释+区分+判断"? **是**。D1 要求复述+示例,Socratic 要求口头判断。
- **ILO2↔AT2**: solution TODO1 + Drill1 阶段3 + C2 → 是否测量"分析+形式化"? **是**。阶段3 独立解 AgentState 是可执行评估。
- **ILO3↔AT3**: solution TODO2-3 + Drill3 阶段3 + C3/C6 → 是否测量"构建+观察轨迹"? **是**。轨迹提取 + 因果标注是可观察产出。
- **ILO4↔AT4**: solution TODO5 + Drill3 多轮验证 → 是否测量"实现+理解"? **是**。多轮续接验证是功能测试。
- **ILO5↔AT5**: solution TODO6 + Drill4 阶段3 300字 → 是否测量"实现+对比+边界"? **是**。300字分析是可评量产出。
- **ILO6↔AT6**: Poster + exit artifact → 是否测量"分析+识别"? **是**。因果链图 + 不可逆点标注是可观察产出。

**Feed Back 结论**: 所有 ILO 都有 >=1 个 AT 测量,且 AT 产出可观察(代码/轨迹/文字/图),无主观打分。

### 自检 3: 不经 TLA 能过 AT 吗? (Feed Forward, 前瞻对齐)

> **关键检验**: 若学生不参加任何 TLA,仅靠先验知识能过 AT,则对齐失败(AT 太易或与 TLA 无关)。

- **AT1 (D1+Socratic+C1)**: 不读 notes.md 自主性谱系表,能否过? **难**。L0-L4 五级名称是本单元特有框架,先验概率低。**对齐成立**。
- **AT2 (TODO1+Drill1阶段3+C2)**: 不做 TODO1 填空 + 不做 Drill1 Worked-Faded,能否过? **难**。pydantic BDI Schema 的营销语义字段需要 TLA 训练。**对齐成立**。
- **AT3 (TODO2-3+Drill3阶段3+C3/C6)**: 不做 TODO2-3 + 不做 Drill2-3,能否过? **难**。LangChain `@tool` + LangGraph `create_react_agent` 是真实库 API,需上机训练。**对齐成立**。
- **AT4 (TODO5+Drill3多轮)**: 不做 TODO5,能否过? **可能**。MemorySaver API 简单,先验强学生可能猜对。**风险点** → 缓解:Drill3 多轮续接验证要求 Belief 状态正确恢复,不是简单 API 调用。**缓解后对齐成立**。
- **AT5 (TODO6+Drill4阶段3+C5)**: 不做 TODO6 + 不做 Drill4,能否过? **难**。Plan-Execute vs ReAct 步数对比需真实跑过。**对齐成立**。
- **AT6 (Poster+exit)**: 不读天道推演 + 不做 Drill3/4 因果标注,能否过? **难**。因果节点+不可逆点标注需 TLA 训练。**对齐成立**。

**Feed Forward 结论**: 6 个 ILO 中 5 个对齐牢固,1 个(ILO4/AT4)有风险但已通过 Drill3 多轮验证缓解。无需重新设计。

---

## 三、Mastery 阈值总览

| ILO | mastery_threshold | 测量方式 | 未达标的补救 |
|-----|---|---|---|
| ILO1 | >=80% (L0-L4 名称+示例各对1) | D1+Socratic+C1 | 重读 notes.md § 关键回顾1 + C1 卡重排 |
| ILO2 | >=80% (三模型字段+营销语义) | TODO1+Drill1阶段3+C2 | Drill1 weak_loop 回退 Worked |
| ILO3 | >=80% (轨迹>=2轮+契约四要素) | TODO2-3+Drill3阶段3 | Drill2/3 weak_loop |
| ILO4 | >=80% (多轮续接 Belief 正确) | TODO5+Drill3多轮 | TODO5 重做 + C7 卡 |
| ILO5 | >=80% (步数对比+边界判断) | TODO6+Drill4阶段3 | Drill4 weak_loop |
| ILO6 | >=80% (>=2不可逆点+因果节点) | Poster+exit | 天道推演章重读 + 1:1 答疑 |

---

*本文件 v6.0 学习科学层新增,不修改 v5.0 任何文件。设计依据:Biggs(1996) constructive alignment / Bloom 可观察动词 / mastery learning(Bloom 1968)/ 三阶反馈 Hattie & Timperley(2007)。*
