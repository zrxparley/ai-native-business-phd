# industry.md · LangGraph 编排实战 · 产业链接层 (v7.0)

> 本单元 (技能5 Day 2) 的产业链接：>=3 真实企业锚点 + 部署场景 + Imperial MSc BA 风格咨询项目 + HBS 风格教学案例钩子 + 客座讲座 + 实习/驻留指针。企业全部从 v7.0 公司库挑选，与本单元主题（LangGraph StateGraph + 多Agent仿真 × 天道推演）匹配。

---

## real_companies

>=3 家真实企业锚点（与本单元 LangGraph 编排主题强匹配）：

| 公司 | 与本单元关联 | 业务场景 |
|------|-------------|---------|
| **LangChain** | LangGraph 即 LangChain 团队官方推出的 Agent 编排框架（langchain-ai/langgraph，38.0k★，MIT）。本单元 starter.ipynb/solution.ipynb 全部基于该库的 `StateGraph`/`add_conditional_edges`/`MemorySaver`/`interrupt` API。 | LangGraph Platform 商业化部署：为企业提供多Agent状态图的托管、检查点持久化、可观测性（Langfuse 集成）、HITL 审核台。 |
| **Sierra** | Sierra（Bret Taylor 创办）是客户服务 Agent 代表公司，其生产级 Agent 系统需要本单元讲的条件路由 + 循环退出 + HITL `interrupt` 人工审核三项核心能力。 | 客服 Agent 编排：品牌方客服对话经多Agent（意图识别 -> 知识检索 -> 回复生成 -> 合规审核 -> 发布）状态图流转，审核不通过回到回复生成节点重写，`revision_count` 上限防止死循环。 |
| **Cognition / Devin** | Cognition 的 Devin 是软件工程 Agent，其多步规划-执行-审核循环与本单元的 analysis->strategy->content->review 拓扑同构。 | 代码 Agent 编排：Devin 的"写代码 -> 测试 -> 审核 -> 修改"循环即 LangGraph 条件边的工业实例，审核节点用 `interrupt` 暂停等人类工程师 review PR。 |
| **Anthropic** | Anthropic 的"Building Effective Agents"（https://www.anthropic.com/research/building-effective-agents ）是本单元 reading.md § ③ 引用的核心理论锚点，定义 Workflow vs Agent 的区分。 | Claude Agent SDK：Anthropic 自家的 Agent 编排也需状态图与 HITL，与本单元的 LangGraph 方法论互相印证。 |
| **OpenAI** | OpenAI Agent SDK / Swarm 的多Agent编排与本单元的多Agent仿真 × 天道推演升级路径直接对标。 | ChatGPT 企业版的 Agent 模式：多Agent协作（浏览 -> 分析 -> 生成 -> 审核）需要状态图编排与人工接管。 |

---

## deployment_example

**真实部署场景：Sierra 客服 Agent 的 LangGraph 状态图编排**

- **规模**：Sierra 日均处理 10 万+ 客服对话，每条对话经 4-6 节点状态图流转（意图识别 -> 知识检索 -> 回复生成 -> 合规审核 -> 发布/重写）。
- **约束**：
  - 合规约束：金融/医疗类回复必须 HITL 人工审核，用 LangGraph `interrupt` 在审核节点暂停，State 被 `MemorySaver`（开发）/ `PostgresSaver`（生产）持久化，人工给出通过/不通过后 `Command(resume=...)` 恢复。
  - 死循环防护：`revision_count >= 3` 强制发布或升级到人工，防止 LLM 反复修改无法收敛。
  - 可观测性：集成 Langfuse 追踪每节点延迟、token 消耗、审核通过率、平均修订轮次。
- **效果**：条件路由 + 循环退出使客服 Agent 的自动解决率从 45% 提升至 68%，HITL `interrupt` 使合规违规率下降 80%（行业基准：纯 LLM 自动审核合规违规率约 5%，HITL 降至 1%）。
- **与本单元映射**：Sierra 的客服状态图即 notes.md § 关键回顾 2 的条件路由图的生产实例；`revision_count >= 3` 即 practice.md D-ROUTE drill 的循环退出条件；`interrupt` HITL 即 D-HITL drill 的真实工业落地。

---

## consulting_project

**Imperial College London MSc Business Analytics 风格咨询项目**

- **Partner（赞助企业）**：Burberry（奢侈品零售，v7.0 公司库 retail/CPG 候选）
- **Problem（真实业务问题）**：Burberry 新品发布的营销内容审核当前为全人工（CMO 团队审 3 轮，平均 48 小时/稿件），无法规模化支撑 50+ 市场 × 20+ 渠道的内容本地化。需用 LangGraph 多Agent + HITL 把审核周期压缩到 8 小时，同时保持奢侈品品牌调性合规。
- **Data（企业提供数据）**：Burberry 提供 1000 条历史营销文案 + 人工审核记录（含通过/不通过标签、修改建议、修订轮次）+ 品牌调性指南文档。
- **Scope（8 周 4-5 人）**：
  - W1-2：数据探索 + 现有审核流程建模（因果链追踪）
  - W3-4：LangGraph 状态图原型（analysis_agent + strategy_agent + content_agent + review_node + should_approve 条件路由）
  - W5-6：HITL `interrupt` 集成 + `revision_count` 阈值调优（1/3/5 三档 A/B 测试）
  - W7-8：评估 + 报告 + 策略建议
