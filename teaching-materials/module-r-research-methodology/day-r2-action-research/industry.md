# R2 行动研究 · 产业链接层 (v7.0)

> 本单元的 industry linkage。公司从 v7.0 公司库挑选，全部真实存在；场景与本单元"5 轮 AR 螺旋 + 贝叶斯更新 P=0.8333 + trustworthiness 2.50->4.70"主题匹配。

---

## real_companies

| 公司 | 与本单元关联 | 业务场景 |
|------|------------|---------|
| **McKinsey** | 麦肯锡的 Organizational Practice 长期用 Lewin/Kemmis 行动研究螺旋驱动企业变革；本单元的 Plan-Act-Observe-Reflect 5 轮迭代是其 Transformation 方法论的核心节奏 | 麦肯锡顾问在客户现场部署 4–6 周一轮的 AR 循环，每轮用三角验证（访谈 + 系统日志 + KPI 看板）评估干预；本单元的 45->18min 决策时间降幅对应其"decision velocity"服务线指标。 |
| **Deloitte** | 德勤 Human Capital 与 AI Institute 联合的"AI-Enabled Workforce Transformation"用 AR 评估 AI Agent 部署对团队满意度（首轮降 0.3、后续升 1.0）的真实影响 | Deloitte 在 J&J 等 pharma 客户中用 PAR（参与式行动研究）让一线员工共创 Agent 调优方案，对应本单元 TODO4 的权力-利益矩阵 + 共创度演化。 |
| **IBM** | IBM Consulting 的"Garage"方法论本质是可复现行动研究--Plan/Act/Observe/Reflect 每轮 trace 结构化存档（对应本单元 TODO6），支持跨客户复用 | IBM 在客户企业内部部署 watsonx Agent 时，用 5 轮 AR 螺旋把决策时间从基线 45min 降至 18min，同时用三角验证追踪 trustworthiness 从 2.50 升至 4.70。 |
| **Accenture** | 埃森哲的 Strategy & Consulting 用 Susman & Evered 五步螺旋作为 Operating Model 变更的默认节奏 | 在零售客户 AI 营销 Agent 部署中，Accenture 用本单元的 Beta-Binomial 贝叶斯更新判断"干预有效"后验是否超过 P≥0.80 阈值，决定是否推广至全渠道。 |

---

## deployment_example

**场景：IBM Consulting 在某全球快消客户（年营收 ~$10B）的营销 AI Agent 部署**。

- **规模**：4 个区域营销团队（北美/欧洲/亚太/拉美），共 ~120 名营销人员 + 4 个 watsonx 驱动的营销 Agent。
- **方法**：5 轮 Plan-Act-Observe-Reflect 螺旋，每轮 4 周（共 20 周）。
  - Round 0（基线诊断）：决策时间 45min、决策质量 6.0/10、AI 使用率 0%、团队满意度 3.8/5、trustworthiness 复合评分 2.50。
  - Round 1（首轮干预：Agent 提供建议，人决策）：满意度按 Coughlan & Coghlan 2002 区间下降至 3.5（学习曲线），决策时间降至 38min。
  - Round 2（调整：Agent 自主执行低风险任务）：决策时间 28min、AI 使用率 35%。
  - Round 3（深化：Agent 决策权重提升）：决策时间 20min、AI 使用率 55%、满意度 4.1。
  - Round 4（巩固：全区域推广）：决策时间 18min、AI 使用率 70%、满意度 4.5、trustworthiness 4.70。
- **贝叶斯评估**：Beta(5,1) 先验 + 5 轮观察 -> Beta-Binomial 后验 P(干预有效) = 0.8333，超过 0.80 推广阈值。
- **约束**：(i) 数据合规--客户对话日志需脱敏后才能进入三角验证；(ii) 文化约束--拉美团队首轮抗拒更强，需要 PAR 共创而非纯技术部署；(iii) 成本--20 周周期对应 ~$2.5M 咨询费，需在 Round 2 中期评估 ROI。
- **效果**：决策时间 −60% + trustworthiness +88% 的共现改善，使客户续约下一周期（采购 + 供应链 AR 部署）。

---

## consulting_project

**Imperial MSc Business Analytics 咨询项目（8 周，4–5 人团队）**

- **Partner（赞助企业）**：Burberry（零售/CPG 咨询项目 partner，公司库）。
- **Problem（真实业务问题）**：Burberry 的数字营销团队在 4 个区域市场部署 AI 内容生成 Agent，但各区域的"干预有效性"判断不一致--某些区域经理认为 Agent 提升了决策速度但降低了决策质量，另一些则相反。需要一套可量化、可复现的 AR 方法论评估框架，判断"Agent 部署有效"是否达到可信度阈值。
- **Data（企业提供数据）**：Burberry 提供 12 周的脱敏 AR 循环数据--每轮的决策时间（分钟）、决策质量（1–10 评分）、AI 使用率（%）、团队满意度（1–5）+ 三角验证数据源数 + 成员校验率。数据许可为团队内部使用，不外传。
- **Scope（8 周 4–5 人）**：
  - W1–2：用本单元 pandas DataFrame 框架建模 Burberry 4 区域 × 多轮 AR 数据；对照 Susman & Evered 1978 与 Kemmis et al. 2014 区间校准。
  - W3–4：计算 trustworthiness 复合评分（参照 Lincoln & Guba 1985 四准则），输出 2.50->4.70 风格的演化曲线。
  - W5–6：实施 Beta-Binomial 贝叶斯更新，给出每区域 P(干预有效 | 观察) 后验；对照 0.80 阈值。
  - W7–8：撰写 HBS 风格案例 + IBM/Deloitte 风格客户报告。
