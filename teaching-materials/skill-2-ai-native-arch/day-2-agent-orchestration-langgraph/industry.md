# industry.md - Day 2 Agent 编排架构 + LangGraph · 产业链接层 (v7.0)

> 本文件锚定本单元 `notes.md` 的真实技术栈（LangGraph 1.x StateGraph / 条件分支 / 循环 / HITL `interrupt_before` / `MemorySaver` Checkpointing / Supervisor 拓扑 / Plan-Execute / A2A vs MCP / 天道推演×多Agent仿真），遵循 Imperial MSc BA 咨询项目模式（Burberry/Expedia/J&J）/ HBS 案例法 / MIT Sloan 行动学习模式。

---

## real_companies

| 公司 | 与本单元关联 | 业务场景 |
|------|-------------|---------|
| **LangChain** | LangGraph 的开发与商业运营方（`langchain-ai/langgraph`，MIT，"Build resilient agents"）。本单元 `starter.ipynb` 6 个 TODO 全部基于其 API。LangChain 提供 LangSmith（可观测性）/ LangGraph Cloud（托管部署）/ LangGraph Platform 商业化路径。 | 企业级 LangGraph 多 Agent 工作流的商业化托管 + 可观测性（对应本单元 `MemorySaver` 检查点持久化在生产环境的 LangSmith/LangGraph Cloud 升级）。 |
| **CrewAI** | LangGraph 在多 Agent 编排框架赛道的主要竞品。CrewAI 走"角色化 Agent + 任务委派"抽象（Crew/Agent/Task），LangGraph 走"有状态有向图"抽象（StateGraph/Node/Edge）。本单元的 Supervisor 拓扑在 CrewAI 中对应 `Process.hierarchical`。 | 跨框架对比选型：企业选 LangGraph（图可控 + HITL 原生）还是 CrewAI（角色隐喻 + 上手快）。本单元 `alignment.md` 的拓扑选型自检直接锚定该决策。 |
| **Sierra** | Bret Taylor 创办的对话式 AI 客服 Agent 平台（估值 45 亿美元，2024）。Sierra 在生产中大规模部署企业级 Agent 编排，其高风险节点（退款/换货/账户变更）天然需要 HITL 审批 + 状态持久化 -- 即本单元 `interrupt_before=["approval"]` + `MemorySaver` 的产业映射。 | 客服 Agent 编排：顺序（识别意图 -> 检索知识库 -> 生成回复）+ 条件（高风险路由人工）+ HITL（退款审批）+ 循环（不满意重生成）。Sierra 是本单元"营销 Agent 编排"模式的同构产业实例。 |
| **Anthropic** | Claude 模型 + MCP（Model Context Protocol）协议的提出方。本单元明确 MCP（接工具）/ A2A（接 Agent）/ LangGraph（进程内编排）三层互补定位 -- Anthropic 的 MCP 是工具接入层。同时 Anthropic "Building Effective Agents" 博客（https://www.anthropic.com/research/building-effective-agents）是本单元五种编排模式的概念源头。 | MCP 工具协议 + Claude 模型作为 LangGraph 节点的 LLM 后端 -- 企业级 Agent 编排的"模型 + 工具协议"基础设施。 |

> 四家公司全部真实存在（来源于公司库），覆盖本单元四个关键面向：框架方（LangChain）/ 竞品（CrewAI）/ 应用方（Sierra）/ 基础设施（Anthropic）。

---

## deployment_example

**Sierra 的企业级客服 Agent 编排部署（真实产业映射）**

Sierra 在生产中为大型企业（如 SiriusXM、Sonos、WeightWatchers）部署对话式客服 Agent，其编排架构与本单元的 LangGraph 营销编排图高度同构：

