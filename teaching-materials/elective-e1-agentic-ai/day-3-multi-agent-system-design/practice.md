---
unit: E1-D3
title: 多Agent系统设计 · 刻意练习 (Deliberate Practice)
version: v6.0
based_on: Ericsson + MIT OCW CS229 pset0 + Harvard/Stanford worked-faded
---

# 多Agent系统设计 · 刻意练习手册

> 配套 [`notes.md`](./notes.md) v5.0 + [`starter.ipynb`](./starter.ipynb) 6 个 TODO。
> 所有 drill 的 `feedback_rule` 均绑定本单元真实库 (LangGraph `StateGraph` / networkx / pydantic `AgentMessage`) 与真实场景 (B2B SaaS 营销多Agent协作)。

## skill_target

**可观察、可评估的一句话技能**: 给定一个 B2B 营销任务 Brief, 学员能独立用 `LangGraph.StateGraph` + `add_conditional_edges` 构建一个 supervisor 中心化多Agent拓扑 (researcher/strategist/writer/reviewer), 用 pydantic 定义 `AgentMessage` 三层协议 (传输/格式/语义), 并用 `networkx` 计算度中心性与连通性, 识别瓶颈Agent与单点故障, 在 90 分钟内跑通并产出 300 字涌现行为分析 (引用天道推演沙盘映射)。

## diagnostic (CS229 pset0 式先测, 探测先验缺口)

> 3 道先测题, 不计分, 仅定位盲点。每题 60 秒直觉作答。

**D1 (协议层)**: A2A 协议 (Google 2025) 与 MCP 协议 (Anthropic) 各解决什么层的连接？若你的多Agent系统既要跨框架协作又要复用工具, 二者是替代还是互补？写出你的直觉判断。

**D2 (拓扑选型)**: 营销场景「调研->策略->文案->审核」若采用「辩论模式」而非「流水线」, 在 convergence (收敛性) 与 latency (延迟) 上分别会付出什么代价？中心化与去中心化各自的关键失败模式是什么？

**D3 (涌现度量)**: 若 supervisor 节点的 networkx `degree_centrality=1.0` 而其他Agent均为 0.2, 这说明拓扑是什么形状？这种拓扑在「决策质量」与「单点故障」两个维度上各打几分？天道推演的「关键因果节点」对应 networkx 哪个指标？

## subskills (3 个子技能拆解)

- **S1 协议设计子技能**: 用 pydantic 定义 `AgentMessage` (含 sender/receiver/msg_type/payload/timestamp), 区分 `MessageType` 枚举 (REQUEST/RESPONSE/NOTIFY/NEGOTIATE/VOTE), 能解释三层协议 (传输同步异步 / 格式JSON vs NL / 语义协商投票) 与 A2A/MCP 的互补关系。
- **S2 拓扑构建子技能**: 用 `StateGraph` 定义 supervisor 中心化与 team 去中心化两种拓扑, 用 `add_conditional_edges` 实现路由 (基于 `next_agent` 字段), 能调试 supervisor 死循环与 team 不收敛。
- **S3 涌现分析子技能**: 用 networkx 将 Agent 视为节点、消息流视为边, 计算 degree_centrality / connectivity / 关键路径, 识别瓶颈Agent, 用天道推演的沙盘多分支方法预测不同拓扑下的涌现决策质量与通信开销。

## drills (>=3, 每个含 drill_id/difficulty/reps_required/feedback_rule/worked_faded 三阶段)

### drill_id: D-PROTO-01
- **difficulty**: 2
- **reps_required**: 3
- **绑定真实库**: pydantic v2 + LangGraph `MultiAgentState` (TypedDict)
- **任务**: 定义 `AgentMessage` (pydantic BaseModel) 与 `MessageType` 枚举 (REQUEST/RESPONSE/NOTIFY/NEGOTIATE/VOTE) 与 `MultiAgentState` (TypedDict, 含 messages/next_agent/current_agent/task_done)。再写一段 `negotiate()` 函数模拟 Content Agent 与 Compliance Agent 的协商语义。
- **worked_faded**:
  - 阶段1 (Worked 完整示范): 学员阅读 `solution.ipynb` TODO1 区段的完整 `AgentMessage` 类定义, 教师逐行解释 `msg_type: MessageType` 字段的语义层意义。
  - 阶段2 (Faded 部分填空): 学员在 `starter.ipynb` TODO1 中补全 `MessageType` 枚举的 5 个值与 `MultiAgentState` 的 `next_agent` 字段类型注解。
  - 阶段3 (Independent 独立解): 学员独立新增第 6 种 `MessageType.DELEGATE` (层级委托语义), 并写一段 docstring 解释它与 `NOTIFY` 的语义差异。
