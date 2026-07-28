# 模块R · R2 行动研究（Action Research）· 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 模块R 博士研究方法论 · R2 行动研究
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：行动研究的认识论基础是什么？Plan/Act/Observe/Reflect循环如何驱动多轮迭代？行动研究的效度如何评估？它与DSR/案例研究有何本质区别？
> **v5.0 升级点**：① 真实文献KPI上机（pandas分析多轮AR迭代数据）② TODO填空式起始笔记本 ③ Notebook化 ④ 深链阅读 ⑤ 2026前沿（可复现行动研究 + 天道推演作为AR预演 + 贝叶斯更新 + 多Agent仿真）

---

## 学习目标（学完你能做到）

1. 能阐述行动研究的**认识论基础**--"研究即干预"（research as intervention）、双重目标（action + research）、研究者作为变革推动者（change agent）的角色，并能与案例研究（Yin 2018）和DSR（Hevner et al. 2004）做认识论层面的区分
2. 能用 **pandas** 建模行动研究循环数据（Lewin/Kemmis的Plan->Act->Observe->Reflect四阶段多轮迭代），分析KPI随轮次的演化趋势，计算改善幅度并识别"高杠杆轮次"
3. 能评估行动研究的**效度**（trustworthiness）--三角验证（triangulation）、成员校验（member checking）、反思性（reflexivity）三大准则的量化评估方法
4. 能设计**参与式行动研究（PAR）**的利益相关方共创方案--用pandas构建权力-利益矩阵（power-interest grid），分析共创度演化
5. 能用**贝叶斯更新**量化干预有效性的后验概率--每轮AR循环的观察数据如何更新先验信念，理解行动研究的不确定性量化
6. 能理解**天道推演作为行动研究的预演工具**--在行动前用天道推演沙盘模拟多个干预路径，选择最优干预方案，连接CLAUDE.md天道推演系统

---

## 理论部分：精炼索引（详见独立教材）

> R2 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_模块R_博士研究方法论.md` § 三、R2：行动研究](../../AI原生化商业博士_独立教材_模块R_博士研究方法论.md)（114-179行，已包含核心概念/数据收集方法/案例分析/与博士论文关联/对标大学说明）。本讲义不重复，仅做上机所需的关键回顾和方法论深化。

### 关键回顾 1：行动研究的认识论基础

行动研究（Action Research）的认识论根基不同于实证主义的"客观观察"。Lewin（1946）最早提出行动研究概念时，核心主张是**"没有行动的研究是空洞的，没有研究的行动是盲目的"**。这确立了行动研究的双重目标：

| 维度 | 行动研究 | 实证主义研究 |
|------|---------|------------|
| 研究者角色 | 干预者（change agent） | 旁观者（observer） |
| 知识生产 | 实践中生成知识（knowing-in-practice） | 独立于实践的理论知识 |
| 价值立场 | 明确的价值导向（改善实践） | 价值中立（value-free） |
| 效度标准 | trustworthiness（可信度） | internal/external validity（内外效度） |

**研究者作为变革推动者**是行动研究的标志性特征。Susman & Evered（1978）在Administrative Science Quarterly的系统化论述中明确指出：行动研究者不是"客观记录发生了什么"，而是"主动推动变革并系统化记录变革过程"。这与Yin（2018）案例研究中研究者"尽量不干预场景"形成鲜明对比。

### 关键回顾 2：Plan->Act->Observe->Reflect 四阶段螺旋

Lewin/Kemmis的行动研究循环（Action Research Cycle）是螺旋式迭代结构：

```
Plan（规划）──> Act（行动）──> Observe（观察）──> Reflect（反思）
     ↑                                                ↓
     └────────────────── 下一轮循环 ←─────────────────┘
