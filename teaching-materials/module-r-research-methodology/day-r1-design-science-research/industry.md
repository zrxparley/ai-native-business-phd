# R1 产业链接层 (v7.0)

> 单元主题: 设计科学研究 (DSR) - Hevner 七准则 + Peffers 六步 + March&Smith 四型 + 天道推演↔DSR 同构
> 产业映射: 营销 AI Agent artifact 的 DSR 评估 / 因果证据驱动营销策略 / Agent 平台设计原则产出

---

## real_companies

(>=3 真实企业, 全部来自公司库, 与本单元 DSR + Agent + 因果推断主题匹配)

| 公司 | 与本单元关联 | 业务场景 |
|------|-------------|---------|
| **Stitch Fix** | DSR instantiation 型 artifact (March&Smith 1995) 实例化, 营销 AI artifact 锚点 | 推荐系统 + 营销策略 Agent, 用 causaldata 风格 RCT 评估 uplift, 对标本单元 NSW ATE=1794.34 评估范式; Stitch Fix 内部数据科学团队长期发布因果推断 + 营销方法论博客 |
| **LangChain** | DSR artifact 的工程载体, LangGraph 三节点 Agent 即本单元 instantiations | 企业 Agent 平台, 营销策略 Agent 部署在 LangGraph, 需用 Hevner 七准则评估其设计严谨性 (rigor); LangChain 开源生态天然满足 DSR 准则 7 (研究交流) |
| **Booking.com** | DSR Step 5 评估的实验文化, A/B 测试 + 因果推断是 artifact 评估核心 | 全球实验平台, 每年跑数千 A/B 测试, 对标本单元 NSW 真实 RCT 评估方法论; Booking.com 已发表多篇 industry paper 论述 experimentation culture |
| **McKinsey** | DSR 方法论的咨询落地, 把 Hevner 七准则转为客户端 AI 系统评估框架 | AI 战略咨询, 用 DSR 框架评估企业 AI 系统是否产出可复用设计原则 (准则 4), 是 rigor-vs-design 张力的咨询视角 |
| **Burberry** | Imperial MSc BA 咨询项目 partner, 零售营销 AI 场景 | 营销 Agent 系统在奢侈品零售的部署, 评估"因果证据优先"设计原则的实践有效性; Imperial MSc BA 长期合作 partner |

---

## deployment_example

**Stitch Fix 营销策略 Agent 部署场景 (真实/合理)**:

- **规模**: Stitch Fix 服务数百万用户, 每日生成个性化营销策略与推荐; 内部数据科学团队规模 100+ 人, 营销 AI Agent 系统已部署 3+ 年。
- **约束**: (1) 非确定性 Agent 输出需可追溯 - langsmith / Langfuse trace 存档记录每次运行的 prompt/tool call/output/latency; (2) API/模型版本漂移需监控 - deepeval CI 测试用例确保代码变更后评估结果可追踪; (3) 营销决策需因果证据支撑 - 避免相关性误导 (经典反例: 推荐系统相关性 vs 因果 uplift)。
- **效果**: 对标本单元 NSW ATE=1794.34 的评估范式, Stitch Fix 内部 uplift 模型与 A/B 测试平台产出 ATE-style 估计, 用于评估营销 Agent artifact 的有效性 (Hevner 准则 3 设计评估); 内部报告显示个性化营销策略相对 holdout 组 uplift 显著。
- **本单元工具链复用**: 本单元的 pydantic `DSRArtifact` schema 可直接作为 Stitch Fix 内部 Agent artifact 规格模板 (TODO1), pandas 七准则 DataFrame 可作为月度 Agent 设计评审工具 (TODO3/4), 天道推演↔DSR 同构可作为新 Agent 设计阶段的沙盘推演工具 (TODO6)。

---

## consulting_project

**Imperial MSc BA 风格咨询项目 (8 周, 4-5 人团队)**:

- **Partner (赞助企业)**: Burberry (奢侈品零售, Imperial MSc BA 长期合作 partner, 与本单元营销 AI artifact 主题高度匹配)
- **Problem (真实业务问题)**: Burberry 的营销 AI 系统目前以"做了一个系统"模式交付, 各区域营销团队重复造轮子, 缺乏可复用设计原则 (Hevner 准则 4 缺失); 需用 DSR 方法论将其重新定位为可发表 DSR artifact, 产出 4 条可跨区域复用的设计原则。
- **Data (企业提供数据)**: Burberry 提供 12 个月多区域营销活动 RCT 数据 (结构对标本单元 NSW: treat/revenue/covariates), 约 50K 样本, 含客户分层 (VIP/常规/新客) 与渠道变量 (email/app/in-store); 数据脱敏后存档至 OSF 项目空间。
- **Scope (8 周, 4-5 人团队)**:
  - Week 1-2: 用 pydantic 定义 Burberry 营销 Agent 的 DSR artifact schema (对标本单元 TODO1, 复用 `ArtifactType` 枚举与六步子模型)
  - Week 3-4: pandas 七准则评估 Burberry 现有营销 AI 系统 (对标 TODO3/4, 7×4 DataFrame)
  - Week 5-6: 用 causaldata NSW 方法论评估 12 个月 RCT 数据的 ATE (对标 TODO2, 频率派 + PyMC 贝叶斯扩展)
  - Week 7: 提取 4 条设计原则 (对标 TODO5, 含原则/依据/泛化性)
  - Week 8: 用天道推演沙盘模拟设计原则在新区域 (亚太/北美) 的泛化 (对标 TODO6, 5×3 同构 DataFrame) + 客户最终汇报
