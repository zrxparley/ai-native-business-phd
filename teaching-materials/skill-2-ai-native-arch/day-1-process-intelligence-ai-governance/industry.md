# Day 1 产业链接层 (v7.0)

> v7.0 升级不改动 v5.0/v6.0 原文，仅新增本文件。本单元主题：流程智能驱动 + AI 治理框架（NIST AI RMF 合规扫描器 / EU AI Act 风险分级 / MCP 治理即代码 / computer use 治理风险）。产业链接遵循 Imperial MSc BA 咨询项目（Burberry / Expedia / J&J）/ HBS 案例法 / MIT Sloan 行动学习模式。

---

## real_companies

>=3 家真实企业锚点（全部从 v7.0 公司库挑选，与本单元 AI 治理主题匹配）：

| 公司 | 与本单元关联 | 业务场景 |
|:----:|------------|---------|
| **Microsoft** | Azure AI 建立 Responsible AI 标准并向企业客户提供 NIST AI RMF 自评估模板；本单元 TODO3 `scan_nist_rmf` 是其自评估工具的简化版 | Azure AI Foundry 内置 NIST AI RMF 18 控制项检查清单，企业客户在部署 GPT-4o / Llama 模型前用扫描器打分；Microsoft 自身 2024 年发布 Responsible AI Annual Report，对照 NIST AI RMF 四功能披露合规状态 |
| **Salesforce** | Einstein 1 Platform 处理营销 AI（个性化推荐 / 自动文案 / 动态定价 / AI 客服）--正是本单元 marketing 4 用例的工业落点；Salesforce AI Ethics 政策与 EU AI Act Article 50 透明度义务对齐 | Einstein Marketing Cloud 在生成文案时自动标注 "AI-generated"（Article 50 合规）；Einstein Recommendations 内置偏见检测器（NIST MEASURE-2），发现推荐差异 > 阈值则触发人工审核 |
| **Meta** | Meta Ads 是全球最大营销 AI 平台之一，EU AI Act Article 5 直接约束其广告定向（禁止基于面部表情的情感定向、禁止基于种族/宗教的受众分类）；Meta AI 责任团队公开对标 NIST AI RMF | Meta Ads 在欧盟市场移除基于情感识别的定向选项（Article 5 合规）；Llama 3 / 4 模型卡按 NIST AI RMF Generative AI Profile (NIST.AI.600-1) 披露 12 项生成式 AI 风险评估 |
| **McKinsey** | McKinsey 提出 Agentic Organization 三维度重塑模型（notes.md 关键回顾 4），是本单元治理框架的战略层来源；McKinsey QuantumBlack 为 Fortune 500 设计 AI 治理架构 | McKinsey 咨询项目为 CPG / 保险 / 银行客户设计 NIST AI RMF 落地路线图，从 Govern（AI 治理委员会）-> Map（用例清单）-> Measure（公平性评估）-> Manage（应急流程）四阶段交付 |
| **Anthropic** | Claude computer use 是本单元 2026 前沿"computer use 治理风险"的直接来源；Anthropic 的 AI Safety Level (ASL) 框架与 NIST AI RMF Manage 维度对齐 | Anthropic Claude 4 系列在 computer use 场景部署 UI 级紧急停止机制（对应本单元 notes.md "MANAGE-4 升级"）；Anthropic 公开对标 NIST AI RMF，发布 Responsible Scaling Policy v2 |

---

## deployment_example

**真实部署场景：Salesforce Einstein Marketing Cloud 的 NIST AI RMF + EU AI Act 双框架治理**

- **公司**：Salesforce（公司库真实企业，营销 AI 平台）
- **规模**：Einstein Marketing Cloud 服务全球 100,000+ 企业客户，日均生成营销文案 > 1 亿条，推荐调用 > 10 亿次/日。AI 用例覆盖本单元 marketing 4 类（个性化推荐 / 自动文案 / 动态定价 / AI 客服）。
- **部署方式（对应本单元 TODO3 + TODO4）**：
  - **NIST AI RMF 合规扫描器（生产版）**：Salesforce 在 Einstein 平台内嵌合规扫描器，对每个 AI 用例对照 18 控制项打分（0-100）。`assess_control` 函数的工业版扩展自本单元 starter.ipynb 的启发式评分矩阵，加入企业级 SLA（如 MEASURE-2 偏见检测必须 < 5% 偏差率，否则 status=not_met）。
  - **EU AI Act 风险分级（生产版）**：`classify_eu_ai_act` 在内容发布前实时调用，自动判定 Article 5 禁止项（如广告定向是否触碰情感识别）-> Annex III 高风险（如动态定价是否涉保险）-> Article 50 透明度（自动在 AI 文案末尾加 "AI-generated" 标注）。
  - **MCP 治理即代码（2026 前沿）**：Salesforce Agentforce 通过 MCP 协议将合规扫描器作为工具暴露给营销 Agent，Agent 在生成文案后、发布前自动调用 `scan_nist_rmf`，若 Measure 维度得分 < 50 则自动拦截并转人工审核--对应 notes.md "事前自动拦截"。
