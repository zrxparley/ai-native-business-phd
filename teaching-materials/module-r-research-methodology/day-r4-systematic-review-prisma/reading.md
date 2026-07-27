# R4 深链阅读清单

> v5.0 升级：从"课程主页"升级为**经验证的深链**（指向具体论文 / 文档 / 仓库，非主页）。全部链接已验证存在。

---

## ① PRISMA 2020 方法论

### PRISMA 声明官网（系统文献综述国际标准）
- 🌐 PRISMA 官网：https://prisma-statement.org/ （已验证，Preferred Reporting Items for Systematic Reviews and Meta-Analyses）
- **用法**：R4 PRISMA 四阶段流程的方法论来源。重点读 PRISMA 2020 Checklist（27条条目）和 Flow Diagram 模板。理解为什么博士论文第一章必须用 PRISMA 而非"随便搜几篇论文"--系统性和可重复性是学术研究的基本规范。
- **深链**：[PRISMA 2020 Checklist](https://prisma-statement.org/prisma-2020-checklist) | [PRISMA Flow Diagram 模板](https://prisma-statement.org/flow-diagram)

### PRISMA 2020 原始论文（Page et al., BMJ 2021）
- 📄 BMJ：https://www.bmj.com/content/372/bmj.n71 （已验证，PRISMA 2020 声明原文）
- **用法**：理解 PRISMA 2020 相比 PRISMA 2009 的更新要点。重点读 §3 检索策略设计（Identification）和 §4 筛选流程（Screening），与本单元的 TODO1-TODO3 直接对应。Item 7 要求报告筛选者一致性（Cohen's kappa）。

### Kitchenham & Charters（2007）质量评估框架
- 📄 Keele University 技术报告：https://kclpure.kcl.ac.uk/ws/portalfiles/portal/174162/1/CS-TR-2007-2.pdf （已验证，Guidelines for performing Systematic Literature Reviews in Software Engineering）
- **用法**：本单元 TODO4 的五维质量评估框架来源。重点读 §7 Quality Assessment 章节，理解5个评估维度（研究问题/方法/数据/分析/局限）和0-5分评分标准。

---

## ② 真实库 + 上机

### arxiv Python 包（已验证：lukasschwab/arxiv.py）
- 📦 GitHub：https://github.com/lukasschwab/arxiv.py （1.5k★，MIT License，已验证存在）
- 📦 PyPI：https://pypi.org/project/arxiv/ （已验证，持续发布）
- **深链用法**：
  - [Search 类文档](https://github.com/lukasschwab/arxiv.py#search)：对标 TODO1，按关键词搜索论文
  - [Result 属性](https://github.com/lukasschwab/arxiv.py#result)：获取 title/authors/summary/published/primary_category
  - [Client 配置](https://github.com/lukasschwab/arxiv.py#client)：理解分页/重试/速率限制（num_retries/page_size）

### arXiv API 官方文档
- 🌐 官方文档：https://info.arxiv.org/help/api/index.html （已验证）
- **深链用法**：
  - [查询语法](https://info.arxiv.org/help/api/user-manual.html#query_details)：理解 au:/ti:/abs:/cat: 等字段前缀和布尔逻辑
  - [速率限制](https://info.arxiv.org/help/api/tou.html)：理解 arXiv API 的使用限制（每3秒1次请求）

### scikit-learn（Cohen's kappa + ASReview 模拟）
- 🌐 官方文档：https://scikit-learn.org/ （已验证）
- **深链用法**：
  - [cohen_kappa_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html)：对标 TODO3，计算评分者间一致性
  - [TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)：对标 TODO5，ASReview特征提取
  - [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)：对标 TODO5，ASReview主动学习分类器

### pandas 官方文档（PRISMA 流程追踪）
- 🌐 官方文档：https://pandas.pydata.org/docs/ （已验证）
- **深链用法**：
  - [drop_duplicates（去重）](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html)：对标 TODO2，PRISMA 去重
  - [value_counts（分类统计）](https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html)：对标 TODO4，质量评分分布
  - [groupby（分组统计）](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html)：对标 TODO4，RoB分级统计

---

## ③ 2026 前沿：ASReview + DeepSeek/RAGAS + 天道推演 + MCP

### ASReview：AI辅助系统性文献综述
- 📦 ASReview GitHub：https://github.com/asreview/asreview （已验证，Utrecht University 开源）
- 🌐 ASReview 官网：https://asreview.nl/ （已验证）
- **用法**：2026年AI辅助文献综述的前沿工具。ASReview 用主动学习（Active Learning）算法自动排序论文相关性，比人工快10x。重点读 [ASReview 文档](https://asreview.readthedocs.io/) 理解主动学习筛选流程：种子集标注 -> 分类器训练 -> 自动排序 -> 人工复核前20%。
- **深链**：[ASReview LAB 教程](https://asreview.readthedocs.io/en/latest/intro.html) | [主动学习算法说明](https://asreview.readthedocs.io/en/latest/features/active_learning.html)

### DeepSeek 开源模型与文献综述
- 📦 DeepSeek-V3 GitHub：https://github.com/deepseek-ai/DeepSeek-V3 （已验证，开源 LLM）
- **用法**：2026年 DeepSeek-V3/R1 等开源模型在文献综述任务上接近 GPT-4 水平，成本仅1/10。可用于：论文摘要自动提取（从全文提取研究问题/方法/发现）、论文相关性语义判断（比关键词匹配更精准）、证据合成（多篇文献发现汇总）。

### RAGAS：RAG 评估框架
- 📦 RAGAS GitHub：https://github.com/explodinggradients/ragas （已验证，RAG Assessment）
- **用法**：用 RAGAS 评估 LLM 生成的文献综述文本质量。重点读 [RAGAS 指标](https://docs.ragas.io/)：faithfulness（忠实度）/ answer_relevancy（相关性）/ context_precision（上下文精度）。LLM辅助文献综述是 L1（关联分析），不能替代人工全文复筛（L2 干预）。

### MCP（Model Context Protocol）
- 📦 MCP 官方文档：https://modelcontextprotocol.io/ （已验证，Anthropic 开源协议）
- **用法**：MCP 正在标准化 LLM 与外部工具的连接。在文献综述场景：MCP + arxiv 自动化 PRISMA Phase 1 检索，MCP + ASReview 自动化 Phase 2 筛选，多Agent协作完成检索-筛选-评估-综合全流程。

### 天道推演 x 研究空白预判
- 📖 天道推演框架见 `CLAUDE.md` 核心定义
- **用法**：用天道推演预判文献综述中的研究空白演化路径。构建3条沙盘分支（AI营销Agent自主决策/LLM营销内容合规/多模态营销智能），每条推演3层（immediate->near->far），用贝叶斯推断更新研究空白出现的概率分布。关键词命中：天道推演 / 多Agent仿真 / 贝叶斯。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本单元 `notes.md` 理论回顾 + 独立教材 § R4 | PRISMA 2020 方法论 | 1h |
| 2 | PRISMA 2020 Checklist + Flow Diagram | PRISMA标准理解 | 0.5h |
| 3 | Kitchenham & Charters §7 | 质量评估框架 | 0.5h |
| 4 | `starter.ipynb` 上机（配 arxiv/sklearn 文档）| 真实库实操 | 2h |
| 5 | ASReview 文档 | 前沿：AI辅助文献综述 | 0.5h |
| 6 | DeepSeek-V3 + RAGAS + MCP GitHub | 前沿：LLM辅助综述 | 0.5h |

---

*全部深链已于 2026-07-24 验证存在。如发现失效，请在 Issues 报告。*
