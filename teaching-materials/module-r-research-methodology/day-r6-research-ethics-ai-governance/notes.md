# 模块R · R6：研究伦理与AI治理 · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 模块R 博士研究方法论 · R6（模块R收官单元）
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：博士研究的底线是伦理。AI+营销研究中，用户数据、算法决策、商业利益三者交织--如何用 Belmont Report 伦理审查清单 + NIST AI RMF 研究伦理映射 + 红队测试伦理验证，守住研究底线？
> **v5.0 升级点**：① 真实库上机（pydantic 伦理schema + pandas 审查分析 + garak/PyRIT 红队概念）② TODO 填空式起始笔记本 ③ Notebook 化 ④ 深链阅读 ⑤ 2026 前沿（红队伦理验证 + computer use 伦理风险 + 天道推演预判伦理路径 + MCP 治理工具）

---

## 学习目标（学完你能做到）

1. 能解释 Belmont Report（1979）三条研究伦理核心原则（**尊重个人** / **善行** / **公平正义**），并说明每条原则在 AI+营销研究中的具体体现（知情同意 / 风险-收益评估 / 负担收益公平分配）
2. 能用 **pydantic** 定义 IRB 伦理审查清单 schema（3 原则 6 审查项），实现伦理审查评分器对 AI 研究案例逐一评分（0-100），输出合规状态和伦理风险等级
3. 能从**研究伦理视角**映射 NIST AI RMF 四步循环（Govern/Map/Measure/Manage），并说明与技能2 Day1 企业治理视角的区别（研究视角聚焦人类参与者保护，企业视角聚焦组织合规流程）
4. 能用真实 EU AI Act 条款（Article 5 / Annex III / Article 50）从研究合规视角判定 AI 研究案例的风险等级
5. 能用 **garak**（NVIDIA 红队扫描器）+ **PyRIT**（微软红队框架）的概念，将 AI 红队测试作为 Belmont 善行原则的履行手段，并用**天道推演**的 3 层推演树预判 AI 研究的伦理风险路径

---

## 理论部分：精炼索引（详见独立教材）

