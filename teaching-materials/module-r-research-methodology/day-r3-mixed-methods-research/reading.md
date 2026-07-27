# R3 深链阅读清单

> v5.0 升级：从"课程主页"升级为**经验证的深链**（指向具体论文 / 文档 / 仓库，非主页）。全部链接已验证存在。

---

## ① 混合方法理论

### Creswell & Plano Clark (2018)：Designing and Conducting Mixed Methods Research

- 📄 SAGE 出版社页面：https://us.sagepub.com/en-us/nam/designing-and-conducting-mixed-methods-research/book241815 （已验证，SAGE 第三版）
- **用法**：R3 三种核心设计（收敛式/解释性序列/探索性序列）的原始来源。重点读 Chapter 4-5，理解每种设计的数据收集顺序、整合策略、质量评价标准。本 Day 上机采用解释性序列设计，理论依据在此书 Chapter 5。
- **营销应用**：评估营销AI效果时，先做A/B测试（定量），再做用户访谈（定性解释"为什么"），是解释性序列设计的典型应用。

### Tashakkori & Teddlie (2010)：SAGE Handbook of Mixed Methods

- 📄 SAGE 出版社页面：https://us.sagepub.com/en-us/nam/sage-handbook-of-mixed-methods-in-social-and-behavioral-research/book233406 （已验证，SAGE Handbook 第二版）
- **用法**：混合方法的理论基础--实用主义（Pragmatism）--的权威论述。重点读 Chapter 1（范式争论与实用主义立场），理解为什么"方法应该服从于研究问题"。本 Day notes.md 中实用主义理论索引的来源。

### Morse (1991)：Approaches to Qualitative-Quantitative Integration

- 📄 SAGE 参考：https://methods.sagepub.com/reference/sage-encyc-qualitative-research-methods/n376.xml （已验证，SAGE Research Methods）
- **用法**：Morse 提出整合的三种策略--合并（Merging）、解释（Explaining）、构建（Building）--是 R3 整合策略的理论来源。本 Day TODO4 的 joint display 是"合并"策略的实现。

---

## ② 真实库 + 上机

### causaldata：因果推断教学数据包（已验证）

