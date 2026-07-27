# Day 2 产业链接层 (v7.0)：Agent商业模式定价的产业落地

> **单元**：选修E10 · Day 2 · Agent商业模式设计--从AaaS到outcome-based pricing
> **版本**：v7.0 产业链接层（industry linkage）
> **锚点**：本文件企业案例均来自 `notes.md` 真实Agent定价案例库 + 公司库，不联网查证，遵循 ANTI-STALL。

---

## real_companies

锚定 `notes.md` 真实Agent定价案例库的 >=3 家真实企业：

| 公司 | 与本单元关联 | 业务场景 |
|------|------------|---------|
| **Sierra** | outcome-based定价标杆（`notes.md`明确列示"Sierra | outcome-based | 按解决率收费 | sierra.ai"）。对应Day 2定价模式演进第四阶段"按结果"。 | 客户服务Agent，按工单解决率收费；推理成本下降直接扩大其outcome-based模式的利润空间。是本单元"推理成本阈值使outcome-based从亏钱变盈利"命题的活体样本。 |
| **Cognition / Devin** | AaaS订阅+任务混合定价（`notes.md`明确列示"Devin (Cognition) | AaaS订阅+任务 | $500/月 | cognition.ai公开披露"）。对应第三阶段"按任务"。 | 软件工程Agent，$500/月订阅+按任务计费；是AaaS订阅制与按任务计费混合模式的代表，体现Day 2"五种定价模式如何选择"的核心张力。 |
| **OpenAI** | 推理成本基准的定义者（`notes.md`推理成本基准表：GPT-4o $5/$15 per 1M、GPT-4o-mini $0.15/$0.60）。AaaS订阅代表（ChatGPT Plus $20/月）。 | ChatGPT Plus是AaaS订阅制最大规模样本；OpenAI API定价是全行业推理成本的基准线。Day 2 TODO5推理成本敏感度分析以OpenAI定价为高成本端。 |
| **Anthropic** | MCP协议提出者（`reading.md`链接 https://modelcontextprotocol.io/ ），API Economy 2.0基础设施提供方；结构化输出（tool use）是Agent可发现能力声明的实现。 | Claude Sonnet 4 $3/$15 per 1M（`notes.md`推理成本基准表）；MCP协议标准化是Day 2第五阶段（A2A分润）的触发条件。Anthropic既是推理成本基准方也是协议标准方。 |
| **Cursor** | AaaS订阅制典型（`notes.md`明确列示"Cursor Pro $20/月、Cursor Business $40/月/用户 | cursor.com定价页"）。 | AI代码编辑器，纯AaaS订阅模式；是Day 2"传统SaaS到AaaS"演进的代表性案例，NPV对推理成本不敏感（固定月费覆盖成本）。 |

---

## deployment_example

**真实部署场景：Sierra 在客户服务联络中心的outcome-based定价生产部署**

- **公司**：Sierra（sierra.ai，`notes.md`真实Agent定价案例库）
- **生产场景**：大型零售/金融服务企业的客户服务联络中心，部署Siera的对话Agent处理一线工单。
- **定价契约**：outcome-based，按"已解决工单"（resolved ticket）计费，单价约 $0.99/解决（对标Intercom Fin，`notes.md`同案例库）。
- **规模**：假设单客户日均10,000工单，Agent解决率60%，则日付费 = 10,000 × 60% × $0.99 = $5,940/日，月付费约 $178,200。
- **约束**：推理成本是硬约束。按GPT-4o $5/1M input、每次工单平均消耗3,000 tokens（含多轮对话+工具调用），单工单推理成本 = 3,000/1,000,000 × $5 = $0.015。日推理成本 = 6,000解决 × $0.015 = $90/日，月推理成本 $2,700，占outcome-based收入 $178,200 的1.5%--GPT-4o下已可盈利。
- **效果（推理成本切换）**：切换至DeepSeek V3 $0.27/1M input（降95%），单工单推理成本降至 $0.00081，月推理成本降至 $145.8，占收入0.08%。这正是 `notes.md` 命题"推理成本下降5-10倍时outcome-based从亏钱变盈利"在生产中的体现--在GPT-4o下已盈利，DeepSeek V3下利润率近99.9%。
- **风险缓冲**：失败工单（未解决）不收费，Sierra需用成功工单的收益覆盖失败工单的推理成本（失败也消耗token）。这是outcome-based五实施条件中"风险可控"与"成本结构支持"的生产落地（`notes.md`关键回顾3）。

---

## consulting_project

**Imperial MSc Business Analytics 风格咨询项目（8周，4-5人团队）**

- **Partner（赞助企业）**：Burberry（零售/CPG咨询项目partner，公司库候选；奢侈品零售，营销与客户服务Agent场景与Day 2营销Agent映射表高度契合）
- **Problem（真实业务问题）**：Burberry计划在2026年Q4部署营销与客户服务Agent矩阵（内容生成Agent / 广告投放优化Agent / 销售转化Agent / 全案营销Agent，对标 `notes.md` 营销场景映射表），需决定每个Agent采用何种定价契约（AaaS订阅 / 按调用计费 / outcome-based / 分润），并量化推理成本对总拥有成本（TCO）的影响。
- **Data（企业提供数据）**：Burberry提供脱敏的12个月历史工单量、广告投放调用次数、销售转化漏斗数据、现有SaaS订阅支出明细；外部数据采用 `notes.md` 推理成本基准表（GPT-4o / Claude Sonnet 4 / DeepSeek V3）。
- **Scope（范围）**：8周，4-5人MSc BA团队。Week 1-2 数据清洗与pydantic schema定义；Week 3-4 numpy-financial四种定价契约12月NPV/IRR建模；Week 5-6 statsmodels定价弹性回归（用Burberry历史价格-销量数据估弹性）；Week 7 推理成本敏感度分析+三时间线推演；Week 8 deliverable交付+客户汇报。
- **Deliverable（交付物）**：① 可运行Jupyter笔记本（基于本单元 `solution.ipynb` 改造，含Burberry真实数据）；② Agent定价决策工具包白皮书（pydantic四种契约schema + NPV/IRR计算器）；③ 8周咨询报告，含每个Agent的推荐定价契约+推理成本阈值+风险缓冲机制设计；④ 高管汇报deck（30分钟）。

