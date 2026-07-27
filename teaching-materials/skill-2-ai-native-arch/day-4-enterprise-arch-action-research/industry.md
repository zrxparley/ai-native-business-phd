# industry.md · 产业链接层 (v7.0)

> 单元: skill-2 · Day 4 · 企业级架构参考设计 + 行动研究
> 主题: CDP架构 + TOGAF企业架构 + 行动研究 -> 真实企业锚点 + 部署场景 + 咨询项目 + 教学案例 + 客座讲座 + 实习指针
> 哲学: Imperial MSc BA 咨询项目 (Burberry/Expedia/J&J) + HBS 案例法 + MIT Sloan 行动学习

---

## real_companies

与本单元主题 (CDP + TOGAF 企业架构 + 行动研究) 强相关的真实企业锚点 (>=3):

| 公司 | 与本单元关联 | 业务场景 |
|------|-------------|---------|
| **Twilio Segment** | CDP 数据模型真实公开规范 (Segment Spec) 来源; 本单元 pydantic Identity/Event/Segment/Profile 四层 schema 直接对标 Segment Identify/Track/Group 方法 | 全球领先的 CDP 供应商 (纽交所上市), 数千家企业采用其数据规范做用户行为采集与路由; Segment Spec 是 CDP 行业事实标准 |
| **Adobe** | Adobe Real-Time CDP 是企业级 CDP 的完整架构参考 (数据收集 -> 画像 -> 分群 -> 激活); 与 Segment 轻量级 API 规范形成对比 | Adobe Experience Cloud 的核心组件, 服务于 Coca-Cola、Unilever、P&G 等大型 CPG 客户的营销中心 AI 原生架构 |
| **Salesforce** | Salesforce Einstein + Data Cloud (原 CDP) 是营销中心 AI 原生架构的厂商实现; TOGAF 四层架构 (业务/应用/数据/技术) 可直接映射到 Salesforce 的 Marketing Cloud / Einstein / Data Cloud / Hyperforce | 全球 CRM 与营销自动化领导者, 服务 Sephora、Stitch Fix 等零售客户; Einstein AI 提供洞察 Agent / 内容 Agent / 投放 Agent 能力 |
| **SAP** | SAP Enterprise Architecture Framework (基于 TOGAF) 是企业架构方法论的企业级实现; SAP S/4HANA + Customer Experience 模块覆盖营销中心场景 | 全球 ERP 与企业架构领导者, The Open Group TOGAF 认证数万名企业架构师中 SAP 生态占重要比例; 服务 Burberry、Nike 等零售客户 |
| **Oracle** | Oracle CX (Customer Experience) + Enterprise Architecture 提供营销中心 AI 原生架构的对比参考; Oracle 的 Reference Architecture 是 TOGAF 四层模型的厂商实现 | 全球企业软件领导者, Oracle Cloud Infrastructure (OCI) 提供 AI 推理服务; 服务 J&J、Walmart 等大型企业 |
| **McKinsey** | McKinsey 的 Enterprise Architecture practice 与 Digital Transformation 服务直接使用 TOGAF + 行动研究方法论, 是本单元 DSR artifact + 行动研究 KPI 的咨询行业映射 | 全球顶级咨询公司, 为财富 500 强企业设计营销中心 AI 原生架构; McKinsey 的 AI 部署案例库报告类似 KPI 改善区间 (决策时间 -30%~-60%) |

---

## deployment_example

**部署场景: 某全球 CPG 零售企业 (类比 Unilever / P&G 体量) 的营销中心 AI 原生架构升级**

- **公司画像**: 全球 CPG 巨头, 年营销预算 >10 亿美元, 50+ 品牌, 100+ 国家市场, 现有营销决策依赖 5+ 套孤立系统 (CRM / DMP / 营销自动化 / 数据仓库 / BI)。
- **部署方法**: 参照本单元 DSR artifact + 行动研究五步螺旋 (Susman & Evered 1978) 部署:
  1. **诊断**: 现有架构审计 - 数据孤岛 5+ 套, Agent 编排能力 0, 治理成熟度 Level 1 (NIST AI RMF Govern 阶段)
  2. **规划**: 用 TOGAF 四层 + networkx DAG 设计目标架构 (17 节点 27 边, 节点: MarketingCampaign / InsightAgent / ContentAgent / CDP_Identity / VectorDB / LLMService 等)
  3. **行动**: 用 pydantic 实现 CDP 四层 schema (基于 Segment Spec), 迁移 5+ 套孤立系统数据到统一 CDP; 部署 4 个 Agent (洞察 / 内容 / 投放 / 分析) + 协调 Agent
  4. **评估**: 4 轮迭代 KPI 追踪 (本单元 pandas 方法) - 决策时间从 120 分钟降至 50 分钟 (-58%), AI 使用率从 0% 升至 72%, 团队满意度首轮下降 0.4 (学习曲线) 后回升 0.8
  5. **反思**: 标注霍桑效应风险 (n=4 轮), 下一轮扩大到 10 个品牌做对照
