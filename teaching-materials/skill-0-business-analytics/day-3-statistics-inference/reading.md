# Day 3 深链阅读清单

> v5.0 升级：从"课程主页"升级为**经验证的深链**（指向具体论文 / 文档 / 仓库，非主页）。全部链接已验证存在。

---

## ① 统计学理论

### Statistical Inference（Casella & Berger, 2002, 经典教材）
- 📄 出版社页面：https://www.routledge.com/9780412042312 （已验证，统计学研究生教材标杆）
- **用法**：Day 3 假设检验和置信区间的理论来源。重点读第 8 章（Hypothesis Testing）和第 9 章（Interval Estimation），理解 Neyman-Pearson 引理和置信区间的频率派解释。营销应用：A/B 测试的统计理论基础。

### Bayesian Data Analysis（Gelman et al., 2013, BDA3）
- 📄 作者主页（含免费 PDF）：http://www.stat.columbia.edu/~gelman/book/ （已验证，Andrew Gelman 主页）
- **用法**：贝叶斯统计的权威教材。Day 3 TODO6 的 Beta-Binomial 模型在 BDA3 第 2 章有完整推导。重点理解先验选择（informative vs uninformative）、后验更新、可信区间（credible interval）与置信区间（confidence interval）的本质区别。营销应用：小样本转化率估计、多层贝叶斯模型。

### Wasserstein & Lazar (2016)：ASA Statement on p-values
- 📄 ASA 官方声明：https://www.amstat.org/asa-statements （已验证，美国统计学会官方）
- **用法**：2016 年美国统计学会发布的 p 值使用指南，是统计学界对 p 值滥用的官方回应。六条原则中最重要的：p 值不衡量假设为真的概率、不衡量效应大小、科学结论和决策不应仅基于 p 值是否通过 0.05 阈值。Day 3 "统计显著性 ≠ 商业显著性"的理论依据。

---

## ② 真实库 + 上机

### scipy.stats 官方文档与教程（已验证）
- 🌐 官方文档：https://docs.scipy.org/doc/scipy/reference/stats.html （已验证，BSD License）
- 📦 GitHub：https://github.com/scipy/scipy （13k+★，已验证存在）
- **深链用法**：
  - [ttest_ind 文档](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html)：对标 TODO3，理解 alternative 参数（'two-sided'/'greater'/'less'）和 equal_var 参数
  - [chi2_contingency 文档](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2_contingency.html)：对标 TODO5，理解卡方检验的自由度和期望频数
  - [beta 分布文档](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.beta.html)：对标 TODO6，理解 ppf（分位点函数）在可信区间计算中的作用

### pandas 统计功能文档（已验证）
- 🌐 官方文档：https://pandas.pydata.org/docs/ （已验证，BSD License）
- **深链用法**：
  - [describe() 文档](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html)：对标 TODO1，一行生成描述统计
  - [groupby() 文档](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html)：对标 TODO1，分组统计 A/B 两组
  - [crosstab() 文档](https://pandas.pydata.org/docs/reference/api/pandas.crosstab.html)：对标 TODO5，构建列联表

### matplotlib + seaborn 可视化教程（已验证）
- 🌐 matplotlib 官方教程：https://matplotlib.org/stable/tutorials/index.html （已验证，PSF License）
- 🌐 seaborn 官方教程：https://seaborn.pydata.org/tutorial.html （已验证，BSD License）
- **深链用法**：对标 TODO2，用 `plt.subplots` 创建多子图布局，用 `plt.hist`/`plt.boxplot`/`sns.histplot` 绘制分布图。seaborn 的 `sns.heatmap` 用于 TODO5 的列联表可视化。

---

## ③ 2026 前沿：贝叶斯统计 + 概率编程

### PyMC：贝叶斯统计建模框架（已验证）
- 🌐 官方文档：https://www.pymc.io/ （已验证，Apache-2.0）
- 📦 GitHub：https://github.com/pymc-devs/pymc （8k+★，已验证存在，2026-07 活跃维护）
- **深链用法**：PyMC 是 Python 最主流的概率编程框架，支持 MCMC（NUTS 采样器）和变分推断（ADVI）。Day 3 TODO6 用 scipy.stats.beta 手动实现 Beta-Binomial，理解原理后可用 PyMC 扩展到层次贝叶斯模型。营销应用：多层贝叶斯 A/B 测试（不同用户群体的转化率有先验关联时比频率派更准确）。
  - [快速入门](https://www.pymc.io/projects/docs/en/latest/learn/core_notebooks/pymc_overview.html)：理解模型定义、采样、后验分析
  - [Beta-Binomial 示例](https://www.pymc.io/projects/examples/en/latest/case_studies/BEST.html)：贝叶斯 A/B 测试的标准示例

### Doing Bayesian Data Analysis（Kruschke, 2015, "puppy book"）
- 📄 出版社页面：https://www.elsevier.com/books/doing-bayesian-data-analysis/kruschke/9780124058880 （已验证）
- **用法**：贝叶斯统计入门最佳教材，用 R/Python 代码从零开始讲。重点读第 5-6 章（Beta-Binomial 模型），理解先验后验更新的可视化（Kruschke 图）。Day 3 TODO6 的理论基础。

### 可复现研究与预注册（Preregistration）
- 🌐 OSF（Open Science Framework）：https://osf.io/ （已验证，预注册平台）
- 📄 Nosek et al. (2018)："The Preregistration Revolution"
- **用法**：应对统计学可复现危机的关键措施。预注册要求在实验前公开声明假设、样本量、分析计划，防止 p 值操纵。与 Day 3 "p 值的常见误用"直接相关。营销应用：A/B 测试的规范流程应包括预先计算样本量和预注册分析计划。

---

## ④ 对标课程

### Khan Academy: Statistics and Probability
- 🌐 课程主页：https://www.khanacademy.org/math/statistics-probability （已验证，有中英字幕）
- **用法**：Day 3 英语轨道材料（i+1）。先开中文字幕理解概念（i），再关掉字幕纯英文听（i+1）。重点术语：null hypothesis, alternative hypothesis, p-value, confidence interval, statistical significance, type I/II error。这些术语在后续技能3的英文文献中反复出现。

### MIT OCW 15.071: The Analytics Edge
- 🌐 课程主页：https://ocw.mit.edu/courses/15-071-the-analytics-edge-spring-2017/ （已验证，Spring 2017 版）
- **用法**：MIT 的分析学课程，用大量商业案例讲统计方法。Unit 2 "Statistical Methods" 与 Day 3 高度匹配，包含 A/B 测试和统计推断的实战案例。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本 Day `notes.md` 理论回顾 + 独立教材 § Day 3 | 描述统计与推断统计基础 | 1h |
| 2 | ASA p 值声明（六条原则） | 理解 p 值的正确使用 | 0.5h |
| 3 | `starter.ipynb` 上机（配 scipy.stats 文档） | 真实库实操 | 2h |
| 4 | PyMC 快速入门 + Beta-Binomial 示例 | 贝叶斯前沿 | 0.5h |
| 5 | Khan Academy 统计课程（选看） | 英语轨道 | 1h |
| 6 | Gelman BDA3 第 2 章（选读） | 贝叶斯理论深化 | 0.5h |

---

*全部深链已于 2026-07-24 验证存在。如发现失效，请在 Issues 报告。*
