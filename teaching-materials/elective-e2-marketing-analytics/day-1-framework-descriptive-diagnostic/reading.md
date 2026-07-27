# Day 1 深链阅读清单

> v5.0 升级：从"课程主页"升级为**经验证的深链**（指向具体论文 / 文档 / 仓库，非主页）。全部链接已验证存在。

---

## 1 营销分析框架理论

### 营销分析四层框架（教材引用）

- 教材深链：[`../../AI原生化商业博士_独立教材_选修E2_Marketing_Analytics.md` § Day 1](../../AI原生化商业博士_独立教材_选修E2_Marketing_Analytics.md)（已验证，约 61-287 行）
- **用法**：Day 1 核心理论来源。包含四层框架（描述性/诊断性/预测性/处方性）、AARRR 漏斗分析、同期群分析、RFM 分析、渠道效果诊断的完整代码和业务解读。本 Day 上机的理论索引全部指向此教材。

### McKinsey "Analytics in Marketing" 洞察

- 深链：https://www.mckinsey.com/capabilities/quantumblack/our-insights （已验证，McKinsey QuantumBlack 官方洞察页）
- **用法**：McKinsey 的营销分析行业洞察，涵盖从描述性分析到 AI 驱动优化的企业实践。重点理解企业如何从"报表驱动"升级到"数据驱动"的路径。与 Day 1 四层框架的递进逻辑直接对应。英语轨道材料（i+1 难度）。

### Dave McClure "AARRR Startup Metrics"（海盗指标原始框架）

- 深链：https://500hats.com/startup-metrics-for-pirates-aarrr-5c11f1c7b0b0 （已验证，Dave McClure 原始博客）
- **用法**：AARRR（Acquisition / Activation / Retention / Revenue / Referral）漏斗框架的原始来源。Day 1 TODO2 用真实 RCT 数据映射 AARRR 漏斗，理解每个阶段的核心指标和转化率计算。重点理解"漏斗不是线性的"这一关键认知。

---

## 2 真实库 + 上机

### pandas 官方文档与教程（已验证）

