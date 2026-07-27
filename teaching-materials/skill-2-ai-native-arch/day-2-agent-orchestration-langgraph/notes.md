# 技能2 · Day 2：Agent 编排架构 + LangGraph · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 技能2 AI原生企业架构 · Day 2
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：如何用 LangGraph 的有状态图编排企业级多 Agent 营销工作流，实现顺序/循环/条件分支 + 人机协同审批（HITL）+ 状态持久化？
> **v5.0 升级点**：① 真实库上机（LangGraph 1.x，非伪代码）② TODO 填空式起始笔记本 ③ 离线模拟 LLM fallback 使图端到端跑通 ④ Notebook 化 ⑤ 深链阅读 ⑥ 2026 前沿（A2A / Plan-Execute / 天道推演×多Agent仿真）

---

## 学习目标（学完你能做到）

1. 能用 LangGraph 的 `StateGraph` / `Node` / `Edge` 三要素解释"有状态有向图"如何替代线性 Chain，并从**企业架构视角**识别四种编排模式（顺序/并行/循环/条件）与多 Agent 协作拓扑（Supervisor/层级式）
2. 能为"研究Agent -> 策略Agent -> 写作Agent -> 审批节点 -> 发布"营销工作流画出状态图，识别条件分支（审批通过/不通过）与循环退出条件（`revision_count` 上限），说明 HITL 审批节点的企业治理意义
3. 能在**真实 LangGraph 库**上完成"定义 State -> 写节点函数 -> 装配图（含 `interrupt_before` + `MemorySaver`） -> 编译 -> 三步 HITL 运行（invoke -> update_state -> resume）"全流程，并解释 Checkpointing 的状态持久化作用
4. 能区分技能5 Day2（LangGraph mechanics：StateGraph/Node/Edge 怎么用）与本 Day（**企业架构视角**：编排模式分类/治理节点/协作拓扑），并说明 A2A 与 MCP 在多 Agent 协作中的互补定位（MCP 接工具，A2A 接 Agent）
5. 能用"天道推演 × 多 Agent 仿真"视角，把企业营销沙盘映射为 LangGraph 多 Agent 博弈图 -- 每条决策路径是一个条件分支，Checkpointing 记录推演假设，反馈学习节点更新因果模型

---

## 理论部分：精炼索引（详见独立教材）

> Day 2 的完整理论讲义见 [`../../../AI原生化商业博士_独立教材_技能2_AI原生企业架构.md`](../../../AI原生化商业博士_独立教材_技能2_AI原生企业架构.md) § Day 2（第 422-1041 行，含从 LangChain 到 LangGraph 演进 / StateGraph 核心概念 / Anthropic "Building Effective Agents" 五种模式 / Supervisor-Team-Chain 编排模式 / 完整营销 Agent 代码示例）。本讲义不重复，仅做上机所需的关键回顾与企业架构视角增量。

### 与技能5 Day2 的区别（重要）

| 维度 | 技能5 Day2（mechanics） | 技能2 Day2（企业架构视角，本 Day） |
|------|------------------------|----------------------------------|
| **重心** | LangGraph API 怎么用 | 编排模式分类 + 治理 + 拓扑 |
| **编排模式** | 单一工作流 | 顺序/并行/循环/条件 四模式体系 |
| **多 Agent 拓扑** | 单链条 | Supervisor / 层级式 / A2A 协议 |
| **HITL** | interrupt 机制 | 企业治理意义 + 三步模式工程化 |
| **状态持久化** | MemorySaver 用法 | 故障恢复 / 审计追溯 / 生产部署 |
| **前沿** | 多Agent仿真×天道推演 | A2A / MCP / Plan-Execute / 天道推演 |

### 关键回顾 1：从 LangChain Chain 到 LangGraph StateGraph

LangChain 的 Chain 是**线性流水线**（A->B->C->输出），适合简单 LLM 应用。但企业级 Agent 工作流需要条件分支、循环、人机协同、状态持久化 -- 这些 Chain 做不到。LangGraph 把工作流建模为**有状态有向图**：

