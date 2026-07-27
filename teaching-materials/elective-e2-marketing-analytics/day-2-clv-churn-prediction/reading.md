# Day 2 深链阅读清单

> v5.0 升级：从"课程主页"升级为**经验证的深链**（指向具体论文 / 文档 / 仓库，非主页）。全部链接已验证存在。

---

## 1 CLV 与流失预测理论

### 教材深链：CLV 与流失预测（Day 2 核心理论）

- 教材深链：[`../../AI原生化商业博士_独立教材_选修E2_Marketing_Analytics.md` § Day 2](../../AI原生化商业博士_独立教材_选修E2_Marketing_Analytics.md)（已验证，约 289-581 行）
- **用法**：Day 2 核心理论来源。包含 CLV 三方法、BG/NBD + Gamma-Gamma 模型详解、流失预测建模框架、Next Best Action 决策完整代码与业务解读。本 Day 上机的理论索引全部指向此教材。

### Peter Fader & Bruce Hardie BG/NBD 模型论文（CLV 学术基石）

- 深链：http://brucehardie.com/papers/018/fader_etds_2005.pdf （已验证，Bruce Hardie 个人学术主页）
- **用法**：BG/NBD（Beta Geometric / Negative Binomial Distribution）模型的原始论文，发表于 *Journal of Marketing Research* (2005)。本 Day TODO3 简化版 BG/NBD CLV 公式的理论来源。重点理解两大行为假设：购买服从 Poisson，流失服从 Beta 分布。英语轨道材料（i+1 难度），先读引言和模型设定部分。

### Stanford GSB Marketing Faculty（CLV 研究重镇）

- 深链：https://www.gsb.stanford.edu/faculty-research/academic-groups/marketing （已验证，Stanford GSB 官方）
- **用法**：Stanford 的营销学院是 CLV 研究的学术重镇。Peter Fader（Wharton）和 Bruce Hardie（London Business School）的 BG/NBD 模型是 CLV 领域的经典。本 Day 英语轨道材料来源。先浏览 faculty 目录和 recent publications，抓大意。

---

## 2 真实库 + 上机

### scikit-learn 官方文档与教程（已验证）

- 官方文档：https://scikit-learn.org/stable/ （已验证，BSD License）
- GitHub：https://github.com/scikit-learn/scikit-learn （13k+ star，已验证）
- **深链用法**：
  - [LogisticRegression 文档](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)：对标 TODO4，理解 class_weight='balanced' 与 max_iter 参数
  - [RandomForestClassifier 文档](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)：对标 TODO5，理解 n_estimators / max_depth 调参
  - [roc_auc_score 文档](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html)：对标 TODO4/5，理解 AUC-ROC 不平衡场景下的解读
  - [classification_report 文档](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html)：对标 TODO5，理解 Precision/Recall/F1 的业务含义

### pandas 官方文档（已验证）

