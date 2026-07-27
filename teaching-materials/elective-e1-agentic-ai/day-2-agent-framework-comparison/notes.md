# 选修E1 · Day 2：Agent框架对比 · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 选修E1 Agentic AI · Day 2
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：同一个营销Agent，用不同框架实现，差异在哪里？如何为营销场景选型？
> **v5.0 升级点**：① 真实库上机（LangGraph实跑ReAct vs Plan-Execute双模式）② TODO填空式起始笔记本 ③ 独立.ipynb ④ 深链阅读 ⑤ 2026前沿（LangGraph/CrewAI/AutoGen/MetaGPT四框架对比 + A2A/MCP协议生态 + 多Agent仿真）

---

## 学习目标（学完你能做到）

1. 能解释四大Agent框架（LangGraph/CrewAI/AutoGen/MetaGPT）的设计哲学差异--Agent即图、Agent即角色、Agent即对话者、Agent即流程执行者，并在营销场景中准确选型
2. 能用LangGraph的`StateGraph`显式定义Agent工作流图（节点+边+条件分支），并用`create_react_agent`构建ReAct模式Agent，在真实营销任务上运行
3. 能用LangGraph实现Plan-Execute模式（plan_node + execute_node + 条件边），并与ReAct模式在同一个营销任务上对比步数、调用次数和输出质量
4. 能读写CrewAI的Agent/Task/Crew API结构（角色化协作模式），即便未安装也能通过静态API分析理解其设计哲学与适用场景
5. 能读写AutoGen的ConversableAgent/GroupChat API结构（对话驱动模式），理解多Agent讨论与协商的适用边界
6. 能用天道推演框架分析"同一营销任务、不同框架实现"的因果链差异，识别各框架在营销Agent场景下的高杠杆点和不可逆节点

---

## 理论部分：精炼索引（详见独立教材）

