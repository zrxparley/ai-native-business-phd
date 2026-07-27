# R6 产业链接层 (v7.0)

> 本单元将研究伦理与 AI 治理锚定到真实产业实践：>=3 家真实企业锚点 + 部署场景 + Imperial MSc BA 咨询项目 + HBS 教学案例 + 客座讲座 + 实习指针。聚焦 AI 安全/对齐/红队测试/治理领域，从公司库挑真实企业。

---

## real_companies

**真实企业锚点（>=3 家，从公司库挑，与本单元 AI 伦理/治理/红队主题匹配）**：

| 公司 | 与本单元关联 | 业务场景 |
|:----:|------------|---------|
| **Anthropic** | 安全/对齐赛道。本单元 notes.md 2026 前沿引用 Anthropic computer use 文档（https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/computer-use）作为 computer use 伦理新风险的案例来源。Anthropic 的 Responsible Scaling Policies 与本单元 Belmont 善行原则（最大化收益、最小化伤害）+ NIST AI RMF Manage（风险缓解）直接对应。 | Claude 模型部署前红队测试；computer use 能力的知情同意/可逆性/隐私保护伦理审查；Alignment Residency 项目。 |
| **Apollo Research** | 安全/对齐赛道。Apollo Research 专注 AI safety evaluations 与 deceptive alignment 检测，其方法论与本单元 garak/PyRIT 红队测试作为 Belmont 善行原则履行手段的定位高度契合--主动发现 AI 系统漏洞是伦理义务。 | AI 安全评估平台；为前沿模型实验室提供部署前 safety evaluation；发布 AI 行为异常检测研究。 |
| **Scale AI** | 安全赛道。Scale AI 提供 AI red teaming / safety testing 服务，其 Scale AI Red Team Network 与本单元 PyRIT（Microsoft）红队框架 + garak（NVIDIA）probes 的技术栈互补，对应 NIST AI RMF Measure（偏见/公平性度量）+ Belmont 善行（主动发现伤害）。 | 为政府与企业客户提供 AI 系统红队测试服务；DOE/NIST 合作的红队评估；数据标注与安全评估平台。 |
| **NVIDIA** | 平台赛道。NVIDIA 开发并开源 garak（https://github.com/NVIDIA/garak，0.15.1）--本单元 TODO6 红队测试工具。garak 的 probes（dan/promptinject/encoding/goodside）在本单元按营销 AI 研究领域映射。 | garak LLM 漏洞扫描器开发维护；NVIDIA NeMo Guardrails 集成；为企业 LLM 部署提供红队扫描。 |
| **Microsoft** | LLM/平台赛道。Microsoft 开发并开源 PyRIT（https://github.com/microsoft/PyRIT，1.0.0）--本单元 TODO6 红队风险评分概念来源。PyRIT 的 Scorer 与 Orchestrator 概念用于量化 AI 研究红队风险。 | PyRIT 自动化红队框架；Azure AI Content Safety；Microsoft Responsible AI Standard 内部治理流程。 |

---

## deployment_example

**真实部署场景：Anthropic Claude computer use 部署前红队测试与伦理审查**

- **公司**：Anthropic
- **生产部署**：Claude 3.5 Sonnet / Claude 4 系列 computer use 能力（AI Agent 直接操作浏览器、桌面应用、文件系统）于 2025 年部署。本单元 notes.md 2026 前沿部分引用其官方文档作为 computer use 伦理新风险（知情同意/隐私保护/可逆性/风险-收益）的案例来源。
- **规模**：Anthropic 在每次重大模型发布前组织内部红队 + 外部研究者红队（NDA 约束，responsible disclosure 流程），覆盖数百名测试者与数千个 adversarial probes。
- **与本单元方法映射**：
  - **Belmont 善行原则**：红队测试主动发现 computer use 漏洞（如 Agent 被诱导删除文件/发送邮件）= 最小化伤害的伦理义务（对应本单元 TODO6）。
  - **NIST AI RMF Measure**：用 garak/PyRIT 风格的 probes 量化 Claude 的 prompt injection 抗性、偏见指数、安全拒绝率（对应本单元 TODO4 NIST 映射）。
  - **EU AI Act 有限风险**：computer use 作为 AI Agent 需履行 Article 50 透明度义务（标注 AI 操作）（对应本单元 TODO4 EU AI Act 分级）。
  - **天道推演三层树**：immediate（Agent 误操作用户文件）-> near（用户投诉/监管介入）-> far（能力回滚+声誉损失），高杠杆点为部署前加不可逆操作确认机制。
