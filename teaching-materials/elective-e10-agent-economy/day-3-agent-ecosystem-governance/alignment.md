# alignment.md - Day 3 Agent生态治理 · 建构对齐 (v6.0)

> 基础理论: Biggs constructive alignment (ILO↔TLA↔AT) + Bloom mastery learning + Hattie visible learning.
> 本文件确保"预期学习产出 -> 教学学习活动 -> 评估任务"三者对齐, 杜绝"未训练却能过"的虚浮评估。

---

## ILO↔TLA↔AT 对齐矩阵 (>=3 行)

> ILO = Intended Learning Outcome (预期学习产出)
> TLA = Teaching & Learning Activity (教学学习活动, 引用 starter/drill/tutorial)
> AT = Assessment Task (评估任务, 引用 solution/tutorial 后测)
> mastery_threshold = 达标线 (>=80% 视为掌握)

| ILO (预期学习产出) | TLA (教学学习活动) | AT (评估任务) | mastery_threshold |
|------|------|------|------|
| **ILO1**: 能用 `pydantic` 定义 Agent 平台治理规则的 4 类 schema 契约 (AdmissionRule/RevenueShare/PenaltyRule/ReputationScoring), 支持 API Economy 2.0 可发现治理声明 | • 阅读 notes.md § 关键回顾4 (激励4原则) <br>• 完成 `starter.ipynb` TODO1 (pydantic 4 schema) <br>• 练习 `practice.md` drill D1 (3 阶段 worked-faded) <br>• 参加 tutorial.ipynb Socratic 第 1-2 轮追问 | • `solution.ipynb` TODO1 后测: 4 schema 全部通过 `model.validate()` <br>• practice.md D1 阶段3 独立解: 写出 `PenaltyRule` 与 `ReputationScoring` 并 `model_dump_json()` 输出 <br>• tutorial.ipynb 第 1 次苏格拉底回应质量评分 | >= 80% (4 schema 字段完整 + 归一约束正确 + json 输出可被其它 Agent 解析) |
| **ILO2**: 能用 `networkx` 构建 Agent 生态网络 (平台=hub/Agent=节点/A2A-MCP=边), 计算度分布/聚类系数/核心-边缘/中心性, 识别单点故障风险 | • 阅读 notes.md § 真实库1 (networkx) <br>• 完成 `starter.ipynb` TODO2+TODO3 (构建+分析) <br>• 练习 `practice.md` drill D2 (3 阶段 worked-faded) <br>• 参加 tutorial.ipynb Socratic 第 3-4 轮追问 (反例: 如果 hub 全部失效会怎样) | • `solution.ipynb` TODO2+TODO3 后测: MultiDiGraph 含 7 个真实平台 (Coze/Dify/LangGraph/GPT Store/HF Spaces/MCP/A2A) <br>• practice.md D2 阶段3 独立解: 100 字结论引用具体 betweenness 数值标注单点故障 <br>• tutorial.ipynb 第 2 次苏格拉底回应 | >= 80% (拓扑图含 7 hub + 3 类中心性数值 + 单点故障标注有数值依据) |
| **ILO3**: 能用 `mesa` 仿真 30 agents/15 ticks 对比"严准入+高分润"vs"宽准入+低分润"两种治理规则的 Gini/成交率/欺诈率/平台收入, 并用 `numpy-financial` 算 12 月 NPV | • 阅读 notes.md § 真实库2+4 (mesa+numpy-financial) 与天道推演×生态治理沙盘 <br>• 完成 `starter.ipynb` TODO4+TODO5 (mesa 仿真 + NPV 估值) <br>• 练习 `practice.md` drill D3 (4 reps, 难度 5) <br>• 参加 tutorial.ipynb Socratic 第 5+ 轮追问 (贝叶斯后验分布解读) | • `solution.ipynb` TODO4+TODO5 后测: 两种治理各 5 次 run 的 Gini 均值±std + 12 月 NPV 对比 <br>• practice.md D3 阶段3 独立解: 300 字分析引用 Gini 与 NPV 证据 <br>• tutorial.ipynb 第 3 次苏格拉底回应 | >= 80% (mesa 跑通 + Gini 差 >=0.05 + NPV 差 >=10% + 300 字分析有数值证据) |
| **ILO4**: 能用天道推演三时间线 (immediate 月/near 年/far 3 年) 推演 2026-2028 年 Agent 平台在 MCP+A2A 协议下的演化走向, 标注假设与盲点 | • 阅读 notes.md § 天道推演×生态治理沙盘 + 2026 前沿 (MCP/A2A) <br>• 练习 `practice.md` drill D4 (天道推演整合) <br>• 参加 tutorial.ipynb Socratic 全程追问 (尤其 far 3 年线) | • practice.md D4 阶段3 独立解: MCP vs OpenAI GPT Store 三时间线推演 <br>• progressive_project 的 poster: 必须含 far 3 年线推演假设与盲点 <br>• tutorial.ipynb exit artifact: 2-3 个盲点 + 推荐复习单元 | >= 80% (三时间线齐全 + far 涉及 MCP+A2A 演化 + 至少 3 个标注盲点) |

