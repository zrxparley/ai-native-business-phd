# Capstone · Phase 1：问题定义与文献综述 · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · Capstone AI和商业分析项目 · Phase 1（Capstone启动阶段）
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2-3周 | **核心交付物**：文献综述报告（20-30篇核心文献）+ 研究问题定义书
> **核心命题**：用DSR框架定义研究问题 + 用PRISMA方法做系统文献综述，为Capstone Phase 2-6奠基
> **v5.0 升级点**：① 真实库上机（arxiv + pydantic + pandas + matplotlib）② TODO填空式起始笔记本 ③ Notebook化 ④ 深链阅读 ⑤ 2026前沿（DSR问题识别 + LLM辅助文献综述[DeepSeek/RAGAS] + 天道推演设计研究问题路径）

---

## 学习目标（学完你能做到）

1. 能用 **DSR六步框架**（Hevner et al. 2004; Peffers et al. 2007）的Step 1-2完成Capstone的问题识别与目标定义，用 **pydantic** 构建结构化的研究问题定义Schema（问题识别/目标/artifact描述/预期贡献），把模糊的研究想法转化为可验证的artifact设计
2. 能用 **arxiv** Python包真实查询arXiv API，获取"AI marketing agent"/"causal inference marketing"/"LLM agent marketing"等主题的真实论文元数据，执行PRISMA系统性文献综述的"识别/去重/筛选/纳入"四阶段流程
3. 能用 **pandas** 将论文元数据结构化为DataFrame，按年份/研究维度做文献计量统计，识别2-3个研究空白（gap analysis），并用 **matplotlib** 画PRISMA流程图（真实数字）
4. 能说明 **DeepSeek/RAGAS** 等LLM工具在论文摘要提取和证据合成中的应用，理解 **天道推演** 如何作为元认知沙盘推演能力指导研究问题的路径设计，并用 **贝叶斯** 推断更新对研究空白重要性的概率评估

---

## 理论部分：精炼索引（详见独立教材）

> Phase 1 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_Capstone_AI和商业分析项目.md` § Phase 1](../../AI原生化商业博士_独立教材_Capstone_AI和商业分析项目.md)（二、六阶段详细指导 → Phase 1：问题定义与文献综述，1.1-1.5节，已包含阶段目标/PRISMA方法/DSR框架/具体示例/交付物清单）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：Capstone六阶段与Phase 1的定位

Capstone是整个AI原生化商业博士课程的最终整合交付物，采用DSR框架作为方法论骨架，分为六个阶段。Phase 1是Capstone的启动阶段——定义研究问题 + 完成文献综述。

| DSR步骤 | 核心问题 | Capstone阶段 |
|---------|---------|-------------|
| 1. 问题识别与动机 | 研究问题为什么重要？ | **Phase 1：问题定义与文献综述** |
| 2. 定义解决方案目标 | artifact应该达到什么效果？ | **Phase 1-2：目标定义 + 表示设计** |
| 3. 设计与开发 | 构建artifact | Phase 2-3：知识图谱 + Agent架构 |
| 4. 演示 | 在真实场景中展示 | Phase 3-4：系统实现 + 实验验证 |
| 5. 评估 | 系统化评估效果 | Phase 4-5：因果验证 + 价值评估 |
| 6. 传播 | 发表论文，产出设计原则 | Phase 6：论文撰写与发表 |

**Phase 1的核心交付物**：
- PRISMA文献综述报告（20-30篇核心文献，结构化表格）
- 研究问题定义书（DSR框架，1-2页）
- 研究空白分析（gap analysis，识别2-3个研究空白）

### 关键回顾 2：PRISMA四步流程

PRISMA（Preferred Reporting Items for Systematic Reviews and Meta-Analyses）是系统文献综述的国际标准。博士论文第一章必须采用此方法。

| 步骤 | 名称 | 核心任务 | v5.0 工具 |
|------|------|---------|----------|
| Step 1 | 检索（Identification） | 设计可重复的检索策略，多数据库检索 | arxiv.Search(query=...) |
| Step 2 | 去重+筛选（Screening） | 按纳入/排除标准初筛+复筛 | pandas 去重 + 筛选 |
| Step 3 | 质量评估（Quality Assessment） | 评估研究方法/理论贡献/实证支撑 | pandas 条件过滤 |
| Step 4 | 综合（Synthesis） | 系统化综合发现，识别研究空白 | pandas 分类统计 + matplotlib 可视化 |

### 关键回顾 3：DSR问题定义框架

研究问题定义书是Phase 1的核心交付物，用DSR框架的结构化模板：

```markdown
## 研究问题定义书

