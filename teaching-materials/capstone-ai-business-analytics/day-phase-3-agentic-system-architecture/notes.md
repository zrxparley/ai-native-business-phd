# Capstone · Phase 3：Agentic系统架构设计 · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · Capstone AI和商业分析项目 · Phase 3
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2-3周 | **核心交付物**：系统架构文档 + Agent工作流代码
> **核心命题**：如何用LangGraph的有状态图构建Capstone三层架构的Agent编排系统，整合Phase 2知识图谱数据层，实现researcher->strategist->writer多Agent协作 + 条件分支 + 人机协同审批（HITL）？
> **v5.0升级点**：① 真实库上机（LangGraph，非伪代码）② TODO填空式起始笔记本 ③ 离线模拟LLM fallback ④ Notebook化 ⑤ 深链阅读 ⑥ 整合技能5(Agent架构Day1-2)+技能2(编排Day2) ⑦ 2026前沿（LangGraph/MCP/A2A/天道推演×多Agent仿真/Plan-Execute）

---

## 学习目标（学完你能做到）

1. 能用Capstone**三层架构**（用户交互层/Agent编排层/数据与知识层）解释Agent系统如何从Phase 2数据层获取知识、经多Agent编排产出营销方案、通过HITL审批交付用户，并指出各层对应的LangGraph代码对象
2. 能用LangGraph的 `StateGraph` / `Node` / `Edge` 三要素构建"researcher->strategist->writer->review->publish"多Agent营销系统，识别其中的**条件边**（审核通过/不通过）与**循环退出条件**（修改次数上限），说明HITL审批节点的Capstone治理意义
3. 能在**真实LangGraph库**上完成"定义State -> 写节点函数 -> 装配图（含 `interrupt_before` + `MemorySaver`） -> 编译 -> 三步HITL运行（invoke -> update_state -> resume）"全流程，并解释Checkpointing的状态持久化作用
4. 能用**Plan-Execute模式**解释strategist(Plan阶段)与writer(Execute阶段)的分工，用**MCP工具接入**概念解释researcher_agent如何通过知识图谱检索获取市场知识，用**A2A Agent协作**概念解释多Agent如何通过State共享通信
5. 能用"天道推演 × 多Agent仿真"视角，把Capstone营销沙盘映射为LangGraph多Agent博弈图 -- 每条决策路径是一个条件分支，Checkpointing记录推演假设，反馈学习节点更新因果模型，为Phase 4因果评估提供可审计的Agent决策链

---

## 理论部分：精炼索引（详见独立教材）

> Phase 3的完整理论见 [`../../AI原生化商业博士_独立教材_Capstone_AI和商业分析项目.md` § Phase 3](../../AI原生化商业博士_独立教材_Capstone_AI和商业分析项目.md)（第438-660行，含三层架构/Agent工作流设计/人机协作治理框架/交付物清单）。本讲义不重复，仅做上机所需的关键回顾与整合视角增量。

### 关键回顾 1：Capstone三层架构

Phase 3的核心是把Phase 2的数据表示层转化为完整的Agent系统架构。教材定义了三层架构：

| 层 | 职责 | 本Phase对应 |
|----|------|------------|
| **用户交互层** | 营销人员界面/管理层仪表盘/API层 | Brief输入 + HITL审批 + final_output |
| **Agent编排层** | LangGraph多Agent协作 | researcher->strategist->writer->review->publish |
| **数据与知识层** | 知识图谱/GraphRAG/因果引擎 | Phase 2知识图谱（knowledge_context字段） |

### 关键回顾 2：LangGraph Agent工作流

教材给出了基于 `StateGraph` 的Agent工作流设计（第498-630行），包含：
- `AgentState`（TypedDict）：所有节点共享的全局状态
- 节点Agent：insight_agent / creative_agent / placement_agent / safety_check_agent / human_review
- 协调Agent（coordinator_agent）：条件路由函数，决定下一步执行哪个Agent
- 条件边：`add_conditional_edges` 实现分支与循环

本Phase在此基础上整合技能5(Agent架构)与技能2(编排)，用Plan-Execute模式重构为researcher(研究)->strategist(策略)->writer(写作)->review(审核)的工作流。

### 关键回顾 3：人机协作治理框架

教材定义了人机分工矩阵（第634-643行）：
- **战略决策**：人类制定战略，Agent提供数据分析
- **创意生成**：Agent生成变体，人类审核选择（混合决策权）
- **安全审查**：人类制定政策，Agent执行检查

本Phase的 `review_node` + `interrupt_before` 是这一治理框架的工程实现。

### 关键回顾 4：整合技能5 + 技能2

| 技能 | 内容 | 本Phase整合点 |
|------|------|-------------|
| 技能5 Day1 | Agent架构模式（ReAct/Plan-Execute/Reflection） | 本Phase用Plan-Execute模式 |
| 技能5 Day2 | LangGraph编排（StateGraph/条件边/HITL） | 本Phase用StateGraph+interrupt |
| 技能2 Day2 | 企业编排（顺序/并行/循环/条件 + Supervisor拓扑） | 本Phase用顺序+条件+循环+HITL |

---