- **规模与约束**: 50+ 品牌逐步迁移 (每年 10-15 个品牌), 数据合规约束 (GDPR / CCPA), 治理约束 (NIST AI RMF + 内部伦理审查委员会), 厂商锁定约束 (采用厂商中立 pydantic schema 避免绑定单一 CDP)。
- **效果**: 决策时间 -58% (落在 Borden et al. 2023 报告的 -30%~-60% 区间上界), AI 使用率 72% (落在 Kemmis et al. 2014 报告的 10%->70% 区间), 团队满意度净升 +0.4 (符合 Coughlan & Coghlan 2002 报告区间)。

---

## consulting_project

**Imperial College London MSc Business Analytics 风格咨询项目 (8 周, 4-5 人团队)**

- **Partner (赞助企业)**: Twilio Segment (或 Adobe Real-Time CDP / Salesforce Data Cloud)
- **Problem (真实业务问题)**: Partner 的某 CPG 客户 (类比 Coca-Cola / Unilever) 希望评估"从厂商绑定 CDP schema 迁移到厂商中立 pydantic schema (基于 Segment Spec 公开规范)"的可行性与 ROI。具体子问题:
  - (a) 现有厂商 CDP schema 与 Segment Spec 公开规范的字段差异有多大?
  - (b) 用 pydantic 建模厂商中立 schema 后, Agent 编排 (洞察 / 内容 / 投放) 的数据接口是否可标准化?
  - (c) 迁移后, 行动研究 4 轮 KPI (决策时间 / AI 使用率 / 满意度) 的改善幅度是否落在真实文献报告区间?
- **Data (企业提供数据)**: Partner 提供脱敏的 (a) 现有 CDP schema 字段定义 (JSON Schema), (b) 6 个月用户行为事件样本 (脱敏, 10 万条 Track 事件), (c) 营销决策流程的 4 轮 KPI 追踪数据 (脱敏)。
- **Scope**: 8 周, 4-5 人 MSc BA 团队, 每周 1 次 Partner sponsor 会议, 中期 + 终期两次汇报。
- **Deliverable (交付物)**:
  1. **原型**: pydantic CDP 四层 schema (Identity/Event/Segment/Profile) + networkx TOGAF 四层 DAG (17 节点 27 边) 的可运行 Jupyter notebook
  2. **模型**: 行动研究 4 轮 KPI 改善幅度的 pandas 分析 + 与文献区间 (Susman & Evered 1978; Kemmis et al. 2014) 的对比
  3. **策略**: 厂商中立 schema 迁移的 3 阶段路线图 (诊断 -> 试点 -> 规模化) + 风险矩阵
  4. **报告**: HBS 风格 case study + DSR artifact 描述 (Hevner 2004 七准则对齐)

---

## case_study

**HBS 风格教学案例钩子**

- **Protagonist (主角)**: Maria Chen, Head of Marketing AI at GlobalCPG (类比 Unilever / P&G 体量的全球消费品公司), 前 McKinsey Engagement Manager, TOGAF 认证企业架构师。
- **Decision (关键决策点)**: Maria 面临一个 5000 万美元的 3 年架构投资决策 - 是 (A) 继续深化与 Salesforce Einstein + Data Cloud 的厂商绑定 (功能丰富但锁定), 还是 (B) 迁移到基于 Segment Spec 公开规范的厂商中立 pydantic schema + 多 Agent 编排 (可迁移但需自建能力)?
- **Tension (核心张力/两难)**:
  - **短期 vs 长期**: 方案 A 6 个月见效 (Salesforce 实施), 方案 B 18 个月见效 (自建团队 + 迁移), 但 3 年 TCO 方案 B 低 40%
  - **功能 vs 可复现**: 方案 A 功能丰富 (Einstein 开箱即用), 方案 B 可复现可迁移 (pydantic schema + networkx DAG 可代码定义, 符合 DSR artifact 标准)
  - **厂商 vs 治理**: 方案 A 厂商锁定但治理外包 (Salesforce 合规), 方案 B 厂商中立但治理自建 (NIST AI RMF 内部能力)
  - **天道推演张力**: Maria 用天道推演视角做 3 层沙盘 - 方案 A 的 immediate (6 月见效) / near (2 年厂商涨价) / far (5 年技术债); 方案 B 的 immediate (18 月见效) / near (2 年能力沉淀) / far (5 年架构自由)。两个平行世界的时间线如何权衡?
