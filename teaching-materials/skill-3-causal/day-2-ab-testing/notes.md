# 技能3 · Day 2：实验设计与 A/B 测试统计 · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 技能3 因果推断与规模实验 · Day 2
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：随机化如何把"相关"变成"因果"？A/B 测试的统计底气从何而来？
> **v5.0 升级点**：① 新增真实 RCT 数据上机（NSW 实验数据）② 新增 TODO 填空式起始笔记本 ③ Notebook 化 ④ 深链阅读 ⑤ 2026 前沿（CUPED 方差缩减，A/B 工业标准）

---

## 学习目标（学完你能做到）

1. 能在**真实 RCT 数据**（NSW 职业培训实验）上验证随机化均衡性，解释为什么 RCT 的均值差 = ATE（无需后门调整）
2. 能为营销 A/B 测试计算所需样本量（给定基线转化率、MDE、α、power）
3. 能完成比例 Z 检验 / t 检验、置信区间、事后功效分析，正确解读统计显著性（不被"p<0.05"绑架）
4. 能用 CUPED 方差缩减技术提升 A/B 测试灵敏度，理解"相同样本量检测更小效应"的工业实践

---

## 理论部分：精炼索引（详见独立教材）

> Day 2 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_技能3_因果推断与规模实验.md` § Day 2](../../AI原生化商业博士_独立教材_技能3_因果推断与规模实验.md)（2.1–2.5 节，已包含 RCT 原理/样本量/检验/准实验设计）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：为什么 RCT 的均值差 = ATE

**Day 1 的教训**：观测数据中，朴素均值差 = ATE + Bias（混杂偏差），需后门调整。

**RCT 的数学保证**：随机化使处理组和对照组在所有特征（可观测 + 不可观测）上的期望分布相同：

$$E[Y(0)|T=1] = E[Y(0)|T=0] = E[Y(0)]$$

因此：

$$E[Y^{obs}|T=1] - E[Y^{obs}|T=0] = E[Y(1)] - E[Y(0)] = \text{ATE}$$

**随机化 = do 操作的物理实现**（Day 1 因果阶梯 L2）。不需要后门调整、不需要 DoWhy--简单的均值差就是无偏的 ATE 估计。这是 A/B 测试被视为"因果推断金标准"的根本原因。

但 A/B 测试仍有统计挑战：**样本量够不够？功效足不足？显著性怎么判？** 这就是今天的核心。

### 关键回顾 2：样本量计算

比例指标（如转化率）A/B 测试每组样本量：

$$n = \frac{(z_{\alpha/2} + z_{\beta})^2 \cdot [p_1(1-p_1) + p_2(1-p_2)]}{(p_2 - p_1)^2}$$

- $p_1$ = 基线转化率，$p_2 = p_1 + \text{MDE}$（最小可检测效应）
- $z_{\alpha/2}$ = 显著性边界（α=0.05 时 ≈1.96），$z_{\beta}$ = 功效边界（power=0.80 时 ≈0.84）

**直觉**：效应越小、方差越大、要求越严（α 小、power 高），所需样本越多。营销实践中"贴片广告 +0.1% CTR 提升"需要的样本量远大于"优惠券 +5% 转化提升"。

### 关键回顾 3：显著性检验与两类错误

| | H0 为真 | H0 为假 |
|---|---|---|
| 拒绝 H0 | **第一类错误（假阳性）**= α | 正确发现（功效 = 1-β） |
| 不拒绝 H0 | 正确 | **第二类错误（假阴性）**= β |

- **p 值**：在 H0 为真时观察到当前或更极端结果的概率。p < α 拒绝 H0。
- **置信区间**：95% CI 不包含 0 等价于 p < 0.05。
- **营销警示**：p<0.05 不等于"效应重要"。大样本下微小效应也显著；要看效应大小 + 置信区间 + 业务意义。

### 关键回顾 4：CUPED 方差缩减

A/B 测试灵敏度取决于方差：方差越大，标准误越大，越难检测真实效应。

**CUPED**（Deng et al. 2013）利用实验前协变量 X 缩减 Y 的方差：

$$\theta = Y - \beta \cdot (X - \bar{X}), \quad \beta = \frac{\text{Cov}(Y, X)}{\text{Var}(X)}$$

方差缩减比例 = 1 - ρ²（ρ 是 Y 与 X 的相关系数）。

**NSW 应用**：`re75`（1975 收入，实验前）与 `re78`（1978 收入，实验后）高度相关 -> 理想 CUPED 协变量。
**营销应用**：用用户实验前活跃度/消费作 CUPED 协变量，相同样本量检测更小效应 -> 直接节省实验成本。

### 关键回顾 5：准实验设计（当无法随机化时）

| 方法 | 核心假设 | 营销场景 |
|------|---------|---------|
| DiD 双重差分 | 平行趋势 | A 城市上线 AI 推荐，B 城市没有，比较 GMV 变化差异 |
| RDD 断点回归 | 断点处局部随机 | 活跃度>80 分推送个性化内容，在 80 分附近做 RDD |
| ITS 中断时间序列 | 无干预时趋势稳定 | 全量上线新广告算法后，分析 ROI 时间序列趋势变化 |

---

## 上机部分：在真实 RCT 数据上做 A/B 测试统计分析

> 📓 **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO 填空版，你来做）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，gated，做完再看）
> 📊 **真实数据集**：[`data/README.md`](./data/README.md)（NSW 职业培训实验真实 RCT 数据）

### 为什么用 NSW 的 RCT 视角

Day 1 把 NSW 当**观测数据**（处理组与观测对照组混杂严重，需后门调整）。今天把 NSW 当它本来的面目--**真实随机对照试验**--做 A/B 测试统计分析。同一数据集，两个视角，让你直观看到"随机化消除混杂"的威力：Day 1 的均值差有偏，今天的均值差无偏。

### 营销映射

| NSW 变量 | 营销映射 | 角色 |
|---------|---------|------|
| `treat` | 是否看到新广告/收到优惠券 | 处理 T |
| `re78` | 转化率/GMV/客单价 | 结果 Y（连续，t 检验） |
| `re78 > 0`（衍生） | 是否转化（0/1） | 结果 Y（二值，比例 Z 检验） |
| `re75` | 实验前历史消费 | CUPED 协变量 |
| `age`,`education`,... | 用户画像 | 协变量 X（均衡性检验） |

### 上机任务（6 个 TODO，见 starter.ipynb）

1. **TODO1**：加载真实 NSW RCT 数据
2. **TODO2**：验证 RCT 均衡性（逐变量 t 检验，p>0.05 表示均衡）
3. **TODO3**：样本量计算（基线 5%、MDE=1% 场景）
4. **TODO4**：A/B 显著性检验（t 检验 + 比例 Z 检验）
5. **TODO5**：置信区间 + 事后功效分析
6. **TODO6（可选）**：CUPED 方差缩减，对比前后 t/p

---

## 2026 前沿补充：CUPED 方差缩减（A/B 测试工业标准）

> v5.0 新增前沿点。CUPED（Deng et al. 2013, WSDM）是 A/B 测试的**工业标准方差缩减技术**，在微软/谷歌/亚马逊/Netflix 等公司广泛使用，2026 年仍是业界最佳实践。

**核心思想**：利用实验前的协变量 X（与结果 Y 相关但不受处理影响）调整 Y，缩减方差：

$$\theta = Y - \beta \cdot (X - \bar{X}), \quad \beta = \text{Cov}(Y,X)/\text{Var}(X)$$

方差缩减比例 = 1 - ρ²。在 NSW 中，`re75` 与 `re78` 高度相关，是理想 CUPED 协变量。

**营销应用**：广告 A/B 测试中，用用户实验前的活跃度/消费/点击数据作为 CUPED 协变量，可在相同样本量下检测更小的效应，或用更少样本达到相同灵敏度 -> 直接节省实验成本。这是 2026 年营销 A/B 测试从"能做"走向"高效"的关键技术。

参考：Deng, Xu, Kohavi, Walker (2013), WSDM. DOI: 10.1145/2433396.2433413

> 🔗 深入阅读见 [`reading.md`](./reading.md) 的 CUPED 条目。

---

## 与后续 Day 的衔接

- **Day 1**：因果推断基础（观测数据后门调整）--今天是实验数据，对照"随机化消除混杂"
- **Day 3**：观测数据的因果推断（PSM/DiD/IV/RDD）--今天能随机化，Day 3 处理不能随机化的情况（准实验的严格版）
- **Day 5**：规模实验与营销应用--今天的单指标 A/B 升级为营销归因/增量/规模实验

---

## 作业与评估

作业、5 分制量表、费曼演练、2 分钟话术、复盘自诊表--沿用独立教材 § Day 2 既有设计。本学习材料包不重复，仅新增上机交付物：

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6 个 TODO 全部填好，能跑通）
- [ ] 一段 300 字分析：NSW 的 RCT 均衡性检验结果 vs Day 1 观测数据的不均衡，说明了什么？
- [ ] （可选）CUPED 缩减了多少方差？对营销 A/B 测试的实践意义是什么？

---

*本讲义由 v5.0 学习材料包升级生成。理论部分引用独立教材，上机部分用真实 RCT 数据 + TODO 脚手架。*
*最后更新：2026-07-24*

---

## 学习科学层 (v6.0)

> Loop Engineering v6.0 升级: 在 v5.0 真实即严谨的基础上, 引入学习科学四件套, 把"练习"升级为"刻意练习 (deliberate practice) + 间隔重复 (spaced retrieval) + 建构对齐 (constructive alignment) + 牛津tutorial (Socratic) 仿真"。

### 1. 刻意练习 (Ericsson + MIT)
- 新增 `practice.md`: skill_target + 3 subskills (均衡性/样本量/CUPED) + 3 drills (D1/D2/D3, 每含 difficulty/reps_required/feedback_rule/worked-faded 三阶段)
- 渐退示例 (Worked-Faded): 完整示范 -> 部分填空 -> 独立解, 符合 4C/ID 认知负荷理论
- 弱项循环 (weak_loop): 连续 2 次失败回退到 worked example + tutorial Socratic 追问
- 交叉 (interleaving): A1B1C1...B2C2A2...C3A3B3 不块状排布, 穿插 Day1/Day3 旧知识, 强化方法选择 (ILO4)

### 2. 间隔重复 (FSRS-6 / SM-2)
- 新增 `schedule.json`: 5 张卡片, 每张 due=[1,3,8,21,60,180], ef0=2.5, request_retention=0.9
- 算法: FSRS-6 主 (21 weights), SM-2 备份 (EF₀=2.5, I(1)=1, I(2)=6)
- 卡片覆盖 ILO1-ILO3: RCT 均值差=ATE / 样本量公式 / CUPED 1-ρ² / 均衡性检验 / p<0.05 陷阱
- mastery 阈值: 首次复习正确率 >=60% (FSRS-6 EF 不下降)

### 3. 建构对齐 (Biggs ILO↔TLA↔AT)
- 新增 `alignment.md`: 4 行矩阵 (ILO1-ILO4) + mastery_threshold + 3 自检 (Feed Up/Back/Forward)
- 防抄机制: progressive_project M3 (300字无标准答案) + tutorial Socratic 口头辩护 + diagnostic 前测
- Biggs 3 问: TLA 是否训练 ILO? AT 是否测量 ILO? 不经 TLA 能过 AT 吗?

### 4. 牛津 Tutorial LLM 仿真 (Oxford + Hattie formative feedback)
- 新增 `tutorial.ipynb`: 6 cells
  - persona: Oxford fellow, Socratic 追问, 禁直接答案, devil's advocate
  - pre-task 强制 retrieval practice (Butler 2010: 检索 68% vs 重学 44%)
  - 4 轮 Socratic loop (静态 if/else, 不调 API), 每轮降 scaffold
  - student_model.json 跨单元复用 (记录掌握度/盲点)
  - Hattie 四级反馈 [TASK]/[PROCESS]/[SELF-REG]/[FEED-FORWARD] (避免 Self 级表扬)
  - 限频 (1次/天) + exit artifact (2-3 盲点 + 推荐复习单元)

### 研究依据
- Ericsson 刻意练习 5 要素 (合理难度+即时反馈+重复+专注+脚手架)
- FSRS-6 (request_retention=0.9) + SM-2 备份 (EF₀=2.5)
- Biggs 建构对齐 ILO↔TLA↔AT
- Hattie (2007 RER 77(1):81-112) 3 问 × 4 级 formative feedback
- Butler 2010 retrieval practice (推断题 68% vs 重学 44%)
- Oxford tutorial 1对1-3 + 每周 + 强制 + 口头辩护
- MIT OpenLearning: Worked-Faded + interleaving A1B1C1 + 提取练习

### 与 v5.0 的关系
v5.0 基线 (notes.md/data/starter.ipynb/solution.ipynb/reading.md) 不动, 本节仅追加。v6.0 四件套 (practice.md/schedule.json/alignment.md/tutorial.ipynb) 是 v5.0 之上的学习科学层, 让"练过"变成"掌握 (mastery)"。

*最后更新：2026-07-25 (v6.0 学习科学层追加)*

---

## 研究产出与产业链接层 (v7.0)
本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+arXiv链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。详见 research.md 与 industry.md。
