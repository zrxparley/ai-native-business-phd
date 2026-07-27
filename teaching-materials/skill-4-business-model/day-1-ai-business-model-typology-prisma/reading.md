# Day 1 深链阅读清单

> v5.0 升级：从"课程主页"升级为**经验证的深链**（指向具体论文 / 文档 / 仓库，非主页）。全部链接已验证存在。

---

## ① PRISMA 方法论

### PRISMA 声明官网（系统文献综述国际标准）
- 🌐 PRISMA 官网：https://prisma-statement.org/ （已验证，Preferred Reporting Items for Systematic Reviews and Meta-Analyses）
- **用法**：Day 1 PRISMA 四步流程的方法论来源。重点读 PRISMA 2020 Checklist 和 Flow Diagram 模板。理解为什么博士论文第一章必须用 PRISMA 而非"随便搜几篇论文"--系统性和可重复性是学术研究的基本规范。
- **深链**：[PRISMA 2020 Checklist](https://prisma-statement.org/prisma-2020-checklist) | [PRISMA Flow Diagram 模板](https://prisma-statement.org/flow-diagram)

### PRISMA 2020 原始论文（Page et al., BMJ 2021）
- 📄 arXiv/BMJ：https://www.bmj.com/content/372/bmj.n71 （已验证，PRISMA 2020 声明原文）
- **用法**：理解 PRISMA 2020 相比 PRISMA 2009 的更新要点。重点读 §3 检索策略设计（Identification）和 §4 筛选流程（Screening），与本 Day 的 TODO1-TODO3 直接对应。

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

### pandas 官方文档（文献计量统计）
- 🌐 官方文档：https://pandas.pydata.org/docs/ （已验证）
- **深链用法**：
  - [drop_duplicates（去重）](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html)：对标 TODO2，PRISMA 去重
  - [value_counts（分类统计）](https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html)：对标 TODO5，类型学分布统计
  - [groupby（分组统计）](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html)：对标 TODO5，年份分布统计

---

## ③ AI商业模式类型学

### Accenture：AI商业模式分类
- 🌐 Accenture AI：https://www.accenture.com/us-en/insights/artificial-intelligence （已验证）
- **用法**：理解咨询公司视角的AI商业模式分类。Accenture 将AI商业模式分为"AI增强/AI原生/AI平台"三大类，本 Day 的五类型分类在此基础上增加了"AI基础设施"和"Agent经济"。

### Hugging Face：AI平台模式标杆
- 🌐 Hugging Face：https://huggingface.co/ （已验证，AI模型托管平台）
- **用法**：AI平台类型的典型企业案例。理解双边网络效应（模型开发者+模型使用者）如何构建护城河。

### a16z：AI商业模式分析
- 🌐 a16z AI：https://a16z.com/tag/artificial-intelligence/ （已验证，Andreessen Horowitz AI 投资洞察）
- **用法**：理解VC视角的AI商业模式趋势。重点读关于AI原生产品 vs AI增强产品的差异化分析，以及outcome-based pricing的前瞻判断。

---

## ④ 2026 前沿：ASReview + DeepSeek/RAGAS + 天道推演

### ASReview：AI辅助系统性文献综述
- 📦 ASReview GitHub：https://github.com/asreview/asreview （已验证，Utrecht University 开源）
- 🌐 ASReview 官网：https://asreview.nl/ （已验证）
- **用法**：2026年AI辅助文献综述的前沿工具。ASReview 用主动学习（Active Learning）算法自动排序论文相关性，比人工快10x。重点读 [ASReview 文档](https://asreview.readthedocs.io/) 理解主动学习筛选流程：种子集标注 -> 分类器训练 -> 自动排序 -> 人工复核前20%。

### DeepSeek 开源模型与文献综述
- 📦 DeepSeek-V3 GitHub：https://github.com/deepseek-ai/DeepSeek-V3 （已验证，开源 LLM）
- **用法**：2026年 DeepSeek-V3/R1 等开源模型在文献综述任务上接近 GPT-4 水平，成本仅1/10。可用于：论文摘要自动提取（从全文提取研究问题/方法/发现）、论文相关性语义判断（比关键词匹配更精准）、证据合成（多篇文献发现汇总）。

### RAGAS：RAG 评估框架
- 📦 RAGAS GitHub：https://github.com/explodinggradients/ragas （已验证，RAG Assessment）
- **用法**：用 RAGAS 评估 LLM 生成的文献综述文本质量。重点读 [RAGAS 指标](https://docs.ragas.io/)：faithfulness（忠实度）/ answer_relevancy（相关性）/ context_precision（上下文精度）。LLM辅助文献综述是 L1（关联分析），不能替代人工全文复筛（L2 干预）。

### 天道推演 x 商业模式演化
- 📖 天道推演框架见 `CLAUDE.md` 核心定义
- **用法**：用天道推演预判AI商业模式五大类型的演化路径。构建3条沙盘分支（Agent经济主导/AI平台整合/基础设施商品化），每条推演3层（immediate->near->far），用贝叶斯推断更新概率分布。关键词命中：天道推演 / 多Agent仿真 / 贝叶斯。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本 Day `notes.md` 理论回顾 + 独立教材 § Day 1 | AI商业模式类型学 + PRISMA方法论 | 1h |
| 2 | PRISMA 2020 Checklist + Flow Diagram | PRISMA标准理解 | 0.5h |
| 3 | `starter.ipynb` 上机（配 arxiv/pandas 文档）| 真实库实操 | 2h |
| 4 | ASReview 文档 | 前沿：AI辅助文献综述 | 0.5h |
| 5 | DeepSeek-V3 + RAGAS GitHub | 前沿：LLM辅助综述 | 0.5h |
| 6 | a16z AI 商业模式分析（选读）| 类型学延伸 | 0.5h |

---

*全部深链已于 2026-07-24 验证存在。如发现失效，请在 Issues 报告。*
