# frontier.md (v9.0 学术前沿注入层)

> **所属**：skill-2-ai-native-arch · day-2-agent-orchestration-langgraph
> **版本**：v9.0（学术前沿注入层）
> **本单元前沿课题**：2025-2026 年企业 Agent 编排的分类框架、延迟感知执行图学习、MCP 协调的多角色解耦、拍卖式任务分配，如何更新本单元所教的 LangGraph 四编排模式（顺序/条件/循环/HITL）+ Supervisor 拓扑 + Plan-Execute。

---

## frontier_topic

本单元教 LangGraph StateGraph 的四种编排模式（顺序/条件分支/循环/HITL）+ Supervisor 条件路由 + Plan-Execute 两阶段 + MemorySaver 检查点，本质是"手工装配有状态有向图"。前沿子问题是：2025-2026 年的编排分类框架（四属性决策）、延迟感知执行图学习（LAMaS 关键路径信用分配）、MCP Orchestrator 多角色解耦、拍卖式任务分配，如何把"手工装配图"升级为"分类驱动选型 + 学习优化执行图 + 动态任务分配"。

---

## recent_papers

### 1. Design and Implementation of Agentic Orchestrations and Orchestration of Agents
- **arXiv**: https://arxiv.org/abs/2606.31518
- **作者**: Stefanie Rinderle-Ma, Juergen Mangler
- **年份**: 2026
- **摘要**: 提供 agentic orchestration 选项的分类框架，沿任务特异性、可追溯性、自主性、正确性保证等属性分类。给出不同场景的定性决策标准和通过预测光感场景 agentic 实现评估的定量指标。
- **与本单元的关联**: 本单元的"四种编排模式"是按控制流结构分类（顺序/条件/循环/HITL）；该论文按"任务特异性 × 可追溯性 × 自主性 × 正确性保证"四属性分类，为本单元 `build_campaign_graph` 的编排选型提供决策框架。

### 2. Learning Latency-Aware Orchestration for Multi-Agent Systems
- **arXiv**: https://arxiv.org/abs/2607.13359
- **作者**: Xi Shi, Mengxin Zheng
- **年份**: 2026
- **摘要**: 提出延迟感知编排框架 LAMaS，通过约束优化和关键路径感知信用分配学习执行图。端到端延迟降低 50% 以上且保持竞争性准确率，轻量推理时控制器消除冗余 agent 交互。
- **与本单元的关联**: 本单元 `build_campaign_graph` 的 research->strategy->copywriter->approval 顺序链是手工装配；LAMaS 把执行图从"手工装配"升级为"学习优化"，关键路径感知信用分配可直接优化本单元 revision_count 循环的延迟。

### 3. Decoupled Intelligence: A Multi-Agent LLM Framework for Controllable Traffic Scenario Generation in SUMO
- **arXiv**: https://arxiv.org/abs/2605.27685
- **作者**: Shuyang Li, Ruimin Ke
- **年份**: 2026
- **摘要**: 多 agent 框架自动化 SUMO 交通仿真，将流程解耦为专业化角色（Planner, Builder, Demand, Runner, Analyst），由状态持久化 Orchestrator 通过 MCP（Model Context Protocol）协调。角色消融研究表明任务成功率和参数准确率显著优于单 agent 基线。
- **与本单元的关联**: 本单元 `notes.md` 第 61 行提到"MCP 接工具，A2A 接 Agent"但本单元代码用 LangGraph State 共享通信；该论文是语料库中唯一直接用 MCP 协调多角色的 verified 论文，为本单元 A2A/MCP 互补定位提供实证。

### 4. Agora: Enhancing LLM Agent Reasoning Via Auction-Based Task Allocation
- **arXiv**: https://arxiv.org/abs/2607.09600
- **作者**: Kaiji Zhou, Ales Leonardis
- **年份**: 2026
- **摘要**: 引入激励兼容拍卖机制，将推理步骤视为可交易物品，动态分配推理任务给专家模型。Agent 基于"校正能力"竞标，确保关键逻辑路由到最有能力的求解器而非最过度自信的求解器。
- **与本单元的关联**: 本单元 Supervisor 拓扑（`route_after_approval` 条件路由）是固定路由；Agora 把"路由"从"固定条件函数"升级为"拍卖式动态竞标"，为本单元 Supervisor 拓扑提供替代方案。

### 5. ACE: Pluggable Adaptive Context Elasticizer across Agents
- **arXiv**: https://arxiv.org/abs/2606.31564
- **作者**: Ning Liao, Zihao Long
- **年份**: 2026
- **摘要**: 即插即用模块，通过在每个决策步为每个步骤分配弹性类型（raw/abstract/drop）来弹性编排历史步骤信息到 agent 上下文。适配 ReAct 和 DeepAgent 等四个 agent 框架无需训练，持续优于截断和摘要基线。
- **与本单元的关联**: 本单元 `CampaignState` 用 `Annotated[list, operator.add]` 累积 messages，无上下文管理；ACE 为 LangGraph 节点的上下文增长提供"raw/abstract/drop"弹性编排方案，直接挑战本单元 State 累积模式。

---

## critical_synthesis

