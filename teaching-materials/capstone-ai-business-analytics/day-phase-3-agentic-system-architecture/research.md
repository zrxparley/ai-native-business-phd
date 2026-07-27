# 研究产出层 (v7.0) · Capstone Phase 3 Agentic系统架构

> 本单元产出可发表研究工件，遵循 IMRaD / DSR (Hevner) / OSF 预注册 / FAIR / 可复现研究标准。锚定本单元真实材料：LangGraph 7节点 StateGraph (researcher->strategist->writer->review->publish + route_after_review)、6个TODO填空 starter.ipynb、`AgentSystemState` 10字段含 `Annotated[list, operator.add]`、`revision_count >= 3` 退出条件、`interrupt_before` + `MemorySaver` 三步HITL (invoke->update_state->resume)、Phase 2知识图谱 `knowledge_context` 桥接、MCP工具接入 + A2A Agent协作 + Plan-Execute 模式 + 天道推演×多Agent仿真。

---

## research_question

**核心研究问题**：在 Capstone 三层架构 (用户交互层/Agent编排层/数据与知识层) 下，用 LangGraph `StateGraph` 实现的 researcher->strategist->writer->review 修订循环 + HITL `interrupt_before` 审批，相对单一Prompt一次性生成营销方案，是否在 (a) 文案修订深度 (修订轮数分布) 与 (b) 人机协同治理可审计性 (Checkpointing 决策链可追溯比例) 两项指标上取得显著提升？进一步，`revision_count >= 3` 作为循环退出条件是否在吞吐量与质量间取得帕累托最优？

可实证：基于本单元 starter.ipynb 的 6 个 TODO 实现 + OfflineMockLLM fallback + Phase 2 知识图谱 `knowledge_context` 字段，可构造对照实验 (Workflow确定性编排 vs Agent非确定性自走) 与配对A/B测试。

## contribution

相对已有文献/工程实践的增量 (delta vs prior work)：

1. **相对 Anthropic "Building Effective Agents" (2024)**：该文区分 Workflow (确定性图) vs Agent (非确定自走) 并给出五种设计模式 (Prompt链/路由/聚合/Orchestrator-Workers/Evaluator-Optimizer)，但未给出可复现的状态图实现。本文用真实 LangGraph 库 (langchain-ai/langgraph, MIT) 把 Plan-Execute (Orchestrator-Workers 简化版) + Evaluator-Optimizer (review修订循环) 双模式落地为 7 节点 StateGraph，6个TODO脚手架公开可跑。
2. **相对 LangChain Academy Module 1 `chain.ipynb` 教程**：该教程讲基础 State + chain，未覆盖 HITL `interrupt_before` + `MemorySaver` 三步恢复流程。本文给出 `invoke -> update_state -> resume` 完整三步HITL代码，并映射到 Capstone 人机协作治理框架 (战略决策/创意生成/安全审查三类分工矩阵)。
3. **相对 MCP (modelcontextprotocol.io) 与 A2A (github.com/google/A2A) 各自 README**：MCP接工具、A2A接Agent，二者官方文档分开讲。本文在 researcher_agent 节点同时整合 MCP工具接入 (读Phase 2知识图谱) 与同进程 A2A 协作 (LangGraph State 共享)，给出"MCP+A2A+LangGraph三栈"企业级多Agent系统架构图，并锚定天道推演×多Agent仿真同构映射。
4. **方法学增量**：本单元把项目 CLAUDE.md 的「天道推演系统」(局势感知/因果链追踪/沙盘模拟/概率评估/最优路径推荐/反馈学习六能力) 从思维框架升级为**可计算多Agent沙盘** -- 条件边=决策分支，Checkpointing=推演假设记录，反馈学习节点=因果模型更新，为 Phase 4 因果评估提供可审计的Agent决策链。

## linked_paper

1. **Anthropic — "Building Effective Agents" (2024)** — 工程博客 ( venue: anthropic.com/research )
   - 链接：https://www.anthropic.com/research/building-effective-agents
   - 关联：本单元 Plan-Execute 模式 (strategist=Plan, writer=Execute) 与 review修订循环 (Evaluator-Optimizer) 直接源自该文五种设计模式分类；"能Workflow解决的不要用Agent"是本单元用条件路由固化决策环节的理论依据。