## 上机部分：在真实LangGraph上构建Capstone Agent系统

> 配套笔记本：[`starter.ipynb`](./starter.ipynb)（TODO填空版，6个TODO）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，gated）
> 真实库与资源：[`data/README.md`](./data/README.md)（LangGraph库 + langchain-core + pydantic + Phase 2知识图谱）

### 为什么用真实库LangGraph而非伪代码

v4.0的代码用"伪代码/模拟框架"--模拟框架学不到真实API的细节（State怎么定义、条件边怎么注册、检查点怎么编译、interrupt怎么暂停-恢复）。v5.0改用**LangGraph**（langchain-ai/langgraph，MIT，"Build resilient agents"）：LangChain团队官方Agent编排框架，生产级复杂Agent的事实标准。教材已有完整LangGraph实现，本Phase把它改写成TODO填空版让你亲手写一遍。

### 离线模拟LLM fallback

无 `OPENAI_API_KEY` 时，自动降级为 `OfflineMockLLM`（返回固定营销文案），使图能端到端跑通。这不是"伪代码"--编排逻辑（StateGraph/条件边/interrupt/Checkpointing）全部是真实LangGraph API；只有LLM返回值是固定的，聚焦编排学习。

### 营销映射（Capstone整合视角）

| LangGraph节点 | 营销职能 | 架构模式 | Capstone层 |
|---------------|---------|---------|-----------|
| `researcher_agent` | 市场研究员：基于知识图谱分析市场 | MCP工具调用 | 数据与知识层 -> Agent编排层 |
| `strategist_agent` | 策略总监：制定营销策略 | Plan-Execute Plan阶段 | Agent编排层 |
| `writer_agent` | 创意文案：生成/修改文案 | Plan-Execute Execute + 循环 | Agent编排层 |
| `review_node` | 安全审核：安全检查+合规 | 条件分支 + HITL | Agent编排层 + 治理 |
| `route_after_review` | Coordinator路由 | 条件路由(Supervisor) | Agent编排层 |
| `publish_node` | 发布终态 | 顺序终点 | 用户交互层输出 |

### 上机任务（6个TODO，见starter.ipynb）

1. **TODO 1**：定义 `AgentSystemState`（TypedDict，10个字段，含 `Annotated[list, operator.add]` 追加模式 + `knowledge_context` Phase 2知识图谱字段）
2. **TODO 2**：实现 `researcher_agent`（MCP工具调用概念：读取Phase 2知识图谱）和 `strategist_agent`（Plan-Execute Plan阶段）
3. **TODO 3**：实现 `writer_agent`（Plan-Execute Execute阶段，带审核反馈的循环修改）
4. **TODO 4**：实现 `review_node`（安全检查+合规审核+HITL）和 `route_after_review`（条件路由+循环退出，Coordinator角色）
5. **TODO 5**：实现 `build_agent_system`（StateGraph装配：add_node + add_edge + add_conditional_edges + compile(interrupt_before + MemorySaver)）
6. **TODO 6**：实现 `run_capstone_hitl`（三步HITL：invoke -> update_state -> resume，打印真实输出）

---

## 2026前沿补充：LangGraph/MCP/A2A/天道推演×多Agent仿真

> v5.0新增前沿点，本Phase特色。这是本课程**独有**的交叉点。

### LangGraph企业编排

LangChain团队官方Agent编排框架（https://github.com/langchain-ai/langgraph），把Agent工作流建模为**有状态有向图**，原生支持条件路由、循环、状态持久化与人机交互（HITL）。生产级复杂Agent的事实标准。本Phase的StateGraph/条件边/interrupt/MemorySaver全部是真实LangGraph API。

### MCP工具接入

**MCP（Model Context Protocol）**：Anthropic提出的LLM接工具的标准协议。本Phase的researcher_agent通过读取Phase 2知识图谱模拟MCP工具调用 -- Agent通过标准协议调用知识图谱工具检索市场知识。企业级多Agent系统的未来：LangGraph做进程内编排 + MCP做工具接入 + A2A做跨进程协作。

### A2A Agent协作

**A2A（Agent-to-Agent Protocol）**：Google提出的Agent间通信协议（https://github.com/google/A2A）。本Phase的多Agent通过LangGraph State共享通信（同进程内A2A协作）；A2A解决的是跨进程、跨组织、跨框架的Agent间通信。**与MCP互补：MCP接工具，A2A接Agent**。

### 天道推演 × 多Agent仿真

**核心洞察**：LangGraph多Agent编排与项目CLAUDE.md的「天道推演系统」高度同构--

| 天道推演（思维框架） | LangGraph（可计算实现） |
|--------------------|-----------------------|
| 在意识中构建多路径沙盘 | 在代码中构建多Agent状态图 |
| 模拟不同决策路径下的未来走向 | 条件边展开多分支执行 |
| 选择最优路径或预判风险 | 评估各分支输出择优 |
| 记录前提假设、追踪偏差、更新因果模型 | Checkpointing持久化 + 反馈学习节点 |

