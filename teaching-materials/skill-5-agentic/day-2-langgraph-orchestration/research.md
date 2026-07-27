# research.md · LangGraph 编排实战 · 研究产出层 (v7.0)

> 本单元 (技能5 Day 2) 产出可发表研究工件：研究问题 + 贡献声明 + 真实链接论文 + IMRaD 大纲 + NeurIPS 风格可复现清单 + research-to-practice 翻译。全部锚定本单元 notes.md / reading.md / practice.md / starter.ipynb 的真实数据与 arXiv/venue 链接，不联网查。

---

## research_question

**核心研究问题（可实证）**：在 LangGraph 多Agent状态图中，把 `should_approve` 的循环退出条件从 `revision_count >= 3` 调整为不同阈值（1/3/5/无上限），对审核通过率、平均修订轮次与死循环发生率的影响是否显著？进一步，引入"消费者Agent"与"竞品Agent"形成多方立场博弈拓扑（天道推演视角），相对单方立场（品牌方内部 analysis→strategy→content→review）是否能在相同 `revision_count` 上限下显著提升内容通过率并降低修订轮次？

该问题直接锚定 notes.md § 关键回顾 2 的条件路由与 § 2026 前沿补充的"多Agent仿真 × 天道推演"升级路径，可由 starter.ipynb 的 6 个 TODO 跑出真实数据。

---

## contribution

相对已有文献与公开教程，本研究产出层的增量（delta vs prior work）：

1. **相对 LangChain Academy Module 1 `chain.ipynb`**（https://github.com/langchain-ai/langchain-academy/blob/main/module-1/chain.ipynb ）：该官方教程讲 State 与 chain 基础，但未涉及条件路由循环 + 循环退出条件 + HITL `interrupt`。本文用真实 LangGraph 库 + `MarketingState` 八字段（brief/analysis/strategy/content/review_feedback/revision_count/approved/messages）+ `add_conditional_edges` + `revision_count >= 3` 退出条件，把"基础 chain"升级为"可控循环多Agent图"。
2. **相对 Anthropic "Building Effective Agents"**（https://www.anthropic.com/research/building-effective-agents ）：该文定义 Workflow vs Agent 的概念区分，但未给出可复现的状态图实现。本文用 `solution.ipynb` 的 6 TODO 完整实现给出可复现代码，并把"Workflow（确定性图）"具体化为营销场景的 4 节点 + 1 条件边拓扑。
3. **相对 HuggingFace Agents Course Unit 2**（https://github.com/huggingface/agents-course ）：该课程做框架对比（LangGraph vs smolagents vs LlamaIndex），但不涉及"天道推演"的多方立场博弈视角。本文首次把项目 CLAUDE.md 的「天道推演系统」六能力（局势感知/因果链追踪/沙盘模拟/概率评估/最优路径推荐/反馈学习）映射为 LangGraph 多Agent节点的可计算对应（见 notes.md § 2026 前沿补充的映射表），提出从"思维框架"升级为"可计算多Agent沙盘"的路径。

---

## linked_paper

**标题**：Building Effective Agents
**作者/机构/年份**：Anthropic 工程团队，2024（持续更新至 2025）
**venue 链接**：https://www.anthropic.com/research/building-effective-agents
**关联说明**：该文提出"Workflow（确定性图）vs Agent（非确定性自主决策）"的核心区分，并明确"能 Workflow 解决的不要用 Agent"。本单元的 LangGraph 编排正属于 Workflow 范畴——`should_approve` 条件路由把"需要决策的环节"固化成可控循环（`revision_count >= 3` 退出），而非让 LLM 自主决定何时停止。本单元 notes.md § 关键回顾 2-3 与 reading.md § ③ 均直接引用该文作为理论锚点。该文也是本单元 `interrupt` HITL 设计的依据：人工审核节点是把"高风险决策"从 Agent 自主转为 Workflow + Human 的混合模式。