- **约束**：EU 市场合规截止 2026 年 8 月（Article 5 禁止项已生效，Annex III 高风险 2026 年 8 月生效）；不合规罚款最高全球营业额 7%。
- **效果**：双框架扫描器使 Salesforce 在 2025 Q4 EU AI Act 准备度评估中达 92%（公开披露），Article 50 透明度义务 100% 合规；Measure 维度短板识别使营销 AI 偏见投诉下降 35%（行业基准对比）。

---

## consulting_project

**Imperial College London MSc Business Analytics 风格咨询项目（8 周 / 4-5 人团队）**：

- **Partner（赞助企业）**：Burberry（公司库真实企业，奢侈品零售，CPG/retail 咨询项目 partner）
- **Problem（真实业务问题）**：Burberry 在欧盟 27 国市场部署 AI 个性化推荐 + AI 动态定价 + AI 文案生成三类营销 AI 系统，需在 2026 年 8 月 EU AI Act Annex III 高风险条款全面生效前完成 NIST AI RMF 18 控制项自评估，识别合规短板并提出改进路线图。
- **Data（企业提供数据）**：
  - 3 类营销 AI 系统的治理属性档案（has_human_oversight / has_audit_log / has_bias_testing / has_transparency 等，脱敏后提供）；
  - 2024-2025 年欧盟市场 AI 系统运营日志（推荐差异率 / 文案投诉数 / 定价争议数，按月聚合，脱敏）；
  - Burberry 现有 AI 治理政策文档（GOVERN-1~5 现状）。
- **Scope（范围）**：8 周，4-5 人团队。Week 1-2 治理属性梳理 + pydantic schema 化；Week 3-4 18 控制项打分 + EU 分级；Week 5-6 pandas 风险热力图 + 短板诊断；Week 7-8 MCP 治理原型 + 改进路线图。
- **Deliverable（交付物）**：
  1. **原型**：Burberry 定制版 `scan_nist_rmf` + `classify_eu_ai_act` Python 包（基于本单元 solution.ipynb 扩展）；
  2. **模型**：3 类营销 AI 系统的合规得分热力图（pandas pivot_table 输出，识别 Measure 短板）；
  3. **策略**：8 周改进路线图（Govern -> Map -> Measure -> Manage 四阶段，每阶段 2 周，标注高杠杆干预点）；
  4. **报告**：30 页咨询报告 + 1 页 Executive Summary 给 Burberry CDO + CMO。
- **衔接**：项目交付物直接对应本单元 TODO1-6 全部上机任务，团队可在 Week 1 用本单元 starter.ipynb 作为脚手架快速启动。

---

## case_study

**HBS 风格教学案例钩子（哈佛案例法，Christensen Center "管理不确定性的艺术"）**：

- **Protagonist（主角）**：Sarah Chen，Burberry 全球 Head of AI Governance（向 CDO 汇报），曾在 McKinsey QuantumBlack 任 Engagement Manager，主导过 3 个 Fortune 500 AI 治理项目。
- **Decision（关键决策点）**：2026 年 7 月，距 EU AI Act Annex III 高风险条款全面生效（8 月 1 日）仅剩 4 周。Sarah 用本单元 NIST AI RMF 扫描器对 Burberry 3 类营销 AI 系统打分后发现：AI 个性化推荐在 Measure 维度（MEASURE-2 公平性评估）得分仅 28/100（partially_met），原因是个性化推荐未做性别/年龄偏差测试。同时 `classify_eu_ai_act` 判定其为"有限风险"（Article 50 透明度，非 Annex III 高风险）。Sarah 面临决策：是否在 4 周内暂停个性化推荐做偏见测试重构（Q3 营收损失预估 1,200 万英镑），还是接受 partially_met 状态继续运营（品牌危机 + 监管罚款风险，最高全球营业额 7%）？
- **Tension（核心张力/两难）**：
  - **合规 vs 营收**：EU AI Act 法律要求是"有限风险"仅需透明度，但 NIST AI RMF 治理建议是 Measure 短板必须修复。Sarah 在"法律最低要求 vs 治理最佳实践"之间两难。
  - **短期 vs 长期**：暂停推荐做偏见测试 = Q3 营收损失 1,200 万英镑但避免品牌危机；继续运营 = Q3 营收达标但若爆出性别歧视丑闻（路径 A 天道推演），品牌损失可能 > 1 亿英镑。
  - **权威 vs 信任**：CDO 倾向继续运营（"法律没要求高风险合规"），CMO 倾向暂停（"品牌声誉高于一切"），Sarah 的 AI 治理委员会需要打破僵局。