**升级路径**：把天道推演从"思维框架"升级为**可计算多Agent沙盘**--用LangGraph模拟多个利益相关方Agent（品牌方/渠道方/消费者/竞品方）博弈，每个Agent是一个节点，条件边模拟博弈分支，推演不同决策路径下的结果分布。这把"天道推演"从个人认知能力变成可复现、可版本化、可团队协作的决策工具。

### Plan-Execute模式

先规划再执行的两阶段Agent架构（技能5 Day1 + LangGraph典型模式）。本Phase的strategist_agent(Plan) + writer_agent(Execute)即此模式。优势：比"让LLM一次性完成"更可控、更可调试、每阶段可独立评估。

---

## Capstone整合性

### Phase 2 -> Phase 3（数据层 -> Agent层）
- Phase 2产出知识图谱（实体-关系-实体三元组）
- Phase 3的researcher_agent读取知识图谱作为市场研究的知识基础
- `knowledge_context`字段是Phase 2到Phase 3的数据桥梁

### Phase 3 -> Phase 4（Agent层 -> 因果评估层）
- Phase 3产出的Agent系统做出营销决策（策略/文案/投放方案）
- Phase 4对Agent决策的因果效应进行验证（A/B测试/因果推断）
- HITL审批节点的Checkpointing为Phase 4提供可审计的决策链

### 技能5 + 技能2整合
- 技能5的Agent架构模式（Plan-Execute）-> strategist + writer
- 技能2的编排模式（顺序/条件/循环/HITL）-> StateGraph全流程
- 两个技能在Capstone Phase 3交汇：用技能2的编排工具实现技能5的架构模式

---

## 与后续Phase的衔接

- **Phase 2**：数据表示与知识图谱 -- 本Phase的researcher_agent调用Phase 2产出
- **Phase 4**：因果实验设计与验证 -- 本Phase的Agent决策由Phase 4验证因果效应
- **Phase 5**：商业模式评估 -- 本Phase的Agent系统是商业价值的技术载体

---

## 作业与评估

沿用独立教材Phase 3交付物清单（第654-659行）：系统架构文档 + LangGraph Agent工作流代码 + 人机协作治理框架 + Agent安全检查方案。本学习材料包新增上机交付物：

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6个TODO全部填好，基础版+HITL版均能跑通）
- [ ] 一段300字分析：修订循环的退出条件（`revision_count >= 3`）设成多少合理？为什么？取消退出条件会怎样？
- [ ] 一段300字分析：Phase 2知识图谱如何提升researcher_agent的研究质量？如果不用知识图谱，研究质量会怎样退化？
- [ ] （选做）用"天道推演 × 多Agent仿真"视角，为本Phase营销系统增加一个"消费者Agent"节点（模拟消费者反应），画出新的状态图

---

*本讲义由v5.0学习材料包升级生成。理论部分引用独立教材，上机部分用真实LangGraph库 + TODO脚手架 + 离线模拟LLM fallback + Phase 2知识图谱整合。*
*最后更新：2026-07-24*

## 学习科学层 (v6.0)

本单元采用刻意练习(Ericsson)/间隔重复(FSRS-6,SM-2)/建构对齐(Biggs ILO↔TLA↔AT)/牛津tutorial LLM仿真(Socratic,Hattie四级反馈)。mastery 阈值与 Worked-Faded 示例见 practice.md 与 alignment.md。交叉练习(interleaving)促进迁移, 提取练习(retrieval practice)优于重读。

## 研究产出与产业链接层 (v7.0)
本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+arXiv/https链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。详见 research.md 与 industry.md。

---

## 学术前沿层 (v9.0)

本单元新增 `frontier.md`：注入 2025-2026 最新学术前沿（N 篇真实 arXiv 论文 + 批判性综述 + delta_to_unit + ≥3 开放研究问题 + 方法论批评）。论文来自 `_frontier_corpus/capstone-ai-business-analytics.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证），覆盖前沿课题：端到端AI原生企业闭环（综合）。面向博后/教授级读者：批判性综述非罗列，delta_to_unit 显式指出前沿如何更新本单元所教，开放问题为可发表研究方向。详见 `frontier.md`。

---

## AI工程从零构建层 (v11.0)

本单元新增 `from_scratch.md`：手写 agent 编排状态机（Plan-Execute-Verify 三阶段 + 验证门控 + 修订循环），从零构建 python/dataclasses 版 FSM 编排引擎，不调 LangGraph StateGraph、不调 langchain。对应 rohitg00 P19/24 Plan Execute Control Flow + P19/29 End to End Coding Task Demo。core_algorithm 从第一性原理推导 DFA 转移函数 $\delta: Q \times \Sigma \to Q$ + 几何停止概率 $P(\text{ACCEPT}) = 1-(1-p)^K$，code_artifact 含手写骨架（AgentState dataclass + VerificationGate ABC + transition 转移函数），verification_property 验证 FSM 必然终止 + ACCEPT/REJECT 条件 + 几何概率数值。与 notes.md 的 LangGraph 库实现对比：库版用 StateGraph+add_conditional_edges+interrupt_before+MemorySaver 黑箱，from-scratch 版让控制流可逐行审计。这是 agent 编排的可计算内核--ai-engineering-from-scratch 的工程底座。
