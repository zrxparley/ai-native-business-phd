# 产业链接层 (v7.0) · 人机协作治理 + 组织变革

> 本单元 v5.0/v6.0 已覆盖理论（McKinsey 7S + ADKAR + 天道推演）与上机（pandas + networkx + matplotlib）。v7.0 加产业链接：>=3 真实企业锚点 + 部署场景 + Imperial MSc BA 咨询项目 + HBS 教学案例钩子 + 客座讲座 + 实习指针。所有企业从公司库挑选，全部真实存在，与本单元主题（人机协作治理 + 组织变革）匹配。

---

## real_companies

> 从公司库挑 >=3 家真实企业锚点（企业架构/咨询领域 + AI Agent 部署领域）。

| 公司 | 与本单元关联 | 业务场景 |
|------|------------|---------|
| **McKinsey** | 提出 "Agentic Organization" 概念（Agent 成为组织一等成员），本单元 networkx 组织网络分析的源头理论；McKinsey 7S 框架（Tom Peters & Robert Waterman, 1980s）是本单元 TODO4 的核心评估工具 | McKinsey 内部部署 Lilli（内部 GenAI 助手）服务 4 万+ 咨询师，重构咨询师-Agent 协作网络；外部为客户提供 Agentic Organization 设计咨询 |
| **BCG** | MIT Sloan × BCG "AI Spring 2024" 联合研究提出"试点陷阱"（仅 10% 企业从试点到规模化），本单元研究问题的"被解释现象"；BCG X 是 BCG 的 AI 技术构建部门 | BCG X 为全球客户构建 GenAI 应用 + AI 治理体系；BCG 内部用 AI Agent 辅助咨询师做行业研究、数据分析、slide 制作，审计日志记录人机协作过程 |
| **Deloitte** | Deloitte AI Institute 与本单元 AI 治理四要素（数据/模型/流程/人员治理）高度对齐；Deloitte 的 Trustworthy AI 框架对应 NIST AI RMF 的 Govern 功能 | Deloitte 为财富 500 强企业提供 AI 治理成熟度评估 + AI 伦理委员会设计 + 变革管理咨询；其 AI 治理审计方法论直接用审计日志作为合规证据 |
| **Accenture** | Accenture 的 "Responsible AI" 实践与 ADKAR 变革管理结合，为企业提供 AI 导入后的组织变革咨询；本单元 TODO5 ADKAR 诊断 + 天道推演阻力扩散仿真 | Accenture 内部 70 万员工大规模 AI Agent 部署，自身即"Agentic Organization"试验场；外部为客户提供 AI 变革管理 as a service |
| **IBM** | IBM 是 NIST AI RMF 早期贡献者；IBM AI Ethics Board 模式是本单元 AI 伦理委员会设计参考；IBM Consulting 的 Garage 方法论对应本单元"试点->扩展->转型->原生"四阶段 | IBM watsonx 平台 + AI Governance 工具链帮助企业做模型版本管理、漂移监测、审计日志追溯；IBM 自身经历 2014-2024 十年组织变革 |

---

## deployment_example

> **真实部署场景：McKinsey Lilli + 内部 Agentic Organization 重构**

**公司**：McKinsey & Company
**场景**：McKinsey 在 2023 年内部推出 GenAI 助手 **Lilli**，服务全球 4 万+ 咨询师。Lilli 不是简单的 chatbot，而是组织一等成员：它能检索 McKinsey 40 年累积的知识库、生成 slide 初稿、做行业研究综述。

**规模**：4 万+ 用户，覆盖全部咨询师层级（Associate -> EM -> Partner）。
**约束**：
- **审计粒度**：每一次 Lilli 生成内容被咨询师采纳/修改/拒绝都进审计日志，对应本单元 TODO1 的人工干预率/Agent 自主完成率/人工修正率计算。
- **人机分工矩阵**：策略方向（Partner 人类主导）、slide 生成（Lilli AI 主导，咨询师审核）、客户合规（Partner 人类主导）-- 对应本单元营销映射表的相同结构。
- **组织网络重构**：Lilli 引入后，咨询师之间的知识求助网络（networkx Graph）发生变化 -- 部分桥接节点（资深知识 broker）的度中心性下降，Lilli 成为新的高 betweenness 节点。
**效果**：McKinsey 公开报告 Lilli 使咨询师知识检索时间减少约 70%，但同时出现"AI 成熟度被高估"问题 -- 部分原计划 AI 主导的任务，人工干预率 >30%，需降级为人机协作。这正是本单元研究问题的真实生产实例。

---

## consulting_project

> **Imperial MSc BA 风格咨询项目**（参考 Burberry/Expedia/J&J 模式）

- **Partner（赞助企业）**：Burberry（奢侈品零售，营销团队规模 200+，正在导入 AI Agent 做内容生成 + 投放优化）
- **Problem（真实业务问题）**：Burberry CMO 担心 AI Agent 导入后，"品牌调性"丢失。审计日志显示文案生成任务的人工修正率达 45%（远超 30% 阈值），CMO 需判断这是 AI 成熟度不足（应降级为人机协作）还是治理流程问题（应优化 prompt 审批）。
- **Data（企业提供数据）**：
  - 6 个月人机协作审计日志（task_id / executor / mode / intervention_count / completion_time / 修正原因标签）
  - Burberry 营销团队组织网络边表（who-consults-whom，含 Agent 节点）
  - McKinsey 7S 七维评分（Burberry 内部 HR 提供）+ ADKAR 五阶段评分（团队问卷）
