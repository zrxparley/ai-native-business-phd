---
unit: U5-D1
topic: Agent系统架构设计 (ReAct/Plan-Execute/Reflection/Tool Calling/Memory/MCP)
version: v6.0 学习科学层
skill_target: 能在 LangGraph 中独立设计并实现一个带工具调用、短期记忆与 Reflection 自检的 ReAct Agent, 并用 Anthropic 五模式论证"何时用 Workflow vs Agent"
---

# Day 1 刻意练习 (Deliberate Practice, Ericsson + MIT CS229/CS230 + Harvard/Stanford)

> 本文件锚定 Day 1 上机交付物 (`starter.ipynb` 6 个 TODO / `solution.ipynb`), 把"看完讲义能复述"逼成"在真实 LangGraph 库上能跑通"。所有 drill 的 feedback_rule 引用本单元真实库/数据集, 不是通用模板。

---

## 0. diagnostic (CS229 pset0 式先测, 不计分, 探测先验缺口)

> 限时 15 分钟, 闭卷, 不许翻 notes.md。每题先写"我确信 / 我猜的 / 我不会", 据此选 drill 起点。

- **D1**. 给定以下 LangGraph 输出片段, 指出 Agent 下一时刻应进入哪个状态? 写出 Thought→Action→Observation 三元组。
  ```
  Thought: 用户要推护肤品, 需算 ROI
  Action: ???
  ```
  选项: (a) `calculate_roi(revenue=598000, cost=66000)` (b) `write_strategy(...)` (c) `analyze_sentiment(...)` (d) 直接生成最终答案

- **D2**. 下面 `@tool` 定义有一处会让 LLM 误调或漏调, 找出来并修:
  ```python
  @tool
  def calc(x, y):
      return (x - y) / y * 100
  ```

- **D3**. 你的 ReAct Agent 在第 4 轮还在调 `calculate_roi` 反复算同一组数。这违反 Anthropic 五模式中的哪条直觉? 该转 Workflow 还是加 Reflection? 给出 1 句理由。

> 评分钥匙: D1 选 (a) 且能写出 `Observation: ROI=806.1%`; D2 指出"无 docstring + 参数名无语义 + 无类型注解", 修法至少含 docstring+`revenue: float, cost: float`; D3 提到"Workflow 优先 / Agent 非确定性 / 死循环"任一关键词即对。

---

## 1. subskills (3 个可独立训练的子技能)

| ID | 子技能 | 可观察行为 | 对应 starter TODO |
|----|--------|------------|-------------------|
| S1 | 工具契约设计 (Tool Contract) | 能用 `@tool` + docstring + 类型注解定义让 LLM 正确选择的工具, 写出会"骗到 LLM"的反例 | TODO1 |
| S2 | ReAct loop 编排 (ReAct Orchestration) | 能用 `create_react_agent` + `MemorySaver(checkpointer)` 跑通多轮 Thought-Action-Observation, 解释 `thread_id` 隔离 | TODO2-4 |
| S3 | 架构选型论证 (Architecture Tradeoff) | 能在 ReAct/Plan-Execute/Reflection/Anthropic 五模式中按可控性/延迟/复杂度举证选型, 指出何时该 Workflow | TODO5-6 |

---

## 2. drills (>=3, 每个 difficulty 1-5, reps_required, feedback_rule, worked_faded 三阶段)

### drill_id: DR1
- **subskill**: S1 工具契约设计
- **difficulty**: 2
- **reps_required**: 4 (独立解 4 次正确, 每次换不同营销工具)
- **worked_faded**:
  - Stage A (Worked): 完整示范 `calculate_roi(revenue: float, cost: float) -> str` 含 docstring, 直接抄
  - Stage B (Faded): 给 `analyze_sentiment` 只留 docstring, 学员补 `@tool`+签名+返回
  - Stage C (Independent): 学员独立写 `write_strategy(path: str, content: str) -> str`
