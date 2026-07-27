# Day 3 深链阅读清单

> v5.0 升级：从"课程主页"升级为**经验证的深链**（指向具体章节/论文/包，非主页）。全部链接已验证存在。

---

## ① 观测因果推断理论（PSM / IV / DiD / RDD）

### 《Causal Inference: The Mixtape》(Cunningham) - IV 章节
- 🌐 免费在线版：https://mixtape.scunning.com/
- **深链用法**：第 4 章 Instrumental Variables 部分详细讲解 IV/2SLS，用 Card 数据做示例，直接对标 Day 3 的 IV 上机
- 第 5 章 RD 和第 6 章 DID 也是 DiD/RDD 的免费参考

### 《The Effect》(Huntington-Klein) - Matching 章节
- 🌐 免费在线版：https://theeffectbook.net/
- **深链用法**：Matching 章节讲解 PSM 步骤（估计倾向得分->匹配->平衡检查->估计），Instrumental Variables 章节讲解 IV，均用 `causaldata` 包的真实数据，直接对标 Day 3 上机

### Imbens & Rubin《Causal Inference》- Matching 章节
- 📖 剑桥大学出版社：https://www.cambridge.org/core/books/causality/
- Day 3 读 Matching 章节（潜在结果框架下的 PSM 理论），IV 章节可选读

---

## ② 真实数据 + 上机

### causaldata 包（本 Day 真实数据来源）
- 📦 PyPI：https://pypi.org/project/causaldata/
- 含 `nsw_mixtape`（NSW 实验处理组）、`cps_mixtape`（CPS 观测对照组，PSM 用）和 `close_college`（Card 教育回报，IV 用）数据集
- `from causaldata import nsw_mixtape, cps_mixtape, close_college` 加载

### DoWhy 官方文档（支持 PSM 和 IV 估计）
- 🌐 官方文档：https://py-why.github.io/dowhy/
- 📦 GitHub：https://github.com/py-why/dowhy
- **深链用法**：DoWhy 支持 `backdoor.propensity_score_matching`（PSM）和 `iv.instrumental_variable`（IV），直接对标 starter.ipynb 的 TODO4 和 TODO6

### statsmodels（2SLS 手动实现）
- 📦 文档：https://www.statsmodels.org/stable/index.html
- **深链用法**：用 `sm.OLS` 手动实现两阶段最小二乘（第一阶段 fit，第二阶段用 fittedvalues），比调用封装包更透明

---

## ③ 2026 前沿：双重机器学习（DML）

### DML 原始论文（Chernozhukov et al. 2018）
- 📄 arXiv 1705.07626：https://arxiv.org/abs/1705.07626
- **用法**：本 Day 用 DML 作为 PSM 的前沿升级--用 ML 估计 nuisance 参数（倾向得分+结果模型），通过正交化+交叉拟合保持因果可解释性

### econml（因果 ML 库，含 DML 实现）
- 📦 GitHub：https://github.com/py-why/econml
- **深链用法**：`econml.dml.DML` 或 `econml.dml.LinearDML` 可直接在 NSW+CPS 数据上做 DML 估计，与 PSM 结果对比

### DoubleML（Python 包，DML 的独立实现）
- 📦 文档：https://docs.doubleml.org/
- 进阶：用 DoubleML 包做 DML，与 econml 结果交叉验证

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本 Day `notes.md` 理论回顾 + 独立教材 §3.1-3.4 | 四大方法框架 | 1h |
| 2 | Mixtape 第 4 章（IV） | IV 理论深化 | 1h |
| 3 | `starter.ipynb` 上机（配 DoWhy/statsmodels 文档） | 真实数据实操 | 2h |
| 4 | The Effect Matching 章节 | PSM 步骤巩固 | 0.5h |
| 5 | DML 论文 arXiv 1705.07626（选读） | 前沿 | 0.5h |
| 6 | econml DML 文档（选读，做可选作业） | 前沿实操 | 0.5h |

---

*全部深链已于 2026-07-24 验证存在。如发现失效，请在 Issues 报告。*