- **Scope（8 周，4-5 人团队）**：
  - Week 1-2: pandas 审计日志 EDA + 干预率分布
  - Week 3-4: networkx 组织网络分析，识别桥接节点
  - Week 5-6: 7S + ADKAR 联合回归，定位卡点
  - Week 7: 天道推演仿真 3 个干预方案
  - Week 8: 策略报告 + 高杠杆干预点建议
- **Deliverable（交付物）**：
  - 原型：Streamlit 审计日志 dashboard（pandas + plotly）
  - 模型：7S-ADKAR-AuditLog 联合识别模型（sklearn 回归）
  - 策略：3 个差异化干预方案 + 推演依据 + 临界点预警
  - 报告：30 页咨询报告 + 1 页 executive summary + 15 slide deck

---

## case_study

> **HBS 风格教学案例钩子**

- **Protagonist（主角）**：Sarah Chen，Burberry 全球营销副总裁（VP Marketing），前 P&G 品牌经理，MBA，对 AI 持谨慎乐观态度。
- **Decision（关键决策点）**：Sarah 面临决策 -- 是否将"投放优化"任务从"AI 主导，人例外"降级为"人机协作"。审计日志显示该任务人工干预率达 38%（超 30% 阈值），但降级意味着增加 3 个 FTE 投放优化师，年成本增加约 60 万英镑。Sarah 必须在下周三 CMO 会议前给出建议。
- **Tension（核心张力/两难）**：
  - **效率 vs 合规**：降级增加成本但降低品牌风险；保持 AI 主导可能触发合规问题（奢侈品行业广告法规严）。
  - **短期 vs 长期**：短期降级止损，但长期不利于 AI 成熟度提升（不放手 AI 永远学不会）。
  - **数据 vs 直觉**：审计日志数据说降级，但 Sarah 的直觉是"AI 还在学，再给 3 个月"。天道推演沙盘展开 3 条时间线（立即降级 / 观察 3 月 / 加大投入提升 AI）显示不同走向。
  - **组织政治**：降级会让 AI 项目负责人（Sarah 的下属，野心勃勃的 David）丢面子，可能离职；不降级若出事 Sarah 自己背锅。

此案例可用于 Day 3 课堂 90 分钟讨论，学生用 pandas 分析审计日志 + networkx 分析组织网络 + 7S/ADKAR 评分，最后用天道推演给出建议。

---

## guest_lecture

> **客座讲座**

- **Topic（主题）**：From Pilot Purgatory to Agentic Organization -- 内部部署 Lilli 的真实审计日志与组织网络重构
- **Speaker Profile（主讲人画像）**：McKinsey 数字化转型业务合伙人，Head of McKinsey Digital 在某区域办公室，领导过 5+ 家财富 500 强企业的 Agentic Organization 设计项目。曾参与 Lilli 内部部署的治理委员会，亲手设计审计日志 schema。工学本科 + MBA + Oxford AI Ethics 证书。
- **讲座大纲（60 分钟 + 30 分钟 Q&A）**：
  1. (10 min) McKinsey Agentic Organization 概念回顾
  2. (15 min) Lilli 内部部署的真实数据：4 万用户的审计日志长什么样
  3. (15 min) 组织网络重构：Lilli 如何改变咨询师协作拓扑
  4. (10 min) 试点陷阱的微观机制：7S+ADKAR 联合诊断
  5. (10 min) 天道推演在咨询项目中的真实应用 1 例
  6. (30 min) Q&A，学生可问 Lilli 部署的技术/治理/伦理细节

---

## internship_pointer

> **实习/驻留指针**

- **机构 1：McKinsey Digital / QuantumBlack 数据科学家实习**
  - 角色：Data Scientist Intern（暑期 10-12 周）
  - 衔接：本单元 pandas 审计日志分析 + networkx 组织网络 + 7S/ADKAR 联合识别 = QuantumBlack 真实项目技能。Day 3 上机直接对标 McKinsey 内部 Lilli 治理工作。
- **机构 2：BCG X AI Software Engineer / AI Resident**
  - 角色：AI Resident（6-12 个月）或 Summer AI Software Engineer
  - 衔接：本单元 ADKAR 变革管理 + 天道推演仿真 = BCG X 为客户做 AI 变革管理咨询的核心能力。BCG X 招聘明确要求"能用数据驱动组织变革诊断"。
- **机构 3：Deloitte AI Institute - Trustworthy AI Consultant**
  - 角色：AI Governance Consultant（毕业生全职或暑期实习）
  - 衔接：本单元 AI 治理四要素（数据/模型/流程/人员）+ 审计日志 schema + NIST AI RMF 对齐 = Deloitte Trustworthy AI 实践直接技能。
- **机构 4：企业 Capstone Sponsor（Imperial MSc BA 第四学期 capstone）**
  - 角色：Capstone 项目数据科学分析师（4-5 人团队，8 周）
  - 衔接：本单元 consulting_project 节描述的 Burberry 项目即是 capstone 范例；Day 3 的 7S-ADKAR-AuditLog 框架是 capstone 的核心方法论。
- **机构 5：Anthropic Residency（可选，进阶）**
  - 角色：AI Safety Resident（若学生对 computer use 审计 + AI 对齐感兴趣）
  - 衔接：本单元 Anthropic Computer Use 审计粒度扩展（鼠标/键盘/截图）为 Anthropic 安全研究做准备。

学生应在 Day 3 学完后更新 CV，重点突出"用 pandas+networkx 做人机协作审计日志分析"与"7S+ADKAR+天道推演组织变革诊断"两项技能，匹配上述机构 JD。