- **feedback_rule**: 自动检查 pydantic 模型能否 `parse_obj` 通过 5 种 msg_type 样例; 若失败, 提示「检查 `msg_type` 是否为 `MessageType` 枚举而非 `str` (强类型是 A2A 互操作的基础)」; 若 `negotiate()` 未体现多轮协商, 提示「协商语义需包含 propose->counter->accept/reject 三态, 单轮是 NOTIFY 不是 NEGOTIATE」。

### drill_id: D-TOPO-02
- **difficulty**: 4
- **reps_required**: 4
- **绑定真实库**: LangGraph `StateGraph` + `add_conditional_edges` + 4 个营销 Agent (researcher/strategist/writer/reviewer) + supervisor
- **任务**: 用 `StateGraph(MultiAgentState)` 构建两种拓扑: (a) supervisor 中心化 (supervisor 路由到 4 个 Agent, Agent 回流 supervisor); (b) team 去中心化 (Agent 间直接传递 `AgentMessage`, 无中心协调者)。每种拓扑需能跑通 2 轮迭代。
- **worked_faded**:
  - 阶段1 (Worked): 教师在白板画出 supervisor 拓扑的有向图 (节点+边), 解释 `add_conditional_edges(supervisor, lambda s: s["next_agent"], {"researcher":"researcher","strategist":"strategist",...})` 的路由字典含义。
  - 阶段2 (Faded): 学员在 `starter.ipynb` TODO3 中补全 supervisor 节点函数与条件边路由字典 (字典 key 已给, value 留空)。
  - 阶段3 (Independent): 学员独立实现 TODO4 team 去中心化拓扑, 并选择合适的共识机制 (投票/权威/协商) 让 4 个 Agent 在无 supervisor 时收敛。
- **feedback_rule**: 跑 `graph.compile().invoke(initial_state)` 必须返回终态; 若 supervisor 死循环 (next_agent 永远不为 END), 提示「检查 supervisor 是否在 task_done=True 时返回 `END` (因果链不可逆点)」; 若 team 拓扑不收敛, 提示「无 supervisor 的 team 必须显式选共识机制, 营销审核推荐权威机制 (Compliance Agent 终决), 看笔记关键回顾4」。

### drill_id: D-EMERGE-03
- **difficulty**: 5
- **reps_required**: 3
- **绑定真实库**: networkx (DiGraph / degree_centrality / connected_components)
- **任务**: 将 D-TOPO-02 的两种拓扑分别转为 `nx.DiGraph` (Agent=节点, AgentMessage=有向边), 计算 (a) supervisor 与每个 Agent 的 `degree_centrality`, (b) 弱连通分量数, (c) 最长关键路径长度。再用天道推演的「沙盘多分支」方法预测: 若移除 supervisor 节点, 拓扑的连通性如何变化？涌现决策质量是上升还是下降？
- **worked_faded**:
  - 阶段1 (Worked): 教师展示 supervisor 拓扑的 `nx.degree_centrality` 输出 `{supervisor:1.0, researcher:0.2, ...}` 并解释「supervisor 是星型拓扑 hub, 单点故障即全盘瘫痪」。
  - 阶段2 (Faded): 学员补全 team 拓扑的 DiGraph 构建代码与 `degree_centrality` 调用 (函数名已给, 参数留空)。
  - 阶段3 (Independent): 学员独立写 300 字涌现分析: 对比两种拓扑在「决策质量 vs 通信开销 vs 单点故障」三维的权衡, 用天道推演「因果链追踪」视角说明为何 supervisor 拓扑在合规严格场景更优。
- **feedback_rule**: networkx 输出必须为 dict 且 supervisor 的 centrality 在中心化拓扑应 >=0.8, 在 team 拓扑应 <=0.5; 若不符, 提示「检查你的边方向: AgentMessage 是 sender->receiver 有向边, 反向会让 centrality 失真」; 若涌现分析未引用天道推演, 提示「Day3 核心特色是沙盘↔多Agent同构, 必须出现『沙盘』『因果链』『关键节点』等天道推演术语, 见 notes.md 天道推演视角表」。

