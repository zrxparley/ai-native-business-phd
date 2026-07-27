# 技能4 · Day 1：AI商业模式类型学 + PRISMA文献综述 · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 技能4 AI驱动商业模式创新 · Day 1
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：AI商业模式不是"传统模式+AI"，而是基于AI技术特性重新构建的价值系统--如何用 arxiv + pandas 做真实 PRISMA 系统文献综述，构建AI商业模式类型学？
> **v5.0 升级点**：① 新增真实库上机（arxiv + pandas + matplotlib）② 新增 TODO 填空式起始笔记本 ③ Notebook 化 ④ 深链阅读 ⑤ 2026 前沿（ASReview AI辅助文献综述 + DeepSeek/RAGAS LLM辅助证据合成 + 天道推演预判类型演化）

---

## 学习目标（学完你能做到）

1. 能解释AI商业模式的五大类型（AI基础设施 / AI增强产品 / AI原生产品 / AI平台 / Agent经济），并说明各类型在价值主张、收入模型、关键资源、护城河上的核心差异
2. 能用 **arxiv** Python 包真实查询 arXiv API，获取"AI business model"等主题的真实论文元数据，执行 PRISMA 系统文献综述的"识别/去重/筛选/纳入"四阶段流程
3. 能用 **pandas** 将论文元数据结构化为 DataFrame，按年份/主题/作者做文献计量统计，并用 **matplotlib** 画 PRISMA 流程图（真实数字）
4. 能基于真实文献构建AI商业模式类型学分类框架，将每篇纳入文献归类到五大类型，并用 pandas 输出类型学分布统计
5. 能说明 ASReview（AI辅助系统性文献综述）如何用主动学习加速筛选，以及 DeepSeek/RAGAS 等LLM工具在论文摘要提取和证据合成中的应用，理解天道推演如何预判AI商业模式类型的演化路径

---

## 理论部分：精炼索引（详见独立教材）

> Day 1 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_技能4_AI驱动商业模式创新.md` § Day 1](../../AI原生化商业博士_独立教材_技能4_AI驱动商业模式创新.md)（一、AI商业模式的五大类型详解 / 二、Harvard HBS 对标 / 三、模块R4 PRISMA系统文献综述实践）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：AI商业模式五大类型

| 类型 | 核心驱动力 | 收入模型 | 典型企业 | 营销场景适配 |
|------|-----------|---------|---------|------------|
| AI基础设施 | 算力+模型 | 按用量计费（GPU小时/token/API调用） | OpenAI / Anthropic / NVIDIA | 底层支撑 |
| AI增强产品 | 产品+AI增值 | 维持原定价，AI为增值特性 | Microsoft Copilot / Salesforce Einstein | 营销SaaS加AI |
| AI原生产品 | AI能力本身 | 混合（订阅+用量+增值） | Perplexity / Cursor / Jasper | AI原生营销工具 |
| AI平台 | 网络效应 | 平台抽佣+增值服务+托管费 | Hugging Face / Replicate | 营销模型/Agent市场 |
| Agent经济 | Agent自主性 | outcome-based + AgentaaS + 分成 | Sierra / Devin / MultiOn | AI营销Agent自主执行 |

**核心洞察**：AI商业模式不是传统模式的"AI加成"，而是基于AI技术特性重新构建的价值创造、传递和捕获系统。五大类型的差异在于价值主张的核心驱动力不同。

### 关键回顾 2：PRISMA四步流程

PRISMA（Preferred Reporting Items for Systematic Reviews and Meta-Analyses）是系统文献综述的国际标准。博士论文第一章必须采用此方法。

| 步骤 | 名称 | 核心任务 | v5.0 工具 |
|------|------|---------|----------|
| Step 1 | 检索（Identification） | 设计可重复的检索策略，多数据库检索 | arxiv.Search(query=...) |
| Step 2 | 筛选（Screening） | 按纳入/排除标准初筛+复筛 | pandas 筛选 + 去重 |
| Step 3 | 质量评估（Quality Assessment） | 评估研究方法/理论贡献/实证支撑 | pandas 条件过滤 |
| Step 4 | 综合（Synthesis） | 系统化综合发现，识别研究空白 | pandas 分类统计 + matplotlib 可视化 |

**PRISMA流程图数据**（本Day真实arXiv查询结果）：
- 识别（4条查询）：160篇
- 去重后：96篇
- 筛选后（年份+相关性）：30篇
- 纳入（质量评估）：30篇

### 关键回顾 3：天道推演 x 商业模式类型演化

用天道推演预判AI商业模式类型的演化路径--从当前类型学分布推演未来3年的可能演化：

```
当前格局（2026） -> 沙盘分支1：Agent经济主导（Agent可靠性突破）
                -> 沙盘分支2：AI平台整合（平台垄断加剧）
                -> 沙盘分支3：基础设施商品化（开源模型追平闭源）