---

## 3 自检问题 (Feed Up / Feed Back / Feed Forward)

### 自检 1 (Feed Up): TLA 是否训练 ILO?

- ILO1 (pydantic schema) 的 TLA 是否真的训练了 schema 定义? - 是。`starter.ipynb` TODO1 + drill D1 三阶段 worked-faded + tutorial 苏格拉底追问, 三层都在练 pydantic 字段约束、归一化、`model_dump_json()`。
- ILO3 (mesa+NPV) 的 TLA 是否真的训练了仿真+估值? - 是。但需确认: 学生是否真的跑通了 30 agents/15 ticks? 若只读 mesa 文档而不跑, TLA 未训练 ILO。**自检结论**: tutorial.ipynb 的 pre-tutorial task 必须要求学生提交一段 mesa `step()` 代码截图, 否则 TLA 未真正训练 ILO3。

### 自检 2 (Feed Back): AT 是否测量 ILO?

- ILO2 (networkx 拓扑) 的 AT 是否真的测量了"识别单点故障"? - 是, 但要警惕虚浮。`solution.ipynb` TODO3 后测要求"100 字结论引用具体 betweenness 数值", 这测的是识别能力。若学生只交了一张 matplotlib 图而无数值引用, 则 AT 未真正测量 ILO2 的"识别单点故障"维度。**自检结论**: 评分量规必须明确"无 betweenness 数值 = 不达标"。
- ILO4 (天道推演) 的 AT 是否真的测量了三时间线推演? - 需检查。practice.md D4 阶段3 要求"far 3 年必须涉及 MCP+A2A 协议演化", 但若学生只抄 notes.md 的 MCP/A2A 段落而未做推演, AT 可能误判为达标。**自检结论**: tutorial.ipynb 苏格拉底第 5+ 轮必须追问"如果 MCP 2027 年被某大厂收购, 你的 far 3 年推演如何变化?" - 用反事实追问测真理解。

### 自检 3 (Feed Forward): 不经 TLA 能过 AT 吗? 若能 = 对齐失败

- 不经 TLA 能过 ILO1 的 AT (pydantic schema 后测) 吗? - **理论上不能**。pydantic v2 的 `Field(ge=0, le=1)` 约束、`model_dump_json()` 输出, 不实际操作过很难一次写对。**风险点**: 若学生有 pydantic v1 经验, 可能跳过 TLA 直接过 AT - 因此 tutorial 苏格拉底必须追问 "pydantic v2 与 v1 的性能差异是什么?" (v2 用 Rust 重写, 快 5-50x) 来确认真理解。
- 不经 TLA 能过 ILO3 的 AT (mesa+NPV) 吗? - **不能**。mesa 的 `DataCollector` API、`numpy-financial.npv` 签名都需要实操。**风险点**: 学生可能用 ChatGPT 生成代码直接交, 看似过 AT 但未训练 ILO。**对策**: tutorial.ipynb 要求学生口头解释自己代码中 `PlatformAgent.apply_rule()` 的逻辑, 不能解释 = 未训练 = 对齐失败, 触发 weak_loop。
- 不经 TLA 能过 ILO4 的 AT (天道推演三时间线) 吗? - **可能**。天道推演是元认知能力, 若学生只抄 notes.md 的 MCP/A2A 段落, 看似能写三时间线。**对策**: AT 评分必须看"假设标注"与"盲点标注"的具体性 - 抄袭的推演假设往往是泛泛的"市场可能变化", 真理解的推演假设是具体的"MCP 若被 Anthropic 收费会改变 0 抽成范式"。**自检结论**: 此项最易对齐失败, 需 tutorial 苏格拉底反事实追问把关。

---

## mastery 阈值与重修

- 单 ILO mastery: AT 得分 >= 80%
- 单元 mastery: ILO1+ILO2+ILO3+ILO4 全部 >= 80% + progressive_project 的 final `solution.ipynb` 6 个 TODO 全填且 mesa 仿真能跑通
- 未达 mastery 的 ILO: 触发 practice.md `weak_loop` (回退上一 drill + worked example + 间隔重复 schedule.json 对应卡片)
- 重修: 失败的 ILO 可在次周重交, 但必须附 200 字反思 (上次哪里错了、这次怎么改), 并参加一次 tutorial.ipynb 苏格拉底 tutorial

---

## 与 v5.0 基线的兼容性

本文件不修改 v5.0 的任何文件 (notes.md/data/README.md/starter.ipynb/solution.ipynb/reading.md)。
所有 AT 都引用 v5.0 已有的 `solution.ipynb` TODO 编号, 确保评估任务有锚点。
所有 TLA 都引用 v5.0 已有的 `starter.ipynb` TODO 与 v6.0 新增的 `practice.md` drill / `tutorial.ipynb` 苏格拉底。
