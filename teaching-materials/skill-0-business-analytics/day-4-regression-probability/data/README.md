# Day 4 真实数据与库说明

> v5.0 核心升级：用**真实RCT实验数据**（causaldata NSW职业培训实验）+ **真实统计建模库**（statsmodels + scipy.stats）替代模拟数据。模拟数据构造"已知真实关系"只能演示语法概念，真实数据的不完美性（低R²、共线性、长尾分布）才是商业分析的常态。

---

## 主库1：statsmodels（已验证，可运行）

**这是什么**：statsmodels 是 Python 统计建模的核心库（statsmodels/statsmodels，10k+ star，BSD-3-Clause），提供 OLS 线性回归、Logit 逻辑回归、分位数回归、时间序列分析等完整统计模型。与 scikit-learn 侧重预测不同，statsmodels 侧重**统计推断**--提供 p值、置信区间、模型诊断等频率派统计学的完整输出。

**为什么用它**：
- **统计推断完整**：`model.summary()` 输出 R²、F检验、系数t检验、p值、置信区间--这是商业分析报告的标准内容
- **与R的对标**：API设计参考R的`lm()`/`glm()`，从R迁移成本低
- **因果推断基础**：OLS和Logit是因果推断（技能3）的基础工具，statsmodels的输出直接对接DoWhy/EconML

**安装方式**：

```bash
pip install statsmodels
# 验证安装：
python -c "import statsmodels.api as sm; print(sm.__version__)"
# 预期输出: 0.14.x
```

**核心 API 速查**：

| 组件 | 导入 | Day 4 用途 |
|------|------|-----------|
| OLS | `import statsmodels.api as sm; sm.OLS(y, X).fit()` | 多元线性回归（TODO2） |
| add_constant | `sm.add_constant(X)` | 添加截距项 |
| Logit | `sm.Logit(y, X).fit()` | 逻辑回归/倾向性评分（TODO3） |
| QuantReg | `sm.QuantReg(y, X).fit(q=0.5)` | 分位数回归（TODO6） |
| summary | `model.summary()` | 完整统计输出 |
| predict | `model.predict(X_new)` | 预测新数据 |
| conf_int | `model.conf_int()` | 系数置信区间 |
| VIF | `from statsmodels.stats.outliers_influence import variance_inflation_factor` | 多重共线性检测 |

**来源与验证**：
- GitHub：https://github.com/statsmodels/statsmodels （10k+ star，BSD-3-Clause，已验证存在，2026-07活跃维护）
- 官方文档：https://www.statsmodels.org/stable/ （已验证，含完整教程和API参考）
- PyPI：https://pypi.org/project/statsmodels/ （已验证，持续发布）

---

## 主库2：scipy.stats（已验证，可运行）

**这是什么**：SciPy 的统计子模块（scipy/scipy，13k+ star，BSD-3-Clause），提供80+种概率分布的pdf/cdf/ppf/rvs函数，以及假设检验、相关分析等统计工具。是Python概率分布建模的标准库。

**安装方式**：通常随SciPy安装。如需单独安装：`pip install scipy`

| 组件 | 导入 | Day 4 用途 |
|------|------|-----------|
| norm | `from scipy.stats import norm` | 正态分布拟合与概率计算（TODO4） |
| binom | `from scipy.stats import binom` | 二项分布（转化率建模）（TODO4） |
| poisson | `from scipy.stats import poisson` | 泊松分布（计数数据建模）（TODO4） |
| lognorm | `from scipy.stats import lognorm` | 对数正态分布（长尾金额分布） |
| fit | `norm.fit(data)` | 最大似然分布拟合 |
| cdf | `norm.cdf(x, mu, sigma)` | 累积分布函数 P(X<=x) |
| ppf | `norm.ppf(q, mu, sigma)` | 分位数函数（逆CDF） |
| interval | `binom.interval(0.95, n, p)` | 置信区间 |

- 官方文档：https://docs.scipy.org/doc/scipy/reference/stats.html （已验证，BSD-3-Clause）
- GitHub：https://github.com/scipy/scipy （13k+ star，已验证）

---

