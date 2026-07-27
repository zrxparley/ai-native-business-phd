# 选修E9 · Day 3：AI治理框架--从NIST AI RMF到企业安全策略 · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 选修E9 AI安全与对齐 · Day 3
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：当营销Agent从"工具"变为"自主决策者"，AI治理如何从"事后合规检查"升级为"治理即代码"？--用pydantic实现NIST AI RMF合规扫描 + 三框架风险分级（NIST/EU AI Act/中国） + 治理闭环台账 + 企业5层安全策略
> **v5.0 升级点**：① 真实框架上机（NIST AI RMF 1.0 + EU AI Act + 中国生成式AI管理办法三框架对比）② pydantic治schema + pandas治理台账 ③ TODO填空式起始笔记本 ④ Notebook化 ⑤ 深链阅读 ⑥ 2026前沿（MCP治理即代码 + computer use治理风险 + garak/PyRIT红队对标）

---

## 学习目标（学完你能做到）

1. 能解释 **NIST AI RMF 1.0** 的四步循环（Govern/Map/Measure/Manage），说明为什么Govern贯穿全过程而非"第一步"，并用pydantic定义18个真实控制项的schema
2. 能实现**三框架风险分级器**：NIST AI RMF（治理方法论，怎么管）+ EU AI Act（4级法律合规，必须怎么管）+ 中国生成式AI管理办法（备案/标识/透明，中国怎么管），并说明三者的互补关系
3. 能用 **pandas** 构建企业AI治理台账（用例清单/风险分级/控制措施/审计记录），追踪**治理闭环**（登记->评估->控制->监控->审计），识别闭环中的"断链"风险
4. 能为营销AI系统（推荐/文案/定价/客服/画像/竞品/投放/深合/情感）设计**企业AI安全策略5层架构**（治理层/评估层/技术防护层/运营层/合规层），并执行落地检查
5. 能区分 **MCP治理即代码**（事前自动拦截）和 **computer use治理风险**（UI操作权限/可逆性/审计粒度）的治理挑战，理解garak/PyRIT红队测试在治理框架中的定位（Measure层的度量手段）

---

## 理论部分：精炼索引（详见独立教材）

