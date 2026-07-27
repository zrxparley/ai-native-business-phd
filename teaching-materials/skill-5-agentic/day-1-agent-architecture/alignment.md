# Day 1 建构对齐矩阵 (Biggs Constructive Alignment + Mastery Learning)

> Biggs 的核心命题: ILO(Intended Learning Outcome) -> TLA(Teaching/Learning Activity) -> AT(Assessment Task) 必须三方对齐。若不经 TLA 也能过 AT, 即对齐失败。
> 本单元 mastery 阈值统一定义为"对应 AT 在限定条件下达成 >=80%"。

---

## 1. ILO ↔ TLA ↔ AT 矩阵

| ILO (预期学习产出) | TLA (教学/学习活动) | AT (评估任务) | mastery_threshold |
|-------------------|--------------------|---------------|-------------------|
| ILO1: 能用 ReAct/Plan-Execute/Reflection 三模式解释 Agent 决策, 指出营销场景适用边界 | 读 notes.md §关键回顾2 + 做 `practice.md` DR3 (架构选型论证) + `tutorial.ipynb` Socratic 追问 | `solution.ipynb` TODO5 的 300 字分析: "为何先 ROI 再 sentiment" + `practice.md` DR3-C 独立选型论证 | 选型论证命中 Anthropic 五模式表至少 2 列 (可控性/延迟/复杂度) 且含 1 句反例, >=80% 命中 |
| ILO2: 能用 LangGraph `create_react_agent` + `MemorySaver` 构建带 Tool Calling + 短期记忆的 ReAct Agent, 在营销任务上跑通 | 做 `starter.ipynb` TODO1-4 + `practice.md` DR1 (工具契约) + DR2 (ReAct loop 编排) | `starter.ipynb` TODO1-4 全部填好且 LLM 正确选工具, `thread_id` 隔离生效, 跑 2 轮多轮对话 | TODO1-4 全跑通 + LLM 工具选择顺序符合预期 + MemorySaver 多轮不失忆, 达成度 >=80% |
| ILO3: 能为营销 Agent 设计工具集, 解释工具签名如何影响 LLM 工具选择 | 做 `practice.md` DR1 (Worked->Faded->Independent 三阶段) + `tutorial.ipynb` cell2 pre-tutorial 提交 1 个工具定义 | `practice.md` DR1-C 独立写 `write_strategy` 工具 + `solution.ipynb` TODO1 三个工具契约逐字段比对 | 独立写的工具被 LLM 正确调用 (无漏调/误调) + 能指出反例工具为何骗到 LLM, >=80% |
| ILO4: 能实现 Reflection (评估者-优化者) 循环, 让 Agent 自检并改进输出 | 做 `starter.ipynb` TODO5 + `practice.md` DR3 Stage B + `tutorial.ipynb` cell5 Hattie [FEED-FORWARD] | `solution.ipynb` TODO5 Reflection 至少指出 1 个真实问题 + 改进 1 次策略输出 | Reflection 评估者指出的 >=1 问题确实成立 (非套话) + 改进后策略在 5 分制量表 >=3, 达成度 >=80% |
| ILO5: 能用 Anthropic 五模式为营销需求选型, 说明何时用 Workflow vs Agent | 读 notes.md §关键回顾5 + 做 `practice.md` DR3 + `tutorial.ipynb` cell3 Socratic "凭什么选 Agent 不选 Workflow" | `practice.md` DR3-C 独立选型 + `solution.ipynb` 300 字分析中"为何不用 Workflow"一句 | 选型同时给出: 选哪个/不选哪个/1 句反例 + 反例命中 Workflow 优先直觉, >=80% |

---

## 2. 三自检问题 (Feed Up / Feed Back / Feed Forward, Hattie)

### Q1. Feed Up (TLA 是否训练 ILO?)
- ILO1 的 TLA (`practice.md` DR3 + notes.md 关键回顾2) 是否真的训练了"三模式解释 + 适用边界"?
- 自检方法: 抽 3 个学员, 看他们做完 DR3-A (Worked) 后能否独立说出"何时选 Plan-Execute 而非 ReAct"。
- 若答不出 = TLA 训练不足, 需在 DR3 加一个 Worked example 显式对比两模式。

### Q2. Feed Back (AT 是否测量 ILO?)
- ILO2 的 AT (`starter.ipynb` TODO1-4 跑通) 是否真测量了"用 LangGraph 构建 ReAct Agent"?
- 自检方法: 把 AT 拆成"工具契约 + create_react_agent 接线 + MemorySaver 接线"3 个子分, 看每个子分是否独立可判。
- 若学员 TODO4 跑通但说不清 `thread_id` 作用 = AT 测量漏了"短期记忆隔离"维度, 需补一道口头追问。

### Q3. Feed Forward (不经 TLA 能过 AT 吗? 若能 = 对齐失败)
- ILO3 的 AT (`practice.md` DR1-C 独立写 `write_strategy`) 不经 TLA (DR1-A/B + tutorial cell2) 能过吗?
- 自检方法: 找一个没做 DR1-A/B 的学员, 直接让他做 DR1-C。若他能写出正确工具定义, 说明 AT 太弱 (会写 Python 函数就能过, 没测到"LLM 接口契约"这一 ILO 维度)。
- 修复: AT 必须包含"用真实 LLM 验证工具被正确调用"这一步, 否则对齐失败。

---

## 3. mastery_threshold 操作定义

- **>=80% 达成** = 该 ILO 对应 AT 在限定条件 (闭卷/限时/独立) 下, 评审 rubric 命中 >=80%。
- **未达 80%** = 触发 `practice.md` §6 weak_loop: 回退一级 + 补 worked example + 24h 后复测。
- **mastery 而非 curve**: 不与同学比排名, 只看是否达到 ILO 阈值。全班都达 80% 也 OK。

---

## 4. 对齐覆盖检查 (ILO 全覆盖?)

| ILO | TLA 命中 | AT 命中 | 备注 |
|-----|---------|---------|------|
| ILO1 | DR3 + notes §关键回顾2 + tutorial Socratic | DR3-C + solution 300字 | OK |
| ILO2 | starter TODO1-4 + DR1 + DR2 | starter TODO1-4 跑通 | OK |
| ILO3 | DR1 + tutorial cell2 | DR1-C + solution TODO1 比对 | OK |
| ILO4 | starter TODO5 + DR3-B + tutorial cell5 | solution TODO5 Reflection | OK |
| ILO5 | DR3 + notes §关键回顾5 + tutorial cell3 | DR3-C + solution 300字 | OK |

5 个 ILO 全部三方对齐, 无悬空 ILO, 无未对齐的 AT。
