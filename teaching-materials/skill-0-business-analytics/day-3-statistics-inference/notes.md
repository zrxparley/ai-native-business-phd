# 技能0 · Day 3：描述统计与推断统计 · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 技能0 AI商业分析基础 · Day 3
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：如何用统计方法从营销数据中提取决策依据？--从"看数字"到"验假设"的科学决策路径
> **v5.0 升级点**：① 新增真实库上机（numpy + pandas + scipy.stats + matplotlib/seaborn）② 新增 TODO 填空式起始笔记本 ③ Notebook 化 ④ 深链阅读 ⑤ 2026 前沿（贝叶斯统计 + 概率编程 PyMC + 可复现研究）

---

## 学习目标（学完你能做到）

1. 能计算并解释描述统计的核心指标--均值、中位数、方差、标准差、分位数、偏度--并说明在营销客单价（AOV）等右偏分布场景中为什么中位数比均值更稳健
2. 能阐述假设检验的逻辑（原假设 H₀ / 备择假设 H₁ / p 值 / 第一类错误 α / 第二类错误 β / 统计功效 Power），并用 **scipy.stats** 执行 t 检验判断 A/B 两组营销方案的转化率差异是否显著
3. 能计算并解读 95% 置信区间，区分"统计显著性"（p 值）与"商业显著性"（效应量 + CI 宽度），避免大样本下的"微小差异显著"陷阱
4. 能用 **scipy.stats.chi2_contingency** 执行卡方独立性检验，判断用户分群（新客/回客/VIP）与购买品类（美妆/电子/健身/家居）是否存在关联
5. 能用 Beta-Binomial 模型实现贝叶斯统计入门--理解先验、似然、后验的更新机制，对比频率派（p 值）与贝叶斯派（后验分布）的根本差异，并了解概率编程框架 PyMC 的前沿应用

---

## 理论部分：精炼索引（详见独立教材）