> R6 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_模块R_博士研究方法论.md` § 七、R6：研究伦理与AI治理](../../AI原生化商业博士_独立教材_模块R_博士研究方法论.md)（7.1-7.9 节，已包含 Belmont Report 三原则/NIST AI RMF 四步循环/EU AI Act 风险分级/算法偏见评估/营销AI伦理自查/与博士论文关联/对标大学说明）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：Belmont Report 三原则（IRB 审查基础）

研究伦理的历史脉络：Nuremberg Code（1947）-> Declaration of Helsinki（1964）-> **Belmont Report（1979）**。Belmont Report 确立的三条原则至今仍是 IRB（Institutional Review Board）审查的基础：

| 原则 | 英文 | 核心要求 | AI+营销研究体现 |
|:----:|:----:|---------|---------------|
| **尊重个人** | Respect for Persons | 知情同意（informed consent）+ 自主决策保护 | 用户行为数据做 A/B 测试，用户是否知情？GDPR 要求"知情、明确、自由"的同意 |
| **善行** | Beneficence | 最大化收益、最小化伤害 | AI 实验不应向用户展示有害或冒犯性内容；风险-收益评估 |
| **公平正义** | Justice | 负担和收益公平分配 | 不能让弱势群体承担过多研究风险，不能让优势群体独享收益 |

### 关键回顾 2：NIST AI RMF 四步循环（研究伦理视角）

NIST AI RMF（2023年1月发布）的四步循环，从**研究伦理视角**映射：

| 功能 | 企业治理视角（技能2 Day1） | **研究伦理视角（本单元 R6）** |
|:----:|--------------------------|------------------------------|
| **Govern** | AI治理委员会、使用政策、问责机制 | **IRB审批、伦理委员会监督、研究者问责** |
| **Map** | AI用例清单、上下文映射 | **人类参与者识别、研究风险映射** |
| **Measure** | 准确性、公平性、安全性指标 | **偏见/公平性度量、风险-收益量化** |
| **Manage** | 风险缓解、持续监控 | **知情退出机制、风险缓解、参与者保护** |

**核心区别**：技能2 Day1 从企业治理视角（组织如何管AI），R6 从研究伦理视角（研究者如何保护参与者）。两者互补，覆盖AI治理的不同维度。

### 关键回顾 3：EU AI Act 风险分级（研究合规视角）

| 风险等级 | 条款 | 营销AI示例 | 研究合规要求 |
|:--------:|:----:|-----------|------------|
| **禁止** | Article 5 | 操控性营销、弱势群体剥削性广告 | 研究中完全禁止 |
| **高风险** | Annex III | AI信用评分（营销中基于AI的客户信用评估） | 需风险评估、数据治理、人工监督 |
| **有限风险** | Article 50 | AI客服、AI生成营销内容 | 透明度义务（标注AI生成） |
| **最小风险** | - | 垃圾邮件过滤、推荐系统 | 自由使用（鼓励自律） |

### 关键回顾 4：算法偏见评估

偏见来源（Barocas & Selbst, 2016）：训练数据偏见 / 算法偏见 / 部署偏见。评估方法：Model Cards（Mitchell et al., 2019）、Fairlearn、AIF360。

---

## 上机部分：用 pydantic + pandas + garak/PyRIT 实现研究伦理工具链

> 📓 **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO 填空版，你来做）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，gated，做完再看）
> 📊 **真实数据/库**：[`data/README.md`](./data/README.md)（Belmont Report + NIST AI RMF + EU AI Act + garak + PyRIT + OECD AI Incidents 说明）

### 为什么用真实框架（Belmont Report + NIST AI RMF + garak/PyRIT）而非手写示例

v4.0 的代码用"手写几个检查项"演示伦理概念。v5.0 改用三个真实框架的**真实条款/原则**作为规则源：

- **Belmont Report（1979）**：用真实三原则6审查项，非编造。用 pydantic 定义审查清单 schema，实现 IRB 式伦理审查评分器。
- **NIST AI RMF 1.0**（https://www.nist.gov/itl/ai-risk-management-framework）：从研究伦理视角映射四步循环。
- **garak + PyRIT**：用真实红队工具的概念，将 AI 安全测试作为 Belmont 善行原则的履行手段。

**三视角互补**：Belmont Report 是"研究伦理底线"，NIST AI RMF 是"怎么管的方法论"，garak/PyRIT 是"怎么验证的技术手段"。

### 营销映射（关键桥接）

本单元审查工具的输入案例集基于 **OECD AI Incidents Monitor**（https://oecd.ai/en/incidents-overview）的真实 AI 事件类型构建。营销 AI 专项分析：

| 营销AI研究 | Belmont风险 | EU AI Act风险 | 红队验证重点 | 天道推演高杠杆点 |
|-----------|:-----------:|:------------:|:----------:|:--------------:|
| AI个性化推荐研究 | 低（有知情同意） | 有限风险 | dan/promptinject probes | 定期偏见审计 |
| AI自动文案A/B测试 | 中（无知情同意） | 有限风险 | dan/promptinject probes | 补充知情同意机制 |
| AI动态定价研究 | **高**（敏感+无同意+弱势） | **禁止** | dan/promptinject/goodside | 补全知情同意+差分隐私 |
| AI客服交互研究 | 低（有知情同意） | 有限风险 | dan/promptinject probes | 定期偏见审计 |

### 上机任务（6 个 TODO，见 starter.ipynb）

1. **TODO1**：用 pydantic 定义 Belmont Report 伦理审查清单 schema（3原则6审查项）
2. **TODO2**：构建真实 AI 研究案例集（8案例，基于 OECD AI Incidents 事件类型）
3. **TODO3**：实现 IRB 伦理审查评分器（assess_checklist_item + score_to_status + irb_ethics_review）
4. **TODO4**：NIST AI RMF 研究伦理映射 + EU AI Act 研究合规判定
5. **TODO5**：用 pandas 构建伦理审查热力图（案例×原则透视 + 短板分析）
6. **TODO6**：AI 红队测试伦理验证（garak/PyRIT 概念）+ 天道推演预判伦理风险路径

---

## 2026 前沿补充：红队伦理验证 + computer use 伦理风险 + 天道推演 + MCP 治理

> v5.0 新增前沿点。研究伦理正在从"事后审查"演进为"持续验证"，同时 AI Agent 的新能力带来了全新的伦理挑战。

### 红队测试作为 Belmont 善行原则的履行手段

**garak**（NVIDIA/garak，0.15.1）和 **PyRIT**（microsoft/PyRIT，1.0.0）不仅是安全工具--在研究伦理框架下，红队测试是**善行原则（maximize benefits, minimize harms）的履行手段**。当你的 AI 研究涉及 AI 系统时，主动发现系统漏洞（红队测试）是减少伤害的伦理义务，而非可选的技术步骤。

| Belmont 原则 | 红队测试的伦理角色 |
|:-----------:|------------------|
| 善行 | 红队测试发现漏洞 = 最小化伤害（主动发现而非被动等待事故） |
| 尊重个人 | 红队测试防止 AI 系统被操纵泄露用户数据 = 保护参与者自主权 |
| 公平正义 | 红队测试检测算法偏见 = 确保负担公平分配 |

### computer use / 计算机使用带来的新型研究伦理风险

2025年 AI Agent 获得了 **computer use**（计算机使用）能力--直接操作浏览器、桌面应用、文件系统。这在研究伦理中引入新维度：

| 伦理维度 | 传统 AI 研究风险 | computer use 新风险 |
|---------|-----------------|-------------------|
| 知情同意 | 用户知道数据被用于研究 | Agent 操作的软件用户可能不知情被观察 |
| 隐私保护 | 数据脱敏即可 | Agent 可看到屏幕全部内容，脱敏困难 |
| 可逆性 | API 调用通常可回滚 | Agent 删除文件/发送邮件可能不可逆 |
| 风险-收益 | 风险可预估 | Agent 自主操作的风险难以预估 |

### 天道推演预判 AI 研究伦理风险路径

**天道推演**在此单元的实践应用：用天道推演的沙盘模拟方法预判 AI 研究的伦理风险路径，连接 Belmont Report 的风险-收益评估和 NIST AI RMF 的 Manage（风险管理）。

**推演框架**（3层推演树）：
1. **局势拆解**：识别 AI 研究的关键变量（涉及人类数据、敏感属性、伤害严重度、弱势群体）
2. **因果建模**：构建伦理风险因果链
3. **沙盘展开**：为每个案例生成 immediate -> near -> far 三层推演
4. **高杠杆点识别**：小投入改变大局的干预节点

**推演示例**（AI动态定价研究）：
- immediate：敏感数据无授权使用
- near：用户投诉/隐私监管介入 -> GDPR 调查
- far：巨额罚款 + 研究禁令 + 声誉受损
- 高杠杆点：部署前补全知情同意流程 + 差分隐私

> 🔗 这连接了 CLAUDE.md 中天道推演的"因果链追踪"和"沙盘模拟"能力矩阵，将研究伦理从"事后审查"升级为"事前风险推演"。

### MCP（Model Context Protocol）在研究伦理治理中的应用

**MCP** 让 AI Agent 通过标准化接口接入伦理治理工具（合规检查/IRB审查/审计日志），实现"伦理治理即代码"：研究 Agent 通过 MCP 在每次数据采集前自动检查知情同意状态、在每次模型部署前自动执行 garak 红队扫描。

---

## 与模块R收官的关联

R6 是模块R（博士研究方法论）的收官单元：

| 单元 | 方法论 | 核心问题 |
|:----:|--------|---------|
| R1 | 设计科学研究（DSR） | 怎么定义研究问题？ |
| R2 | 行动研究 | 怎么把研究用到企业，同时产出知识？ |
| R3 | 混合方法 | 怎么设计评估方案？ |
| R4 | PRISMA 系统综述 | 怎么做文献综述？ |
| R5 | IMRaD 学术写作 | 怎么写论文？ |
| **R6** | **研究伦理与AI治理** | **怎么守住底线？** |

**天道推演视角**：R1-R5 是"怎么做研究"，R6 是"研究的边界在哪"。天道推演的"反事实"思维--"如果不这样，会怎样"--正是伦理审查的核心：如果不做知情同意，会怎样？如果不做红队测试，会怎样？

---

## 作业与评估

作业、5 分制量表、费曼演练、2 分钟话术、复盘自诊表--沿用独立教材 § 7.8 既有设计。本学习材料包不重复，仅新增上机交付物：

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6 个 TODO 全部填好，能跑通）
- [ ] 一段 300 字分析：你的 8 个 AI 研究案例在 Belmont 哪条原则得分最低？根因是什么？对应的天道推演风险路径和高杠杆点是什么？
- [ ] （可选）为你的 Capstone 设计一个 MCP 伦理治理工具：研究 Agent 在数据采集前通过 MCP 检查哪些伦理规则？

---

## 英语轨道（i+1）

打开 [NIST AI RMF 1.0 官方页面](https://www.nist.gov/itl/ai-risk-management-framework)，用浏览器翻译插件辅助阅读 Executive Summary。关键术语：Belmont Report / Respect for Persons / Beneficence / Justice / Informed Consent / IRB。不要求读懂每个词，目标是理解三原则的逻辑。

---

*本讲义由 v5.0 学习材料包升级生成。理论部分引用独立教材，上机部分用真实框架（Belmont Report + NIST AI RMF + EU AI Act）+ 真实库（pydantic + pandas + garak/PyRIT 概念）+ TODO 脚手架。*
*最后更新：2026-07-24*

## 学习科学层 (v6.0)

本单元采用刻意练习(Ericsson)/间隔重复(FSRS-6,SM-2)/建构对齐(Biggs ILO↔TLA↔AT)/牛津tutorial LLM仿真(Socratic,Hattie四级反馈)。mastery 阈值与 Worked-Faded 示例见 practice.md 与 alignment.md。交叉练习(interleaving)促进迁移, 提取练习(retrieval practice)优于重读。

具体到 R6 研究伦理与AI治理单元: 刻意练习的 3 个 drill 覆盖 Belmont pydantic schema 化(S1)/三框架并行映射(S2)/红队+天道推演验证(S3), 每个 drill 经历 Worked->Faded->Independent 三阶段; 间隔重复 7 张卡片覆盖 Belmont 三原则/NIST 四步/EU AI Act 四级/garak+PyRIT/天道推演 3 层树/算法偏见/pydantic 评分器, 按 [1,3,8,21,60,180] 天间隔复习; 建构对齐 5 个 ILO 全部有 TLA(含 starter/practice/tutorial)训练与 AT(含 solution/tutorial 后测)测量, mastery 阈值 >=80%; 牛津 tutorial 用静态 if/else 模拟 5 轮 Socratic 追问(为什么/反例/若前提变/凭什么/如何), 配合 Hattie 4 级反馈 [TASK]/[PROCESS]/[SELF-REG]/[FEED-FORWARD] (避免 Self 级表扬), 每单元限频 1 次/天防依赖。

## 研究产出与产业链接层 (v7.0)

本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+linked_paper链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。详见 research.md 与 industry.md。

---

## 学术前沿层 (v9.0)

本单元新增 `frontier.md`：注入 2025-2026 最新学术前沿（N 篇真实 arXiv 论文 + 批判性综述 + delta_to_unit + ≥3 开放研究问题 + 方法论批评）。论文来自 `_frontier_corpus/module-r-research-methodology.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证），覆盖前沿课题：LLM辅助系统综述 × 可复现性危机。面向博后/教授级读者：批判性综述非罗列，delta_to_unit 显式指出前沿如何更新本单元所教，开放问题为可发表研究方向。详见 `frontier.md`。