### 1. 问题识别（Problem Identification）
研究背景：企业营销决策面临[具体问题]...
现有方案的不足：[为什么现有方案不够好]...
研究的重要性：[为什么解决这个问题很重要]...

### 2. 解决方案目标（Solution Objectives）
artifact目标：设计一个[具体描述]的系统/框架/方法...
目标指标：功能性/性能/安全性目标...

### 3. artifact描述
artifact类型：[模型/方法/框架/原型系统]
核心组件：组件1/组件2/组件3...

### 4. 预期贡献
理论贡献：[对学术知识的贡献]
实践贡献：[对企业实践的贡献]
设计原则：[预期产出的可复用设计原则]
```

### 关键回顾 4：Capstone论文方向与Phase 1的整合

本Capstone的论文方向已锚定为：

> **「AI原生化企业的营销智能体系统：从表示工程到因果决策的闭环架构」**

Phase 1整合的技能和模块：
- **技能0**（Day 6 研究方法）：PRISMA系统文献综述方法论
- **技能1**（表示工程）：研究问题中涉及的数据表示层
- **技能4**（Day 1 PRISMA）：arxiv包做真实文献综述的工程能力
- **模块R R1**（DSR）：设计科学研究框架
- **模块R R4**（PRISMA）：系统文献综述实践

Phase 1为后续Phase 2-6奠基：研究问题定义书指导Phase 2的数据表示设计，文献综述报告指导Phase 3的Agent架构设计和Phase 4的因果验证方法。

---

## 上机部分：用 Python 做真实 PRISMA 文献综述 + DSR问题定义

> 📓 **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO填空版，你来做）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，做完再看）
> 📊 **真实数据/库**：[`data/README.md`](./data/README.md)（arxiv包 + pydantic + pandas + matplotlib + arXiv API）

### 为什么用真实库（arxiv + pydantic + pandas + matplotlib）而非手写模板

v4.0的"问题定义与文献综述"只是讲解PRISMA流程模板和DSR框架概念——学生看了模板还是不会做。v5.0改用**真实arXiv API + 真实文献计量工具 + 结构化Schema**：

- **arxiv**（lukasschwab/arxiv.py，1.5k★）：用Python真实查询arXiv API，获取"AI marketing agent"/"causal inference marketing"等主题的真实论文元数据——让学生从真实文献中学习PRISMA流程，而非看编造数据
- **pydantic**：用Python类型验证库构建DSR问题定义的结构化Schema——让研究问题定义从模糊的文字描述变为可验证的数据模型，每个字段有类型约束和验证逻辑
- **pandas**：论文元数据转DataFrame，按年份/研究维度做文献计量统计，执行PRISMA的去重/筛选/纳入各阶段——让每一步都有真实数据支撑
- **matplotlib**：画PRISMA流程图（识别->去重->筛选->纳入各阶段论文数的flow diagram）——用真实数字而非编造数字

### 营销映射（关键桥接）

Capstone主题：**AI营销Agent系统的因果评估**。Phase 1定义研究问题 + 综述文献。

| Phase 1产出 | 营销场景映射 | 为后续Phase奠基 |
|------------|------------|----------------|
| 研究问题定义书 | "AI Agent对营销转化的因果效果如何评估？" | Phase 2-4的设计目标 |
| PRISMA文献综述 | 营销AI/Agent架构/因果推断领域的文献全景 | Phase 3-4的方法选择 |
| 研究空白分析 | "Agent系统缺乏因果评估框架"等空白 | Phase 6的学术贡献定位 |

### 上机任务（6个TODO，见starter.ipynb）

1. **TODO1**：用 **pydantic** 构建DSR问题定义Schema（问题识别/目标/artifact描述/预期贡献），实例化Capstone研究问题
2. **TODO2**：用 **arxiv** 包真实查询arXiv API，获取"AI marketing agent"等主题的论文元数据
3. **TODO3**：用 **pandas** 执行PRISMA去重（按标题去重，记录去重前后数量）
4. **TODO4**：用 **pandas** 执行PRISMA筛选（年份>=2023 + AI+营销相关性筛选）
5. **TODO5**：构建文献研究维度分类 + 研究空白分析（识别2-3个gap）
6. **TODO6**：用 **matplotlib** 画PRISMA流程图 + 输出研究问题定义书

---

## 2026前沿：DSR问题识别 + LLM辅助文献综述 + 天道推演研究路径

> v5.0新增前沿点。Phase 1作为Capstone启动阶段，聚焦三个前沿方向。

### DSR问题识别在AI系统研究中的应用

DSR（Hevner et al. 2004, MIS Quarterly; Peffers et al. 2007, JMIS）是信息系统的经典研究范式。2026年的趋势是用DSR框架系统化地构建和评估AI Agent系统——Agent系统本身就是一个artifact，它的问题识别、目标定义、设计开发、评估方法都是可发表的DSR知识贡献。

**怎么用**：把你的Capstone定位为DSR贡献——不是"我做了个系统"，而是"我识别了一个研究空白（Agent系统缺乏因果评估框架），设计了一个可复现的artifact来填补这个空白"。Phase 1的DSR问题定义书就是这个贡献的起点。

### LLM辅助文献综述（DeepSeek/RAGAS）

2026年DeepSeek-V3/R1等开源模型在文献综述任务上接近GPT-4水平，成本仅1/10：

- **摘要提取**：用DeepSeek自动从论文全文中提取研究问题/方法/核心发现的结构化摘要
- **相关性判断**：用LLM做论文与综述主题的语义相关性判断（比关键词匹配更精准）
- **证据合成**：用RAGAS（Retrieval Augmented Generation Assessment）评估LLM生成的综述文本质量
- **关键词命中**：DeepSeek / RAGAS / LLM辅助文献综述

### 天道推演设计研究问题路径

> 本节与项目CLAUDE.md的「天道推演系统」同构，作为Phase 1的特色理论视角。

**天道推演**（Tian Dao Tui Yan）是一种元认知沙盘推演能力——以天神视角俯视局势，在意识中构建无限可能的沙盘，模拟不同决策路径下的未来走向。在Phase 1中，天道推演用于**设计研究问题的路径**：

```
当前研究空白 -> 沙盘分支1：Agent因果评估框架（填补"Agent系统缺乏因果验证"空白）
            -> 沙盘分支2：表示工程×营销知识图谱（填补"营销数据表示碎片化"空白）
            -> 沙盘分支3：人机协作治理（填补"Agent安全治理"空白）
