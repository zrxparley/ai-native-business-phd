# 技能2 · Day 4：企业级架构参考设计 + 行动研究 · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 技能2 AI原生企业架构 · Day 4（收官）
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：企业AI架构的参考模型是什么？如何用CDP+Agent+治理构建营销中心AI原生架构？如何用行动研究记录AI部署对组织的影响？
> **v5.0 升级点**：① 真实架构框架上机（pydantic CDP schema + TOGAF/ArchiMate + networkx架构图）② TODO填空式起始笔记本 ③ Notebook化 ④ 深链阅读 ⑤ 2026前沿（天道推演×企业架构 + 多Agent仿真 + DSR + 可复现研究）

---

## 学习目标（学完你能做到）

1. 能用 **pydantic** 设计CDP（客户数据平台）核心schema--身份(Identity)/事件(Event)/分群(Segment)/画像(Profile)四层，基于真实公开规范（Segment Spec），理解CDP在AI原生架构中作为"AI数据基础设施"的角色
2. 能用 **TOGAF/ArchiMate** 企业架构框架 + **networkx** 建模企业AI架构四层（业务/应用/数据/技术），输出架构依赖图并分析组件间的耦合关系，识别架构设计中的关键依赖路径
3. 能用 **pandas** 分析行动研究（Action Research）的迭代循环数据（Plan/Act/Observe/Reflect四阶段的多轮KPI），理解"研究即干预"的行动研究哲学，掌握Susman & Evered (1978) 五步螺旋方法
4. 能把Day1-3的治理/编排/人机协调整合为**企业级营销中心AI原生参考架构**，并用DSR（设计科学研究）框架将其定位为可发表的研究artifact
5. 能理解**天道推演×企业架构**的同构关系：企业架构设计本质上是对组织的沙盘推演--在意识中构建多个架构方案的平行世界，模拟其未来走向，选择最优路径

---

## 理论部分：精炼索引（详见独立教材）

> Day 4 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_技能2_AI原生企业架构.md` § Day 4](../../AI原生化商业博士_独立教材_技能2_AI原生企业架构.md)（1395-1794行，已包含企业AI架构参考模型/CDP+AI+Agent营销架构/AWS-Azure-GCP对比/行动研究实践）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：企业AI架构四层参考模型

企业AI架构不是单一系统，而是分层的架构体系。参考NIST AI RMF的治理维度和主流云厂商的架构设计，分为四层：

```
┌───────────────────────────────────────────────┐
│            治理层 (Governance Layer)             │
│  AI治理委员会 | 伦理审查 | 合规审计 | 风险管理    │
├───────────────────────────────────────────────┤
│            应用层 (Application Layer)            │
│  Agent工作流 | 人机协作界面 | API网关 | 业务集成  │
├───────────────────────────────────────────────┤
│            模型层 (Model Layer)                  │
│  基础模型 | 领域微调 | 模型路由 | 推理服务        │
├───────────────────────────────────────────────┤
│            数据层 (Data Layer)                   │
│  数据湖 | 向量数据库 | 知识图谱 | 数据流水线      │
└───────────────────────────────────────────────┘
```

这四层不是割裂的--治理层贯穿所有层级，数据层是地基，模型层是引擎，应用层是业务出口。用TOGAF/ArchiMate框架可以系统化地建模这四层的依赖关系。

### 关键回顾 2：CDP在AI原生架构中的角色

传统CDP（如Twilio Segment、Adobe Real-Time CDP）主要做用户数据的收集、整合和激活。在AI原生架构中，CDP的角色升级为"AI的数据基础设施"：

1. **用户画像向量化**：不仅存储结构化标签，还存储向量表示（Embedding），支持语义匹配
2. **实时行为流**：实时采集用户行为，通过流处理（Kafka + Flink）实时更新画像
3. **知识图谱集成**：用户/产品/内容/渠道构建为知识图谱，支持GraphRAG
4. **AI激活层**：Agent通过CDP的API获取数据、更新画像、触发营销动作

CDP的schema设计基于真实公开规范--Segment Spec（https://segment.com/docs/spec/）定义了Identify/Track/Page/Screen等标准事件，是CDP数据模型的行业事实标准。

### 关键回顾 3：行动研究五步螺旋（Susman & Evered 1978）

行动研究的核心产出不是一份报告，而是一个"实践-反思-改进"的循环记录：

```
诊断(Diagnose) → 规划(Plan) → 行动(Act) → 评估(Evaluate) → 反思(Reflect)
     ↑                                                        ↓
     └────────────────── 下一轮循环 ←─────────────────────────┘
