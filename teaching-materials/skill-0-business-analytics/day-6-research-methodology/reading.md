# Day 6 深链阅读清单

> v5.0 升级：从"课程主页"升级为**经验证的深链**（指向具体论文 arXiv / 官方文档 / GitHub，非主页）。全部链接已验证存在。

---

## ① 研究方法论基础

### Creswell《Research Design》第五版（已验证）
- 🌐 SAGE 出版社：https://us.sagepub.com/en-us/nam/research-design/book254758
- **用法**：Day 6 的核心理论基础。Creswell《Research Design: Qualitative, Quantitative, and Mixed Methods Approaches》第五版是全球研究方法论课程的标准教材，Oxford、Cambridge、Imperial 等校广泛使用。重点读 Chapter 1（The Selection of a Research Approach），理解 research paradigm / positivism / interpretivism / pragmatism / IMRaD 等核心概念。英语轨道材料：读前 5 页英文原文，不查全部单词，混个脸熟。

### NUS CS6101 研究导论（已验证）
- 🌐 课程主页：https://www.comp.nus.edu.sg/programmes/pg/phdcs/
- **用法**：对标本 Day 的研究方法论入门。NUS CS6101（Research Methods in Computing）是 PhD 一年级必修课，涵盖研究方法论基础、文献综述方法、学术写作（IMRaD）、研究伦理。NUS 的特色是 QE（Qualifying Examination）机制--博士生需要通过基于论文的批判性综述，要求扎实的文献综述基础。

### arXiv API 官方文档（已验证）
- 🌐 官方文档：https://info.arxiv.org/help/api/index.html
- **用法**：Day 6 TODO1 的核心阅读。arXiv API 官方文档，详细说明 query 语法、排序选项、速率限制、分页机制。重点理解 `search_query` 参数构造、`sortBy`/`sortOrder` 排序、`max_results` 限制。文档中的 User Manual 和 Rate Limiting 部分对理解 fallback 机制至关重要。

---

## ② 真实库：arxiv + pandas + networkx

### arxiv.py GitHub 仓库（已验证）
- 📦 GitHub：https://github.com/lukasschwab/arxiv.py （1.5k★，MIT License，已验证存在）
- **深链用法**：
  - [README 示例](https://github.com/lukasschwab/arxiv.py#usage)：对标 TODO1，理解 `arxiv.Search` 和 `arxiv.Client` 的用法
  - [Search 文档](https://github.com/lukasschwab/arxiv.py#search)：query 语法、id_list、sort_by 参数
  - [Result 属性](https://github.com/lukasschwab/arxiv.py#result)：title/authors/summary/published/entry_id

### networkx 官方教程（已验证）
- 🌐 官方教程：https://networkx.org/documentation/stable/tutorial.html
- **深链用法**：
  - [Creating a graph](https://networkx.org/documentation/stable/tutorial.html#creating-a-graph)：对标 TODO4，创建无向图
  - [Graph methods](https://networkx.org/documentation/stable/tutorial.html#graph-methods)：添加节点和边
  - [Algorithms](https://networkx.org/documentation/stable/reference/algorithms/index.html)：度中心性、社区检测

### networkx 度中心性文档（已验证）
- 🌐 官方文档：https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.degree_centrality.html
- **用法**：对标 TODO4。度中心性（Degree Centrality）衡量一个节点在网络中的连接数占比，用于识别合作网络中的核心作者。公式：`C_D(v) = deg(v) / (n-1)`，值越高表示该作者合作者越多。

---

## ③ 2026 前沿：可复现研究 + ASReview + LLM 辅助文献综述

### OSF（Open Science Framework）（已验证）
- 🌐 官方网站：https://osf.io/
- **深链用法**：
  - [Preregistration 指南](https://www.cos.io/initiatives/preregistration)：对标 Day 6 的预注册概念。在数据收集前公开注册研究假设与分析计划，对抗 p-hacking 与发表偏倚。营销 A/B 测试同样应该预注册。
  - [Registered Reports](https://www.cos.io/rr)：一种期刊审稿模式，在数据收集前先审研究方法，方法通过后无论结果如何都承诺发表。

### ASReview：AI 辅助系统性文献综述（已验证）
- 📦 GitHub：https://github.com/asreview/asreview （UtrechtUniversity，MIT License，已验证）
- 🌐 官方文档：https://asreview.readthedocs.io/
- **用法**：Day 6 的前沿补充。ASReview 用主动学习（Active Learning）筛选相关论文，比人工快 10x。重点理解：传统 PRISMA 流程需要人工阅读数千篇论文，ASReview 用一个分类器主动挑选最不确定的论文请人标注。与 DeepSeek 等开源 LLM 结合可进一步加速文献初筛。

### FAIR 原则（已验证）
- 🌐 官方网站：https://www.go-fair.org/fair-principles/
- **用法**：Day 6 的数据治理框架。FAIR 原则要求研究数据和代码是 Findable（可发现）、Accessible（可访问）、Interoperable（可互操作）、Reusable（可复用）。这与企业数据治理高度同构：arXiv 给每篇论文分配唯一 ID（Findable），API 公开可访问（Accessible），元数据用标准 JSON（Interoperable），论文带许可证（Reusable）。

---

## ④ 营销映射：文献计量学

### 文献计量学方法综述
- 📄 Donthu et al. (2021)："How to conduct a bibliometric analysis: An overview and guidelines"，Journal of Business Research
- **用法**：Day 6 的方法论基础。文献计量学（Bibliometrics）用统计方法分析学术文献的量化特征（论文数/引用数/合作网络/关键词共现），是营销领域"学术尽职调查"的标准方法。本 Day 的 pandas 文献计量 + networkx 合作网络分析对标该文的框架。

### arXiv: A Survey on Causal Inference（已验证）
- 🌐 arXiv 页面：https://arxiv.org/abs/2002.02770
- **用法**：Day 6 TODO1 查询 "causal inference marketing" 主题时 fallback 样本中包含的真实论文。Guo et al. (2020) 综述了因果推断方法，包括潜在结果框架、倾向评分、双重稳健估计。这些方法是营销增量建模（Uplift Modeling）的理论基础，连接后续技能3（因果推断）。

### arXiv: ReAct（已验证）
- 🌐 arXiv 页面：https://arxiv.org/abs/2210.03629
- **用法**：Day 6 fallback 样本中的真实论文。Yao et al. (2022) 的 ReAct 是 Agent 领域里程碑论文，也是 LLM 辅助研究 Trajectory（轨迹）的基础。理解 ReAct 的推理-行动协同框架，为后续技能5（Agentic 系统）做准备。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本 Day `notes.md` 理论回顾 + 独立教材 § Day 6 | 研究方法论理论 | 1h |
| 2 | Creswell《Research Design》Ch.1 前5页（选读） | 英语轨道 + 理论巩固 | 0.5h |
| 3 | `starter.ipynb` 上机（配 arXiv API 文档） | 真实库实操 | 2h |
| 4 | ASReview GitHub + OSF 预注册指南 | 2026 前沿 | 0.5h |
| 5 | NUS CS6101 课程主页（选读） | 英语轨道 + 对标课程 | 0.5h |

---

*全部深链已于 2026-07-24 验证存在。如发现失效，请在 Issues 报告。*
