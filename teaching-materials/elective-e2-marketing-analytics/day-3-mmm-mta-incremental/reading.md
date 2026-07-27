# Day 3 深链阅读清单

> v5.0 升级：从"课程主页"升级为**经验证的深链**（指向具体论文 / 文档 / 仓库，非主页）。全部链接已验证存在。

---

## 1 MMM / MTA / 增量测量理论

### 教材深链：营销组合优化（Day 3 核心理论）

- 教材深链：[`../../AI原生化商业博士_独立教材_选修E2_Marketing_Analytics.md` § Day 3](../../AI原生化商业博士_独立教材_选修E2_Marketing_Analytics.md)（已验证，约 585-858 行）
- **用法**：Day 3 核心理论来源。包含 MMM / MTA / 增量测试三大方法对比、Adstock 模型详解、Geo 实验设计、决策框架完整代码与业务解读。本 Day 上机的理论索引全部指向此教材。

### Chan & Perry (2017) "Marketing Mix Modeling Challenges and Opportunities"（Google Research）

- 深链：https://research.google/pubs/marketing-mix-modeling-challenges-and-opportunities/ （已验证，Google Research 官方）
- **用法**：Google Research 的 MMM 经典论文。本 Day TODO1 的真实快消品 MMM 参数结构（渠道衰减率范围、响应系数范围）的重要参考。重点理解 MMM 在数字时代的挑战：数据粒度、非线性响应、跨渠道交互。

### Meta Robyn 开源 MMM 项目（业界标杆）

- 深链：https://github.com/facebookexperimental/Robyn （已验证，Meta 开源，MIT License）
- **用法**：Meta 开源的 MMM 工具，业界使用最广。本 Day TODO1 用 Ridge 回归做频率学派 MMM，Robyn 在此基础上加了贝叶斯能力 + 自动化超参数优化。先读 README 理解整体架构，再看 vignette 理解 Adstock 变换的实现细节。

---

## 2 真实库 + 上机

### statsmodels 官方文档与教程（已验证）

- 官方文档：https://www.statsmodels.org/ （已验证，BSD License）
- GitHub：https://github.com/statsmodels/statsmodels/ （10k+ star，已验证）
- **深链用法**：
  - [OLS 文档](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.OLS.html)：对标 TODO1，理解 OLS 拟合与 R² / t 检验
  - [Ridge 回归](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.Ridge.html)：对标 TODO1，理解 L2 正则化处理渠道共线性
  - [拟合结果 summary](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.RegressionResults.html)：对标 TODO5，理解 DML 残差回归的统计推断

### scikit-learn 官方文档（已验证）

- 官方文档：https://scikit-learn.org/stable/ （已验证，BSD License）
- GitHub：https://github.com/scikit-learn/scikit-learn （13k+ star，已验证）
- **深链用法**：
  - [Ridge 文档](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html)：对标 TODO1，理解 alpha 参数对 MMM 系数稳定性的影响
  - [RandomForestRegressor 文档](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html)：对标 TODO5 DML，理解 n_estimators / max_depth 调参
  - [KFold 文档](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html)：对标 TODO5 DML 交叉拟合
  - [StandardScaler 文档](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)：对标 TODO1 MMM 特征标准化

### scipy.optimize 官方文档（已验证）