> Day 3 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_选修E9_AI安全与对齐.md` § Day 3](../../AI原生化商业博士_独立教材_选修E9_AI安全与对齐.md)（3.1-3.4节，已包含NIST AI RMF四步循环/EU AI Act风险分级/中国AI监管体系/企业AI安全策略5层架构）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：NIST AI RMF 四步循环

NIST AI RMF（AI Risk Management Framework）是美国NIST于2023年1月发布的AI治理框架，已成为全球企业AI治理的事实标准之一。核心是四步循环：

| 功能 | 核心问题 | 关键活动 | 营销实践 |
|:----:|---------|---------|---------|
| **Govern**（治理） | 谁负责AI治理？ | 治理委员会、使用政策、问责人、角色责任 | 营销AI使用政策：哪些决策AI可自主/需人审/禁止 |
| **Map**（映射） | 有哪些AI系统？风险在哪？ | AI用例清单、上下文映射、风险识别、影响评估 | 梳理营销AI用例（文案/推荐/投放/客服），映射风险 |
| **Measure**（度量） | 风险有多大？ | 评估方法、可信特征评估、指标追踪、红队测试 | 文案质量评分、推荐公平性、投放偏差监测、Prompt Injection测试 |
| **Manage**（管理） | 如何应对风险？ | 风险优先级、资源分配、第三方风险、风险响应 | 内容安全过滤、偏差阈值告警、人工审核流程、事件应急 |

**核心洞察**：Govern贯穿全过程，不是第一步做完就结束。Map/Measure/Manage是"执行三步"，Govern是"组织保障"。Day 2的5层Prompt Injection防御对应Measure层（度量安全风险），Day 3的治理框架是"覆盖四步的系统化方法论"。

### 关键回顾 2：EU AI Act 4级风险分级

EU AI Act（2024年8月1日生效，2026年分阶段执行）是全球第一部全面AI监管法律，采用基于风险的分级监管：

| 风险等级 | 条款 | 合规要求 | 营销AI映射 |
|:--------:|:----:|---------|-----------|
| **禁止** | Article 5 | 完全禁止 | 潜意识操纵、社会评分、工作场所情感识别、实时生物识别 |
| **高风险** | Annex III | 合格评定+CE标志+严格合规 | 保险营销中的AI定价（若涉及保险）、信贷评估 |
| **有限风险** | Article 50 | 透明度义务（标注AI生成） | AI文案/图片/视频需标注"AI生成"；AI客服需告知用户 |
| **最小风险** | - | 自由使用 | 关键词推荐、内容审核、营销数据分析 |

**营销AI合规要点**：AI生成内容标注、深度伪造披露、聊天机器人透明度、生物识别限制、数据治理。

### 关键回顾 3：中国AI监管体系

中国已形成多层次AI监管体系，与NIST/EU AI Act形成"三框架"对比：

| 法规 | 核心要求 | 营销AI影响 | 与NIST/EU对应 |
|------|---------|-----------|--------------|
| 《数据安全法》 | 数据分级分类、跨境传输限制 | 客户数据存储传输合规 | 对应NIST MAP-5（第三方风险） |
| 《个人信息保护法》 | 知情同意、最小必要 | 用户画像和定向投放需同意 | 对应NIST MEASURE-2（隐私性） |
| 《生成式AI服务管理暂行办法》 | 生成式AI服务需备案 | 文案生成工具可能需备案 | EU AI Act无直接对应（备案制vs分级制） |
| 《算法推荐管理规定》 | 推荐需透明、可关闭 | 推荐系统需提供关闭选项 | 对应EU AI Act Article 50透明度 |
| 《深度合成管理规定》 | 深度合成内容需标识 | AI图片/视频需标注 | 对应EU AI Act Article 50深伪 |

**三框架互补**：NIST是"怎么管"（治理方法论），EU AI Act是"必须怎么管"（法律合规分级），中国法规是"中国怎么管"（备案+标识+透明）。三者覆盖AI治理的不同维度，跨国企业需同时满足。

### 关键回顾 4：企业AI安全策略5层架构

综合NIST + EU AI Act + 中国法规，企业AI安全策略的完整框架：

| 层 | 名称 | 关键控制 | 与Day 2衔接 |
|:--:|------|---------|------------|
| **L1 治理层** | Governance | AI治理委员会、使用政策、RACI、事件响应SOP | Day 2"防御原则"的组织基础 |
| **L2 评估层** | Assessment | 风险分级、上线前评估、偏见审计、DPIA | Day 2"红队测试"是评估手段 |
| **L3 技术防护层** | Technical Defense | Prompt Injection防御、输出过滤、权限管理、监控告警 | **Day 2已实现5层防御** |
| **L4 运营层** | Operations | 持续监控、定期红队、事件响应、培训、合规报告 | Day 2"反馈学习"的运营化 |
| **L5 合规层** | Compliance | NIST对标、EU AI Act、中国法规、行业合规 | 本Day三框架分级 |

**落地路线图**：基础建设（1-2月）-> 技术防护（3-4月）-> 评估测试（5-6月）-> 持续运营（持续）。

---

## 上机部分：pydantic治schema + pandas治理台账 + 三框架风险分级

> 📓 **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO填空版，你来做）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，gated，做完再看）
> 📊 **真实数据/库**：[`data/README.md`](./data/README.md)（NIST AI RMF + EU AI Act + 中国AI法规 + pydantic + pandas说明）

### 为什么用真实框架（NIST AI RMF + EU AI Act + 中国法规）而非手写示例

v4.0的代码用"手写几个规则"演示治理概念。v5.0改用三个真实治理框架的**真实条款文本**作为规则源：

- **NIST AI RMF 1.0**（https://www.nist.gov/itl/ai-risk-management-framework）：用真实控制项清单（Govern-1~5 / Map-1~5 / Measure-1~4 / Manage-1~4），pydantic定义schema，实现合规扫描器
- **EU AI Act**（https://artificialintelligenceact.eu/）：用真实法规条款（Article 5禁止 / Annex III高风险 / Article 50有限风险），实现4级风险分级器
- **中国AI法规**：用真实法规要求（《生成式AI服务管理暂行办法》备案 / 《算法推荐管理规定》透明 / 《深度合成管理规定》标识 / 《个人信息保护法》知情同意 / 《数据安全法》跨境评估），实现合规要求判定

**互补关系**：NIST是"怎么管"（治理方法论），EU AI Act是"必须怎么管"（法律合规），中国法规是"中国怎么管"（备案+标识）。三者覆盖AI治理的不同维度。

### 营销映射（关键桥接）

本 Day 治理工具的输入用例集基于**真实营销场景**构建9个AI用例：

| 营销AI系统 | EU AI Act风险 | 中国法规要求 | NIST治理重点 | 关键控制点 |
|-----------|:------------:|:----------:|:----------:|-----------|
| AI个性化推荐 | 有限风险 | 算法推荐透明 | Measure（公平性） | 偏见测试、推荐差异监测 |
| AI自动文案生成 | 有限风险 | 生成式AI备案 | Manage（人工审核） | 品牌调性审核、内容安全过滤 |
| AI动态定价 | 最小风险* | 个人信息保护 | Govern（问责） | 价格歧视检测、透明度 |
| AI客服机器人 | 有限风险 | 生成式AI备案 | Map（上下文） | 对话日志、人工转接 |
| AI用户画像 | 最小风险 | 个人信息保护 | Measure（隐私性） | 最小必要、画像透明 |
| AI竞品分析 | 最小风险 | 一般合规 | Map（第三方风险） | 数据来源合规 |
| AI投放优化 | 有限风险 | 算法推荐透明 | Manage（风险响应） | 预算阈值、人工审批 |
| AI深度合成广告 | 有限风险 | 深度合成标识 | Manage（人工审核） | 深伪标识、内容审核 |
| AI情感分析定向 | 最小风险/禁止* | 个人信息保护 | Measure（公平性） | 情感标签脱敏、定向透明 |

> *动态定价若涉及保险/信贷则升为高风险（Annex III）。情感分析若在工作场所/教育机构使用则属Article 5禁止；非工作场所使用为最小风险，但中国法规下仍需个人信息保护合规。

### 上机任务（6个TODO，见starter.ipynb）

1. **TODO1**：用pydantic定义NIST AI RMF控制项schema（ComplianceStatus枚举 + ControlItem模型 + 18个真实控制项）
2. **TODO2**：构建营销AI用例治理登记表（AIUseCase模型 + 9个真实营销AI用例，含三框架分类属性）
3. **TODO3**：实现NIST AI RMF合规扫描器（assess_control + score_to_status + scan_nist_rmf）
4. **TODO4**：实现三框架风险分级器（classify_eu_ai_act + classify_china_ai_law + compare_three_frameworks）
5. **TODO5**：用pandas构建治理台账 + 闭环追踪（build_governance_ledger + closed_loop_status）
6. **TODO6**：企业AI安全策略5层架构检查 + 营销AI治理专项分析（enterprise_security_check + marketing_governance_analysis）

---

## 2026前沿补充：MCP治理即代码 + computer use治理风险 + garak/PyRIT对标

> v5.0新增前沿点。AI治理正在从"人工合规检查"演进为"治理即代码"（Governance as Code），同时AI Agent的新能力（computer use）带来了全新的治理挑战。

### MCP（Model Context Protocol）在AI治理中的应用

**MCP**（Model Context Protocol）是Anthropic于2024年提出的开放协议，让AI Agent通过标准化接口接入外部工具和数据源。在AI治理领域，MCP的颠覆性在于实现**治理即代码**：

- **合规检查Agent**：Agent通过MCP接入合规规则库，在每次行动前自动检查是否违反NIST/EU AI Act/中国法规控制项。不再需要人工事后审计，而是"事前自动拦截"。
- **审计日志MCP Server**：Agent的所有决策通过MCP实时写入审计日志，实现完整可追溯链路。NIST AI RMF的GOVERN-2（问责结构）从"文档化"升级为"代码化"。
- **治理工具链集成**：MCP让合规扫描器、风险分级器、红队测试工具成为Agent可调用的工具，治理从"独立流程"变为"内嵌能力"。

**对营销AI的启示**：营销Agent通过MCP在发布内容前自动检查EU AI Act透明度义务（是否标注AI生成）、中国深度合成标识义务、品牌安全规则、广告法合规。治理不再是瓶颈，而是Agent工作流的有机部分。

### computer use / 计算机使用带来的新型治理风险

2025年AI Agent获得了**computer use**（计算机使用）能力--直接操作浏览器、桌面应用、文件系统。这带来了全新的治理挑战：

| 治理维度 | 传统AI风险 | computer use新风险 | NIST对应 |
|---------|-----------|-------------------|----------|
| 权限控制 | AI只能通过API访问数据 | AI可操作整个软件系统，权限边界模糊 | GOVERN-2问责 |
| 可逆性 | API调用通常可回滚 | Agent删除文件/发送邮件/提交表单可能不可逆 | MANAGE-4风险响应 |
| 审计粒度 | API调用日志结构化 | Agent的UI操作难以完整审计（点击/输入/滚动） | MEASURE-3指标追踪 |
| 隔离性 | API有rate limit和scope限制 | Agent可绕过API限制直接操作UI | MANAGE-3第三方风险 |

**治理升级**：computer use场景下，MANAGE-4（风险响应）必须升级--不仅要有API级别的应急方案，还需要UI级别的"紧急停止"机制。GOVERN-5（全生命周期治理）需要新增"Agent操作权限矩阵"：哪些软件可以操作、哪些操作需要人工确认。

### garak/PyRIT红队测试在治理框架中的定位

Day 2已认知的**garak**（NVIDIA LLM漏洞扫描器）和**PyRIT**（微软自动化红队框架）在NIST AI RMF中的定位是**Measure层**的度量手段：

- **garak**：系统化扫描LLM接口漏洞（20+ probes），是MEASURE-1（评估方法选择）的工具化实现
- **PyRIT**：自动化红队编排（Orchestrator + Target + Scorer），是MEASURE-2（可信特征评估-安全性）的工程实现
- **Day 2的5层防御**：对应MANAGE层（风险响应）的技术防护实现

**注意**：红队测试是"发现漏洞的手段"，不能证明"没有漏洞"（garak通过 不等于 安全）。治理框架是"系统化覆盖四步"的方法论，红队是Measure层的工具。两者互补，不能替代。

> 🔗 这连接了CLAUDE.md中天道推演的"因果链追踪"和"沙盘模拟"能力矩阵--AI治理的Map（风险识别）+ Manage（风险管理）本质是"预判AI系统的风险路径"，与本Day的治理闭环追踪形成"事前推演+事后闭环"的完整治理链路。

---

## 与前后Day的衔接

- **Day 1**：AI对齐问题（价值对齐/Constitutional AI）--今天的"治理框架"是Day 1"对齐评估"的组织化落地：对齐是技术层，治理是组织层
- **Day 2**：AI安全威胁与防御（Prompt Injection/红队）--今天的"NIST Measure层"对应Day 2的"红队测试"，今天的"L3技术防护层"对应Day 2的"5层防御"。Day 2是"技术防护"，Day 3是"系统化治理"

---

## 作业与评估

作业、5分制量表、费曼演练、2分钟话术、复盘自诊表--沿用独立教材 § Day 3 既有设计。本学习材料包不重复，仅新增上机交付物：

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6个TODO全部填好，能跑通）
- [ ] 一段300字分析：你的9个营销AI用例在三框架（NIST/EU/中国）下，哪个框架识别出的风险最多？治理闭环中哪个环节最容易断链？对应的天道推演风险路径是什么？
- [ ] （可选）为你的企业营销AI系统设计一个MCP治理工具：Agent在执行操作前通过MCP检查哪些合规规则？computer use场景下需要哪些额外权限控制？

---

## 英语轨道（i+1）

打开 [NIST AI RMF 1.0 官方页面](https://www.nist.gov/itl/ai-risk-management-framework)，用浏览器翻译插件辅助阅读Executive Summary。关键术语：Govern / Map / Measure / Manage / Trustworthy AI / Accountable Owner。不要求读懂每个词，目标是理解四步循环的逻辑。

---

*本讲义由v5.0学习材料包升级生成。理论部分引用独立教材，上机部分用真实框架（NIST AI RMF + EU AI Act + 中国AI法规）+ 真实库（pydantic + pandas）+ TODO脚手架。*
*最后更新：2026-07-25*

---

## 学习科学层 (v6.0)

本单元采用刻意练习(Ericsson)/间隔重复(FSRS-6,SM-2)/建构对齐(Biggs ILO↔TLA↔AT)/牛津tutorial LLM仿真(Socratic,Hattie四级反馈)。mastery 阈值与 Worked-Faded 示例见 practice.md 与 alignment.md。交叉练习(interleaving)促进迁移, 提取练习(retrieval practice)优于重读。

## 研究产出与产业链接层 (v7.0)

本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+arXiv/法规链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业 Salesforce Einstein/Microsoft/McKinsey/Anthropic/Hugging Face + 部署场景 + Imperial MSc BA 咨询项目 partner=Burberry + HBS教学案例 protagonist=Salesforce Head of AI Governance + 客座讲座 + 实习指针 Anthropic/Microsoft/Salesforce Residency)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。linked_paper 锚定 NIST.AI.100-1 (https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf) + NIST.AI.600-1 + EU AI Act 2024/1689。详见 research.md 与 industry.md。

---

## 学术前沿层 (v9.0)

本单元新增 `frontier.md`：注入 2025-2026 最新学术前沿（N 篇真实 arXiv 论文 + 批判性综述 + delta_to_unit + ≥3 开放研究问题 + 方法论批评）。论文来自 `_frontier_corpus/elective-e9-ai-safety-alignment.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证），覆盖前沿课题：可扩展监督 × 机制可解释性 × Agent安全。面向博后/教授级读者：批判性综述非罗列，delta_to_unit 显式指出前沿如何更新本单元所教，开放问题为可发表研究方向。详见 `frontier.md`。