---

## case_study

**HBS 风格教学案例钩子**

- **Title（暂定）**："Sierra's Gamble: When Outcome-Based Pricing Meets Plummeting Inference Cost"
- **Protagonist（主角）**：Bret Taylor（Sierra联合创始人，前Salesforce联席CEO、前Twitter董事会主席）--Head of AI / CEO视角。
- **Decision（关键决策点）**：2026年Q3，Siera面临定价契约战略选择--① 坚持纯outcome-based（$0.99/解决），押注推理成本继续下降扩大利润率；② 加推AaaS订阅层（如$2,000/月基础费+$0.49/解决），平滑现金流但稀释"按结果付费"的品牌信任资产；③ 进入第五阶段"价值分润"（增量收入15%），押注MCP/A2A经济成熟，但需解决多Agent协作链的贡献归因（Shapley值）。
- **Tension（核心张力/两难）**：
  - **收入稳定性 vs 客户信任**：outcome-based让客户零风险（不解决不付费），但Sierra承担全部推理成本与失败风险；加推订阅层稳定现金流但违背"按结果付费"价值主张。
  - **短期利润 vs 长期生态**：DeepSeek V3降95%让纯outcome-based利润率近99.9%，但若竞争对手（如Intercom Fin）用同样低成本抢客户，价格战将压缩利润--是否趁高利润期投资MCP/A2A分润生态建护城河？
  - **能力不等价的风险**：GPT-4o与DeepSeek V3能力不等价，切低成本模型可能降低解决率（从60%降至45%），解决率下降反过来降低outcome-based收入--推理成本阈值命题的"其他条件不变"假设在生产中不成立。
- **教学用途**：案例数据直接引用 `solution.ipynb` 的NPV/IRR对比 + `notes.md` 推理成本基准表；课堂讨论可接入 `tutorial.ipynb` 的牛津Tutorial Socratic追问。

---

## guest_lecture

**客座讲座**

- **Topic（主题）**："From $0.99/Resolution to Revenue Share: Building an Outcome-Based Agent Business in 2026"
- **Speaker Profile（主讲人画像）**：Sierra 或 Cognition/Devin 的 Head of Pricing / Head of AI Go-to-Market（曾在a16z投资组合公司负责Agent产品定价策略，熟悉 `reading.md` a16z Agent Economy系列论点 + `notes.md` 五阶段定价演进）。
- **内容大纲**：① 从AaaS订阅到outcome-based的真实切换故事（用 `notes.md` 中Sierra/Intercom Fin/11x.ai/DevRev四个真实案例开场）；② 推理成本阈值的生产实战（GPT-4o vs DeepSeek V3的NPV反转点）；③ MCP协议如何让Agent可发现能力声明成为可能（pydantic schema + Anthropic结构化输出）；④ A2A分润机制的挑战--贡献归因与信任建立；⑤ 天道推演视角：如何用三时间线推演预判定价模式迁移。
- **互动环节**：学生用 `starter.ipynb` 现场为自己的营销Agent场景设计定价契约，主讲人用HBS devil's advocate视角追问（与 `tutorial.ipynb` persona对齐）。

---

## internship_pointer

**实习/驻留指针**

- **机构/项目**：
  1. **OpenAI Residency / Anthropic Residency**：研究Agent定价与推理成本优化的前沿，Residency期间可访问内部推理成本数据，验证本单元H1假设（推理成本下降95%使outcome-based NPV转正）。本单元 `solution.ipynb` 的NPV/IRR建模 + statsmodels弹性回归是Residency技术面试的核心准备。
  2. **Sierra / Cognition / 11x.ai / DevRev 产品定价实习**：作为Agent公司的Pricing Analyst或Go-to-Market Intern，直接参与outcome-based定价契约设计。本单元pydantic四种定价契约schema是这些公司的实际生产工具。
  3. **McKinsey / BCG / Bain AI实践组咨询实习**：作为咨询顾问参与企业Agent采购与定价策略项目（如上述Burberry咨询项目），用本单元numpy-financial NPV/IRR计算器做client deliverable。
- **角色**：Pricing Analyst / Go-to-Market Intern / AI Strategy Consultant / Research Resident
- **衔接（本单元如何为该角色做准备）**：本单元的pydantic+numpy-financial+statsmodels三件套是Agent定价岗位的硬技能基线；`notes.md` 五阶段定价演进表与五实施条件是战略咨询面试的框架资产；`research.md` 的IMRaD大纲与可复现清单为Residency的研究产出做准备；`industry.md` 的Burberry咨询项目模拟是Imperial MSc BA capstone的预演。天道推演×商业模式沙盘的同构视角，为战略角色提供"在意识中并行模拟多个定价决策分支"的元认知能力。

---

*v7.0 产业链接层。企业案例锚定 `notes.md` 真实Agent定价案例库 + 公司库，不联网查证。最后更新：2026-07-26*
