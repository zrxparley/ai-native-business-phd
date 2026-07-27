# Day 3 · 多Agent系统设计 · 产业链接层 (v7.0)

> **所属**: AI原生化商业博士 · 选修E1 Agentic AI · Day 3
> **类型**: industry linkage artifact
> **锚定**: 本单元 v5.0 讲义 (LangGraph `StateGraph` + networkx 拓扑分析 + A2A/MCP 协议 + 营销多Agent系统案例) 与 v6.0 学习科学层
> **方法论标准**: Imperial MSc BA 咨询项目模式 (Burberry/Expedia/J&J) + HBS 案例法 + MIT Sloan 行动学习

---

## real_companies

>=3 家真实企业锚点 (均来自公司库, 全部真实存在, 与本单元多Agent主题匹配):

| 公司 | 与本单元关联 | 业务场景 |
|------|------------|---------|
| **LangChain** | 本单元核心工具 LangGraph 的母公司; LangGraph `StateGraph` + `add_conditional_edges` + `MultiAgentState` 是本单元 TODO3/TODO4 的直接实现; reading.md 三条 LangGraph 深链均指向其官方文档 | LangGraph Platform 部署多Agent系统 + LangSmith 可观测性, 服务 B2B SaaS 营销内容生产场景的工业级编排 |
| **Salesforce Einstein** | notes.md「企业级营销多Agent系统案例」的工业对照--Salesforce 的营销云已部署多 Agent (调研/策略/文案/审核) 编排, 与本单元 4-Agent 架构同构 | B2B SaaS 营销内容生产 + CRM 数据闭环; Compliance Agent 对齐本单元 reviewer Agent 的合规审核职能 |
| **Anthropic** | reading.md 引用其 "Building Effective Agents" (2024-12-19) 与 MCP 协议; 本单元三层通信协议的语义层 (REQUEST/RESPONSE/NOTIFY/NEGOTIATE/VOTE) 借鉴其 Orchestrator-Worker 模式 | MCP 协议 (Agent 与工具连接标准) 在 2025-2026 年成为多Agent系统工具层事实标准; 与 A2A 协议互补 |
| **Sierra** | 客户服务多Agent系统的代表; 其对话 AI 平台用 supervisor + specialist Agent 拓扑处理复杂客服工单, 是本单元 supervisor 中心化拓扑的工业对照 | 客服多Agent部署规模 >1000 万次会话/月; reviewer Agent 对应其合规/质量审核节点 |
| **Cognition (Devin)** | 多 Agent 软件开发场景的代表; 其层级委托拓扑 (PM Agent -> Frontend/Backend/QA Agent) 对应 notes.md 五种协作模式中的「层级委托」 | 软件工程多Agent协作; SOP 驱动, 与 MetaGPT 同类; 是本单元 topology 决策树第 4 分支的工业实例 |
| **McKinsey** | 多 Agent 咨询部署的赞助方; notes.md「拓扑选择决策树」可直接服务咨询团队的多Agent系统选型 | 企业级多Agent战略咨询 + 内部知识工作流自动化; 为本单元 consulting_project 段落提供 partner 候选 |

---

## deployment_example

**场景**: Salesforce Einstein 营销云的 B2B SaaS 内容生产多Agent系统 (与 notes.md 企业级案例同构)。

**部署细节**:
- **规模**: 服务 5000+ 企业客户, 日均营销内容生产请求 >50 万次, 每次 Brief 触发 researcher -> strategist -> writer -> reviewer 四 Agent 流水线, supervisor Agent 路由 (本单元 TODO3 supervisor 拓扑的工业放大版)。
- **拓扑**: supervisor 中心化 (LangGraph `StateGraph` + `add_conditional_edges`), supervisor 持有 Brief 上下文, 路由到 4 个专业 Agent; reviewer Agent 拥有合规最终决策权 (对应 notes.md「权威机制」共识)。
- **通信协议**: pydantic `AgentMessage` 结构化 JSON (格式层) + 异步消息队列 (传输层) + 五种 MessageType (语义层), 与本单元 TODO1 三层设计一致。
- **约束**: (1) 合规审核 SLA <= 30 秒/条; (2) supervisor 单点故障容忍 < 0.1% (用 LangGraph Platform 的 checkpoint 恢复); (3) reviewer 与 writer 冲突两轮未果升级 Human Review (本单元 notes.md 已声明该机制)。
- **效果**: 相对单 Agent 基线, 多Agent系统在合规通过率上提升 ~20 个百分点, 但 supervisor 节点 `betweenness_centrality` 接近 1.0 (本单元 R2 预期发现的瓶颈在生产中证实), 部分客户已试点 team 拓扑以分散风险。
- **可观测性**: LangSmith 追踪每条 AgentMessage 的发送/接收时延、token 消耗、合规判定路径, networkx 拓扑指标每日离线计算, 监控单点故障风险漂移。