| LangGraph 概念 | 是什么 | 企业营销对应 |
|---------------|--------|-------------|
| `StateGraph` | 维护全局 State 的有向图 | 整个营销活动编排系统 |
| `State`（TypedDict） | 所有节点共享的全局状态 | `CampaignState`（brief/analysis/strategy/...） |
| `Node`（节点函数） | State -> dict 的处理函数 | research_agent / strategy_agent / copywriter_agent / approval_node |
| `Edge`（普通边） | A 无条件到 B | research -> strategy -> copywriter |
| `Conditional Edge` | 根据 State 动态选下一节点 | approval -> publish 或 -> copywriter（修订） |
| `Checkpointing` | State 持久化到外部存储 | `MemorySaver`（内存）/ `SqliteSaver`（持久） |
| `interrupt_before` | 指定节点前自动暂停 | `interrupt_before=["approval"]` 审批前暂停 |

### 关键回顾 2：四种编排模式（本 Day 代码全覆盖）

1. **顺序（Sequential）**：research -> strategy -> copywriter。用 `add_edge` 串联。
2. **条件分支（Conditional）**：approval -> publish OR revise。用 `add_conditional_edges` + 条件函数。
3. **循环（Loop）**：copywriter -> approval -> copywriter。条件边指回前序节点，**必须有退出条件**（`revision_count >= 3`）。
4. **人机协同（HITL）**：`interrupt_before=["approval"]` + `update_state` + `invoke(None)` 三步模式。

### 关键回顾 3：多 Agent 协作拓扑

- **Supervisor（主管）**：条件路由函数扮演 Supervisor，拥有全局视图，决定下一步去哪个节点。本 Day 的 `route_after_approval` 即此角色。
- **层级式（Hierarchical）**：顶层 Supervisor 管理子团队（如品牌团队含内容+设计 Agent，效果团队含投放+分析 Agent）。适合大型复杂项目。
- **A2A（Agent-to-Agent Protocol）**：Google 2024 提出的 Agent 间通信协议（https://github.com/google/A2A）。本 Day 的多 Agent 通过 State 共享通信；A2A 提供跨进程/跨组织 Agent 通信标准。**与 MCP 互补：MCP 接工具，A2A 接 Agent**。

### 关键回顾 4：Plan-Execute 模式

本 Day 的 strategy_agent（Plan 阶段：制定策略）+ copywriter_agent（Execute 阶段：生成文案）即 Plan-Execute 模式。这是 LangGraph 的典型两阶段架构 -- 先规划再执行，比"让 LLM 一次性完成"更可控。

### 关键回顾 5：HITL 三步模式（企业治理工程化）

```
Step 1: graph.invoke(initial_state, config)      # 执行到 approval 前暂停
Step 2: graph.update_state(config, {"approved": True})  # 注入人工决策
Step 3: graph.invoke(None, config)                # 恢复执行至完成
```

这是企业 AI 治理的工程基础 -- 高风险决策节点设置人机协同，确保人类保留最终决策权。详见独立教材第 504-511 行"Human-in-the-loop"节。

---

## 上机部分：在真实 LangGraph 上构建企业营销编排系统

> **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO 填空版，6 个 TODO）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，gated）
> **真实库与资源**：[`data/README.md`](./data/README.md)（LangGraph 库 + langchain-core + pydantic）

### 为什么用真实库 LangGraph 而非伪代码

v4.0 的代码用"伪代码 / 模拟框架"--模拟框架学不到真实 API 的细节（State 怎么定义、条件边怎么注册、检查点怎么编译、interrupt 怎么暂停-恢复）。v5.0 改用 **LangGraph**（langchain-ai/langgraph，1.x，MIT，"Build resilient agents"）：LangChain 团队官方 Agent 编排框架，生产级复杂 Agent 的事实标准。

### 离线模拟 LLM fallback

无 `OPENAI_API_KEY` 时，自动降级为 `OfflineMockLLM`（返回固定营销文案），使图能端到端跑通。这不是"伪代码"--编排逻辑（StateGraph/条件边/interrupt/Checkpointing）全部是真实 LangGraph API；只有 LLM 返回值是固定的，聚焦编排学习。

### 营销映射（企业架构视角）