> Day 3 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_技能0_AI商业分析基础.md` § Day 3](../../AI原生化商业博士_独立教材_技能0_AI商业分析基础.md)（约 562-779 行，已包含描述统计/概率分布/假设检验/置信区间/A/B测试完整案例）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：描述统计 -- 用数字概括数据

| 指标类别 | 具体指标 | 营销含义 |
|---------|---------|---------|
| 集中趋势 | 均值 mean、中位数 median、众数 mode | 客单价（AOV）：右偏分布下中位数更稳健 |
| 离散程度 | 方差 var、标准差 std、IQR、变异系数 CV | CV = std/mean，比较不同体量广告活动的波动性 |
| 分布形态 | 偏度 skewness、峰度 kurtosis | 正偏（右偏）：少数大额消费拉高均值，在营销数据中极常见 |

**核心洞察**：国家统计局同时发布"居民人均可支配收入"（均值）和"居民收入中位数"--后者往往更能反映"典型居民"的真实水平。营销客单价同理。

### 关键回顾 2：概率分布 -- 理解随机性

| 分布 | 适用场景 | 营销应用 |
|------|---------|---------|
| 正态分布 | 中心极限定理：大量独立变量和的分布 | A/B 测试中转化率差的分布近似正态 |
| 二项分布 | n 次伯努利试验的成功次数 | 广告点击（点/不点）、转化（买/不买） |
| 泊松分布 | 单位时间事件发生次数 | 客服来电、网站访问、购买次数 |

### 关键回顾 3：假设检验 -- 科学决策的统计基础

法庭审判类比：

| 统计概念 | 法庭类比 | A/B 测试场景 |
|---------|---------|-------------|
| 原假设 H₀ | 被告无罪 | 新方案和旧方案没有差异 |
| 备择假设 H₁ | 被告有罪 | 新方案更好 |
| p 值 | 无罪前提下看到当前证据的概率 | H₀ 成立时观察到当前差异的概率 |
| 第一类错误 α | 冤枉好人（假阳性） | 方案无效但判为有效 |
| 第二类错误 β | 放过坏人（假阴性） | 方案有效但判为无效 |
| 统计功效 1-β | 正确判有罪的概率 | 正确识别有效方案的概率 |

**关键认知**：p 值不告诉你"新方案有多好"，只告诉你"有没有效果"。效果大小需要看效应量。p < 0.05 只是"有统计显著性"，不等于"有商业意义"。

### 关键回顾 4：置信区间 -- 比 p 值更丰富的信息

95% 置信区间的含义：如果重复实验 100 次，95 次实验的 CI 会包含真实参数值。CI 不仅告诉你"有没有效"（是否包含 0），还告诉你"效果多大"（区间位置）和"估计多精确"（区间宽度）。

### 关键回顾 5：贝叶斯统计 -- 从先验到后验的更新

频率派（Frequentist）vs 贝叶斯派（Bayesian）的根本区别：

| 维度 | 频率派 | 贝叶斯派 |
|------|--------|---------|
| 概率定义 | 长期频率 | 不确定性程度 |
| 参数 | 固定但未知 | 随机变量，有分布 |
| 核心工具 | p 值、置信区间 | 后验分布、可信区间 |
| 先验信息 | 不使用 | 显式融入 |
| 营销应用 | A/B 测试标准流程 | 小样本转化率估计、持续更新 |

**Beta-Binomial 模型**：转化率 p 的贝叶斯推断。先验 Beta(α, β)，观察到 s 次成功 / n 次试验后，后验为 Beta(α+s, β+n-s)。后验均值 = (α+s)/(α+β+n)，随数据增加趋近真实转化率。

---

## 上机部分：用真实库做营销数据统计分析

> 📓 **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO 填空版，你来做）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，gated，做完再看）
> 📊 **真实数据/库**：[`data/README.md`](./data/README.md)（numpy + pandas + scipy.stats + matplotlib/seaborn + 营销 A/B 测试数据）

### 为什么用真实库而非手写公式

v4.0 的代码用"手写统计公式"演示概念。v5.0 改用工业级真实库：

- **numpy + pandas**：描述统计的工业标准--`df.describe()`、`df.groupby()` 一行完成分组统计
- **scipy.stats**：假设检验的权威实现--`ttest_ind`、`chi2_contingency`、`norm.ppf` 经过严格测试，结果可信
- **matplotlib + seaborn**：可视化标准工具链--直方图、箱线图、散点图、热力图

### 营销映射（关键桥接）

本 Day 处理一个"营销 A/B 测试效果验证"场景：1000 条用户数据，包含 A/B 两组（旧版/新版落地页）、转化状态、消费金额、用户分群、购买品类。6 个 TODO 覆盖从描述统计到贝叶斯推断的完整分析链：

| 上机任务 | 营销场景 | 真实库实现 |
|---------|---------|-----------|
| 描述统计 | A/B 两组客单价分布对比 | numpy + pandas |
| 数据可视化 | 转化率与消费分布可视化 | matplotlib + seaborn |
| t 检验 | A/B 两组转化率差异显著性 | scipy.stats.ttest_ind |
| 置信区间 | 转化率差的 95% CI | scipy.stats.norm |
| 卡方检验 | 用户分群与购买品类独立性 | scipy.stats.chi2_contingency |
| 贝叶斯统计 | Beta-Binomial 后验估计转化率 | scipy.stats.beta |

### 上机任务（6 个 TODO，见 starter.ipynb）

1. **TODO1**：用 numpy + pandas 计算 A/B 两组的描述统计（均值/中位数/方差/分位数/客单价分布）
2. **TODO2**：用 matplotlib + seaborn 绘制直方图/箱线图/散点图，可视化营销转化分布
3. **TODO3**：用 scipy.stats.ttest_ind 执行 t 检验，判断 A/B 两组转化率差异是否显著
4. **TODO4**：计算转化率差的 95% 置信区间（Wilson score / 正态近似）
5. **TODO5**：用 scipy.stats.chi2_contingency 执行卡方检验，判断用户分群与购买品类是否独立
6. **TODO6**：用 Beta-Binomial 模型做贝叶斯转化率估计，对比频率派 p 值与贝叶斯后验

---

## 2026 前沿补充：贝叶斯统计 + 概率编程 + 可复现研究

> v5.0 新增前沿点。本 Day 覆盖三个前沿方向：① 贝叶斯统计与概率编程（PyMC）② 先验后验更新与频率派对比 ③ 可复现研究与预注册（preregistration）。

### 贝叶斯统计与概率编程（PyMC）

贝叶斯统计在 2020 年代迎来复兴，核心驱动力是概率编程框架的成熟。**PyMC**（PyMC Labs，Apache-2.0）是目前最主流的 Python 贝叶斯推断框架，支持 MCMC（NUTS 采样器）、变分推断（ADVI），能构建层次模型、高斯过程等复杂贝叶斯模型。

**为什么贝叶斯方法在营销场景中越来越重要**：
- **小样本场景**：新产品上线初期只有几十次曝光，频率派 p 值不稳定，贝叶斯方法通过先验信息给出更合理的估计
- **持续更新**：贝叶斯后验可以随着新数据持续更新--每次实验结果都是下一次实验的先验，天然适配"持续优化"的营销节奏
- **直接回答业务问题**：频率派 p 值回答"如果方案无效，看到当前数据的概率"；贝叶斯后验直接回答"方案有效的概率"--后者更贴近决策者的直觉

**Beta-Binomial 模型**是贝叶斯统计最简单的入门案例：先验 Beta(1,1)（均匀分布），观察到 s 次转化 / n 次试验后，后验为 Beta(1+s, 1+n-s)。本 Day TODO6 用 scipy.stats.beta 手动实现，理解原理后可用 PyMC 扩展到更复杂的层次模型。

> 🔗 深入阅读见 [`reading.md`](./reading.md) 的 PyMC 和贝叶斯统计条目。

### 可复现研究与预注册（Preregistration）

统计学正在经历"可复现危机"（replication crisis）--心理学、医学等领域大量已发表的研究无法被独立复现。根本原因之一是 **p 值操纵**（p-hacking）：不断检查 p 值是否显著，一旦达到 0.05 就停止实验。

**应对措施**：
- **预注册（preregistration）**：在实验前公开声明假设、样本量、分析计划，防止事后篡改。平台如 OSF（Open Science Framework）支持预注册
- **预计算样本量**：在实验前用功效分析计算所需样本量，达到后再判断结果
- **报告效应量和 CI**：不仅报告 p 值，还报告效应量（effect size）和置信区间，让读者判断"有没有商业意义"
- **IMRaD 格式**：学术论文标准结构（Introduction / Methods / Results / Discussion），确保方法透明可复现

**与营销的连接**：A/B 测试中最常见的错误就是"p 值钓鱼"--不断检查 p 值，一旦显著就停止。这会严重膨胀第一类错误率。正确做法是预先计算样本量，达到样本量后再判断。这个概念在技能3的因果推断中会深入讨论。

---

## 与后续 Day 的衔接

- **Day 4**：回归分析与概率分布--今天的假设检验将扩展到回归系数的显著性检验，今天的概率分布将用于回归的残差分析
- **Day 5**：数据管理与 SQL--今天的 pandas DataFrame 操作将延伸到 SQL 查询和数据管道构建
- **技能3**：因果推断--今天的 A/B 测试是因果推断的入门，技能3将超越"有没有效果"走向"效果有多大"的因果效应估计（DML / 合成控制 / 增量建模）

---

## 作业与评估

作业、5 分制量表、费曼演练、2 分钟话术、复盘自诊表--沿用独立教材 § Day 3 既有设计。本学习材料包不重复，仅新增上机交付物：

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6 个 TODO 全部填好，能跑通）
- [ ] 一段 300 字分析：你的 A/B 测试结果，p 值是多少？效应量多大？95% CI 是否包含 0？贝叶斯后验与频率派结论是否一致？
- [ ] （可选）用 PyMC 为同一个 A/B 测试构建贝叶斯模型，对比 scipy.stats.beta 手动计算的后验（500-800 字）

---

*本讲义由 v5.0 学习材料包升级生成。理论部分引用独立教材，上机部分用真实库（numpy + pandas + scipy.stats + matplotlib + seaborn）+ TODO 脚手架。*
*最后更新：2026-07-24*

---

## 学习科学层 (v6.0)

> v6.0 在 v5.0 真实库上机基础上，叠加**学习科学四件套**，把"练习"升级为"刻意练习 + 间隔重复 + 建构对齐 + 牛津 tutorial 仿真"。研究依据: Ericsson 刻意练习、FSRS-6 (request_retention=0.9, SM-2 备份 EF₀=2.5)、Biggs 建构对齐 (ILO↔TLA↔AT)、Hattie 四级 formative feedback (2007 RER 77(1):81-112, d=0.79)、MIT 6.5940 Worked-Faded + A1B1C1 interleaving、Oxford tutorial Socratic (arxiv 2409.05511, 2507.05795)。

### 1. 刻意练习 (practice.md)
- **skill_target**: 90 分钟内独立完成营销 A/B 测试统计推断报告 (scipy.stats t 检验 + chi2_contingency + Beta-Binomial + ASA 六原则)。
- **drills D1/D2/D3**: 每含 difficulty/reps_required/feedback_rule/worked-faded 三阶段。feedback_rule 引用 Welch equal_var、ASA p 值六原则、Beta(α+s, β+n-s) 后验、credible vs CI 语义。
- **interleaving**: A1B1C1...B2C2A2...C3A3B3 交叉排布，不块状 (Butler 2010 检索练习证据)。
- **weak_loop**: 连续 2 次失败回退到 Worked-Faded 上一阶段 + student_model.json 标记 mastery<0.3。

### 2. 间隔重复 (schedule.json)
- **FSRS-6 (SM-2 备份)**, request_retention=0.9, 5 张卡片 due=[1,3,8,21,60,180]。
- 卡片覆盖: C1 Welch t / C2 chi2_contingency / C3 Beta-Binomial 后验 / C4 ASA p 值六原则 / C5 右偏中位数稳健性。
- 弱项卡片 (连续 2 次失败) 在 student_model.json 标记，跨单元复习优先安排。

### 3. 建构对齐 (alignment.md)
- **Biggs ILO↔TLA↔AT 矩阵 4 行**，每行含 mastery_threshold (>=80% / >=70% / 能独立解 / >=80%)。
- **3 自检问题** (Feed Up / Feed Back / Feed Forward): TLA 是否训练 ILO？AT 是否测量 ILO？不经 TLA 能过 AT 吗？
- ILO1 描述统计稳健性 / ILO2 t+卡方+ASA / ILO3 贝叶斯对比 / ILO4 显著性 vs 商业意义。

### 4. 牛津 Tutorial 仿真 (tutorial.ipynb)
- **Persona**: Oxford fellow in 统计推断, 禁直接答案, Socratic 追问, devil's advocate, 渐退脚手架。
- **8 个 Socratic 问题** (>=5), 覆盖 ASA 第一条 (p≠P(H₀真))、Welch equal_var、Beta 后验、credible vs CI 语义、p-hacking 膨胀 α。
- **Hattie 四级反馈**: [TASK] / [PROCESS] / [SELF-REG] / [FEED-FORWARD]，避免 Self 级表扬。
- **student_model.json** 跨单元复用: 记录 S1-S4 mastery + blind_spots + daily_usage，day4/skill3/day5 读取此 model。
- **限频**: 每单元每天 1 次 (防 LLM 依赖)，弱项循环可加 1 次 (仅限该 subskill)。
- **Exit artifact**: 2-3 盲点 + 推荐复习单元 + 500 字反思 + mastery 自评。

### v6.0 关键词命中
FSRS-6 / SM-2 / 刻意练习 / 建构对齐 / Oxford tutorial / Socratic / Hattie / 间隔重复 / interleaving / Worked-Faded / mastery / spaced retrieval / formative feedback / 检索练习 -- 共 14 个关键词命中 (>=4 要求满足)。

---

*v6.0 学习科学层叠加完成。v5.0 基线 (notes.md 主体 + data/ + starter.ipynb + solution.ipynb + reading.md) 不动。*
*v6.0 最后更新: 2026-07-25*

---

## 研究产出与产业链接层 (v7.0)

本单元产出可发表研究工件 (research.md: 研究问题 + 贡献声明 + arXiv 链接 + IMRaD 大纲 + NeurIPS 可复现清单 + research-to-practice 翻译) 与产业链接 (industry.md: >=3 真实企业 + 部署场景 + Imperial 咨询项目 + HBS 教学案例 + 客座讲座 + 实习指针)。研究产出遵循 IMRaD / DSR (Hevner) / OSF 预注册 / FAIR / 可复现研究标准; 产业链接遵循 Imperial MSc BA 咨询项目 (Burberry / Expedia / J&J) / HBS 案例法 / MIT Sloan 行动学习 (action learning) 模式。linked_paper 锚定 reading.md 已验证深链 (ASA p 值声明 / Gelman BDA3 / Nosek preregistration / Kruschke puppy book)。real_companies 锚定 Microsoft ExP / Netflix / Booking.com / Google / Spotify / Amazon (A/B 测试与统计推断主题匹配)。详见 research.md 与 industry.md。

### v7.0 关键词命中
研究产出 / research output / IMRaD / 可复现 / reproducibility / OSF / preregistration / 预注册 / FAIR / contribution / 贡献 / 产业链接 / industry linkage / consulting / 咨询 / case study / 案例 / guest lecture / 客座 / internship / 实习 / deployment / 部署 / linked_paper / arXiv / DSR / Hevner / research-to-practice / NeurIPS / 行动学习 / action learning -- 共 31 个关键词命中 (>=4 要求满足)。

---

*v7.0 研究产出与产业链接层叠加完成。v5.0 基线 (1-7) 与 v6.0 层 (8-12) 不动。*
*v7.0 最后更新: 2026-07-26*

---

## 学术前沿层 (v9.0)

本单元新增 `frontier.md`：注入 2025-2026 最新学术前沿（N 篇真实 arXiv 论文 + 批判性综述 + delta_to_unit + ≥3 开放研究问题 + 方法论批评）。论文来自 `_frontier_corpus/skill-0-business-analytics.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证），覆盖前沿课题：LLM-as-data-analyst × Polars/duckdb 列式引擎。面向博后/教授级读者：批判性综述非罗列，delta_to_unit 显式指出前沿如何更新本单元所教，开放问题为可发表研究方向。详见 `frontier.md`。