## progressive_project (CS230 式渐进交付)

> 把 6 个 TODO 重组为 CS230 式四阶段交付, 每阶段独立可评。

| 阶段 | 交付物 | 对应 TODO | 评分权重 | mastery_threshold |
|------|--------|----------|---------|------------------|
| **proposal** (Day3 当天交) | 1 页 PDF: 描述你要建模的营销多Agent场景 (Brief/Agent角色/选哪种协作模式/为什么), 引用 notes.md 五种模式决策树 | (无 TODO, 设计层) | 15% | >=70% |
| **milestone** (Day3 +3天) | `starter.ipynb` TODO1+TODO2+TODO3 完整跑通: 协议定义 + 4 Agent 节点 + supervisor 中心化拓扑 | TODO1-3 | 30% | >=80% |
| **final** (Day3 +7天) | `starter.ipynb` 全 6 TODO 跑通 + 300 字涌现分析 (含 networkx 指标 + 天道推演映射) | TODO4-6 | 40% | >=80% |
| **poster** (Day3 +10天) | 1 页 A3 海报: 两种拓扑对比图 (networkx 可视化) + 涌现行为量化表 + 1 段「天道推演↔多Agent仿真」同构说明 | (综合) | 15% | >=70% |

## interleaving (交叉排布, 不块状)

> 不按 D-PROTO-01 -> D-TOPO-02 -> D-EMERGE-03 顺序块状刷, 而是交叉以促进迁移 (Rohrer 2007)。

**A=协议 / B=拓扑 / C=涌现**, 推荐 9 次练习的交叉顺序:

```
A1 B1 C1   (第一轮: 各 drill 阶段1 Worked)
B2 C2 A2   (第二轮: 各 drill 阶段2 Faded, 顺序打乱)
C3 A3 B3   (第三轮: 各 drill 阶段3 Independent, 顺序再打乱)
```

**理由**: 协议(A)是拓扑(B)的边, 拓扑(B)是涌现(C)的图, 三者环环相扣但认知负荷不同 (A 记忆为主, B 工程为主, C 推理为主)。交叉让大脑每次切换都需重新激活上下文, 强化远迁移; 块状刷会产生「同一上下文内的虚假流畅感」(Bjork desirable difficulty)。

## retry_policy (CS230 式)

- **10 free late days**: 全学期累计 10 天迟到不扣分 (跨 Day 共享池), 鼓励试错而非赶工。
- **失败重试不罚分**: milestone 若 <80%, 可在 final 截止前重交一次, 取最高分 (前提: 必须附 50 字复盘说明上次失败原因, 命中天道推演「反馈学习」机制)。
- **weak_loop 触发时不计 retry**: 连续 2 次同一 drill 失败进入弱项循环, 不消耗 retry 配额 (见下)。

## weak_loop (连续2次失败触发)

> 当学员在同一 drill_id 上连续 2 次未达 mastery_threshold, 自动触发弱项循环:

1. **回退**: 暂停当前 drill, 回到该 drill 的阶段1 (Worked 示范), 重新阅读 `solution.ipynb` 对应 TODO 区段。
2. **补充 worked example**: 教师额外提供 1 个 worked example (如 D-TOPO-02 触发, 则提供「2 Agent 流水线」的极简完整示范, 而非 4 Agent 中心化)。
3. **重练阶段2**: 用补充 worked example 重新做 Faded 阶段, 教师在线 1v1 答疑 (15 分钟, 限频每天 1 次, 见 tutorial.ipynb)。
4. **解禁条件**: 阶段2 通过后才能再做阶段3 Independent, 否则循环再次触发 (最多 3 次, 第 3 次触发转 1v1 教师面谈)。

**弱项循环的元价值**: 这是天道推演的「反馈学习」能力在练习系统的实例化——记录假设 (你以为会了), 追踪偏差 (连续失败), 更新因果模型 (回退+补 worked), 避免重复犯错。

---

*本刻意练习手册为 v6.0 学习科学层新增, 不修改 v5.0 的 notes.md/starter.ipynb/solution.ipynb/reading.md/data。*
*最后更新: 2026-07-26*
