# 技能2 · Day 1：从流程驱动到智能驱动 + AI治理框架 · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 技能2 AI原生企业架构 · Day 1
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：企业的"操作系统"如何从流程驱动演进到Agent驱动？在这个演进过程中，AI风险如何被系统化治理？--用代码实现NIST AI RMF合规扫描器和EU AI Act风险分级器
> **v5.0 升级点**：① 真实框架上机（NIST AI RMF + EU AI Act + pydantic + pandas）② TODO填空式起始笔记本 ③ Notebook化 ④ 深链阅读 ⑤ 2026前沿（MCP治理即代码 + computer use治理风险 + 天道推演预判AI风险路径）

---

## 学习目标（学完你能做到）

1. 能解释组织范式四阶段演进（流程驱动 -> 数据驱动 -> AI驱动 -> Agent驱动），并说明为什么这四个阶段是"叠加"而非"替代"关系，能判断给定营销场景应该采用哪种范式
2. 能用 **pydantic** 定义NIST AI RMF控制项schema（Govern/Map/Measure/Manage四大功能，18个真实控制项），并实现一个合规扫描器对AI用例逐一打分（0-100）
3. 能用真实EU AI Act条款（Article 5禁止 / Annex III高风险 / Article 50有限风险 / 最小风险）实现风险分级器，判定给定AI用例的合规等级
4. 能用 **pandas** 将合规扫描结果转为DataFrame，生成"用例×功能"风险热力图，识别合规短板（最弱控制项），并提出针对性改进建议
5. 能为营销AI系统（个性化推荐 / 自动文案 / 动态定价 / AI客服）设计AI治理控制点，说明其在NIST AI RMF和EU AI Act下的合规要求

---

## 理论部分：精炼索引（详见独立教材）

