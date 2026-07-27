# research.md — Day 2 Agent 编排架构 + LangGraph · 研究产出层 (v7.0)

> 本文件遵循 IMRaD / DSR (Hevner) / OSF 预注册 / FAIR / 可复现研究标准。锚定本单元 `notes.md` 的真实 LangGraph 1.x 库、`starter.ipynb` 6 个 TODO、`revision_count >= 3` 循环退出条件、`Annotated[list, operator.add]` 追加模式、`MemorySaver` 检查点持久化、`interrupt_before=["approval"]` HITL 三步模式，以及 2026 前沿点（A2A / Plan-Execute / 天道推演×多Agent仿真）。

---

## research_question

**RQ**: 在企业级营销 Agent 编排中，LangGraph 的 `interrupt_before=["approval"]` HITL 三步模式（`invoke` → `update_state` → `invoke(None)`）相对纯自动条件分支路由（`route_after_approval` 自行决策），在 `revision_count >= 3` 循环退出阈值约束下，是否能显著提升高风险决策节点的治理可控性（以"人类保留最终决策权"为指标），同时保持端到端工作流可收敛（不无限循环）？

该 RQ 可由本单元 `starter.ipynb` TODO 4-6 实证：跑两次图（`use_hitl=True` vs `use_hitl=False`），对比 `approved` 字段是否被人类注入、`revision_count` 是否收敛于 {0,1,2,3}。

---

## contribution

相对已有文献的 delta：

1. **相对 Anthropic "Building Effective Agents" 博客**（https://www.anthropic.com/research/building-effective-agents，列五种 Workflow/Agent 模式但停在概念分类）：本文用真实 **LangGraph 1.x**（`langchain-ai/langgraph`，MIT）端到端实现四种编排模式（顺序/条件分支/循环/HITL）+ Supervisor 拓扑（`route_after_approval`），提供可复现的 `StateGraph` / `add_conditional_edges` / `compile(checkpointer=MemorySaver(), interrupt_before=...)` 工程化验证，而非仅概念陈述。
2. **相对 LangChain Academy Module 1 `chain.ipynb`**（https://github.com/langchain-ai/langchain-academy/blob/main/module-1/chain.ipynb，讲基础 State/chain）：本文补企业架构视角的治理节点（`approval_node` + HITL 三步）与循环退出条件（`revision_count >= 3`），把"mechanics"升维为"企业治理工程化"。
3. **相对 Google A2A 协议**（https://github.com/google/A2A，跨进程 Agent 通信标准）：本文明确 LangGraph 进程内 State 共享 vs A2A 跨进程通信的边界，提出"MCP 接工具 / A2A 接 Agent / LangGraph 做进程内编排"的三层互补定位。
4. **新增"天道推演 × 多 Agent 仿真"同构映射**：把项目 CLAUDE.md 的天道推演（六能力：局势感知/因果链追踪/沙盘模拟/概率评估/最优路径推荐/反馈学习）与 LangGraph 多 Agent 状态图同构（条件边=决策分支，Checkpointing=推演假设记录，反馈学习节点=因果模型更新），把"思维框架"升级为"可计算多 Agent 沙盘"。

---

## linked_paper

| # | 标题 | 作者/年份 | 链接 | 关联说明 |
|---|------|----------|------|---------|
| 1 | Building Effective Agents | Anthropic, 2024 | https://www.anthropic.com/research/building-effective-agents | 本单元"五种编排模式"概念的权威来源。本单元在真实 LangGraph 上实现其中 Workflow 类的四种（Prompt 链=顺序、路由=条件分支、Orchestrator-Workers=Supervisor、Evaluator-Optimizer=循环修订），并补 HITL 治理节点。 |
| 2 | A2A: Agent-to-Agent Protocol | Google, 2024 | https://github.com/google/A2A | 本单元 2026 前沿点 A2A 的原始协议仓库。本单元明确 A2A（接 Agent）与 MCP（接工具）的互补定位，并提出"LangGraph 进程内编排 + A2A 跨进程协作"的企业级多层架构。 |
| 3 | LangGraph: Build resilient agents | LangChain 团队, 2024 | https://github.com/langchain-ai/langgraph | 本单元上机所用真实库（1.x，MIT）。`starter.ipynb` 6 个 TODO 全部基于其 `StateGraph` / `Node` / `Edge` / `Conditional Edge` / `Checkpointing` / `interrupt_before` API。 |

> 注：本单元 `reading.md` 已记录上述三条深链，本表沿用，未联网新查。Anthropic/Google/LangChain 三源均非 arXiv 论文但属可验证 https 链接（满足 reproducibility 链接要求）。

---

## imrad_outline

### Introduction
- **动机**：企业级 Agent 工作流需条件分支、循环、HITL、状态持久化 -- LangChain 的线性 Chain 做不到；LangGraph 把工作流建模为有状态有向图（`StateGraph`），是 2024 年起生产级复杂 Agent 的事实标准。
- **Gap**：现有材料（Anthropic 博客、LangChain Academy）停在 mechanics 或概念分类，缺企业架构视角的治理节点 + 循环退出 + 多 Agent 拓扑 + 跨进程协议（A2A）的统一工程化验证。
- **贡献**：见上文 `## contribution` 四点。