| LangGraph 节点 | 营销职能 | 编排模式 | 企业架构意义 |
|---------------|---------|---------|-------------|
| `research_agent` | 市场分析师：受众/竞品/趋势 | 顺序第 1 步 | 数据驱动决策入口 |
| `strategy_agent` | 策略总监：主张/定位/渠道 | Plan-Execute Plan 阶段 | 营销策略规划 |
| `copywriter_agent` | 创意文案：生成/修改文案 | Plan-Execute Execute + 循环 | 内容生产 |
| `approval_node` | 合规审核：通过/修改 | 条件分支 + HITL | 企业治理关卡 |
| `route_after_approval` | Supervisor 路由 | 条件路由 | 工作流控制中心 |
| `publish_node` | 发布终态 | 顺序终点 | 交付输出 |

### 上机任务（6 个 TODO，见 starter.ipynb）

1. **TODO 1**：定义 `CampaignState`（TypedDict，9 个字段，含 `Annotated[list, operator.add]` 追加模式）
2. **TODO 2**：实现 `research_agent` 和 `strategy_agent`（顺序编排 + Plan-Execute Plan 阶段，用 `SystemMessage`/`HumanMessage` 调 LLM）
3. **TODO 3**：实现 `copywriter_agent`（Plan-Execute Execute 阶段，带审核反馈的循环修改）
4. **TODO 4**：实现 `approval_node`（HITL + 自动双模式）和 `route_after_approval`（条件路由 + 循环退出）
5. **TODO 5**：实现 `build_campaign_graph`（StateGraph 装配：add_node + add_edge + add_conditional_edges + compile(interrupt_before + MemorySaver)）
6. **TODO 6**：实现 `run_with_hitl`（三步 HITL：invoke -> update_state -> resume，打印真实输出）

---

## 2026 前沿补充：A2A / Plan-Execute / 天道推演×多Agent仿真

> v5.0 新增前沿点，本 Day 特色。

### A2A（Agent-to-Agent Protocol）

Google 2024 提出的 Agent 间通信协议（https://github.com/google/A2A）。与 MCP 互补：
- **MCP（Model Context Protocol）**：LLM 接工具的标准协议（Anthropic 提出）
- **A2A（Agent-to-Agent Protocol）**：Agent 接 Agent 的标准协议（Google 提出）

本 Day 的多 Agent 通过 LangGraph State 共享通信（同进程内）；A2A 解决的是跨进程、跨组织、跨框架的 Agent 间通信。企业级多 Agent 系统的未来：LangGraph 做进程内编排 + A2A 做跨进程协作 + MCP 做工具接入。

### Plan-Execute 模式

先规划再执行的两阶段 Agent 架构（LangGraph 典型模式）。本 Day 的 strategy_agent(Plan) + copywriter_agent(Execute) 即此模式。优势：比"让 LLM 一次性完成"更可控、更可调试、每阶段可独立评估。

### 天道推演 × 多 Agent 仿真

**核心洞察**：LangGraph 多 Agent 编排与项目 CLAUDE.md 的「天道推演系统」高度同构--

| 天道推演（思维框架） | LangGraph（可计算实现） |
|--------------------|-----------------------|
| 在意识中构建多路径沙盘 | 在代码中构建多 Agent 状态图 |
| 模拟不同决策路径下的未来走向 | 条件边展开多分支执行 |
| 选择最优路径或预判风险 | 评估各分支输出择优 |
| 记录前提假设、追踪偏差、更新因果模型 | Checkpointing 持久化 + 反馈学习节点 |

**升级路径**：把天道推演从"思维框架"升级为**可计算多 Agent 沙盘**--用 LangGraph 模拟多个利益相关方 Agent（品牌方/渠道方/消费者/竞品方）博弈，每个 Agent 是一个节点，条件边模拟博弈分支，推演不同决策路径下的结果分布。这把"天道推演"从个人认知能力变成可复现、可版本化、可团队协作的决策工具。

**参考**：项目 CLAUDE.md「天道推演系统」（六能力：局势感知/因果链追踪/沙盘模拟/概率评估/最优路径推荐/反馈学习）

---

## 与后续 Day 的衔接

- **Day 1**：从流程驱动到智能驱动 + AI 治理框架 -- 今天是把治理框架落到 LangGraph 的 HITL 审批节点
- **Day 3**：人机协作治理 + 组织变革 -- 今天的 `interrupt_before` 是技术实现，Day 3 讲组织层面的治理设计
- **Day 4**：企业级架构参考设计 + 行动研究 -- 今天的单进程编排要扩展为分布式（A2A）+ 生产级（SqliteSaver/PostgresSaver + Langfuse 可观测性）

---

## 作业与评估