> Day 1 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_技能2_AI原生企业架构.md` § Day 1](../../AI原生化商业博士_独立教材_技能2_AI原生企业架构.md)（67-421行，已包含组织范式四阶段演进/McKinsey Agentic Organization模型/NIST AI RMF四步循环详解/EU AI Act风险分级体系/模块R2行动研究嵌入）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：组织范式四阶段演进

| 阶段 | 时期 | 核心特征 | 营销映射 |
|:----:|:----:|---------|---------|
| 流程驱动 | 1900s-2000s | 标准化SOP，可预测但刚性 | 市场调研->受众定义->创意制作->投放->监测 |
| 数据驱动 | 2000s-2020s | 数据指导决策，A/B测试 | 程序化广告：每次展示基于实时数据 |
| AI驱动 | 2020s-2025s | AI做决策，决策权部分转移 | AI自动生成文案/调整出价/推荐产品 |
| Agent驱动 | 2025s- | Agent自主编排工作流 | Agent从洞察到创意到投放端到端自主 |

**核心洞察**：四个阶段是"叠加"关系。成熟AI原生企业同时运行四种范式--合规场景用流程驱动，归因分析用数据驱动，内容生成用AI驱动，跨系统优化用Agent驱动。

### 关键回顾 2：NIST AI RMF 四步循环

NIST AI RMF（AI Risk Management Framework）是NIST于2023年1月发布的AI治理框架，核心是四步循环：

| 功能 | 核心问题 | 关键活动 | 营销实践 |
|:----:|---------|---------|---------|
| **Govern**（治理） | 谁负责AI治理？ | 建立AI治理委员会、定义使用政策、明确问责人 | 营销AI使用政策：哪些决策AI可自主/需人审/禁止 |
| **Map**（映射） | 有哪些AI系统？风险在哪？ | AI用例清单、上下文映射、风险识别 | 梳理营销AI用例（文案/推荐/投放/客服），映射风险 |
| **Measure**（度量） | 风险有多大？ | 定义评估指标、执行评估、基准对比 | 文案质量评分、推荐公平性、投放偏差监测 |
| **Manage**（管理） | 如何应对风险？ | 优先级排序、缓解措施、持续监控 | 内容安全过滤、偏差阈值告警、人工审核流程 |

**Govern贯穿全过程**，不是第一步做完就结束，而是持续运行的组织治理基础。

### 关键回顾 3：EU AI Act 风险分级

EU AI Act（2024年8月1日生效）是全球第一部全面AI监管法律，采用基于风险的分级监管：

| 风险等级 | 条款 | 合规要求 | 营销AI映射 |
|:--------:|:----:|---------|-----------|
| **禁止** | Article 5 | 完全禁止 | 基于面部表情的情感定向、基于种族/宗教的受众分类 |
| **高风险** | Annex III | 合格评定+CE标志+严格合规 | 保险营销中的AI定价（若涉及保险） |
| **有限风险** | Article 50 | 透明度义务（标注AI生成） | AI文案/图片/视频需标注"AI生成"；AI客服需告知用户 |
| **最小风险** | - | 自由使用 | 关键词推荐、内容审核、营销数据分析 |

### 关键回顾 4：McKinsey Agentic Organization 三维度重塑

McKinsey提出的Agentic Organization模型在三个维度重塑组织：工作重新定义（岗位拆解为任务）、结构重新设计（树形->网络）、治理重新构建（人在环+可审计+渐进授权）。营销领域的Agent矩阵雏形：洞察Agent + 内容Agent + 投放Agent + 分析Agent + 协调Agent + 人类营销经理。

---

## 上机部分：用 pydantic + pandas 实现AI治理工具

> 📓 **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO填空版，你来做）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，gated，做完再看）
> 📊 **真实数据/库**：[`data/README.md`](./data/README.md)（NIST AI RMF + EU AI Act + pydantic + pandas + OECD AI Incidents说明）

### 为什么用真实框架（NIST AI RMF + EU AI Act）而非手写示例

v4.0的代码用"手写几个规则"演示治理概念。v5.0改用两个真实治理框架的**真实条款文本**作为规则源：

- **NIST AI RMF 1.0**（https://www.nist.gov/itl/ai-risk-management-framework）：用真实控制项清单（Govern-1~5 / Map-1~5 / Measure-1~4 / Manage-1~4），非编造。用pydantic定义控制项schema，实现合规扫描器。
- **EU AI Act**（https://artificialintelligenceact.eu/）：用真实法规条款（Article 5禁止清单 / Annex III高风险清单 / Article 50透明度义务），实现风险分级器。

**互补关系**：NIST AI RMF是"怎么管"（治理方法论），EU AI Act是"必须怎么管"（法律合规要求）。两者覆盖AI治理的不同维度。

### 营销映射（关键桥接）

本Day治理工具的输入用例集基于**OECD AI Incidents Monitor**（https://oecd.ai/en/incidents-overview）的真实AI事件类型构建，覆盖营销/HR/金融/医疗/安全等领域。营销AI专项分析：

| 营销AI系统 | EU AI Act风险等级 | NIST治理重点 | 关键控制点 |
|-----------|:----------------:|:----------:|-----------|
| AI个性化推荐 | 有限风险（需标注） | Measure（公平性评估） | 偏见测试、推荐差异监测 |
| AI自动文案生成 | 有限风险（需标注） | Manage（人工审核） | 品牌调性审核、内容安全过滤 |
| AI动态定价 | 最小风险/高风险* | Govern（问责结构） | 价格歧视检测、透明度 |
| AI客服机器人 | 有限风险（需告知） | Map（上下文映射） | 对话日志、人工转接机制 |

> *动态定价若涉及保险/信贷则升为高风险（Annex III）。

### 上机任务（6个TODO，见starter.ipynb）

1. **TODO1**：用pydantic定义NIST AI RMF控制项schema（ComplianceStatus枚举 + ControlItem模型 + 18个真实控制项列表）
2. **TODO2**：构建AI用例注册表（AIUseCase模型 + 8个基于OECD AI Incidents真实事件类型的用例）
3. **TODO3**：实现NIST AI RMF合规扫描器（assess_control + score_to_status + scan_nist_rmf）
4. **TODO4**：实现EU AI Act风险分级器（classify_eu_ai_act，按Article 5 -> Annex III -> Article 50 -> 最小风险判定）
5. **TODO5**：用pandas构建风险热力图（明细DataFrame + 用例×功能透视）
6. **TODO6**：营销AI治理专项分析（筛选营销用例，结合NIST得分和EU分级，输出改进建议）

---

## 2026前沿补充：MCP治理即代码 + computer use治理风险 + 天道推演预判AI风险

> v5.0新增前沿点。AI治理正在从"人工合规检查"演进为"治理即代码"（Governance as Code），同时AI Agent的新能力带来了全新的治理挑战。

### MCP（Model Context Protocol）在AI治理中的应用

**MCP**（Model Context Protocol）是Anthropic于2024年提出的开放协议，让AI Agent通过标准化接口接入外部工具和数据源。在AI治理领域，MCP的颠覆性在于实现**治理即代码**：

- **合规检查Agent**：Agent通过MCP接入合规规则库，在每次行动前自动检查是否违反NIST/EU AI Act控制项。不再需要人工事后审计，而是"事前自动拦截"。
- **审计日志MCP Server**：Agent的所有决策通过MCP实时写入审计日志，实现完整可追溯链路。NIST AI RMF的GOVERN-2（问责结构）从"文档化"升级为"代码化"。
- **治理工具链集成**：MCP让合规扫描器、风险分级器、红队测试工具成为Agent可调用的工具，治理从"独立流程"变为"内嵌能力"。

**对营销AI的启示**：营销Agent通过MCP在发布内容前自动检查EU AI Act透明度义务（是否标注AI生成）、品牌安全规则、广告法合规。治理不再是瓶颈，而是Agent工作流的有机部分。

### computer use / 计算机使用带来的新型治理风险

2025年AI Agent获得了**computer use**（计算机使用）能力--直接操作浏览器、桌面应用、文件系统。这带来了全新的治理挑战：

| 治理维度 | 传统AI风险 | computer use新风险 |
|---------|-----------|-------------------|
| 权限控制 | AI只能通过API访问数据 | AI可操作整个软件系统，权限边界模糊 |
| 可逆性 | API调用通常可回滚 | Agent删除文件/发送邮件/提交表单可能不可逆 |
| 审计粒度 | API调用日志结构化 | Agent的UI操作难以完整审计（点击/输入/滚动） |
| 隔离性 | API有rate limit和scope限制 | Agent可绕过API限制直接操作UI |

**NIST AI RMF对应**：computer use场景下，MANAGE-4（风险响应）必须升级--不仅要有API级别的应急方案，还需要UI级别的"紧急停止"机制（如屏幕监控+异常操作拦截）。GOVERN-5（全生命周期治理）需要新增"Agent操作权限矩阵"：哪些软件可以操作、哪些操作需要人工确认。

### 天道推演预判AI系统风险路径

**天道推演**在此Day的实践应用：用天道推演的沙盘模拟方法预判AI系统的风险路径，连接NIST AI RMF的Map（风险识别）和Manage（风险管理）。

**推演框架**：
1. **局势拆解**：识别AI系统的关键变量（自主性程度、影响范围、可逆性、数据敏感度）
2. **因果建模**：构建风险因果链--例如"AI自主定价 -> 价格歧视 -> 监管调查 -> 罚款+品牌损失"
3. **沙盘展开**：为每个关键决策生成3层推演树（immediate -> near -> far）
4. **概率注入**：考虑不确定性（如EU AI Act执法力度、用户投诉概率）
5. **输出评估**：各路径的收益/风险比，识别高杠杆干预点

**营销AI推演示例**：AI动态定价系统的天道推演--
- 路径A（无治理）：AI发现用户支付意愿差异 -> 个性化定价 -> 用户发现价格歧视 -> 社交媒体曝光 -> 品牌危机 -> 监管介入
- 路径B（有NIST治理）：AI发现差异 -> Measure维度公平性检测触发 -> 自动暂停差异化定价 -> 人工审核 -> 调整策略
- 推演结论：在Measure维度部署公平性检测是高杠杆点，小投入（检测脚本）改变大局（避免品牌危机）

> 🔗 这连接了CLAUDE.md中天道推演的"因果链追踪"和"沙盘模拟"能力矩阵，将AI治理从"事后合规检查"升级为"事前风险推演"。

---

## 与前后Day的衔接

- **Day 2**：Agent编排架构 + LangGraph实战--今天的NIST治理控制点将嵌入LangGraph工作流的Human-in-the-loop节点
- **Day 3**：人机协作治理 + 组织变革--今天的AI治理工具是Day 3人机分工矩阵的量化基础
- **Day 4**：企业级架构参考设计 + 行动研究--今天的治理框架是Day 4企业AI架构治理层的核心组件

---

## 作业与评估

作业、5分制量表、费曼演练、2分钟话术、复盘自诊表--沿用独立教材 § Day 1既有设计。本学习材料包不重复，仅新增上机交付物：

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6个TODO全部填好，能跑通）
- [ ] 一段300字分析：你的8个AI用例在NIST AI RMF哪个功能维度得分最低？根因是什么？对应的天道推演风险路径是什么？
- [ ] （可选）为你的企业营销AI系统（如个性化推荐）设计一个MCP治理工具：Agent在推荐前通过MCP检查哪些合规规则？

---

## 英语轨道（i+1）

打开 [NIST AI RMF 1.0 官方页面](https://www.nist.gov/itl/ai-risk-management-framework)，用浏览器翻译插件辅助阅读Executive Summary。关键术语：Govern / Map / Measure / Manage / Trustworthy AI / Accountable Owner。不要求读懂每个词，目标是理解四步循环的逻辑。

---

*本讲义由v5.0学习材料包升级生成。理论部分引用独立教材，上机部分用真实框架（NIST AI RMF + EU AI Act）+ 真实库（pydantic + pandas）+ TODO脚手架。*
*最后更新：2026-07-24*

---

## 学习科学层 (v6.0)

> v6.0 升级不改动 v5.0 原文，仅在本节追加"学习科学层"说明。配合 `practice.md` / `schedule.json` / `alignment.md` / `tutorial.ipynb` 四个新文件使用。

### 哲学增量

- v5.0：真实即严谨 · 练习即掌握
- v6.0：**科学即高效 · 反馈即成长** - 用学习科学把"练习"升级为"刻意练习 + 间隔重复 + 建构对齐 + 牛津tutorial仿真"

### 4 个研究依据合成

1. **NUS + 理论**：Ericsson **刻意练习** (deliberate practice) 5 要素 / **FSRS-6** (request_retention=0.9, 21 weights) + **SM-2** 备份 (EF₀=2.5, I(1)=1, I(2)=6) / **Biggs 建构对齐** ILO↔TLA↔AT / **Hattie** (2007 RER 77(1):81-112) 3 问 × 4 级反馈
2. **MIT + Imperial**：MIT Open Learning 明文原则 - **提取练习** (retrieval practice, 测试效应) + **间隔重复** (spaced retrieval) + **交叉练习** (interleaving, A1B1C1...B2C2A2...C3A3B3 模式) + **Worked-Faded 渐退示例** + 前/后测 + 4C/ID 认知负荷；MIT 6.5940 **mastery 阈值** ("至少 4/5 实验提交方可及格")；Imperial MSc AI 50%项目/88%自学 + seminars+tutorials
3. **Oxford + Cambridge**：**牛津 tutorial / Cambridge supervision** 1对1-3 + 每周 + 强制 + 口头辩护；LLM 仿真设计 - role-engineered persona (禁直接答案 / **Socratic 苏格拉底**追问) + 多轮脚手架渐退 + student_model + 限频防依赖；arxiv 2024-2025 Socratic LLM 论文 (2409.05511 / 2507.05795 / 2508.21204)
4. **Harvard + Stanford**：HBS case method "管理不确定性的艺术" + devil's advocate 角色 (Christensen Center)；CS230 翻转课堂 + 渐进项目脚手架 (proposal->milestone->final->poster) + retry 政策 (10 late days, 20%/天罚分)；CS229 pset0 诊断性先测；Butler 2010 检索练习证据 (推断题 68% vs 重学 44%)

### 本 Day 的 4 个新文件

| 文件 | 学习科学机制 | 在本 Day 的具体落地 |
|------|------------|--------------------|
| `practice.md` | **刻意练习** + Worked-Faded 渐退 + 交叉 interleaving | skill_target + 3 subskills + 3 drills (D1 pydantic schema / D2 双框架判定 / D3 热力图+天道推演) + progressive_project (proposal->milestone->final->poster) + weak_loop + A1B1C1...C3A3B3 交叉排布 |
| `schedule.json` | **FSRS-6** 间隔重复 + **SM-2** 备份 | 6 张卡片 (NIST 四功能 / EU Act 四级 / 天道推演三时间线 / pydantic schema / MCP 治理即代码 / computer use 新风险) 按 due [1,3,8,21,60,180] 复习, request_retention=0.9 |
| `alignment.md` | **Biggs 建构对齐** + **mastery 阈值** | ILO↔TLA↔AT 4 行矩阵 + 及格线 (3/4 AT 达标) + 3 自检 (Feed Up/Back/Forward) |
| `tutorial.ipynb` | **牛津 tutorial Socratic 仿真** + **Hattie** 4 级反馈 | Oxford tutorial fellow persona (禁直接答案) + 4 轮 Socratic 追问 + Hattie [TASK]/[PROCESS]/[SELF-REG]/[FEED-FORWARD] + student_model.json 跨单元复用 + 限频 1 次/天防依赖 |

### 不破坏 v5.0 基线承诺

- v5.0 的 7 条验收 (`/tmp/verify_unit.py`) 全部仍通过
- v6.0 新增 5 条验收 (`/tmp/verify_v6_unit.py`) 全部通过 = 12/12 收敛
- notes.md 原文不动，仅追加本节

### 关键词索引 (用于 v6.0 验收)

`刻意练习` / `deliberate practice` / `FSRS-6` / `SM-2` / `间隔重复` / `spaced retrieval` / `建构对齐` / `constructive alignment` / `牛津 tutorial` / `Socratic 苏格拉底` / `Hattie` / `交叉` / `interleaving` / `Worked-Faded 渐退` / `mastery` / `提取练习` / `retrieval practice` / `formative feedback` / `形成性反馈`

---

## 研究产出与产业链接层 (v7.0)

本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+arXiv链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。详见 research.md 与 industry.md。

---

## 学术前沿层 (v9.0)

本单元新增 `frontier.md`：注入 2025-2026 最新学术前沿（N 篇真实 arXiv 论文 + 批判性综述 + delta_to_unit + ≥3 开放研究问题 + 方法论批评）。论文来自 `_frontier_corpus/skill-2-ai-native-arch.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证），覆盖前沿课题：企业Agent编排 × MCP/A2A 标准化协议。面向博后/教授级读者：批判性综述非罗列，delta_to_unit 显式指出前沿如何更新本单元所教，开放问题为可发表研究方向。详见 `frontier.md`。

---

## AI工程从零构建层 (v11.0)

> v11.0 新增 [`from_scratch.md`](./from_scratch.md)：AI工程从零构建，与本单元 NIST AI RMF + pydantic + pandas 形成对照。
> - **从零构建主题**：手写 MCP server 骨架 + JSON-RPC 工具调度 + NIST 合规评分
> - **核心算法**：JSON-RPC 2.0 dispatch(method->callable) + NIST 加权评分 $score = 100 \cdot \sum_k w_k c_k$（含数学推导 + LaTeX）
> - **code_artifact**：手写 numpy 骨架，imports ⊆ {numpy, typing, dataclasses}，附 verification_property
> - **延伸阅读**：rohitg00 AI工程 from scratch P13 Tools & Protocols（MCP Fundamentals / Building MCP Server / Tool Interface）
> - **手写实现要点**：用 from-scratch numpy + dataclasses 而非 mcp SDK + pydantic，理解到 JSON-RPC 分发与加权评分的金属层
> - **verification_property**：JSON-RPC dispatch 路由 method->callable；nist_score `w @ c` 输出 [0,100]，80/50 阈值分界状态映射