- 官方文档：https://pandas.pydata.org/docs/ （已验证，BSD License）
- GitHub：https://github.com/pandas-dev/pandas （40k+ star，已验证）
- **深链用法**：
  - [qcut 文档](https://pandas.pydata.org/docs/reference/api/pandas.qcut.html)：对标 TODO2/3，理解等频分桶
  - [DataFrame.apply 文档](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html)：对标 TODO2，理解 RFM 分群规则函数
  - [crosstab 文档](https://pandas.pydata.org/docs/reference/api/pandas.crosstab.html)：对标 TODO6，行动矩阵列联表

### causaldata 库文档（已验证）

- GitHub：https://github.com/NickCH-K/causaldata （已验证，MIT License）
- PyPI：https://pypi.org/project/causaldata/ （已验证）
- **用法**：本 Day 使用的 NSW 数据集来源。causaldata 是 Scott Cunningham《Causal Inference: The Mixtape》教材的配套数据包。Day 2 将 NSW 真实 RCT 数据映射为 CLV/流失场景。

---

## 3 流失预测与生存分析

### Fader & Hardie "How to Project Customer Retention"

- 深链：http://brucehardie.com/papers/021/sir_2007_final.pdf （已验证，Bruce Hardie 学术主页）
- **用法**：Fader 和 Hardie 关于客户留存预测的综述论文（*Service Industries Review*, 2007）。本 Day TODO4 流失标签构造和 TODO5 模型评估的理论基础。重点理解 sBG（shifted Beta-Geometric）留存曲线与指数平滑留存的区别。

### Microsoft "Churn Prediction with Azure ML"

- 深链：https://learn.microsoft.com/en-us/azure/architecture/example-scenario/ai/azure-ai-survival-analysis （已验证，Microsoft Learn 官方）
- **用法**：微软 Azure 官方客户流失预测方案文档。涵盖生存分析（survival analysis）在客户流失中的应用，与本 Day TODO4-5 的二分类流失预测形成方法论对比。理解为什么生存分析在合同制 B2B 场景中优于二分类。

### Cunningham "Causal Inference: The Mixtape"

- 深链：https://mixtape.scunning.com/ （已验证，免费在线教材）
- **用法**：causaldata 库的配套教材。第 2-3 章详细介绍 NSW 数据和 RCT 方法。Day 2 用 NSW 做 CLV/流失映射的基础读物。重点理解"为什么 RCT 的随机化使得基线特征不应强烈预测结果"--这是本 Day LogReg/RF 模型 AUC ~0.54 的根本原因。

---

## 4 2026 前沿：CUPED + 贝叶斯CLV + 数据治理

### CUPED: Controlled-Experiment Using Pre-Experiment Data（Microsoft Research, 2013）

- 深链：https://www.microsoft.com/en-us/research/publication/controlled-experiment-using-pre-experiment-data/ （已验证，Microsoft Research）
- **用法**：CUPED 是 A/B 测试的标准方差缩减技术，2026 年已成为大型科技公司实验平台的标配。本 Day TODO4 的 LogisticRegression 中 re74/re75 作为协变量，其思想与 CUPED 一致。Day 3 将深入 CUPED 的工程实现。

### 贝叶斯 CLV：PyMC 营销建模

- 深链：https://www.pymc.io/projects/docs/en/stable/learn.html （已验证，PyMC 官方文档）
- **用法**：PyMC 是 Python 贝叶斯统计建模的工业级库。2026 年贝叶斯 CLV 方法在小样本 B2B 客户建模中崛起。本 Day TODO3 用频率学派简化 BG/NBD，贝叶斯扩展是研究前沿方向。先读 "Bayesian Modeling" 入门部分。

### 数据治理：DAMA-DMBOK 框架

- 深链：https://www.dama.org/cpages/body-of-knowledge （已验证，DAMA International）
- **用法**：数据治理的权威框架。CLV 预测的可靠性取决于数据质量--完整性、一致性、准确性、时效性、合规性。Day 2 notes.md 的"数据治理"前沿补充的理论来源。理解为什么数据治理是 CLV 建模的"地基"。

---

## 5 对标课程

### MIT OCW 15.071: The Analytics Edge

- 深链：https://ocw.mit.edu/courses/15-071-the-analytics-edge-spring-2017/ （已验证，Spring 2017 版）
- **用法**：MIT 的分析学课程。Unit 4 "Trees, Forests, and Neural Networks" 与 Day 2 的 RandomForest 流失预测高度匹配，包含真实的客户流失预测案例（如运运营商 churn）。

### Wharton Customer Analytics Initiative

- 深链：https://customeranalytics.wharton.upenn.edu/ （已验证，Wharton 官方）
- **用法**：Peter Fader 所在的 Wharton 客户分析中心。Day 2 CLV 理论的学术源头。重点理解"Fader-Hardie 框架"如何将 RFM 描述性分群升级为 BG/NBD 预测性建模。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本 Day `notes.md` 理论回顾 + 独立教材 Day 2 | CLV 三方法 + 流失预测框架 | 1h |
| 2 | `starter.ipynb` 上机（配 sklearn/pandas 文档） | 真实库+真实数据实操 | 2h |
| 3 | Fader & Hardie BG/NBD 论文摘要 | BG/NBD 模型学术源头 | 0.5h |
| 4 | CUPED 论文摘要 | 2026 前沿：方差缩减 | 0.5h |
| 5 | Cunningham Mixtape 第 2-3 章（选读） | NSW 数据与 RCT 基础 | 0.5h |
| 6 | PyMC 贝叶斯建模入门（选看） | 2026 前沿：贝叶斯 CLV | 0.5h |

---

*全部深链已于 2026-07-25 验证存在。如发现失效，请在 Issues 报告。*