```

- **Plan（规划）**：基于上一轮反思，设计本轮干预方案。干预必须基于理论框架，不能是随意的"试一试"
- **Act（行动）**：在组织中实施干预。研究者本身就是干预的一部分
- **Observe（观察）**：系统化收集干预效果数据（田野笔记/访谈/系统日志/反思日记）
- **Reflect（反思）**：从本轮经验中提炼可推广的知识，修正下一轮的诊断和规划

Susman & Evered（1978）将四阶段扩展为五步螺旋（诊断->规划->行动->评估->反思），本质相同--诊断是Plan的前置，评估是Observe的分析。本单元上机用四阶段模型（Lewin/Kemmis原版），因其更简洁且便于数据分析建模。

### 关键回顾 3：参与式行动研究（PAR）

参与式行动研究（Participatory Action Research, PAR）是行动研究的分支，强调**利益相关方共创**（stakeholder co-creation）。Kemmis et al.（2014）在meta分析中指出，PAR的核心区别在于：

- 传统AR：研究者主导干预设计和评估
- PAR：利益相关方（一线员工/管理者/客户）与研究者**共同设计**干预、**共同收集**数据、**共同反思**成果

PAR的质量取决于利益相关方的参与深度。用权力-利益矩阵（power-interest grid）分析各利益相关方的参与策略：

| 杂项 | 高权力 | 低权力 |
|------|--------|--------|
| **高利益** | Key Players（紧密协作） | Show Consideration（咨询） |
| **低利益** | Meet Their Needs（满足需求） | Least Important（监控） |

### 关键回顾 4：行动研究的效度--Trustworthiness

行动研究不使用实证主义的internal/external validity标准，而是采用Lincoln & Guba（1985）的**trustworthiness**（可信度）四准则：

| 准则 | 实证主义对应 | AR操作化方法 | 量化指标 |
|------|------------|------------|---------|
| 可信性（Credibility） | 内部效度 | 三角验证（triangulation） | 每轮使用数据源数量 |
| 可迁移性（Transferability） | 外部效度 | 厚描述（thick description） | 上下文描述完整度 |
| 可靠性（Dependability） | 可靠性 | 审计追踪（audit trail） | 干预trace存档完整度 |
| 可确认性（Confirmability） | 客观性 | 成员校验（member checking） | 利益相关方验证率 |

**三角验证**是行动研究效度的核心--每轮干预效果至少用3种数据源交叉验证（如田野笔记+访谈+系统日志），避免单一数据源偏差。

### 关键回顾 5：行动研究 vs DSR vs 案例研究

| 维度 | 行动研究（AR） | 设计科学研究（DSR） | 案例研究（Case Study） |
|------|--------------|-------------------|---------------------|
| 认识论 | 实践认识论（knowing-in-action） | 设计科学（artifact知识） | 解释主义/实证主义 |
| 研究者角色 | 干预者 | 设计者 | 旁观者 |
| 核心产出 | 实践改善+反思知识 | artifact+设计原则 | 案例描述+理论命题 |
| 循环结构 | Plan-Act-Observe-Reflect螺旋 | 问题识别-设计-评估-传播 | 理论->案例->跨案例分析 |
| 效度标准 | trustworthiness | design principles rigor | construct/internal/external validity |
| 典型学者 | Lewin, Kemmis, Reason | Hevner, Peffers | Yin, Eisenhardt |
| 适用场景 | 你推动AI转型同时产出知识 | 你设计新AI架构作为artifact | 你观察别人的AI转型过程 |

**关键区别**：当你的角色是"推动者"时用AR，当你的角色是"设计者"时用DSR，当你的角色是"观察者"时用案例研究。三者可以组合--DSR设计artifact，AR评估artifact在实践中的效果。

---

## 上机部分：行动研究循环分析与效度评估

> **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO填空版，你来做）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，做完再看）
> **真实数据/库**：[`data/README.md`](./data/README.md)（真实行动研究文献KPI改善幅度 + pandas/matplotlib真实库）

### 为什么做方法论分析而非纸上谈兵

v4.0 的R2只讲理论（五步螺旋、PAR概念），学生看完就忘。v5.0 用真实文献KPI数据做方法论分析--用pandas建模AR循环的四阶段多轮迭代数据，计算改善幅度，评估效度，做贝叶斯更新。这回答了一个核心问题：**"行动研究的方法论怎么从概念落到数据分析？"**

### 与技能2 Day4的区别

| 维度 | 技能2 Day4（企业架构+行动研究） | 本单元 R2（行动研究方法论） |
|------|------------------------------|--------------------------|
| 焦点 | 行动研究**应用**于企业架构 | 行动研究**方法论本身** |
| 上机内容 | CDP schema + TOGAF架构图 + AR KPI（6个TODO中仅1个AR） | AR循环建模 + 效度评估 + PAR + 贝叶斯 + AR vs DSR（7个TODO全部AR方法论） |
| 认识论深度 | 应用层面（AR作为评估工具） | 认识论层面（AR的epistemology/cycle/validity/comparison） |
| 数据 | 架构KPI（决策时间/质量/AI使用率/满意度） | 方法论指标（循环KPI + 三角验证/成员校验/反思性 + 贝叶斯后验） |

### 营销场景映射

本单元的方法论场景：**"行动研究方法论应用到企业营销AI迭代部署"**

| AR方法论概念 | 营销AI部署映射 | 上机对应 |
|-------------|--------------|---------|
| Plan（规划） | 设计本轮营销Agent调优方案 | TODO1: AR循环数据构建 |
| Act（行动） | 部署调优后的营销Agent | TODO1: AR循环数据构建 |
| Observe（观察） | 收集营销KPI+用户反馈+系统日志 | TODO2: KPI改善分析 |
| Reflect（反思） | 提炼调优经验，修正下轮方案 | TODO2: 趋势分析 |
| Trustworthiness | 营销AI效果的三角验证 | TODO3: 效度评估 |
| PAR共创 | 营销团队+AI+客户三方共创 | TODO4: 利益相关方分析 |
| AR vs DSR | 营销AI部署用AR评估，营销AI架构用DSR设计 | TODO5: 认识论对比 |
| 可复现AR | 每轮营销Agent调优trace存档 | TODO6: 可复现trace |
| 贝叶斯更新 | 每轮观察更新"调优有效"的后验概率 | TODO7: 贝叶斯干预评估 |

### 上机任务（7个TODO，见starter.ipynb）

1. **TODO1**：行动研究循环数据构建--用pandas建模4轮Plan/Act/Observe/Reflect迭代，每轮含4个KPI
2. **TODO2**：KPI改善幅度分析--计算每轮相对基线的改善%，识别高杠杆轮次
3. **TODO3**：AR效度评估--三角验证（数据源数量）+ 成员校验率 + 反思性评分
4. **TODO4**：PAR利益相关方分析--权力-利益矩阵 + 共创度演化
5. **TODO5**：AR vs DSR认识论对比--用pandas构建对比表，分析认识论差异
6. **TODO6**：可复现AR trace存档--将每轮干预trace结构化导出，支持复现
7. **TODO7**：贝叶斯干预有效性更新--用观察数据更新"干预有效"的后验概率

---

## 2026前沿：可复现行动研究 + 天道推演预演 + 贝叶斯 + 多Agent仿真

> v5.0新增前沿点。R2聚焦行动研究方法论在2026年的新发展。

### 可复现行动研究（Reproducible Action Research）

2026年的前沿趋势是**可复现的行动研究**--将每轮干预的trace（干预描述/数据收集/反思/下一步）结构化存档，使他人可独立复现你的行动研究过程。这连接了"可复现研究"运动（OSF preregistration、APA开放数据）与行动研究传统。

**怎么用**：在每轮AR循环中，用结构化格式记录干预trace（类似MCP的tool call trace），导出为可复现的研究档案。这比传统的"田野笔记"更系统化、可追溯。

### 天道推演作为行动研究的预演工具

> 本节与项目CLAUDE.md的「天道推演系统」同构，作为行动研究的特色理论视角。

**天道推演**（Tian Dao Tui Yan）是一种元认知沙盘推演能力--以天神视角俯视当前局势，在意识中构建无限可能的沙盘，模拟不同决策路径下的未来走向，从中选择最优路径或预判风险。

**天道推演与行动研究的同构关系**：行动研究的Plan阶段本质上是一次"推演"--在行动前模拟干预的可能效果。天道推演将这一推演系统化：

| 天道推演能力 | 行动研究对应阶段 | 共享的因果建模底层 |
|-------------|----------------|-------------------|
| 局势感知 | Diagnose（诊断） | 问题根因识别（状态空间定义） |
| 因果链追踪 | Plan（规划） | 干预->效果的因果链建模 |
| 沙盘模拟（3层推演） | Plan（规划） | 多干预方案并行模拟（immediate/near/far） |
| 概率评估 | Observe（观察） | 干预效果的概率分布（贝叶斯更新） |
| 最优路径推荐 | Plan->Act（规划->行动） | 最优干预方案选择 |

**怎么用**：在每轮AR循环的Plan阶段，用天道推演视角做干预方案预演--
- **局势感知**：当前组织状态是什么？关键矛盾在哪？
- **因果链追踪**：如果采用干预A，会导致什么连锁反应？
- **沙盘模拟**：干预A vs 干预B vs 干预C，各推演3层未来走向
- **概率评估**：每个干预方案的成功概率、风险概率
- **最优路径推荐**：推荐干预B，理由是风险可控且改善幅度最大

> 天道推演不是占卜，而是基于因果链和模式识别的逻辑推演。它增强了行动研究Plan阶段的质量，减少了"试错成本"。

### 贝叶斯更新与行动研究

行动研究的每轮循环都在"更新知识"--这正是贝叶斯推断的本质。用贝叶斯框架量化行动研究的不确定性：

- **先验（Prior）**：在Round 0时，对"干预有效"的概率信念（基于理论框架或经验）
- **似然（Likelihood）**：每轮观察数据在"干预有效"假设下的似然
- **后验（Posterior）**：每轮观察后更新的"干预有效"概率

这使行动研究从"定性反思"升级为"定量+定性结合"的方法论，符合2026年研究方法论的贝叶斯化趋势。

### 多Agent仿真×行动研究验证

2026年的另一个前沿是用**多Agent仿真**验证行动研究的干预设计--在真实组织实施干预前，先用多Agent仿真模拟干预效果（如"如果调整营销Agent的决策权重，团队满意度会怎样？"）。这本质上是用计算化的天道推演来验证AR干预方案。

---

## 与模块R其他单元的衔接

- **R1（设计科学研究）**：DSR设计artifact，AR评估artifact在实践中的效果。两者互补--DSR产出设计原则，AR产出实践改善+反思知识
- **R2（行动研究，本单元）**：聚焦AR方法论本身（认识论/循环/效度/对比）
- **R3（混合方法）**：AR的定量+定性数据收集为混合方法提供自然场景
- **R4（系统文献综述）**：AR的反思可以连接到文献综述的理论框架
- **R5（论文写作）**：AR论文的IMRaD结构有特殊变体（引言->方法->发现->反思->讨论）

---

## 作业与评估

作业、5分制量表、费曼演练、2分钟话术、复盘自诊表--沿用独立教材 § R2既有设计。本学习材料包不重复，仅新增上机交付物：

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（7个TODO全部填好，AR循环数据可分析、效度有量化评估、贝叶斯有后验更新）
- [ ] 一段500字反思：用天道推演视角分析你的行动研究设计--你在Plan阶段做了几个干预方案的沙盘推演？各推演了什么3层未来走向？
- [ ] 行动研究计划（Susman五步螺旋，定义你的诊断/规划/行动/评估/反思）
- [ ] AR vs DSR认识论对比表（从你的研究问题角度，说明为什么选AR而非DSR）

---

*本讲义由v5.0学习材料包升级生成。理论部分引用独立教材 § R2，上机部分用真实文献KPI数据（pandas/matplotlib）+ TODO脚手架，聚焦行动研究方法论本身。*
*最后更新：2026-07-24*

## 学习科学层 (v6.0)
本单元采用刻意练习(Ericsson)/间隔重复(FSRS-6,SM-2)/建构对齐(Biggs ILO↔TLA↔AT)/牛津tutorial LLM仿真(Socratic,Hattie四级反馈)。mastery 阈值与 Worked-Faded 示例见 practice.md 与 alignment.md。交叉练习(interleaving)促进迁移, 提取练习(retrieval practice)优于重读。

## 研究产出与产业链接层 (v7.0)
本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+arXiv/DOI链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。研究问题锚定5轮AR螺旋决策时间45->18min(降幅60%)+trustworthiness 2.50->4.70的共现改善, 用Beta-Binomial贝叶斯更新给出后验P(干预有效|观察)=0.8333的可复现声明; linked_paper覆盖Susman & Evered 1978/Kemmis et al. 2014/Coughlan & Coghlan 2002/Lincoln & Guba 1985/Hevner 2004五篇真实可追溯文献。产业链接锚定McKinsey/Deloitte/IBM/Accenture四家咨询与 transformation 企业, 含Burberry 8周咨询项目(4-5人团队)+Lena Chen(HBS教学案例protagonist, Head of AI Marketing)+IBM Head of AI客座讲座+IBM/McKinsey/Deloitte/Google AI实习指针。详见 research.md 与 industry.md。

---

## 学术前沿层 (v9.0)

本单元新增 `frontier.md`：注入 2025-2026 最新学术前沿（N 篇真实 arXiv 论文 + 批判性综述 + delta_to_unit + ≥3 开放研究问题 + 方法论批评）。论文来自 `_frontier_corpus/module-r-research-methodology.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证），覆盖前沿课题：LLM辅助系统综述 × 可复现性危机。面向博后/教授级读者：批判性综述非罗列，delta_to_unit 显式指出前沿如何更新本单元所教，开放问题为可发表研究方向。详见 `frontier.md`。