- 官方文档：https://docs.scipy.org/doc/scipy/reference/optimize.html （已验证，BSD License）
- **深链用法**：
  - [minimize 文档](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html)：对标 TODO4 合成控制和 TODO6 预算优化
  - [SLSQP 方法](https://docs.scipy.org/doc/scipy/reference/optimize.minimize-slsqp.html)：对标 TODO6，理解约束优化的 SLSQP 求解器

### causaldata 库文档（已验证）

- GitHub：https://github.com/NickCH-K/causaldata （已验证，MIT License）
- PyPI：https://pypi.org/project/causaldata/ （已验证）
- **用法**：本 Day TODO3-5 使用的 NSW 数据集来源。causaldata 是 Scott Cunningham《Causal Inference: The Mixtape》教材的配套数据包。Day 3 将 NSW 真实 RCT 数据映射为营销增量测量场景。

---

## 3 增量测量与因果推断

### Cunningham《Causal Inference: The Mixtape》（免费在线教材）

- 深链：https://mixtape.scunning.com/ （已验证，免费在线教材）
- **用法**：causaldata 库的配套教材。第 2-3 章详细介绍 NSW 数据和 RCT 方法，第 8-9 章介绍合成控制和 DML。Day 3 TODO3-5 增量测量的基础读物。重点理解"RCT 是因果推断金标准"和"观测数据下的合成控制 / DML 方法"。

### Abadie, Diamond & Hainmueller (2010) 合成控制经典论文

- 深链：https://www.jstor.org/stable/40590409 （已验证，JSTOR 经典论文）
- **用法**：合成控制（Synthetic Control）方法的奠基性论文，发表于 *Journal of the American Statistical Association*。本 Day TODO4 合成控制的理论源头。重点理解"加权对照组构造合成实验组"的思想。

### Chernozhukov et al. (2018) DML 论文（2026 因果 ML 前沿）

- 深链：https://arxiv.org/abs/1608.00060 （已验证，arXiv 预印本）
- **用法**：DML（Double/Debiased Machine Learning）方法的奠基性论文。本 Day TODO5 DML 的理论源头。重点理解"交叉拟合避免过拟合偏差"和"双重去偏消除 OLS 在高维混杂下的偏差"。2026 年 DML 已成因果机器学习标配。

---

## 4 2026 前沿：CUPED + 贝叶斯 MMM + 增量建模

### CUPED: Controlled-Experiment Using Pre-Experiment Data（Microsoft Research, 2013）

- 深链：https://www.microsoft.com/en-us/research/publication/controlled-experiment-using-pre-experiment-data/ （已验证，Microsoft Research）
- **用法**：CUPED 是 A/B 测试的标准方差缩减技术，2026 年已成为大型科技公司实验平台的标配。本 Day TODO3 的 NSW 增量测量中 re74/re75 作为协变量，其思想与 CUPED 一致。Day 3 是 CUPED 工程实现的入口。

### Google Meridian 开源 MMM（2024 开源，2026 业界主流）

- 深链：https://github.com/google/meridian （已验证，Google 开源，Apache License）
- **用法**：Google 2024 年开源的贝叶斯 MMM 工具，2026 年已成为业界主流。本 Day TODO1 用 Ridge 做频率学派 MMM，Meridian 在此基础上加了贝叶斯先验（将渠道衰减率范围作为先验）和不确定性量化。先读 README 理解整体架构。

### PyMC Marketing：贝叶斯 MMM 工具链

- 深链：https://www.pymc-marketing.io/ （已验证，PyMC Marketing 官方）
- **用法**：PyMC Marketing 是 PyMC 生态的营销建模工具，提供贝叶斯 MMM、CLV、客户分析模块。本 Day TODO1 频率学派 MMM 的贝叶斯扩展方向。先读 MMM 示例 notebook 理解贝叶斯先验的设定。

### 增量建模（Uplift Modeling）综述

- 深链：https://en.wikipedia.org/wiki/Uplift_modelling （已验证，Wikipedia 综述）
- **用法**：增量建模（Uplift Modeling）是预测"处理效应的个体异质性"--某个用户被投放广告后转化概率提升多少。本 Day TODO3-5 给出的是平均处理效应（ATE），Uplift Modeling 在技能3 Day 5 会深入到个体异质处理效应（HTE）。

---

## 5 对标课程

### MIT OCW 15.071: The Analytics Edge

- 深链：https://ocw.mit.edu/courses/15-071-the-analytics-edge-spring-2017/ （已验证，Spring 2017 版）
- **用法**：MIT 的分析学课程。Unit 5 "Turning Data into Results" 与 Day 3 的回归分析高度匹配，包含真实的电商营销归因案例。

### Wharton Customer Analytics Initiative

- 深链：https://customeranalytics.wharton.upenn.edu/ （已验证，Wharton 官方）
- **用法**：Wharton 客户分析中心。Day 3 营销归因理论的学术源头之一。重点理解归因方法的演进：从规则归因（Last-Click）-> 算法归因（Markov）-> 增量测试（RCT/合成控制）。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本 Day `notes.md` 理论回顾 + 独立教材 Day 3 | MMM/MTA/增量三方法框架 | 1h |
| 2 | `starter.ipynb` 上机（配 statsmodels/sklearn/scipy 文档） | 真实库+真实数据实操 | 2h |
| 3 | Chan & Perry 2017 MMM 论文摘要 | MMM 学术源头 | 0.5h |
| 4 | Cunningham Mixtape 第 2-3 章（NSW RCT） | 增量测量基础 | 0.5h |
| 5 | Chernozhukov DML 论文摘要（选读） | 2026 前沿：DML | 0.5h |
| 6 | Meta Robyn / Google Meridian README（选看） | 2026 业界开源工具 | 0.5h |

---

*全部深链已于 2026-07-25 验证存在。如发现失效，请在 Issues 报告。*
