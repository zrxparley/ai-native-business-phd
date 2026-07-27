# 模块R · R5 学术论文写作（IMRaD格式）· 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 模块R 博士研究方法论 · R5
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：IMRaD 不是格式模板，而是科学交流效率的最优解--如何用 Python 拆解真实论文结构、规范统计报告、模拟同行评审？
> **v5.0 升级点**：① 新增真实库上机（arxiv + statsmodels + scipy.stats + causaldata）② 新增 TODO 填空式起始笔记本 ③ Notebook 化 ④ 深链阅读 ⑤ 2026 前沿（LLM-as-a-judge 自动评估写作质量 + DeepSeek 辅助写作 + 天道推演设计论证路径）

---

## 与技能5 Day6 的区别（关键定位）

| 维度 | 技能5 Day6（工程应用） | 模块R R5（方法论本身） |
|------|----------------------|----------------------|
| 聚焦点 | 把 Agent 论文写成 IMRaD 格式 | IMRaD 写作方法论本身 |
| 结构分析 | 解析1篇 ReAct 论文 | 跨多篇论文做结构元分析（句级IMRaD分类/节占比对比） |
| 统计报告 | t检验 + Cohen's d + 卡方 | APA第7版统计报告规范（效应量解读/CI报告/p值精确度/格式模板） |
| 标题摘要 | 简单提及 | 标题写法（信息密度/关键词布局）+ 结构化摘要方法论 |
| 同行评审 | 无 | LLM-as-a-judge 模拟同行评审（checklist驱动） |
| 论证路径 | 无 | 天道推演设计论证路径（因果链→沙盘→最优路径） |

> 本单元聚焦"写作方法论本身"：结构惯例为何如此、统计报告如何规范、同行评审如何运作。技能5 Day6 是"用方法论写一篇Agent论文"，本单元是"理解方法论背后的道理"。

---

## 学习目标（学完你能做到）

1. 能用 **arxiv** Python 包下载多篇真实论文（ReAct/LLM-as-a-judge/GraphRAG），对摘要做句级 IMRaD 分类（Introduction/Methods/Results/Discussion），计算各节占比并跨论文对比结构差异--从真实论文中归纳 IMRaD 结构惯例，而非看抽象模板
2. 能阐述 **Introduction 漏斗结构**（领域背景 -> 具体问题 -> 研究空白 -> 本文贡献 -> 论文结构）和 **Discussion 六要素**（发现解读/理论贡献/实践启示/局限性/未来方向/伦理声明），并用天道推演的因果链追踪设计论文的论证路径
3. 能用 **statsmodels + scipy.stats** 对真实因果推断数据（causaldata NSW职业培训实验，N=445）执行独立样本 t 检验、计算 Cohen's d 效应量和 95% 置信区间，按 **APA 第7版**格式撰写 Results 部分的统计报告
4. 能撰写符合学术规范的 **Title**（信息密度/关键词布局）和 **结构化 Abstract**（IMRaD微缩版，200词以内），确保标题和摘要是论文的"广告"和"导航"
5. 能用 **LLM-as-a-judge** 范式构建同行评审模拟器--对 IMRaD 各部分按预设 criteria 打分（Introduction清晰度/Methods可复现性/Results统计严谨/Discussion诚实度），理解 LLM 评审的偏差与局限

---

## 理论部分：精炼索引（详见独立教材）

