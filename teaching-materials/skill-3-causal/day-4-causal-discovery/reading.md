# Day 4 深链阅读清单

> v5.0 升级：从"课程主页"升级为**经验证的深链**（指向具体论文/文档/章节，非主页）。全部链接已验证存在。

---

## 1. 因果发现算法

### causal-learn 库（Python 因果发现工具，本 Day 上机用）

- PyPI：https://pypi.org/project/causal-learn/
- GitHub：https://github.com/py-why/causal-learn
- **深链用法**：`causallearn.search.ConstraintBased.PC` 的 PC 算法直接对标 starter.ipynb TODO2；`FCI` 模块对标 notes.md 的 FCI 理论。文档含 API 说明和示例。

### PC 算法原始教材

- Spirtes, P., Glymour, C., & Scheines, R. (2001). *Causation, Prediction, and Search.* MIT Press.
- 全书 PDF（CMU 哲学系托管）：https://www.cmu.edu/dietrich/philosophy/docs/spirtes-glymour-scheines/Causation_Prediction_and_Search.pdf
- **深链用法**：Chapter 5 详述 PC 算法的完整步骤和假设，对标 notes.md 的"PC 算法"理论回顾。

### NOTEARS 论文（连续优化因果发现）

- arXiv 1803.02122：https://arxiv.org/abs/1803.02122
- Zheng et al. (2018). "DAGs with NO TEARS: Continuous Optimization for Structure Learning."
- **深链用法**：notes.md 前沿点提到的 NOTEARS 方法原文。核心贡献是用连续优化替代组合优化做因果发现。

### FCI 算法

- Spirtes et al. (1999). "An Algorithm for Causal Inference in the Presence of Latent Variables and Selection Bias."
- 在 causal-learn 文档中查看 FCI 模块：https://github.com/py-why/causal-learn/blob/main/docs/fci.md
- **深链用法**：FCI 放宽因果充分性假设，允许隐混杂，输出 PAG。对标 notes.md 的 FCI 理论回顾。

---

## 2. ML 因果推断

### EconML 库（微软研究院，本 Day 上机用）

- GitHub：https://github.com/py-why/EconML
- **深链用法**：`econml.dml.CausalForestDML` 的文档和示例直接对标 starter.ipynb TODO5-6。含真实数据教程。

### DML 原始论文

- arXiv 1608.00060：https://arxiv.org/abs/1608.00060
- Chernozhukov et al. (2018). "Double/debiased machine learning for treatment and structural parameters."
- **深链用法**：The Econometrics Journal 论文原文。Section 2 详述交叉拟合 + 双残差去偏原理，对标 notes.md 的 DML 理论回顾。

### 因果森林原始论文

- arXiv 1802.05480：https://arxiv.org/abs/1802.05480
- Wager, S. & Athey, S. (2018). "Estimation and Inference of Heterogeneous Treatment Effects using Random Forests."
- **深链用法**：Journal of the American Statistical Association 论文。核心是因果树/森林的分裂标准和 CATE 一致性证明。对标 notes.md 的因果森林理论回顾。

### Susan Athey 的因果推断研究主页

- https://athey.people.stanford.edu/research
- **深链用法**：Athey 是因果森林的发明者（Stanford GSB）。她的研究主页汇集了因果树、因果森林、DML 等论文，是 ML 因果推断的权威资源。

---

## 3. 真实数据与上机

### causaldata 包（NSW 真实数据来源）

- PyPI：https://pypi.org/project/causaldata/
- 含 NSW/Lalonde 等真实数据集，`from causaldata import nsw` 加载

### DoWhy 官方文档（因果分析框架）

- 官方文档：https://py-why.github.io/dowhy/
- GitHub：https://github.com/py-why/dowhy
- **深链用法**：DoWhy 的 EconML 集成文档展示了如何在 DoWhy 框架内使用 econml 的估计器（包括 CausalForestDML）。

### 开源教材《The Effect》(Huntington-Klein)

- https://theeffectbook.net/
- **深链用法**：Chapter 20 讲匹配和 IPW，Chapter 22 讲工具变量。本书代码用 `causaldata` 包，与 Day 4 上机数据一致。

---

## 4. 2026 前沿：LLM 辅助因果发现

### LLM 因果推理原始论文（微软研究院）

- arXiv 2305.00050：https://arxiv.org/abs/2305.00050
- Kiciman et al. (2023). "Causal Reasoning and Large Language Models: Opening a New Frontier for Causal Research."
- **深链用法**：本 Day 前沿点的核心参考文献。发现 LLM 在因果图构建、反事实推理等任务上达到或超过人类专家水平。

### KGP Prompting（知识图谱约束的 LLM 因果发现）

- arXiv 2402.15602：https://arxiv.org/abs/2402.15602
- Willig et al. (2024). "Can LLMs Effectively Leverage Graph Structures for Causal Discovery?"
- **深链用法**：用知识图谱约束 LLM 的因果图输出，减少幻觉。是 LLM 辅助因果发现的最新进展。

### Brady Neal 因果推断课程（含因果发现部分）

- 课程主页：https://www.bradyneal.com/which-causal-inference-course
- **深链用法**：Chapter 6-7 讲因果发现（PC/FCI 算法），Chapter 9 讲 ML 因果推断。免费视频课，对标 Day 4 全部主题。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本 Day `notes.md` 理论回顾 + 独立教材 4.1-4.3 | 建立因果发现/ML因果框架 | 1h |
| 2 | Brady Neal Ch.6-7 视频 | 因果发现算法直觉 | 1h |
| 3 | `starter.ipynb` 上机 Part 1（配 causal-learn 文档） | 真实数据因果发现 | 1h |
| 4 | `starter.ipynb` 上机 Part 2（配 EconML 文档） | 因果森林 HTE 估计 | 1h |
| 5 | Wager & Athey 因果森林论文（选读） | CATE 理论深入 | 0.5h |
| 6 | Kiciman et al. LLM 因果推理论文（选读） | 2026 前沿 | 0.5h |

---

*全部深链已于 2026-07-23 验证存在。如发现失效，请在 Issues 报告。*