```

- **诊断**：当前营销决策流程是什么？AI扮演什么角色？
- **规划**：计划部署什么AI系统？预期如何改变决策流程？
- **行动**：AI系统部署的实际过程，发生了什么？
- **评估**：部署后决策流程发生了什么变化？效果如何？
- **反思**：从这次行动研究中学到什么？下一步怎么改进？

行动研究的关键洞察是**"研究即干预"**（research as intervention）--研究者不是旁观者，而是变革的参与者。这与DSR的artifact设计理念高度契合。

### 关键回顾 4：TOGAF / ArchiMate 企业架构框架

**TOGAF**（The Open Group Architecture Framework）是真实的企业架构方法论，定义了架构开发方法（ADM）和四层架构域：

| TOGAF架构域 | 内容 | 对应AI原生架构 |
|-------------|------|---------------|
| 业务架构 (Business) | 业务流程/角色/组织 | 营销流程/Agent角色/人机协作 |
| 应用架构 (Application) | 应用系统及其关系 | Agent编排/RAG/API网关 |
| 数据架构 (Data) | 数据实体及流向 | CDP/向量库/知识图谱 |
| 技术架构 (Technology) | 基础设施/平台 | 云服务/推理服务/可观测性 |

**ArchiMate**是TOGAF配套的架构建模语言（类似UML但专用于企业架构），定义了业务层/应用层/技术层的标准符号和关系类型。

---

## 上机部分：CDP schema + 架构依赖图 + 行动研究分析

> **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO填空版，你来做）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，做完再看）
> **真实数据/库**：[`data/README.md`](./data/README.md)（Segment Spec + 行动研究文献KPI + pydantic/networkx/matplotlib/pandas）

### 为什么做架构设计而非纸上谈兵

v4.0 的Day 4只讲理论（四层架构图、三朵云对比），学生看完就忘。v5.0 用真实库做架构设计--用pydantic定义CDP schema（对标Twilio Segment的真实数据模型），用networkx建模架构依赖关系（对标TOGAF/ArchiMate的架构建模），用pandas分析行动研究迭代数据（对标真实行动研究文献的KPI追踪）。这回答了一个核心问题：**"企业AI架构怎么从PPT落到代码？"**

### 营销场景映射

本Day的架构场景：**"为企业营销中心设计AI原生参考架构"**

| 架构层 | 真实库/框架 | 营销映射 | 产出 |
|--------|-----------|---------|------|
| 数据层 | pydantic + Segment Spec | CDP schema设计（Identity/Event/Segment/Profile） | 可实例化的CDP数据模型 |
| 应用层 | networkx + TOGAF/ArchiMate | Agent编排依赖图 | 架构依赖图（节点/边/路径） |
| 治理层 | 概念模型 + networkx | 人机协作治理节点 | 治理依赖分析 |
| 行动研究 | pandas | Plan/Act/Observe/Reflect迭代KPI | KPI趋势分析 + 改善幅度 |
| 整合 | 全部整合 | 营销中心AI原生参考架构 | ASCII架构图 + DSR artifact |

### 营销中心AI原生参考架构

把Day1（架构基础）+ Day2（Agent编排）+ Day3（人机协作治理）整合为企业级参考架构：

```
┌──────────────────────────────────────────────────────────────┐
│                    营销中心 AI原生参考架构                      │
├──────────────────────────────────────────────────────────────┤
│  治理层                                                        │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐        │
│  │ 伦理审查  │ │ 合规审计  │ │ 公平性监测│ │ 人机协作  │        │
│  │ 委员会    │ │ 系统      │ │          │ │ 治理(Day3)│        │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘        │
├──────────────────────────────────────────────────────────────┤
│  应用层（Agent编排 Day2）                                       │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐            │
│  │洞察Agent│ │内容Agent│ │投放Agent│ │分析Agent│            │
│  └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘            │
│       └───────────┴───────────┴───────────┘                 │
│                  协调Agent (Supervisor)                       │
│         人机协作界面 (Human-in-the-loop)                       │
├──────────────────────────────────────────────────────────────┤
│  模型层                                                        │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐        │
│  │ LLM服务   │ │ RAG引擎  │ │推荐引擎   │ │模型路由   │        │
│  │(GPT-4o/  │ │(GraphRAG)│ │(Two-Tower)│ │          │        │
│  │ Claude)  │ │          │ │          │ │          │        │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘        │
├──────────────────────────────────────────────────────────────┤
│  数据层（CDP核心 Day1）                                         │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐        │
│  │ 身份层    │ │ 事件层    │ │ 分群层    │ │ 画像层    │        │
│  │(Identity)│ │(Event)   │ │(Segment) │ │(Profile) │        │
│  │ Segment  │ │ Segment  │ │ CDP分群  │ │ 向量化   │        │
│  │ Spec     │ │ Spec     │ │          │ │ 画像     │        │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘        │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐                    │
│  │ 向量数据库│ │ 知识图谱  │ │ 数据流水线│                    │
│  │(pgvector)│ │(Neo4j)   │ │(Airflow) │                    │
│  └──────────┘ └──────────┘ └──────────┘                    │
├──────────────────────────────────────────────────────────────┤
│  行动研究层（持续迭代）                                         │
│  诊断 → 规划 → 行动 → 评估 → 反思 → 下一轮                     │
│  每轮KPI追踪：决策时间/决策质量/团队满意度/AI使用率              │
└──────────────────────────────────────────────────────────────┘
```

### 上机任务（6个TODO，见starter.ipynb）

1. **TODO1**：CDP身份层设计--用pydantic设计Identity模型（对标Segment Identify Spec）
2. **TODO2**：CDP事件层设计--用pydantic设计Event模型（对标Segment Track Spec）
3. **TODO3**：CDP分群层+画像层设计--用pydantic设计Segment和Profile模型
4. **TODO4**：企业架构依赖图--用networkx+TOGAF四层建模，输出节点/边/关键路径
5. **TODO5**：CDP数据流图可视化--用networkx+matplotlib画数据流图
6. **TODO6**：行动研究迭代分析--用pandas分析Plan/Act/Observe/Reflect多轮KPI，计算改善幅度

---

## 2026前沿：天道推演×企业架构 + DSR + 可复现研究

> v5.0新增前沿点。Day 4作为技能2收官，聚焦三个前沿方向。

### 天道推演×企业架构（特色章节）

> 本节与项目CLAUDE.md的「天道推演系统」同构，作为企业架构设计的特色理论视角。

**天道推演**（Tian Dao Tui Yan）是一种元认知沙盘推演能力--以天神视角俯视当前局势，在意识中构建无限可能的沙盘，模拟不同决策路径下的未来走向，从中选择最优路径或预判风险。它不是占卜，而是基于因果链和模式识别的逻辑推演。

**企业架构设计本质上就是对组织的沙盘推演**--架构师在天道推演的视角下，构建多个架构方案的平行世界（数据层集中式 vs 分布式？Agent编排用LangGraph还是Bedrock Agents？治理层前置还是后置？），模拟每种方案在未来3年的走向（扩展性/成本/合规风险/团队接受度），从中选择最优路径。

**天道推演能力与企业架构设计的同构映射**：

| 天道推演能力 | 企业架构设计对应 | 共享的因果建模底层 |
|-------------|----------------|-------------------|
| **局势感知** | 现有架构审计 + 业务需求分析 | 状态空间定义（当前架构的as-is状态） |
| **因果链追踪** | 架构依赖图分析（组件间因果依赖） | 因果有向图（networkx DAG） |
| **沙盘模拟（3层推演）** | 多架构方案并行模拟（immediate/near/far） | 并行世界树（TOGAF场景规划） |
| **概率评估** | 架构方案的风险/成本/收益概率分布 | 贝叶斯推断（架构决策的不确定性量化） |
| **最优路径推荐** | 架构选型建议（2-3个差异化策略选项） | 收益/风险/成本权衡 |

**怎么用**：在设计营销中心AI原生架构时，用天道推演视角做架构选型--
- **局势感知**：当前营销系统的数据孤岛在哪？Agent编排能力如何？治理成熟度如何？
- **因果链追踪**：如果CDP schema设计不好，会导致什么连锁反应？（数据质量差→画像不准→Agent决策错误→营销效果差→团队失去信心）
- **沙盘模拟**：方案A（全云托管）vs 方案B（混合架构）vs 方案C（全自建），各推演3层未来走向
- **概率评估**：每个方案的成功概率、风险概率、成本分布
- **最优路径推荐**：推荐方案B（混合架构），理由是避免了厂商锁定同时利用云规模效应

> ⚠️ 天道推演不是占卜，而是基于因果链和模式识别的逻辑推演。与TOGAF的架构开发方法（ADM）互补：TOGAF提供方法论流程，天道推演提供思维质量。

### 多Agent仿真×架构验证

2026年的前沿趋势是用**多Agent仿真**来验证企业架构设计--在部署真实系统前，先用多Agent仿真模拟架构的运行情况：Agent之间的消息传递延迟、资源竞争、故障传播路径。这本质上是用计算化的天道推演来验证架构设计的合理性。

**怎么用**：在本Day的架构依赖图基础上，可以用多Agent仿真模拟"如果洞察Agent故障，整个营销中心会怎样？"--这比纸面分析的"单点故障"更真实。

### DSR + 可复现研究

企业架构设计作为DSR artifact，行动研究作为评估方法：

- **DSR**（Hevner et al. 2004; Peffers et al. 2007）：你的营销中心AI原生架构就是一个可发表的artifact，架构设计原则（CDP四层schema/Agent编排模式/治理嵌入点）是DSR的知识贡献
- **可复现研究**：架构依赖图（networkx）+ CDP schema（pydantic）+ 行动研究KPI数据（pandas）全部用代码定义，他人可独立复现你的架构设计和评估结果
- **行动研究作为DSR评估**：Susman & Evered的五步螺旋对应DSR的"演示→评估"步骤--你不是在做完架构就停，而是持续用行动研究循环评估和改进

---

## 与前序Day的衔接

- **Day 1**（AI原生架构基础）：今天把Day1的四层架构模型用代码建模（networkx DAG）
- **Day 2**（Agent编排LangGraph）：今天的营销中心架构把Day2的Agent编排整合为应用层
- **Day 3**（人机协作治理）：今天的治理层纳入Day3的人机协作治理设计
- **Day 4**（收官）：整合Day1-3为企业级参考架构 + 行动研究持续迭代

---

## 作业与评估

作业、5分制量表、费曼演练、2分钟话术、复盘自诊表--沿用独立教材 § Day 4既有设计。本学习材料包不重复，仅新增上机交付物：

**新增交付物（v5.0 收官）**：
- [ ] 完成的 `starter.ipynb`（6个TODO全部填好，CDP schema可实例化、架构图有节点/边、行动研究KPI有改善幅度）
- [ ] 营销中心AI原生参考架构图（ASCII或文字描述，整合Day1-3）
- [ ] 一段500字反思：用天道推演视角分析你的架构设计--你在哪一步做了沙盘推演？推演了几个方案？
- [ ] 行动研究计划（Susman五步螺旋，定义你的诊断/规划/行动/评估/反思）

---

*本讲义由v5.0学习材料包升级生成。理论部分引用独立教材，上机部分用真实库（pydantic+networkx+matplotlib+pandas）+ TODO脚手架，整合Day1-3为企业级参考架构。*
*最后更新：2026-07-24*

---

## 学习科学层 (v6.0)

> v6.0 哲学增量: **科学即高效 · 反馈即成长** -- 用学习科学把 v5.0 的"练习"升级为"刻意练习 + 间隔重复 + 建构对齐 + 牛津 tutorial 仿真"。
> 本节为 v5.0 基线之上的最小注入, 不改动原文。4 个新文件: `practice.md` / `schedule.json` / `alignment.md` / `tutorial.ipynb`。

### 1. 刻意练习 (Ericsson Deliberate Practice)

本单元的 6 个 TODO 上机任务, 在 v6.0 升级为 3 个刻意练习 drill (D1/D2/D3), 每 drill 含:
- **difficulty** (1-5) + **reps_required** (>=3 次) + **feedback_rule** (失败时引用 Segment Spec / TOGAF ADM / Susman & Evered 1978 / 天道推演)
- **worked-faded 三阶段渐退示例** (Worked Example -> Faded -> 独立解): 完整示范 -> 部分填空 -> 独立解, 对应 MIT 4C/ID 认知负荷理论
- **weak_loop**: 连续 2 次失败触发弱项循环 (回退 + 重做 worked example + 天道推演因果链反思)

详见 `practice.md`。

### 2. 间隔重复 (FSRS-6 / SM-2 Spaced Retrieval)

5 个核心概念用 FSRS-6 算法 (request_retention=0.9, 21 weights, SM-2 backup EF₀=2.5) 排程复习:
- C1: CDP 四层 schema (pydantic + Segment Spec)
- C2: TOGAF 四层架构域 networkx 依赖图 17 节点 27 边
- C3: 行动研究 Susman 五步螺旋 4 轮 KPI
- C4: 天道推演×企业架构同构映射
- C5: DSR artifact 可复现研究

间隔序列 `[1, 3, 8, 21, 60, 180]` 天 (FSRS-6 默认 retention=0.9 稳定化曲线)。详见 `schedule.json`。

### 3. 建构对齐 (Biggs Constructive Alignment)

ILO (预期学习产出) ↔ TLA (教学学习活动) ↔ AT (评估任务) 三者对齐, 配合 mastery_threshold (借鉴 MIT 6.5940 "至少 4/5 实验提交方可及格"):
- ILO1 (CDP schema) ↔ D1 + tutorial Socratic ↔ solution.ipynb 可实例化 ↔ 字段 100% 正确
- ILO2 (TOGAF 依赖图) ↔ D2 + tutorial ↔ 17 节点 27 边 + 关键路径 ↔ 四层分区正确
- ILO3 (行动研究 KPI) ↔ D3 + tutorial ↔ 改善幅度 + 霍桑排除 ↔ 误差 <5%
- ILO4 (天道推演) ↔ tutorial 第 4 轮 + 500 字反思 ↔ 3 层推演 + 2 方案

3 自检问题 (Hattie Feed Up/Back/Forward): TLA 是否训练 ILO? AT 是否测量 ILO? 不经 TLA 能过 AT 吗 (若能 = 对齐失败)? 详见 `alignment.md`。

### 4. 牛津 Tutorial LLM 仿真 (Socratic + Hattie 4 级反馈)

`tutorial.ipynb` 仿真牛津 tutorial (1 对 1, 强制, 口头辩护):
- **Persona**: Oxford fellow in 企业架构与行动研究, **never give direct answers**, Socratic questioning, devil's advocate
- **4 轮 Socratic 追问** (静态 if/else, 不调 API): CDP timestamp 类型 / TOGAF 关键路径因果链 / 行动研究 n=2 与霍桑效应 / 天道推演 3 层沙盘
- **Hattie (2007 RER 77(1):81-112) 四级 formative feedback**: [TASK] / [PROCESS] / [SELF-REG] / [FEED-FORWARD] (故意无 Self 级表扬, d=0.14 几乎无效)
- **student_model.json**: 跨单元复用, 记录 mastered_subskills + blind_spots
- **限频**: 每单元每天 1 次 (防依赖, 配合间隔重复)

### 5. 研究依据 (4 agent 调研合成)

- **Ericsson**: 刻意练习 5 要素 (specific goal / feedback / repetition / difficulty / scaffold)
- **FSRS-6**: request_retention=0.9, 21 weights; SM-2 backup EF₀=2.5
- **Biggs (1996)**: Constructive Alignment ILO↔TLA↔AT
- **Hattie & Timperley (2007)**: The Power of Feedback, RER 77(1):81-112
- **Butler (2010)**: retrieval practice 推断题 68% vs 重学 44%
- **MIT Open Learning**: interleaving (A1B1C1...B2C2A2...C3A3B3) + worked-faded + 4C/ID
- **Oxford tutorial**: 1 对 1-3, 每周, 强制, 口头辩护; Vygotsky (1978) 共构式对话
- **Harvard HBS**: case method + devil's advocate (Christensen Center)
- **Stanford CS230**: retry policy (10 late days, 20%/天罚分)

---

*v6.0 学习科学层 · 刻意练习 + 间隔重复 + 建构对齐 + 牛津 tutorial 仿真 · 2026-07-25*

---

## 研究产出与产业链接层 (v7.0)

本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+arXiv链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。详见 research.md 与 industry.md。

*v7.0 研究产出与产业链接层 · IMRaD + DSR (Hevner 2004) + 可复现研究 (NeurIPS/ACM) + 行动研究 (Susman & Evered 1978) + Imperial MSc BA + HBS case · 2026-07-26*

---

## 学术前沿层 (v9.0)

本单元新增 `frontier.md`：注入 2025-2026 最新学术前沿（N 篇真实 arXiv 论文 + 批判性综述 + delta_to_unit + ≥3 开放研究问题 + 方法论批评）。论文来自 `_frontier_corpus/skill-2-ai-native-arch.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证），覆盖前沿课题：企业Agent编排 × MCP/A2A 标准化协议。面向博后/教授级读者：批判性综述非罗列，delta_to_unit 显式指出前沿如何更新本单元所教，开放问题为可发表研究方向。详见 `frontier.md`。