> Day 2 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_选修E1_Agentic_AI.md` § Day 2](../../AI原生化商业博士_独立教材_选修E1_Agentic_AI.md)（一至三节，已包含四框架设计哲学/双框架实现/AutoGen与MetaGPT适用场景）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：四框架设计哲学对比

| 维度 | LangGraph | CrewAI | AutoGen | MetaGPT |
|------|-----------|--------|---------|---------|
| **设计哲学** | Agent是状态图 | Agent是角色化的Crew成员 | Agent是多轮对话参与者 | Agent是软件工程流程中的角色 |
| **核心抽象** | StateGraph（有状态有向图） | Crew + Agent + Task | ConversableAgent + GroupChat | Role + Protocol + Environment |
| **控制流** | 开发者显式定义图结构 | 框架根据Task分配自动编排 | 通过对话消息驱动 | 预定义SOP（标准操作流程） |
| **灵活性** | 极高（完全控制） | 中高（角色+任务定义） | 中（对话驱动） | 中低（SOP固定） |
| **学习曲线** | 陡峭 | 平缓 | 中等 | 中等 |
| **适用场景** | 复杂工作流、精确控制 | 角色明确的团队协作 | 需要Agent间讨论和协商 | 模拟软件团队开发流程 |
| **维护方** | LangChain公司 | CrewAI公司 | 微软 | DeepWisdom |

**核心洞见**：四个框架解决同一类问题（如何构建Agent系统），但设计哲学截然不同。选型不是"哪个最好"，而是"哪个最匹配你的任务结构"。

### 关键回顾 2：LangGraph -- Agent即图

LangGraph的核心洞见是：Agent系统的复杂性来自于状态管理和流程控制，而有向图是表达复杂流程的最佳数据结构。开发者将Agent工作流建模为StateGraph，每个节点是一个处理函数，每条边定义了流转规则。

- **优势**：精确控制每一步、支持条件分支和循环、状态持久化、Human-in-the-loop原生支持、原生fan-out/fan-in并行
- **劣势**：需要开发者预先设计整个流程图，对于真正需要Agent自主规划的场景不够灵活
- **核心API**：`StateGraph`（自定义图）、`create_react_agent`（预构建ReAct）、`MemorySaver`（会话持久化）、`add_conditional_edges`（条件分支）

### 关键回顾 3：CrewAI -- Agent即角色

CrewAI的核心洞见是：复杂任务可以通过"角色分工+任务分配"来分解。开发者定义一组Agent（每个有role/goal/backstory）和一组Task（每个有description/expected_output/agent），CrewAI自动编排执行顺序。

- **优势**：直觉性的角色化设计、代码简洁、适合"团队协作"模式的任务
- **劣势**：对执行流程的控制力较弱，Agent间的交互模式较为固定
- **核心API**：`Agent(role, goal, backstory, tools, llm)`、`Task(description, expected_output, agent, context)`、`Crew(agents, tasks, process)`、`crew.kickoff(inputs)`

### 关键回顾 4：AutoGen -- Agent即对话者

AutoGen的核心洞见是：多Agent协作本质上是对话。每个Agent是一个ConversableAgent，通过GroupChat机制在同一个对话中交互。

- **优势**：灵活的Agent间通信、支持Agent间的讨论和协商、对话历史自然记录
- **劣势**：对话驱动可能导致执行效率低（Agent间可能无限讨论）、难以精确控制执行顺序
- **核心API**：`ConversableAgent(name, system_message)`、`GroupChat(agents, messages, max_round)`、`GroupChatManager(group_chat)`、`agent.initiate_chat(manager, message)`

### 关键回顾 5：MetaGPT -- Agent即流程执行者

MetaGPT预定义了软件开发的标准流程（产品经理 -> 架构师 -> 工程师 -> QA），每个Agent在流程中扮演特定角色，遵循特定的输入输出协议。

- **优势**：结构化程度高、输出质量稳定、适合流程明确的领域
- **劣势**：SOP是预定义的，灵活性有限，不适合需要动态规划的场景

---

## 上机部分：用真实库对比Agent框架

> 📓 **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO填空版，你来做）| [`solution.ipynb`](./solution.ipynb)（参考答案，做完再看）
> 📦 **真实库说明**：[`data/README.md`](./data/README.md)（LangGraph真实库 + CrewAI/AutoGen静态分析 + 真实营销数据）

### 为什么用真实库而非模拟代码

v4.0的代码用"伪代码+模拟输出"。v5.0改用 **LangGraph 真实库**：`create_react_agent`和`StateGraph`是生产级API，可直接用于生产。CrewAI/AutoGen因环境未安装，采用"静态API结构对比+设计哲学分析"模式，代码结构真实反映各框架API设计。

### 营销映射（关键桥接）

同一个营销任务（透肌精华竞品分析+策略生成）用不同框架实现：

| 框架 | 营销任务映射 | 本Day实现方式 |
|------|-------------|--------------|
| LangGraph ReAct | 边推理边调用工具（搜索产品->分析竞品->写策略） | `create_react_agent`真实运行 |
| LangGraph Plan-Execute | 先规划4步再顺序执行 | `StateGraph`真实运行 |
| CrewAI | 4个角色化Agent分工（调研员/分析师/策略师/撰写人） | 静态API结构对比 |
| AutoGen | 多Agent对话讨论营销方案 | 静态API结构对比 |

### 上机任务（6个TODO，见starter.ipynb）

1. **TODO1**：定义营销工具（search_product_info/analyze_competitor/write_strategy）和StubChatModel
2. **TODO2**：用`create_react_agent`构建LangGraph ReAct Agent，预编排工具调用轨迹
3. **TODO3**：用`StateGraph`构建LangGraph Plan-Execute Agent（plan_node + execute_node + 条件边）
4. **TODO4**：运行ReAct和Plan-Execute两种模式，对比步数/调用次数/输出质量
5. **TODO5**：用CrewAI API结构（Agent/Task/Crew）编写等价实现（含import guard），静态对比设计哲学
6. **TODO6**：用AutoGen API结构（ConversableAgent/GroupChat）编写等价实现，生成四框架对比表

---

## 天道推演视角：框架选型的因果链分析

天道推演框架可用于分析"同一任务、不同框架"的因果网络差异：

```
输入：营销任务（透肌精华竞品分析+策略） + 4个框架候选

推演：
  1. LangGraph ReAct路径：感知任务 -> Thought -> Action(工具) -> Obs -> 循环
     - 因果节点：每次Action改变Belief，影响下一次Thought
     - 不可逆点：write_strategy执行后文件已写入
     - 风险：循环不终止、工具选择错误
     - 适用：信息不足需探索的营销任务
  
  2. LangGraph Plan-Execute路径：感知任务 -> 一次性规划 -> 顺序执行
     - 因果节点：Plan阶段的错误会传播到所有后续Execute步骤
     - 不可逆点：Plan一旦确定，Execute阶段无法动态调整
     - 风险：前提假设错误导致整个计划失效
     - 适用：信息充分、流程结构化的营销任务
  
  3. CrewAI路径：角色分工 -> Task依赖编排 -> 各Agent执行
     - 因果节点：Task的context依赖决定执行顺序
     - 不可逆点：角色定义错误导致整个Crew输出偏差
     - 风险：角色边界模糊导致Task重复或遗漏
     - 适用：角色明确、可清晰分工的营销团队协作
  
  4. AutoGen路径：多Agent对话 -> 讨论协商 -> 决策者汇总
     - 因果节点：每轮对话改变其他Agent的认知
     - 不可逆点：max_round耗尽仍未达成共识
     - 风险：Agent间无限讨论、收敛困难
     - 适用：需要多视角辩论的营销策略制定

