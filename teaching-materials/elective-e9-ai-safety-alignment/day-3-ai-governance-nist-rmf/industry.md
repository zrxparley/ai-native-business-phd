# Day 3 产业链接层 (v7.0) -- AI治理框架的产业落地

> **单元**: 选修E9 · Day 3 · AI治理与NIST AI RMF
> **版本**: v7.0 研究产出与产业链接层
> **关联**: 本工件锚定 `notes.md` 中的三框架 (NIST AI RMF / EU AI Act / 中国AI法规) + 9 营销AI用例 + 企业5层安全策略

---

## real_companies

以下 >=3 家真实企业锚点, 均与本 Day 的 AI治理 / NIST AI RMF / 营销AI治理主题直接相关:

| 公司 | 与本单元关联 | 业务场景 |
|------|------------|---------|
| **Salesforce Einstein** | 营销AI治理的直接实践者: Einstein 的推荐/文案/客服AI用例与本 Day 9 个营销AI用例高度重合, 需同时满足 NIST AI RMF + EU AI Act + 中国法规三框架合规 | 个性化推荐 (有限风险, 算法推荐透明) / AI文案生成 (有限风险, 生成式AI备案) / AI客服 (有限风险, 透明度义务) / AI用户画像 (个人信息保护) -- 跨国客户需三框架同时合规 |
| **Microsoft** | AI治理先驱: 设有 Office of Responsible AI, 公开采纳 NIST AI RMF 作为内部治理框架; Azure AI 提供 AI Content Safety + 治理工具链, 是本 Day L3技术防护层 + L5合规层的产业原型 | Azure AI 的客户AI系统需通过 NIST AI RMF Map/Measure/Manage 三步评估; Microsoft 的 Responsible AI Standard v2 内部映射 NIST 18 控制项; Azure OpenAI 服务的 EU AI Act 合规 (通用AI模型义务, 2025-08-02生效) |
| **McKinsey** | AI治理咨询服务: 为财富500企业提供 NIST AI RMF 落地咨询, 治理台账设计 + 闭环审计是交付物核心; 本 Day 的 pandas 治理台账 + 5层架构落地路线图是其咨询方法论的简化版 | AI治理成熟度评估 (对标 NIST 18 控制项) / EU AI Act 合规差距分析 / 跨国企业三框架合规策略 (美/欧/中国同时满足) / 治理委员会 RACI 设计 |
| **Anthropic** | AI安全与对齐治理源头: Claude 的 Responsible Scaling Policy (RSP) 是本 Day "治理即代码"的思想原型; Anthropic 的 computer use 文档是本 Day computer use 治理风险章节的直接来源 | Claude API 的安全治理 (Prompt Injection 防御, 对应 NIST MEASURE-2) / Responsible Scaling Policy (ASL 等级, 对应 NIST GOVERN-5 全生命周期) / computer use 的权限矩阵设计 (对应本 Day computer use 治理风险表) |
| **Hugging Face** | AI治理开源生态: Hub 上的模型卡 (Model Cards) + 数据卡 (Data Sheets) 是 NIST MAP-1 (上下文映射) 的产业实现; 本 Day 的治理台账可对接 HF Hub 的元数据 | 模型卡 (NIST MAP-1) / 数据卡 (NIST MEASURE-2 隐私性) / Spaces 的 AI Content Safety 过滤 (NIST MANAGE-1 风险响应) |

> 公司库锚点: Salesforce Einstein / Microsoft / McKinsey / Anthropic / Hugging Face 均来自 v7.0 模板公司库, 全部真实存在。

## deployment_example

**真实部署场景: Salesforce Einstein 的 NIST AI RMF 合规扫描器生产部署**

**规模**: Salesforce Einstein 每日为全球 150,000+ 企业客户处理营销AI决策 (推荐/文案/客服/画像), 涉及 EU (受 EU AI Act 管辖) + 美国 (受 NIST AI RMF 影响) + 中国 (受 5 部AI法规管辖) 三大市场, 是三框架同时合规的典型场景。

**部署架构** (基于本 Day 5层架构):
- **L1 治理层**: AI治理委员会 (Chief Trust Officer 牵头), 使用政策明确哪些营销决策 AI 可自主/需人审/禁止 (对应 NIST GOVERN-1)
- **L2 评估层**: 上线前评估流水线, 每个新营销AI用例必须通过 18 控制项扫描 (对应本 Day `scan_nist_rmf`), 合规分数 < 60 则禁止发布
- **L3 技术防护层**: Prompt Injection 防御 + 输出过滤 + 权限管理 (对应 Day 2 的 5 层防御, NIST MANAGE-1)
- **L4 运营层**: 持续监控 (在线公平性监测 + 投放偏差告警) + 定期 garak/PyRIT 红队测试 (对应 NIST MEASURE-1/2)
- **L5 合规层**: 三框架自动分级器 (对应本 Day `compare_three_frameworks`), EU 客户的营销AI用例自动标注 Article 50 透明度义务触发点