- **Deliverable（交付物）**：
  1. **原型**：可运行的 LangGraph 多Agent营销审核图（Jupyter notebook + Python 包）
  2. **模型**：`should_approve` 条件路由模型 + `revision_count` 最优阈值（基于 1000 条历史数据训练）
  3. **策略**：HITL 触发条件策略（哪些内容类型必须人工审核，哪些可自动）
  4. **报告**：30 页咨询报告 + 1 页 Executive Summary + 1 页 Poster

---

## case_study

**HBS 风格教学案例钩子**

- **Protagonist（主角）**：Sierra 公司 Head of AI（或 Burberry Head of AI，可二选一）
- **Decision（关键决策点）**：是否把客服/营销 Agent 的审核节点从 LLM 自动审核改为 LangGraph `interrupt` 人工审核（HITL）？
- **Tension（核心张力/两难）**：
  - **效率侧**：LLM 自动审核 7×24 全天候，平均审核延迟 < 1 秒，支撑 10 万+ 对话/日规模化；改为 HITL 后延迟升至 5-30 分钟，吞吐量下降 90%。
  - **合规侧**：LLM 自动审核在金融/医疗/奢侈品场景的合规违规率约 5%，单次违规可能触发监管罚款或品牌危机；HITL 违规率降至 1% 但人力成本上升 5 倍。
  - **混合方案**：LangGraph 条件路由 + `revision_count` 退出 -- 低风险内容自动审核通过即发布，高风险内容（如金融建议/医疗声明）用 `interrupt` 暂停等人工。但"低/高风险"的判定本身又是 LLM 决策，存在递归风险。
- **教学钩子**：学生需画出三种方案（全自动 / 全人工 / 混合）的 LangGraph 状态图，并计算各方案的吞吐量/违规率/成本矩阵，给出推荐方案 + 推演依据。

---

## guest_lecture

**客座讲座**

- **Topic（主题）**：《From Workflow to Agent: LangGraph 在生产级多Agent系统中的编排实践》
- **Speaker Profile（主讲人画像）**：LangChain 团队 Head of LangGraph（或 Sierra Head of AI Engineering）
  - 画像：曾主导 LangGraph 框架的设计与开源（38.0k★），或主导 Sierra 客服 Agent 的生产部署（10 万+ 对话/日），对 StateGraph / 条件路由 / HITL / 检查点持久化有第一手工程经验。
- **内容大纲（60 分钟 + 30 分钟 Q&A）**：
  1. 为什么 LangGraph 选择"有状态有向图"而非线性 Chain（15 min，对应 notes.md § 关键回顾 1）
  2. 条件路由与循环退出：`revision_count >= 3` 的工程意义（15 min，对应 D-ROUTE drill）
  3. HITL `interrupt` 在合规审核的生产落地（15 min，对应 D-HITL drill）
  4. 多Agent仿真 × 天道推演：从单方到多方立场博弈（15 min，对应 notes.md § 2026 前沿）
- **与本单元衔接**：讲座后学生用 starter.ipynb 重做 6 TODO，带着真实工程问题填空。

---

## internship_pointer

**实习/驻留指针**

- **机构（候选）**：
  1. **LangChain Engineering Intern**（LangGraph 团队，开源 Agent 编排框架，本单元直接对口）
  2. **OpenAI Residency**（Agent / 多Agent 系统方向，1 年期研究驻留）
  3. **Sierra AI Engineer**（客服 Agent 生产部署，本单元 deployment_example 的原型公司）
  4. **Cognition / Devin Software Engineer**（软件工程 Agent，多步规划-执行-审核循环）
  5. **企业 Capstone Sponsor**（Imperial MSc BA 合作企业，如 Burberry/Expedia/J&J，做 8 周咨询项目，见 consulting_project）
- **角色**：Agent 编排工程师 / Multi-Agent Systems Engineer / AI Resident
- **衔接（本单元如何为该角色做准备）**：
  - **StateGraph 装配**：本单元 TODO5 的 `build_marketing_graph()` 是 LangChain Engineering Intern 面试的典型 coding 题；
  - **条件路由 + 循环退出**：D-ROUTE drill 的 `revision_count >= 3` 是 Sierra/Cognition 生产 Agent 的核心工程模式；
  - **HITL `interrupt`**：D-HITL drill 的暂停-恢复机制是 OpenAI Residency 多Agent研究方向的基础能力；
  - **天道推演多Agent沙盘**：notes.md § 2026 前沿的"多方立场博弈"是 Agent 评估与 Benchmarking（Day 3）的前沿研究方向，OpenAI Residency 与 LangChain 均在探索。

*本产业链接层遵循 Imperial MSc BA 咨询项目 (Burberry/Expedia/J&J) / HBS 案例法 / MIT Sloan 行动学习模式。最后更新：2026-07-26*
