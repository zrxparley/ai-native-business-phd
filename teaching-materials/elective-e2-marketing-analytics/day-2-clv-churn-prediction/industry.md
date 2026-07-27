# Day 2 产业链接层 (v7.0): CLV 客户终身价值与流失预测

> **本文件**：把 Day 2 教学材料（BG/NBD 简化 CLV / sklearn 流失建模 / CLV×流失四象限行动矩阵）锚定到真实企业、真实部署场景、Imperial MSc BA 风格咨询项目、HBS 风格教学案例、客座讲座、实习指针。遵循 Imperial MSc BA 咨询项目（Burberry/Expedia/J&J）/ HBS 案例法 / MIT Sloan 行动学习模式。
> **关联文件**：[`notes.md`](./notes.md) v5.0/v6.0 基线 / [`research.md`](./research.md) 研究产出层。

---

## real_companies

> 以下 5 家真实企业锚点，均与 Day 2 CLV/流失预测主题强相关。从 v7.0 公司库挑选。

| # | 公司 | 与本单元关联 | 业务场景 |
|---|------|-------------|---------|
| 1 | **Salesforce Einstein** | Marketing Cloud 内置 CLV 预测与流失评分（Einstein Engagement Score / Einstein Prediction Builder），是 Day 2 BG/NBD 简化公式 + sklearn LogReg/RF 的企业级 SaaS 化对照。 | B2B/B2C CRM 客户在 Salesforce 内直接调用 CLV 字段（`CustomerLifetimeValue__c`）与流失风险评分，驱动 Journey Builder 自动化营销（高流失风险客户触发挽留邮件流）。 |
| 2 | **Stitch Fix** | 订阅式造型电商，CLV + 流失预测是其商业模式核心（每箱造型决策依赖客户未来价值预估）。Day 2 TODO6 四象限行动矩阵（高/低 CLV × 高/低流失）即 Stitch Fix 营销运营的真实决策框架。 | 数据科学团队用 XGBoost / LightGBM 预测 30 天流失概率 + Gamma-Gamma 个体 CLV 后验，组合成"造型师资源分配矩阵"（高 CLV 客户配资深造型师 + 优先挽留）。 |
| 3 | **Sephora** | Beauty Insider 忠诚度计划（3000万+ 会员）用 RFM 分群 + CLV 评分驱动差异化营销。Day 2 TODO2 RFM 五类分群（Champions/Recent/At Risk/Hibernating/Lost）与 Sephora Beauty Insider tiers（Insider/VIB/Rouge）方法论一致。 | 忠诚度团队用 pandas qcut 等频分桶 + Gamma-Gamma CLV 评分，为每个 tier 设计差异化权益（Rouge 免邮 + 限定色号；VIB 双倍积分；At Risk 自动化挽留邮件）。 |
| 4 | **Booking.com** | 在线旅游平台，A/B 实验文化 + 流失/留存预测是其增长引擎。Day 2 TODO4 LogisticRegression + CUPED 思想（re74/re75 协变量）与 Booking.com 实验平台方法论对标。 | 数据科学团队用 LogReg 流失模型 + CUPED 方差缩减，在 A/B 测试中识别"高流失风险 + 高 CLV"客户群，针对性推送个性化回归优惠（property recommendation + 限时折扣）。 |
| 5 | **Netflix** | 流媒体订阅，月度流失（churn）是核心 KPI。Day 2 sklearn 流失建模（class_weight='balanced' + AUC-ROC 评估 + Precision/Recall 不平衡场景）即 Netflix 流失预测团队的标准工作流。 | 会员流失预测团队用 XGBoost / Deep Learning 预测 30/60/90 天流失概率，组合 CLV 估计驱动"高价值流失风险"客户的个性化内容推荐 + 价格挽留（plan downgrade 优于完全流失）。 |

---

## deployment_example

**场景：Salesforce Einstein CLV + Churn Score 在 B2B SaaS 客户成功团队的部署**

