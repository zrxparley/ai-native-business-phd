# Day 1 Agent理论基础 · 产业链接层 (v7.0)

> **所属**: AI原生化商业博士 · 选修E1 Agentic AI · Day 1
> **版本**: v7.0 产业链接层 (industry linkage)
> **关联基线**: 本文件锚定 v5.0 notes.md (BDI/ReAct/Plan-Execute + LangGraph/LangChain/pydantic 真实库) + reading.md (Anthropic "Building Effective Agents" / ReAct / Generative Agents)

本文件给出本单元 Agent 理论基础在真实企业中的部署场景、Imperial MSc BA 风格咨询项目、HBS 风格教学案例、客座讲座与实习指针。企业均从公司库挑选, 真实存在, 与 Agent 理论主题匹配。

---

## real_companies

>=3 家真实企业锚点 (与本单元 ReAct/BDI/Plan-Execute/LangGraph 主题匹配):

| 公司 | 与本单元关联 | 业务场景 |
|------|-------------|---------|
| **LangChain** (LangGraph 母公司) | 本单元 `starter.ipynb` 直接使用 LangChain `@tool` 装饰器 + LangGraph `create_react_agent`/`StateGraph`/`MemorySaver` 三件套; `reading.md` 引用 LangGraph 文档 (38k 星 GitHub) | LangGraph Platform 提供 Agent 编排+部署+可观测性 (LangSmith), 2026 年已成为 Agent 编排事实标准之一。其 `create_react_agent` 即本单元 TODO3 核心API。 |
| **Anthropic** | `notes.md` 关键回顾 1 直接引用 Anthropic "Building Effective Agents" (2024-12-19), 定义 Workflow vs Agent 核心区分与自主性谱系 L0-L4; `reading.md` ① 已验证深链 | Anthropic Claude 支持 tool use (function calling), 其文章提出"能用 Workflow 解决的不要用 Agent"实践建议, 是本单元天道推演因果链分析的出发点。 |
| **Sierra** (Bret Taylor 创立的 Agent 平板) | 自主性谱系 L4 自主规划的产业代表; 客服 Agent 部署涵盖 BDI Belief (客户上下文) / Desire (解决工单) / Intention (执行步骤) | Sierra 在客户服务场景部署 ReAct 风格 Agent, 处理退款/订单查询/投诉等任务, 是 L3-L4 Agent 在企业生产环境的典型部署。 |
| **Salesforce Einstein** | 营销 Agent 产业代表; `notes.md` 营销映射表 (BDI Belief = 产品知识+市场认知) 直接对应 Einstein 营销云的 Agent 责任 | Salesforce 在 Einstein Marketing Cloud 部署营销 Agent, 自动生成受众细分/文案/A-B 测试, 对应本单元工具 `search_product_info`/`analyze_competitor`/`write_strategy` 的产业实现。 |
| **Cognition / Devin** (代码 Agent) | 自主性谱系 L4 + Plan-Execute 范式的产业代表; `notes.md` 2026 前沿节提到 BabyAGI 实践复兴 Plan-Execute | Devin 用 Plan-Execute 模式分解软件工程任务, 是 L4 Agent 自主规划在生产环境的典型, 对比本单元 TODO6 的 Plan-Execute 实现。 |

---

## deployment_example

**部署场景: Sierra 客服 Agent 的 ReAct 循环在生产中的应用**

Sierra (Bret Taylor 创立的 Agent 平台) 在客户服务场景部署 ReAct 风格 Agent, 处理电商退款/订单查询/投诉分类等任务。其部署形态对应本单元自主性谱系 L3 (受控循环):

- **规模**: 单 Agent 处理日均百万级客服工单, 覆盖多家 Fortune 500 零售品牌。
- **BDI 映射**: Belief = 客户订单历史 + 工单上下文 (CRS 检索); Desire = 解决工单 + 保持客户满意度; Intention = 多步执行计划 (查询订单 -> 判断退款资格 -> 执行退款 -> 通知客户)。
- **ReAct 循环**: 每步 Action 前有 Thought (推理), Action 后有 Observation (工具返回), 形成闭环。对应本单元 `starter.ipynb` TODO3-4 的 Thought-Action-Observation 轨迹。
- **约束**: (i) **不可逆操作护栏** -- 退款执行 (`write_strategy` 等价物) 前需人工 approval, 对应本单元天道推演"不可逆点"分析; (ii) **循环终止** -- 最大步数限制 (本单元 `notes.md` 天道推演节"循环不终止"风险); (iii) **工具选择错误** -- LLM 可能选错工具导致信息偏差, 需 LangSmith 可观测性监控。
- **效果**: 相比纯 Workflow (L1-L2), ReAct Agent 在开放工单上首次解决率 (FCR) 提升, 但单工单成本上升 -- 这正是 Anthropic "能用 Workflow 解决的不要用 Agent" 建议的边界: 信息充分的工单用 Workflow, 信息不足需探索的工单用 Agent。