输出：
  ├── 路径诊断：营销竞品分析（结构化任务）-> Plan-Execute或CrewAI更优
  ├── 策略建议：信息充分用Plan-Execute，需多视角用AutoGen，需精确控制用LangGraph
  └── 认知盲点：StubLLM无法真实模拟LLM的推理质量，真实LLM可能出现非预期工具选择
```

> 💡 **天道推演与框架选型的结合**：框架选型本质上是在构建不同的因果网络。LangGraph让你显式控制每个因果节点，CrewAI让你通过角色分工隐式编排因果链，AutoGen让因果链在对话中涌现。用天道推演的沙盘模拟方法，可以在部署前推演不同框架在同一营销任务上的行为路径差异。

---

## 2026前沿补充：Agent框架生态演进

> v5.0新增前沿点。本Day对比四大框架，2026年前沿已扩展到协议层和生态层：

**LangGraph生态成熟**：LangGraph从2024年的新兴框架发展为2026年Agent编排的事实标准之一。`create_react_agent`、`StateGraph`、`MemorySaver`构成Agent开发的"三件套"，与LangSmith（可观测性）、LangGraph Platform（部署）形成完整生产链路。

**A2A（Agent-to-Agent）协议**：Google于2025年提出A2A协议，定义Agent间互操作的开放标准。与MCP（Model Context Protocol，Anthropic提出的工具/上下文协议）互补：MCP解决Agent与工具的连接，A2A解决Agent与Agent的连接。2026年多Agent仿真和跨框架协作的核心基础设施。

**MCP（Model Context Protocol）普及**：Anthropic提出的MCP协议在2025-2026年快速普及，成为Agent连接外部工具和数据源的事实标准。LangGraph/CrewAI/AutoGen均逐步支持MCP，框架间的工具层正在标准化。

**多Agent仿真成为热点**：2024-2026年研究热点从单Agent转向多Agent协作仿真。Generative Agents（Stanford, arXiv 2304.03442）展示了Agent的长期记忆和计划修订，MetaGPT将SOP引入多Agent协作。多Agent仿真已成为模拟复杂商业场景的核心技术。

**Plan-Execute的复兴**：Plan-Execute模式在2025年因Plan-and-Solve论文和BabyAGI的实践重新受到关注。其"先规划后执行"的思路在结构化营销任务中表现优于ReAct的逐步探索。

> 🔗 深入阅读见 [`reading.md`](./reading.md)。

---

## 框架选择决策树（独立教材 § Day 2 三节）

1. 需要精确控制执行流程？-> LangGraph
2. 任务可以按角色分工？-> CrewAI
3. 需要Agent间讨论和辩论？-> AutoGen
4. 有标准化的SOP需要遵循？-> MetaGPT
5. 以上都不满足，需要混合方案？-> 以LangGraph为骨架，在关键节点嵌入CrewAI/AutoGen

---

## 与前后Day的衔接

- **Day 1**：Agent理论基础--ReAct/Plan-Execute范式（本Day用真实框架实现这两范式）
- **Day 3**：多Agent系统设计--本Day对比单Agent框架，Day 3进入多Agent协作（通信协议/共识机制/冲突解决）

---

## 作业与评估

作业、评分标准、费曼演练沿用独立教材 § Day 2 既有设计。本学习材料包新增上机交付物：

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6个TODO全部填好，能跑通）
- [ ] 一段300字分析：同一个营销任务，你会在LangGraph ReAct、LangGraph Plan-Execute、CrewAI、AutoGen中选哪个？用天道推演的因果链视角说明理由
- [ ] （可选）为本Day的营销任务设计一个混合方案（LangGraph骨架+CrewAI角色化节点），并说明为什么混合优于单一框架

---

*本讲义由v5.0学习材料包升级生成。理论部分引用独立教材，上机部分用真实库+TODO脚手架。*
*最后更新：2026-07-25*

## 学习科学层 (v6.0)
本单元采用刻意练习(Ericsson)/间隔重复(FSRS-6,SM-2)/建构对齐(Biggs ILO↔TLA↔AT)/牛津tutorial LLM仿真(Socratic,Hattie四级反馈)。mastery 阈值与 Worked-Faded 示例见 practice.md 与 alignment.md。交叉练习(interleaving)促进迁移, 提取练习(retrieval practice)优于重读。

## 研究产出与产业链接层 (v7.0)
本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+arXiv链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。本研究锚定同一营销竞品分析任务上LangGraph ReAct/Plan-Execute/CrewAI/AutoGen四框架控制对比, linked_paper引用Generative Agents(arXiv 2304.03442)与Plan-and-Solve(arXiv 2305.04091); 产业链接锚定LangChain/CrewAI/Microsoft/Sierra/Anthropic真实企业, 含Sephora部署场景与咨询项目。详见 research.md 与 industry.md。