- **Deliverable (交付物)**:
  - (a) DSR artifact schema 模板 (pydantic, 可复用至 Burberry 其他 AI 系统)
  - (b) 七准则评估报告 (pandas DataFrame + 可视化 + 改进 action item)
  - (c) 4 条设计原则文档 (含 Hevner 准则 4 研究贡献声明)
  - (d) HBS 风格教学案例草稿 (8-10 页, 详见下方 `case_study`)
  - (e) OSF 预注册文档 (hypothesis + artifact schema 版本冻结)

---

## case_study

**HBS 风格教学案例钩子**:

- **Protagonist (主角)**: Burberry Head of AI (前咨询顾问出身, 既需交付工程价值也需产出学术贡献, 5+ 年 Agent 系统工程经验, 熟悉 Hevner 七准则)
- **Decision (关键决策点)**: 是否将现有营销 AI 系统重新定位为 DSR artifact, 投入 8 周咨询项目资源 (4-5 人团队, 50K 样本数据访问权限) 用 Hevner 七准则评估并产出 4 条设计原则, 还是继续以"做了一个系统"模式快速迭代各区域营销 Agent?
- **Tension (核心张力)**: rigor vs design 的核心张力 (Hevner 2004 §3) - 快速迭代可短期交付工程价值 (design 高, rigor 低), 但无法产出可复用设计原则 (Hevner 准则 4 研究贡献缺失, 各区域重复造轮子); DSR 路径投入 8 周后产出可发表/可跨区域复用的设计原则 (rigor 高, design 短期受影响, 但长期 ROI 更高)。
- **决策推演工具**: 主角用天道推演沙盘模拟两条路径的 3 层未来走向 (immediate: 8 周投入 vs 快速迭代; near: 6 个月后设计原则复用 vs 各区域重新交付; far: 12 个月后可发表 DSR 论文 vs 仍是工程系统), 对标本单元 TODO6 天道推演↔DSR 同构映射。
- **案例讨论核心**: 何时该把工程系统升级为 DSR artifact? 升级的触发条件是什么? (参考 Hevner 准则 2 问题相关性 + 准则 4 研究贡献) 设计原则的跨区域泛化性如何评估? (参考本单元 NSW ATE=1794.34 评估范式)

---

## guest_lecture

**客座讲座**:

- **Topic (主题)**: "From System to Design Principles: 用 DSR 七准则把 Agent 工程实践转为学术贡献" - 一个 Agent 平台公司的视角
- **Speaker Profile (主讲人画像)**: LangChain Head of Solutions (或 Stitch Fix Head of AI), 5+ 年 Agent 系统工程经验, 同时在 DESRIST / ACL / NeurIPS Workshop 等会议发表过 DSR/Agent 论文, 既懂工程交付也懂学术发表; 能现场 demo pydantic DSR schema + pandas 七准则评估 + 真实营销 Agent 案例。
- **讲座结构 (60 分钟 = 40 分钟分享 + 20 分钟 Q&A)**:
  - 0-10 min: 为什么"做了一个系统"不够 - Hevner 准则 4 (研究贡献) 的工程意义
  - 10-25 min: DSR 六步 (Peffers 2007) 在 LangChain Agent 平台的实操 - 以营销 Agent 为例
  - 25-35 min: 现场 demo - 用本单元 pydantic schema + NSW ATE=1794.34 数据评估一个真实 Agent artifact
  - 35-40 min: 设计原则产出 (Hevner 准则 6 设计即搜索) 与天道推演沙盘推演
  - 40-60 min: Q&A - 重点讨论 rigor vs design 张力、Agent 可复现性 (langsmith trace)、DESRIST 投稿路径

---

## internship_pointer

**实习/驻留指针**:

- **机构 (3 个候选, 按匹配度排序)**:
  1. **OpenAI Residency / Anthropic Residency / Google DeepMind Residency** - AI 安全/对齐与 Agent 系统研究驻留项目, 12-24 个月, 在 Mentor 指导下产出可发表 DSR artifact (最匹配本单元 DSR + Agent + 可复现研究主题)
  2. **Stitch Fix / Burberry Data Science Capstone Sponsor** - Imperial MSc BA capstone sponsor, 6-12 个月企业数据科学项目, 直接应用本单元 DSR 方法论到营销 AI artifact
  3. **DESRIST 会议研究实习** - DSR 领域年度会议 (CCF-C, 适合初学者), 投稿前可联系 program chair 做方法论 review
- **角色**: AI Research Resident (Agent 系统方向) 或 Data Science Capstone Researcher; 核心职责为在 Mentor 指导下用 DSR 六步 + Hevner 七准则定位一个真实 Agent 系统研究问题, 产出可复现 artifact + 4 条设计原则 + DESRIST/JMIS 投稿草稿。
- **衔接 (本单元如何为该角色做准备)**: 本单元的 DSR 六步 (Peffers 2007) + Hevner 七准则 + pydantic schema + pandas 评估 + NSW ATE=1794.34 真实数据 + 天道推演↔DSR 同构, 直接构成 Residency 入职前的方法论基础。申请者可在 cover letter 中明确: "我已用 pydantic 将 DSR 六步操作化为可验证 schema (TODO1), 用 pandas 评估了真实 NSW RCT 数据的 artifact (TODO3/4), 理解 rigor vs design 张力 (Hevner 准则 5 vs 2), 能在 Residency 中第一天就用 DSR 框架定位 Agent 系统研究问题并产出可复用设计原则 (准则 4)。" 此外, 本单元的 IMRaD 大纲 (见 research.md) 与 NeurIPS 可复现清单 (7 项) 直接构成 Residency 申请的研究计划模板, DESRIST 会议 (CCF-C) 是初学者友好的 DSR 论文投稿目标。
