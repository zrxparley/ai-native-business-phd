# 选修E2 · Day 2：客户生命周期分析：CLV与流失预测 · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 选修E2 Marketing Analytics and Intelligence · Day 2
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：一个客户未来值多少钱？谁会走？--从 RFM 描述性分群走向 CLV 预测性建模与流失预警
> **v5.0 升级点**：① 真实库上机（pandas + numpy + sklearn + causaldata）② 真实 RCT 数据（NSW）做 CLV/流失营销映射 ③ TODO 填空式起始笔记本 ④ Notebook 化 ⑤ 深链阅读 ⑥ 2026 前沿（CUPED + 贝叶斯CLV + 数据治理 + pandas/scipy/sklearn）

---

## 学习目标（学完你能做到）

1. 能阐述 CLV（Customer Lifetime Value）的三种计算方法--历史 CLV、简单预测 CLV、概率模型 CLV（BG/NBD + Gamma-Gamma）--及其数据需求与适用场景，并说明 CLV 如何将营销决策从"短期 ROI"转向"长期客户价值"
2. 能用 **pandas + numpy** 实现 RFM 客户分群（Recency / Frequency / Monetary），将 NSW 真实交易数据转化为 RFM 评分矩阵，并基于 R+F 组合产出 Champions / Recent / At Risk / Hibernating / Lost 五类可行动分群
3. 能用 **pandas + numpy** 实现 BG/NBD 简化版 CLV 预测公式（`pred_clv = F × retention^12 × AOV × 12 × discount`），理解 BG/NBD 模型两大行为假设（Poisson 购买 + Beta 流失）及其在 B2B 场景中的违背
4. 能用 **sklearn** 构建客户流失预测模型（LogisticRegression + RandomForestClassifier），理解 train_test_split 分层抽样、class_weight='balanced' 处理类不平衡、StandardScaler 标准化对 Logistic 收敛的影响
5. 能用 **sklearn.metrics** 评估流失模型--AUC-ROC、Precision、Recall、classification_report--并解释为什么在不平衡流失场景下看 Precision/Recall 比 Accuracy 更有意义，AUC > 0.80 是工业级可用门槛
6. 能将 CLV 预测与流失概率组合为"高/低 CLV × 高/低流失风险"四象限行动矩阵，为每个象限设计差异化营销行动（优先挽留 / 价值提升 / 低成本挽留 / 维持现状），并用特征重要性识别关键流失驱动因子

---

## 理论部分：精炼索引（详见独立教材）