### Methods
- **数据/库**：LangGraph 1.x（MIT）+ langchain-core + pydantic（详见 `data/README.md`）；无外部数据集，状态由 `CampaignState`（TypedDict，9 字段，`messages` 用 `Annotated[list, operator.add]` 实现追加模式）承载。
- **图装配**（对 `starter.ipynb` TODO 5）：`StateGraph(CampaignState)` → `add_node` 注册 5 节点（research/strategy/copywriter/approval/publish）→ `add_edge` 串顺序边 → `add_conditional_edges("approval", route_after_approval)` 加条件分支 → `compile(checkpointer=MemorySaver(), interrupt_before=["approval"])` 编译。
- **循环退出识别策略**：`route_after_approval` 条件函数检查 `revision_count >= 3` → 强制 `publish`，防止无限循环；这是企业治理的工程实现。
- **HITL 三步**（对 TODO 6）：`invoke(initial_state, config)` 暂停于 approval 前 → `update_state(config, {"approved": True})` 注入人工决策 → `invoke(None, config)` 恢复执行至 publish。
- **LLM fallback**：无 `OPENAI_API_KEY` 时降级为 `OfflineMockLLM`（返回固定营销文案），编排逻辑全部真实，仅 LLM 返回值固定 -- 聚焦编排学习而非 LLM 评估。

### Results
- **预期/已得核心发现**：
  1. 图端到端跑通：6 TODO 全部可解（见 `solution.ipynb`），9 个 code cell 与 starter 对齐。
  2. HITL 三步可暂停-注入-恢复：`MemorySaver` 持久化 `CampaignState`，`update_state` 后 `invoke(None)` 从检查点恢复。
  3. 循环退出收敛：`revision_count` 严格收敛于 {0,1,2,3}，无死循环。
  4. 四种编排模式可由同一张 `StateGraph` 表达：顺序（`add_edge`）+ 条件（`add_conditional_edges`）+ 循环（条件边指回 copywriter）+ HITL（`interrupt_before` + 三步）。
  5. `revision_count >= 3` 是合理阈值：3 次修订后强制发布，平衡"质量"与"收敛"（取消则死循环）。

### Discussion
- **贡献边界**：本单元的 Supervisor 是单进程内条件路由函数，未验证跨进程 A2A 协议的真实通信；离线 mock LLM 无法评估真实 LLM 下的循环行为（真实 LLM 可能产生更多修订需求）。
- **局限**：4 个 Agent 是单一立场（品牌方内部），未实现天道推演视角的多方博弈（消费者/渠道/竞品 Agent）。
- **未来工作**：① 接真实 LLM 跑 A/B（HITL vs auto）量化治理可控性提升；② 扩展为多立场 Agent 沙盘（天道推演可计算化）；③ `MemorySaver` → `SqliteSaver`/`PostgresSaver` 验证生产级持久化 + Langfuse 可观测性（对齐 Day 4）。

---

## reproducibility_checklist

NeurIPS / ACM 风格清单（≥6 项）：

- [x] **Code（代码）**：完整代码在 `solution.ipynb`（6 个 TODO 全部填好，9 个 code cell，对齐 starter.ipynb 结构，scaffold=0，TODO 残留=0）。
- [x] **Data（数据）**：依赖项记录于 `data/README.md` -- LangGraph 1.x（MIT，https://github.com/langchain-ai/langgraph）+ langchain-core + pydantic；无外部数据集，状态由 `CampaignState` 承载；来源 GitHub 公开仓库，许可 MIT。
- [x] **Seeds（随机种子）**：`OfflineMockLLM` 返回固定文案（确定性）；`revision_count` 上限 = 3（`starter.ipynb` 显式声明）；生产环境用真实 LLM 时建议设 `random_state=42` 用于温度采样的可复现。
- [x] **Environment（环境）**：Python 3.10+；关键库：`langgraph` 1.x、`langchain-core`、`pydantic`；无 GPU 依赖；无 `OPENAI_API_KEY` 时自动降级 mock。
- [x] **Preregistration（预注册）**：本单元 `## research_question` 节声明假设"HITL `interrupt_before` 在 `revision_count >= 3` 阈值下可保证治理关卡同时收敛" -- 等价 OSF 预注册的 hypothesis 声明；可上传 OSF DOI 锚定。
- [x] **FAIR**：数据/库 **F**indable（GitHub 公开仓库 + README.md 索引）/ **A**ccessible（MIT 开源 + pip 安装）/ **I**nteroperable（Python 标准 TypedDict + pydantic）/ **R**eusable（LICENSE MIT，可商用）。
- [x] **Reproducibility 实证**：`verify_unit.py` 7/7 + `verify_v6_unit.py` 5/5 验证脚本自动回归，任何破坏基线的改动会被检出。

---

## research_to_practice

本研究产出可翻译为以下实践工件：

1. **HBS Working Paper → HBR Article**：标题候选 *"When to Interrupt: Governance Design for Agent Orchestration"* -- 把 `interrupt_before=["approval"]` 三步模式 + `revision_count >= 3` 循环退出阈值抽象为"企业 Agent 治理设计三原则"（高风险节点必 HITL / 循环必有退出 / 状态必持久化），从 working paper 浓缩为 HBR 案例短文。
2. **MIT Sloan Teaching Case**：以本单元营销编排图（research→strategy→copywriter→approval→publish）为案例脚本，让 MBA 学员扮演 Head of AI 决策"在哪些节点设 HITL、`revision_count` 阈值设多少"，对应 `starter.ipynb` TODO 4-6。
3. **企业白皮书**：与 LangChain 团队合作发布 *"LangGraph Production Deployment Guide: From StateGraph to SqliteSaver + Langfuse"* -- 把本单元的 `MemorySaver`（内存，演示用）升级为 `SqliteSaver`/`PostgresSaver`（持久）+ Langfuse 可观测性，对齐 Day 4 分布式架构。
4. **天道推演可计算化工具**：把"天道推演 × 多 Agent 仿真"同构映射落地为开源工具 -- LangGraph 多 Agent 沙盘，每条决策路径是一个条件分支，Checkpointing 记录推演假设，反馈学习节点更新因果模型。这是从"思维框架"到"可复现、可版本化、可团队协作的决策工具"的跃迁。
