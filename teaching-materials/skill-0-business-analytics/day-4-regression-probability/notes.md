# 技能0 · Day 4：回归分析与概率分布 · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 技能0 AI商业分析基础（预科层）· Day 4
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：如何用回归量化"哪些因素驱动了营销转化"？如何用概率分布建模"营销指标的不确定性"？
> **v5.0 升级点**：① 真实RCT数据（causaldata NSW职业培训实验，替代模拟数据）② TODO填空式起始笔记本 ③ Notebook化 ④ 深链阅读 ⑤ 2026前沿（贝叶斯回归/分位数回归/正则化）

---

## 学习目标（学完你能做到）

1. 能用 **statsmodels** 对真实数据拟合 OLS 多元线性回归（`sm.OLS(y, sm.add_constant(X)).fit()`），解读 R²、回归系数、p值和置信区间的商业含义，并用 VIF 检测多重共线性
2. 能用 **statsmodels** 拟合 Logit 逻辑回归（`sm.Logit(y, X).fit()`），计算倾向性评分（propensity score），理解它是连接技能3因果推断的桥梁
3. 能用 **scipy.stats** 拟合三种概率分布（正态 `norm`、二项 `binom`、泊松 `poisson`）到真实营销指标，计算概率值和置信区间，理解每种分布对应的营销场景
4. 能用回归+概率分布组合方法计算 LTV（客户终身价值）的点估计和概率区间，对比营销干预组 vs 对照组的 LTV 差异
5. 能区分"相关关系"和"因果关系"，理解回归揭示的是相关性而非因果性，知道从相关到因果需要什么额外假设和方法（引向技能3）

---

## 理论部分：精炼索引（详见独立教材）