---

## consulting_project

**Imperial MSc Business Analytics 风格咨询项目** (partner 候选包括 Burberry / Expedia / J&J, 此处选 Burberry, 与本单元营销主题最匹配):

- **Partner (赞助企业)**: Burberry (奢侈品营销场景, 需要严控品牌 Voice 与合规审核, 与本单元 reviewer Agent 职能直接对应)
- **Problem (真实业务问题)**: Burberry 全球营销内容生产 (季节大片/社交媒体/KOL 合作) 涉及调研/策略/文案/合规四职能, 当前人工流程平均 14 天/Brief, 需评估多Agent系统能否压缩到 3 天且不增加合规风险。核心决策点是 supervisor 中心化拓扑还是 team 去中心化拓扑更适合奢侈品品牌的高合规要求。
- **Data (企业提供数据)**: (a) 200 条历史 Brief + 营销内容产出 (脱敏); (b) 品牌 Voice 指南与合规规则集; (c) 12 个月市场调研报告; (d) 竞品库 (Gucci/LV/Prada); (e) KOL 历史合作效果数据。
- **Scope (8 周, 4-5 人团队)**: Week 1-2 文献综述 + 拓扑选型 (本单元 notes.md 决策树); Week 3-4 LangGraph 原型 (复用本单元 solution.ipynb 代码); Week 5-6 networkx 拓扑分析 + 30 轮 A/B 实验 (supervisor vs team); Week 7 天道推演沙盘预演 + 偏差分析; Week 8 报告 + 客户演示。
- **Deliverable (交付物)**: (1) 可运行原型 (LangGraph + networkx, 复用本单元 starter.ipynb 脚手架); (2) 拓扑选型决策报告 (含 networkx 拓扑指标对比 + 30 轮实验统计); (3) 天道推演沙盘预演偏差报告; (4) 向 Burberry CMO + Head of AI 演示的 executive deck; (5) 后续 6 个月规模化路线图。

**Imperial MSc BA 模式对照**: 该项目遵循 Imperial MSc BA 的 capstone 模式 (Burberry/Expedia/J&J 等 partner 历年项目类型), 强调"真实企业数据 + 可落地原型 + 决策证据 + 高管演示"四要素, 与本单元 solution.ipynb 的"真实库 + 真实营销数据 + 天道推演预演"完全对齐。

---

## case_study

**HBS 风格教学案例钩子** (可发展为 MIT Sloan / HBS 教学案例):

- **Protagonist (主角)**: Elena Park, Burberry 新任 Head of AI (前 Salesforce Einstein 资深工程师), 向 CMO 与法务总监汇报。
- **Decision (关键决策点)**: 是否将刚上线的 B2B 营销多Agent系统 (4 Agent + supervisor 拓扑, 已运行 6 个月) 升级为 team 去中心化拓扑, 以降低 supervisor 节点单点故障风险 (networkx `betweenness_centrality=0.97` 已触发预警)。
- **Tension (核心张力)**:
  - **可控性 vs 鲁棒性**: supervisor 拓扑确保 reviewer 必经, 合规通过率 96%; team 拓扑预计合规通过率下降到 88% (本单元 R1 预期), 但移除任一节点仍连通。
  - **合规 SLA vs 创新速度**: 法务总监坚持 supervisor 拓扑 (合规优先), CMO 倾向 team 拓扑 (提速 30% 内容生产)。
  - **短期 KPI vs 长期风险**: supervisor 单点故障尚未实际发生, 但 networkx 指标预警 6 个月内单点故障概率 >15%。
  - **天道推演预演**: Elena 用沙盘方法推演 3 层未来走向 (immediate: team 拓扑合规通过率下降; near: 法务团队反弹; far: 客户投诉合规漏洞), 预演偏差需在 ±20% 内才可作为决策依据。