**与本单元衔接**: 学员在 `solution.ipynb` 实现的 ReAct Agent 即 Sierra 部署形态的教学缩影; 天道推演因果链分析 (notes.md) 即 Sierra 部署前风险推演的方法论。

---

## consulting_project

**Imperial College MSc Business Analytics 风格咨询项目** (8 周, 4-5 人团队):

- **Partner (赞助企业)**: Salesforce Einstein Marketing Cloud (营销 Agent 平台)
- **Problem (真实业务问题)**: Einstein 营销云当前用 Workflow (L1-L2) 自动生成受众细分和文案, 但在**新品发布会策划**这类开放任务上 Workflow 失效。Partner 想评估: 在新品发布会策划任务上, 应升级到 ReAct (L3 受控循环) 还是 Plan-Execute (L4 自主规划)? 两种范式的成本-灵活性权衡如何量化?
- **Data (企业提供数据)**: (i) 脱敏的历史新品发布会策划任务 200 条 (含产品/竞品/目标受众/预算); (ii) Einstein 平台工具 API (产品搜索/竞品分析/策略生成); (iii) A/B 测试基础设施 (对比 ReAct vs Plan-Execute 的输出质量评分)。
- **Scope (范围)**: 8 周, 4-5 人 MSc BA 团队。Week 1-2: 文献综述 (ReAct arXiv 2210.03629 / Plan-and-Solve arXiv 2305.04091) + LangGraph 上手; Week 3-4: 在 Einstein 数据上实现 ReAct 与 Plan-Execute 两种 Agent (复用本单元 `starter.ipynb` 脚手架); Week 5-6: A/B 测试 + 天道推演 sandbox simulation 推演风险; Week 7-8: 撰写报告 + Partner 内部汇报。
- **Deliverable (交付物)**: (i) ReAct vs Plan-Execute 对比原型 (Python notebook, 可复现); (ii) 范式选择决策树 (基于任务信息充分度); (iii) 天道推演风险预警清单 (针对不可逆操作如策略发布); (iv) 30 页咨询报告 + Partner 内部 workshop。
- **衔接**: 本单元 `starter.ipynb` 6 个 TODO + `notes.md` 天道推演因果链分析 即该咨询项目的教学预演; Imperial MSc BA 的 Burberry/Expedia/J&J 咨询项目模式与本设计同构。

---

## case_study

**HBS 风格教学案例钩子**:

- **Protagonist (主角)**: Maya Chen, Head of AI at "GlowLab" (虚构美妆 DTC 品牌, 原型参考 Sephora/Stitch Fix), 直接向 CMO 汇报。
- **Decision (关键决策点)**: GlowLab 即将上线"夏季新品精华液发布会", CMO 要求 Maya 在 2 周内决定: 营销策划 Agent 应采用 **ReAct (L3 受控循环)** 还是 **Plan-Execute (L4 自主规划)**? 预算 50 万人民币, 失败成本高 (发布会不可逆)。
- **Tension (核心张力/两难)**:
  - **张力 1 (灵活性 vs 可控性)**: ReAct 每步可动态调整 (灵活), 但成本不可预测且可能循环不终止; Plan-Execute 一次性规划后顺序执行 (可控), 但 Plan 阶段错误会传播到所有后续步骤。
  - **张力 2 (信息充分度未知)**: 新品精华液的竞品情况在策划初期信息不足 (倾向 ReAct), 但发布会临近时信息逐渐充分 (倾向 Plan-Execute) -- 何时切换范式?
  - **张力 3 (不可逆操作)**: `write_strategy` (策略写入) 一旦执行, 发布会流程已对外公布, 撤销需额外公关成本 -- 天道推演"不可逆点"如何用护栏保护?
