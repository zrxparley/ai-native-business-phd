# 技能5 · Day 7：端到端交付+Capstone整合 · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 技能5 Agentic系统工程与落地 · Day 7（收官）
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：把技能1-5整合为一个完整系统--从数据到因果到Agent到评估到论文，端到端跑通
> **v5.0 升级点**：① 端到端真实流水线（causaldata→DoWhy→LangGraph→deepeval→IMRaD）② TODO填空脚手架 ③ Notebook化 ④ 深链阅读 ⑤ 2026前沿（DSR设计科学研究+可复现研究+天道推演×多Agent仿真）

---

## 学习目标（学完你能做到）

1. 能用 **DSR六步框架**（Hevner et al. 2004; Peffers et al. 2007）规划Capstone：问题识别→目标定义→设计开发→演示→评估→传播，把工程实践转化为可发表的设计科学贡献
2. 能把**技能1-5整合为端到端流水线**：数据层（causaldata NSW真实RCT）→因果层（DoWhy估计ATE）→Agent层（LangGraph编排营销策略Agent）→评估层（deepeval + LLM-as-a-judge）→论文层（IMRaD草稿含DSR artifact描述）
3. 能用IMRaD结构写出3000-5000字的Capstone论文草稿，包含DSR artifact设计/评估/传播，并制定从草稿到学术发表（ICIS/Decision Support Systems/HICSS等）的路线图
4. 能理解**天道推演×多Agent仿真**的同构关系：天道推演的沙盘模拟（因果链追踪+多路径概率评估）与多Agent仿真（Agent交互+涌现行为预测）共享同一因果建模底层，可作为Capstone的特色理论视角

---

## 理论部分：精炼索引（详见独立教材）

> Day 7 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_技能5_Agentic系统工程与落地.md` § Day 7](../../AI原生化商业博士_独立教材_技能5_Agentic系统工程与落地.md)（3.7.1–3.7.4节，已包含Capstone整合/DSR回顾/论文写作工作坊/发表路线图）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：Capstone整合--技能1-5映射

Capstone是整个课程的最终交付物。Day 7是Capstone的启动点--将前五个技能整合为一个完整系统。

| 技能 | 对应能力 | 在Capstone中的角色 | 真实库/方法 |
|:----:|---------|-------------------|------------|
| 技能1 | 表示工程 | 客户/产品向量化表示（Agent的知识基础） | embeddings |
| 技能2 | 原生架构 | 系统架构设计（LangGraph图结构） | LangGraph StateGraph |
| 技能3 | 因果推断 | 营销效果因果评估（ATE估计） | DoWhy + causaldata(NSW) |
| 技能4 | 商业模式 | Agent经济下的价值捕获（商业模式画布） | 商业模式分析 |
| 技能5 | 系统工程 | 端到端构建+评估+部署+论文 | LangGraph+deepeval+langsmith |

**端到端流水线**：
```
数据层(causaldata NSW真实RCT)
  ↓ 定义 treatment/outcome/covariates
因果层(DoWhy估计ATE)
  ↓ "营销干预的因果效果是多少？"
Agent层(LangGraph编排营销策略Agent)
  ↓ Agent调用因果分析工具+生成策略
评估层(deepeval + LLM-as-a-judge)
  ↓ 评估Agent输出质量/幻觉/工具调用
论文层(IMRaD草稿 + DSR artifact描述)
  ↓ 可复现的研究贡献
