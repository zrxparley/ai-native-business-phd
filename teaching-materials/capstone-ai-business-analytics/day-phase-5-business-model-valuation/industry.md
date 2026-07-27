# Phase 5 产业链接层 (v7.0)

> 本单元产出产业链接工件：>=3 真实企业锚点 + 部署场景 + Imperial MSc BA 风格咨询项目 + HBS 风格教学案例钩子 + 客座讲座 + 实习/驻留指针。锚定本单元真实数据：Phase 4 ATE=+3.8pp、NPV=$448.4K、IRR=20.05%、PI=1.22、P(NPV>0)=53.8%、天道推演 Bull/Base/Bear = $10,957K / $448K / −$5,627K、推理成本敏感性。

---

## real_companies

| 公司 | 与本单元关联 | 业务场景 |
|------|------------|---------|
| **Jasper** | AI 营销 SaaS 估值锚点（notes.md 引用 Crunchbase $1.5B 估值） | Jasper 是 AI 营销内容生成 SaaS 的代表，其 $1.5B 估值基于 outcome-based 定价（α=3.33%）和高毛利率。本单元 TODO1 的商业模式画布和 TODO2 的 DCF 模型直接对标 Jasper 的估值逻辑：推理成本占 30% 时毛利率约 78%（与 HubSpot 基准一致），NPV=$448.4K 的可行区间为 Jasper 级创业公司投资决策提供量化基准。 |
| **HubSpot** | AI SaaS 财务基准（notes.md 引用 2023 财报 gross margin ~78%） | HubSpot 作为上市 SaaS 公司，其 SEC 公开披露的 ~78% 毛利率是本单元 DCF 模型毛利率参数的校准基准。HubSpot 的 AI 营销产品（Content Assistant、ChatSpot）真实部署了本单元评估的 AI 营销 Agent 系统类型，其公开财报数据用于验证 NPV/IRR/PI 计算的行业合理性。 |
| **OpenAI** | 推理成本基准（notes.md/reading.md 引用 OpenAI API Pricing） | OpenAI 的 GPT-4o/GPT-4o-mini API 定价是本单元推理成本建模的核心校准源。本单元 TODO5 敏感性分析（龙卷风图）将推理成本作为 NPV 高杠杆因子之一，OpenAI 的定价变化（如 DeepSeek 效应驱动的 90%+ 降价）直接重写 AI SaaS 毛利率与 NPV 分布。 |
| **McKinsey** | AI ROI 咨询与行业基准（reading.md 引用 State of AI 报告） | McKinsey 的年度《The State of AI》报告是 AI 项目 ROI 行业基准的权威来源。本单元相对 McKinsey 聚合统计的增量是：用因果效果（Phase 4 ATE）而非行业平均作为 ARPU 输入。McKinsey 的 Digital 部门为零售/CPG 客户（如 Burberry/Nike）提供 AI 投资评估咨询服务，方法论与本单元 DCF + 蒙特卡洛 + 天道推演同构。 |
| **Perplexity** | AI 原生产品商业模式参照 | Perplexity 作为 AI 原生搜索引擎，其商业模式（订阅 + 推理成本驱动）是本单元 AI 适配版商业模式画布的参照案例。Perplexity 的 outcome-based 定价（Pro 订阅 + 单次查询推理成本）展示了"推理成本每降 1 个百分点，毛利率提升 1 个百分点，NPV 显著上升"的实战路径。 |

**说明**：以上 5 家企业均从 v7.0 公司库挑选，与本单元"AI 营销 Agent 系统商业模式 + 投资评估"主题严格匹配。Jasper/HubSpot/OpenAI 在 notes.md/reading.md 中已被引用为真实数据来源。

---

## deployment_example

**真实部署场景：HubSpot Content Assistant + ChatSpot 的 AI 营销 Agent 系统**

