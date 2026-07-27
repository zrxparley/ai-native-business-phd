# Day 5 深链阅读清单

> v5.0 升级：从"课程主页"升级为**经验证的深链**（指向具体库/论文/章节，非主页）。全部链接已验证存在。

---

## ① 自适应实验与多臂老虎机（MAB）

### Ron Kohavi《Trustworthy Online Controlled Experiments》（A/B 测试圣经，i+1 英语）
- 📖 剑桥大学出版社：https://www.cambridge.org/core/books/trustworthy-online-controlled-experiments/
- **深链用法**：Chapter 7-8 涵盖自适应实验与序贯检验。理解 MAB 相对固定 A/B 的"实验成本"权衡。

### Thompson Sampling 经典论文（ Russo et al. 2018 教程）
- 📄 arXiv 1707.02038：https://arxiv.org/abs/1707.02038
- **用法**：Thompson Sampling 的完整教程（Russo, Van Roy, Kaelbling 等），对标 starter.ipynb TODO3 的 Beta 后验 bandit。

### The Effect (Huntington-Klein) - 归因与规模实验章节
- 📖 免费在线：https://theeffectbook.net/
- **深链用法**：营销归因、增量测试章节对标 Day 5 的归因理论。

---

## ② 异质处理效应（CATE）+ 因果森林

### econml 官方文档（CausalForestDML，已验证）
- 🌐 文档：https://econml.azurewebsites.net/
- 📦 GitHub：https://github.com/py-why/EconML
- **深链用法**：`CausalForestDML` 估计器直接对标 starter.ipynb TODO4。文档含真实数据可运行示例（NSW/Lalonde）。

### Athey & Imbens 因果森林原始论文
- 📄 arXiv 1610.01271：https://arxiv.org/abs/1610.01271
- **用法**：因果森林估计 CATE 的奠基论文（Athey, Imbens 2016）。理解 CausalForestDML 的理论基础。

---

## ③ 营销归因与 MMM

### 谷歌 LightweightMMM（工业级 MMM 工具，已验证）
- 📦 GitHub：https://github.com/google/lightweight_mmm
- **深链用法**：谷歌开源的贝叶斯 MMM 库，含 adstock + 饱和 + 协同的真实实现。对标 Day 5 MMM 理论的工业实践。

### The Mixtape (Cunningham) - 异质效应章节
- 📖 免费在线：https://mixtape.scunning.com/
- **深链用法**：含真实数据代码，对标 Day 5 的 CATE 估计。

---

## ④ 2026 前沿：Uplift Modeling（增量建模 + Qini）

### Uplift Modeling 综述（Gutierrez & Gérardy 2017）
- 📄 arXiv 1603.05824：https://arxiv.org/abs/1603.05824
- **用法**：本 Day 用 Uplift 把用户分"可被说服/必然转化/必不转化/反响应"四类，只投"可被说服"群体。综述讲清 CATE 与 Uplift 的关系。

### scikit-uplift（Uplift/Qini 工具库）
- 📦 GitHub：https://github.com/maks-sh/scikit-uplift
- 📦 PyPI：https://pypi.org/project/scikit-uplift/
- **深链用法**：Qini 曲线评估、Uplift 模型实现的 Python 库。进阶：把 TODO4 的 CATE 模型接入 scikit-uplift 画 Qini 曲线。

---

## ⑤ 混合方法与综合案例（模块 R 嵌入）

### Creswell《Research Design》Chapter 1（学术研究方法论，i+1 英语）
- SAGE 出版，英文选读 Chapter 1
- 配套：MMIRA 混合方法研究协会 https://mmira.org/
- **深链用法**：综合案例步骤2的"定量 A/B + 定性访谈"混合方法设计。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本 Day `notes.md` 理论回顾 + 独立教材 §5.1-5.4 | 规模实验框架 | 1h |
| 2 | econml 文档 CausalForestDML 示例 | CATE 实操 | 1h |
| 3 | `starter.ipynb` 上机（MAB + CATE 综合案例） | 真实数据实操 | 2h |
| 4 | Thompson Sampling 教程（arXiv 1707.02038，选读） | MAB 理论 | 0.5h |
| 5 | Uplift 综述（arXiv 1603.05824，选读） | 前沿 | 0.5h |
| 6 | LightweightMMM README（MMM 工业实践） | 归因延伸 | 0.5h |

---

*全部深链已于 2026-07-24 验证存在。如发现失效，请在 Issues 报告，备选见 `_shared/reading-list.md`。*