- **约束**：NDA + responsible disclosure 漏洞修复窗口；红队发现的高危漏洞需在发布前修复或 mitigations 到位。
- **效果**：Anthropic 在 Claude computer use 发布博客中公开红队发现的风险类别与 mitigations，履行透明度义务。

---

## consulting_project

**Imperial MSc BA 风格咨询项目（8 周，4-5 人团队）**：

- **Partner（赞助企业）**：Deloitte AI Governance Practice（Deloitte Risk & Financial Advisory 下属 AI 治理团队）
- **Problem（真实业务问题）**：Deloitte 的一家零售行业客户（年营收 50 亿欧元，欧盟市场）正在其营销部门部署 AI 动态定价系统，该系统使用用户行为数据 + 敏感属性推断进行实时价格个性化。客户需在 2026 年 EU AI Act 全面生效前完成伦理合规审查--该系统可能触发 Article 5 禁止级（弱势群体剥削性定价）或 Annex III 高风险级（AI 信用评分类比）。Deloitte 需要一个可复用的伦理审查工具向客户交付。
- **Data（企业提供数据）**：客户提供匿名化的用户定价交互日志（100 万条会话，已脱敏，含价格/购买/浏览行为；不含直接 PII）；现有 AI 定价模型的 Model Card（Mitchell et al., 2019 风格）；已有 A/B 测试历史结果。
- **Scope（范围）**：8 周，4-5 人 Imperial MSc BA 学生团队；每周与 Deloitte engagement manager 同步；第 4 周中期评审，第 8 周终期汇报。
- **Deliverable（交付物）**：
  1. **原型工具**：基于本单元 pydantic Belmont schema 的 IRB 自动化审查评分器（扩展至客户真实数据规模），输出 8 维度（3 原则 6 审查项）合规热力图；
  2. **治理策略报告**：Belmont + NIST AI RMF + EU AI Act 三框架并行审查报告，含天道推演三层风险路径（immediate -> near -> far）与高杠杆点建议（部署前补全知情同意 + 差分隐私）；
  3. **红队验证附录**：garak/PyRIT 概念性红队扫描结果（probes: dan/promptinject/goodside），量化 AI 定价系统的 prompt injection 抗性与 Belmont 善行原则履行度；
  4. **MCP 治理工具原型**（可选）：研究 Agent 在定价决策前通过 MCP 自动检查知情同意状态的红线拦截原型。

---

## case_study

**HBS 风格教学案例钩子**：

- **Protagonist（主角）**：Dr. Lin Wei，某全球营销科技公司（年营收 20 亿美元，业务横跨欧盟/北美/亚太）Head of AI Ethics，向 Chief AI Officer 汇报，曾在 Stanford HAI 做博士后研究 AI 公平性。
- **Decision（关键决策点）**：公司营销部门计划在下季度上线"AI 动态定价研究项目"--使用用户浏览历史 + 设备指纹 + 地理位置推断支付意愿，对同一商品向不同用户显示不同价格。Dr. Lin Wei 必须在下周的 AI 治理委员会上决定：**是否批准该研究项目上线，还是要求先补全知情同意机制 + 差分隐私 + 红队验证（延迟 6 个月）？**
- **Tension（核心张力/两难）**：
  - **商业侧**：CMO 估计动态定价可提升毛利率 8-12%，竞争对手已上线类似系统，延迟 6 个月可能损失 1.5 亿欧元收入。
  - **伦理侧**：Dr. Lin Wei 用本单元 pydantic Belmont 评分器对该案例预评分--善行原则得分 22/100（敏感数据无授权 + 弱势群体可能被剥削），尊重个人原则 18/100（无知情同意）；EU AI Act 判定可能触发 Article 5 禁止级（弱势群体剥削性广告）。
  - **天道推演三层树**：immediate（敏感数据无授权使用）-> near（用户投诉 + GDPR 调查）-> far（巨额罚款 + 研究禁令 + 声誉受损），高杠杆点为部署前补全知情同意 + 差分隐私。
  - **决策两难**：批准上线（商业收益 1.5 亿欧元 vs 伦理风险 + 监管风险）vs 叫停补全（延迟 6 个月 vs 伦理合规 + 长期可持续）。Dr. Lin Wei 能否用 Belmont + EU AI Act + 红队三框架证据说服委员会叫停？