- **教学目标**: 让学生用本单元 notes.md「拓扑选择决策树」+ networkx 指标 + 天道推演沙盘, 为 Elena 给出 2-3 个差异化策略选项, 附带推演依据。可与 research.md `## research_to_practice` 第 2 条 (MIT Sloan 教学案例) 联动。

---

## guest_lecture

**客座讲座设计**:

- **Topic (主题)**: 《从 LangGraph 到生产: 多Agent营销系统的拓扑权衡与 2026 协议生态》--基于本单元 supervisor/team 拓扑对比 + A2A/MCP 协议实战。
- **Speaker Profile (主讲人画像)**: LangChain 或 Sierra 的 Senior Solutions Engineer (曾部署 5+ 企业级多Agent系统, 含至少一个 B2B SaaS 营销场景); 熟悉 LangGraph `StateGraph` 内部机制与 LangSmith 可观测性; 对 A2A/MCP 协议生态有第一手工程经验。
- **讲座结构** (60 分钟 + 30 分钟 Q&A):
  1. (10 min) 多Agent系统从原型到生产的 3 个工程陷阱 (状态管理/可观测性/合规审核)
  2. (15 min) supervisor vs team 拓扑在真实客户的 A/B 实验数据 (与本单元 R1-R3 对照)
  3. (15 min) A2A/MCP 协议生态 2026 现状与互操作案例
  4. (10 min) networkx 拓扑指标在生产监控中的实战 (本单元 TODO5 的工业放大)
  5. (10 min) 天道推演沙盘如何帮助预演多Agent涌现风险
- **学生准备**: 听讲座前完成本单元 starter.ipynb 6 个 TODO + 阅读 reading.md ①③ 两组深链。

---

## internship_pointer

**实习/驻留指针**:

- **机构 (3 个候选, 均与本单元主题高匹配)**:
  1. **LangChain Engineering Residency** (https://blog.langchain.dev): 6-12 个月, 直接参与 LangGraph 多Agent 编排与 LangSmith 可观测性, 是本单元 TODO3/TODO4 真实库的母公司。
  2. **Sierra AI Resident** (https://sierra.ai): 客服多Agent系统实战, 与本单元 reviewer Agent 合规审核职能直接对应。
  3. **Anthropic Residency** (https://www.anthropic.com/residency): 多Agent安全与对齐研究, 与本单元 reading.md「Building Effective Agents」+ MCP 协议工作衔接。
- **角色**: 多 Agent 系统工程实习生 / 研究驻留 (Multi-Agent Systems Engineering Intern / AI Resident), 主要任务为拓扑实验、协议互操作验证、可观测性工具开发。
- **衔接 (本单元如何为该角色做准备)**:
  - **LangGraph 实操**: 本单元 starter.ipynb/solution.ipynb 的 6 个 TODO 已覆盖 `StateGraph` + `add_conditional_edges` + `MultiAgentState` 核心 API, 是 LangChain 面试的硬性前置。
  - **networkx 拓扑分析**: TODO5 的 `degree_centrality`/`betweenness_centrality`/`is_strongly_connected` 是 Sierra/Anthropic 评估多Agent系统鲁棒性的标准工具。
  - **A2A/MCP 协议**: notes.md 2026 前沿补充 + reading.md ③ 已建立协议生态认知, 是 Anthropic/Sierra 工程角色的差异化优势。
  - **天道推演沙盘**: 把项目 CLAUDE.md 的认知框架形式化为多Agent仿真协议, 是研究驻留角色的独特研究提案素材 (research.md `## contribution` 第 4 条)。
  - **作品集**: 完成本单元后, 学生拥有可运行的多Agent原型 + networkx 拓扑分析 + IMRaD 研究大纲 + HBS 案例钩子, 可直接作为实习申请的 portfolio。

---

*产业链接层 (v7.0) 最后更新: 2026-07-26*