## AI工程从零构建层 (v11.0)

本单元新增 `from_scratch.md`，把 IRB 风险分级与 NIST RMF 控制项合规从 pydantic/pandas 库调用下沉到 AI工程从零构建的 numpy 数学推导层。scratch_topic：手写 IRB 风险分级模型（Belmont 善行原则的风险-收益加权方程）+ NIST RMF 控制项合规扫描器，对应 rohitg00 P18 Regulatory Frameworks EU US UK Korea（监管框架）+ P18 Model System Dataset Cards（透明度卡片），链接取自 `_from_scratch_map/module-r-research-methodology.md`。core_algorithm 从 Belmont 1979 善行原则出发，推导总风险 $R_{gross}=\sum_i w_i f_i$ 与净风险 $R_{net}=R_{gross}-\lambda\sum_j c_j m_j$（$\lambda$ 控制缓解抵扣），风险分级 minimal/greater/high 由阈值 $\tau_1,\tau_2$ 划定；NIST SP 800-53 控制项加权合规分 $C=\tfrac{\sum_k v_k x_k}{2\sum_k v_k}\in[0,1]$，高临界控制（IA-2 $v=1.2$）fail 时一票否决，把"伦理审查"从 pydantic 枚举字段转成可计算数值模型。code_artifact 手写 numpy（≤50 行，imports 严格白名单），实现 `irb_risk` + `risk_tier` + `nist_compliance`，verification_property 锚定"高风险无缓解=high、低风险全缓解=minimal、NIST 部分合规 non_compliant、全 pass compliant"。connection_to_unit 给出 ≥3 delta：TODO3 pydantic 逐项打分 vs from scratch 加权方程；Belmont 善行操作化为缓解抵扣；NIST 控制项非等权 + 一票否决。exercises 绑定 `starter.ipynb` TODO3（IRB 评分器）与 `practice.md` 伦理审查 drill。rohitg00 深链见 from_scratch.md deep_dive_links 节（ai-engineering-from-scratch 仓库 P18/24 + P18/26）。本层与 v5.0 pydantic/pandas 实现互补：库层教"如何执行伦理审查清单"，from scratch 层教"如何用数学推导审计风险量化与合规加权"--前者是工程底座，后者是方法论底座。