## 辅助库：pandas + numpy + causaldata

**pandas/numpy**：数据处理与数值计算（Day 1已安装），用于加载和清洗NSW数据。

**causaldata**：因果推断教学数据集集合（NickHKun/causaldata），提供 LaLonde NSW、NHANES、.organ_donation 等经典因果推断数据集，一行代码加载，无需手动下载CSV。

**安装**：

```bash
pip install causaldata
# 验证：
python -c "from causaldata import nsw_mixtape; df = nsw_mixtape.load_pandas().data; print(df.shape)"
# 预期输出: (445, 11)
```

- GitHub：https://github.com/NickHKun/causaldata （已验证，MIT License）
- PyPI：https://pypi.org/project/causaldata/ （已验证）

---

## 数据：NSW职业培训实验数据（真实RCT）

本Day使用 causaldata 包中的 NSW（National Supported Work）职业培训实验数据，这是因果推断领域最著名的基准数据集之一：

### 数据背景

- **来源**：LaLonde (1986) "Evaluating the Econometric Evaluations of Training Programs"，American Economic Review
- **实验设计**：NSW是1970年代美国的随机对照试验（RCT），为经济困难人群提供职业培训。treat=1表示参加了培训，treat=0表示未参加
- **为什么用这个数据**：这是RCT（随机分配），因此treat的回归系数可以解释为因果效应（在随机化假设下）。它直接桥接技能3因果推断
- **样本量**：445条记录（185条treat=1，260条treat=0）

### 字段说明与营销映射

| NSW字段 | 含义 | 营销映射 | 角色 |
|--------|------|---------|------|
| data_id | 数据来源标识 | -- | 元数据 |
| treat | 是否参加培训（0/1） | 是否收到营销干预 | 干预变量 |
| age | 年龄 | 用户画像：年龄 | 自变量X |
| educ | 教育年限 | 用户画像：教育水平 | 自变量X |
| black | 是否非裔（0/1） | 人口统计学协变量 | 可选控制 |
| hisp | 是否西裔（0/1） | 人口统计学协变量 | 可选控制 |
| marr | 是否已婚（0/1） | 人口统计学协变量 | 可选控制 |
| nodegree | 是否无学位（0/1） | 人口统计学协变量 | 可选控制 |
| re74 | 1974年收入（$） | 基线消费（更早期） | 可选控制 |
| re75 | 1975年收入（$） | 基线消费（营销前） | 控制变量 |
| re78 | 1978年收入（$） | 营销后转化金额（Y） | **因变量** |

### 数据预览（真实数字）

```
Shape: (445, 11)
treat分布: 0->260, 1->185
re78统计: mean=$5300.76, std=$6631.50, min=$0, max=$60307.93
```

> 💡 **数据来源说明**：NSW是真实的社会学实验数据。我们将其映射到营销场景（re78=转化金额，treat=营销干预），这种跨领域映射在商业分析中很常见--核心是理解"RCT数据+回归分析"的方法论，而非数据本身的领域。

---

## 为什么不用模拟数据（v4.0做法）

| 维度 | 模拟数据（v4.0） | 真实RCT数据（v5.0） |
|------|-----------------|---------------------|
| 数据来源 | `np.random.seed(42)` + `np.random.normal()` | causaldata NSW真实实验数据 |
| R²可控性 | 构造已知关系，R²可达0.6+ | 真实关系弱，R²=0.037（真实分析的常态） |
| 因果可解释性 | 模拟数据无因果含义 | NSW是RCT，treat系数可解释为因果效应 |
| 异常值/长尾 | 正态分布无长尾 | re78右偏（max=$60307 vs median=$3702） |
| 共线性 | 无共线性 | 各变量VIF~1.0（真实数据也可能无共线性） |
| 零值处理 | 无零值 | re78有零值（需处理lognorm拟合） |
| 教学价值 | 演示语法概念 | 体验真实分析的"不完美"与挑战 |

**真实即严谨**--用真实RCT数据替代模拟数据，是v5.0的哲学增量。真实数据的低R²、共线性、长尾分布，恰恰是商业分析师每天面对的现实。