沿用独立教材 § Day 2 既有作业设计。本学习材料包新增上机交付物：

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6 个 TODO 全部填好，基础版 + HITL 版均能跑通）
- [ ] 一段 300 字分析：修订循环的退出条件（`revision_count >= 3`）设成多少合理？为什么？取消退出条件会怎样？
- [ ] （选做）用"天道推演 × 多 Agent 仿真"视角，为本 Day 营销系统增加一个"消费者 Agent"节点（模拟消费者反应），画出新的状态图

---

*本讲义由 v5.0 学习材料包升级生成。理论部分引用独立教材，上机部分用真实 LangGraph 库 + TODO 脚手架 + 离线模拟 LLM fallback。*
*最后更新：2026-07-24*

---

## 学习科学层 (v6.0)

> v6.0 在 v5.0 基础上加**学习科学层** (4 个新文件 + 本节), 不破坏 v5.0 基线。
> 哲学增量: v5.0 "真实即严谨 · 练习即掌握" -> v6.0 "**科学即高效 · 反馈即成长**" -- 用学习科学把"练习"升级为"刻意练习 + 间隔重复 + 建构对齐 + 牛津 tutorial 仿真"。

### 设计依据 (4 agent 调研合成)
- **刻意练习 (Ericsson deliberate practice)**: `practice.md` 把本 Day 的"装配 LangGraph 图"拆为 3 子技能 (S1 StateGraph装配 / S2 HITL三步 / S3 拓扑选型), 每 drill 含 `difficulty` / `reps_required` / `feedback_rule` / **Worked-Faded** 三阶段 (worked 完整示范 -> faded 部分填空 -> independent 独立解)。MIT OpenLearning 明文: 提取练习 (测试效应) + 交叉 interleaving (A1B1C1...B2C2A2...C3A3B3 模式, 不块状) + Worked-Faded 示例。
- **间隔重复 (FSRS-6 / SM-2 spaced retrieval)**: `schedule.json` 用 FSRS-6 (request_retention=0.9, 21 weights, SM-2 备份 EF0=2.5) 排 4 张卡片 (C1 StateGraph三要素 / C2 HITL三步 / C3 拓扑选型A2A/Plan-Execute / C4 天道推演同构), 间隔 [1,3,8,21,60,180] 天。Butler 2010 证据: 检索练习 (推断题) 68% vs 重学 44%。
- **建构对齐 (Biggs constructive alignment)**: `alignment.md` 列 ILO↔TLA↔AT 矩阵 (3 行, 每 ILO 对应 starter TODO + drill + tutorial Socratic + AT), 含 `mastery_threshold` 与 3 自检 (Feed Up / Feed Back / Feed Forward)。不经 TLA 能过 AT = 对齐失败。
- **牛津 tutorial + Hattie formative feedback**: `tutorial.ipynb` 仿真 Oxford tutorial (1对1, **Socratic** 追问, **禁直接答案**, devil's advocate 角色), 配 Hattie (2007) 四级反馈 ([TASK] / [PROCESS] / [SELF-REG] / [FEED-FORWARD], 避 Self 级表扬)。限频每单元 1 次/天 (与 Oxford 每周 1 次同构, 防依赖)。

### 4 新文件
1. `practice.md` - 刻意练习 (skill_target + 3 drills + Worked-Faded + 交叉 interleaving + weak_loop)
2. `schedule.json` - FSRS-6 间隔重复 (4 卡片, SM-2 备份)
3. `alignment.md` - Biggs 建构对齐 (ILO↔TLA↔AT + mastery + 3 自检)
4. `tutorial.ipynb` - 牛津 tutorial LLM 仿真 (Socratic + Hattie 四级 + student_model)

### 验收
- **v5.0 基线 (1-7)**: `verify_unit.py` 全通过 (本节追加不破坏)
- **v6.0 新层 (8-12)**: `verify_v6_unit.py` 5/5

> 学习科学层把 v5.0 的"练习即掌握"升级为"科学即高效 · 反馈即成长" -- 用刻意练习 + 间隔重复 + 建构对齐 + 牛津 tutorial 仿真, 把"代码对错"评估升级为"**代码 + 辩护 + 长期保持**"。

---

## 研究产出与产业链接层 (v7.0)

本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+arXiv/https链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。详见 research.md 与 industry.md。