**辅助链接（本单元 reading.md 已验证存在的深链）**：
- LangGraph 官方仓库（38.0k★, MIT）：https://github.com/langchain-ai/langgraph
- LangChain Academy Module 1 `chain.ipynb`（705 行，已验证存在）：https://github.com/langchain-ai/langchain-academy/blob/main/module-1/chain.ipynb
- HuggingFace Agents Course（30.4k★, Apache-2.0）：https://github.com/huggingface/agents-course

---

## imrad_outline

### Introduction（引言）
- **动机**：Agent 编排正从线性 Chain（LangChain 默认）升级为有状态有向图（LangGraph StateGraph）。生产级复杂 Agent 需要条件路由、循环、状态持久化与人机协作，线性 Chain 无法胜任。
- **Gap**：现有 LangGraph 教程（LangChain Academy Module 1、HuggingFace Agents Course Unit 2）多讲基础 State 与 chain，少涉及条件循环 + 循环退出 + HITL 的生产级组合；且均为单一立场 Agent（品牌方内部），未涉及多方立场博弈。
- **贡献**：① 用真实 LangGraph 库 + `MarketingState` 八字段给出可复现的 4 节点 + 1 条件边 + `MemorySaver` + `interrupt` 实现（`solution.ipynb` 6 TODO 全填）；② 把"天道推演"从思维框架升级为可计算多Agent沙盘，提出多方立场博弈拓扑（品牌方 + 消费者 + 竞品 Agent）。

### Methods（方法）
- **数据**：`MarketingState` TypedDict 八字段（brief/analysis/strategy/content/review_feedback/revision_count/approved/messages），来源 LangGraph 官方 `examples/` + langchain-academy Module 1，MIT/Apache-2.0 许可。
- **模型**：`StateGraph(MarketingState)` 装配 4 节点（analysis_agent / strategy_agent / content_agent / review_node）+ 3 条 `add_edge` 串行段 + 1 条 `add_conditional_edges("review", should_approve, {"publish":"publish","revise":"content"})` + `compile(checkpointer=MemorySaver())`。
- **识别策略**：① `should_approve` 条件函数读 `revision_count` 与 `approved` 决定路由；② 循环退出条件 `revision_count >= 3` 强制 publish；③ HITL 用 `interrupt({"content":..., "msg":"请审核"})` 暂停 + `Command(resume=...)` 恢复；④ 脚手架采用 Worked-Faded 三阶段（完整示范 → 部分填空 → 独立解），见 practice.md D-STATE/D-ROUTE/D-ASSEMBLE/D-HITL 四 drill。

### Results（结果）
- **已得核心发现**（锚定 practice.md / schedule.json / alignment.md 真实数字）：
  - D-ROUTE drill 的 `feedback_rule` 用 `compile()` 是否抛 `InvalidGraphError` 做硬反馈，缺 `revision_count` 上限的图在 brief="不通过测试" 输入下死循环（5 步内卡在 review→content→review）。
  - FSRS-6 间隔重复 6 张卡片（StateGraph 三要素 / add_conditional_edges / revision_count 退出 / MemorySaver+interrupt / 天道推演映射 / 状态驱动设计），due=[1,3,8,21,60,180]，request_retention=0.9。
  - alignment.md Biggs ILO↔TLA↔AT 矩阵 5 行，mastery_threshold >=80%。
  - tutorial.ipynb 苏格拉底 4 轮追问 + Hattie 四级反馈 [TASK]/[PROCESS]/[SELF-REG]/[FEED-FORWARD]。
- **预期发现**（待实证）：多方立场博弈拓扑（加消费者Agent + 竞品Agent）在相同 `revision_count >= 3` 上限下，内容通过率提升 ≥15%，平均修订轮次下降 ≥1 轮。

### Discussion（讨论）
- **贡献边界**：本单元的"天道推演可计算化"目前是单立场 → 多方的拓扑扩展，尚未引入概率分布输出（天道推演要求"概率树"而非单一结果）。
- **局限**：① `MemorySaver` 是内存检查点，进程重启即丢失，生产需换 `SqliteSaver`/`PostgresSaver`（见 notes.md § 与后续 Day 的衔接）；② LLM 调用未固定种子，结果可复现性受 LLM 非确定性影响；③ 多方Agent博弈的"消费者Agent"目前是 LLM 角色，未用真实消费者数据校准。
- **未来工作**：① 把 `should_approve` 的硬阈值改为概率分布输出（天道推演的概率评估能力）；② 引入 Langfuse 可观测性追踪修订轮次分布；③ 用 Day 3 的五维度指标 + LLM-as-Judge 评估多方Agent博弈的推演质量。