- **规模**：日均处理数百万次对话，覆盖售前咨询、售后支持、账户管理、退款/换货等场景。
- **编排映射**（对应本单元 `starter.ipynb` 5 节点）：
  - `research_agent` -> Sierra 的"意图识别 + 知识库检索"节点
  - `strategy_agent` -> "策略选择"节点（自助解决 / 转人工 / 升级）
  - `copywriter_agent` -> "回复生成"节点（带品牌语调约束）
  - `approval_node` -> **HITL 审批**节点（高风险操作如退款 > $100、账户删除必暂停）
  - `publish_node` -> "回复发送"终态
- **HITL 工程化**（对应本单元 `interrupt_before=["approval"]` 三步模式）：Sierra 的客服 Agent 在高风险节点暂停，状态持久化到外部存储（对应本单元 `MemorySaver` -> 生产级 `SqliteSaver`/`PostgresSaver`），人工审核后注入决策恢复执行 -- 这正是本单元 HITL 三步（`invoke` -> `update_state` -> `invoke(None)`）的产业实现。
- **约束**：SLA 要求首次响应 < 2s，整体解决率 > 70%，HITL 暂停不超 5 分钟；循环退出阈值类似本单元 `revision_count >= 3`（防止无限重生成）。
- **效果**：Sierra 公开案例显示客户自助解决率显著提升，人工工单量下降 30-50%（具体数字因客户而异）。

---

## consulting_project

**Imperial MSc Business Analytics 风格咨询项目**

- **Partner（赞助企业）**：Burberry（奢侈品零售，公司库成员，Imperial MSc BA 传统合作方）
- **Problem（真实业务问题）**：Burberry 的全球营销活动需跨 4 个职能（市场研究 -> 策略 -> 创意文案 -> 合规审核）协同，现行流程靠邮件 + Slack 串行，平均周期 14 天，合规违规率约 8%（不同市场法规差异）。能否用 LangGraph 多 Agent 编排把周期压缩到 3 天以内，同时让合规审核节点保留人工最终决策权（HITL）？
- **Data（企业提供数据）**：
  - 历史营销活动 brief + 最终文案 + 合规审核记录（脱敏，200 条）
  - 4 个市场的合规规则文档（EU GDPR / 中国 PIPL / 美国 FTC / 日本景品表示法）
  - 现行流程的时间戳日志（每个环节耗时）
- **Scope（8 周，4-5 人团队）**：
  - W1-2：现状建模（用 LangGraph `StateGraph` 还原现行流程，定位瓶颈节点）
  - W3-4：HITL 节点设计（哪些市场/哪些文案类型必 `interrupt_before`，`revision_count` 阈值定多少）
  - W5-6：原型实现（基于本单元 `starter.ipynb` 扩展，4 个 Agent 节点 + 合规审核节点 + Langfuse 可观测性）
  - W7：A/B 测试（HITL 模式 vs 纯自动模式，对比合规违规率与周期）
  - W8：交付 + 策略报告
- **Deliverable（交付物）**：
  1. **原型**：可运行的 LangGraph 多 Agent 营销编排系统（Python + LangGraph 1.x + 离线 mock LLM fallback）
  2. **模型**：HITL 节点配置模型（决策树：何时 `interrupt_before`，`revision_count` 阈值规则）
  3. **策略报告**：周期压缩 vs 合规违规率的权衡曲线 + 推荐部署方案
  4. **演示**：Burberry 营销团队可直接试用的 demo 环境

---

## case_study

**HBS 风格教学案例钩子**

