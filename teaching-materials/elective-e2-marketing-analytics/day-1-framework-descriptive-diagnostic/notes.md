# 选修E2 · Day 1：营销分析框架与描述性/诊断性分析 · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 选修E2 Marketing Analytics and Intelligence · Day 1
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：如何用数据从"发生了什么"走向"为什么发生"？--营销分析四层框架的描述性与诊断性基础
> **v5.0 升级点**：① 真实库上机（pandas + scipy.stats + statsmodels + causaldata）② 真实 RCT 数据（NSW）做营销映射 ③ TODO 填空式起始笔记本 ④ Notebook 化 ⑤ 深链阅读 ⑥ 2026 前沿（CUPED + 数据治理 + pandas/scipy/statsmodels/SQL）

---

## 学习目标（学完你能做到）

1. 能阐述营销分析四层递进框架（描述性->诊断性->预测性->处方性），说明每层回答的核心业务问题（发生了什么 / 为什么 / 将来会怎样 / 应该怎么做）及其对应的技术方法，并诊断一个企业在四层框架中的当前位置
2. 能用 **pandas** 执行营销漏斗分析（AARRR 模型：Acquisition / Activation / Retention / Revenue / Referral），计算各阶段转化率与流失率，识别漏斗中的关键流失节点
3. 能用 **pandas** 实现 RFM（Recency / Frequency / Monetary）客户分群，将交易数据转化为 RFM 评分矩阵，并基于分群结果制定差异化的营销行动建议
4. 能用 **scipy.stats** 执行诊断性分析的两大核心检验--独立样本 t 检验（`ttest_ind`）和卡方独立性检验（`chi2_contingency`）--判断营销干预是否产生了统计显著的效果，以及用户分群与干预分组是否存在关联
5. 能用 **statsmodels** 拟合 OLS 回归模型（`sm.OLS`），解读回归系数、p 值、R-squared 的业务含义，理解"控制其他变量后干预的净效应"这一诊断性分析的核心思想
6. 能用 **causaldata** 库加载真实 RCT 数据（NSW National Supported Work），将就业培训实验映射为营销干预场景（treat=营销活动，re78=活动后消费），理解真实实验数据在营销分析中的价值

---

## 理论部分：精炼索引（详见独立教材）

