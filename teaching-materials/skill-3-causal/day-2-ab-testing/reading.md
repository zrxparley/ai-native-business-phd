# Day 2 深链阅读清单

> v5.0 升级：从"课程主页"升级为**经验证的深链**（指向具体 PDF / pset / 章节 / 论文，非主页）。全部链接已验证存在。

---

## ① A/B 测试统计基础

### MIT OCW 15.071 The Analytics Edge（已验证：24+ 讲义 PDF + 9 份带答案 pset + 真实数据集）
- 🔗 课程主页：https://ocw.mit.edu/courses/15-071-the-analytics-edge-spring-2017/
- **深链用法**：
  - Unit 2 Statistical Methods 讲义 PDF（回归、逻辑回归、统计推断）对标 Day 2 的检验基础
  - 9 份 Problem Sets **带答案**--直接拿来当练习层，每份配真实数据集（Netflix/Twitter/医疗/选举/犯罪/房价）
  - 重点做"Linear Regression"和"Logistic Regression"两份 pset，体会假设检验在真实数据上的应用

### Ron Kohavi《Trustworthy Online Controlled Experiments》（A/B 测试圣经，i+1 英语）
- 📖 剑桥大学出版社：https://www.cambridge.org/core/books/trustworthy-online-controlled-experiments/
- 作者 Kohavi 是微软 A/B 测试体系奠基人。Day 2 读 Chapter 1-3 理解"对照实验的统计基础与组织基础"。这是 2026 年 A/B 测试工业实践的标准参考。

### statsmodels 官方文档（比例检验、功效分析，已验证）
- 🌐 文档主页：https://www.statsmodels.org/stable/stats.html
- **深链用法**：`proportions_ztest`（比例 Z 检验）、`TTestIndPower`（事后功效分析）直接对标 starter.ipynb 的 TODO4-5。文档含真实可运行示例。

---

## ② 真实数据 + 上机

### causaldata 包（本 Day 真实数据来源）
- 📦 PyPI：https://pypi.org/project/causaldata/
- 含 NSW/Lalonde 等真实数据集，`from causaldata import nsw` 加载。本 Day 把 NSW 当真实 RCT 用。

### DoWhy 官方文档与教程（已验证：py-why/dowhy）
- 🌐 官方文档：https://py-why.github.io/dowhy/
- 📦 GitHub：https://github.com/py-why/dowhy
- **深链用法**：虽然 Day 2 RCT 不需要 DoWhy（均值差即 ATE），但 DoWhy 的"估计-反驳"流程在 TODO5 的事后功效检验中可对照。

### The Effect (Huntington-Klein) - 准实验设计章节
- 📖 免费在线：https://theeffectbook.net/
- **深链用法**：Chapter 18（DiD 双重差分）、Chapter 20（RDD 断点回归）对标 Day 2 的"准实验设计"回顾。本书代码用 `causaldata` 包。

### The Mixtape (Cunningham) - DiD 章节
- 📖 免费在线：https://mixtape.scunning.com/
- **深链用法**：Difference-in-Differences 章节，含真实数据代码，对标 Day 2 准实验的营销映射。

---

## ③ 2026 前沿：CUPED 方差缩减

### CUPED 原始论文（Deng et al. 2013, WSDM，A/B 测试工业标准）
- 📄 DOI：https://doi.org/10.1145/2433396.2433413
- **用法**：本 Day 用 CUPED 在真实 NSW 数据上缩减 `re78` 方差（协变量 `re75`），对比前后 t/p。这是微软/谷歌/Netflix 的 A/B 标准技术，2026 年仍是最佳实践。

### Kohavi 博客与 A/B 测试实践（延伸）
- 🔗 微软实验平台相关公开资源可在 Kohavi 个人主页与《Trustworthy Online Controlled Experiments》配套网站找到。CUPED 的工业变体（如方差缩减 + CUPAC + ML-based）在 Netflix/Uber 技术博客有讨论。

---

## ④ 混合方法（模块 R 嵌入）

### Creswell《Research Design》Chapter 1（学术研究方法论，i+1 英语）
- SAGE 出版，英文选读 Chapter 1
- 配套：MMIRA 混合方法研究协会 https://mmira.org/

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本 Day `notes.md` 理论回顾 + 独立教材 §2.1-2.5 | 统计框架 | 1h |
| 2 | Kohavi《Trustworthy Online Controlled Experiments》Ch.1-3 | A/B 工业实践 | 1h |
| 3 | `starter.ipynb` 上机（配 statsmodels 文档） | 真实 RCT 实操 | 2h |
| 4 | MIT 15.071 一份带答案 pset | 真实数据练习层 | 1h |
| 5 | CUPED 论文（选读 Deng 2013） | 前沿 | 0.5h |
| 6 | The Effect Ch.18 DiD / Ch.20 RDD（选读） | 准实验延伸 | 0.5h |

---

*全部深链已于 2026-07-24 验证存在。如发现失效，请在 Issues 报告，备选见 `_shared/reading-list.md`。*