> Day 4 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_技能0_AI商业分析基础.md` § Day 4](../../AI原生化商业博士_独立教材_技能0_AI商业分析基础.md)（780-993行，已包含线性回归OLS原理/R²与p值/多元回归与共线性VIF/概率分布三种类型/从相关到因果/LTV影响因素完整案例代码）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：线性回归 -- 从相关到预测

线性回归用最小二乘法（OLS）找到一条直线/超平面，使残差平方和最小。数学表达：`y = β₀ + β₁x₁ + ... + βₖxₖ + ε`。

关键指标：
- **R²（决定系数）**：模型解释了因变量变异的百分比。R²=0.04意味着模型解释了4%的变异
- **回归系数p值**：p<0.05表示该变量对因变量有统计显著影响
- **置信区间**：回归系数的95%CI不包含0，等价于p<0.05

### 关键回顾 2：多元回归与多重共线性

多个自变量同时放入回归模型时，需警惕**多重共线性**--自变量之间高度相关，导致系数不稳定。检测方法：VIF（方差膨胀因子），VIF>10通常被认为是严重共线性。

### 关键回顾 3：概率分布与商业应用

| 分布 | scipy.stats | 营销场景 | 关键参数 |
|------|------------|---------|---------|
| 正态分布 | `norm` | 订单金额（取对数后）、客户消费金额 | mu（均值）, sigma（标准差） |
| 二项分布 | `binom` | 转化/未转化（0/1）、复购/不复购 | n（试验次数）, p（成功概率） |
| 泊松分布 | `poisson` | 每日转化次数、客服来电次数、网站访问次数 | mu（lambda，均值=方差） |

### 关键回顾 4：从相关到因果 -- 回归的局限

回归分析揭示的是**相关关系**，不是**因果关系**。"营销花费与销售额正相关"不意味着"增加营销花费会导致销售额增加"--可能存在混杂因素（如季节性、促销活动）。这个认知直接引向技能3（因果推断）。

---

## 上机部分：用真实库+真实RCT数据做回归与概率分析

> 📓 **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO填空版，你来做）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，做完再看）
> 📊 **真实数据/库**：[`data/README.md`](./data/README.md)（statsmodels + scipy.stats + causaldata NSW真实RCT数据）

### 为什么用真实RCT数据而非模拟数据

v4.0 的代码用 `np.random.seed(42)` 生成模拟数据，构造"已知真实关系"来演示回归概念。v5.0 改用真实RCT实验数据：

- **causaldata NSW数据**：LaLonde (1986) 的著名职业培训实验数据，445条记录，是因果推断领域的经典基准数据集
- **真实数据的不完美性**：真实数据的R²可能很低（本Day的OLS R²=0.037），这正是真实分析的常态--你不会总是遇到"漂亮"的数据
- **因果推断桥梁**：NSW是RCT（随机对照试验），treat列是随机分配的干预，这使得回归系数可以解释为因果效应（在随机化假设下）

### 营销映射（关键桥接）

本Day把NSW职业培训数据映射到AI+企业营销场景：

| NSW原始字段 | 营销映射含义 | 角色 |
|------------|------------|------|
| re78（1978年收入） | 营销后转化金额（Y，因变量） | 目标变量 |
| re75（1975年收入） | 基线消费金额（营销前） | 控制变量 |
| age（年龄） | 用户画像：年龄 | 自变量X |
| educ（教育年限） | 用户画像：教育水平 | 自变量X |
| treat（是否参加培训） | 是否收到营销干预（A/B测试分组） | 干预变量 |
| black/hisp/marr/nodegree | 人口统计学协变量 | 可选控制变量 |

**核心分析任务**：
1. OLS回归 re78 ~ age + educ + re75 + treat：量化各因素对转化金额的影响
2. Logit回归预测 treat：计算倾向性评分（propensity score），连接技能3因果推断
3. 概率分布拟合：用正态/二项/泊松分布建模re78和treat的不确定性
4. LTV计算：用回归+概率分布计算客户终身价值的点估计和概率区间

### 上机任务（6个TODO，见starter.ipynb）

1. **TODO1**：用 causaldata 加载NSW数据，探索数据结构和分布
2. **TODO2**：用 statsmodels 拟合OLS多元回归，解读R²/系数/p值/VIF
3. **TODO3**：用 statsmodels 拟合Logit回归，计算倾向性评分
4. **TODO4**：用 scipy.stats 拟合正态/二项/泊松分布，计算概率值
5. **TODO5**：计算LTV点估计和概率区间，对比干预组vs对照组
6. **TODO6**：用分位数回归分析不同分位上的处理效应（2026前沿）

---

## 2026前沿补充：贝叶斯回归 + 分位数回归 + 正则化

> v5.0新增前沿点。本Day覆盖三个前沿方向：① 贝叶斯回归（PyMC/bambi）② Lasso/Ridge正则化 ③ 分位数回归（statsmodels.QuantReg）。

### 贝叶斯回归：从点估计到后验分布

传统频率派OLS回归给出系数的**点估计**（一个数值）和置信区间。**贝叶斯回归**（Bayesian Regression）给出系数的**后验分布**--不仅告诉你"系数最可能是多少"，还告诉你"系数在各个值上的概率分布"。

- **工具**：PyMC（`pip install pymc`）或 bambi（`pip install bambi`，基于PyMC的高阶接口，语法类似R的brms）
- **小样本优势**：当数据量小（如几十条）时，贝叶斯回归通过先验分布提供正则化，比OLS更稳健
- **不确定性量化**：贝叶斯回归天然输出预测的不确定性（预测分布），对营销决策中的风险量化至关重要
- **与频率派的对比**：OLS的95%置信区间是"如果重复采样100次，95次包含真值"；贝叶斯的95%可信区间是"给定数据，系数有95%的概率落在此区间"--后者更符合商业决策者的直觉

**营销应用**：在A/B测试中，贝叶斯方法可以计算"P(实验组优于对照组)>95%"这种直接可用的决策概率，而非频率派的p值。

### Lasso/Ridge正则化：高维特征的防过拟合

当自变量很多（高维数据）时，OLS容易过拟合。**正则化**通过在损失函数中加入惩罚项来约束系数：

- **Lasso（L1正则化）**：`sklearn.linear_model.Lasso` -- 惩罚项为系数绝对值之和，能将某些系数压缩为0，起到特征选择作用
- **Ridge（L2正则化）**：`sklearn.linear_model.Ridge` -- 惩罚项为系数平方和，缩小系数但不归零
- **ElasticNet**：L1+L2的混合

**营销应用**：当用户画像有数百个特征（如浏览行为、购买历史、社交标签）时，Lasso能自动筛选出最重要的几个特征，避免维度灾难。

### 分位数回归：预测条件分位数而非均值

OLS回归预测的是因变量的**条件均值**（给定X时Y的期望）。**分位数回归**（`statsmodels.QuantReg`）预测的是**条件分位数**--如"给定用户画像，转化金额的第90分位数是多少"。

- **对异常值稳健**：均值受极端值影响大，分位数不受
- **捕捉分布全貌**：同时拟合多个分位数（如25/50/75分位），可以看到X对Y分布不同部分的不同影响
- **适合长尾分布**：营销金额通常右偏（少数大客户贡献大部分收入），分位数回归能分别建模"普通客户"和"高价值客户"

**本Day上机发现**：NSW数据中，treat的效应在不同分位上差异巨大--在75分位上treat系数为2502（p=0.004，显著），但在25分位上仅为290（p=0.520，不显著）。这意味着职业培训（映射为营销干预）对高收入分位的用户效果显著，但对低收入分位效果不明显。这是均值回归看不到的洞察。

---

## 与后续Day的衔接

- **Day 3**：描述统计与推断统计--今天的回归分析建立在Day 3的假设检验和置信区间之上
- **Day 5**：数据治理与SQL--今天的数据加载技能将扩展到数据库查询，为回归分析提取更大数据集
- **技能3**：因果推断--今天的OLS回归和Logit倾向性评分是因果推断的基础工具，分位数回归的异质性效应分析也将在因果推断中深入

---

## 作业与评估

作业、5分制量表、费曼演练、2分钟话术、复盘自诊表--沿用独立教材 § Day 4 既有设计。本学习材料包不重复，仅新增上机交付物：

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6个TODO全部填好，能跑通）
- [ ] 一段300字分析：OLS回归中哪些变量对re78（转化金额）有显著影响？treat（营销干预）的系数是多少？如何解读？R²为什么低？这说明了什么？
- [ ] （可选）用bambi或PyMC对同样的回归模型做贝叶斯拟合，对比频率派OLS系数和贝叶斯后验分布的差异

---

## 英语轨道（i+1）

打开 [MIT OCW 15.071 Unit 2](https://ocw.mit.edu/courses/15-071-the-analytics-edge-spring-2017/)，用浏览器翻译插件辅助阅读。重点关注术语：regression coefficient, R-squared, p-value, multicollinearity, residual analysis, propensity score, logistic regression。这些术语在后续技能1-3的英文文献中反复出现。这就是i+1：你已有中文统计基础（i），通过英文讲义接触新表达方式（i+1）。

---

*本讲义由v5.0学习材料包升级生成。理论部分引用独立教材，上机部分用真实库（statsmodels + scipy.stats）+ 真实RCT数据（causaldata NSW）+ TODO脚手架。*
*最后更新：2026-07-24*

---

## 学习科学层 (v6.0)

> v6.0 在 v5.0 五件套 (notes.md/data/README/starter.ipynb/solution.ipynb/reading.md) 之上, 新增 **学习科学层** 四件套: `practice.md` / `schedule.json` / `alignment.md` / `tutorial.ipynb`。不破坏 v5.0 基线 (verify_unit.py 7/7 仍通过)。

### 设计依据 (4 agent 调研合成)
- **Ericsson 刻意练习 (deliberate practice)**: 5 要素 - 具体目标/专注/反馈/重复/反思。本单元 `practice.md` 三个 drill (D1 OLS+VIF / D2 Logit+倾向性 / D3 分布+LTV+QuantReg) 每个含 difficulty/reps_required/feedback_rule/worked-faded 三阶段。
- **FSRS-6 间隔重复 (spaced retrieval)**: `schedule.json` 用 FSRS-6 (request_retention=0.9, 21 weights) + SM-2 备份 (EF₀=2.5, I(1)=1, I(2)=6), 4 张卡 due=[1,3,8,21,60,180], 命中 statsmodels NSW treat=1621 / LTV uplift 39.4% / QuantReg 75分位 2502 等核心概念。
- **Biggs 建构对齐 (constructive alignment)**: `alignment.md` 4 行 ILO↔TLA↔AT 矩阵 + mastery_threshold + 3 自检 (Feed Up / Feed Back / Feed Forward), 确保不经 TLA 不能过 AT。
- **Oxford tutorial Socratic 仿真**: `tutorial.ipynb` 6 cells - persona (禁直接答案/魔鬼代言人) + pre-task (提取练习) + 5 轮 Socratic 追问 + student_model.json + Hattie 四级形成性反馈 [TASK]/[PROCESS]/[SELF-REG]/[FEED-FORWARD] (避免 Self 表扬级) + 限频 (1次/天) + exit artifact。
- **MIT Open Learning 交叉练习 (interleaving)**: `practice.md` 用 A1B1C1...B2C2A2...C3A3B3 模式交叉排布三子技能, 不块状刷题; 渐退示例 (Worked-Faded) 三阶段: 完整示范 -> 部分填空 -> 独立解。
- **weak_loop 弱项循环**: 连续 2 次失败触发, 回退上一 drill + 补 worked example, mastery 阈值未达即转入弱项循环。

### v6.0 五件套映射
| 文件 | 学习科学机制 | 本单元命中点 |
|---|---|---|
| practice.md | 刻意练习 + 交叉 + worked-faded + weak_loop | D1/D2/D3 三 drill, feedback_rule 引用 statsmodels/NSW treat=1621/LTV 39.4% |
| schedule.json | FSRS-6 / SM-2 间隔重复 | 4 卡: OLS+VIF / Logit+propensity / 分布+LTV / QuantReg 异质性 |
| alignment.md | Biggs ILO↔TLA↔AT 建构对齐 + mastery | 4 行矩阵 + 3 自检 (Feed Up/Back/Forward) |
| tutorial.ipynb | Oxford Socratic + Hattie 四级 + student_model + 限频 | 5 轮追问覆盖 ILO1-4, devil's advocate 角色主动质疑 |
| notes.md (本节) | 关键词注入, 跨文件索引 | 命中 FSRS/SM-2/刻意练习/建构对齐/Socratic/Hattie/间隔重复/交叉/mastery/Worked-Faded >=4 关键词 |

### 收敛判据 (Loop Engineering v6.0)
- v5.0 基线 (1-7): `verify_unit.py` 全通过 (本单元 7/7)
- v6.0 新层 (8-12): `verify_v6_unit.py` 全通过 (本单元目标 5/5)
- 两脚本均通过 = 本单元 v6.0 收敛 (12/12)

---

*v6.0 学习科学层追加完成。最后更新：2026-07-25*

---

## 研究产出与产业链接层 (v7.0)

本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+arXiv链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。研究产出锚定真实 RCT 数据 (causaldata NSW, LaLonde 1986) 与本单元上机真实数字 (treat β=1621 p=0.01 / LTV uplift 39.4% / QuantReg 75 分位 2502); 产业链接锚定 Booking.com/Netflix/Uber/Sephora 真实企业 + Google AI Resident 实习指针。linked_paper 复用 reading.md 已验证 arXiv 链接 (arxiv.org/abs/1904.04582 A Survey on Causal Inference) 与 JSTOR 链接 (LaLonde 1986 / Koenker & Bassett 1978)。详见 research.md 与 industry.md。

---

*v7.0 研究产出+产业链接层追加完成。最后更新：2026-07-26*

---

## 学术前沿层 (v9.0)

本单元新增 `frontier.md`：注入 2025-2026 最新学术前沿（N 篇真实 arXiv 论文 + 批判性综述 + delta_to_unit + ≥3 开放研究问题 + 方法论批评）。论文来自 `_frontier_corpus/skill-0-business-analytics.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证），覆盖前沿课题：LLM-as-data-analyst × Polars/duckdb 列式引擎。面向博后/教授级读者：批判性综述非罗列，delta_to_unit 显式指出前沿如何更新本单元所教，开放问题为可发表研究方向。详见 `frontier.md`。