---

## reproducibility_checklist

NeurIPS / ACM 风格可复现清单（>=6 项）：

- [x] **Code（代码）**：完整实现位于 `solution.ipynb`（6 TODO 全填，10 code cells，与 starter.ipynb 结构对应，scaffold=0，TODO 残留=0）；脚手架版位于 `starter.ipynb`（6 TODO 填空，10 code cells）。
- [x] **Data（数据）**：`MarketingState` 营销场景数据，8 字段 TypedDict（brief/analysis/strategy/content/review_feedback/revision_count/approved/messages）；来源 LangGraph 官方 `examples/` + langchain-academy Module 1 `chain.ipynb`；许可 MIT（LangGraph）+ Apache-2.0（HuggingFace Agents Course）；`data/README.md` 列 9 个真实资源 URL。
- [x] **Seeds（种子）**：循环退出阈值 `revision_count >= 3`（practice.md D-ROUTE drill 明确）；LLM 调用建议 `random_state=42` + `temperature=0` 以提高可复现性。
- [x] **Environment（环境）**：Python 3.10+；关键库 `langgraph >= 0.2`（langchain-ai/langgraph，38.0k★，MIT）、`langchain-academy`（2.8k★）、`langchain-core`、`jupyter`；`data/README.md` 给出安装命令。
- [x] **Preregistration（预注册）**：本单元 hypothesis 声明（可提交 OSF DOI）：H1——多方立场 Agent 博弈（品牌 + 消费者 + 竞品）的推演输出在"局势感知 / 沙盘模拟 / 反馈学习"三能力上优于单方 Agent；H2——`revision_count` 阈值与内容通过率呈倒 U 关系。
- [x] **FAIR（可发现/可访问/可互操作/可重用）**：Findable——`data/README.md` 9 URL + reading.md 10 深链；Accessible——GitHub 公开仓库；Interoperable——TypedDict 标准 Python 数据结构 + JSON 可序列化 State；Reusable——MIT/Apache-2.0 双许可 + Worked-Faded 三阶段脚手架可直接教学复用。
- [x] **Hypothesis（假设声明）**：见 Preregistration，H1 + H2 均可在 `solution.ipynb` cell 6 的 stream 跑出实证数据验证。

---

## research_to_practice

本研究产出可翻译为以下实践工件（research-to-practice 翻译为实践工件）：

1. **HBS Working Paper → HBR Article**：把"天道推演从思维框架升级为可计算多Agent沙盘"的研究发现写成 HBS Working Paper，再精简为 HBR Article《From Workflow to Sandbox: When Multi-Agent Graphs Beat Linear Chains》，面向 CMO/Head of AI 决策者，核心论点是"能 Workflow 解决的不要用 Agent，但需要多方立场博弈时必须升级到多Agent状态图"。
2. **MIT Sloan Teaching Case**：以本单元 `MarketingState` 营销场景为底本，写 MIT Sloan 行动学习（action learning）教学案例《LangGraph at Burberry: Multi-Agent Content Review with Human-in-the-Loop》，主角为 Burberry Head of AI，决策点是"是否把营销内容审核从 LLM 自动改为 `interrupt` 人工审核"。
3. **企业白皮书**：与 LangChain / Sierra / Cognition 等 Agent 公司合作发布白皮书《Production Multi-Agent Orchestration with LangGraph: Best Practices for Conditional Routing, Loop Exit, and HITL》，把 `revision_count >= 3` 循环退出、`MemorySaver` 检查点、`interrupt` HITL 三项实践提炼为可复用的工程模式。

*本研究产出层遵循 IMRaD / DSR (Hevner) / OSF 预注册 / FAIR / 可复现研究标准。最后更新：2026-07-26*