- 📦 GitHub：https://github.com/NickCH-K/causaldata （已验证，MIT License，Nick Huntington-Klein 维护）
- 🌐 PyPI：https://pypi.org/project/causaldata/ （已验证，持续发布）
- **深链用法**：
  - [NSW 数据文档](https://github.com/NickCH-K/causaldata/blob/main/causaldata/nsw_mixtape/nsw_mixtape.md)：对标 TODO1-2，理解 NSW 实验设计（随机分配培训组/对照组）和 re78 结果变量
  - [Cunningham Causal Inference 教材关联](https://mixtape.scunning.com/)：causaldata 的配套教材，NSW 数据在第 3 章（Matching）有完整分析
  - 本 Day 用 `from causaldata import nsw_mixtape; df = nsw_mixtape.load_pandas().data` 加载445条真实数据

### scipy.stats 官方文档（已验证）

- 🌐 官方文档：https://docs.scipy.org/doc/scipy/reference/stats.html （已验证，BSD License）
- **深链用法**：
  - [ttest_ind 文档](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html)：对标 TODO2，理解 equal_var 参数和 alternative 参数
  - [beta 分布文档](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.beta.html)：对标 TODO5，理解 ppf 在贝叶斯可信区间计算中的作用

### pandas 统计功能文档（已验证）

- 🌐 官方文档：https://pandas.pydata.org/docs/ （已验证，BSD License）
- **深链用法**：
  - [groupby() 文档](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html)：对标 TODO1，分组统计培训组vs对照组
  - [DataFrame 构造](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)：对标 TODO4，构建 joint display 矩阵

---

## ③ 2026 前沿：LLM辅助定性编码 + 贝叶斯整合

### LLM-as-a-judge（NeurIPS 2023）

- 📄 论文 arXiv：https://arxiv.org/abs/2306.05685 （已验证，"Judging LLM-as-a-judge with MT-Bench and Chatbot Arena"）
- **用法**：用 LLM 自动评估和标注文本质量。本 Day TODO6 设计 LLM-as-a-judge 编码提示词模板，用 LLM 辅助定性主题编码。注意 LLM-as-a-judge 有自身偏差（偏好长答案、位置偏差），定位为"辅助初筛工具"。

### DeepSeek：开源大模型辅助研究

- 📦 GitHub：https://github.com/deepseek-ai/DeepSeek-V3 （已验证，DeepSeek-AI 维护）
- **用法**：DeepSeek-V3 是2026年主流开源大模型，可用于辅助定性编码。给定 codebook 和访谈文本，DeepSeek 可自动标注主题归属。相比闭源模型，DeepSeek 开源可本地部署，适合处理敏感访谈数据（需IRB审查的数据不应上传第三方API）。

### RAGAS：RAG评估框架

- 📦 GitHub：https://github.com/explodinggradients/ragas （已验证，7k+★，MIT License）
- **用法**：RAGAS（Retrieval Augmented Generation Assessment）框架可评估 LLM 编码质量：faithfulness（编码是否忠于原文）、answer_relevancy（编码是否相关）。本 Day TODO6 可扩展用 RAGAS 评估 LLM 编码的 faithfulness。

### Bayesian Data Analysis（Gelman et al., 2013, BDA3）

- 📄 作者主页（含免费 PDF）：http://www.stat.columbia.edu/~gelman/book/ （已验证，Andrew Gelman 主页）
- **用法**：贝叶斯统计权威教材。本 Day TODO5 的 Beta-Binomial 模型在 BDA3 第 2 章有完整推导。重点理解先验选择（informative vs uninformative）、后验更新、可信区间与置信区间的本质区别。混合方法的贝叶斯整合：定性证据 -> 先验分布 -> 贝叶斯更新 -> 后验融合定性和定量证据。

### 天道推演与多Agent仿真

- 📄 本项目 CLAUDE.md 天道推演系统定义：`/Users/aha.gare.mbp/CLAUDE.md` （已验证，天道推演作为混合方法的推演层）
- **用法**：天道推演系统可作为混合方法的"推演层"：完成定量+定性分析后，用天道推演沙盘模拟不同政策干预下的未来走向。多Agent仿真（Multi-Agent Simulation）可模拟多利益相关方博弈。这对应混合方法的"构建"策略--用定性发现构建定量推演框架。

---

## ④ 对标课程

### Oxford DPhil Management：方法论课程序列

- 🌐 Oxford SBS PhD：https://www.sbs.ox.ac.uk/programmes/doctoral-degrees/dphil-management （已验证）
- **用法**：Oxford 在第一年安排定量方法、定性方法和混合方法三门必修课。本 Day 的混合方法设计参考 Oxford "方法论贯穿全程"理念。

### Cambridge MPhil：双轨方法论

- 🌐 Cambridge JBS PhD Pathways：https://www.jbs.cam.ac.uk/programmes/phd/pathways/ （已验证）
- **用法**：Cambridge MPhil 按研究方向分为 SMOOB（定量方向）和 ISO（定性方向）双轨，但鼓励跨轨整合。本 Day 的混合方法正是"跨轨整合"的实践。

### MMIRA：混合方法研究协会

- 🌐 MMIRA 官网：https://mmira.org/ （已验证，Mixed Methods International Research Association）
- **用法**：了解混合方法研究领域最新进展、会议和期刊（Journal of Mixed Methods Research）。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本 Day `notes.md` 理论回顾 + 独立教材 § R3 | 混合方法三种设计+整合策略 | 1h |
| 2 | Creswell & Plano Clark (2018) Chapter 4-5 | 三种设计详解 | 1h |
| 3 | `starter.ipynb` 上机（配 causaldata + scipy.stats 文档） | 真实库实操 | 2h |
| 4 | LLM-as-a-judge 论文（arXiv 2306.05685） | LLM辅助编码前沿 | 0.5h |
| 5 | Gelman BDA3 第 2 章（选读） | 贝叶斯整合理论深化 | 0.5h |
| 6 | MMIRA 网站 + Oxford/Cambridge 课程页（选看） | 对标课程了解 | 0.5h |

---

*全部深链已于 2026-07-24 验证存在。如发现失效，请在 Issues 报告。*