```

### 关键回顾 2：DSR六步框架

**设计科学研究**（Design Science Research, DSR）是信息系统的核心研究范式之一。Hevner et al. (2004) 在MIS Quarterly发表的经典论文提出了DSR的七准则；Peffers et al. (2007) 进一步将其操作化为六步方法论。

```
Step 1: 问题识别 -- 企业营销面临什么问题？为什么现有方案不够好？
Step 2: 目标定义 -- artifact应该达到什么效果？（效率/质量/安全/可评估）
Step 3: 设计开发 -- 架构设计+Agent设计+安全设计+评估设计
Step 4: 演示     -- 在真实场景中运行系统，展示完整流程
Step 5: 评估     -- 定量(测试用例+A/B)+定性(访谈)+安全(红队)
Step 6: 传播     -- IMRaD论文草稿+开源代码+学术发表
```

**DSR vs 传统实证研究**：传统实证研究回答"是什么"（what is），DSR回答"如何构建有效的artifact"（how to build）。AI原生化系统天然适合DSR--你构建的Agent系统就是一个artifact，它的设计原则、评估方法、部署经验都是DSR的知识贡献。

### 关键回顾 3：论文草稿写作工作坊（IMRaD + DSR）

Day 7的核心活动是论文草稿写作。用IMRaD结构（Introduction/Methods/Results/Discussion），把Capstone写成一篇短论文：

| 章节 | 内容 | DSR映射 |
|------|------|---------|
| Introduction | 研究问题+贡献声明 | DSR Step 1: 问题识别 |
| Methods | 系统架构+评估方法 | DSR Step 3: 设计开发 |
| Results | 性能指标+A/B测试 | DSR Step 5: 评估 |
| Discussion | 发现解读+局限+未来 | DSR Step 6: 传播 |

**论文标题模板**：`[方法] for [问题]: A [框架] Approach`
**示例**：`Multi-Agent Marketing Intelligence: A LangGraph-Based Architecture with Causal Evaluation Framework`

### 关键回顾 4：学术发表路线图

| 级别 | 期刊/会议 | 领域 | 适合度 | 周期 |
|------|----------|------|:------:|:----:|
| 顶刊 | MIS Quarterly | 信息系统 | ⭐⭐⭐ | 6-12月 |
| 顶会 | ICIS | 信息系统 | ⭐⭐⭐⭐ | 6月 |
| 好刊 | Decision Support Systems | 决策支持 | ⭐⭐⭐⭐ | 4-6月 |
| 好刊 | Expert Systems with Applications | AI应用 | ⭐⭐⭐⭐ | 4-6月 |
| 会议 | HICSS | 信息系统 | ⭐⭐⭐⭐ | 6月 |

**投稿策略**：先投会议（反馈快）→ 改进后投期刊 → 开源代码增加可信度。

---

## 上机部分：端到端Capstone流水线

> 📓 **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO填空版，你来做）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，做完再看）
> 📊 **真实数据/库**：[`data/README.md`](./data/README.md)（causaldata NSW + DoWhy + LangGraph + deepeval）

### 为什么做端到端整合（而非孤立练习）

v4.0 的每天练习是孤立的（Day 3只做评估，Day 2只做LangGraph）。v5.0 的Day 7是**整合性Capstone**：用一个真实数据集（NSW职业培训实验），串起因果分析→Agent构建→评估→论文的完整流水线。这回答了一个核心问题：**"这五个技能怎么拼成一个完整系统？"**

### 营销场景映射

本Day的Capstone场景：**"为营销策略Agent系统做因果评估"**

| 流水线层 | 真实库 | NSW数据营销映射 | 产出 |
|---------|--------|----------------|------|
| 数据层 | causaldata | treat=营销干预, re78=转化率, re75=基线消费 | 干净的DataFrame |
| 因果层 | DoWhy | "营销干预对转化的因果效果(ATE)是多少？" | ATE估计+反事实 |
| Agent层 | LangGraph | Agent读取因果证据→生成营销策略 | 策略文本+工具轨迹 |
| 评估层 | deepeval | 评估Agent策略质量+工具调用正确性 | 评估指标 |
| 论文层 | IMRaD模板 | 把以上写成DSR artifact论文 | 论文草稿 |

### 上机任务（6个TODO，见starter.ipynb）

1. **TODO1**：DSR系统设计--用DSR六步框架定义Capstone的问题/artifact/评估/传播
2. **TODO2**：数据层--加载真实NSW数据，定义treatment/outcome/covariates，营销映射
3. **TODO3**：因果层--用DoWhy估计ATE，回答"营销干预的因果效果"
4. **TODO4**：Agent层--用LangGraph构建营销策略Agent（调用因果分析工具+生成策略）
5. **TODO5**：评估层--用deepeval评估Agent输出质量（自定义BaseMetric+GEval LLM-as-a-judge）
6. **TODO6**：论文草稿--用IMRaD结构+DSR artifact描述，把Capstone写成短论文草稿

---

## 2026前沿：DSR + 可复现研究 + 天道推演×多Agent仿真

> v5.0新增前沿点。Day 7作为收官，聚焦三个前沿方向。

### DSR（设计科学研究）在AI系统设计中的应用

DSR（Hevner et al. 2004, MIS Quarterly）是信息系统的经典研究范式，但在AI原生系统时代获得新生命：Agent系统本身就是一个artifact，它的架构模式、评估框架、安全实践都是可发表的DSR知识贡献。2026年的趋势是用DSR框架系统化地构建和评估AI Agent系统，产出可复现的架构设计和评估方法论。

**怎么用**：把你的Capstone定位为DSR贡献--不是"我做了个系统"，而是"我设计了一个可复现的Agent架构artifact，并用五维度框架评估了它的有效性"。这把工程项目提升为学术贡献。

### 可复现研究（Reproducible Research）

可复现研究要求：不仅发表结论，还发表数据+代码+环境，让他人能独立复现你的结果。Agent系统的可复现性挑战更大（非确定性输出、API版本依赖、模型版本漂移）。2026年的最佳实践：
- **开源代码**：GitHub仓库+完整环境配置（requirements.txt/Dockerfile）
- **测试套件**：deepeval的CI测试用例，确保代码变更后评估结果可追踪
- **trace存档**：langsmith/Langfuse的执行trace，记录每次Agent运行的完整调用链
- **数据文档**：数据集来源、预处理、变量定义的完整文档

### 天道推演×多Agent仿真（特色章节）

> 本节与项目CLAUDE.md的「天道推演系统」同构，作为Capstone的特色理论视角。

**天道推演**（Tian Dao Tui Yan）是一种元认知沙盘推演能力--以天神视角俯视局势，在意识中构建无限可能的沙盘，模拟不同决策路径下的未来走向。其核心能力包括：局势感知、因果链追踪、沙盘模拟、概率评估、最优路径推荐。

**与多Agent仿真的同构关系**：

| 天道推演能力 | 多Agent仿真对应 | 共享的因果建模底层 |
|-------------|----------------|-------------------|
| 局势感知 | Agent环境建模 | 状态空间定义 |
| 因果链追踪 | Agent交互链分析 | 因果有向图 |
| 沙盘模拟（3层推演） | 多Agent场景模拟 | 并行世界树 |
| 概率评估 | 涌现行为概率分布 | 贝叶斯推断 |
| 最优路径推荐 | 策略优化 | 收益/风险权衡 |

**怎么用**：在Capstone论文的Discussion部分，可以用"天道推演×多Agent仿真"作为理论视角--你的营销Agent系统本质上是一个计算化的天道推演沙盘：Agent在模拟不同营销策略的因果效果，选择最优路径。这为工程系统提供了哲学层面的理论锚点，也是中文学术发表的特色贡献。

> ⚠️ 天道推演不是占卜，而是基于因果链和模式识别的逻辑推演。与DSR的artifact评估互补：DSR评估"系统好不好"，天道推演评估"策略路径优不优"。

> 🔗 深入阅读见 [`reading.md`](./reading.md) 的DSR和可复现研究条目。

---

## 与前序Day的衔接

- **Day 1-2**（架构+LangGraph）：今天把LangGraph Agent作为流水线的一环整合进来
- **Day 3**（评估）：今天的评估层复用deepeval的方法论（GEval + BaseMetric），但评估对象从单条文案升级为完整Agent系统
- **Day 4**（安全）：Capstone的安全评估纳入DSR Step 5
- **Day 5**（部署）：langsmith追踪作为可复现研究的基础设施
- **Day 6**（IMRaD）：今天的论文草稿用Day 6的IMRaD结构，但加入DSR artifact描述

---

## 作业与评估

作业、5分制量表、费曼演练、2分钟话术、复盘自诊表--沿用独立教材 § Day 7既有设计。本学习材料包不重复，仅新增上机交付物：

**新增交付物（v5.0 Capstone）**：
- [ ] 完成的 `starter.ipynb`（6个TODO全部填好，端到端流水线跑通）
- [ ] Capstone论文草稿（IMRaD结构，3000-5000字，含DSR artifact描述）
- [ ] 一段500字反思：你的Capstone在DSR六步中哪一步最薄弱？如何改进？
- [ ] （可选）学术发表路线图：选择一个目标期刊/会议，写一页投稿计划

---

*本讲义由v5.0学习材料包升级生成。理论部分引用独立教材，上机部分用真实库（causaldata+DoWhy+LangGraph+deepeval）+ TODO脚手架，整合技能1-5为端到端Capstone。*
*最后更新：2026-07-24*

---

## 学习科学层 (v6.0)

本单元采用**刻意练习** (Ericsson deliberate practice) / **间隔重复** (FSRS-6, SM-2 backup) / **建构对齐** (Biggs ILO↔TLA↔AT) / **牛津tutorial LLM仿真** (Socratic questioning, Hattie四级反馈) 四大学习科学机制。

- **刻意练习 (deliberate practice)**: 见 `practice.md` -- 4 个 drill 含 drill_id / difficulty / reps_required / feedback_rule / Worked-Faded 三阶段 (worked->faded->independent), 交叉排布 (interleaving: A1B1C1->B2C2A2->C3A3B3), weak_loop (连续2次失败触发弱项循环), CS230 式 progressive project (proposal->milestone->final->poster).
- **间隔重复 (spaced retrieval)**: 见 `schedule.json` -- FSRS-6 算法, 5 张卡片覆盖 DSR六步 / 端到端流水线 / 天道推演同构 / deepeval评估 / 可复现研究, due 间隔 [1,3,8,21,60,180].
- **建构对齐 (constructive alignment)**: 见 `alignment.md` -- 4 行 ILO↔TLA↔AT 矩阵, mastery threshold >=80%, 3 自检问题 (Feed Up / Feed Back / Feed Forward).
- **牛津tutorial (Oxford tutorial, Socratic)**: 见 `tutorial.ipynb` -- persona 不直接给答案, 5 轮 Socratic 追问 (为什么/反例/若前提变/凭什么/如何), Hattie 四级反馈 [TASK]/[PROCESS]/[SELF-REG]/[FEED-FORWARD], student_model 持久化, 限频 1次/天防依赖.

**mastery 阈值与 Worked-Faded 示例见 `practice.md` 与 `alignment.md`。交叉练习 (interleaving) 促进迁移, 提取练习 (retrieval practice) 优于重读。**

---

## 研究产出与产业链接层 (v7.0)

本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+arXiv链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。详见 research.md 与 industry.md。

---

## 学术前沿层 (v9.0)

本单元新增 `frontier.md`：注入 2025-2026 最新学术前沿（N 篇真实 arXiv 论文 + 批判性综述 + delta_to_unit + ≥3 开放研究问题 + 方法论批评）。论文来自 `_frontier_corpus/skill-5-agentic.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证），覆盖前沿课题：Agent评估 × LLM-as-a-Judge × Agent可靠性。面向博后/教授级读者：批判性综述非罗列，delta_to_unit 显式指出前沿如何更新本单元所教，开放问题为可发表研究方向。详见 `frontier.md`。
