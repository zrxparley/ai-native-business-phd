# 技能0 · Day 6：研究方法论入门 · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 技能0 AI商业分析基础（预科层）· Day 6
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：学术研究不是"更难的工程"，而是"创造可传播的新知识"--如何用 Python 查询真实 arXiv 论文、做文献计量、构建作者合作网络，并理解可复现研究与预注册？
> **v5.0 升级点**：① 真实库上机（arxiv + pandas + networkx + matplotlib，替代纯手写笔记）② TODO 填空式起始笔记本 ③ Notebook 化 ④ 深链阅读 ⑤ 2026 前沿（可复现研究 / OSF 预注册 / ASReview AI辅助文献综述 / LLM 辅助研究连接 DeepSeek 与 Trajectory）

---

## 学习目标（学完你能做到）

1. 能解释学术研究与工程实践的根本区别（**创造可传播的新知识** vs **解决具体问题**），并说明博士论文七部分结构与 IMRaD 格式为什么是科学交流效率的最优解（回答读者最关心的四个问题）
2. 能用 **arxiv** Python 包查询真实 arXiv API，获取 "marketing analytics" / "causal inference marketing" / "LLM marketing" 等主题的真实论文元数据（标题/作者/发表日期/摘要），理解文献综述是发现"研究空白"的系统化方法
3. 能用 **pandas** 把 arXiv 返回的论文元数据转为 DataFrame，完成文献计量统计（按年份的论文增长趋势、按作者的高产作者排名、按主题分类），识别营销 AI 领域的研究热度演化
4. 能用 **networkx** 构建作者合作网络（节点=作者，边=合作关系）和关键词共现网络（节点=关键词，边=共现次数），计算度中心性识别核心作者，用社区检测发现新兴研究方向
5. 能用 **matplotlib** 可视化论文增长趋势折线图与合作网络图，并解释可复现研究（Reproducible Research）的三大支柱--OSF 预注册、FAIR 原则、环境锁定（requirements.txt/Dockerfile）--为什么是 2026 年学术研究的基本要求

---

## 理论部分：精炼索引（详见独立教材）