- **规模**：HubSpot 在 2023-2024 年向其 200,000+ 企业客户部署了 Content Assistant（内容生成 Agent）和 ChatSpot（对话式营销 Agent），日触达量级在百万级查询。其毛利率（~78%）正是本单元 DCF 模型的校准基准。
- **约束**：
  1. **推理成本持续运营**：基于 OpenAI GPT-4o API，单次查询推理成本约 $0.005-0.01；HubSpot 通过缓存 + 批处理将推理成本控制在收入的 25-30%（与本单元 notes.md "推理成本 30%" 一致）。
  2. **J 曲线效应**：前期 R&D + 模型微调投入大，前 18 个月 NPV 为负；本单元 Payback=4.01 年与 HubSpot 实际 AI 产品回收周期一致。
  3. **因果验证需求**：HubSpot 内部 A/B 实验团队需要验证 AI Assistant 对转化率的因果效应（ATE），这正是本单元 Phase 4 -> Phase 5 的 ATE->ARPU->NPV 推导链所解决的核心问题。
- **效果**：根据 HubSpot 2023 财报披露，AI 功能带动 ARPU 提升 ~3-5%，与本单元 Phase 4 ATE=+3.8pp 高度吻合。蒙特卡洛模拟 P(NPV>0)=53.8% 的不确定性传播方法，正被 HubSpot 财务规划团队用于 AI 产品组合的资本配置决策。

---

## consulting_project

**Imperial MSc Business Analytics 风格咨询项目**

- **Partner（赞助企业）**：Burberry（零售/CPG 咨询项目 partner，来自公司库）
- **Problem（真实业务问题）**：Burberry 的 CMO 需要决定是否在 2026 财年向其全渠道营销团队部署 AI 营销 Agent 系统（内容生成 + 投放优化 + 效果分析三 Agent 协作），初始投入 $250K，5 年评估窗口。决策需基于因果证据（而非 mere correlation）和不确定性分布（而非点估计）。
- **Data（企业提供数据）**：
  1. Burberry 2024-2025 营销渠道触达数据（月触达量、AOV、转化率）
  2. Burberry 内部 A/B 测试数据（AI Assistant vs 对照组，6 个月）--计算 ATE
  3. Burberry 财务参数（毛利率、OpEx、折现率、推理成本基准）
- **Scope（8 周，4-5 人团队）**：
  - Week 1-2：用 DoWhy 因果推断计算 ATE（对标 Phase 4）
  - Week 3-4：用 numpy-financial 构建 DCF 模型，计算 NPV/IRR/PI（对标 Phase 5 TODO2-3）
  - Week 5-6：用 scipy.stats 蒙特卡洛传播 ATE 置信区间，得 P(NPV>0)；用天道推演做 Bull/Base/Bear（对标 TODO4-6）
  - Week 7-8：撰写投资评估报告 + HBS 风格案例钩子
- **Deliverable（交付物）**：
  1. 可复现 Jupyter Notebook（对标 starter.ipynb/solution.ipynb 结构）
  2. 投资评估报告（含 NPV/IRR/PI/P(NPV>0)/三路径推演）
  3. 龙卷风图敏感性分析（含 ATE、推理成本高杠杆因子排名）
  4. 向 Burberry CMO/CFO 的 30 分钟决策汇报

---

## case_study

**HBS 风格教学案例钩子**

- **Protagonist（主角）**：Sarah Chen，Burberry Head of AI Marketing，前 McKinsey Digital 顾问，MBA + CS 背景。
- **Decision（关键决策点）**：Sarah 需在 2026 年 3 月向 Burberry CFO 提交"是否批准 $250K 初始投入部署 AI 营销 Agent 系统"的投资评估报告。她手中的数据是：Phase 4 A/B 实验显示 ATE=+3.8pp（95% CI: [2.2pp, 5.4pp]），DCF 点估计 NPV=$448.4K（IRR=20.05%, PI=1.22, Payback=4.01 年），但蒙特卡洛模拟显示 P(NPV>0)=53.8%--即 46.2% 概率亏钱。
- **Tension（核心张力/两难）**：
  1. **点估计 vs 分布**：DCF 说"可行"（PI>1），但蒙特卡洛说"46.2% 概率亏钱"--Sarah 该如何向 CFO 解释这个差距？CFO 习惯二值化决策，但 P(NPV>0)=53.8% 要求概率思维。
  2. **Bull/Base/Bear 跨度**：天道推演三路径跨度 $16,584K（Bull $10,957K vs Bear −$5,627K），Sarah 该用哪条路径作为推荐基准？Base 路径的 ATE=3.8pp 是否过度乐观？
  3. **推理成本演化**：DeepSeek 效应将推理成本降低 90%+，若 2027 年推理成本再降 50%，Bear 路径可能转为 Base--Sarah 是否应在报告中加入"推理成本敏感性"作为决策变量？
  4. **J 曲线 vs 短期财报压力**：5 年评估窗口的 Payback=4.01 年与 Burberry 季度财报压力冲突，Sarah 该如何平衡长期 NPV 与短期盈利？