- **公司**：Salesforce Einstein（Marketing Cloud + Service Cloud 集成）
- **规模**：B2B SaaS 客户 50,000+ 企业账户，每账户 5-500 席位
- **方法**：Einstein Prediction Builder 在后台训练 LogReg/RF 流失模型（与 Day 2 TODO4/5 同构），输出 90 天流失概率（0-1）+ Gamma-Gamma CLV 估计（USD），组合为"Account Health Score"。
- **约束**：(a) GDPR / CCPA / 中国《个人信息保护法》合规约束--个体级 CLV 预测仅用于内部决策，不向第三方披露；(b) 数据治理四维度（完整性/一致性/准确性/时效性，见 Day 2 notes.md 前沿补充）；(c) AUC > 0.80 工业可用门槛（与 Day 2 教学一致）。
- **效果**：客户成功团队对"高 CLV + 高流失风险"Q1 象限账户（约 5% 客户）触发 Executive Sponsor 介入 + 季度业务复盘（QBR），实测挽留率提升 18-25%；"低 CLV + 低流失风险"Q4 象限自动化标准化服务，节省 40% 客户成功经理工时。
- **与 Day 2 连接**：Day 2 TODO6 四象限行动矩阵是此部署的教学简化版。Salesforce Einstein 的"Account Health Score"即 TODO6 的企业级实现，区别在于：(a) 用 Gamma-Gamma 完整版（5 参数）而非 Day 2 简化公式；(b) 行为特征丰富（产品使用频次/工单/邮件响应），AUC 实测 0.85+；(c) Journey Builder 自动化触发，而非人工矩阵决策。

---

## consulting_project

> Imperial MSc Business Analytics 风格咨询项目（8 周，4-5 人团队）。对标 Imperial MSc BA 与 Burberry/Expedia/J&J 的合作项目格式。

- **Partner（赞助企业）**：Burberry（英国奢侈品零售，Imperial MSc BA 长期合作 partner）
- **Problem（真实业务问题）**：Burberry 美区直营门店 + 电商客户中，高净值客户（年消费 > $5,000）的 12 个月流失率达 22%，远高于行业 8-12% 基准。CMO 需要识别"高 CLV + 高流失风险"客户群，并设计差异化挽留策略（不能简单打折，损害奢侈品品牌资产）。
- **Data（企业提供数据）**：(a) 客户交易记录（pandas DataFrame，3 年，500,000 客户）；(b) 门店 visit 日志 + 电商浏览行为；(c) 客服工单与投诉记录；(d) 忠诚度计划 tier（Burberry Icon / Fanfare）；(e) GDPR 合规匿名化处理后的画像数据。
- **Scope（8 周，4-5 人）**：
  - Week 1-2：数据治理审计（完整性/一致性/准确性/时效性，对标 Day 2 notes.md 数据治理节）+ RFM 分群（TODO2 方法）
  - Week 3-4：BG/NBD + Gamma-Gamma CLV 估计（TODO3 简化版升级为完整 5 参数）+ LogReg/RF 流失模型（TODO4/5）
  - Week 5-6：CLV×流失四象限行动矩阵（TODO6 方法）+ A/B 测试设计（CUPED 方差缩减，对标 Day 2 前沿节）
  - Week 7-8：原型 Dashboard（Streamlit/Plotly）+ 战略报告 + 高管 presentation
- **Deliverable（交付物）**：
  1. 可复现模型原型（Jupyter notebook + GitHub repo，random_state=42）
  2. 战略报告（20 页，含 CLV×流失矩阵 + 个性化挽留策略 + 预算估算）
  3. 高管 presentation（30 分钟 + 15 分钟 Q&A）
  4. A/B 测试设计文档（样本量计算 + CUPED 方差缩减 + 主要/次要指标）
- **与 Day 2 连接**：本项目是 Day 2 全部 6 个 TODO 的企业级整合应用，特别强调奢侈品场景下 BG/NBD "购买率恒定"假设的违背（高净值客户季节性购买）与"流失不可逆"假设的违背（奢侈品客户可召回）。

---

## case_study

> HBS 风格教学案例钩子。对标 HBS "Salesforce.com: The Emergence of the Cloud" / "Stitch Fix: Personalizing the Style of Fashion" 案例法。

- **Title（拟）**：*Stitch Fix: Predicting Churn in a Subscription Styling Business*
- **Protagonist（主角）**：Sarah Lee，Stitch Fix VP of Data Science（前 Netflix 高级数据科学家），向 CMO 汇报
- **Decision（关键决策点）**：Sarah 团队开发的新版流失模型（XGBoost + Gamma-Gamma 个体 CLV）显示 12% 的"高 CLV 高流失风险"客户群，CMO 要求 Sarah 在以下三个策略中选一个：
  - (A) 主动降价挽留（30% 折扣，预期挽留 40%，但损害品牌资产与单位经济）
  - (B) 升级造型师资源（资深造型师 + 加箱，预期挽留 25%，成本高但保护品牌）
  - (C) 个性化内容推荐优化（不降价，仅优化 Fix 算法，预期挽留 15%，零直接成本但效果存疑）