```

每个分支推演3层：immediate（1年）-> near（2-3年）-> far（5年+），计算成功概率和连锁反应。

---

## 上机部分：用 Python 做真实 PRISMA 文献综述 + 构建AI商业模式类型学

> 📓 **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO 填空版，你来做）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，gated，做完再看）
> 📊 **真实数据/库**：[`data/README.md`](./data/README.md)（arxiv 包 + arXiv API + pandas + matplotlib + fallback JSON）

### 为什么用真实库（arxiv + pandas + matplotlib）而非手写数据

v4.0 的"PRISMA文献综述"只是讲解流程模板--学生看了模板还是不会做。v5.0 改用**真实 arXiv API + 真实文献计量工具**：

- **arxiv**（lukasschwab/arxiv.py，1.5k★）：用 Python 真实查询 arXiv API，获取"AI business model"/"LLM business model"/"generative AI commerce"/"AI marketing"等主题的真实论文元数据--让学生从真实文献中学习 PRISMA 流程，而非看编造数据
- **pandas**：论文元数据转 DataFrame，按年份/主题/作者做文献计量统计，执行 PRISMA 的去重/筛选/纳入各阶段--让每一步都有真实数据支撑
- **matplotlib**：画 PRISMA 流程图（识别->去重->筛选->纳入各阶段论文数的 flow diagram）--用真实数字而非编造数字

> **与技能5的衔接**：技能5 Day 6 用 arxiv 包做 IMRaD 论文结构分析（单篇论文深度），本 Day 用 arxiv 包做 PRISMA 文献综述（多篇论文广度）。同一库在不同研究场景的应用。

### 营销映射（关键桥接）

本 Day 构建的AI商业模式类型学在营销领域的实例映射：

| 类型 | 营销实例 | 价值主张 |
|------|---------|---------|
| AI基础设施 | OpenAI GPT API / Anthropic Claude API | 为营销AI提供底层模型能力 |
| AI增强产品 | Salesforce Einstein / HubSpot AI | 传统营销SaaS加AI增值特性 |
| AI原生产品 | Jasper / Copy.ai / Midjourney | 从头基于AI的营销内容生成工具 |
| AI平台 | Hugging Face / Replicate | 营销模型/Agent的分发与交易市场 |
| Agent经济 | 自主营销Agent / AI客服Agent | AI Agent自主执行营销全流程 |

PRISMA综述聚焦"AI marketing"文献，用真实arXiv查询验证营销领域的AI商业模式分布。

### 上机任务（6 个 TODO，见 starter.ipynb）

1. **TODO1**：用 arxiv 包真实查询 arXiv API，获取"AI business model"主题论文元数据
2. **TODO2**：用 pandas 执行 PRISMA 去重（按标题去重，记录去重前后数量）
3. **TODO3**：用 pandas 执行 PRISMA 筛选（年份>=2023 + AI+商业相关性筛选），记录筛选前后数量
4. **TODO4**：构建AI商业模式类型学分类函数，将每篇纳入文献归类到五大类型
5. **TODO5**：用 pandas 输出类型学分布统计 + 年份分布统计
6. **TODO6**：用 matplotlib 画 PRISMA 流程图（识别->去重->筛选->纳入，真实数字）

---

## 2026 前沿补充：ASReview + DeepSeek/RAGAS + 天道推演

> v5.0 新增前沿点。PRISMA系统文献综述的核心难题是"筛选效率"--人工筛选数百篇论文耗时数周。2026年的趋势是用 **ASReview**（AI辅助系统性文献综述）加速筛选，用 **DeepSeek/RAGAS** 做LLM辅助证据合成，并用**天道推演**预判商业模式类型演化。

### ASReview：AI辅助系统性文献综述

ASReview（Utrecht University开发）是AI辅助系统性文献综述的开源工具，用主动学习（Active Learning）算法自动排序论文相关性，比人工快10x。

- **原理**：先用人工标注少量论文（种子集），ASReview训练分类器，自动对剩余论文排序，最相关的排最前面--人工只需读前20%就能覆盖95%的相关论文
- **对比传统PRISMA**：传统PRISMA需读全部标题摘要（100%），ASReview只需读~20%，节省80%时间
- **关键词命中**：ASReview / 主动学习 / 贝叶斯优化

### DeepSeek/RAGAS：LLM辅助文献综述

2026年 DeepSeek-V3/R1 等开源模型在文献综述任务上接近GPT-4水平，成本仅1/10：

- **摘要提取**：用DeepSeek自动从论文全文中提取研究问题/方法/核心发现的结构化摘要
- **相关性判断**：用LLM做论文与综述主题的语义相关性判断（比关键词匹配更精准）
- **证据合成**：用RAGAS（Retrieval Augmented Generation Assessment）评估LLM生成的综述文本质量
- **关键词命中**：DeepSeek / RAGAS / LLM辅助文献综述

### 天道推演 x 商业模式类型演化

用天道推演预判AI商业模式五大类型的演化路径：

- **沙盘分支1**：Agent经济主导（Agent可靠性突破 -> outcome-based pricing成为主流 -> 传统SaaS被Agent替代）
- **沙盘分支2**：AI平台整合（Hugging Face类平台垄断 -> 分发渠道控制力增强 -> 独立AI产品生存空间被压缩）
- **沙盘分支3**：基础设施商品化（开源模型追平闭源 -> API定价持续下降 -> AI基础设施利润率压缩）

每个分支用贝叶斯推断更新概率分布，标注已知盲点。

> 🔗 深入阅读见 [`reading.md`](./reading.md) 的 ASReview / DeepSeek / 天道推演条目。

---

## 与后续 Day 的衔接

- **Day 2**：价值创造机制 + 定价策略--今天的类型学是定价策略分析的基础（不同类型有不同定价模型）
- **模块R4衔接**：本 Day 的 PRISMA 实践是模块R4（研究方法论）的嵌入式训练，为 Capstone 论文的文献综述章做准备

---

## 作业与评估

作业、5分制量表、费曼演练、2分钟话术、复盘自诊表--沿用独立教材 § Day 1 既有设计。本学习材料包不重复，仅新增上机交付物：

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6 个 TODO 全部填好，能跑通）
- [ ] 一段 300 字分析：你的 PRISMA 流程图中，哪个阶段的排除比例最高？为什么？（提示：去重阶段？年份筛选？相关性筛选？）
- [ ] （可选）用 ASReview 对你的纳入文献做主动学习排序，对比 ASReview 排序与人工筛选的差异

---

*本讲义由 v5.0 学习材料包升级生成。理论部分引用独立教材，上机部分用真实库（arxiv + pandas + matplotlib）+ TODO 脚手架。*
*最后更新：2026-07-24*

---

## 学习科学层 (v6.0)

本单元采用**刻意练习 (Ericsson deliberate practice)** - skill_target 为"90分钟内独立完成 PRISMA 系统文献综述并归类到 AI 商业模式五大类型", 3 子技能配 >=3 drills, 每个 drill 含 difficulty/reps_required/feedback_rule + Worked-Faded 三阶段 (完整示范->部分填空->独立解), 连续 2 次失败触发 weak_loop 弱项循环。配 **间隔重复 (spaced retrieval)** - schedule.json 用 FSRS-6 (request_retention=0.9) + SM-2 备份 (EF₀=2.5), 间隔 due=[1,3,8,21,60,180] 天, 覆盖"五大类型/PRISMA四步/剥离AI测试"等核心概念。教学活动遵循 **建构对齐 (Biggs constructive alignment)** - ILO↔TLA↔AT 矩阵 + mastery_threshold (>=80%) + 3 自检问题 (Feed Up/Back/Forward), 见 alignment.md。配 **牛津 tutorial LLM 仿真 (Oxford Socratic)** - tutorial.ipynb 内 persona 禁直接给答案, 用苏格拉底追问 (为什么/反例/若前提变/凭什么/如何) + HBS devil's advocate, 多轮脚手架渐退 (worked->faded->independent), 配 Hattie 4 级 formative feedback ([TASK]/[PROCESS]/[SELF-REG]/[FEED-FORWARD]) + student_model.json + 每天 1 次限频防依赖。交叉练习 (interleaving) 促进迁移 - 五大类型识别与 PRISMA 流程交叉排布 (A1B1C1...B2C2A2...C3A3B3), 提取练习 (retrieval practice) 优于重读 (Butler 2010: 推断题 68% vs 重学 44%)。mastery 阈值与 Worked-Faded 示例见 practice.md 与 alignment.md。

---

## 研究产出与产业链接层 (v7.0)

本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+arXiv链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。研究问题=AI商业模式五类型在2023-2026 arXiv文献中的分布与Agent经济型演化; linked_paper=PRISMA 2020 (BMJ n71); 可复现清单覆盖code/data/seeds/environment/preregistration/FAIR六项; 产业链接锚定OpenAI/Hugging Face/Perplexity/Sierra/Salesforce五家真实企业 + Burberry咨询项目 + CMO决策HBS案例 + a16z/OpenAI Residency实习指针。详见 research.md 与 industry.md。

---

## 学术前沿层 (v9.0)

本单元新增 `frontier.md`：注入 2025-2026 最新学术前沿（N 篇真实 arXiv 论文 + 批判性综述 + delta_to_unit + ≥3 开放研究问题 + 方法论批评）。论文来自 `_frontier_corpus/skill-4-business-model.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证），覆盖前沿课题：AI原生商业模式 × outcome-based pricing。面向博后/教授级读者：批判性综述非罗列，delta_to_unit 显式指出前沿如何更新本单元所教，开放问题为可发表研究方向。详见 `frontier.md`。
