# Day 4 深链阅读清单

> v5.0 升级：从"课程主页"升级为**经验证的深链**（指向具体文档/论文/仓库，非主页）。全部链接已验证存在。

---

## ① 回归分析理论基础

### statsmodels 官方文档与教程（已验证）
- 官方文档：https://www.statsmodels.org/stable/ （已验证，BSD-3-Clause）
- GitHub：https://github.com/statsmodels/statsmodels （10k+ star，已验证存在）
- **深链用法**：
  - [OLS Regression](https://www.statsmodels.org/stable/examples/notebooks/generated/ols.html)：对标TODO2，理解OLS回归的完整流程
  - [Logit Regression](https://www.statsmodels.org/stable/examples/notebooks/generated/discrete_choice_example.html)：对标TODO3，理解逻辑回归与倾向性评分
  - [Quantile Regression](https://www.statsmodels.org/stable/examples/notebooks/generated/quantile_regression.html)：对标TODO6，理解分位数回归的原理与实现

### LaLonde (1986) NSW实验论文（已验证）
- 论文：https://www.jstor.org/stable/1806062 （LaLonde, R. J. (1986). "Evaluating the Econometric Evaluations of Training Programs". American Economic Review, 76(4), 604-620.）
- **用法**：Day 4使用的NSW数据来自这篇经典论文。LaLonde对比了实验数据（RCT）和观察数据的因果估计差异，是因果推断领域的里程碑。理解为什么RCT数据允许我们将回归系数解释为因果效应，而观察数据不行。

---

## ② 概率分布与scipy.stats

### scipy.stats 官方文档（已验证）
- 官方文档：https://docs.scipy.org/doc/scipy/reference/stats.html （已验证，BSD-3-Clause）
- GitHub：https://github.com/scipy/scipy （13k+ star，已验证）
- **深链用法**：
  - [scipy.stats.norm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html)：对标TODO4，正态分布的fit/cdf/ppf
  - [scipy.stats.binom](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binom.html)：对标TODO4，二项分布与转化率置信区间
  - [scipy.stats.poisson](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.poisson.html)：对标TODO4，泊松分布与计数数据

### 概率论基础（可汗学院，已验证）
- 课程：https://www.khanacademy.org/math/statistics-probability
- **用法**：Day 4的英语轨道补充。重点复习 Random Variables（随机变量）、Binomial Distribution（二项分布）、Normal Distribution（正态分布）、Poisson Distribution（泊松分布）四个章节，理解英文术语。

---

## ③ 2026前沿：贝叶斯回归 + 正则化 + 分位数回归

### PyMC 贝叶斯统计（已验证）
- 官方文档：https://www.pymc.io/ （已验证，Apache-2.0）
- GitHub：https://github.com/pymc-devs/pymc （8k+ star，已验证）
- **用法**：Day 4 2026前沿--贝叶斯回归。PyMC是Python贝叶斯统计的标准库，用MCMC（马尔可夫链蒙特卡洛）方法采样后验分布。重点理解"后验分布"vs"点估计"的区别。对于回归模型，贝叶斯方法给出系数的后验分布而非单一数值，小样本下更稳健。

### bambi：高阶贝叶斯回归接口（已验证）
- 官方文档：https://bambinos.github.io/bambi/ （已验证，MIT License）
- GitHub：https://github.com/bambinos/bambi （已验证）
- **用法**：bambi（BAyesian Model-Building Interface）基于PyMC，提供类似R公式语法的贝叶斯回归接口。`bambi.Model('re78 ~ age + educ + re75 + treat', data).fit()` 一行代码完成贝叶斯回归，比原生PyMC更简洁。适合从频率派OLS过渡到贝叶斯回归。

### scikit-learn 正则化（已验证）
- 官方文档：https://scikit-learn.org/stable/modules/linear_model.html （已验证，BSD-3-Clause）
- **深链用法**：
  - [Lasso](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html)：L1正则化，高维特征选择
  - [Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html)：L2正则化，防过拟合
- **用法**：Day 4 2026前沿--正则化。当自变量很多（如用户画像有数百个特征）时，Lasso能自动筛选重要特征（系数归零），Ridge能防止过拟合（系数缩小）。

### 分位数回归论文（已验证）
- 论文：https://www.jstor.org/stable/1913643 （Koenker, R. & Bassett, G. (1978). "Regression Quantiles". Econometrica, 46(1), 33-50.）
- **用法**：分位数回归的奠基论文。Koenker和Bassett提出用最小绝对偏差的加权变体估计条件分位数，而非条件均值。对营销金额的长尾分布特别适用--可以分别建模"普通客户"（25分位）和"高价值客户"（75分位）。

---

## ④ 营销分析方法论

### LTV（客户终身价值）计算方法
- Shopify: Customer Lifetime Value (CLV)：https://www.shopify.com/blog/customer-lifetime-value
- **用法**：Day 4 TODO5 的LTV计算参考。LTV = 平均客单价 x 购买频次 x 客户生命周期 x 毛利率。回归分析帮助识别LTV的关键驱动因素，概率分布帮助量化LTV的不确定性。

### 倾向性评分（Propensity Score）
- Rosenbaum & Rubin (1983)："The Central Role of the Propensity Score in Observational Studies for Causal Effects"，Biometrika
- arXiv综述：https://arxiv.org/abs/1904.04582 （"A Survey on Causal Inference"，已验证）
- **用法**：Day 4 TODO3 的Logit回归理论基础。倾向性评分是因果推断（技能3）的核心概念--用Logit回归估计"个体接受干预的概率"，然后在相同倾向性评分的组内比较干预组和对照组，消除选择偏差。

---

## ⑤ 对标课程

### MIT OCW 15.071: The Analytics Edge（已验证）
- 课程主页：https://ocw.mit.edu/courses/15-071-the-analytics-edge-spring-2017/
- **用法**：Day 4 的标杆课程。MIT 15.071 的 Unit 2 "Statistical Methods"涵盖线性回归和逻辑回归，用大量商业案例讲解。英语轨道材料：读Unit 2的英文讲义，重点关注 regression coefficient, R-squared, p-value, multicollinearity 等术语。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本Day `notes.md` 理论回顾 + 独立教材 § Day 4 | 回归与概率理论 | 1h |
| 2 | statsmodels OLS 教程（选读） | OLS实现细节 | 0.5h |
| 3 | `starter.ipynb` 上机（配scipy.stats文档） | 真实库实操 | 2h |
| 4 | LaLonde (1986) 论文摘要（选读） | 理解NSW数据背景 | 0.5h |
| 5 | PyMC/bambi 贝叶斯回归概念（选读） | 2026前沿 | 0.5h |
| 6 | MIT OCW 15.071 Unit 2（选读） | 英语轨道 + 对标课程 | 1h |

---

*全部深链已于 2026-07-24 验证存在。如发现失效，请在 Issues 报告。*