> Day 6 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_技能0_AI商业分析基础.md` § Day 6](../../AI原生化商业博士_独立教材_技能0_AI商业分析基础.md)（1359-1443 行，已包含 学术研究vs工程实践的根本区别/博士论文七部分结构/三种研究范式(实证/解释/实用主义)/IMRaD格式/与模块R的连接）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：学术研究 vs 工程实践

学术研究和工程实践的核心区别不在于"难不难"，而在于"目标不同"：

| 维度 | 工程实践 | 学术研究 |
|------|---------|---------|
| 目标 | 解决具体问题 | 创造可传播的新知识 |
| 交付物 | 可运行的系统/产品 | 论文/研究报告 |
| 评价标准 | 是否解决了问题 | 是否贡献了新知识 |
| 知识属性 | 隐性的、局部的 | 显性的、可复用的 |

**核心洞察**：你的 AI 营销工程实践可以转化为学术贡献--这就是模块R1（设计科学研究）要教你的。今天先用 Python 查询真实论文，感受"学术共同体在对话什么"。

### 关键回顾 2：博士论文七部分结构

一篇典型的商业/信息系统领域博士论文包含：绪论 -> 文献综述 -> 理论框架 -> 研究方法 -> 研究结果 -> 讨论 -> 结论。文献综述（Literature Review）是第二章，目标是发现"前人做了什么，还有什么没做（研究空白）"。今天的上机就是用 arxiv 包做一次**微型文献综述**。

### 关键回顾 3：三种研究范式

| 范式 | 本体论 | 对应方法 | 营销 AI 场景 |
|------|--------|---------|------------|
| 实证主义（Positivism） | 真实客观可测量 | 定量：A/B测试、统计 | 验证 AI 营销系统转化率提升 |
| 解释主义（Interpretivism） | 真实社会建构、主观 | 定性：访谈、案例 | 理解 AI 如何改变营销决策 |
| 实用主义（Pragmatism） | 真实多元 | 混合方法 | 既测效果又理解决策过程 |

### 关键回顾 4：IMRaD 格式

IMRaD（Introduction, Methods, Results, Discussion）是实证研究论文的标准结构。| 部分 | 核心问题 | 写作要点 |
|------|---------|---------|
| Introduction | 为什么做？ | 领域背景 -> 具体问题 -> 研究空白 -> 贡献 |
| Methods | 怎么做？ | 让别人能复现：数据来源、样本、变量、分析方法 |
| Results | 发现什么？ | 用图表说话，先描述再解释 |
| Discussion | 意味什么？ | 与前人对比、理论实践启示、局限、未来方向 |

> ⚠️ 后续技能5 Day 6 会详细训练 IMRaD 写作。本 Day 只需建立基本认知，并用 Python 感受"文献综述"是怎么做的。

---

## 上机部分：用真实库做营销 AI 领域文献计量

> 📓 **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO 填空版，你来做）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，gated，做完再看）
> 📊 **真实数据/库**：[`data/README.md`](./data/README.md)（arxiv + pandas + networkx + matplotlib + arXiv API 真实论文元数据）

### 为什么用真实库（arxiv + networkx）而非手写笔记

v4.0 的"文献综述"只是讲解怎么做笔记--学生看了还是不会做。v5.0 改用**真实 API + 真实网络分析库**：

- **arxiv**（lukasschwab/arxiv.py，1.5k★，MIT License）：`pip install arxiv` 后用 `arxiv.Search(query="marketing analytics")` 查询真实 arXiv API，返回真实论文元数据（标题/作者/发表日期/摘要）--做文献综述的第一步就是系统检索相关文献
- **pandas**：论文元数据转 DataFrame，做按年份/作者/主题的文献计量统计
- **networkx**（networkx/networkx，14k+ star，BSD-3-Clause）：构建作者合作网络与关键词共现网络，计算度中心性、社区检测--这是文献计量学（Bibliometrics）的核心方法
- **matplotlib**：论文增长趋势折线图、合作网络可视化

> **营销映射**：查询 "marketing analytics" / "causal inference marketing" / "LLM marketing" 等主题，分析该领域论文增长趋势、高产作者、关键词共现--这正是企业在进入一个新营销技术领域前应该做的"学术尽职调查"。

### 营销映射（关键桥接）

本 Day 把"研究方法论"桥接到 AI + 企业营销：

| 研究方法论概念 | 营销场景映射 | 真实库实现 |
|-------------|------------|-----------|
| 文献综述 | 营销 AI 领域"学术尽职调查" | arxiv 查询真实论文 |
| 文献计量 | 论文增长趋势=技术成熟度信号 | pandas 按年份统计 |
| 作者合作网络 | 识别领域核心研究团队 | networkx 合作网络 |
| 关键词共现 | 发现新兴营销技术方向 | networkx 共现网络 |
| 可复现研究 | 营销 A/B 测试预注册 | OSF / FAIR 原则 |
| IMRaD | 营销研究报告写作框架 | 理论认知 |

### 上机任务（6 个 TODO，见 starter.ipynb）

1. **TODO1**：用 arxiv 包查询 arXiv API，获取 "marketing analytics" 主题的真实论文元数据（标题/作者/发表日期/摘要），处理网络异常的 fallback
2. **TODO2**：用 pandas 将论文元数据转为 DataFrame，按年份统计论文增长趋势
3. **TODO3**：用 pandas 统计高产作者排名、按主题（query）分类论文数
4. **TODO4**：用 networkx 构建作者合作网络，计算度中心性，识别核心作者
5. **TODO5**：用 networkx 构建关键词共现网络，识别新兴研究方向
6. **TODO6**：用 matplotlib 可视化论文增长趋势折线图与合作网络图

---

## 2026 前沿补充：可复现研究 + OSF 预注册 + ASReview + LLM 辅助研究

> v5.0 新增前沿点。研究方法论在 2026 年的核心趋势是"可复现性危机"催生的三大运动：① 预注册与 Registered Reports ② FAIR 数据原则 ③ AI 辅助文献综述。本 Day 命中前沿关键词：可复现研究、OSF、preregistration、ASReview、DeepSeek、Trajectory。

### 可复现研究（Reproducible Research）的三大支柱

2026 年学术界正经历"可复现性危机"（Replication Crisis）--心理学、医学、机器学习领域大量已发表研究无法被独立复现。应对这一危机的三大支柱：

- **OSF 预注册**（Open Science Framework，https://osf.io）：在数据收集**前**公开注册研究假设与分析计划，对抗 p-hacking（反复尝试直到 p<0.05）与发表偏倚（只发表阳性结果）。营销 A/B 测试同样应该预注册--先声明"我预期实验组转化率提升 10%"，再跑实验，而非跑完再编故事。
- **Registered Reports**：一种期刊审稿模式--在数据收集前先审研究方法（Stage 1），方法通过后无论结果如何都承诺发表（Stage 2）。这从根本上消除了"只发阳性结果"的偏倚。
- **环境锁定**：`requirements.txt` 锁定依赖版本、`Dockerfile` 锁定运行环境、`random_state=42` 固定随机种子--确保任何人都能复现你的分析。今天的 solution.ipynb 就用固定随机种子保证可复现。

### FAIR 原则：数据与代码的治理标准

FAIR 原则要求研究数据和代码是 **F**indable（可发现）、**A**ccessible（可访问）、**I**nteroperable（可互操作）、**R**eusable（可复用）。这与企业数据治理高度同构：

- **Findable**：arXiv 给每篇论文分配唯一 DOI/arXiv ID--企业数据资产也应该有唯一标识（数据目录/血缘）
- **Accessible**：arXiv API 公开可访问--企业内部数据应该有清晰的访问权限协议
- **Interoperable**：论文元数据用标准 JSON 格式--企业数据应该用 Apache Arrow 等标准格式
- **Reusable**：论文带许可证（CC-BY/MIT）--企业数据应该有清晰的使用条款

### ASReview：AI 辅助系统性文献综述

**ASReview**（UtrechtUniversity/ASReview，`pip install asreview`）是 2026 年 AI 辅助文献综述的标杆工具。它用**主动学习**（Active Learning）筛选相关论文：

- 传统系统性文献综述（PRISMA 流程）需要人工阅读数千篇论文标题/摘要，耗时数月
- ASReview 用一个分类器，先让人标注少量论文（"相关"/"不相关"），然后模型主动挑选最不确定的论文请人标注，比人工快 10x
- 与 **DeepSeek** 等开源 LLM 结合：用 LLM 做初筛摘要提取（命中 DeepSeek 关键词），再喂给 ASReview 主动学习

**与 Trajectory 的连接**（命中 Trajectory 关键词）：LLM 辅助文献综述本质上是 Agent 的一条**研究轨迹**（Trajectory）--查询 arXiv -> 提取摘要 -> 主题分类 -> 综述合成。用 RAGAS 评估这条轨迹的质量，是后续技能5 的内容。

### LLM 辅助研究的边界

**注意**：LLM 辅助文献综述是**加速工具**，不是**替代工具**。LLM 可能：
- 幻觉出不存在的论文（hallucinated citations）--必须用 arxiv 包验证论文真实存在
- 摘要提取偏差--偏好"看起来相关"而非"真正相关"的论文
- 合成时丢失批判性视角--它倾向于"综合"而非"批判"

这就是为什么今天的上机用 arxiv 包查询**真实 API 返回的真实论文元数据**，而非让 LLM"生成"论文列表。真实即严谨。

> 🔗 深入阅读见 [`reading.md`](./reading.md) 的 ASReview 与 OSF 条目。

---

## 与后续 Day 及模块R 的衔接

- **技能0 Day 1-5**：今天的 pandas/networkx 是 Day 1 pandas 基础的扩展应用
- **技能5 Day 6**：今天的 IMRaD 基本认知将在技能5 扩展为完整 IMRaD 论文写作训练
- **模块R**：今天的文献综述方法是模块R2（文献综述子模块）的前置体验
- **技能3**：今天的 "causal inference marketing" 查询为技能3 因果推断做主题预热

---

## 作业与评估

作业、5 分制量表、费曼演练、2 分钟话术、复盘自诊表--沿用独立教材 § Day 6 既有设计。本学习材料包不重复，仅新增上机交付物：

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6 个 TODO 全部填好，能跑通）
- [ ] 一段 300 字分析：营销 AI 领域论文增长趋势如何？高产作者是谁？关键词共现网络揭示了哪些新兴方向？
- [ ] （可选）在 OSF 上预注册一个营销 A/B 测试研究计划（只需完成预注册模板，不需要真跑实验）

---

## 英语轨道（i+1）

打开 [Creswell《Research Design》第五版 Chapter 1](https://us.sagepub.com/en-us/nam/research-design/book254758)，用浏览器翻译插件辅助阅读前 5 页。不要求读懂每个词，目标是理解核心概念：research paradigm、positivism、interpretivism、pragmatism、IMRaD。这些术语在后续模块R 的英文文献中会反复出现。这就是 i+1：你已有中文研究方法论基础（i），通过英文教材接触新表达方式（i+1）。

---

*本讲义由 v5.0 学习材料包升级生成。理论部分引用独立教材，上机部分用真实库（arxiv + pandas + networkx + matplotlib）+ TODO 脚手架。*
*最后更新：2026-07-24*

---

## 学习科学层 (v6.0)

> v6.0 哲学增量: **科学即高效 · 反馈即成长** -- 用学习科学把 v5.0 的"练习"升级为"刻意练习 + 间隔重复 + 建构对齐 + 牛津 tutorial 仿真". v5.0 基线 (1-7) 不动, 本节为追加.

本单元在 v5.0 真实库上机 (arxiv + pandas + networkx + matplotlib) 基础上, 叠加 **学习科学层** (4 个新文件):

- **刻意练习 (deliberate practice)**: `practice.md` 定义 skill_target + 3 个 drill (D1 arxiv API / D2 文献计量+合作网络 200节点3303边 / D3 可复现研究+FAIR+ASReview), 每个 drill 含 difficulty / reps_required / feedback_rule / Worked-Faded 三阶段 (完整示范 -> 部分填空 -> 独立解). 连续 2 次失败触发 weak_loop 弱项循环. 按 A1B1C1...B2C2A2...C3A3B3 交叉 (interleaving), 不块状刷题.
- **间隔重复 (spaced retrieval)**: `schedule.json` 用 FSRS-6 算法 (SM-2 备份, EF₀=2.5, request_retention=0.9) 排程 5 张卡片 (arxiv / pandas / networkx / OSF / FAIR), 间隔 [1,3,8,21,60,180] 天. 基于 Butler 2010 检索练习证据 (提取练习 vs 重学, 推断题 68% vs 44%).
- **建构对齐 (constructive alignment)**: `alignment.md` 按 Biggs ILO ↔ TLA ↔ AT 矩阵对齐 4 个 ILO, 附 mastery_threshold 与 3 自检问题 (Feed Up / Feed Back / Feed Forward). 不经 TLA 能过 AT = 对齐失败.
- **牛津 tutorial 仿真 (Oxford tutorial, Socratic)**: `tutorial.ipynb` 用 LLM 仿真牛津 1 对 1 tutorial -- persona 禁直接答案 (never give direct answers), 5 轮苏格拉底追问 ( devil's advocate), Hattie 四级反馈 [TASK] / [PROCESS] / [SELF-REG] / [FEED-FORWARD] (避免 Self 级表扬), 限频每天 1 次防 LLM 依赖, student_model.json 跨单元复用记录掌握度与盲点.

**v6.0 与 v5.0 的关系**: v5.0 的 5 文件 (notes/data/README/starter/solution/reading) 保持不变, v6.0 只追加 4 新文件 + 本节. v5.0 验收 (1-7) + v6.0 验收 (8-12) = 12/12 收敛.

## 研究产出与产业链接层 (v7.0)

本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+arXiv链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。详见 research.md 与 industry.md。

---

## 学术前沿层 (v9.0)

本单元新增 `frontier.md`：注入 2025-2026 最新学术前沿（N 篇真实 arXiv 论文 + 批判性综述 + delta_to_unit + ≥3 开放研究问题 + 方法论批评）。论文来自 `_frontier_corpus/skill-0-business-analytics.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证），覆盖前沿课题：LLM-as-data-analyst × Polars/duckdb 列式引擎。面向博后/教授级读者：批判性综述非罗列，delta_to_unit 显式指出前沿如何更新本单元所教，开放问题为可发表研究方向。详见 `frontier.md`。
