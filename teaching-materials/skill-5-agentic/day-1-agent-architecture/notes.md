# 技能5 · Day 1：Agent系统架构设计 · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 技能5 Agentic系统工程与落地 · Day 1
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：如何为营销场景设计一个可控、可观测的Agent系统？
> **v5.0 升级点**：① 新增真实库上机（LangChain/LangGraph 构建 ReAct Agent）② 新增 TODO 填空式起始笔记本 ③ Notebook 化 ④ 深链阅读 ⑤ 2026 前沿（MCP 协议）

---

## 学习目标（学完你能做到）

1. 能用 ReAct/Plan-Execute/Reflection 三大 Agent 架构模式解释"Agent如何决策"，并指出各模式在营销场景中的适用边界
2. 能用 LangChain/LangGraph 真实库构建一个带工具调用（Tool Calling）和短期记忆（Memory）的 ReAct Agent，并在真实营销任务上运行
3. 能为营销 Agent 设计工具集（计算器/文本分析/文件读写），解释工具签名（名称/描述/参数Schema）如何影响 LLM 的工具选择
4. 能实现一个 Reflection（评估者-优化者）循环，让 Agent 自检并改进输出质量
5. 能用 Anthropic "Building Effective Agents" 五种模式为营销需求选择合适架构，并说明何时用 Workflow vs Agent

---

## 理论部分：精炼索引（详见独立教材）

> Day 1 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_技能5_Agentic系统工程与落地.md` § Day 1](../../AI原生化商业博士_独立教材_技能5_Agentic系统工程与落地.md)（3.1.1-3.1.4 节，已包含四大组件/三大模式/单多Agent/Anthropic五模式）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：Agent 四大核心组件

| 组件 | 问题 | 营销示例 |
|------|------|---------|
| Perception（感知） | Agent 如何"看到"世界？ | 读取用户输入、检索知识库、调用市场数据API |
| Planning（规划） | Agent 如何"决定"下一步？ | ReAct循环 / Plan-Execute / Reflection |
| Memory（记忆） | Agent 如何"记住"过去？ | 短期（对话上下文）/ 长期（用户偏好、历史交互） |
| Action（行动） | Agent 如何"改变"世界？ | 调用工具（搜索/计算/API）、生成内容、触发业务流程 |

四大组件构成 OODA 循环（Observe-Orient-Decide-Act），与军事决策理论一脉相承。

### 关键回顾 2：三大 Agent 架构模式

**ReAct（Reasoning + Acting）**：Thought-Action-Observation 交替循环

```
Thought: 用户要推广护肤品，我需要先计算ROI
Action: calculate_roi(revenue=598000, cost=66000)
Observation: ROI = 806.1%
Thought: ROI很高，接下来分析用户评价
Action: analyze_sentiment("效果好，推荐！")
Observation: 情感得分: 2（正面）
Thought: 评价正面，现在写策略
Action: write_strategy("strategy.txt", "...")
```

优势：简单直观、灵活适应。劣势：可能陷入循环、成本不可控。

**Plan-and-Execute**：先规划再执行

```
Planner: 1.分析目标人群 2.竞品分析 3.差异化定位 4.投放策略 5.创意内容
Executor: 逐步执行步骤1 -> 2 -> ... -> 5
```

优势：全局计划、成本可预测。劣势：计划静态，前提错误需重规划。

**Reflection（反思）**：生成 -> 评估 -> 改进循环

```
生成初稿 -> 评估("品牌调性不一致，缺少数据支撑") -> 修改 -> 再评估 -> 最终输出
```

优势：利用 LLM 自我批评提升质量。劣势：增加 token 消耗和延迟。

### 关键回顾 3：工具调用（Tool Calling）

工具是 Agent 的"手"。在 LangChain 中，用 `@tool` 装饰器定义工具：

```python
from langchain_core.tools import tool

@tool
def calculate_roi(revenue: float, cost: float) -> str:
    """计算营销投资回报率（ROI）。
    参数：revenue - 总收入（元）；cost - 总成本（元）
    返回：ROI 百分比"""
    roi = (revenue - cost) / cost * 100
    return f"ROI = {roi:.1f}%"