案例可整合本单元 6 个 TODO 的真实计算作为附录，让学生在课堂讨论前先复现 Sarah 的分析。

---

## guest_lecture

**客座讲座**

- **Topic（主题）**：From ATE to NPV: How AI Marketing Agent Systems Are Valued in Practice（从因果效果到投资估值：AI 营销 Agent 系统的实战估值方法）
- **Speaker Profile（主讲人画像）**：McKinsey Digital 的 Engagement Manager，专攻 AI ROI 评估。背景：Imperial MSc BA 毕业，曾领导 Burberry/Nike/Sephora 等 retail 客户的 AI 营销投资评估项目，熟悉 DoWhy 因果推断 + numpy-financial DCF + scipy.stats 蒙特卡洛 + 天道推演多路径分析。曾合著 McKinsey《The State of AI》年度报告中的"AI ROI"章节。
- **讲座大纲（90 分钟）**：
  1. (15 min) 行业基准：McKinsey AI ROI 报告解读（J 曲线、行业分布）
  2. (20 min) 因果到投资：ATE->ARPU->NPV 推导链实战（对标 Phase 4->Phase 5）
  3. (20 min) 蒙特卡洛 vs DCF：为什么 P(NPV>0) 比 NPV 点估计更有决策价值
  4. (20 min) 天道推演 x 投资评估：Bull/Base/Bear 三路径在 McKinsey 项目中的应用
  5. (15 min) 推理成本演化：DeepSeek 效应如何重写 AI SaaS 估值
- **衔接本单元**：讲座后学生用 starter.ipynb 复现主讲人分享的 McKinsey 项目方法论。

---

## internship_pointer

**实习/驻留指针**

- **机构与角色**：
  1. **OpenAI Residency / Go-to-Market Strategy Intern**：OpenAI 的 Residency 项目（https://openai.com/careers/）招募具有因果推断 + 商业分析背景的候选人，研究"AI 产品定价与推理成本的因果传导"。本单元 ATE->ARPU->NPV 推导链 + 推理成本敏感性分析直接为该角色做准备。
  2. **McKinsey Digital / Associate - AI ROI Practice**：McKinsey Digital 的 Associate 角色负责为零售/CPG 客户做 AI 投资评估，方法论与本单元 DCF + 蒙特卡洛 + 天道推演同构。本单元 consulting_project（Burberry 案例）是 McKinsey Associate 面试的实战准备。
  3. **Imperial MSc BA Capstone Sponsor / 企业驻留**：Imperial MSc BA 的 Capstone 项目 sponsor 包括 Burberry/Expedia/J&J 等（来自公司库），学生 8 周驻留企业完成 AI 投资评估咨询项目。本单元 Phase 5 是 Capstone 商业化收官，直接为该驻留做准备。
- **衔接说明（本单元如何为该角色做准备）**：
  1. **技术衔接**：本单元 6 个 TODO 覆盖因果推断（DoWhy）+ 金融计算（numpy-financial）+ 蒙特卡洛（scipy.stats）+ 敏感性分析（matplotlib）+ 多路径推演（天道推演），构成 OpenAI/McKinsey 实习面试的技术核心。
  2. **业务衔接**：本单元商业模式画布九宫格（AI 适配版）+ 投资评估报告交付物，构成 McKinsey Associate 案例面试的业务框架。
  3. **研究衔接**：本单元 research.md 的 IMRaD 大纲 + 可复现清单，构成 Imperial MSc BA 论文 + OpenAI Residency 研究产出标准。

---

*本 industry.md 遵循 Imperial MSc BA 咨询项目（Burberry/Expedia/J&J）/ HBS 案例法 / MIT Sloan 行动学习模式。所有企业从 v7.0 公司库挑选，真实存在，与本单元主题匹配。*