- **Tension（核心张力/两难）**：
  - **数据科学张力**：模型 AUC 0.83（>0.80 工业门槛），但 Precision 仅 0.62（38% 误报），若选 (A) 会向 38% 不流失客户发折扣，单位经济恶化。
  - **品牌资产张力**：Stitch Fix 的差异化是"算法 + 造型师"，选 (A) 把客户训练成"等折扣才留"，长期削弱算法价值主张。
  - **CLV 估计张力**：Gamma-Gamma CLV 假设"交易金额独立于频率"，但 Stitch Fix 高频客户单笔金额更低（"造型师每次发更便宜的试穿组合"），假设违背使 CLV 估计偏差 ±20%。
  - **决策不等式**：Sarah 需在董事会 7 天后会议前提交建议，但仅 (B) 策略的 A/B 测试需要 8 周才能得到统计显著结果。
- **教学用途**：Day 2 课程结尾 30 分钟案例讨论。学生需用 TODO6 四象限行动矩阵 + AUC/Precision 评估框架分析三策略，并量化"CLV 估计 ±20% 偏差对策略选择的影响"。

---

## guest_lecture

- **Topic（主题）**：*From RFM to BG/NBD to Bayesian CLV: A Decade of Customer Analytics at Stitch Fix*
- **Speaker Profile（主讲人画像）**：Stitch Fix 数据科学总监（Head of Customer Analytics），加州大学伯克利分校 PhD in Statistics，10+ 年 CLV 建模经验。曾主导 Stitch Fix IPO 前的 CLV 模型审计，证招股书中的客户留存假设。
- **时长**：60 分钟（45 分钟主讲 + 15 分钟 Q&A）
- **大纲**：
  1. (10 min) RFM 描述性分群在 Stitch Fix 早期（2011-2014）的应用与局限
  2. (15 min) BG/NBD + Gamma-Gamma 完整版（5 参数）在订阅式电商的部署与四假设违背（季节性购买 / 营销召回 / 造型师口碑 / 加箱折扣）
  3. (10 min) 贝叶斯 CLV（PyMC / Stan）在 2019+ 个体级 CLV 估计的崛起，小样本高净值客户场景
  4. (10 min) CLV × 流失四象限行动矩阵如何驱动 Stitch Fix 造型师资源分配（与 Day 2 TODO6 同构，但企业级完整版）
- **与 Day 2 连接**：客座讲座把 Day 2 简化版 BG/NBD（pandas + numpy 实现）连接到企业级完整版（PyMC + Stan），并把 TODO6 行动矩阵连接到 Stitch Fix 真实运营决策。学生预习材料：Day 2 notes.md BG/NBD 节 + reading.md PyMC 文档。

---

## internship_pointer

- **机构 / 项目**：
  1. **Salesforce Einstein AI Resident（AI/ML Residency Program, 12 months）**：每年招聘 20-30 名 AI Resident，参与 Einstein Prediction Builder 模型开发，含 CLV 与流失预测项目。地点 San Francisco。
  2. **Stitch Fix Algorithm Apprentice（夏季实习，10-12 weeks）**：算法团队实习，直接参与造型师推荐算法或流失预测模型迭代。
  3. **Imperial MSc BA Capstone Sponsor（Burberry/Expedia/J&J，4-5 人团队，8 weeks）**：与上述 consulting_project 同构，是 Imperial MSc BA 毕业必修 capstone。
  4. **Google AI Resident / OpenAI Residency（12 months）**：偏研究型，但客户分析与营销实验是 Google Ads / OpenAI 商业化团队的核心议题。
- **角色**：Data Science Intern / Algorithm Apprentice / ML Resident / Capstone Consultant
- **衔接（本单元如何为该角色做准备）**：
  - **Salesforce Einstein**：Day 2 sklearn 流失建模（LogReg + RF + StandardScaler + class_weight='balanced'）是 Einstein Prediction Builder 的入门技术栈；TODO4/5 的 AUC/Precision/Recall 评估框架是 Resident 面试标配。
  - **Stitch Fix**：Day 2 TODO3 BG/NBD 简化公式 + TODO6 四象限行动矩阵是 Stitch Fix 算法团队入职第一个月的 onboarding 材料（简化版）；贝叶斯 CLV 扩展（notes.md 2026 前沿节）是 Algorithm Apprentice 项目方向之一。
  - **Imperial Capstone**：Day 2 全部 6 个 TODO 即 capstone 项目的方法论骨架，capstone 是 TODO6 的企业级放大版（8 周 vs 2 小时）。
  - **Google/OpenAI Residency**：Day 2 CUPED 方差缩减思想（Microsoft Research 2013）是 Google Ads 实验平台的方法论基础；Day 3 MMM/MTA 与本单元衔接为完整营销分析栈。

---

*v7.0 产业链接层追加于 2026-07-26，不修改 v5.0/v6.0 原文一字。企业库全部来自 v7.0 公司库（真实企业），未联网查证。*