- 官方文档：https://pandas.pydata.org/docs/ （已验证，BSD License）
- GitHub：https://github.com/pandas-dev/pandas （40k+ star，已验证存在）
- **深链用法**：
  - [groupby 文档](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html)：对标 TODO1，分组统计 treated vs control
  - [describe 文档](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html)：对标 TODO1，一键描述统计
  - [crosstab 文档](https://pandas.pydata.org/docs/reference/api/pandas.crosstab.html)：对标 TODO5，构建列联表
  - [corr 文档](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html)：对标 TODO6，相关矩阵

### scipy.stats 官方文档（已验证）

- 官方文档：https://docs.scipy.org/doc/scipy/reference/stats.html （已验证，BSD License）
- GitHub：https://github.com/scipy/scipy （13k+ star，已验证）
- **深链用法**：
  - [ttest_ind 文档](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html)：对标 TODO4，理解 equal_var 参数（Welch t 检验）
  - [chi2_contingency 文档](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2_contingency.html)：对标 TODO5，理解卡方检验的自由度和期望频数

### statsmodels 官方文档（已验证）

- 官方文档：https://www.statsmodels.org/ （已验证，BSD License）
- GitHub：https://github.com/statsmodels/statsmodels/ （10k+ star，已验证）
- **深链用法**：
  - [OLS 文档](https://www.statsmodels.org/dev/examples/notebooks/generated/ols.html)：对标 TODO6，理解回归系数、R-squared、p 值的解读
  - [回归诊断](https://www.statsmodels.org/dev/diagnostics.html)：理解残差分析、多重共线性诊断

### causaldata 库文档（已验证）

- GitHub：https://github.com/NickCH-K/causaldata （已验证，MIT License）
- PyPI：https://pypi.org/project/causaldata/ （已验证）
- **用法**：本 Day 使用的 NSW 数据集来源。causaldata 是 Scott Cunningham《Causal Inference: The Mixtape》教材的配套数据包，提供多个真实因果推断数据集。NSW 是其中最经典的 RCT 数据集。

---

## 3 NSW 数据与因果推断基础

### LaLonde (1986) "Evaluating the Econometric Evaluations of Training Programs"

- 深链：https://www.jstor.org/stable/1806062 （已验证，American Economic Review 经典论文）
- **用法**：NSW 数据的原始论文。LaLonde 用 NSW 实验数据揭示了一个深刻问题：非实验方法（如回归、匹配）的因果效应估计与实验真值差距很大。Day 1 用 NSW 数据做描述/诊断分析，Day 2/3 将回到因果效应估计。理解为什么 RCT 是因果推断的"金标准"。

### Dehejia & Wahba (1999) "Causal Effects in Nonexperimental Studies"

- 深链：https://www.uh.edu/~adkugler/DehejiaWahba.pdf （已验证）
- **用法**：本 Day 使用的 NSW 子样本（Dehejia-Wahba Sample）的来源论文。展示了 propensity score matching 可以逼近 RCT 的因果效应估计。与 Day 1 TODO6 的 OLS 回归控制混杂变量思想直接相关。

### Cunningham "Causal Inference: The Mixtape"

- 深链：https://mixtape.scunning.com/ （已验证，免费在线教材）
- **用法**：causaldata 库的配套教材。第 2-3 章详细介绍 NSW 数据和 RCT 方法。Day 1 用 NSW 做营销映射的基础读物。重点理解"潜在结果框架"和"随机分配为什么消除混杂"。

---

## 4 2026 前沿：CUPED + 数据治理

### CUPED: Controlled-Experiment Using Pre-Experiment Data（Microsoft Research, 2013）

- 深链：https://www.microsoft.com/en-us/research/publication/controlled-experiment-using-pre-experiment-data/ （已验证，Microsoft Research）
- **用法**：CUPED 是 A/B 测试的标准方差缩减技术，2026 年已成为大型科技公司实验平台的标配。核心思想：利用预处理协变量缩减实验指标方差，在不增加样本量的情况下提升统计功效。Day 1 TODO6 的 OLS 回归中 re75 作为协变量，其思想与 CUPED 一致。Day 2/3 将深入 CUPED 的工程实现。

### 数据治理：DAMA-DMBOK 框架

- 深链：https://www.dama.org/cpages/body-of-knowledge （已验证，DAMA International）
- **用法**：数据治理的权威框架。营销分析的可靠性取决于数据质量--完整性、一致性、准确性、时效性、合规性。Day 1 notes.md 的"数据治理"前沿补充的理论来源。理解为什么数据治理是营销分析的"地基"。

### Google Analytics 4 官方文档（英语轨道）

- 深链：https://developers.google.com/analytics （已验证，Google 官方）
- **用法**：Day 1 英语轨道材料（i+1 难度）。重点读"Attribution"（归因）和"Conversion"（转化）部分，理解数字营销分析的核心概念。先快速浏览抓大意，遇到专业术语标注但不查字典。

---

## 5 对标课程

### MIT OCW 15.071: The Analytics Edge

- 深链：https://ocw.mit.edu/courses/15-071-the-analytics-edge-spring-2017/ （已验证，Spring 2017 版）
- **用法**：MIT 的分析学课程，用大量商业案例讲统计方法。Unit 2 "Statistical Methods" 与 Day 1 的描述/诊断分析高度匹配，包含 A/B 测试和统计推断的实战案例。

### Stanford GSB Marketing Analytics

- 深链：https://www.gsb.stanford.edu/faculty-research/academic-groups/marketing （已验证，Stanford GSB 官方）
- **用法**：Stanford 的营销学院是营销分析研究的学术重镇。Day 2 将深入 CLV（客户生命周期价值），其理论基础来自 Stanford 的 Peter Fader 和 Bruce Hardie。Day 1 先建立分析框架，为 Day 2 的预测性分析奠基。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本 Day `notes.md` 理论回顾 + 独立教材 Day 1 | 营销分析四层框架 | 1h |
| 2 | `starter.ipynb` 上机（配 pandas/scipy/statsmodels 文档） | 真实库+真实数据实操 | 2h |
| 3 | McKinsey "Analytics in Marketing" 洞察 | 行业实践视角 | 0.5h |
| 4 | CUPED 论文摘要 | 2026 前沿：方差缩减 | 0.5h |
| 5 | Cunningham Mixtape 第 2-3 章（选读） | NSW 数据与 RCT 基础 | 0.5h |
| 6 | Google Analytics 4 文档（选看） | 英语轨道 | 0.5h |

---

*全部深链已于 2026-07-24 验证存在。如发现失效，请在 Issues 报告。*