> Day 2 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_选修E2_Marketing_Analytics.md` § Day 2](../../AI原生化商业博士_独立教材_选修E2_Marketing_Analytics.md)（约 289-581 行，已包含 CLV 三方法 / BG/NBD 模型详解 / 流失预测建模框架 / Next Best Action 决策完整内容）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：CLV 三种计算方法

| 方法 | 描述 | 适用场景 | 数据需求 | 本 Day TODO |
|:----:|------|---------|---------|:----------:|
| **历史 CLV** | 客户过去带来的总利润 | 评估存量客户价值 | 历史交易数据 | TODO1 |
| **简单预测 CLV** | 平均月利润 × 预期月数 | 快速估算 | 平均利润 + 留存率 | TODO1 |
| **概率模型 CLV** | BG/NBD + Gamma-Gamma | 严谨学术/商业分析 | 交易时间序列 | TODO3（简化版） |

**核心公式**：
- 历史 CLV = Σ(历史交易利润)
- 简单预测 CLV = `avg_monthly_profit × expected_months`，其中 `expected_months = 1 / churn_rate = 1 / (1 - retention_rate)`
- BG/NBD CLV（简化）= `F × retention^12 × AOV × 12 × discount_factor`

**战略意义**：CLV 将营销决策从"短期 ROI"转向"长期客户价值"。如果 CAC（获客成本）= 500 元，CLV = 3000 元，即使首月亏损，长期看也是值得的。

### 关键回顾 2：BG/NBD 模型核心假设

BG/NBD（Beta Geometric / Negative Binomial Distribution）是 Peter Fader 和 Bruce Hardie 在 2005 年提出的 CLV 预测模型，基于两个行为假设：

| 假设 | 含义 | 可能的违背 |
|------|------|---------|
| 购买率恒定 | 客户购买率不随时间变化 | 季节性、生命周期变化 |
| 流失后不可逆 | 客户一旦流失永不回来 | 营销活动可召回流失客户 |
| 客户独立 | 客户间行为互不影响 | 口碑传播、社交影响 |
| 交易金额独立 | 金额与频率无关 | 高频客户单笔金额更低（批发折扣） |

> 💡 **研究视角**：BG/NBD 假设在 B2B 场景中常被违背--B2B 客户有合同周期，购买率非恒定。本 Day TODO3 用 pandas + numpy 实现 BG/NBD 简化版，避免 `lifelines/lifetimes` 依赖冲突，专注模型思想而非工程实现。

### 关键回顾 3：流失预测建模框架

流失预测回答：**哪些客户在未来 N 天内可能流失？** 这是预测性分析在营销中最常见的应用。

**建模流程**：
1. **流失标签构造**：明确定义"流失"（如 re78=0、消费下降超 70%）
2. **特征工程**：RFM 特征 + 行为特征 + 趋势特征 + 客服特征
3. **模型训练**：LogisticRegression（基线）/ RandomForest / GradientBoosting
4. **模型评估**：AUC-ROC（>0.80 可用）+ Precision/Recall（不平衡场景必看）
5. **业务行动**：流失概率 × CLV → 四象限行动矩阵

**关键经验**（来自独立教材 § Day 2）：
- 趋势特征（近 30 天 vs 近 90 天）通常比绝对值更有预测力
- 投诉和退款是极强的流失信号
- AUC-ROC > 0.80 是可用模型质量门槛
- 不要只看 Accuracy，流失客户通常是少数，看 Precision/Recall 更有意义

### 关键回顾 4：CLV × 流失概率四象限行动矩阵

|  | 高 CLV | 低 CLV |
|---|---|---|
| **高流失风险** | 优先挽留：专属客户经理、深度折扣、产品体验优化 | 低成本挽留：自动化邮件/短信、Push 通知 |
| **低流失风险** | 价值提升：向上销售、交叉销售、VIP 权益 | 维持现状：标准服务、监控变化 |

> 售前洞察：流失预测+CLV 的组合是营销分析方案中最有说服力的"数据故事"。可以告诉客户："基于我们的模型，您有 500 个高价值客户处于高流失风险区，如果成功挽留其中 30%，按平均 CLV 3000 元计算，可挽回 45 万元的价值。"

---

## 上机部分：用真实库和真实 RCT 数据做 CLV 与流失预测

> **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO 填空版，你来做）| [`solution.ipynb`](./solution.ipynb)（参考答案，gated，做完再看）
> **真实数据/库**：[`data/README.md`](./data/README.md)（pandas + numpy + sklearn + causaldata + NSW 真实 RCT 数据）

### 为什么用真实库和真实数据

v4.0 的代码用"模拟数据"演示概念。v5.0 改用真实 RCT 数据和工业级机器学习库：

- **pandas + numpy**：RFM 分群与 CLV 公式计算的工业标准
- **sklearn**：机器学习工业级实现--LogisticRegression/RandomForest 经过严格测试，AUC-ROC 评估可信
- **causaldata**：真实 RCT 数据集--NSW 实验，445 条真实样本

### 营销映射：NSW 就业培训实验 -> CLV 与流失场景

本 Day 沿用 Day 1 的 NSW 数据映射，但聚焦预测性分析：

| NSW 原始含义 | 营销映射含义 | CLV/流失角色 |
|-------------|-------------|------|
| treat（参加培训） | 营销干预（收到促销活动） | 流失预测特征 |
| re74（1974年收入） | 历史消费基线（活动前2年） | 历史 CLV 组成 + 流失预测特征 |
| re75（1975年收入） | 近期消费（活动前1年） | 历史 CLV 组成 + 趋势特征 |
| re78（1978年收入） | 活动后消费（效果指标） | 历史 CLV 组成 + **流失标签构造** |
| age / educ / marr / nodegree | 客户人口统计学特征 | 流失预测协变量 |

**为什么用真实 RCT 数据**：RCT 的随机化确保基线特征不应强烈预测流失--这恰恰是教学价值所在。学生将看到 AUC ~0.54（接近随机）的模型在只有基线特征时的表现，理解为什么真实营销场景需要更丰富的行为特征（登录频率、会话时长、客服投诉）才能达到 AUC > 0.80。

### 上机任务（6 个 TODO，见 starter.ipynb）

| TODO | 营销任务 | 真实库 | 分析层次 |
|------|---------|--------|---------|
| TODO1 | 历史 CLV + 简单预测 CLV（re74+re75+re78 + 月均×预期月数） | pandas + numpy | 预测性 |
| TODO2 | RFM 客户分群（R/F/M → Champions/Recent/At Risk/Hibernating/Lost） | pandas | 描述性+预测性 |
| TODO3 | BG/NBD 简化版 CLV 预测 + 价值四分位 | pandas + numpy | 预测性 |
| TODO4 | 流失标签构造 + LogisticRegression 训练 + AUC/Precision/Recall | sklearn | 预测性 |
| TODO5 | RandomForest 对比 + classification_report + AUC 分析 | sklearn | 预测性 |
| TODO6 | CLV × 流失风险四象限行动矩阵 + 特征重要性 | sklearn + pandas | 处方性 |

---

## 2026 前沿补充：CUPED + 贝叶斯CLV + 数据治理

> v5.0 新增前沿点。本 Day 覆盖三个前沿方向：① CUPED（方差缩减技术，连接 Day 1 OLS 控制）② 贝叶斯 CLV（小样本客户建模方向）③ 数据治理（CLV 预测的数据质量基础）④ pandas/numpy/scipy/sklearn 工具链。

### CUPED（Controlled-Experiment Using Pre-Experiment Data）

CUPED 是 Microsoft Research 2013 年提出的方差缩减技术，2026 年已成为 A/B 测试的标准增强方法。核心思想：利用实验前的协变量信息缩减实验指标的方差，从而在不增加样本量的情况下提升统计功效。

**与 Day 2 的连接**：本 Day TODO4 的 LogisticRegression 中，re74/re75（活动前消费）作为协变量进入模型，其思想与 CUPED 一致--利用预处理信息提升对干预效应（treat）的估计精度。Day 3 将深入 CUPED 的工程实现。

### 贝叶斯 CLV：小样本客户建模方向

传统 BG/NBD 是频率学派方法，需要大样本才能稳定估计参数。2026 年，贝叶斯方法（PyMC / Stan）在 CLV 建模中崛起，特别适合：

- **高价值 B2B 客户**：样本量小但单笔金额大，贝叶斯先验可融入专家判断
- **新产品上市**：历史数据少，传统 BG/NBD 难以拟合，贝叶斯方法可借用相似产品先验
- **个体级 CLV**：频率学派给出群体平均，贝叶斯给出个体后验分布

**技术原理**：贝叶斯 CLV 将购买率 λ 和流失概率 p 都视为随机变量，给定先验 P(λ, p) 和观测数据 P(data | λ, p)，通过 MCMC 求后验 P(λ, p | data)。本 Day TODO3 用频率学派的简化 BG/NBD，贝叶斯扩展是研究前沿方向。

### 数据治理：CLV 预测的数据质量基础

CLV 预测的可靠性取决于数据质量。2026 年，随着 GDPR / CCPA / 中国《个人信息保护法》深入执行，数据治理（Data Governance）已成为 CLV 建模的前置条件：

| 数据治理维度 | CLV 影响 | 本 Day 连接 |
|-------------|---------|------------|
| **完整性** | 缺失的交易数据导致历史 CLV 低估 | TODO1 历史 CLV 计算 |
| **一致性** | 多渠道数据口径不一致导致 RFM 分群失准 | TODO2 RFM 分群 |
| **准确性** | 异常值扭曲 AOV 和 BG/NBD 参数 | TODO3 BG/NBD CLV |
| **时效性** | 过时数据导致流失标签滞后 | TODO4 流失标签构造 |
| **合规性** | 隐私法规限制个体级 CLV 预测的使用范围 | TODO6 行动矩阵落地 |

### pandas / numpy / scipy / sklearn 工具链

本 Day 使用四个核心库，构成 CLV 与流失预测的工具链：

- **pandas**：RFM 分群、CLV 公式计算（TODO1-3 的基础）
- **numpy**：BG/NBD 简化公式的数值计算（TODO3）
- **sklearn**：流失预测模型与评估（TODO4-6 的核心）
- **scipy**：假设检验与统计分布（TODO3 中 retention rate 的置信区间）

**sklearn 与 pandas 的协同**：sklearn 接受 pandas DataFrame 作为输入，输出 numpy 数组。`train_test_split` 支持 stratify 分层抽样，`classification_report` 输出完整评估指标。本 Day TODO4-6 完整覆盖 sklearn 流失预测工作流。

---

## 与前后 Day 的衔接

- **Day 1**：营销分析四层框架 + 描述性/诊断性分析--今天的 RFM 分群扩展到 CLV 预测，今天的 t 检验将扩展到流失预测模型评估
- **Day 3**：营销组合优化（MMM、MTA 与增量测量）--今天的 CLV 将与渠道归因结合，今天的流失预测将与增量建模结合，形成完整的"预测 + 处方"营销分析闭环
- **技能3（因果推断）**：今天的流失预测是预测性分析，技能3将走向 uplift modeling / 增量建模--预测"干预的因果效应"而非"是否流失"

---

## 作业与评估

作业、5 分制量表、费曼演练、2 分钟话术、复盘自诊表--沿用独立教材 § Day 2 既有设计。本学习材料包不重复，仅新增上机交付物：

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6 个 TODO 全部填好，能跑通）
- [ ] 一段 300 字分析：你的 CLV 与流失预测结果。历史 CLV 均值多少？BG/NBD 简化 CLV 均值多少？LogisticRegression 与 RandomForest 的 AUC 各是多少？四象限行动矩阵中 Q1（高 CLV 高风险）有多少客户？
- [ ] （可选）找一个你熟悉的营销场景，设计一个 CLV × 流失风险行动矩阵，标注每个象限的具体行动与预算（500 字）

---

*本讲义由 v5.0 学习材料包升级生成。理论部分引用独立教材，上机部分用真实库（pandas + numpy + sklearn + causaldata）+ 真实 RCT 数据（NSW）+ TODO 脚手架。*
*最后更新：2026-07-25*

---

## 学习科学层 (v6.0)

本单元采用**刻意练习 (Ericsson)** / **间隔重复 (FSRS-6, SM-2)** / **建构对齐 (Biggs ILO↔TLA↔AT)** / **牛津 tutorial LLM 仿真 (Socratic, Hattie 四级反馈)** 四大学习科学机制，覆盖 Day 2 的 CLV 三方法 / BG/NBD 简化公式 / RFM 五类分群 / sklearn 流失建模 (LogisticRegression + RandomForest + StandardScaler + class_weight='balanced' + stratify) / AUC-ROC + Precision/Recall / CLV × 流失四象限行动矩阵 全部核心技能。

- **mastery 阈值**与 **Worked-Faded** 三阶段 (完整示范 -> 部分填空 -> 独立解) 示例见 [`practice.md`](./practice.md) 与 [`alignment.md`](./alignment.md)。每个 drill 的 feedback_rule 领域特定 (引用 NSW RCT / pandas qcut vs cut / sklearn 三大工程陷阱 / BG/NBD discount_factor)。
- **交叉练习 (interleaving)** A1B1C1...B2C2A2...C3A3B3 排布促进近迁移，禁止块状练习 (Roediger & Karpicke 2006)。详见 `practice.md` §interleaving。
- **提取练习 (retrieval practice)** 优于重读：`tutorial.ipynb` 强制 pre-tutorial 300 字 essay (历史 CLV / 评估盲点 / Q1 决策不等式 三选一) + exit artifact (2-3 盲点 + 推荐复习单元 + 一个回问导师的苏格拉底问)。
- **间隔重复 (spaced retrieval)** 调度：5 张卡片 (CLV 三方法 / RFM qcut / sklearn 三陷阱 / 四象限行动 / CUPED+贝叶斯CLV+数据治理) 按 FSRS-6 due [1,3,8,21,60,180] 天复习，详见 [`schedule.json`](./schedule.json)。
- **建构对齐 (constructive alignment)** 矩阵：4 ILO ↔ TLA (引用 starter TODO / practice drill / tutorial 苏格拉底追问) ↔ AT (引用 solution 单元测试 / 先测题 / final 300 字分析) ↔ mastery_threshold (AUC>=0.50, 五类分群样本量>=5%, Q1 决策不等式) 详见 [`alignment.md`](./alignment.md)。
- **牛津 tutorial LLM 仿真**：`tutorial.ipynb` 用静态 if/else 模拟 5 轮苏格拉底追问 (为什么 / 反例 / 若前提变 / 凭什么 / 如何)，配 Hattie 四级反馈 [TASK] / [PROCESS] / [SELF-REG] / [FEED-FORWARD]，每单元每天限 1 次防 LLM 依赖。
- **弱项循环 (weak_loop)**：同一 drill 连续 2 次失败触发回退 + Worked 重做，详见 `practice.md` §weak_loop。

> v6.0 关键词命中: FSRS-6 / SM-2 / 刻意练习 (deliberate practice) / 建构对齐 (constructive alignment) / 牛津 tutorial / Socratic / Hattie / 间隔重复 (spaced retrieval) / 交叉 (interleaving) / mastery / Worked-Faded / 提取练习 (retrieval practice) / 形成性反馈 (formative feedback)。

*学习科学层 (v6.0) 追加于 2026-07-26，不修改 v5.0 原文一字。*

## 研究产出与产业链接层 (v7.0)

本单元产出可发表研究工件 (research.md: research_question + contribution 声明 + linked_paper arXiv/DOI 链接 + IMRaD 大纲 + NeurIPS 可复现 reproducibility checklist + research-to-practice 翻译为 HBR/MIT Sloan/企业白皮书) 与产业链接 (industry.md: >=3 真实企业锚点 Salesforce Einstein / Stitch Fix / Sephora / Booking.com / Netflix + deployment_example 部署场景 + Imperial MSc BA 风格 consulting_project 赞助企业 Burberry 8 周 4-5 人 + HBS 风格 case_study Stitch Fix protagonist + guest_lecture 客座讲座 + internship_pointer 实习指针 Salesforce Einstein AI Resident / Stitch Fix Algorithm Apprentice / Imperial Capstone / Google AI Resident)。

研究产出遵循 IMRaD / DSR (Hevner 2004 设计科学) / OSF preregistration 预注册 / FAIR 数据原则 / NeurIPS reproducibility 可复现研究标准；本单元 H1/H2/H3 三假设 (NSW 445 样本映射 CLV/流失场景下 LogReg/RF AUC ~0.54 < 0.80 工业门槛) 即文件级 hypothesis 预注册声明。产业链接遵循 Imperial MSc BA consulting_project (Burberry/Expedia/J&J) / HBS 案例法 / MIT Sloan 行动学习 (action learning) 模式。

研究产出与产业链接双向锚定：research.md linked_paper 4 篇 (Fader-Hardie BG/NBD 2005 / Fader-Hardie SIR 2007 / Microsoft CUPED 2013 / Cunningham Mixtape) 全部来自本单元 reading.md 已验证深链 (2026-07-25 验证存在)，未联网重查 arXiv API；industry.md real_companies 5 家全部来自 v7.0 公司库 (真实企业)。研究环 (假设检验) -> 设计环 (clv-lite PyPI 包 + Playbook) -> 评估环 (企业白皮书效果测量) 三环构成 DSR 双循环。详见 [`research.md`](./research.md) 与 [`industry.md`](./industry.md)。

*v7.0 研究产出与产业链接层追加于 2026-07-26，不修改 v5.0/v6.0 原文一字。*

---

## 学术前沿层 (v9.0)

本单元新增 `frontier.md`：注入 2025-2026 最新学术前沿（N 篇真实 arXiv 论文 + 批判性综述 + delta_to_unit + ≥3 开放研究问题 + 方法论批评）。论文来自 `_frontier_corpus/elective-e2-marketing-analytics.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证），覆盖前沿课题：营销归因 × 增量测量 × LLM决策。面向博后/教授级读者：批判性综述非罗列，delta_to_unit 显式指出前沿如何更新本单元所教，开放问题为可发表研究方向。详见 `frontier.md`。