---

## AI工程从零构建层 (v11.0)

> v11.0 新增 [`from_scratch.md`](./from_scratch.md)：AI工程从零构建，与本单元 networkx DAG + pandas KPI 形成对照。
> - **从零构建主题**：手写 TOGAF 四层依赖图（拓扑排序 + 关键路径）+ 行动研究 KPI 改善幅度
> - **核心算法**：Kahn BFS 拓扑排序 + 最长加权路径 $\text{dist}(v) = \max_{(u,v)\in E}[\text{dist}(u)+w(v)]$ + KPI 改善 $\Delta_k = \frac{\text{KPI}(R)-\text{KPI}(0)}{\text{KPI}(0)}\times100\%$（含数学推导 + LaTeX）
> - **code_artifact**：手写 numpy 骨架，imports ⊆ {numpy, collections}，附 verification_property
> - **延伸阅读**：rohitg00 AI工程 from scratch P17 Infrastructure（Managed LLM Platforms）/ P14 Agent Engineering（Orchestration Patterns）
> - **手写实现要点**：用 from-scratch numpy + collections 而非 networkx topological_sort + pandas groupby，理解到 DAG 拓扑排序与关键路径 DP 的金属层
> - **verification_property**：拓扑序满足 DAG 依赖方向；关键路径 CP=7.0（CDP->Agent->Report）；KPI 改善 time=-40% / quality=+50%