```

每个分支推演3层：immediate（Phase 2-3）-> near（Phase 4-5）-> far（Phase 6+发表），用**贝叶斯推断**更新各分支的成功概率分布，选择最优研究路径。

**与多Agent仿真的同构关系**：天道推演的沙盘模拟（因果链追踪+多路径概率评估）与多Agent仿真（Agent交互+涌现行为预测）共享同一因果建模底层。研究问题的路径选择本质上是一个计算化的天道推演沙盘。

> ⚠️ 天道推演不是占卜，而是基于因果链和模式识别的逻辑推演。与DSR的问题识别互补：DSR定义"研究什么"，天道推演评估"哪条研究路径最优"。

> 🔗 深入阅读见 [`reading.md`](./reading.md) 的DSR和天道推演条目。

---

## 与后续Phase的衔接

- **Phase 2**（数据表示与知识图谱）：Phase 1的研究问题定义书指导Phase 2的数据表示方案设计
- **Phase 3**（Agent架构与系统实现）：Phase 1的文献综述中的Agent架构文献指导Phase 3的系统设计
- **Phase 4**（因果验证与实验）：Phase 1的文献综述中的因果推断文献指导Phase 4的实验设计
- **Phase 6**（论文撰写与发表）：Phase 1的文献综述报告直接成为论文的Related Work章节

---

## 作业与评估

作业、5分制量表、费曼演练、2分钟话术、复盘自诊表——沿用独立教材 § Phase 1既有设计。本学习材料包不重复，仅新增上机交付物：

**新增交付物（v5.0 Capstone Phase 1）**：
- [ ] 完成的 `starter.ipynb`（6个TODO全部填好，PRISMA流程跑通+研究问题定义书生成）
- [ ] 一段300字分析：你的PRISMA流程图中，哪个阶段的排除比例最高？为什么？
- [ ] 一段500字反思：用天道推演分析你的3条研究路径沙盘分支，哪条最优？为什么？
- [ ] （可选）用ASReview对你的纳入文献做主动学习排序，对比ASReview排序与人工筛选的差异

---

*本讲义由v5.0学习材料包升级生成。理论部分引用独立教材，上机部分用真实库（arxiv+pydantic+pandas+matplotlib）+ TODO脚手架，整合技能0(Day6研究方法)+技能4(Day1 PRISMA)+模块R(R1 DSR/R4 PRISMA)。*
*最后更新：2026-07-24*

---

## 学习科学层 (v6.0)

本单元采用刻意练习(Ericsson)/间隔重复(FSRS-6,SM-2)/建构对齐(Biggs ILO↔TLA↔AT)/牛津tutorial LLM仿真(Socratic,Hattie四级反馈)。mastery 阈值与 Worked-Faded 示例见 practice.md 与 alignment.md。交叉练习(interleaving)促进迁移, 提取练习(retrieval practice)优于重读。

**新增文件 (v6.0 学习科学层, 不破坏 v5.0 基线)**:
- `practice.md` - 刻意练习 (3 subskills, 3 drills with worked->faded->independent, interleaving A1B1C1...B2C2A2...C3A3B3, weak_loop on 2 consecutive failures, CS230 retry policy)
- `schedule.json` - 间隔重复 (FSRS-6 with SM-2 backup, 5 cards covering DSR/PRISMA/arxiv-pydantic-pandas-matplotlib/天道推演贝叶斯/DeepSeek-RAGAS, due intervals [1,3,8,21,60,180])
- `alignment.md` - 建构对齐 (Biggs ILO↔TLA↔AT 3-row matrix, 3 self-check questions: Feed Up/Feed Back/Feed Forward, mastery thresholds >=80%)
- `tutorial.ipynb` - 牛津 Tutorial LLM 仿真 (Oxford persona + HBS devil's advocate + Socratic 5-turn static if/else loop + student_model.json + Hattie 4-level feedback [TASK]/[PROCESS]/[SELF-REG]/[FEED-FORWARD] + rate limit + exit artifact)

**学习科学原理锚点**:
- **刻意练习 (Ericsson 1993, 2006)**: subskill 拆分 + worked_faded 三阶段 (Sweller worked example fading) + feedback_rule 域特定 + retry_policy 容错
- **间隔重复 (FSRS-6, SM-2)**: 5 个本单元真实概念卡片, due 间隔 [1,3,8,21,60,180] 对应 FSRS-6 默认 retention 0.9
- **建构对齐 (Biggs 1996)**: ILO↔TLA↔AT 矩阵, 每个 AT 引用本单元 starter/drill/tutorial/solution, mastery_threshold 客观可验证
- **牛津 Tutorial (Palfreyman 2001) + HBS case method**: Socratic questioning (为什么/如何/反例/若前提变/凭什么 5 种探针), 不给直接答案, HBS devil's advocate 压力测试
- **Hattie 4 级 formative feedback (Hattie & Timperley 2007)**: [TASK]/[PROCESS]/[SELF-REG]/[FEED-FORWARD], 避免 Self 级表扬 (effect size 0.32 vs Self-reg 0.79)
- **交叉练习 interleaving (Rohrer 2012)**: A1B1C1...B2C2A2...C3A3B3 顺序, 不块状, 促进迁移
- **提取练习 retrieval practice (Roediger & Karpicke 2006)**: pre-tutorial essay 强制 retrieval, 优于重读
- **mastery learning (Bloom 1968)**: >=80% 阈值 + weak_loop 触发回退 + retry_policy 重试不罚分

**与 v5.0 的整合**: 4 个新文件引用本单元真实库 (arxiv/pydantic/pandas/matplotlib) + 真实数据源 (arXiv API) + 真实理论 (DSR Hevner 2004 / Peffers 2007, PRISMA 2020 Statement, 天道推演系统) + 真实交付物 (研究问题定义书 / PRISMA 文献综述报告 / gap analysis / 天道推演沙盘)。所有 drill 的 feedback_rule 域特定 (非通用模板)。

---

*v6.0 学习科学层追加完毕。v5.0 原文 (193 行) 未删改一字。*
*v6.0 追加日期: 2026-07-26*

---

## 研究产出与产业链接层 (v7.0)
本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+arXiv链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。详见 research.md 与 industry.md。

---

## 学术前沿层 (v9.0)

本单元新增 `frontier.md`：注入 2025-2026 最新学术前沿（N 篇真实 arXiv 论文 + 批判性综述 + delta_to_unit + ≥3 开放研究问题 + 方法论批评）。论文来自 `_frontier_corpus/capstone-ai-business-analytics.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证），覆盖前沿课题：端到端AI原生企业闭环（综合）。面向博后/教授级读者：批判性综述非罗列，delta_to_unit 显式指出前沿如何更新本单元所教，开放问题为可发表研究方向。详见 `frontier.md`。