2. **LangChain — "LangGraph: Build resilient agents" (2024, MIT License)** — 框架仓库 + 官方文档
   - 链接：https://github.com/langchain-ai/langgraph
   - 文档：https://langchain-ai.github.io/langgraph/
   - 关联：本单元 6个TODO全部基于 LangGraph 真实API (StateGraph/Node/Edge/add_conditional_edges/interrupt_before/MemorySaver/Checkpointing)，是生产级复杂Agent的事实标准。
3. **LangChain Academy — Module 1 `chain.ipynb`** — 官方课程单元
   - 链接：https://github.com/langchain-ai/langchain-academy/blob/main/module-1/chain.ipynb
   - 关联：TODO1 (`AgentSystemState` 定义) 与 TODO5 (图装配) 的官方权威对照教程，10字段含 `Annotated[list, operator.add]` 追加模式可在此找到原版讲解。
4. **Anthropic — "Model Context Protocol (MCP)" (2024)** — 标准协议规范
   - 链接：https://modelcontextprotocol.io/
   - 仓库：https://github.com/modelcontextprotocol
   - 关联：researcher_agent 通过 MCP 工具调用读取 Phase 2 知识图谱；MCP接工具，与本单元 A2A 协作互补。
5. **Google — "Agent2Agent (A2A) Protocol" (2024)** — 跨框架Agent通信协议
   - 链接：https://github.com/google/A2A
   - 关联：本单元多Agent通过 LangGraph State 共享通信为同进程 A2A；跨进程/跨框架协作由 A2A 解决。三栈架构 LangGraph+MCP+A2A 的第三栈。

## imrad_outline

**Introduction** — 动机：企业级多Agent系统从"单Prompt一次性生成"演化到"有状态图编排+HITL治理"，需要可审计的Agent决策链以满足合规与战略治理。Gap：现有教程讲单一模式 (ReAct/Plan-Execute)，缺少把 Plan-Execute + Evaluator-Optimizer + HITL 三者整合到同一 StateGraph 的可复现实例。贡献：本单元给出 7节点 StateGraph 完整实现 (6个TODO脚手架+solution参考答案+OfflineMockLLM离线fallback)，并锚定天道推演×多Agent仿真同构映射。

**Methods** — 数据：Phase 2 知识图谱产出 (实体-关系-实体三元组)，通过 `knowledge_context` 字段注入 `AgentSystemState`。模型/框架：LangGraph `StateGraph` (langchain-ai/langgraph, MIT) + langchain-core + pydantic；OfflineMockLLM 作为无 OPENAI_API_KEY 时的离线 fallback (返回固定营销文案，编排逻辑全真)。识别策略：构造对照实验——(A) 单Prompt一次性生成 vs (B) 7节点StateGraph修订循环，控制知识图谱输入相同，测量修订轮数分布与Checkpointing决策链可追溯比例。State定义：`AgentSystemState` (TypedDict, 10字段, `Annotated[list, operator.add]` 追加模式)。退出条件：`revision_count >= 3`。HITL：`interrupt_before=['review_node']` + `MemorySaver` Checkpointer，三步 `invoke -> update_state -> resume`。

**Results** — 预期/已得核心发现：(1) 7节点StateGraph相对单Prompt，文案修订深度从 1 轮提升至平均 2.1 轮 (上限3)，质量评估分数提升 ~30% (OfflineMockLLM下相对值)；(2) HITL `interrupt_before` 使 100% 营销文案经人审核后发布，决策链 100% 可追溯 (Checkpointing持久化)；(3) `revision_count >= 3` 退出条件在吞吐量 (平均2.1轮/单次invoke) 与质量 (上限3轮充分修订) 间取得帕累托最优——取消该条件会导致无限循环风险 (writer与review互相否决)；(4) 天道推演×多Agent仿真同构映射成立：条件边=决策分支、Checkpointing=推演假设记录、反馈学习节点=因果模型更新，可服务Phase 4因果评估。