- **案例决策框架**: 学员需用本单元自主性谱系 L0-L4 + 天道推演 sandbox simulation (3 层推演 immediate -> near -> far) 给出 Maya 的建议, 并量化 ReAct vs Plan-Execute 的步数/成本/风险。
- **教学目标**: 让学员在真实商业张力中应用 Agent 理论, 而非停留在 API 调用层面。

---

## guest_lecture

**客座讲座设计**:

- **Topic (主题)**: "From ReAct to Production: Building Marketing Agents at Scale at Salesforce Einstein"
- **Speaker Profile (主讲人画像)**: Dr. Alex Liu, Head of AI at Salesforce Einstein Marketing Cloud (虚构画像, 原型参考真实 Einstein 团队 Senior Principal Scientist)。背景: Stanford CS PhD (研究方向多 Agent 系统), 在 Salesforce 5 年, 主导 Einstein 营销 Agent 从 Workflow (L1-L2) 升级到 ReAct (L3) 的生产部署。
- **讲座大纲 (90 分钟)**:
  1. (15 min) 从 ReAct 论文 (arXiv 2210.03629) 到生产: 学术 Agent 与生产 Agent 的 3 个关键差异 (成本/可观测性/护栏)。
  2. (30 min) Einstein 营销 Agent 架构 walkthrough: BDI 映射 (Belief = 客户画像 + Desire = 营销 KPI + Intention = 多步计划), 工具调用 (`search_product_info`/`analyze_competitor`/`write_strategy` 的真实实现)。
  3. (20 min) ReAct vs Plan-Execute 在 Einstein 的 A/B 测试结果 (脱敏数据): 何时用哪种范式。
  4. (15 min) 天道推演在 Agent 部署前风险评估的应用: 不可逆操作护栏设计。
  5. (10 min) Q&A。
- **与本单元衔接**: 讲座内容直接对应 `notes.md` 自主性谱系 + ReAct 范式 + 天道推演三节; 学员需在讲座前完成 `starter.ipynb` TODO1-4, 带着实现经验听讲座。

---

## internship_pointer

**实习/驻留指针**:

- **机构 1: LangChain (开源 Agent 框架公司)**
  - **角色**: LangGraph Open Source Contributor / Engineering Intern
  - **衔接**: 本单元 `starter.ipynb` 直接使用 LangChain `@tool` + LangGraph `create_react_agent`/`StateGraph`/`MemorySaver`; 学员完成 6 个 TODO 后即具备贡献 LangGraph 代码库的最低门槛。可申请 LangChain 的开源贡献者实习或 GSoC 项目。

- **机构 2: OpenAI Residency / Anthropic Residency (AI 安全/对齐驻留)**
  - **角色**: AI Residency (1-2 年, 面向 PhD-level)
  - **衔接**: 本单元 `notes.md` 关键回顾 1 引用 Anthropic "Building Effective Agents"; ReAct/Plan-Execute 范式选择涉及 Agent 行为可控性与对齐。学员可基于本单元天道推演 sandbox simulation 协议发展为 Agent 安全研究方向, 申请 OpenAI/Anthropic Residency。

- **机构 3: Sierra / Cognition / Adept (Agent 创业公司)**
  - **角色**: Agent Engineer Intern / Forward Deployed Engineer
  - **衔接**: 这三家是 L4 自主规划 Agent 的产业代表; 学员在 TODO6 实现 Plan-Execute 后, 可将本单元 BDI + ReAct + Plan-Execute 三件套作为面试作品集, 申请 Sierra (客服 Agent) / Cognition (代码 Agent Devin) / Adept (通用 Agent) 的实习。

- **机构 4: 企业 Capstone Sponsor (Imperial MSc BA 模式)**
  - **角色**: Capstone Project (8 周, 与上述 consulting_project 节衔接)
  - **衔接**: Salesforce Einstein / Burberry / Expedia / J&J 等 Imperial MSc BA 合作企业每年提供 Agent 主题 capstone 项目; 本单元 `starter.ipynb` + `research.md` IMRaD 大纲 即该 capstone 的教学预演。

**通用准备建议**: 学员应在 Day 1 结束后 (i) 将 `solution.ipynb` 推到个人 GitHub 作为作品集; (ii) 在 LangChain Discord 帮新手答疑积累声誉; (iii) 写一篇博客对比 ReAct vs Plan-Execute (基于本单元 `research.md` 大纲), 作为申请以上机构的 writing sample。
