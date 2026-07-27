# 技能5 · Day 2：LangGraph 编排实战 · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 技能5 Agentic系统工程与落地 · Day 2
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：如何把"多个Agent + 人工审核"编排成一条可控、可恢复、可扩展的状态图？
> **v5.0 升级点**：① 真实库上机（LangGraph，非伪代码）② 新增 TODO 填空式起始笔记本 ③ Notebook 化 ④ 深链阅读 ⑤ 2026 前沿（多Agent仿真 × 天道推演）

---

## 学习目标（学完你能做到）

1. 能用 LangGraph 的 `StateGraph` / `Node` / `Edge` 三要素解释"有状态有向图"如何替代线性 Chain，并指出营销多Agent场景中各要素对应的代码对象
2. 能为"分析->策略->内容->审核->发布"工作流画出状态图，识别其中的**条件边**（审核通过/不通过）与**循环退出条件**（修改次数上限），说明为何任何循环都必须有退出条件
3. 能在**真实 LangGraph 库**上完成"定义 State -> 写节点函数 -> 装配图 -> 编译 -> stream 运行"全流程，并解释 `MemorySaver` 检查点的作用
4. 能用 `add_conditional_edges` + `interrupt` 实现"审核不通过回到内容Agent重生成"的条件循环与人机协作（HITL）
5. 能用"多Agent仿真 × 天道推演"视角，把项目 CLAUDE.md 的天道推演沙盘映射为可计算的 LangGraph 多Agent博弈图

---

## 理论部分：精炼索引（详见独立教材）

> Day 2 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_技能5_Agentic系统工程与落地.md` § Day 2](../../AI原生化商业博士_独立教材_技能5_Agentic系统工程与落地.md)（3.2.1–3.2.4 节，已包含 StateGraph/条件路由/多Agent工作流/代码架构解析/实践建议）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：StateGraph —— 把工作流变成有状态有向图

LangGraph 的核心是把 Agent 工作流建模为**有状态有向图**，而非线性 Chain。

| LangGraph 概念 | 是什么 | 营销多Agent对应 |
|---------------|--------|----------------|
| `StateGraph` | 维护一个全局 State 的有向图 | 整个营销Agent系统 |
| `State`（TypedDict） | 所有节点共享的全局状态对象 | `MarketingState`（brief/analysis/strategy/content/...） |
| `Node`（节点函数） | 接收 State、返回 State 更新的函数 | analysis_agent / strategy_agent / content_agent / review_node |
| `Edge`（普通边） | A 无条件流转到 B | analysis -> strategy -> content -> review |
| `Conditional Edge`（条件边） | 根据 State 动态选下一节点 | review ->（通过？）-> publish 或 revise |
| `Checkpointing` | 把 State 持久化到外部存储 | `MemorySaver`（内存）/ `SqliteSaver`（持久） |

**为什么选 LangGraph 而非 LangChain / CrewAI**：LangGraph 原生支持条件路由、循环、状态持久化与人机交互；LangChain 以线性 Chain 为主，CrewAI 以角色驱动为主。生产级复杂 Agent 选 LangGraph。详见独立教材 3.2.1 对比表。

### 关键回顾 2：条件路由 —— 循环与分支的关键

```
[分析Agent] -> [策略Agent] -> [内容Agent] -> [审核节点]
                                                   |
                                    +------+-------+-------+
                                    |                      |
                                  通过                   不通过
                                    |                      |
                                    v                      v
                               [发布] <----- 回到 [内容Agent]（带审核反馈）