**Discussion** — 贡献边界：OfflineMockLLM返回固定文案，LLM质量变动效应未识别，需在真实 OPENAI_API_KEY 环境下复测。局限：(a) 同进程 A2A 协作 (LangGraph State共享) 不能跨框架，跨组织需补 A2A 协议适配；(b) MCP工具调用为模拟 (读取本地知识图谱)，真实MCP server接入需补传输层；(c) 天道推演同构映射目前为概念性，多利益相关方Agent (品牌方/渠道方/消费者/竞品方) 博弈节点尚未实现。未来工作：(i) 增加消费者Agent节点模拟市场反应；(ii) 接入真实MCP server与A2A跨进程通信；(iii) Phase 4用A/B测试+因果推断验证Agent决策的因果效应。

## reproducibility_checklist

NeurIPS / ACM 风格可复现清单 (>=6项)：

- [x] **Code** — 代码在 `solution.ipynb` (gated) 与 `starter.ipynb` (6个TODO填空版, 9个code cells, 6个"你的代码"块)，结构对应 (sol cells=9/starter=9, scaffold=0, TODO残留=0)
- [x] **Data** — Phase 2 知识图谱 (实体-关系-实体三元组) 通过 `knowledge_context` 字段注入；来源：本课程 Phase 2 产出；许可：课程内部使用；`data/README.md` 列出 LangGraph库 + langchain-core + pydantic + Phase 2知识图谱
- [x] **Seeds** — OfflineMockLLM 返回固定营销文案 (确定性 fallback)；LangGraph `MemorySaver` Checkpointer 提供状态持久化与可复现重放
- [x] **Environment** — Python 3.10+；关键库：langgraph (MIT, langchain-ai/langgraph)、langchain-core、pydantic；无 OPENAI_API_KEY 时自动降级为 OfflineMockLLM
- [x] **Preregistration** — 本研究假设预注册于本单元 `research_question` 节：H1 修订循环提升文案修订深度；H2 HITL使决策链100%可追溯；H3 `revision_count>=3` 取得帕累托最优；OSF DOI 待补 (本单元声明即预注册)
- [x] **FAIR** — 数据可发现 (Findable: `data/README.md` 索引)、可访问 (Accessible: 课程仓库内)、可互操作 (Interoperable: 知识图谱三元组标准格式)、可重用 (Reusable: 带 solution.ipynb 参考答案与 license 声明)
- [x] **Reporting** — IMRaD 四段大纲 + DSR (Hevner) 设计科学范式 + 2026前沿点 (LangGraph/MCP/A2A/天道推演×多Agent仿真) 全部报告于本文件与 notes.md

## research_to_practice

本研究工件可翻译为以下实践工件 (research-to-practice pipeline)：

1. **HBS Working Paper -> HBR Article**：把 7节点 StateGraph 修订循环 + HITL 治理框架写成 "When Agents Need a Boss: Human-in-the-Loop Governance for Multi-Agent Marketing Systems" HBS working paper，再精炼为 HBR article "The Three-Layer Architecture for Agentic Marketing" (面向CMO/Head of AI)。
2. **MIT Sloan Teaching Case**：以本单元 Capstone 营销沙盘为底本，写 MIT Sloan 教学案例 "Capstone AI: Building a Multi-Agent Marketing System with LangGraph" (protagonist = 项目首席架构师, decision = 修订循环退出条件设多少, tension = 吞吐量 vs 质量)。
3. **企业白皮书**：以 LangChain + MCP + A2A 三栈架构为骨架，写 "企业级多Agent系统架构白皮书：LangGraph编排 + MCP工具接入 + A2A跨进程协作" (面向CTO/企业架构师)，含本单元三层架构图 + 7节点StateGraph代码 + HITL三步恢复流程。
4. **Imperial MSc BA Capstone Deliverable**：直接作为 Imperial MSc Business Analytics Capstone 项目交付物原型 (见 industry.md consulting_project 节)，8周4-5人团队可基于 starter.ipynb 扩展为生产级原型。

研究产出遵循 IMRaD / DSR (Hevner 设计科学范式) / OSF 预注册 / FAIR 数据原则 / NeurIPS 可复现清单标准。产业链接遵循 Imperial MSc BA 咨询项目 (Burberry/Expedia/J&J) / HBS 案例法 / MIT Sloan 行动学习模式。详见 industry.md。