```

**关键点**：工具的**名称、docstring、参数类型**就是 LLM 看到的"接口契约"。docstring 写不清楚，LLM 就不会正确调用。

### 关键回顾 4：Agent 记忆（Memory）

- **短期记忆**：当前对话的 messages 列表。LangGraph 用 `MemorySaver`（checkpointer）实现，按 `thread_id` 隔离不同会话。
- **长期记忆**：跨会话的用户偏好、历史交互。生产中通常用向量数据库（如 Chroma/Pinecone）+ 结构化存储（如 Redis/PostgreSQL）。

### 关键回顾 5：Anthropic 五种模式（生产实践参考）

| 模式 | 复杂度 | 可控性 | 延迟 | 适用场景 |
|------|:------:|:------:|:----:|---------|
| Prompt Chaining | 低 | 高 | 中 | 固定步骤流程 |
| Routing | 低 | 高 | 低 | 输入分类处理 |
| Parallelization | 中 | 中 | 低 | 可分解并行任务 |
| Orchestrator-Workers | 高 | 中 | 高 | 动态分解复杂任务 |
| Evaluator-Optimizer | 中 | 高 | 高 | 质量敏感的生成任务 |

**实践建议**：从简单模式开始，"能用 Workflow 解决的，不要用 Agent"。Workflow 是确定性的、可控的；Agent 是非确定性的、难以预测的。

---

## 上机部分：用真实库构建营销 ReAct Agent

> 📓 **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO 填空版，你来做）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，做完再看）
> 📦 **真实库说明**：[`data/README.md`](./data/README.md)（LangChain/LangGraph + 真实工具 + LLM API 配置）

### 为什么用真实库而非模拟代码

v4.0 的代码用"伪代码 + 模拟输出"--模拟代码让你看到结构，但学不到"真实工具如何定义、Agent loop 如何运行、LLM 如何选择工具"。v5.0 改用 **LangChain + LangGraph 真实库**：`create_react_agent` 是生产级 API，`@tool` 装饰器是真实工具定义方式，`MemorySaver` 是真实的会话持久化。你写的代码可以直接用于生产。

### 营销映射（关键桥接）

Agent 架构直接映射到营销 Agent 流水线：

| Agent 组件 | 营销对应 | 本 Day 实现 |
|-----------|---------|------------|
| 感知（用户输入） | 营销需求描述 | "为一款护肤品制定策略" |
| 工具：calculate_roi | ROI 计算 | 投入产出比分析 |
| 工具：analyze_sentiment | 用户评价分析 | 评论区情感分析 |
| 工具：write_strategy | 策略输出 | 写入策略文件 |
| ReAct 规划 | 分析 -> 策略 -> 内容 -> 审核 | `create_react_agent` |
| 记忆 | 多轮对话上下文 | `MemorySaver` |
| Reflection | 策略质量自检 | Evaluator-Optimizer 循环 |

### 上机任务（6 个 TODO，见 starter.ipynb）

1. **TODO1**：用 `@tool` 定义三个真实工具（ROI计算器、情感分析器、策略写入器）
2. **TODO2**：用 LangGraph 的 `create_react_agent` 构建 ReAct Agent
3. **TODO3**：运行 Agent 处理营销任务，观察 Thought-Action-Observation 循环
4. **TODO4**：用 `MemorySaver` 添加短期记忆，实现多轮对话
5. **TODO5**：实现 Reflection（评估者-优化者）循环，自检并改进策略
6. **TODO6（可选）**：实现 Plan-Execute 模式，对比与 ReAct 的差异

---

## 2026 前沿补充：MCP（Model Context Protocol）

> v5.0 新增前沿点。你的 v4.0 教材在 Agent 工具调用上只讲"自己定义 @tool 函数"。2024 年底 Anthropic 发布 **MCP（Model Context Protocol）**，2025-2026 年成为 Agent 互操作的事实标准。

**MCP 是什么**：一个开放协议，标准化了"AI 应用如何从外部获取上下文和调用工具"。类似于 USB-C 之于硬件--MCP 让任何 AI 应用（MCP Host/Client）能连接任何工具服务器（MCP Server），无需为每个工具写定制集成。

**MCP 架构**：
- **MCP Host**：AI 应用（如 Claude Desktop、VS Code），管理多个 MCP Client
- **MCP Client**：维护与一个 MCP Server 的连接
- **MCP Server**：提供 Tools（可执行函数）、Resources（数据源）、Prompts（交互模板）

**为什么对营销 Agent 重要**：如果你的营销 Agent 需要调用 CRM、广告平台 API、数据分析工具，不用为每个 API 写定制集成--只需接入对应的 MCP Server。2026 年已有 Salesforce CRM、Google Drive、Slack、PostgreSQL 等数百个 MCP Server 可用。

**与本 Day 的关系**：本 Day 的 `@tool` 是"应用内工具"（tool 与 agent 在同一进程内）。MCP 是"进程外工具"（tool 由独立 Server 提供，通过 JSON-RPC 协议通信）。生产级 Agent 系统通常混合使用：简单工具用 `@tool`，企业系统集成用 MCP。

> 🔗 深入阅读见 [`reading.md`](./reading.md) 的 MCP 条目。

---

## 与后续 Day 的衔接

- **Day 2**：LangGraph 编排实战--今天是 `create_react_agent`（预构建），Day 2 是用 `StateGraph` 自定义 Agent 图
- **Day 3**：多 Agent 协作系统--今天是单 Agent，Day 3 是多 Agent 编排（Supervisor/Hierarchical）
- **Day 4**：Agent 评估与可观测性--今天关注架构，Day 4 关注如何评估和监控 Agent 质量
- **Day 5**：Agent 生产化部署--今天在笔记本里跑，Day 5 部署到生产（LangGraph Platform/自托管）

---

## 作业与评估

作业、5 分制量表、费曼演练、2 分钟话术、复盘自诊表--沿用独立教材 § Day 1 既有设计（v3.1 以来未变，质量已验证）。本学习材料包不重复，仅新增上机交付物：

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6 个 TODO 全部填好，能跑通）
- [ ] 一段 300 字分析：你的 ReAct Agent 在处理营销任务时，选择工具的顺序是否符合预期？为什么？
- [ ] （可选）用 Reflection 循环改进一次策略输出，记录评估者指出的 1 个问题

---

*本讲义由 v5.0 学习材料包升级生成。理论部分引用独立教材，上机部分用真实库 + TODO 脚手架。*
*最后更新：2026-07-24*

---

## 学习科学层 (v6.0)

本单元采用刻意练习(Ericsson)/间隔重复(FSRS-6,SM-2)/建构对齐(Biggs ILO↔TLA↔AT)/牛津tutorial LLM仿真(Socratic,Hattie四级反馈)。mastery 阈值与 Worked-Faded 示例见 practice.md 与 alignment.md。交叉练习(interleaving)促进迁移, 提取练习(retrieval practice)优于重读。

**v6.0 新增文件** (Day 1 学习科学层, 不破坏 v5.0 基线):
- `practice.md` - 刻意练习 (3 子技能 S1工具契约/S2 ReAct编排/S3架构选型 + 4 drill + Worked-Faded 三阶段 + interleaving A1B1C1... + weak_loop + retry_policy)
- `schedule.json` - FSRS-6 间隔重复 (6 卡片覆盖 ReAct/Plan-Execute/Reflection/Tool Calling/Memory/Anthropic五模式/MCP)
- `alignment.md` - Biggs 建构对齐 (5 ILO ↔ TLA ↔ AT 矩阵 + mastery >=80% + Feed Up/Back/Forward 三自检)
- `tutorial.ipynb` - 牛津 Tutorial LLM 仿真 (persona 禁直接答案 + 静态 if/else Socratic loop 6轮 + student_model.json + Hattie [TASK]/[PROCESS]/[SELF-REG]/[FEED-FORWARD] 四级反馈 + 每日1次限频)

**领域锚定** (非通用模板): 所有 drill 的 feedback_rule 引用本单元真实库 (LangChain `@tool` / LangGraph `create_react_agent` / `MemorySaver(thread_id=...)` / Anthropic 五模式 / MCP JSON-RPC), 所有 AT 引用 `starter.ipynb`/`solution.ipynb` 的具体 TODO 编号。

---

## 研究产出与产业链接层 (v7.0)

本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+arXiv链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。详见 research.md 与 industry.md。

**v7.0 领域锚定** (非通用模板):
- research.md 的 research_question 锚定本单元真实营销任务 (ROI=806.1% / 情感得分=2 / 6 TODO), linked_paper 引用 reading.md 已记录的真实 arXiv 链接 (ReAct 2210.03629 / Self-Refine 2303.17651), imrad_outline 引用 `starter.ipynb` 真实方法与 `solution.ipynb` 真实结果, reproducibility_checklist 引用 `data/README.md` 真实库版本与 model id。
- industry.md 的 real_companies 从公司库挑 (LangChain/Sierra/Cognition/Anthropic/OpenAI, 全部真实), deployment_example 锚定 LangGraph Platform + MemorySaver + MCP 生产部署, consulting_project partner = Sephora (公司库零售/CPG 候选), case_study protagonist = Sephora Head of AI, guest_lecture speaker = LangChain 创始团队, internship_pointer = OpenAI/Anthropic Residency + LangChain Capstone。
- 与 v5.0/v6.0 衔接: research.md IMRaD Methods 引用 `starter.ipynb` TODO1-6, industry.md consulting_project 引用 practice.md 刻意练习子技能, case_study 引用 alignment.md ILO 矩阵, guest_lecture 引用 reading.md 深链。