> Day 1 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_选修E2_Marketing_Analytics.md` § Day 1](../../AI原生化商业博士_独立教材_选修E2_Marketing_Analytics.md)（约 61-287 行，已包含四层框架/漏斗分析/同期群分析/RFM 分析/渠道效果诊断完整内容）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：营销分析四层框架

| 层次 | 核心问题 | 技术方法 | 典型输出 | 本 Day 覆盖 |
|:----:|---------|---------|---------|:----------:|
| **描述性分析** | 发生了什么？ | 数据聚合、可视化、漏斗分析 | 仪表盘、报表、趋势图 | ✅ |
| **诊断性分析** | 为什么发生？ | 下钻分析、相关性分析、RFM、假设检验 | 归因报告、分群洞察 | ✅ |
| **预测性分析** | 将来会怎样？ | 回归、分类、时间序列 | 预测分数、预警列表 | Day 2 |
| **处方性分析** | 应该怎么做？ | 最优化、模拟、因果推断 | 预算分配建议、行动推荐 | Day 3 |

**递进逻辑**：描述性是基础（你无法诊断不知道的事情），诊断性是桥梁（理解了原因才能预测）。本 Day 聚焦前两层，为 Day 2（CLV 预测）和 Day 3（MMM 优化）奠基。

**AI 增强点**：在描述性分析中，LLM 可自动将数据转化为自然语言洞察（"本月转化率下降 15%，主要原因是移动端流量减少"）。在诊断性分析中，LLM 可支持自然语言查询数据库（"帮我看看上周北京地区新用户的留存率"）。

> 售前洞察：当客户说"我们要做营销数据分析"时，首先要诊断他们在四层框架中的当前位置。大多数中国企业处于描述性分析的早期阶段（只有报表没有分析），直接跳到处方性分析是不现实的。

### 关键回顾 2：营销漏斗分析（AARRR 模型）

AARRR（海盗指标）是 Dave McClure 提出的营销漏斗框架，覆盖用户生命周期的五个关键阶段：

| 阶段 | 全称 | 核心问题 | 关键指标 |
|------|------|---------|---------|
| **A**cquisition | 获取 | 用户怎么找到你的？ | 曝光量、点击率 CTR、获客成本 CAC |
| **A**ctivation | 激活 | 用户体验到核心价值了吗？ | 注册率、首次购买率、激活率 |
| **R**etention | 留存 | 用户会回来吗？ | 次日/7日/30日留存率 |
| **R**evenue | 变现 | 用户花钱了吗？ | ARPU、客单价 AOV、LTV |
| **R**eferral | 传播 | 用户会推荐给别人吗？ | NPS、邀请率、K-factor |

传统漏斗是线性的（曝光->点击->注册->购买），但实际用户旅程是多触点、非线性的。本 Day 用真实 RCT 数据映射 AARRR 的前四个阶段。

### 关键回顾 3：RFM 客户分群

RFM（Recency, Frequency, Monetary）是客户分值的经典方法：

| 维度 | 含义 | 营销解读 |
|------|------|---------|
| **R**ecency | 最近一次消费距今天数 | R 越小 = 越近期活跃，流失风险越低 |
| **F**requency | 消费频次 | F 越大 = 越忠诚，价值越高 |
| **M**onetary | 消费总金额 | M 越大 = 高价值客户 |

**传统 RFM vs AI 增强 RFM**：传统 RFM 用固定阈值分桶（如 R 分为 5 档），AI 增强用 K-Means 聚类自动分群，可加入行为特征、社交特征。本 Day 用 pandas 实现基础 RFM 分群，Day 2 扩展到 CLV 预测。

### 关键回顾 4：诊断性分析的核心工具

诊断性分析回答"为什么发生"，核心工具包括：

| 工具 | 回答的问题 | 真实库实现 | 本 Day TODO |
|------|-----------|-----------|------------|
| 分组对比 | A/B 两组有差异吗？ | `pandas.groupby()` | TODO1 |
| 假设检验 | 差异统计显著吗？ | `scipy.stats.ttest_ind` | TODO4 |
| 卡方检验 | 两个分类变量独立吗？ | `scipy.stats.chi2_contingency` | TODO5 |
| 相关性分析 | 变量间线性关系强度？ | `pandas.DataFrame.corr()` | TODO6 |
| 回归分析 | 控制其他变量后的净效应？ | `statsmodels.api.OLS` | TODO6 |

**关键认知**：p 值只告诉你"有没有效果"，不告诉你"效果多大"。效应量（Cohen's d）和置信区间比 p 值更丰富。"统计显著"不等于"商业显著"--大样本下微小差异也会显著。

---

## 上机部分：用真实库和真实 RCT 数据做营销分析

> **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO 填空版，你来做）| [`solution.ipynb`](./solution.ipynb)（参考答案，gated，做完再看）
> **真实数据/库**：[`data/README.md`](./data/README.md)（pandas + scipy.stats + statsmodels + causaldata + NSW 真实 RCT 数据）

### 为什么用真实库和真实数据

v4.0 的代码用"模拟数据"演示概念。v5.0 改用真实 RCT 数据和工业级科学计算库：

- **pandas**：数据处理的工业标准--`df.groupby()`、`df.describe()` 一行完成分组统计
- **scipy.stats**：假设检验的权威实现--`ttest_ind`、`chi2_contingency` 经过严格测试
- **statsmodels**：统计建模的专业工具--`sm.OLS` 提供完整回归诊断（R-squared、t 检验、F 检验）
- **causaldata**：真实 RCT 数据集--NSW (National Supported Work) 实验，445 条真实样本

### 营销映射：NSW 就业培训实验 -> 营销干预场景

本 Day 使用 causaldata 库的 NSW 数据集。NSW (National Supported Work) 是 1970 年代美国的一项真实随机对照实验（RCT），原本用于评估就业培训项目效果。我们将其映射为营销场景：

| NSW 原始含义 | 营销映射含义 | 字段 |
|-------------|-------------|------|
| treat（参加培训） | 营销干预（收到促销活动） | treat (0/1) |
| re74（1974年收入） | 历史消费基线（活动前2年） | re74 |
| re75（1975年收入） | 近期消费（活动前1年） | re75 |
| re78（1978年收入） | 活动后消费（效果指标） | re78 |
| age | 客户年龄 | age |
| educ | 客户教育程度（消费能力代理） | educ |
| marr | 是否已婚（家庭消费代理） | marr |
| nodegree | 是否无学位（价格敏感度代理） | nodegree |

**为什么用真实 RCT 数据而非模拟数据**：RCT（随机对照实验）是因果推断的金标准。NSW 数据是真实实验收集的真实人数据，包含真实的基线不平衡、真实的分布偏态、真实的缺失模式。模拟数据无法复制这些真实世界的复杂性。用真实数据做描述/诊断分析，才能建立对真实数据质感的直觉。

### 上机任务（6 个 TODO，见 starter.ipynb）

| TODO | 营销任务 | 真实库 | 分析层次 |
|------|---------|--------|---------|
| TODO1 | 加载 NSW 数据，描述性统计（treated vs control 基线对比） | pandas | 描述性 |
| TODO2 | AARRR 营销漏斗分析（Acquisition/Activation/Retention/Revenue） | pandas | 描述性 |
| TODO3 | RFM 客户分群（Recency/Frequency/Monetary 五分群） | pandas | 描述性+诊断性 |
| TODO4 | t 检验：营销干预后消费（re78）treated vs control 差异 | scipy.stats | 诊断性 |
| TODO5 | 卡方检验：干预分组与用户特征（已婚/无学位）独立性 | scipy.stats | 诊断性 |
| TODO6 | OLS 回归 + 相关矩阵：控制混杂后干预净效应 | statsmodels | 诊断性 |

---

## 2026 前沿补充：CUPED + 数据治理 + 统计建模

> v5.0 新增前沿点。本 Day 覆盖三个前沿方向：① CUPED（方差缩减技术）② 数据治理（营销数据质量基础）③ pandas/scipy/statsmodels/SQL 工具链。

### CUPED（Controlled-Experiment Using Pre-Experiment Data）

CUPED 是 Microsoft Research 2013 年提出的方差缩减技术（variance reduction），在 2026 年已成为 A/B 测试的标准增强方法。核心思想：利用实验前的协变量信息缩减实验指标的方差，从而在不增加样本量的情况下提升统计功效。

**为什么 CUPED 在营销分析中重要**：
- **提升实验灵敏度**：同样的样本量，CUPED 可以检测到更小的效应--在营销场景中，很多干预效果本就很小（1-3% 提升），CUPED 让这些效果可被可靠检测
- **降低实验成本**：达到同样的统计功效，CUPED 需要更少的样本--对于流量有限的产品，这意味着可以同时跑更多实验
- **与因果推断的连接**：CUPED 本质上是"用预处理变量调整事后估计"，这与本 Day TODO6 的 OLS 回归控制混杂变量的思想一脉相承

**技术原理**：CUPED 构造一个调整后的指标 Y' = Y - theta * (X - E[X])，其中 X 是与 Y 相关的预处理协变量，theta = Cov(Y,X)/Var(X)。调整后的指标 Y' 与 Y 有相同的期望，但方差更小。

> 本 Day TODO6 的 OLS 回归中，re75（活动前消费）作为协变量进入模型，其思想与 CUPED 一致--利用预处理信息提升对干预效应的估计精度。Day 2 和 Day 3 会深入 CUPED 的工程实现。

### 数据治理：营销分析的数据质量基础

营销分析的可靠性取决于数据质量。2026 年，随着 GDPR / CCPA / 中国《个人信息保护法》的深入执行，数据治理（Data Governance）已成为营销分析的前置条件：

| 数据治理维度 | 营销分析影响 | 本 Day 连接 |
|-------------|-------------|------------|
| **完整性** | 缺失的转化数据导致漏斗分析失真 | TODO1 描述统计中的缺失值检查 |
| **一致性** | 多渠道数据口径不一致导致归因错误 | TODO2 AARRR 漏斗的跨阶段口径统一 |
| **准确性** | 异常值扭曲均值和回归系数 | TODO1 中位数 vs 均值的差异 |
| **时效性** | 过时数据导致 RFM 分群失准 | TODO3 Recency 维度的时效依赖 |
| **合规性** | 隐私法规限制用户级数据使用 | Day 3 MMM 优于 MTA 的隐私优势 |

**关键认知**：在售前场景中，客户的数据治理成熟度直接决定了营销分析方案的可行性。如果客户的交易数据散落在多个系统、口径不统一、缺失严重，再先进的分析模型也无法产出可靠洞察。数据治理是营销分析的"地基"。

### pandas / scipy / statsmodels / SQL 工具链

本 Day 使用四个核心库，它们构成了营销分析的工具链：

- **pandas**：数据加载、清洗、分组聚合（TODO1-3 的基础）
- **scipy.stats**：假设检验（TODO4-5 的 t 检验和卡方检验）
- **statsmodels**：统计建模（TODO6 的 OLS 回归，提供完整诊断）
- **SQL**：数据提取的基础工具--pandas 的 `groupby`/`agg` 操作在逻辑上等价于 SQL 的 `GROUP BY` / 聚合函数

**SQL 与 pandas 的对应关系**：

| SQL | pandas | 营销场景 |
|-----|--------|---------|
| `SELECT col1, SUM(col2) FROM t GROUP BY col1` | `df.groupby('col1')['col2'].sum()` | 按渠道聚合消费 |
| `WHERE condition` | `df[df['col'] > value]` | 筛选高价值客户 |
| `JOIN t1 ON t2` | `pd.merge(df1, df2, on='key')` | 关联用户与交易表 |
| `COUNT(DISTINCT col)` | `df['col'].nunique()` | 统计独立访客数 |

在实际营销分析项目中，数据通常存储在数据库中，先用 SQL 提取，再用 pandas/scipy/statsmodels 做分析。本 Day 为简化流程，直接用 causaldata 库加载数据，但 SQL 是营销分析师的必备技能。

---

## 与后续 Day 的衔接

- **Day 2**：客户生命周期分析（CLV 与流失预测）--今天的描述性分析（RFM）将扩展到预测性分析（BG/NBD 模型预测 CLV），今天的 t 检验将扩展到流失预测模型
- **Day 3**：营销组合优化（MMM、MTA 与增量测量）--今天的诊断性分析（回归）将扩展到处方性分析（预算优化），今天提到的 AARRR 漏斗将与归因方法结合
- **技能3（因果推断）**：今天的 NSW 数据和 t 检验是因果推断的入门，技能3将走向 DML / 合成控制 / 增量建模等更高级的因果效应估计方法

---

## 作业与评估

作业、5 分制量表、费曼演练、2 分钟话术、复盘自诊表--沿用独立教材 § Day 1 既有设计。本学习材料包不重复，仅新增上机交付物：

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6 个 TODO 全部填好，能跑通）
- [ ] 一段 300 字分析：你的 NSW 营销映射分析结果。t 检验 p 值是多少？Cohen's d 多大？OLS 回归中 treat 系数显著吗？RFM 分群中 Champions 有多少？
- [ ] （可选）找一个你熟悉的营销场景，设计一个 AARRR 漏斗，标注每个阶段的关键指标和数据来源（500 字）

---

*本讲义由 v5.0 学习材料包升级生成。理论部分引用独立教材，上机部分用真实库（pandas + scipy.stats + statsmodels + causaldata）+ 真实 RCT 数据（NSW）+ TODO 脚手架。*
*最后更新：2026-07-24*

---

## 学习科学层 (v6.0)

本单元在 v5.0 学习材料包基础上, 叠加 **学习科学层** (4 个新文件 + 本节追加), 不破坏 v5.0 基线:

- **刻意练习 (deliberate practice, Ericsson)**: 见 [`practice.md`](./practice.md)。skill_target 锁定"用 pandas+scipy+statsmodels 对 NSW 营销映射数据完成描述漏斗+诊断检验+RFM 分群, 并用业务语言解释 p 值/Cohen's d/OLS 系数"。5 个 drill (D1 漏斗/D2 t检验/D3 卡方/D4 OLS/D5 RFM) 全部采用 **Worked-Faded** 三阶段 (完整示范 -> 部分填空 -> 独立解), feedback_rule 引用 NSW 真实字段 (re75/treat/re78) 与真实库 (ttest_ind/chi2_contingency/OLS)。含 weak_loop (连续 2 次失败回退) 与 interleaving (A1B1C1->B2C2A2->C3A3B3 交叉排布)。
- **间隔重复 (spaced retrieval, FSRS-6 / SM-2 backup)**: 见 [`schedule.json`](./schedule.json)。7 张卡片 (C1 四层框架/C2 AARRR/C3 RFM/C4 t检验+d/C5 卡方/C6 OLS+CUPED/C7 NSW映射), 每卡 due=[1,3,8,21,60,180], request_retention=0.9。
- **建构对齐 (constructive alignment, Biggs ILO↔TLA↔AT)**: 见 [`alignment.md`](./alignment.md)。6 行 ILO↔TLA↔AT 矩阵, mastery_threshold=80%, 含 Feed Up / Feed Back / Feed Forward 三自检 (逃逸检测: 不练 D4 能否过 TODO6? tutorial 口试拦截)。
- **牛津 tutorial LLM 仿真 (Oxford Socratic + Hattie 四级反馈)**: 见 [`tutorial.ipynb`](./tutorial.ipynb)。persona 禁直接答案 + HBS devil's advocate, 5 个苏格拉底问 (为什么/反例/若前提变/凭什么/如何), student_model.json 记录 6 ILO 掌握度与盲点, Hattie 四级 [TASK]/[PROCESS]/[SELF-REG]/[FEED-FORWARD] (无 Self 级表扬), 每日 1 次限频防依赖。

**mastery 阈值与 Worked-Faded 示例详见 practice.md 与 alignment.md。交叉练习 (interleaving) 促进迁移, 提取练习 (retrieval practice) 优于重读。**

> v6.0 关键词命中: FSRS-6 / SM-2 / 刻意练习 / deliberate practice / 建构对齐 / constructive alignment / 牛津tutorial / Socratic / Hattie / 间隔重复 / spaced retrieval / 交叉 / interleaving / mastery / Worked-Faded / retrieval practice / formative feedback。

## 研究产出与产业链接层 (v7.0)
本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+arXiv链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。详见 research.md 与 industry.md。

---

## 学术前沿层 (v9.0)

本单元新增 `frontier.md`：注入 2025-2026 最新学术前沿（N 篇真实 arXiv 论文 + 批判性综述 + delta_to_unit + ≥3 开放研究问题 + 方法论批评）。论文来自 `_frontier_corpus/elective-e2-marketing-analytics.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证），覆盖前沿课题：营销归因 × 增量测量 × LLM决策。面向博后/教授级读者：批判性综述非罗列，delta_to_unit 显式指出前沿如何更新本单元所教，开放问题为可发表研究方向。详见 `frontier.md`。