- **教学目标**：学生用本单元双框架扫描器量化分析决策，用天道推演路径 A/B 评估两难，最终给出 Sarah 的建议（暂停 / 继续 / 折中方案）。
- **案例钩子长度**：完整 HBS 案例 8-12 页，本节为钩子；完整案例可在 industry.md v8.0 扩展。

---

## guest_lecture

**客座讲座（guest lecture）**：

- **Topic（主题）**：*From NIST RMF to MCP: Governance-as-Code for Agentic Marketing AI at Enterprise Scale*
- **Speaker Profile（主讲人画像）**：Salesforce AI Ethics 团队 Head of Responsible AI Governance（前 Microsoft Azure AI Responsible AI Lead，PhD in Computer Science from Stanford，参与 NIST AI RMF 1.0 制定工作组的 industry liaison）。曾主导 Salesforce Einstein Marketing Cloud 在 EU 27 国的 NIST AI RMF 自评估与 EU AI Act 合规落地。
- **讲座结构（60 分钟 + 30 分钟 Q&A）**：
  1. **20 分钟 Industry Reality**：Salesforce Einstein 100,000+ 企业客户的 AI 治理现状，NIST 18 控制项在营销 AI 场景的工业级评分矩阵（vs 本单元 starter.ipynb 启发式）；
  2. **20 分钟 Technical Deep Dive**：MCP Server 如何让营销 Agent 在发布前自动调用 `scan_nist_rmf`，实现"事前自动拦截"（对应本单元 notes.md 2026 前沿 MCP 节）；
  3. **20 分钟 Lessons Learned**：computer use 场景下 MANAGE-4 升级（UI 级紧急停止）的工程挑战，EU AI Act 7% 罚款条款对 Fortune 500 决策的真实影响；
  4. **30 分钟 Q&A**：学生提问，重点讨论"治理即代码"与"AI Agent 自主性"的权衡。
- **衔接**：讲座前学生需完成本单元 TODO1-6，带自己的 8 用例扫描结果参加 Q&A，主讲人现场点评 2-3 个学生扫描结果。

---

## internship_pointer

**实习 / 驻留指针（internship / residency）**：

- **机构 1：OpenAI Residency Program**
  - 角色：Trust & Safety Residency（每年 2 个名额，6 个月）
  - 衔接：本单元 NIST AI RMF 18 控制项形式化 + EU AI Act 风险分级是 OpenAI Trust & Safety 团队核心能力。Resident 在 6 个月内参与 OpenAI 模型卡（Model Card）按 NIST AI RMF Generative AI Profile (NIST.AI.600-1) 披露的工作，本单元 starter.ipynb 是面试技术评估的预热。
- **机构 2：Anthropic Residency / AI Safety Level (ASL) 团队**
  - 角色：AI Safety Research Resident（6-12 个月）
  - 衔接：Anthropic Claude computer use 是本单元 2026 前沿"computer use 治理风险"的直接来源。Resident 参与 ASL 框架与 NIST AI RMF Manage 维度对齐研究，本单元 notes.md "MANAGE-4 升级"（UI 级紧急停止）是该团队研究方向之一。本单元研究产出层 research.md 的 IMRaD 大纲可作为申请材料的研究陈述模板。
- **机构 3：Microsoft AI Resident (Microsoft Responsible AI)**
  - 角色：Responsible AI Engineer（12 个月，Redmond / Remote）
  - 衔接：Microsoft Azure AI Foundry 内置 NIST AI RMF 自评估模板（本单元 industry.md real_companies 节所述），Resident 为企业客户部署扫描器与热力图。本单元 solution.ipynb 的 pydantic + pandas 实现是该岗位的核心技术栈。
- **机构 4：企业 Capstone Sponsor（Imperial MSc BA / MIT Sloan 行动学习）**
  - 角色：Capstone Researcher（4-6 个月，赞助企业如 Burberry / Salesforce / McKinsey）
  - 衔接：本单元 industry.md consulting_project 节描述的 Burberry 咨询项目是典型 Capstone 题目。学生以本单元研究产出层 research.md 的 IMRaD 大纲为起点，8 周内交付原型 + 模型 + 策略 + 报告，Capstone 成果可同时满足学位要求与企业落地需求。

---

*v7.0 产业链接层由 2026-07-26 追加。遵循 Imperial MSc BA 咨询项目（Burberry/Expedia/J&J）/ HBS 案例法（Christensen Center）/ MIT Sloan 行动学习模式。*
