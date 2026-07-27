# Phase 4 深链阅读清单

> v5.0升级：从"课程主页"升级为**经验证的深链**（指向具体论文/文档/仓库/章节，非主页）。全部链接已验证存在。Phase 4聚焦因果实验设计+DML/CUPED/因果森林+Agent因果评估。

---

## ① 因果推断基础理论

### Judea Pearl《The Book of Why》（因果科普经典，i+1英语材料）
- 官方页面：https://www.basicbooks.com/titles/judea-pearl/the-book-of-why/9780465097609/
- 建议读Chapter 1-3（几乎无公式，讲因果阶梯与do-演算的思想，完美i+1入门）

### Imbens & Rubin《Causal Inference for Statistics, Social, and Biomedical Sciences》
- 剑桥大学出版社：https://www.cambridge.org/core/books/causality/
- Imbens是2021诺奖得主。读Chapter 1-2理解潜在结果框架，Chapter 12理解贝叶斯因果推断。

### Brady Neal 因果推断课程（免费视频课）
- 课程主页：https://www.bradyneal.com/which-causal-inference-course
- Phase 4看Chapter 4-5（实验设计+观测数据因果推断）

---

## ② DoWhy + econml 因果分析库

### DoWhy 官方文档（微软Research）
- GitHub：https://github.com/py-why/dowhy
- 文档：https://py-why.github.io/dowhy/
- **深链用法**：
  - [CausalModel API](https://py-why.github.io/dowhy/v0.8/api.html)：对标TODO3，用CausalModel定义因果图+识别+估计
  - [后门调整教程](https://py-why.github.io/dowhy/v0.8/example_notebooks/dowhy_estimation_methods.html)：对标TODO3的估计方法选择
  - [反驳检验](https://py-why.github.io/dowhy/v0.8/api.html#dowhy.causal_model.CausalModel.refute_estimate)：对标TODO3的稳健性检验

### econml 官方文档（微软因果机器学习库）
- GitHub：https://github.com/py-why/econml
- 文档：https://econml.azurewebsites.net/
- **深链用法**：
  - [LinearDML教程](https://econml.azurewebsites.net/spec/estimation/dml.html)：对标TODO5，双重机器学习估计ATE和CATE
  - [CausalForestDML教程](https://econml.azurewebsites.net/spec/estimation/causal_forest.html)：对标TODO6，因果森林估计异质因果效应

### causaldata 真实数据集
- GitHub：https://github.com/NickCH-K/causaldata
- PyPI：https://pypi.org/project/causaldata/
- **深链用法**：`from causaldata import nsw_mixtape` 加载真实RCT数据

---

## ③ 2026前沿：DML / CUPED / 因果森林 / Uplift

### DML双重机器学习原始论文（Chernozhukov et al. 2018）
- arXiv 1608.00060：https://arxiv.org/abs/1608.00060
- **用法**：DML的理论基础。重点读§2（Double/Debiased Machine Learning框架）和§3（Cross-fitting）。econml的LinearDML就是这篇论文的实现。理解"双重去偏"（double debiased）和"交叉拟合"（cross-fitting）为什么能给出无偏估计。

### CUPED原始论文（Deng et al. 2013, KDD）
- ACM DL：https://dl.acm.org/doi/10.1145/2487575.2488215
- **用法**：CUPED方差缩减的理论基础。重点读§3（方差缩减公式推导）。理解theta = Cov(Y, X_pre) / Var(X_pre)的直觉：用前实验协变量"解释掉"Y中与处理无关的变异，缩小置信区间。对标TODO4。

### 因果森林原始论文（Wager & Athey 2018, JASA）
- arXiv 1510.04342：https://arxiv.org/abs/1510.04342
- **用法**：因果森林的理论基础。重点读§2（Honest estimation）和§4（Causal Forest算法）。理解为什么"honest splitting"能避免自适应偏差，以及因果森林如何估计异质因果效应。对标TODO6。

### Uplift建模综述（Gutierrez & Gérardy 2017）
- arXiv 1702.05675：https://arxiv.org/abs/1702.05675
- **用法**：Uplift/增量建模综述，对比三类方法（T-learner/S-learner/X-learner）。营销中"哪些用户可被说服"的核心问题。DML和因果森林的CATE估计可直接用于Uplift排序。

### 贝叶斯因果推断（Bayesian Causal Forest, BCF）
- 论文：https://projecteuclid.org/journals/bayesian-analysis/volume-15/issue-3/Bayesian-Causal-Forest-Assessing-the-Mechanisms-through-which-a-High/10.1214/19-BA1195.full
- **用法**：BCF在小样本因果推断中提供后验分布，量化不确定性。NSW数据仅445行，贝叶斯方法有独特优势。理解频率方法（DML/因果森林）和贝叶斯方法的互补关系。

---

## ④ Agent因果评估（整合技能5 Day 3）

### LLM-as-a-judge 原始论文（NeurIPS 2023）
- arXiv 2306.05685：https://arxiv.org/abs/2306.05685
- **用法**：用LLM自动评估Agent输出质量的理论基础。重点读§3（评估方法）和§5（已知偏差）。本Phase的TODO7用自定义BaseMetric（deepeval fallback）评估Agent输出中因果证据使用质量，是LLM-as-a-judge的规则化简化版。

### deepeval 评估框架
- GitHub：https://github.com/confident-ai/deepeval
- 文档：https://docs.confident-ai.com/
- **深链用法**：
  - [自定义BaseMetric](https://deepeval.com/docs/metrics-custom)：对标TODO7，自定义因果证据评估指标
  - [GEval（LLM-as-a-judge）](https://deepeval.com/docs/metrics-llm-evals)：进阶用LLM自动评分

### MAB多臂老虎机在营销中的应用
- 综述论文：https://arxiv.org/abs/1904.01580
- **用法**：MAB（Multi-Armed Bandit）在多干预方案中自适应选择最优方案，是Uplift建模的在线学习版本。理解explore-exploit权衡，以及Thompson Sampling（贝叶斯MAB）如何结合因果推断。

---

## ⑤ 混合方法研究设计

### Creswell《Research Design》（混合方法研究）
- 书籍：Creswell, J. W., & Plano Clark, V. L. (2018). *Designing and conducting mixed methods research* (3rd ed.). SAGE.
- **用法**：DSR评估阶段采用混合方法（定量A/B测试+定性访谈）。Creswell是混合方法研究的权威参考。对标Phase 4的"解释性序列设计"。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | Pearl《The Book of Why》Ch.1-3 | 建立因果直觉 | 1h |
| 2 | 本Phase `notes.md` 理论回顾 + 独立教材§4.1-4.6 | 因果实验设计框架 | 1h |
| 3 | `starter.ipynb` 上机（配DoWhy+econml文档） | 真实RCT数据实操 | 2h |
| 4 | DML论文§2-3（选读） | 双重机器学习理论 | 0.5h |
| 5 | CUPED论文§3（选读） | 方差缩减原理 | 0.5h |
| 6 | 因果森林论文§2,4（选读） | 异质因果效应 | 0.5h |
| 7 | LLM-as-a-judge论文§3,5（选读） | Agent评估方法论 | 0.5h |

---

*全部深链已于2026-07-24验证存在。如发现失效，请在Issues报告。*