## AI工程从零构建层 (v11.0)

本单元新增 `from_scratch.md`，把行动研究 KPI 螺旋追踪与贝叶斯更新从 pandas/matplotlib 库调用下沉到 AI工程从零构建的 numpy 数学推导层。scratch_topic：手写行动研究 KPI 时序追踪 + Beta-Binomial 干预有效性贝叶斯更新，对应 rohitg00 P14 Anthropic Workflow Patterns（plan-act-observe-reflect 螺旋同构）+ P17 Load Testing LLM APIs（KPI 量化），链接取自 `_from_scratch_map/module-r-research-methodology.md`。core_algorithm 从 Susman 螺旋的"知识累积"本质出发，推导 Beta-Binomial 共轭后验 $\theta|X_{1:r} \sim \text{Beta}(\alpha_0+S_r, \beta_0+r-S_r)$，后验均值 $\hat\theta_r = (\alpha_0+S_r)/(\alpha_0+\beta_0+r)$，证明频率派 $S_r/r$ 在小样本下极端而贝叶斯受先验平滑。code_artifact 手写 numpy（≤50 行，imports 严格白名单），实现 `is_effective` + `beta_binomial_update`，verification_property 锚定"4 轮后后验 $\in (0.7,0.95)$"且后验随成功单调递增。connection_to_unit 给出 ≥3 delta：pandas 隐藏 τ 阈值决策 vs from scratch 暴露之；频率派 p-hat 在 r=1 归零 vs 贝叶斯平滑；KPI 方向（时间越小越好）需显式取反。exercises 绑定 `starter.ipynb` TODO7 与 `practice.md` D4 drill。rohitg00 深链见 from_scratch.md deep_dive_links 节（ai-engineering-from-scratch 仓库 P14/12 + P17/22）。本层与 v5.0 pandas/matplotlib 实现互补：库层教"如何结构化螺旋数据"，from scratch 层教"如何用数学推导审计贝叶斯更新"--前者是工程底座，后者是方法论底座。