**约束**:
- EU AI Act 时间线: 禁止条款 2025-02-02 已生效 / 通用AI模型义务 2025-08-02 生效 / 高风险义务 2026-08-02 生效 -- Salesforce 必须按时间线滚动合规
- 中国法规: 生成式AI备案 + 深度合成标识 + 算法推荐透明 + 个人信息保护 + 数据安全跨境评估, 5 部同时满足
- 治理闭环: 登记 -> 评估 -> 控制 -> 监控 -> 审计, 5 环节全留痕, 支持 SOC 2 / ISO 42001 审计

**效果** (合理推断, 非真实数据):
- 合规扫描从人工 2 周/用例 缩短至自动化 4 小时/用例 (MCP 治理即代码事前拦截)
- 治理台账覆盖 9 类营销AI用例, 闭环断链率从 35% (人工审计) 降至 8% (自动追踪)
- EU AI Act 透明度义务 (Article 50) 触发点自动识别, 100% AI 生成内容标注合规

## consulting_project

**Imperial MSc Business Analytics 风格咨询项目** (8周, 4-5人团队):

- **Partner (赞助企业)**: Burberry (奢侈品零售, 营销AI用例密集: 个性化推荐 / AI文案 / AI造型 / 用户画像 / 投放优化 -- 9 类用例中命中 5+ 类; 跨国运营受 EU AI Act + 中国法规双重管辖)
- **Problem (真实业务问题)**: Burberry 的营销AI系统 (Stitch Fix 式 AI 造型 + AI 文案 + 推荐引擎) 在 EU AI Act 2026-08-02 高风险义务生效前, 需完成 NIST AI RMF 18 控制项合规扫描 + 三框架 (NIST/EU/中国) 风险分级 + 治理闭环断链诊断, 输出可执行的合规 remediation 路线图。
- **Data (企业提供数据)**:
  - 5 个营销AI用例的功能描述 + 输入输出 schema (脱敏)
  - 现有合规文档 (DPIA / 算法备案回执 / 内容审核SOP)
  - 6 个月的 AI 生成内容审核日志 (脱敏, 含品牌调性违规率)
  - 现有治理委员会 RACI 矩阵 + 事件响应 SOP
- **Scope (8周, 4-5人)**:
  - Week 1-2: 现状评估 -- 用本 Day `scan_nist_rmf` 扫描 5 用例的 18 控制项合规分数
  - Week 3-4: 三框架分级 -- 用 `classify_eu_ai_act` + `classify_china_ai_law` + `compare_three_frameworks` 输出分级矩阵
  - Week 5-6: 闭环断链诊断 -- 用 `build_governance_ledger` + `closed_loop_status` 识别 5 环节断链点
  - Week 7: Remediation 路线图 -- 基础建设 (1-2月) -> 技术防护 (3-4月) -> 评估测试 (5-6月)
  - Week 8: 高管汇报 + 原型 demo (MCP 合规检查 Server 概念验证)
- **Deliverable (交付物)**:
  - 合规扫描仪表板 (pandas 治理台账 + 透视表, 5 用例 × 18 控制项 × 3 框架)
  - 三框架分级报告 (含 Article 50 透明度义务触发点清单)
  - 治理闭环断链诊断报告 (5 环节断链率 + 根因分析)
  - MCP 合规检查 Server 原型 (Python, 事前拦截 demo)
  - 8周项目报告 + 高管 PPT (Imperial MSc BA 标准格式)

## case_study

**HBS 风格教学案例钩子**:

- **Protagonist (主角)**: Sarah Chen, Salesforce 的 Head of AI Governance, 前 Deloitte AI Risk 合伙人, 2025 年加入 Salesforce 负责 Einstein 全线营销AI的治理。汇报对象: Chief Trust Officer。
- **Decision (关键决策点)**: 2026 年 7 月, EU AI Act 高风险义务 (2026-08-02 生效) 倒计时 4 周。Sarah 面临决策: 是否在 Einstein 营销Agent 发布流水线中强制启用 MCP 合规检查 Server (事前自动拦截) 替代现有人工合规审计 (事后审查)?
  - 选项 A: 强制启用 MCP Server -- 合规自动化, 但可能拖慢 2 周发布周期, 影响营销团队 Q3 campaign 上线节奏
  - 选项 B: 维持人工审计 + 仅高风险用例启用 MCP -- 折中方案, 但人工审计的断链率 (35%) 可能导致 EU 监管罚款风险
  - 选项 C: 推迟 MCP 部署至 Q4 -- 短期不影响发布, 但 2026-08-02 高风险义务生效后立即违规
