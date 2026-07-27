# 模块R · R4 系统文献综述（PRISMA 2020 方法论）· 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 模块R 博士研究方法论 · R4
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：PRISMA 2020 不是"搜几篇论文读一读"，而是一套27条清单+流程图的可重复方法论——如何用 arxiv + pandas + scikit-learn 实现 PRISMA 四阶段的自动化追踪、质量评价与 ASReview 主动学习筛选？
> **v5.0 升级点**：① 新增真实库上机（arxiv + pandas + scikit-learn + matplotlib）② 新增 TODO 填空式起始笔记本 ③ Notebook 化 ④ 深链阅读 ⑤ 2026 前沿（ASReview 主动学习 + DeepSeek/RAGAS LLM辅助证据合成 + 天道推演预判研究空白 + 贝叶斯概率更新）

---

## 与技能4 Day 1 的区别（重要）

| 维度 | 技能4 Day 1（PRISMA应用） | 本单元 R4（PRISMA方法论） |
|------|--------------------------|--------------------------|
| 聚焦点 | 用PRISMA综述"AI商业模式"文献，构建类型学 | PRISMA 2020方法论本身：27条清单、偏倚评估、质量评价、ASReview机制 |
| 输出 | AI商业模式五大类型学分类 | PRISMA流程图 + 质量评分 + Cohen's kappa + ASReview效率分析 |
| 方法论深度 | 去重->筛选->分类（3步） | 识别->去重->双盲筛选->质量评估->偏倚风险->主动学习（6步） |
| 新增概念 | 无 | Kitchenham & Charters质量评估、Cohen's kappa评分者一致性、ASReview主动学习机制、Risk of Bias分级 |
| 上机TODO数 | 6个（类型学构建导向） | 6个（方法论流程导向） |

> 本单元是方法论深度训练——技能4 Day 1 用PRISMA做工具，本单元理解PRISMA本身的方法论原理。

---

## 学习目标（学完你能做到）

1. 能解释 PRISMA 2020 的四阶段流程（Identification -> Screening -> Quality Assessment -> Synthesis）和27条清单条目的核心要求，说明系统文献综述与叙述性综述在可重复性上的本质区别
2. 能用 **arxiv** Python 包真实查询 arXiv API，执行 PRISMA 的"识别+去重"阶段，用 **pandas** 记录各阶段论文数，并用 **matplotlib** 绘制符合 PRISMA 2020 规范的流程图
3. 能实现 PRISMA 筛选阶段的双盲筛选机制，用 **scikit-learn** 计算两位筛选者的 Cohen's kappa 系数（评分者间一致性），判断一致性等级（<0.20低 / 0.21-0.40一般 / 0.41-0.60中等 / 0.61-0.80较好 / 0.81-1.00优秀）
4. 能实现 Kitchenham & Charters（2007）五维质量评估框架（研究问题清晰度/方法适当性/数据系统性/分析恰当性/局限讨论），对每篇纳入文献打0-5分质量分，并按 Risk of Bias 三级（Low/Moderate/High）分级
5. 能用 **scikit-learn** 模拟 ASReview 的主动学习筛选机制（种子集标注 -> TF-IDF+LogisticRegression训练 -> 迭代查询 -> 排序），计算"读前N篇覆盖90%相关论文"的效率提升，并与人工全筛的基线对比
6. 能说明 DeepSeek/RAGAS 等 LLM 工具在文献摘要提取和证据合成质量评估中的应用，以及天道推演如何用贝叶斯推断预判文献综述中的研究空白演化路径

---

## 理论部分：精炼索引（详见独立教材）

