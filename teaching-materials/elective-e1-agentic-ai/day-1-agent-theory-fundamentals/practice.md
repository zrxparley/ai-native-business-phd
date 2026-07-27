---
unit: elective-e1-agentic-ai/day-1-agent-theory-fundamentals
version: v6.0 学习科学层
skill_target: 能用LangGraph的create_react_agent和LangChain的@tool装饰器构建一个带工具调用的ReAct营销Agent，并清晰分析Thought-Action-Observation循环轨迹中每一步的因果依据
---

# Day 1 Agent理论基础 · 刻意练习 (Deliberate Practice, Ericsson 1993)

> 设计依据: Ericsson(1993)刻意练习 + MIT CS229 pset0 先测 + Harvard/Stanford Worked-Faded三阶段 + CS230 progressive project。所有 drill 的 feedback_rule 均绑定本单元真实库(LangChain/LangGraph/pydantic)与真实工具(search_product_info / analyze_competitor / write_strategy)。

---

## 一、Diagnostic (先测, CS229 pset0 式, 3 题)

> 探测先验知识缺口。每题先独立作答,再对照 `solution.ipynb` 的 TODO1-3 自评。**不计分**,只定位盲点。

- **D1 (自主性谱系)**: 一个"按用户类型选营销策略"的Workflow属于 L0-L4 哪一级?凭什么?如果一个"反复搜索竞品-推理直到完成"的系统呢?两者本质差异是什么?
- **D2 (BDI 形式化)**: 用一句话写出 Belief/Desire/Intention 各自的哲学含义,并指出在 LLM Agent 中分别对应什么(Belief=? Desire=? Intention=?)。若一个 Agent 没有 Intention 的"坚持性",会出现什么病态行为?
- **D3 (ReAct 范式)**: Yao et al. 2022 (arXiv 2210.03629) 的 ReAct 解决了纯推理型与纯行动型 Agent 各自的什么缺陷?写出 Thought-Action-Observation 三段式的因果依赖关系(谁依赖谁)。

---

## 二、subskills (3 个子技能拆解)

| ID | 子技能 | 可观察行为 | 对应 starter TODO |
|----|--------|-----------|-----------------|
| **S1** | BDI 状态 Schema 形式化 | 用 pydantic 定义 Belief/Desire/Intention 三模型,字段含营销语义 | TODO1 |
| **S2** | @tool 工具契约定义 | 用 LangChain `@tool` 装饰器定义 search_product_info/analyze_competitor/write_strategy,docstring+参数类型即"接口契约" | TODO2 |
| **S3** | ReAct 循环轨迹因果分析 | 用 `create_react_agent` 跑通营销任务,从日志中提取 Thought-Action-Obs 序列,标注每次 Action 如何改变 Belief | TODO3-4 |

---

## 三、Drills (>=3 个, 每个 Worked-Faded 三阶段)

### Drill 1

- **drill_id**: D1-BDI-Schema
- **difficulty**: 2
- **reps_required**: 3
- **目标子技能**: S1
- **feedback_rule**: 用 pydantic `ValidationError` 校验字段缺失;对照独立教材 §Day1 BDI 表(Belief=产品知识+市场认知,Desire=营销任务,Intention=执行计划步骤);若 Intention 模型缺"步骤顺序"字段则反馈"Intention 的坚持性要求有序承诺"
- **worked_faded**:
  - **阶段1 (Worked, 完整示范)**: 给出完整 `class Belief(BaseModel): product: str; target_segment: str` + `class Desire(BaseModel): task: str; success_metric: str` + `class Intention(BaseModel): steps: List[str]`,讲师逐行解释字段如何映射营销语义
  - **阶段2 (Faded, 部分填空)**: 给出 Belief/Desire 完整,Intention 仅留 `class Intention(BaseModel): ____: List[str]` + docstring 框架,学生填字段名与类型
  - **阶段3 (Independent, 独立解)**: 学生独立定义第四个模型 `AgentState(BaseModel): belief: Belief; desire: Desire; intention: Intention; current_step: int`,并解释为何 current_step 必须独立于 Intention

### Drill 2

- **drill_id**: D2-Tool-Contract
- **difficulty**: 3
- **reps_required**: 3
- **目标子技能**: S2
- **feedback_rule**: 用 LangChain `@tool` 装饰器签名校验;检查 docstring 是否含"工具名+用途+参数+返回"四要素(LLM 看到的"接口契约");若 write_strategy 的 docstring 缺"不可逆点"提示则反馈"write_strategy 执行后文件已写入,撤销需额外操作--契约必须警示不可逆性"
- **worked_faded**:
  - **阶段1 (Worked)**: 完整示范 `@tool def search_product_info(product_name: str) -> str: """搜索产品信息..."""`,讲师标注 docstring 四要素
  - **阶段2 (Faded)**: 给出 `analyze_competitor` 的函数签名与 docstring 框架,学生填参数类型与 docstring 用途段
  - **阶段3 (Independent)**: 学生独立定义 `write_strategy`,docstring 必须含"不可逆点:文件写入后需手动撤销"警示

### Drill 3