这 5 篇论文共同揭示了 2025-2026 年企业 Agent 编排的**共识**：编排正从"手工装配有状态图"（LangGraph 范式）走向"分类驱动选型 + 学习优化执行 + 动态任务分配 + 弹性上下文"四维升级。领域共识是：单一编排模式（本单元的 Supervisor 条件路由）不足以应对多场景，需要"任务特异性 × 自主性 × 可追溯性 × 正确性保证"分类框架（论文 1）指导选型。**争议**在于编排优化的路径：LAMaS (2607.13359) 主张"学习执行图"（数据驱动），Agora (2607.09600) 主张"拍卖式动态竞标"（机制设计驱动），ACE (2606.31564) 主张"弹性上下文编排"（信息流驱动）--三条路径尚未统一。方法学趋势是从"静态图装配"走向"动态执行优化"。**局限**：LAMaS 的 50% 延迟降低是在特定多 agent 基准上测得，本单元的 `revision_count >= 3` 修订循环是审批驱动的非纯性能循环，LAMaS 的关键路径优化未必适用；Agora 的拍卖机制假设多个专家模型可竞标，但本单元 `OfflineMockLLM` fallback 场景下无多模型可选；ACE 的 raw/abstract/drop 三类弹性未覆盖本单元 `MemorySaver` 检查点持久化的跨会话上下文管理。此外，所有论文均未涉及本单元强调的 HITL `interrupt_before` 三步模式（invoke -> update_state -> resume）的企业治理意义--HITL 作为编排模式在学术论文中覆盖率仍低。

---

## delta_to_unit

1. **编排选型从结构分类到属性分类**：本单元 `notes.md` 第 50-55 行的"四种编排模式"按控制流结构分类（顺序/条件/循环/HITL）；论文 1 (2606.31518) 的"任务特异性 × 可追溯性 × 自主性 × 正确性保证"四属性分类为本单元 `build_campaign_graph` 选型提供决策维度--例如本单元审批节点的"可追溯性"要求高，应选 HITL 而非纯条件分支，这是本单元未显式给出的选型依据。

2. **执行图从手工装配到学习优化**：本单元 `solution.ipynb` TODO5 的 `build_campaign_graph` 手工 `add_node` + `add_edge` + `add_conditional_edges` 装配图；LAMaS (2607.13359) 通过关键路径感知信用分配学习执行图，可自动消除冗余 agent 交互--本单元 research->strategy->copywriter 的顺序链若经 LAMaS 优化，可能发现 strategy 与 copywriter 可并行而非顺序，挑战本单元"Plan-Execute 必须顺序"假设。

3. **MCP 协调多角色的实证**：本单元 `notes.md` 第 61 行"MCP 接工具，A2A 接 Agent"是概念区分；论文 3 (2605.27685) 是语料库中唯一直接用 MCP Orchestrator 协调 Planner/Builder/Demand/Runner/Analyst 五角色的 verified 论文，角色消融实验显著优于单 agent 基线--为本单元"MCP 接工具"的定位提供反例（MCP 也可协调多角色），本单元的 MCP/A2A 互补定位需更精细化。

4. **Supervisor 路由从固定到拍卖式**：本单元 `route_after_approval` 是固定条件函数（`revision_count >= 3` -> publish else revise）；Agora (2607.09600) 的拍卖式动态竞标把"路由"从"条件函数"升级为"基于校正能力的竞标"，为本单元 Supervisor 拓扑提供替代方案--当多个 Agent 可执行同一任务时，竞标优于固定路由。

5. **State 累积从无管理到弹性编排**：本单元 `CampaignState` 的 `messages: Annotated[list, operator.add]` 无限累积；ACE (2606.31564) 的 raw/abstract/drop 弹性类型为 LangGraph 节点上下文增长提供管理方案，本单元长循环（revision_count 高）场景下 messages 累积会导致上下文爆炸，ACE 是直接补丁。

---

## open_questions

1. LAMaS 的关键路径感知信用分配假设执行图可学习优化，但本单元 HITL `interrupt_before` 引入的人类决策时延是非确定性的（人何时审核完不可预测），学习优化器如何处理 HITL 节点的随机时延？
2. Agora 拍卖机制需要多个专家模型在线竞标，在企业生产环境中模型 API 成本不可忽略，如何设计预算约束下的拍卖机制以避免"竞标战争"导致成本失控？
3. 论文 1 (2606.31518) 的四属性分类框架在"预测光感场景"单一领域评估，推广到本单元营销编排（research/strategy/copywriter/approval）场景时，四属性的相对权重是否需要重新标定？
4. ACE 的 raw/abstract/drop 弹性类型在适配 ReAct/DeepAgent 时无需训练，但本单元 LangGraph 的 `MemorySaver` 检查点持久化跨会话恢复 State 时，abstract/drop 决策是否应持久化--若持久化则丢失原始信息，若不持久化则每次恢复需重算？

---

## methodological_critique

这些论文的局限性需博后级读者警惕：论文 1 (2606.31518) 的分类框架在"预测光感场景"单一 agentic 实现上评估，四属性的通用性缺乏跨场景验证，"定量指标"未与基线编排框架（如 LangGraph/AutoGen）对比，可能存在"为分类而分类"风险。LAMaS (2607.13359) 的 50% 延迟降低标注 unverified，且"竞争性准确率"的表述模糊（未给出绝对值），延迟-准确率权衡曲线未公开，可能存在"降延迟但显著降准确率"的隐藏权衡。论文 3 (2605.27685) 是 verified 但聚焦 SUMO 交通仿真这一狭窄领域，Planner/Builder/Demand/Runner/Analyst 五角色解耦的通用性需更多场景验证，且消融实验未报告角色间通信开销。Agora (2607.09600) 标注 unverified，拍卖机制的"激励兼容"证明依赖"校正能力可量化"假设，但 LLM 自评校正能力的可靠性存疑（LLM 自评偏差是已知问题）。ACE (2606.31564) 标注 unverified，"无需训练"是优势但也意味着弹性类型决策是启发式而非学习得来，在复杂工作流中可能劣于学习方案。所有论文均未覆盖 HITL `interrupt_before` 三步模式，本单元的企业治理 HITL 在学术编排论文中是空白。

---

*本文件由 v9.0 学术前沿注入层生成。所有论文链接来自 `_frontier_corpus/skill-2-ai-native-arch.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证）。*