- **feedback_rule** (领域特定): 用 LangChain `tool` 装饰器 + 真实 LLM 调用验证"LLM 是否按 docstring 正确选工具"。若 LLM 选错或漏调, 反馈定位到"docstring 缺少营销语义 / 参数名无业务含义 / 返回类型非 str"。可对照 `solution.ipynb` TODO1 的契约格式逐字段比对。

### drill_id: DR2
- **subskill**: S2 ReAct loop 编排
- **difficulty**: 4
- **reps_required**: 3
- **worked_faded**:
  - Stage A: 完整给出 `create_react_agent(model, tools, checkpointer=MemorySaver())` + `config={"configurable":{"thread_id":"u1"}}` 的可跑片段, 学员抄
  - Stage B: 把 `thread_id` 留空, 把 `MemorySaver` 换成 `None`, 学员诊断"为什么多轮对话失忆"
  - Stage C: 学员独立把 Day 1 营销任务接上 MemorySaver, 跑 2 轮并打印 messages 历史
- **feedback_rule** (领域特定): 跑 `agent.invoke({"messages":[...]}, config)` 第二轮, 若 LLM 仍问"你刚才说什么"=短期记忆未生效, 反馈指向 `thread_id` 不一致 或 `checkpointer=None`。对照 `solution.ipynb` TODO4 的 MemorySaver 接线, 逐参数 diff。

### drill_id: DR3
- **subskill**: S3 架构选型论证
- **difficulty**: 5
- **reps_required**: 2
- **worked_faded**:
  - Stage A: Worked example 完整给出"营销 ROI 固定流水线 → 选 Prompt Chaining 而非 Agent"的 3 句论证 (可控性高 / 延迟低 / 步骤固定)
  - Stage B: 给"动态竞品分析"场景, 学员只补"为什么该用 Orchestrator-Workers 而非 ReAct"2 句
  - Stage C: 学员独立为"品牌危机公关策略生成"选模式, 必须同时给出: 选哪个 / 不选哪个 / 1 句反例
- **feedback_rule** (领域特定): 论证必须命中 Anthropic 五模式表中的至少 2 列 (可控性/延迟/复杂度)。若学员只说"Agent 更智能"=不合格, 反馈指向"用 Workflow 优先直觉 / Evaluator-Optimizer 适合质量敏感 / Routing 适合分类"。可让学员把论证喂给 `solution.ipynb` TODO5 的 Reflection 评估者, 看是否被打回。

### drill_id: DR4 (bonus)
- **subskill**: S2 + MCP 进阶
- **difficulty**: 5
- **reps_required**: 1
- **worked_faded**:
  - Stage A: 给出 `@tool` (应用内工具) 与 MCP Server (进程外工具, JSON-RPC) 的对比表
  - Stage B: 给"营销 Agent 需接 Salesforce CRM + Slack"场景, 学员补"哪些用 @tool, 哪些走 MCP"
  - Stage C: 学员独立画一张混合工具栈图
- **feedback_rule** (领域特定): 反馈引用 notes.md "MCP 是进程外工具"段落, 若学员把"读本地文件"也塞进 MCP, 反馈指出"简单工具用 @tool, 企业系统集成用 MCP"的混合原则。

---

## 3. progressive_project (CS230 式 proposal→milestone→final→poster)

> 单一项目分 4 阶段交付, 每阶段都有可被同学/助教 review 的 artifact。最终产物可作 Day 2-5 的种子项目。