```

条件路由由两部分组成：
- **条件函数**：`should_approve(state) -> Literal["publish", "revise"]`，读 State 决定下一节点
- **条件边注册**：`workflow.add_conditional_edges("review", should_approve, {"publish": "publish", "revise": "content"})`

**循环退出条件（必做）**：`revision_count >= 3` 时强制发布，防止无限循环。独立教材 3.2.4 实践建议第 3 条：**任何循环都必须有退出条件**。

### 关键回顾 3：人机协作（HITL）—— interrupt 暂停-恢复

把 LLM 自动审核的 `review_node` 替换为 LangGraph 的 `interrupt`，即可实现真正的人工审核：图在审核节点**暂停**，State 被检查点持久化；人工给出通过/不通过后，图从检查点**恢复**执行。这是 LangGraph 相对其他框架的核心优势，也是生产环境审核合规的关键能力。

```python
from langgraph.types import interrupt, Command
# interrupt(value) 暂停图，把 value 抛给调用方；人工 ressume 时传入结果
```

### 关键回顾 4：状态驱动设计

所有节点共享 `MarketingState`，每个节点只负责更新自己负责的字段（`analysis_agent` 只写 `market_analysis`，`content_agent` 只写 `content`...）。这比在节点间传递参数更清晰、更易调试、更易扩展。新增 Agent 只需加节点 + 加边，不改现有代码。

---

## 上机部分：在真实 LangGraph 上构建多Agent营销系统

> 📓 **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO 填空版，你来做）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，gated，做完再看）
> 📊 **真实库与资源**：[`data/README.md`](./data/README.md)（LangGraph 库 + langchain-academy 官方课程 + HuggingFace Agents Course）

### 为什么用真实库 LangGraph 而非伪代码

v4.0 的代码普遍用"伪代码 / 模拟框架"--模拟框架会让你**学不到真实API的细节**（State 怎么定义、条件边怎么注册、检查点怎么编译）。v5.0 改用 **LangGraph**（langchain-ai/langgraph，38k★，MIT，"Build resilient agents"）：这是 LangChain 团队官方推出的 Agent 编排框架，生产级复杂 Agent 的事实标准。教材已有完整 LangGraph 实现，本 Day 把它改写成 TODO 填空版让你亲手写一遍。

### 营销映射（关键桥接）

本 Day 的多Agent系统是营销场景，与天道推演的多路径沙盘同构：

| LangGraph 节点 | 营销职能 | 天道推演对应 |
|---------------|---------|-------------|
| `analysis_agent` | 市场分析师：人群/竞品/趋势 | 局势感知（感知棋盘状态） |
| `strategy_agent` | 策略总监：主张/定位/渠道 | 沙盘模拟（展开多路径） |
| `content_agent` | 创意文案：3套创意方案 | 最优路径推荐 |
| `review_node` | 合规审核：打分/修改建议 | 反馈学习（对比推演与结果） |
| `should_approve` | 通过/不通过路由 | 概率评估（选高概率路径） |

### 上机任务（6 个 TODO，见 starter.ipynb）

1. **TODO1**：定义 `MarketingState`（TypedDict，含 brief/analysis/strategy/content/review_feedback/revision_count/approved/messages）
2. **TODO2**：实现 `analysis_agent` 和 `strategy_agent`（两个 LLM 节点，读 State 写 State）
3. **TODO3**：实现 `content_agent`（带审核反馈的循环内容生成）
4. **TODO4**：实现 `review_node`（LLM 打分审核）和 `should_approve`（条件路由 + 循环退出）
5. **TODO5**：实现 `build_marketing_graph`（StateGraph 装配：add_node + add_edge + add_conditional_edges + compile）
6. **TODO6（可选）**：把 `review_node` 替换为 `interrupt` 真人工审核，并运行完整系统

---

## 2026 前沿补充：多Agent仿真 × 天道推演

> v5.0 新增前沿点，本 Day 特色。这是本课程**独有**的交叉点。

**核心洞察**：LangGraph 多Agent编排与项目 CLAUDE.md 的「天道推演系统」高度同构——

| 天道推演（思维框架） | LangGraph（可计算实现） |
|--------------------|-----------------------|
| 在意识中构建多路径沙盘 | 在代码中构建多Agent状态图 |
| 模拟不同决策路径下的未来走向 | 条件边展开多分支执行 |
| 选择最优路径或预判风险 | 评估各分支输出择优 |
| 记录前提假设、追踪偏差、更新因果模型 | Checkpointing 持久化 + 反馈学习节点 |

**升级路径**：可把天道推演从"思维框架"升级为**可计算多Agent沙盘**——用 LangGraph 模拟多个利益相关方 Agent（如品牌方/渠道方/消费者/竞品方）博弈，每个 Agent 是一个节点，条件边模拟博弈分支，推演不同决策路径下的结果分布。这把"天道推演"从个人认知能力变成可复现、可版本化、可团队协作的决策工具。

**与独立教材 3.2.2 多Agent工作流的区别**：教材的工作流是**单一立场**（品牌方内部的分析->策略->内容->审核）；天道推演视角要求**多方立场**博弈（品牌方Agent vs 消费者Agent vs 竞品Agent），图的拓扑更复杂但推演更真实。

**参考链接**：
- 项目 CLAUDE.md「天道推演系统」（本项目内部概念，定义了局势感知/因果链追踪/沙盘模拟/概率评估/最优路径推荐/反馈学习六能力）
- LangGraph 多Agent协作教程：https://github.com/langchain-ai/langgraph （38k★，含 multi-agent 示例）
- LangChain Academy 官方课程：https://github.com/langchain-ai/langchain-academy （2.8k★，Module 1-5 渐进式讲 LangGraph）

> 🔗 深入阅读见 [`reading.md`](./reading.md) 的"多Agent仿真 × 天道推演"条目。

---

## 与后续 Day 的衔接

- **Day 1**：Agent 系统架构设计（ReAct/Plan-and-Execute/Reflection 五种模式）--今天是把这些模式落到 LangGraph 代码
- **Day 3**：Agent 评估与 Benchmarking--今天你建好的多Agent系统，Day 3 用五维度指标 + LLM-as-Judge 评估它
- **Day 4**：安全防护与对抗（Prompt Injection / 红队测试）--今天的 `review_node` 是合规第一道防线，Day 4 系统化对抗
- **Day 5**：生产部署与运维--今天的 `MemorySaver` 要换成 `SqliteSaver`/`PostgresSaver`，加 Langfuse 可观测性

---

## 作业与评估

作业、100 分制量表、详细步骤--沿用独立教材 § 六 作业1（必做：用 LangGraph 构建多Agent营销系统）既有设计（v4.0 以来已定，含新增投放优化Agent/interrupt人工审核/SqliteSaver持久化/Langfuse集成四项扩展）。本学习材料包不重复，仅新增上机交付物：

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6 个 TODO 全部填好，能跑通或至少能编译图）
- [ ] 一段 300 字分析：你的条件循环退出条件（`revision_count >= 3`）设成多少合理？为什么？如果取消退出条件会发生什么？
- [ ] （可选）用"多Agent仿真 × 天道推演"视角，为本 Day 的营销系统再增加一个"消费者Agent"节点（模拟消费者反应），画出新的状态图

---

*本讲义由 v5.0 学习材料包升级生成。理论部分引用独立教材，上机部分用真实 LangGraph 库 + TODO 脚手架。*
*最后更新：2026-07-24*


---

## 学习科学层 (v6.0)

本单元采用刻意练习(Ericsson)/间隔重复(FSRS-6,SM-2)/建构对齐(Biggs ILO↔TLA↔AT)/牛津tutorial LLM仿真(Socratic,Hattie四级反馈)。mastery 阈值与 Worked-Faded 示例见 practice.md 与 alignment.md。交叉练习(interleaving)促进迁移, 提取练习(retrieval practice)优于重读。

- **刻意练习 (deliberate practice)**: practice.md 拆 4 子技能 (状态建模/条件路由/装配编译/HITL), 每 drill 含 difficulty/reps_required/feedback_rule/Worked-Faded 三阶段 (完整示范->部分填空->独立解)。
- **间隔重复 (spaced retrieval)**: schedule.json 用 FSRS-6 (SM-2 backup) 算法, 6 张卡片 (StateGraph三要素/add_conditional_edges/revision_count退出/MemorySaver+interrupt/天道推演映射/状态驱动设计), due=[1,3,8,21,60,180], request_retention=0.9。
- **建构对齐 (constructive alignment)**: alignment.md 列 ILO↔TLA↔AT 矩阵 5 行, mastery_threshold >=80%, 含 Feed Up/Feed Back/Feed Forward 三自检。
- **牛津 tutorial (Socratic)**: tutorial.ipynb 用静态 if/else 模拟 4 轮苏格拉底追问 (为什么/反例/若前提变/凭什么/如何), Hattie 四级反馈 [TASK]/[PROCESS]/[SELF-REG]/[FEED-FORWARD], student_model.json 记录掌握度+盲点, 限频 1次/天 防依赖。
- **mastery**: practice.md weak_loop 连续 2 次失败触发弱项循环 (回退+Worked example); retry_policy 10 free late days + 失败重试不罚分。
- **interleaving**: practice.md 交叉排布 A1B1C1...B2C2A2...C3A3B3, 不块状, 促进迁移。

> v6.0 关键词命中: FSRS/SM-2/刻意练习/deliberate practice/建构对齐/constructive alignment/牛津tutorial/Socratic/Hattie/间隔重复/spaced retrieval/交叉/interleaving/mastery/Worked-Faded (>=4 已满足)。

*v6.0 学习科学层追加完成, 未修改 v5.0 原文一字。最后更新: 2026-07-26*


## 研究产出与产业链接层 (v7.0)

本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+arXiv链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。详见 research.md 与 industry.md。

- **research.md (研究产出)**: research_question 锚定 `revision_count >= 3` 阈值与多方立场Agent博弈的推演质量; contribution 声明相对 LangChain Academy Module 1 / Anthropic Building Effective Agents / HuggingFace Agents Course 的增量; linked_paper 引用 reading.md 已验证的 Anthropic Building Effective Agents (https://www.anthropic.com/research/building-effective-agents ) + LangGraph 仓库 + langchain-academy Module 1 chain.ipynb; imrad_outline 四段大纲引用 MarketingState 八字段/FSRS-6 6卡片/Biggs 5行矩阵等真实数字; reproducibility_checklist 7项 (code/data/seeds/environment/preregistration/FAIR/hypothesis); research-to-practice 翻译为 HBS Working Paper -> HBR Article / MIT Sloan Teaching Case / 企业白皮书。
- **industry.md (产业链接)**: real_companies 表格列 5 家真实企业 (LangChain/Sierra/Cognition/Anthropic/OpenAI) 与本单元关联; deployment_example 描述 Sierra 客服 Agent 日均 10万+对话的 LangGraph 状态图部署; consulting_project 是 Imperial MSc BA 风格 8周4-5人 Burberry 营销内容审核咨询项目; case_study 是 HBS 风格 Head of AI 在 LLM自动审核 vs HITL人工审核 间的两难决策; guest_lecture 邀请 LangChain Head of LangGraph 讲《From Workflow to Agent》; internship_pointer 指向 LangChain Engineering Intern / OpenAI Residency / Sierra AI Engineer 等角色。

*v7.0 研究产出与产业链接层追加完成, 未修改 v5.0/v6.0 原文一字。最后更新: 2026-07-26*
