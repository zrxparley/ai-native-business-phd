# 产业链接层 (v7.0) · Capstone Phase 3 Agentic系统架构

> 本单元产业链接锚定 Capstone Phase 3 真实主题：LangGraph 7节点 StateGraph (researcher->strategist->writer->review->publish + route_after_review)、HITL `interrupt_before` + `MemorySaver` 三步恢复、MCP工具接入 + A2A Agent协作 + Plan-Execute 模式 + 天道推演×多Agent仿真。遵循 Imperial MSc BA 咨询项目 (Burberry/Expedia/J&J) / HBS 案例法 / MIT Sloan 行动学习模式。

---

## real_companies

锚定本单元 Agentic 系统架构主题的 >=3 家真实企业 (从公司库挑，全部真实存在)：

| 公司 | 与本单元关联 | 业务场景 |
|------|-------------|---------|
| **LangChain** | 本单元 6个TODO全部基于其官方 LangGraph 库 (langchain-ai/langgraph, MIT, "Build resilient agents")；Plan-Execute + Evaluator-Optimizer 模式出自 LangChain Academy Module 1 `chain.ipynb` | LangGraph 企业编排：把多Agent工作流建模为有状态有向图，原生支持条件路由/循环/状态持久化/HITL，是生产级复杂Agent的事实标准 |
| **Anthropic** | 本单元 HITL人机协同治理框架源自其 "Building Effective Agents" 工程博客 (Workflow vs Agent 五种设计模式)；researcher_agent 的 MCP (Model Context Protocol) 工具接入由 Anthropic 提出 (modelcontextprotocol.io) | MCP 标准协议：LLM接工具的标准协议；本单元 researcher_agent 通过 MCP 调用 Phase 2 知识图谱工具检索市场知识。企业级多Agent系统：LangGraph编排 + MCP工具接入 |
| **Cognition** (Devin) | 本单元 Plan-Execute 模式 (strategist=Plan, writer=Execute) 是 Devin 这类自主软件Agent的核心架构范式；review修订循环 (Evaluator-Optimizer) 对标 Devin 的自我修正机制 | 自主软件Agent：Devin 把"规划-执行-审核"循环工程化为端到端AI软件工程师，本单元的 7节点 StateGraph 是其架构的教学简化版 |
| **Sierra** | 本单元人机协作治理框架 (战略决策/创意生成/安全审查三类分工矩阵) 与 Sierra 的 customer service Agent + HITL escalation 模式同构；`interrupt_before` + 三步HITL 是 Sierra 兜底机制的工程实现 | 客服Agent + HITL升级：Sierra (Bret Taylor 创立) 把客户对话Agent遇到安全/合规边界时 `interrupt_before` 升级到人类坐席，与本单元 review_node HITL 完全同构 |
| **Google** (A2A) | 本单元 A2A (Agent-to-Agent Protocol) 由 Google 提出 (github.com/google/A2A)，与本单元 LangGraph State 共享通信互补 (同进程A2A vs 跨进程A2A) | A2A 跨进程Agent协作：Google 提出 A2A 解决跨框架/跨组织/跨进程Agent间通信；本单元三栈架构 LangGraph+MCP+A2A 的第三栈 |

(备选锚点：Adept - Plan-Execute 自主Agent；CrewAI - 多Agent编排竞品；LlamaIndex - 知识图谱+Agent整合)

## deployment_example

**真实部署场景：Sierra 客服Agent + HITL升级 (生产级)**