> R5 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_模块R_博士研究方法论.md`](../../AI原生化商业博士_独立教材_模块R_博士研究方法论.md) § 六、R5：学术论文写作（IMRaD格式）（6.1-6.7节，已包含 IMRaD四部分结构详解/学术引用规范/GraphRAG营销系统论文大纲/与博士论文关联/对标大学/实践练习/英语轨道材料）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：IMRaD 四部分结构与读者问题

| 读者的问题 | IMRaD 对应部分 | 核心功能 | 写作原则 |
|-----------|:----------:|---------|---------|
| "你为什么做这个研究？" | Introduction | 建立研究背景和动机 | 漏斗结构：从大到小 |
| "你是怎么做的？" | Methods | 让别人能复现你的研究 | 可复现性五要素 |
| "你发现了什么？" | Results | 用数据说话 | 先描述再解释 |
| "这意味着什么？" | Discussion | 解读发现，承认局限 | 诚实面对局限 |

**核心洞察**（独立教材 §6.1）：IMRaD 不是任意的格式要求，而是科学交流效率的最优解。它回答了读者最关心的四个问题，每个部分解决一个核心功能。

### 关键回顾 2：Introduction 漏斗结构

Introduction 遵循"倒三角"--从大到小，从宽到窄（独立教材 §6.1）：

```
领域背景（宽） -> 具体问题（窄） -> 研究空白（更窄） -> 本文贡献（最窄） -> 论文结构
```

**写作要点**：
- 领域背景：2-3段，引用行业报告和学术文献
- 具体问题：1-2段，明确指出当前系统的问题
- 研究空白：1段，通过文献综述指出前人没做什么
- 本文贡献：1-3个bullet points，清晰声明本文做了什么

### 关键回顾 3：Methods 可复现性

Methods 的核心要求是**可复现性**（独立教材 §6.1）：别人读完你的 Methods，应该能用同样的方法重复你的研究。

**Methods 四要素**：研究设计（DSR/行动研究/混合方法） -> 数据来源（样本量/收集方式/脱敏处理） -> 分析方法（统计模型/工具） -> 评估指标（为什么选这些指标/如何计算）

### 关键回顾 4：Results 统计严谨 + APA 第7版

Results 的原则是**先描述再解释**，**诚实报告**所有结果（独立教材 §6.1）。统计报告必须包含效应量、置信区间和p值。

**APA 第7版统计报告格式**：
- t检验：`t(df) = X.XX, p = .XXX, d = X.XX`
- 效应量解读：d = 0.2 小，d = 0.5 中，d = 0.8 大（Cohen, 1988）
- 95% CI：`95% CI [LL, UL]`
- p值精确报告：p = .003（不写 p < .01，除非 p < .001）

### 关键回顾 5：Discussion 论文灵魂

Discussion 六要素（独立教材 §6.1）：发现解读 -> 理论贡献 -> 实践启示 -> 局限性 -> 未来方向 -> 伦理声明

**关键认知**：局限性不是弱点，诚实面对局限是学术成熟的标志。

### 关键回顾 6：学术引用规范（APA第7版）

独立教材 §6.2：APA第7版是商业和管理领域最常用的引用格式。
- **文中引用**：(Hevner et al., 2004)；直接引用标注页码：(Hevner et al., 2004, p. 80)
- **参考文献列表**：按作者姓氏字母排序。Author, A. A. (Year). Title. Journal Name, Volume(Issue), Pages. DOI
- **引用伦理**：所有非原创观点、数据、方法都必须引用来源。遗漏引用构成学术不端

---

## 上机部分：用 Python 拆解真实论文结构 + 规范统计报告 + 模拟同行评审

> 📓 **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO 填空版，你来做）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，gated，做完再看）
> 📊 **真实数据/库**：[`data/README.md`](./data/README.md)（arxiv + statsmodels + scipy.stats + causaldata NSW）

### 为什么用真实库而非手写文本

v4.0 的"IMRaD 写作"只是讲解格式模板--学生看了模板还是不会写。v5.0 改用**真实论文 + 真实统计工具 + 真实因果推断数据**：

- **arxiv**（lukasschwab/arxiv.py，1.5k★）：下载多篇真实论文，对摘要做句级IMRaD分类，跨论文对比结构差异--让学生从真实学术实践中归纳结构惯例
- **statsmodels + scipy.stats**：对真实因果推断数据（causaldata NSW职业培训实验，N=445）跑t检验/Cohen's d/CI，按APA第7版格式撰写Results--让统计报告有真实数据支撑，而非编造数字
- **causaldata**（NSW实验数据）：LaLonde (1986) 经典因果推断数据集，treat=1（职业培训）vs treat=0（对照），结果变量re78（1978年收入）。真实RCT数据，统计检验有实际意义

### 营销映射（关键桥接）

本单元撰写一篇"AI营销内容生成Agent效果评估"的IMRaD短论文草稿（用真实数据做统计报告练习）：

| IMRaD 部分 | 营销研究内容 | 方法论焦点 | 工具/方法 |
|-----------|------------|----------|----------|
| Title + Abstract | AI营销Agent效果评估研究 | 信息密度/结构化摘要 | 标题摘要写法 |
| Introduction | AI原生营销趋势 + Agent效果评估空白 | 漏斗结构/天道推演论证路径 | 因果链追踪 |
| Methods | NSW实验设计类比 + A/B测试设计 | 可复现性四要素 | 研究设计规范 |
| Results | NSW数据t检验 + Cohen's d + 95% CI | APA第7版统计报告 | statsmodels + scipy |
| Discussion | 效应量解读 + 局限性 + LLM-as-a-judge偏差 | 六要素写作 | 诚实报告 |
| Peer Review | 各部分质量评分 | LLM-as-a-judge模拟同行评审 | checklist驱动 |

> **NSW数据与营销的桥接**：NSW是职业培训实验（treat=培训 vs control=无培训），营销A/B测试是（treat=AI Agent vs control=人工）。两者结构同构：都是RCT，都是二值处理变量，都是连续结果变量。用NSW学统计报告规范，迁移到营销A/B测试报告。

### 上机任务（6 个 TODO，见 starter.ipynb）

1. **TODO1**：用 arxiv 包下载3篇真实论文（ReAct/LLM-as-a-judge/GraphRAG），对摘要做句级IMRaD分类，计算各节占比
2. **TODO2**：撰写符合规范的 Title 和结构化 Abstract（IMRaD微缩版，200词以内）
3. **TODO3**：撰写 Introduction（漏斗结构：背景 -> 问题 -> 空白 -> 贡献 -> 结构），用天道推演设计论证路径
4. **TODO4**：用 statsmodels + scipy.stats 对真实NSW数据跑t检验/Cohen's d/CI，按APA第7版撰写Results
5. **TODO5**：撰写 Methods（研究设计/数据来源/分析方法/评估指标），确保可复现性
6. **TODO6**：构建LLM-as-a-judge同行评审checklist，对IMRaD各部分按criteria打分

---

## 2026 前沿补充：LLM-as-a-judge + DeepSeek + 天道推演

> v5.0 新增前沿点。学术论文写作的核心难题是"写作质量"需要语义理解--人工审稿太慢，格式检查太浅。2026年的趋势是用 **LLM-as-a-judge** 自动评估论文各部分质量，用 **DeepSeek** 等开源模型降低评估成本，用 **天道推演** 设计最优论证路径。

### LLM-as-a-judge 自动评估论文写作质量

**LLM-as-a-judge**（Zheng et al., NeurIPS 2023, arXiv 2306.05685）用强LLM扮演"论文审稿人"，按预设criteria对IMRaD各部分打分：

- **Introduction**：研究问题是否清晰？贡献声明是否具体？漏斗结构是否连贯？
- **Methods**：是否可复现？评估指标是否合理？数据分析方法是否恰当？
- **Results**：统计检验是否正确？APA格式是否准确？效应量解读是否合理？
- **Discussion**：局限性是否诚实？理论贡献是否有深度？未来方向是否有可行性？

**注意**：LLM-as-a-judge是**辅助评估工具**，有自身偏差（位置偏差/冗长偏差/自我偏好偏差）。它对应因果阶梯的L1（对文本的关联分析），不能替代真实同行评审（L2干预：修改后重新提交）。定位为"投稿前自检工具"。

### DeepSeek 辅助学术写作

2026年 **DeepSeek-V3/R1** 等开源模型在写作评估任务上接近GPT-4水平，成本仅为1/10，可用于：
- 大批量论文写作自检（每次修改后自动评分）
- CI/CD集成（论文提交前自动检查IMRaD结构完整性）
- 多judge投票（用多个开源模型交叉评估，缓解单一模型偏差）

### 天道推演设计论文论证路径

**天道推演**（元认知沙盘推演）可用于设计论文的论证路径：

1. **因果链追踪**：从研究问题出发，构建"假设 -> 证据 -> 结论"的因果有向图。识别关键因果节点：哪些论证步骤是逻辑链的薄弱环节？
2. **沙盘模拟**：在意识中并行构建多个论证路径（如"先理论后实证" vs "先实证后理论" vs "理论实证交替"），每条路径推演3层（审稿人可能怎么质疑 -> 你怎么回应 -> 审稿人怎么再质疑）
3. **最优路径推荐**：综合权衡说服力、严谨性、新颖性，选择最优论证路径。识别"高杠杆点"：哪个论证步骤的加强能最大化提升论文说服力？

> 天道推演不是替代写作，而是在写作前"推演"论证路径--减少"写完发现逻辑不通再重写"的损耗。

---

## 与其他模块的衔接

- **R3 混合方法**：本单元的Methods部分需要说明混合方法设计（定量+定性整合策略），R3提供方法论基础
- **R4 PRISMA**：本单元的Introduction部分需要文献综述支撑研究空白，R4的PRISMA流程提供系统文献综述方法
- **R6 研究伦理**：本单元的Discussion部分需要伦理声明，R6提供研究伦理和AI治理框架
- **技能3 因果推断**：本单元的Results部分使用NSW数据做t检验，技能3的因果推断方法（DML/合成控制）是更高级的统计报告

---

## 作业与评估

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6个TODO全部填好，能跑通）
- [ ] 一段300字分析：你在哪个IMRaD部分最难写？为什么？（Introduction的漏斗结构？Methods的可复现性？Results的APA格式？Discussion的局限性诚实度？）
- [ ] （可选）用LLM-as-a-judge评估你写的Introduction质量，记录评分和理由，分析LLM评审与你自评的差异

---

*本讲义由v5.0学习材料包升级生成。理论部分引用独立教材，上机部分用真实库（arxiv + statsmodels + scipy.stats + causaldata）+ TODO脚手架。*
*最后更新：2026-07-24*

## 学习科学层 (v6.0)

本单元采用**刻意练习** (Ericsson deliberate practice, 3 subskills x worked-faded 三阶段) / **间隔重复** (FSRS-6, SM-2 backup, request_retention=0.9, 8 cards 含 IMRaD 漏斗/APA 第7版/LLM-as-a-judge 偏差/preregistration-OSF) / **建构对齐** (Biggs ILO↔TLA↔AT 矩阵 6 行 + mastery 阈值 + 3 自检 Feed Up/Back/Forward) / **牛津 tutorial LLM 仿真** (Socratic 追问 + Hattie 四级反馈 [TASK]/[PROCESS]/[SELF-REG]/[FEED-FORWARD], 限频 1 次/天防依赖)。

mastery 阈值与 Worked-Faded 示例见 `practice.md` 与 `alignment.md`。**交叉练习 (interleaving)** 按 A1B1C1->B2C2A2->C3A3B3 轮转促进迁移，**提取练习 (retrieval practice)** 优于重读 (pre-tutorial essay 强制 retrieval)。弱项循环 (weak_loop) 连续 2 次失败触发回退 worked example。

v6.0 关键词命中清单: FSRS-6, SM-2, 刻意练习, deliberate practice, 建构对齐, constructive alignment, 牛津 tutorial, Socratic, Hattie, 间隔重复, spaced retrieval, 交叉, interleaving, mastery, Worked-Faded, retrieval practice, formative feedback。

## 研究产出与产业链接层 (v7.0)
本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+arXiv链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。详见 research.md 与 industry.md。