- **Protagonist（主角）**：Marta Reynolds，Burberry 全球营销运营 Head of AI（前 McKinsey Engagement Manager，MBA + CS 背景）。
- **Decision（关键决策点）**：Marta 刚批准部署 LangGraph 多 Agent 营销编排系统（基于本单元架构），首月在英国市场测试成功（周期 14 天 -> 3 天，合规违规率 8% -> 1.5%）。现需决定是否推广到中国市场 -- 中国市场的 PIPL 合规要求更严，且文案需经政府审核（额外 HITL 节点）。同时 CTO 提出竞品方案：用 CrewAI 替代 LangGraph（角色隐喻更直观，但缺原生 HITL）。
- **Tension（核心张力/两难）**：
  1. **治理 vs 速度**：加 PIPL HITL 节点会让周期从 3 天回到 6 天，但删了则违规风险极高 -- `revision_count` 阈值设多少？
  2. **框架锁定 vs 灵活性**：LangGraph 的 `StateGraph` 抽象工程可控但学习曲线陡；CrewAI 的角色隐喻上手快但 HITL 需自实现 -- 切换成本 vs 长期维护成本？
  3. **天道推演视角**：Marta 用天道推演沙盘模拟三个分支（推广中国 + LangGraph / 推广中国 + 切 CrewAI / 暂缓中国先扩美国），每个分支推演 3 层未来走向（immediate 周期/合规 -> near 团队学习曲线 -> far 12 个月后平台演化）。

案例教学目标：让学员用本单元的四种编排模式 + HITL 三步 + 拓扑选型框架（`alignment.md`）分析 Marta 的决策，给出 2-3 个差异化策略选项。

---

## guest_lecture

**客座讲座**

- **Topic（主题）**：*"From StateGraph to Production: Deploying LangGraph Multi-Agent Systems at Enterprise Scale"* -- 从本单元的 `MemorySaver`（内存演示）到生产级 `SqliteSaver`/`PostgresSaver` + Langfuse 可观测性 + LangGraph Cloud 托管的工程跃迁，含 HITL 节点的真实 SLA 设计与 `revision_count` 阈值的 A/B 数据。
- **Speaker Profile（主讲人画像）**：LangChain 团队的 Senior Developer Advocate 或 LangGraph 核心维护者（曾参与 `interrupt_before` API 设计）；或者 Sierra 的 Staff Engineer（在生产中部署 LangGraph 编排客服 Agent，可讲真实 HITL 工程化案例与失败教训）。建议邀请前者讲框架演化、后者讲产业落地，形成 2 场对谈。

---

## internship_pointer

**实习/驻留指针**

- **机构 1：LangChain Open Source Contributor Program**
  - **角色**：LangGraph 生态贡献者（开源 PR 实习生）
  - **衔接**：本单元 `starter.ipynb` 6 个 TODO 让学员掌握 `StateGraph` / 条件边 / `interrupt_before` / `MemorySaver` 全套 API -- 直接对应 LangGraph 仓库的 `examples/` 目录贡献门槛。建议首月提 1-2 个 example PR（如"营销编排 HITL 模式"示例）。

- **机构 2：Sierra AI Residency（或 Customer Engineering 实习）**
  - **角色**：Agent Orchestration Resident / Solutions Engineer Intern
  - **衔接**：本单元的 HITL 三步模式（`invoke` -> `update_state` -> `invoke(None)`）+ 循环退出（`revision_count >= 3`）+ Supervisor 拓扑正是 Sierra 客服 Agent 编排的核心模式。学员可把本单元的营销编排图迁移到客服场景（refund/return/account 节点）作为面试作品。

- **机构 3：Google A2A Protocol Working Group（或 Anthropic MCP 贡献者）**
  - **角色**：协议生态贡献者 / Developer Relations Intern
  - **衔接**：本单元明确 MCP（接工具）/ A2A（接 Agent）/ LangGraph（进程内编排）三层互补定位 -- 学员可基于本单元的多 Agent 图，扩展为 A2A 跨进程协作原型（每个 Agent 独立进程，用 A2A 通信），作为协议工作组的贡献提案。

- **机构 4：Burberry / Expedia / J&J 等 Imperial MSc BA capstone sponsor**
  - **角色**：AI Orchestration Capstone Intern（4-5 人团队，8 周）
  - **衔接**：直接承接上文 `## consulting_project` 的设计 -- 本单元的 LangGraph 营销编排图作为 capstone 的技术起点，学员在 8 周内扩展为可交付原型 + 策略报告。