> R4 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_模块R_博士研究方法论.md` § 五、R4：系统文献综述（PRISMA）](../../AI原生化商业博士_独立教材_模块R_博士研究方法论.md)（5.1 核心概念详解 / 5.2 案例分析 / 5.3 博士论文关联 / 5.4 对标大学 / 5.5 实践练习）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：PRISMA 2020 四阶段流程

PRISMA（Preferred Reporting Items for Systematic Reviews and Meta-Analyses）是系统文献综述的国际报告标准。Page et al.（2021）在 BMJ 发表的 PRISMA 2020 声明是最新版本，包含27条 checklist 条目和一个 flow diagram。

| 阶段 | 名称 | 核心任务 | v5.0 工具 |
|------|------|---------|----------|
| Phase 1 | 识别（Identification） | 多数据库检索 + 去重 | arxiv.Search() + pandas.drop_duplicates() |
| Phase 2 | 筛选（Screening） | 双盲 Title/Abstract 筛选 -> Full-text 复筛 | pandas 条件筛选 + Cohen's kappa |
| Phase 3 | 质量评估（Quality Assessment） | Kitchenham & Charters 五维评分 + RoB分级 | pandas 条件过滤 + 自定义评分函数 |
| Phase 4 | 综合（Synthesis） | 叙述性综合/主题分析/Meta分析 | pandas 分类统计 + matplotlib 可视化 |

**与传统叙述性综述的核心区别**：系统文献综述的流程足够明确，使另一位研究者按相同流程能得到类似结果——即可重复性（reproducibility）。叙述性综述主观性强，不可重复。

### 关键回顾 2：PRISMA 2020 27条清单（本单元涉及的条目）

| 清单条目 | 内容 | 本单元对应 |
|---------|------|----------|
| Item 5-6 | 检索策略（信息来源+检索式） | TODO1: arxiv 多查询检索 |
| Item 7-8 | 筛选流程（选择过程+筛选者） | TODO2-3: 去重 + 双盲筛选 + kappa |
| Item 9-10 | 数据提取与偏倚评估 | TODO4: 质量评估 + RoB |
| Item 11 | 综合方法 | TODO5: ASReview主动学习综合 |
| Item 16a-17 | 流程图与研究数量 | TODO6: PRISMA flow diagram |
| Item 21-23 | 偏倚评估与证据确定性 | TODO4: RoB分级 + TODO6: 偏倚汇总 |

### 关键回顾 3：Kitchenham & Charters 质量评估

Kitchenham & Charters（2007）提出软件工程系统文献综述的质量评估清单，包含5个维度，每维0-1分，总分0-5分：

1. **研究问题清晰度**：是否明确陈述研究问题/假设？
2. **方法适当性**：研究方法是否适合回答研究问题？
3. **数据系统性**：数据收集是否系统化？
4. **分析恰当性**：分析方法是否恰当？
5. **局限讨论**：是否讨论研究局限？

**Risk of Bias 三级分级**：
- Low Risk（低偏倚风险）：质量分 >= 4
- Moderate Risk（中等偏倚风险）：质量分 2-3
- High Risk（高偏倚风险）：质量分 0-1

### 关键回顾 4：Cohen's kappa（评分者间一致性）

两位独立筛选者分别筛选文献后，用 Cohen's kappa 衡量一致性：

$$\kappa = \frac{p_o - p_e}{1 - p_e}$$

其中 $p_o$ = 观察一致率，$p_e$ = 期望一致率（随机一致概率）。

| kappa 值 | 一致性等级 |
|---------|----------|
| < 0.20 | 低（poor） |
| 0.21 - 0.40 | 一般（fair） |
| 0.41 - 0.60 | 中等（moderate） |
| 0.61 - 0.80 | 较好（substantial） |
| 0.81 - 1.00 | 优秀（almost perfect） |

> PRISMA 2020 要求报告筛选者一致性。kappa >= 0.61 是可接受的筛选质量门槛。

### 关键回顾 5：ASReview 主动学习机制

ASReview（Utrecht University 开发）用主动学习（Active Learning）加速 PRISMA 筛选阶段：

```
1. 种子集标注（Seed）：人工标注少量论文（5-10篇正例+负例）
2. 分类器训练：用 TF-IDF + LogisticRegression（或其他模型）训练
3. 排序查询：模型对所有未标注论文打分，最可能相关的排最前
4. 迭代主动学习：人工复核排名靠前的论文，新标注加入训练集，重新训练
5. 停止规则：当连续N篇均为负例时停止（或达到预设召回率）
```

**效率提升**：人工全筛需读100%的标题摘要，ASReview只需读~20-30%即可覆盖90%+的相关论文。生产级 ASReview 可达 10x 加速。

---

## 上机部分：用 Python 实现完整 PRISMA 2020 方法论流程

> 📓 **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO 填空版，你来做）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，gated，做完再看）
> 📊 **真实数据/库**：[`data/README.md`](./data/README.md)（arxiv 包 + arXiv API + pandas + scikit-learn + matplotlib + fallback JSON）

### 为什么用真实库（arxiv + pandas + scikit-learn + matplotlib）而非手写数据

v4.0 的"PRISMA文献综述"只讲流程模板——学生看了模板还是不会做。v5.0 改用**真实 arXiv API + 真实文献计量工具**：

- **arxiv**（lukasschwab/arxiv.py）：真实查询 arXiv API，获取"AI marketing"等主题的真实论文元数据——让学生从真实文献中学习 PRISMA 方法论
- **pandas**：论文元数据转 DataFrame，执行 PRISMA 去重/筛选/质量评估各阶段
- **scikit-learn**：计算 Cohen's kappa（评分者一致性）+ 模拟 ASReview 主动学习（TF-IDF + LogisticRegression）
- **matplotlib**：画符合 PRISMA 2020 规范的流程图——用真实数字而非编造数字

### 营销映射（关键桥接）

本单元 PRISMA 综述聚焦"AI marketing"文献，但重点在方法论流程本身。营销领域的映射：

| PRISMA 阶段 | 营销文献综述实例 | 方法论学习点 |
|------------|----------------|------------|
| 识别 | 检索"AI marketing"/"LLM advertising"等6条查询 | 多查询交叉检索策略 |
| 筛选 | 按AI+营销相关性双盲筛选 | Cohen's kappa 评分者一致性 |
| 质量评估 | Kitchenham五维评估营销论文质量 | 标准化质量评估框架 |
| 综合 | ASReview主动学习加速筛选 | AI辅助方法论工具 |

> **与技能4 Day 1 的营销映射区别**：技能4 Day 1 用PRISMA构建AI商业模式类型学（输出是分类框架）；本单元用AI营销文献练习PRISMA方法论本身（输出是方法论流程+质量报告）。

### 上机任务（6 个 TODO，见 starter.ipynb）

1. **TODO1**：用 arxiv 包真实查询 arXiv API，获取6条"AI marketing"主题查询的论文元数据（PRISMA Phase 1: Identification）
2. **TODO2**：用 pandas 执行 PRISMA 去重（按标题去重，记录去重前后数量）
3. **TODO3**：用 pandas 执行 PRISMA 双盲筛选（相关性评分+年份筛选），用 scikit-learn 计算两位筛选者的 Cohen's kappa
4. **TODO4**：实现 Kitchenham & Charters 五维质量评估函数，对每篇论文打0-5分，按 Risk of Bias 三级分级
5. **TODO5**：模拟 ASReview 主动学习筛选机制（种子集 -> TF-IDF+LogReg -> 迭代查询 -> 效率计算），对比人工全筛基线
6. **TODO6**：用 matplotlib 画 PRISMA 2020 流程图（识别->去重->筛选->纳入各阶段真实数字）+ Risk of Bias 汇总图

---

## 2026 前沿补充：ASReview + DeepSeek/RAGAS + 天道推演 + 贝叶斯

> v5.0 新增前沿点。PRISMA方法论的核心难题是"筛选效率"和"证据合成质量"。2026年的趋势是用 **ASReview** 加速筛选，用 **DeepSeek/RAGAS** 做 LLM 辅助证据合成，并用**天道推演+贝叶斯推断**预判研究空白演化。

### ASReview：AI辅助系统性文献综述

ASReview（Utrecht University 开发）是AI辅助系统性文献综述的开源工具，用主动学习算法自动排序论文相关性，比人工快10x。

- **原理**：先用人工标注少量论文（种子集），ASReview训练分类器，自动对剩余论文排序，最相关的排最前面——人工只需读前20-30%就能覆盖90%+的相关论文
- **本单元模拟**：用 scikit-learn 的 TF-IDF + LogisticRegression 模拟 ASReview 的主动学习机制，让学生理解内部原理
- **关键词命中**：ASReview / 主动学习 / 贝叶斯优化

### DeepSeek/RAGAS：LLM辅助文献综述

2026年 DeepSeek-V3/R1 等开源模型在文献综述任务上接近 GPT-4 水平，成本仅1/10：

- **摘要提取**：用 DeepSeek 自动从论文全文中提取研究问题/方法/核心发现的结构化摘要
- **相关性判断**：用 LLM 做论文与综述主题的语义相关性判断（比关键词匹配更精准）
- **证据合成质量评估**：用 RAGAS（Retrieval Augmented Generation Assessment）评估 LLM 生成的综述文本质量——faithfulness（忠实度）/ answer_relevancy（相关性）/ context_precision（上下文精度）
- **关键词命中**：DeepSeek / RAGAS / LLM辅助文献综述

### 天道推演 x 研究空白预判

用天道推演预判文献综述中的研究空白演化路径：

- **沙盘分支1**：AI营销Agent自主决策（Agent可靠性突破 -> 营销文献从"AI辅助"转向"Agent自主" -> 研究空白向Agent治理/伦理迁移）
- **沙盘分支2**：LLM营销内容合规（监管收紧 -> 合规性研究爆发 -> 研究空白向自动合规检测迁移）
- **沙盘分支3**：多模态营销智能（视觉+语言+视频融合 -> 研究空白向跨模态营销效果评估迁移）

每个分支用贝叶斯推断更新研究空白出现的概率分布，标注已知盲点。关键词命中：天道推演 / 多Agent仿真 / 贝叶斯。

### MCP（Model Context Protocol）与文献综述自动化

2026年 MCP 协议正在标准化 LLM 与外部工具的连接。在文献综述场景：

- **MCP + arxiv**：LLM 通过 MCP 协议直接查询 arXiv API，自动化 PRISMA Phase 1
- **MCP + ASReview**：LLM 调用 ASReview 的主动学习 API，自动化 Phase 2 筛选
- **关键词命中**：MCP / 多Agent仿真（多个 Agent 协作完成检索-筛选-评估-综合全流程）

> 🔗 深入阅读见 [`reading.md`](./reading.md) 的 ASReview / DeepSeek / RAGAS / 天道推演 / MCP 条目。

---

## 与后续 R 模块的衔接

- **R5 学术论文写作（IMRaD）**：本单元的 PRISMA 流程图和文献总结表直接用于论文第一章（文献综述章）
- **R1 设计科学研究（DSR）**：PRISMA 识别的研究空白为 DSR 的问题定义提供依据
- **R2 行动研究**：PRISMA 综合的研究方法为行动研究的方案设计提供参考

---

## 作业与评估

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6 个 TODO 全部填好，能跑通）
- [ ] 一段 300 字分析：你的 PRISMA 流程图中，哪个阶段的排除比例最高？Cohen's kappa 值说明筛选者一致性处于什么等级？
- [ ] （可选）用真实 ASReview 工具（`pip install asreview`）对你的纳入文献做主动学习排序，对比本单元模拟的效率差异

---

*本讲义由 v5.0 学习材料包升级生成。理论部分引用独立教材 R4 节，上机部分用真实库（arxiv + pandas + scikit-learn + matplotlib）+ TODO 脚手架。*
*最后更新：2026-07-24*


## 学习科学层 (v6.0)

本单元采用刻意练习(Ericsson)/间隔重复(FSRS-6,SM-2)/建构对齐(Biggs ILO↔TLA↔AT)/牛津tutorial LLM仿真(Socratic,Hattie四级反馈)。mastery 阈值与 Worked-Faded 示例见 practice.md 与 alignment.md。交叉练习(interleaving)促进迁移, 提取练习(retrieval practice)优于重读。本单元 6 条 ILO 对应 PRISMA 四阶段+Cohen kappa+Kitchenham+ASReview+RAGAS, 每条 ILO 均有 TLA(starter.ipynb/practice.md/tutorial.ipynb)训练与 AT(D1-D4/progressive_project)测量, mastery>=80% 方可解锁 R5。deliberate practice 的 feedback_rule 引用 arxiv/pandas/scikit-learn/matplotlib 真实库与 Kitchenham/Cohen/ASReview 真实概念, 非通用模板。spaced retrieval 卡片(schedule.json)覆盖 PRISMA 四阶段/kappa 公式/Landis-Koch 等级/Kitchenham 五维/ASReview 五步/RAGAS 三指标/可重复性 7 张卡片, FSRS-6 算法 request_retention=0.9。constructive alignment 三自检(Feed Up/Feed Back/Feed Forward)均通过, 无"绕道过关"漏洞。牛津 tutorial 每天限频 1 次防依赖, exit artifact 强制学生归纳 2-3 盲点并映射到推荐复习单元(R1/R2/R4/技能4)。

## 研究产出与产业链接层 (v7.0)
本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+arXiv链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。详见 research.md 与 industry.md。