| 阶段 | 交付物 | 字段 | 评审标准 |
|------|--------|------|---------|
| **proposal** (Day 1 上半场结束) | 1 页方案 | 选题 / 工具清单 / 选哪个模式 / 1 句"为什么不用 Workflow" | 至少 3 个工具 + 1 个非 Prompt Chaining 模式 + 选型有 1 句反例 |
| **milestone** (Day 1 下半场) | `starter.ipynb` TODO1-4 跑通 | ReAct loop 跑 1 轮 + MemorySaver 多轮 | LLM 正确选工具 + `thread_id` 隔离生效 |
| **final** (Day 1 当晚) | `solution.ipynb` 改造版 + 300 字分析 | 加 Reflection (TODO5) + 工具调用顺序分析 | Reflection 至少指出 1 个真实问题 + 顺序分析含"为何先 ROI 再 sentiment" |
| **poster** (Day 2 开场 2 分钟) | 1 张图 + 2 分钟话术 | 工具栈图 + 模式选型一句话 | 同学能 30 秒内复述你的选型理由 |

---

## 4. interleaving (交叉排布, 不块状)

> 不要 S1S1S1S2S2S2S3S3S3。按下面顺序交叉, 强迫大脑每次切换都做"模式识别":

**Day 1 上半场 90 min**: DR1-A → DR2-A → DR1-B → DR3-A → DR2-B → DR1-C
**Day 1 下半场 90 min**: DR3-B → DR2-C → DR1-C(换工具) → DR3-C → DR4-A → DR2-C(换场景)
**当晚复习 30 min**: DR3-C(换场景) → DR1-C(换工具) → DR2-C(换 thread_id) → DR4-B

明文交叉序列: `DR1-A, DR2-A, DR1-B, DR3-A, DR2-B, DR1-C, DR3-B, DR2-C, DR1-C', DR3-C, DR4-A, DR2-C', DR3-C', DR1-C'', DR2-C'', DR4-B`

(A=Worked 示范, B=Faded 填空, C=Independent 独立, ' = 换场景/工具重做一次)

---

## 5. retry_policy (CS230 式, 容错鼓励迁移)

- **10 free late days**: 整个 Skill 5 共享, 不罚分。用于"我昨晚没跑通 MemorySaver, 想明天问助教再交"
- **失败重试不罚分**: 任何 drill 一次没过, 24h 内可重交, 取最高分
- **重交必须附诊断**: 重交时写 1 句"上次为什么错 + 这次改了什么", 否则不受理
- **里程碑降级**: 若 final 阶段 Reflection 没跑通, 可降级为 milestone + 200 字"Reflection 为什么没跑通"分析, 不影响 next Day

---

## 6. weak_loop (连续 2 次失败触发弱项循环)

> 触发条件: 同一 drill 连续 2 次 `feedback_rule` 判定不合格。

触发后:
1. **回退一级**: 从当前 Stage (B/C) 退回上一 Stage (A/B), 重做 1 次 worked/faded
2. **补充 worked example**: 从 `solution.ipynb` 对应 TODO 抽 1 段完整解, 学员手抄一遍并口头解释每行
3. **诊断对话**: 用 `tutorial.ipynb` 的 Socratic loop 触发 1 次限频对话, tutorial 会追问"你的 Thought-Action-Observation 在哪一步断了"
4. **复测**: 24h 后用换过场景的同 drill 再测 1 次, 通过才退出 weak_loop

例: DR2 连续 2 次 `thread_id` 没生效 → 退回 Stage A 重抄 `MemorySaver` 接线 → tutorial 追问"`thread_id` 在哪一行被赋值" → 24h 后换 `thread_id="crisis-PR-001"` 重测

---

## 7. 命中学习科学原则备忘

- **Ericsson deliberate practice**: subskills 拆解 + feedback_rule 领域特定 + reps_required
- **Worked-Faded (Renkl)**: 每 drill 三阶段, Worked→Faded→Independent
- **Interleaving (Bjork)**: A1B1C1... 不块状, 强迫模式识别
- **Retrieval practice**: diagnostic 闭卷, 每次重做都是提取而非重读
- **Mastery learning**: reps_required + weak_loop 保证达标才推进
- **Spacing**: 当晚 + 24h 后复测, 配合 `schedule.json` 的 FSRS-6 间隔