---

## guest_lecture

**客座讲座**：

- **Topic（主题）**："AI Red Teaming as Belmont Beneficence: From garak/PyRIT to Production Safety Evaluations"--AI 红队测试作为 Belmont 善行原则的履行手段：从 garak/PyRIT 概念到生产级安全评估。
- **Speaker Profile（主讲人画像）**：Apollo Research 的 Head of Safety Evaluations（或 Anthropic 的 Alignment Research Lead）--一位在前沿 AI 实验室主导部署前红队评估的研究者，拥有 AI safety / deceptive alignment 研究背景，曾在 garak 或 PyRIT 类框架上发布开源工具或论文。
- **讲座内容大纲**（90 分钟）：
  1. （20 min）从 Belmont Report 到 AI 时代：研究伦理如何从人类参与者保护扩展到 AI 系统安全评估；
  2. （30 min）garak + PyRIT 实战：probes（dan/promptinject/encoding/goodside）在生产红队评估中的真实使用案例（脱敏）；
  3. （20 min）computer use 时代的新伦理维度：Agent 操作软件时的知情同意/可逆性/隐私保护挑战；
  4. （20 min）Q&A：从博士研究到产业安全评估的职业路径（连接 internship_pointer）。
- **与本单元衔接**：讲座直接对应 notes.md TODO6（garak/PyRIT 红队测试伦理验证）与 2026 前沿部分（红队作为善行原则履行 + computer use 伦理风险）。

---

## internship_pointer

**实习/驻留指针**：

- **机构（多个候选）**：
  1. **OpenAI Residency**（https://openai.com/residency）--1 年期研究驻留，面向 AI safety / alignment 研究方向；
  2. **Anthropic Alignment Residency / Visiting Researcher**（https://www.anthropic.com/careers）--Alignment research 与 red teaming 方向；
  3. **Apollo Research Internship / Research Fellowship**（https://www.apolloresearch.ai/）--AI safety evaluations 与 deceptive alignment 检测；
  4. **Scale AI Red Team Network**（https://scale.com/red-team-network）--按项目制参与前沿模型红队评估；
  5. **DeepMind Safety Research Internship**--AI safety / alignment 实习。
- **角色**：AI Safety Researcher / Red Team Researcher / Alignment Resident--参与前沿模型部署前红队评估、安全评估方法学研究、红队工具（garak/PyRIT 类）开发。
- **衔接（本单元如何为该角色做准备）**：
  1. **技术栈**：本单元 TODO6 的 garak probes（dan/promptinject/encoding/goodside）+ PyRIT Scorer/Orchestrator 概念直接对应红队研究员日常工具栈；
  2. **伦理框架**：本单元 Belmont Report 三原则 + NIST AI RMF 四步循环为红队研究员提供"为什么红队测试是伦理义务"的理论 grounding（而非纯技术）；
  3. **推演能力**：本单元天道推演三层树（immediate -> near -> far）训练候选人的风险路径预判能力--这是红队研究员设计 adversarial probes 的核心能力；
  4. **可展示工件**：本单元 solution.ipynb（8 案例 IRB 评分 + 红队概念验证 + 天道推演树）可作为面试 portfolio 的写作样本（writing sample）；
  5. **职业叙事**：候选人可在申请文书中用"从 Belmont 善行原则到 garak 红队验证"框架，展示自己理解 AI 安全的伦理维度而非仅技术维度--这是前沿实验室招聘时看重的差异化特质。