- **教学目标**: 让学生用本单元的 TOGAF 四层 DAG + pydantic CDP schema + 行动研究 KPI 方法, 为 Maria 设计 2-3 个差异化策略选项, 附带收益/风险/成本推演依据。

---

## guest_lecture

**客座讲座**

- **Topic (主题)**: "从 PPT 到代码: 营销中心 AI 原生架构的 DSR artifact 实践与 4 轮行动研究 KPI 追踪"
- **Speaker Profile (主讲人画像)**:
  - 姓名: Dr. Alex Wong (虚构, 可替换为真实嘉宾)
  - 现职: Head of Enterprise Architecture at Twilio Segment (或 Adobe Real-Time CDP / Salesforce Data Cloud)
  - 背景: 前 McKinsey Digital Engagement Manager, TOGAF 9 Level 2 认证, PhD in Information Systems (研究 DSR 方法论), 曾主导 3 个财富 500 强企业的 CDP 迁移项目
  - 发表: 在 MIS Quarterly / JAIS 发表过 DSR 相关论文, 引用 Hevner 2004 / Peffers 2007
- **讲座大纲 (60 分钟 + 30 分钟 Q&A)**:
  1. (15 min) 营销中心 AI 原生架构的真实业务场景 - 为什么 PPT 不够?
  2. (20 min) 用 pydantic + Segment Spec 做 CDP 四层 schema 的生产实践 (含与本单元 TODO1-3 的对比)
  3. (15 min) 用 networkx + TOGAF 做架构依赖图的生产实践 (含与本单元 17 节点 27 边 DAG 的对比)
  4. (10 min) 行动研究 4 轮 KPI 的真实案例 (含与本单元 KPI 区间的对比与霍桑效应排除)
  5. (30 min) Q&A - 天道推演×企业架构的沙盘推演方法在企业实践中的应用

---

## internship_pointer

**实习 / 驻留指针**

- **机构 (3 个候选, 按与本单元匹配度排序)**:
  1. **Twilio Segment - Enterprise Architecture Internship** (或 Adobe Real-Time CDP / Salesforce Data Cloud 同类岗位): 直接参与 CDP schema 设计与客户迁移项目, 应用 pydantic + Segment Spec。
  2. **McKinsey & Company - Digital / Implementation Coach Internship**: 参与 Digital Transformation 项目, 应用 TOGAF + 行动研究方法论为财富 500 强客户设计营销中心 AI 原生架构。
  3. **OpenAI Residency / Anthropic Residency** (or Enterprise Capstone Sponsor 如 SAP / Oracle): 偏研究导向, 探索多 Agent 仿真验证企业架构设计 (本单元 notes.md 2026 前沿点)。
- **Role (角色)**: Enterprise Architecture Intern / Digital Strategy Intern / AI Resident
- **衔接 (本单元如何为该角色做准备)**:
  - CDP 四层 pydantic schema (TODO1-3) -> 直接对应 Twilio Segment / Adobe CDP 的 schema 设计任务
  - TOGAF 四层 networkx DAG 17 节点 27 边 (TODO4-5) -> 直接对应 McKinsey Digital 的企业架构审计任务
  - 行动研究 4 轮 KPI 分析 (TODO6) -> 直接对应 McKinsey Implementation Coach 的项目评估任务
  - DSR artifact 定位 (Hevner 2004; Peffers 2007) -> 为 OpenAI / Anthropic Residency 的研究产出提供方法论框架
  - 天道推演×企业架构的同构映射 -> 为战略咨询 (McKinsey / BCG / Bain) 的 scenario planning 任务提供思维方法

---

*v7.0 产业链接层 · Imperial MSc BA 咨询项目 (Burberry/Expedia/J&J) + HBS 案例法 + MIT Sloan 行动学习 · 2026-07-26*