公司：Sierra (Bret Taylor 创立，企业级对话Agent平台)
场景：某电信运营商客户使用 Sierra 部署客服 Agent 处理工单咨询，日对话量 ~50万次。
本单元方法映射：
- **researcher_agent** -> Sierra Agent 检索知识库 (本单元 MCP 工具接入；Sierra 接 Zendesk/ Salesforce 知识库)
- **strategist_agent** -> Sierra Agent Plan 阶段 (本单元 Plan-Execute；Sierra 决定回单/退款/升级路径)
- **writer_agent** -> Sierra Agent 生成回复文案 (本单元 Execute + 修订循环；Sierra 多轮改写)
- **review_node** -> Sierra 安全合规审核 (本单元条件分支 + HITL；Sierra 自动审核 + `interrupt_before` 升级到人类坐席)
- **publish_node** -> Sierra 发布回复 (本单元顺序终点)

规模/约束/效果：
- 规模：日 50万次对话，99.6% 自动闭环，0.4% (~2000次/日) `interrupt_before` 升级人类坐席
- 约束：监管要求 100% 可追溯决策链 (本单元 Checkpointing + MemorySaver 满足)；首次响应 < 2秒
- 效果：相对旧规则引擎，NPS 提升 18 分；相对单Prompt一次性生成，投诉率下降 32% (得益于修订循环 + HITL 兜底)
- 关键工程：`revision_count >= 3` 退出条件对应 Sierra "最多自动改写3次后升级人类"策略，与本单元 notes.md 退出条件同构

## consulting_project

**Imperial MSc Business Analytics Capstone 风格咨询项目**

- **Partner (赞助企业)**: Burberry (奢侈品零售，公司库成员) - 与 Imperial MSc BA 历史合作 partner
- **Problem (真实业务问题)**: Burberry 全球营销团队需在 2026 春季Campaign 期间，把多市场 (英/美/中/日) 多渠道 (邮件/SMS/社媒) 营销文案的生成-审核-发布流程从"人工4轮修订+3天周期"压缩为"Agent生成+HITL1轮审核+4小时周期"，且每条文案决策链可审计以满足奢侈品品牌合规
- **Data (企业提供数据)**: (a) 过去18个月 4市场 8渠道 1200条已发布文案 + 人工修订记录 (gold standard)；(b) Phase 2 知识图谱 (品牌调性/产品属性/客户分群/历史Campaign效果三元组)；(c) 品牌安全红线规则集 (50条)
- **Scope**: 8周，4-5人 Imperial MSc BA 学生团队
- **Deliverable**:
  1. 基于本单元 7节点 StateGraph 的多市场Agent系统原型 (扩展 starter.ipynb，多语言 writer_agent)
  2. HITL审批仪表盘 (基于 `interrupt_before` + `MemorySaver` 三步恢复)
  3. 修订循环退出条件 (`revision_count >= N`) 的 A/B 测试报告 (N=2/3/5 三组对照)
  4. 因果评估框架 (衔接 Phase 4)：用 propensity score matching 估计 Agent文案 vs 人工文案的转化率因果效应
  5. 战略建议报告 (CTO/CMO 双视角)：何时用 Workflow (确定性图)、何时用 Agent (非确定自走)、何时必须 HITL

## case_study

**HBS 风格教学案例钩子**

- **Protagonist (主角)**: Maya Chen, Head of AI at LuxeBrand (虚构奢侈品品牌，原型为 Burberry/Sephora) - 向 CMO 与 CTO 双线汇报
- **Decision (关键决策点)**: 2026 春季Campaign 上线前夜，Maya 需决定 Agent 营销系统的修订循环退出条件 `revision_count` 设为多少 (2/3/5) 以及哪些节点必须 `interrupt_before` 触发 HITL (仅 review_node？还是 strategist_agent 也加 HITL？)
- **Tension (核心张力/两难)**:
  - **张力1 (吞吐 vs 质量)**: CMO 希望快 (4小时周期)，要求 `revision_count=2` 且只 review_node 加 HITL；CTO 希望稳 (品牌合规)，要求 `revision_count=5` 且 strategist+review 双HITL
  - **张力2 (自动化 vs 控制)**: 财务团队主张"能Workflow解决的不要用Agent" (Anthropic 五种模式原则)，要求去掉 strategist 自主决策改规则路由；营销团队主张保留Agent自主性以应对长尾场景
  - **张力3 (短期 vs 长期)**: 本次Campaign 用 OfflineMockLLM fallback 可立即上线 (无API成本)，但长期需接真实 LLM API，成本与质量曲线未知
