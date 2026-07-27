# 模块R · R1：设计科学研究（DSR）· 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 模块R 博士研究方法论 · R1 设计科学研究
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：如何用DSR方法论把工程实践转化为可发表的学术贡献？--从"做了一个系统"到"产出了设计原则"
> **v5.0 升级点**：① pydantic定义artifact规格schema ② pandas结构化七准则评估 ③ TODO填空脚手架 ④ Notebook化 ⑤ 深链阅读 ⑥ 2026前沿（DSR + 可复现研究 + 天道推演 + 贝叶斯 + 多Agent仿真）

---

## 学习目标（学完你能做到）

1. 能解释 **DSR（设计科学研究）** 的核心概念：artifact四种类型（constructs/models/methods/instantiations，March & Smith 1995）、Hevner七准则（Hevner et al. 2004, MIS Quarterly）、Peffers六步流程（Peffers et al. 2007, JMIS），并说明DSR与传统实证研究的根本区别（"如何构建" vs "是什么"）
2. 能用 **pydantic** 将DSR六步框架建模为结构化artifact规格schema（ProblemIdentification -> Objectives -> DesignDevelopment -> Demonstration -> Evaluation -> Communication），把一个真实AI系统（营销Agent系统）建模为DSR artifact实例
3. 能用 **pandas** 结构化评估一个真实artifact是否满足 **Hevner七准则**（artifact贡献/问题相关性/设计评估/研究贡献/严谨性/设计即搜索/交流），理解 rigor vs design 的核心张力
4. 能理解 **天道推演** 作为DSR设计推演工具的理论锚点：天道推演的沙盘模拟（因果链追踪 + 多路径概率评估）与DSR的设计搜索过程同构，可在构建artifact前模拟不同设计方案的可能走向
5. 能区分"做一个系统"和"产出设计原则"--DSR的学术贡献不在于artifact本身，而在于从设计和评估中产出的可复用的设计原则，这是从工程实践者到知识创造者的认知跃迁

---

## 理论部分：精炼索引（详见独立教材）

> R1 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_模块R_博士研究方法论.md` § 二、R1：设计科学研究](../../AI原生化商业博士_独立教材_模块R_博士研究方法论.md)（47-112行，已包含核心概念详解/GraphRAG案例分析/与博士论文关联/对标大学说明/实践练习/英语轨道材料）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：DSR六步框架（Peffers et al. 2007）

Peffers等人在Journal of Management Information Systems论文中提出DSR的标准执行框架：

```
Step 1: 问题识别与动机（Problem Identification and Motivation）
  -- 明确研究问题为什么重要，基于文献和实际观察论证未被解决的问题
  -- 关键产出：problem statement（清晰、具体、可验证的问题陈述）

Step 2: 定义解决方案目标（Define the Objectives for a Solution）
  -- artifact应该达到什么效果，目标必须可验证
  -- 目标来源：文献中未实现的要求 / 竞品差距 / 用户痛点

Step 3: 设计与开发（Design and Development）
  -- 构建artifact，基于理论知识进行有意识的设计决策
  -- 每个设计决策都有明确的理论依据：为什么选这种架构/算法？

Step 4: 演示（Demonstration）
  -- 在真实或模拟场景中展示artifact如何解决问题
  -- 目的：证明可行性

Step 5: 评估（Evaluation）
  -- 系统化评估artifact效果，与Step 2目标对应
  -- 方法：定量（A/B测试/性能对比）或定性（访谈/专家评审）

Step 6: 传播（Communication）
  -- 发表论文，产出设计原则
  -- 核心：将工程经验抽象为可复用的知识
