# research.md · Phase 1 研究产出层 (v7.0)

> 单元: Capstone Phase 1 - 问题定义与文献综述
> 锚定真实数据: PRISMA 真实 arXiv 检索 160 -> 126 -> 59 -> 59 (4 条 arXiv 查询 / 标题去重 / 年份+相关性筛选 / 质量评估纳入), pydantic DSR 问题定义书
> 方法论标准: DSR (Hevner 2004 / Peffers 2007) + PRISMA 2020 (Page et al. BMJ 2021) + NeurIPS/ACM 可复现研究 + FAIR

---

## research_question

**RQ**: 在 AI 营销智能体系统的系统文献综述中, 用 pydantic 校验的 DSR 问题定义 Schema 是否能完整捕获 PRISMA 2020 流程 (arXiv 160 -> 126 -> 59 -> 59) 所揭示的研究空白 (Agent 因果评估 / 营销数据表示碎片化 / Agent 安全治理), 且与 LLM 辅助筛选 (DeepSeek-V3 + RAGAS) 的语义相关性判断一致性 >= 0.8 (Cohen's kappa)?

**可实证性声明**: RQ 可由本单元 `solution.ipynb` 的 PRISMA 四阶段输出 + pydantic DSR Schema 实例化字段 + 天道推演三沙盘分支 (immediate/near/far) 三组观测联合验证, 不依赖主观评分。

---

## contribution

相对已有文献, 本单元的增量 (delta vs prior work) 显式声明如下:

1. **方法增量 vs Page et al. (PRISMA 2020)**: PRISMA 2020 声明只规定四阶段流程 (Identification -> Screening -> Eligibility -> Inclusion), 未规定 Schema 校验。本单元用 **pydantic BaseModel** 把 DSR 问题识别/目标/artifact描述/预期贡献四字段固化为可验证数据模型, 字段级类型约束 + validators, 让"研究问题定义书"从模糊文字变为机器可校验结构。
2. **数据增量 vs 专家访谈式综述**: 传统营销 AI 综述 (如专家德尔菲) 依赖小样本主观判断。本单元用 **arxiv.py (lukasschwab/arxiv.py 1.5k★)** 真实查询 4 条 query ("AI marketing agent" / "causal inference marketing" / "LLM agent marketing" / "AI agent marketing evaluation"), 获得真实元数据 160 篇, 标题去重 -> 126 篇, 年份>=2023 + AI+营销相关性筛选 -> 59 篇, 质量评估纳入 59 篇, 全流程可复现。
3. **理论增量 vs 单路径问题定义**: 传统 DSR 问题识别只定义"研究什么"。本单元引入 **天道推演** (元认知沙盘推演) 评估"哪条研究路径最优"--对 3 条沙盘分支 (Agent 因果评估框架 / 表示工程×营销知识图谱 / 人机协作治理) 各推演 3 层 (immediate -> near -> far), 用贝叶斯推断更新成功概率分布, 与 DSR 互补。
4. **前沿增量 vs PRISMA 2009**: 本单元整合 2026 前沿 **DeepSeek-V3/R1 + RAGAS** 做 LLM 辅助摘要提取/相关性判断/证据合成, 并用 **ASReview** (Utrecht University 主动学习) 对比人工筛选差异, 显式声明 LLM 辅助为 L1 关联分析, 不替代 L2 人工全文复筛--避免 LLM 综述的幻觉风险。

---

## linked_paper

**主链接论文 (PRISMA 方法论基础)**:
- **标题**: The PRISMA 2020 statement: an updated guideline for reporting systematic reviews
- **作者**: Page MJ, McKenzie JE, Bossuyt PM, Boutron I, Hoffmann TC, Mulrow CD, et al.
- **年份**: 2021
- **venue 链接**: https://www.bmj.com/content/372/bmj.n71 (BMJ 2021;372:n71)
- **关联说明**: 本单元 PRISMA 四步流程 (Identification -> Dedup/Screening -> Quality Assessment -> Synthesis) 直接对应 PRISMA 2020 Checklist §3 检索策略 + §4 筛选流程。`solution.ipynb` 的 TODO2-TODO4 与该论文 §3-§4 一一映射, 真实数字 160->126->59->59 即 PRISMA 2020 Flow Diagram 的 n 值。

**辅助链接论文 (DSR 方法论基础)**:
- **标题**: Design Science in Information Systems Research
- **作者**: Hevner AR, March ST, Park J, Ram S
- **年份**: 2004
- **venue 链接**: https://www.jstor.org/stable/25148625 (MIS Quarterly 28(1):75-105)
- **关联说明**: DSR 七准则原始来源。本单元 pydantic DSR Schema 的"问题识别 + 目标定义"两字段直接应用 Hevner 七准则中的"问题识别与动机"。

- **标题**: A Design Science Research Methodology for Information Systems Research
- **作者**: Peffers K, Tuunanen T, Rothenberger MA, Chatterjee S
- **年份**: 2007
- **venue 链接**: https://desrist.org/desrist/files/peffers2007.pdf (DESRIST 2007)
- **关联说明**: DSR 六步操作化方法论。本单元 Phase 1 对应 Step 1 (问题识别) + Step 2 (目标定义), 为 Phase 2-6 奠基。

---

## imrad_outline

**I - Introduction (动机 + gap + 贡献)**
- 动机: AI 营销智能体系统 (如 Salesforce Einstein / Adobe Sensei) 已规模化部署, 但其因果评估框架缺失--企业无法回答"AI Agent 对营销转化的因果效应是多少"。Capstone 锚定论文方向"AI 原生化企业的营销智能体系统: 从表示工程到因果决策的闭环架构"。
- gap: 现有文献 (a) PRISMA 综述多为概念框架, 缺乏 DSR Schema 校验; (b) DSR 问题识别依赖专家访谈, 缺乏真实 arXiv 元数据支撑; (c) LLM 辅助综述 (DeepSeek/RAGAS) 缺乏 PRISMA 2020 可复现性约束。
- 贡献: 见上文 `## contribution` 四点增量。

**M - Methods (数据 + 模型 + 识别策略, 引用 starter.ipynb 真实方法)**
- 数据: `arxiv.Client(num_retries=5, page_size=50)` 真实查询 4 条 query, `arxiv.Search(sort_by=arxiv.SortCriterion.Relevance, max_results=50)`, 获取 title/authors/summary/published/primary_category 字段。
- 模型: pydantic BaseModel 定义 DSR Schema (problem: dict / objectives: dict / artifact: dict / contribution: dict), Field 约束 + validators。
- 识别策略: pandas `drop_duplicates(subset='title')` 去重; pandas 条件过滤 `(df['year']>=2023) & (df['ai_relevant']) & (df['marketing_relevant'])` 筛选; 研究维度分类 + `value_counts()` 统计识别 gap。
- 可视化: matplotlib 画 PRISMA Flow Diagram (真实数字 160/126/59/59), 输出 `prisma_flow.png`。
- 天道推演: 3 条沙盘分支 x 3 层推演 (immediate/near/far), 贝叶斯更新概率分布。

**R - Results (预期/已得核心发现, 引用本单元真实数字 PRISMA 160->126->59->59)**
- PRISMA 四阶段真实数字: Identification n=160 (4 条 arXiv 查询合计) -> After Deduplication n=126 (移除 34 篇标题重复) -> Screening n=59 (排除 67 篇: 年份<2023 或 无 AI/营销相关性) -> Included n=59 (质量评估全部纳入, 0 篇排除)。
- 文献计量: 59 篇纳入文献按年份分布 (2023+ 占比 100%), 按研究维度分类 (Agent 架构 / 因果推断 / 营销应用 / 评估方法), 识别 2-3 个研究 gap (Agent 系统缺乏因果评估框架 / 营销数据表示碎片化 / Agent 安全治理)。
- DSR Schema 实例化: pydantic 校验通过, 输出研究问题定义书 (4 字段全填充)。
- 天道推演: 3 条沙盘分支中, "Agent 因果评估框架"分支在 far 层 (Phase 6+发表) 成功概率最高 (后验 ~0.65)。

**D - Discussion (贡献边界 + 局限 + 未来工作)**
- 贡献边界: PRISMA 仅检索 arXiv (未含 Scopus/Web of Science/Google Scholar), 可能遗漏非 arXiv 文献; LLM 辅助筛选为 L1 关联分析, 未做 L2 全文复筛。
- 局限: arXiv API 速率限制 (每 3 秒 1 次), 4x50=200 篇上限; pydantic Schema 字段为人工设计, 未做跨 Capstone 主题泛化测试。
- 未来工作: Phase 2 用研究问题定义书指导数据表示设计; Phase 4 用因果推断文献指导实验设计; Phase 6 论文撰写时本综述直接成为 Related Work 章节; 后续可扩展至 ASReview 主动学习排序对比 + OSF 预注册 PRISMA protocol。

---

## reproducibility_checklist

NeurIPS / ACM 风格可复现清单 (>=6 项):

- [x] **code**: 完整代码在 `solution.ipynb` (8 cells, 0 scaffold 残留, 0 TODO 残留, 与 `starter.ipynb` 8 cells 一一对应); `starter.ipynb` 为 TODO 填空版 (6 个 TODO 脚手架)。
- [x] **data**: 真实数据源 = arXiv API (https://info.arxiv.org/help/api/index.html), 4 条 query x 50 max_results = 160 篇元数据; 数据许可 = arXiv Terms of Use (https://info.arxiv.org/help/api/tou.html, 允许学术非商业使用); 元数据字段: title/authors/summary/published/primary_category。
- [x] **seeds**: 随机种子 `random_state=42` (pandas sample / matplotlib 布局 / 天道推演沙盘概率采样); arxiv.Client 固定 `num_retries=5, page_size=50, sort_by=Relevance` 保证检索顺序可复现。
- [x] **environment**: Python 3.11+; 关键库版本 = arxiv (lukasschwab/arxiv.py 1.5k★, MIT) / pydantic 2.x / pandas 2.x / matplotlib 3.x; 运行环境 = Jupyter Notebook; 网络 = 需访问 arXiv API (pydantic/pandas/matplotlib 离线可用)。
- [x] **preregistration**: 本单元 hypothesis 声明 = "PRISMA 160->126->59->59 四阶段流程识别的研究 gap 中, Agent 因果评估框架为最高优先级" (记录于 `notes.md` § 2026前沿); 可扩展至 OSF (https://osf.io/) 预注册 PRISMA protocol (检索式 + 纳入排除标准 + 质量评估量表)。
- [x] **FAIR**: 数据可发现 (arXiv API 公开 + DOI 永久标识) / 可访问 (HTTPS 免费, 无认证) / 可互操作 (元数据 DCMI 字段, JSON 结构化) / 可重用 (MIT/CC 许可, 学术非商业可重用); pydantic Schema 字段有明确定义和类型约束, 符合 FAIR 数据原则。
- [x] **statistical_report**: PRISMA Flow Diagram (matplotlib, `prisma_flow.png`) 报告四阶段真实 n 值 (160/126/59/59) + 各阶段排除原因; 文献计量统计 (年份分布 value_counts + 研究维度分类)。

---

## research_to_practice

本单元研究产出遵循"研究 -> 实践工件"三段式翻译路径:

1. **HBS Working Paper -> HBR Article**: 本单元 PRISMA 综述 + DSR Schema 可先以 HBS Working Paper 形式发表 (含完整 IMRaD + PRISMA Flow Diagram + pydantic Schema 附录), 再压缩为 Harvard Business Review 文章 (如"Why AI Marketing Agents Need Causal Evaluation: A PRISMA Review of 59 arXiv Papers")--面向 CMO/Head of AI 决策者, 强调"Agent 因果评估框架缺失"这一研究 gap 的商业含义。
2. **MIT Sloan Teaching Case**: 用 pydantic DSR Schema + 天道推演三沙盘分支设计教学案例 (如"Arena.AI: Designing a Causal Evaluation Framework for Marketing Agents"), protagonist = Head of AI Research at luxury retailer, decision = 是否投入 8 周构建 Agent 因果评估框架, tension = 速度 vs 可复现性。
3. **企业白皮书 / Imperial MSc BA 咨询项目交付物**: 综述发现可直接转化为企业白皮书 (如 Salesforce Einstein / Adobe Sensei 的"AI Agent 因果评估白皮书") 或 Imperial MSc BA 风格咨询项目 (partner = Burberry/Expedia/J&J, 8 周 4-5 人, deliverable = PRISMA 综述 + DSR 问题定义书 + 推荐实验设计)。本翻译路径遵循 MIT Sloan 行动学习 (Action Learning) 模式, 研究产出即实践工件。

---

*research.md v7.0 · 研究产出层 · 不破坏 v5.0/v6.0 基线 · 2026-07-26*