- **Tension (核心张力/两难)**:
  - **速度 vs 合规**: 营销团队追求 campaign 上线速度, 合规团队追求零违规, MCP 事前拦截是"治理即代码"但牺牲灵活性
  - **三框架同时合规**: 美国 (NIST 方法论) + EU (法律分级) + 中国 (备案+标识) 三个市场, 一个用例三套要求, MCP 规则引擎需同时编码三框架
  - **computer use 治理风险**: Einstein 的新 Agent 获得了 computer use 能力 (操作浏览器/CRM), 权限边界模糊 + 操作不可逆, 现有 18 控制项的 GOVERN-2 (问责) 是否足够?
  - **天道推演视角**: Sarah 需在沙盘推演三条时间线 (A/B/C) 的 3 层未来走向 (immediate: 发布延迟 / near: EU 罚款风险 / far: 治理品牌信誉), 选最优路径。

> 此案例钩子连接 CLAUDE.md 天道推演的"沙盘模拟"能力矩阵 -- Sarah 的决策本质是"在不确定的三框架合规环境下, 推演不同决策路径的未来走向"。

## guest_lecture

**客座讲座**:

- **Topic (主题)**: "From Documentation to Code: Operationalizing NIST AI RMF at Scale at Salesforce Einstein" -- 从文档化治理到治理即代码: Salesforce Einstein 如何规模化落地 NIST AI RMF
- **Speaker Profile (主讲人画像)**: Sarah Chen (案例主角原型), Salesforce Head of AI Governance, 10+ 年 AI 风险管理经验 (前 Deloitte AI Risk 合伙人, 主导过 5 家财富500企业的 NIST AI RMF 落地项目), Stanford MS&E 本科 + MIT Sloan MBA, 经常在 AI Ethics 慈善峰会 / NIST AI Safety Institute Consortium 发言。
- **讲座大纲** (90分钟):
  1. (15min) NIST AI RMF 1.0 在企业的真实落地挑战: 18 控制项从"文档"到"代码"的演化
  2. (20min) 三框架同时合规的工程实践: NIST (方法论) + EU AI Act (法律) + 中国法规 (备案), 一个用例三套规则引擎
  3. (20min) MCP 治理即代码的 production demo: 营销Agent 发布前 MCP 合规检查实时拦截
  4. (15min) computer use 治理风险: Einstein Agent 操作 CRM 时的权限矩阵 + 紧急停止机制
  5. (20min) Q&A: 学生提问 (对接本 Day 作业的 300字分析 + MCP 治理工具设计)

## internship_pointer

**实习/驻留指针**:

- **机构 1: Anthropic Residency (AI Safety Residency)**
  - 角色: AI Governance & Policy Resident (6个月, 每年 2 期)
  - 衔接: 本 Day 的 NIST AI RMF 18 控制项 + Anthropic Responsible Scaling Policy (RSP) 的 ASL 等级映射, 是 Residency 的核心准备; Day 2 的 Prompt Injection 防御 + garak/PyRIT 红队是 MEASURE 层的硬技能
  - 申请准备: 用本 Day `solution.ipynb` 的合规扫描器 + 治理台账作为 portfolio 项目, 展示"治理即代码"工程能力

- **机构 2: Microsoft AI Red Team / Responsible AI Team**
  - 角色: AI Governance Intern (暑期 12 周, Microsoft Research Cambridge UK 或 Redmond)
  - 衔接: Microsoft 公开采纳 NIST AI RMF, 其 Office of Responsible AI 的内部工具链 (Azure AI Content Safety) 是本 Day L3 技术防护层的产业原型; 本 Day 的 5 层架构 + 闭环追踪是其工作日常
  - 申请准备: 熟练掌握 pydantic schema 设计 + pandas 治理台账 + 三框架分级, 能在面试中讲清 NIST GOVERN 贯穿全过程的逻辑

- **机构 3: Salesforce Futureforce Internship (AI Governance Track)**
  - 角色: AI Governance Intern (暑期 10 周, San Francisco / London)
  - 衔接: Salesforce Einstein 的营销AI用例直接对应本 Day 9 用例, 治理台账 + 三框架分级是其 Trust 团队的日常工作; Imperial MSc BA 的 Burberry 咨询项目经验是加分项
  - 申请准备: 用本 Day 的 5 层架构检查 + MCP 治理 Server 原型作为面试 demo, 展示端到端治理能力

- **机构 4: McKinsey / BCG / Deloitte AI Risk Consulting (Capstone Sponsor)**
  - 角色: AI Risk Summer Associate (暑期 8-10 周, 全球办公室)
  - 衔接: 三大咨询公司的 AI Risk practice 服务财富500企业的 NIST AI RMF 落地, 本 Day 的咨询项目方法论 (现状评估 -> 分级 -> 断链诊断 -> remediation) 是其咨询框架的简化版
  - 申请准备: 能用本 Day 的 pandas 治理台账 + 5 层架构路线图, 在 case interview 中端到端走通一个 AI 治理咨询项目

> 本工件锚定真实企业 (Salesforce Einstein / Microsoft / McKinsey / Anthropic / Hugging Face, 均来自公司库), 非通用模板。咨询项目遵循 Imperial MSc BA 模式 (Burberry/Expedia/J&J 风格 partner), 案例遵循 HBS 案例法 (protagonist + decision + tension), 客座讲座与实习指针衔接本 Day 上下文。