- **drill_id**: D3-ReAct-Trace
- **difficulty**: 4
- **reps_required**: 2
- **目标子技能**: S3
- **feedback_rule**: 用 `create_react_agent` 跑通营销任务后,从 `MemorySaver` checkpoint 提取轨迹;轨迹必须含 >=2 轮 Thought-Action-Observation;若 Action 选择错误(如未先 search_product_info 就 analyze_competitor)则反馈"ReAct 的因果依赖:每次 Action 改变 Belief,影响下一次 Thought--信息不足时必须先检索"
- **worked_faded**:
  - **阶段1 (Worked)**: 讲师跑通完整 ReAct 轨迹(Thought1: 需了解竞品 -> Action1: search_product_info -> Obs1: 透肌精华299元 -> Thought2: 分析雅诗兰黛 -> Action2: analyze_competitor -> Obs2: 小棕瓶760元市占18% -> Thought3: 信息足够 -> Action3: write_strategy),逐条标注因果依赖
  - **阶段2 (Faded)**: 给出轨迹的前两轮,学生预测第三轮 Thought 应该是什么,并写出 Action3
  - **阶段3 (Independent)**: 学生独立跑一个新营销任务,提取轨迹,用天道推演框架标注"不可逆点"和"因果节点"

### Drill 4 (拓展)

- **drill_id**: D4-Plan-Execute-VS-ReAct
- **difficulty**: 5
- **reps_required**: 1
- **目标子技能**: S3 拓展(Plan-Execute 范式对比)
- **feedback_rule**: 用 `StateGraph` 实现 Plan-Execute;对比同一营销任务下 ReAct 与 Plan-Execute 的步数和输出质量;若 Plan 阶段前提错误则反馈"Plan-Execute 的因果节点:Plan 错误传播到所有 Execute 步骤--信息不足时 Plan-Execute 失效,应回退 ReAct 探索"
- **worked_faded**:
  - **阶段1 (Worked)**: 讲师示范完整 StateGraph(Plan 节点 -> Execute 节点序列)
  - **阶段2 (Faded)**: 给出 Plan 节点,学生填 Execute 节点的工具调用顺序
  - **阶段3 (Independent)**: 学生独立对比 ReAct vs Plan-Execute 在"信息充分"vs"信息不足"两种场景的步数差异,写 300 字分析

---

## 四、Progressive Project (CS230 式渐进交付)

| 阶段 | 交付物 | 评估标准 | 反馈来源 |
|------|--------|---------|---------|
| **Proposal** (Day1 上机前) | 选定一个营销场景(如"新品发布会策划"),写 1 页 Agent 设计草图(BDI 三要素+候选工具清单) | BDI 三要素齐全,工具 >=3 个 | 同伴互评 + 讲师 |
| **Milestone** (上机中段) | 完成 starter.ipynb TODO1-3(BDI Schema + 3 个 @tool + create_react_agent 跑通) | 能跑通 1 轮 Thought-Action-Obs | `solution.ipynb` 对照 |
| **Final** (上机结束) | 完成 TODO1-6 全部(含 MemorySaver + Plan-Execute) | 多轮对话可续,Plan-Execute 步数 < ReAct 步数(信息充分场景) | `solution.ipynb` + 自动轨迹检查 |
| **Poster** (Day1 课后) | 1 页 A4 海报:ReAct vs Plan-Execute 因果链对比图 + 天道推演盲点标注 | 因果链清晰,标注 >=2 个不可逆点 | 讲师 + 全班 |

---

## 五、Interleaving (交叉排布, 非 block)

> 不要 A1A2A3 B1B2B3 C1C2C3 块状练习。按以下交叉顺序,促进迁移:

```
A1 B1 C1   # 第一轮:每个子技能各 1 次,建立广度
B2 C2 A2   # 第二轮:打乱顺序,强化检索
C3 A3 B3   # 第三轮:再次打乱,接近 mastery
```

其中 A=S1(BDI Schema), B=S2(@tool 契约), C=S3(ReAct 轨迹分析)。
- **A1=Drill1 阶段1**, A2=Drill1 阶段2, A3=Drill1 阶段3
- **B1=Drill2 阶段1**, B2=Drill2 阶段2, B3=Drill2 阶段3
- **C1=Drill3 阶段1**, C2=Drill3 阶段2, C3=Drill3 阶段3

每次切换子技能时,先做 30 秒 retrieval(合上材料默写上一次该子技能的关键点),再开始新一轮。

---

## 六、Retry Policy (CS230 式)

- **10 free late days**: 任何 drill/poster 可延期,累计 10 天内不扣分
- **失败重试不罚分**: Drill 未达 feedback_rule 标准,可无限重试,取最高分
- **weak_loop 触发条件**: 连续 2 次 drill 失败(同一子技能)
- **weak_loop 动作**: 回退到上一个 drill 的 Worked 阶段重看完整示范 + 补充 1 个 worked example(讲师提供) + 再尝试当前 drill 的 Faded 阶段

---

## 七、Weak Loop (弱项循环)

```
if 连续2次 drill 失败(同一子技能 S):
    回退到 S 的上一个 drill 的 Worked 阶段(完整示范)
    补充 1 个 worked example(讲师新增,与本单元营销场景相关)
    重新尝试当前 drill 的 Faded 阶段(部分填空)
    若仍失败 -> 触发 1:1 答疑(tutorial.ipynb Socratic 追问盲点)
```

例:Drill 3 (ReAct 轨迹分析) 连续 2 次未达"轨迹含 >=2 轮 Thought-Action-Obs"标准 -> 回退到 Drill 2 的 Worked 阶段重看 @tool 完整示范 -> 补充 worked example(讲师现场跑一个简化 ReAct 轨迹) -> 再尝试 Drill 3 Faded 阶段。

---

*本文件 v6.0 学习科学层新增,不修改 v5.0 任何文件。设计依据:Ericsson(1993)刻意练习 / MIT CS229 pset0 / Harvard Worked-Faded / CS230 progressive project / 天道推演因果链分析。*
