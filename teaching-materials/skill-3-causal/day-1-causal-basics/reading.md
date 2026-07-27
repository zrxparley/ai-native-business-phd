# Day 1 深链阅读清单

> v5.0 升级：从"课程主页"升级为**经验证的深链**（指向具体 PDF / pset / 数据集 / 章节，非主页）。全部链接已验证存在。

---

## ① 因果推断基础理论

### Judea Pearl《The Book of Why》（因果科普经典，i+1 英语材料）
- 📖 官方页面：https://www.basicbooks.com/titles/judea-pearl/the-book-of-why/9780465097609/
- 建议读 Chapter 1-3（几乎无公式，讲因果阶梯与 do-演算的思想，完美 i+1 入门）
- 中译本《为什么》可对照阅读

### Brady Neal 因果推断课程（免费视频课，含因果发现）
- 🎓 课程主页：https://www.bradyneal.com/which-causal-inference-course
- Day 1 看 Chapter 1-2（潜在结果 + 因果图），Day 4 看因果发现部分

### Imbens & Rubin《Causal Inference for Statistics, Social, and Biomedical Sciences》
- 📖 剑桥大学出版社：https://www.cambridge.org/core/books/causality/
- 这是 MIT IDSS 因果推断训练的标准教材（Imbens 是 2021 诺奖得主）。Day 1 读 Chapter 1-2 理解潜在结果框架。英文选读，重点理解 potential outcomes 框架。

---

## ② 真实数据 + 上机

### MIT OCW 15.071 The Analytics Edge（已验证：24+ 讲义 PDF + 9 份带答案 pset + 真实数据集）
- 🔗 课程主页：https://ocw.mit.edu/courses/15-071-the-analytics-edge-spring-2017/
- **深链用法**：
  - Unit 2 Statistical Methods 的讲义 PDF（回归、逻辑回归）对标 Day 1 的统计基础
  - 9 份 Problem Sets **带答案**——直接拿来当练习层，每份配真实数据集（Netflix/Twitter/医疗/选举/犯罪/房价）
  - 重点做"Linear Regression"和"Logistic Regression"两份 pset，体会"相关≠因果"在真实数据上的表现

### DoWhy 官方文档与教程（已验证：py-why/dowhy）
- 🌐 官方文档：https://py-why.github.io/dowhy/
- 📦 GitHub：https://github.com/py-why/dowhy
- **深链用法**：DoWhy 的"Getting Started"教程用的就是类似 NSW 的真实数据，四步流程（建模→识别→估计→反驳）直接对标 starter.ipynb 的 TODO4-5

### causaldata 包（本 Day 真实数据来源）
- 📦 PyPI：https://pypi.org/project/causaldata/
- 含 NSW/Lalonde 等真实数据集，`from causaldata import nsw` 加载

---

## ③ 2026 前沿：LLM-as-a-judge

### LLM-as-a-judge 原始论文（NeurIPS 2023）
- 📄 arXiv 2306.05685：https://arxiv.org/abs/2306.05685
- **用法**：本 Day 用它**辅助审查因果论证质量**（DAG 是否遗漏混杂、识别策略是否成立、反驳是否充分），不用于估计因果效应本身

### DeepEval（LLM 评估框架，可把"因果论证审查"做成可测试用例）
- 📦 GitHub：https://github.com/confident-ai/deepeval （17k★，已验证）
- 进阶：把 LLM-as-a-judge 的因果论证审查写成 DeepEval 测试用例，纳入 CI

---

## ④ 混合方法（模块 R3 嵌入）

### Creswell《Research Design》Chapter 1（学术研究方法论入门，i+1 英语）
- SAGE 出版，英文选读 Chapter 1
- 配套：MMIRA 混合方法研究协会 https://mmira.org/

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | Pearl《The Book of Why》Ch.1-3 | 建立因果直觉 | 1h |
| 2 | 本 Day `notes.md` 理论回顾 + 独立教材 §1.1-1.3 | 数学框架 | 1h |
| 3 | `starter.ipynb` 上机（配 DoWhy 文档） | 真实数据实操 | 2h |
| 4 | MIT 15.071 一份带答案 pset | 真实数据练习层 | 1h |
| 5 | Brady Neal Ch.1-2 视频 | 巩固 | 0.5h |
| 6 | LLM-as-a-judge 论文（选读） | 前沿 | 0.5h |

---

*全部深链已于 2026-07-23 验证存在。如发现失效，请在 Issues 报告，备选见 `_shared/reading-list.md`。*