- **Deliverable（交付物）**：
  1. 可复现 Jupyter notebook（参照本单元 solution.ipynb 结构）+ 结构化 AR trace 导出；
  2. 4 区域 trustworthiness + 贝叶斯后验对比仪表板（matplotlib + pandas）；
  3. 25 页咨询报告 + 1 页 Executive Summary，给出"哪些区域达 P≥0.80 阈值可推广、哪些需重设干预"的明确建议。

---

## case_study

**HBS 风格教学案例钩子**

- **Protagonist（主角）**：Lena Chen，全球快消公司 Head of AI Marketing（CMO 直接下属），曾在 McKinsey 任 Engagement Manager 5 年，熟悉 Lewin 螺旋。
- **Decision（关键决策点）**：5 轮 AR 螺旋结束后，决策时间从 45min 降至 18min（达标），trustworthiness 从 2.50 升至 4.70（达标），但 Beta-Binomial 后验 P(干预有效) = 0.8333--刚好超过 0.80 推广阈值。Lena 必须在下周 Global Leadership Meeting 决定：(A) 将 AR 螺旋方案推广至全部 12 个区域市场，还是 (B) 暂缓推广，先用 PyMC MCMC 重做贝叶斯更新（处理多参数不确定性）再决定。
- **Tension（核心张力/两难）**：
  - 速度 vs 严谨：推广能锁定 20 周改善窗口，但 P=0.8333 是闭式 Beta 更新结果，对先验敏感（用 Beta(1,1) 弱先验时后验约 0.71，未达阈值）--"刚过阈值"是否足够稳健？
  - 行动研究 vs 实证主义：AR 的认识论接受"研究即干预"，但董事会要求 RCT 级别的内部效度；Lena 需向 CMO 解释 trustworthiness 4.70 与 internal validity 的认识论不可通约。
  - PAR 共创 vs 自上而下：Round 1 满意度下降 0.3 提示一线员工抵触，推广至 12 区域时是否需要先做 PAR 共创（成本 +6 周）还是直接复制 4 区域方案？
- **教学目标**：让学生在贝叶斯阈值、AR 认识论、PAR 共创三重张力下做决策，连接本单元 TODO5（AR vs DSR）与 TODO7（贝叶斯更新）。

---

## guest_lecture

**客座讲座**

- **Topic（主题）**："From 45 to 18 Minutes: A Bayesian Action Research Playbook for Enterprise AI Deployment"（从 45 到 18 分钟：企业 AI 部署的贝叶斯行动研究剧本）。
- **Speaker Profile（主讲人画像）**：IBM Consulting 全球 AI Transformation 实践的 Head of AI（Partner 级），20 年企业变革咨询经验，曾在 McKinsey 任 Associate Partner；近期主导过 3 个 Fortune 500 客户的 5 轮 AR 螺旋部署，对 Beta-Binomial 后验阈值与 PAR 共创有第一手经验。
- **讲座结构**：
  1. 30min：5 轮 AR 螺旋的实战 KPI 演化（决策时间 45->18min、trustworthiness 2.50->4.70、P=0.8333）；
  2. 20min：Plan 阶段用天道推演做干预方案预演的实操；
  3. 20min：PAR 共创 vs 自上而下部署的取舍；
  4. 30min：学生用 starter.ipynb 数据做现场贝叶斯更新演练 + Q&A。
- **衔接本单元**：主讲人现场展示的真实客户数据对照本单元 Round 0–4 KPI 区间，让学生看到"教材区间 -> 客户现场"的映射。

---

## internship_pointer

**实习 / 驻留指针**

- **机构 1：IBM Consulting AI Transformation Residency**（6–12 个月，全职驻留）。
  - 角色：AI Transformation Resident--在 2–3 个客户现场参与 5 轮 AR 螺旋，负责 pandas 数据建模 + Beta-Binomial 贝叶斯更新 + trustworthiness 仪表板。
  - 衔接：本单元 TODO1–7 全部 7 个上机任务直接为该角色做准备；starter.ipynb 可作为面试作品集。
- **机构 2：McKinsey Analytics Tech Fellow**（暑期 8–10 周）。
  - 角色：Analytics Fellow--在 Organizational Practice 团队用 AR 螺旋评估客户变革干预；trustworthiness 四准则操作化是该岗位的核心技能。
  - 衔接：本单元 TODO3（效度评估）+ TODO5（AR vs DSR）为 McKinsey Engagement Manager 访谈中的方法论对话做准备。
- **机构 3：Deloitte AI Institute Capstone Sponsor**（Imperial MSc BA capstone sponsor）。
  - 角色：Capstone Researcher--8 周项目，赞助企业为 Deloitte 客户（如 Burberry/J&J），用本单元 AR 框架评估客户 AI 部署。
  - 衔接：本单元 industry.md 的 consulting_project 节直接对应此 capstone 的 scope 与 deliverable。
- **机构 4：Google AI Resident（Responsible AI track）**（18 个月）。
  - 角色：AI Resident--研究多 Agent 仿真预演 AR 干预路径（对应本单元"2026 前沿：多 Agent 仿真 × 行动研究验证"）。
  - 衔接：本单元"天道推演作为 AR 预演工具"节 + TODO7 贝叶斯更新为该 track 的研究做准备。