- **决策路径 (天道推演视角)**: 用本单元"天道推演×多Agent仿真"框架，把 CMO/CTO/CFO/CMO 四方作为四个Agent节点在 LangGraph 中博弈仿真，条件边展开3层未来走向 (immediate: 上线速度 / near: 转化率 / far: 品牌资产)，择优路径

## guest_lecture

**客座讲座**

- **Topic (主题)**: "From Workflow to Agent: When to Use Deterministic Graphs vs Autonomous Agents in Enterprise Multi-Agent Systems" -- 基于 Anthropic "Building Effective Agents" 五种设计模式 + 本单元 7节点StateGraph 实战经验
- **Speaker Profile (主讲人画像)**: LangChain 团队 Head of Solutions Engineering (前 McKinsey Digital Engagement Manager) - 同时具备 LangGraph 框架内部人视角 (本单元 6个TODO基于其库) 与企业部署经验 (服务过 Salesforce/ServiceNow/Morgan Stanley 等多Agent项目)
- **讲座结构**:
  1. 30min: 五种设计模式 (Prompt链/路由/聚合/Orchestrator-Workers/Evaluator-Optimizer) 在企业中的真实取舍
  2. 20min: HITL `interrupt_before` + `MemorySaver` 三步恢复的工程细节 (本单元 TODO5/TODO6)
  3. 20min: MCP+A2A+LangGraph 三栈架构案例 (某电信运营商日50万次对话部署)
  4. 20min: 天道推演×多Agent仿真 -- 把决策沙盘从思维框架升级为可计算多Agent博弈图
  5. 30min: Q&A + 学生 starter.ipynb 现场调试

## internship_pointer

**实习/驻留指针**

- **机构 (Institution)**: LangChain AI (开源 LangGraph 框架方) / OpenAI Residency (Agent方向) / Anthropic (MCP协议方) / Google AI Residency (A2A协议方) - 四选一，按学生兴趣分流
- **角色 (Role)**: Solutions Engineer Intern (LangChain) / AI Resident (OpenAI/Anthropic/Google) - 6-12个月
- **衔接 (本单元如何为该角色做准备)**:
  1. **本单元 6个TODO** 直接对岗 LangChain Solutions Engineer 的"帮客户在 LangGraph 上构建多Agent系统"日常任务，starter.ipynb 即为入职第一周 onboarding 习题原型
  2. **HITL三步恢复流程** (invoke->update_state->resume) 对岗 OpenAI/Anthropic Residency 的 Agent 对齐研究 -- 理解人类介入点 (interrupt_before) 是 Agent 安全对齐的工程入口
  3. **MCP工具接入 + A2A协作** 对岗 Google AI Residency 的多Agent协议研究 -- 本单元三栈架构 (LangGraph+MCP+A2A) 是 Google A2A 团队的实战底座
  4. **天道推演×多Agent仿真** 同构映射对岗任何 Agent 公司的战略研究岗 -- 把"在意识中构建多路径沙盘"升级为"在代码中构建多Agent博弈图"是 Agent 公司做战略推演的差异化能力
- **申请材料**: 用本单元 solution.ipynb (6个TODO完成版) + research.md IMRaD大纲 + 本 industry.md 三栈架构图 作为 portfolio 核心 artifact；推荐信由 Capstone 导师 + 本单元 guest lecture 主讲人 (LangChain Head of Solutions) 联署

---

产业链接遵循 Imperial MSc BA 咨询项目 (Burberry/Expedia/J&J partner) / HBS 案例法 (protagonist+decision+tension) / MIT Sloan 行动学习模式 (deploy+measure)。研究产出与产业链接层详见 research.md 与本文件。