```

### 关键回顾 2：Hevner七准则（Hevner et al. 2004, MIS Quarterly）

Hevner等人在MIS Quarterly发表的经典论文（引用超30,000次）提出DSR的七条准则：

| 准则 | 核心要求 | 评估要点 |
|------|---------|---------|
| 1. Artifact作为研究贡献 | artifact本身是新的知识贡献 | 是否创造了新的artifact类型？ |
| 2. 问题相关性 | 解决重要的实际问题 | 问题是否具有实际价值？ |
| 3. 设计评估 | artifact经过严格评估 | 评估方法是否系统化？ |
| 4. 研究贡献 | 产出新的设计原则/方法论 | 设计原则是否可泛化？ |
| 5. 研究严谨性 | 设计决策有理论依据 | 理论基础是否扎实？ |
| 6. 设计即搜索 | 设计是有意识的搜索过程 | 是否探索了替代方案？ |
| 7. 研究交流 | 有效传播给学术/实践受众 | 是否已发表/开源？ |

**rigor vs design 核心张力**：DSR的核心在于"设计严谨性"（rigor，理论依据）和"设计相关性"（design，实际问题）的平衡。纯学术artifact可能rigor高但design低；纯工程artifact可能design高但rigor低。好的DSR研究两者兼顾。

### 关键回顾 3：Artifact四种类型（March & Smith 1995）

| 类型 | 定义 | 营销AI示例 |
|------|------|-----------|
| constructs（构造） | 领域的基本概念和词汇 | "营销知识的多模态表示框架" |
| models（模型） | 构造之间的关系 | "营销因果图模型" |
| methods（方法） | 解决问题的算法或流程 | "知识图谱社区摘要增强全局推理" |
| instantiations（实例化） | 可运行的原型系统 | "基于GraphRAG的营销知识增强检索系统" |

### 关键回顾 4：DSR vs 传统实证研究

| 维度 | 传统实证研究 | DSR |
|------|------------|-----|
| 核心问题 | "是什么"（what is） | "如何构建"（how to build） |
| 研究产出 | 理论/规律 | artifact + 设计原则 |
| 评估对象 | 理论的解释力/预测力 | artifact的有效性 |
| 知识贡献 | 验证/挑战/新建理论 | 可复用的设计原则 |
| 适合场景 | 理解现象 | 解决问题 |

---

## 上机部分：用pydantic + pandas做DSR方法论实操

> 📓 **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO填空版，你来做）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，做完再看）
> 📊 **真实数据/库**：[`data/README.md`](./data/README.md)（pydantic + pandas + NSW真实RCT评估数据）

### 为什么用pydantic + pandas（而非手写文档）

v4.0 的DSR教学用Word文档写研究计划。v5.0 改用代码化方法论工具：

- **pydantic**（pydantic/pydantic，13k+ star，MIT License）：用类型安全的schema定义DSR artifact规格，把六步框架从"文档"变成"可验证的数据结构"
- **pandas**（pandas-dev/pandas，43k+ star，BSD-3-Clause）：用DataFrame结构化Hevner七准则评估，支持聚合统计和可视化

**方法论代码化的意义**：不是用代码"替代"研究方法论思考，而是用代码"结构化"方法论思考--pydantic的Field验证确保每个步骤都有内容，pandas的DataFrame确保每条准则都有评分和证据。

### 营销映射（关键桥接）

本单元用技能5 Day7的**营销策略Agent系统**作为DSR artifact实例：

| DSR六步 | 营销Agent系统实例化 | 真实数据/库 |
|---------|-------------------|------------|
| Step 1 问题识别 | 营销策略缺乏因果证据 | 企业实际问题 |
| Step 2 目标定义 | Agent基于因果证据生成策略 | 可验证的成功标准 |
| Step 3 设计开发 | LangGraph三节点Agent | ReAct/DSR/因果推断理论 |
| Step 4 演示 | NSW真实RCT营销映射 | causaldata NSW（445样本） |
| Step 5 评估 | ATE + 策略质量评分 | ATE=1794.34, 评分=0.80 |
| Step 6 传播 | 4条设计原则 + DSS投稿 | 可复用的设计原则 |

### 上机任务（6个TODO，见starter.ipynb）

1. **TODO1**：用pydantic定义DSR artifact规格schema（ArtifactType枚举 + 六步子模型 + DSRArtifact组合模型）
2. **TODO2**：实例化真实营销Agent系统为DSR artifact（填充schema，引用真实评估数据）
3. **TODO3**：用pandas定义Hevner七准则评估结构（DataFrame，7行4列）
4. **TODO4**：评估Artifact -- 填充七准则评分和证据（1-5分 + 具体evidence）
5. **TODO5**：提取设计原则（DSR Step 6: 传播，每条含原则/依据/泛化性）
6. **TODO6**：天道推演作为DSR设计推演工具 -- 构建同构映射（5行3列DataFrame）

---

## 2026前沿：DSR + 可复现研究 + 天道推演 + 贝叶斯 + 多Agent仿真

> v5.0新增前沿点。本单元覆盖五个前沿方向。

### DSR在AI原生系统的新生命

DSR（Hevner et al. 2004）是信息系统的经典研究范式，但在AI原生系统时代获得新生命：**Agent系统本身就是一个artifact**，它的架构模式、评估框架、安全实践都是可发表的DSR知识贡献。2026年的趋势是用DSR框架系统化地构建和评估AI Agent系统，产出可复现的架构设计和评估方法论。

**怎么用**：把你的Capstone定位为DSR贡献--不是"我做了个系统"，而是"我设计了一个可复现的Agent架构artifact，并用七准则框架评估了它的有效性"。

### 可复现研究（Reproducible Research）

可复现研究要求：不仅发表结论，还发表数据+代码+环境，让他人能独立复现你的结果。Agent系统的可复现性挑战更大（非确定性输出、API版本依赖、模型版本漂移）。2026年最佳实践：
- **artifact开源**：GitHub仓库 + 完整环境配置（requirements.txt/Dockerfile）
- **trace存档**：langsmith/Langfuse的执行trace，记录每次Agent运行的完整调用链
- **数据文档**：数据集来源、预处理、变量定义的完整文档
- **评估可复现**：deepeval的CI测试用例，确保代码变更后评估结果可追踪

### 天道推演作为DSR设计推演工具

> 本节与项目CLAUDE.md的「天道推演系统」同构，作为DSR方法论的特色理论视角。

**天道推演**是一种元认知沙盘推演能力--以天神视角俯视局势，在意识中构建无限可能的沙盘，模拟不同决策路径下的未来走向。其核心能力包括：局势感知、因果链追踪、沙盘模拟、概率评估、最优路径推荐。

**与DSR的同构关系**：

| 天道推演能力 | DSR六步对应 | 共享的因果建模底层 |
|-------------|-----------|-------------------|
| 局势感知 | Step 1 问题识别 | 状态空间定义 |
| 因果链追踪 | Step 3 设计开发的因果建模 | 因果有向图 |
| 沙盘模拟（3层推演） | Step 4 演示的多场景模拟 | 并行世界树 |
| 概率评估 | Step 5 评估的概率分布 | 贝叶斯推断 |
| 最优路径推荐 | Step 2 目标 + Step 6 传播 | 收益/风险权衡 |

**怎么用**：天道推演可作为DSR设计阶段的推演工具--在构建artifact前，先用天道推演沙盘模拟不同设计方案的可能走向，选择最优路径。

### 贝叶斯评估

传统DSR评估用点估计（如ATE=1794.34），但点估计隐藏了不确定性。**贝叶斯方法**用概率分布表达评估结果（如ATE ~ N(1794, 500)），更诚实地面对不确定性。2026年的趋势是用贝叶斯方法替代频率派点估计，特别是在样本量有限的DSR评估中。

### 多Agent仿真

**多Agent仿真**可作为DSR Step 4（演示）的高级形式：不是在单一场景中演示artifact，而是在多Agent环境中模拟Agent交互和涌现行为。这连接了DSR与复杂系统研究，为artifact评估提供了更丰富的场景。

> 🔗 深入阅读见 [`reading.md`](./reading.md) 的DSR和可复现研究条目。

---

## 营销映射：DSR方法论在营销AI artifact中的应用

DSR方法论可直接应用到营销AI artifact的设计和评估：

| DSR概念 | 营销AI artifact映射 | 示例 |
|---------|-------------------|------|
| Artifact (instantiation) | 营销Agent系统 | 基于因果推断的营销策略Agent |
| Artifact (method) | 营销知识检索方法 | GraphRAG社区摘要增强全局推理 |
| Artifact (model) | 营销因果图模型 | treat->re78的因果有向图 |
| Artifact (construct) | 营销效果度量构造 | ATE/CUPED/Uplift的概念定义 |
| Hevner准则3 (设计评估) | A/B测试 + 因果推断 | NSW真实RCT的ATE估计 |
| Hevner准则4 (研究贡献) | 营销Agent设计原则 | "因果证据优先"原则 |
| Hevner准则5 (严谨性) | 因果推断理论依据 | 潜在结果框架 (Imbens & Rubin 2015) |

**核心洞察**：营销AI系统的DSR贡献不在于"系统本身能做什么"，而在于"从系统设计中提炼出的设计原则能否被其他营销团队复用"。

---

## 与其他单元的区别

| 维度 | 本单元（R1 DSR方法论） | 技能5 Day7（Capstone工程） |
|------|----------------------|--------------------------|
| 聚焦点 | DSR方法论本身（七准则/六步/Artifact） | 端到端工程实现 |
| 工具 | pydantic (schema) + pandas (评估) | DoWhy + LangGraph + deepeval |
| 产出 | DSR artifact规格 + 七准则评分 + 设计原则 | 可运行的Agent系统 + 论文草稿 |
| 视角 | 方法论视角：如何把工程转化为学术贡献 | 工程视角：如何构建和评估系统 |
| 关系 | 本单元引用Day7的评估数据作为artifact实例 | Day7用DSR框架定位Capstone |

> 本单元不重复Day7的工程实现代码，而是用方法论视角重新审视Day7的系统作为DSR artifact。

---

## 与后续R模块的衔接

- **R2 行动研究**：R1的DSR聚焦artifact设计，R2聚焦在真实组织中部署artifact并产出知识--两者互补
- **R3 混合方法**：R1的DSR Step 5评估需要混合方法（定量+定性），R3提供混合方法的方法论基础
- **R4 PRISMA**：R1的DSR Step 1问题识别需要文献支撑，R4提供系统文献综述的方法论
- **R5 IMRaD**：R1的DSR Step 6传播需要论文写作，R5提供IMRaD格式的方法论
- **R6 研究伦理**：R1的DSR评估涉及用户数据，R6提供伦理审查框架

---

## 作业与评估

作业、5分制量表、费曼演练、2分钟话术、复盘自诊表--沿用独立教材 § R1既有设计。本学习材料包不重复，仅新增上机交付物：

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6个TODO全部填好，pydantic schema + pandas七准则评估跑通）
- [ ] 一段300字分析：你的artifact在Hevner七准则中哪一条最弱？如何改进？
- [ ] （可选）选择你的Capstone方向，用pydantic定义一个DSR artifact schema

---

## 英语轨道（i+1）

打开 [Peffers et al. (2007) 论文](https://desrist.org/desrist/files/peffers2007.pdf)的Abstract和Introduction，用浏览器翻译插件辅助阅读。不要求读懂每个词，目标是理解DSR六步的英文术语（Problem Identification, Objectives, Design and Development, Demonstration, Evaluation, Communication）。遇到关键术语记住英文形式--这些术语在后续所有学术论文中会反复出现。这就是i+1：你已有中文方法论基础（i），通过英文论文接触学术表达方式（i+1）。

---

*本讲义由v5.0学习材料包升级生成。理论部分引用独立教材，上机部分用真实库（pydantic + pandas）+ TODO脚手架，聚焦DSR方法论本身。*
*最后更新：2026-07-24*

## 学习科学层 (v6.0)

本单元采用刻意练习(Ericsson)/间隔重复(FSRS-6,SM-2)/建构对齐(Biggs ILO↔TLA↔AT)/牛津tutorial LLM仿真(Socratic,Hattie四级反馈)。mastery 阈值与 Worked-Faded 示例见 practice.md 与 alignment.md。交叉练习(interleaving)促进迁移, 提取练习(retrieval practice)优于重读。

- **刻意练习 (deliberate practice)**：practice.md 拆 3 子技能（pydantic schema 建模 / pandas 七准则评估 / 设计原则抽取），每子技能 worked-faded 三阶段（完整示范 -> 部分填空 -> 独立解），feedback_rule 全部锚定本单元真实数据（causaldata NSW ATE=1794.34）与真实库（pydantic/pandas/LangGraph）。
- **间隔重复 (spaced retrieval, FSRS-6 + SM-2 backup)**：schedule.json 含 5 张卡（March&Smith 四型 / Hevner 七准则 / Peffers 六步 / 天道推演同构 / 设计原则抽取），due=[1,3,8,21,60,180]，request_retention=0.9。
- **建构对齐 (constructive alignment, Biggs 1996)**：alignment.md 给出 ILO↔TLA↔AT 四行矩阵，每行 TLA 引用 starter.ipynb TODO + practice.md drill + tutorial.ipynb cell，AT 引用 solution.ipynb 自动评分 + drill independent 阶段，mastery_threshold >=80%。
- **牛津 tutorial LLM 仿真 (Oxford tutorial, Socratic)**：tutorial.ipynb 用静态 if/else 模拟牛津 tutor 苏格拉底追问（>=4 轮，5 类问：为什么/凭什么/如何/若前提变/反例），不调真实 LLM API；附 Hattie 四级形成性反馈 [TASK]/[PROCESS]/[SELF-REG]/[FEED-FORWARD]（避免 Self 级表扬，d=0.09 几乎无效；可执行反馈 d=0.79）。
- **限频防依赖**：每单元每天 1 次 tutorial（usage limit 1次/天），超额尝试被拒绝并记录到 student_model.json；间隔重复优于连续追问。
- **mastery 与弱项循环 (weak_loop)**：连续 2 次 drill 失败触发 weak_loop（回退上一难度 + 重做 worked 阶段 + 补充 worked example），通过后才回原 drill Faded 阶段。

## 研究产出与产业链接层 (v7.0)

本单元产出可发表研究工件 (research.md: 研究问题 + 贡献声明 + arXiv/JSTOR/DOI 链接 + IMRaD 大纲 + NeurIPS 可复现清单 7 项 + research-to-practice 翻译) 与产业链接 (industry.md: >=3 真实企业 Stitch Fix/LangChain/Booking.com/McKinsey/Burberry + 部署场景 + Imperial MSc BA 咨询项目 partner=Burberry + HBS 教学案例 + 客座讲座 + 实习指针 OpenAI/Anthropic Residency)。研究产出遵循 IMRaD / DSR (Hevner 2004) / OSF 预注册 / FAIR / NeurIPS 可复现研究标准, 产业链接遵循 Imperial MSc BA 咨询项目 (Burberry/Expedia/J&J) / HBS 案例法 / MIT Sloan 行动学习模式。linked_paper 锚定 Hevner 2004 (MIS Quarterly, JSTOR)、Peffers 2007 (JMIS)、March & Smith 1995 (DSS)、LaLonde 1986 (AER, NSW ATE=1794.34)。contribution 声明 4 条 delta-vs-prior-work (pydantic schema 化 / ArtifactType 枚举化 / 天道推演↔DSR 同构 / 4 条设计原则)。详见 research.md 与 industry.md。

---

## 学术前沿层 (v9.0)

本单元新增 `frontier.md`：注入 2025-2026 最新学术前沿（N 篇真实 arXiv 论文 + 批判性综述 + delta_to_unit + ≥3 开放研究问题 + 方法论批评）。论文来自 `_frontier_corpus/module-r-research-methodology.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证），覆盖前沿课题：LLM辅助系统综述 × 可复现性危机。面向博后/教授级读者：批判性综述非罗列，delta_to_unit 显式指出前沿如何更新本单元所教，开放问题为可发表研究方向。详见 `frontier.md`。
