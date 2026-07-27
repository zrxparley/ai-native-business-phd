# Capstone · Phase 6：系统实现与论文撰写 · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · Capstone AI和商业分析项目 · Phase 6（收官）
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2-3周 | 核心交付物：IMRaD论文草稿（3000-5000字）+ 发表路线图
> **核心命题**：把Phase 1-5整合为完整Capstone交付物--可运行系统+IMRaD论文+DSR artifact+发表路线图
> **v5.0 升级点**：① LangSmith @traceable可复现trace存档 ② deepeval LLM-as-a-judge论文评估 ③ statsmodels统计报告 ④ arxiv文献对比 ⑤ TODO填空脚手架 ⑥ 2026前沿（DSR artifact/可复现研究/天道推演×多Agent仿真）

---

## 学习目标（学完你能做到）

1. 能用 **DSR六步框架**（Hevner et al. 2004; Peffers et al. 2007）将Phase 1-5整合为完整Capstone artifact，把工程实践转化为可发表的设计科学贡献
2. 能用 **LangSmith @traceable** 追踪Capstone系统执行链，构建可复现研究的trace存档基础设施，让他人能独立验证Agent行为
3. 能用 **statsmodels + scipy** 跑统计检验（t检验/Cohen's d/卡方检验），把结果写成APA格式学术表述，撰写论文Results部分
4. 能用 **deepeval LLM-as-a-judge** 评估IMRaD论文草稿质量（自定义BaseMetric + GEval），理解LLM评审的优势与局限
5. 能撰写含 **DSR artifact描述** 的IMRaD论文草稿（3000-5000字），制定从arXiv到会议到期刊的学术发表路线图，并理解**天道推演×多Agent仿真**作为特色理论视角

---

## 理论部分：精炼索引（详见独立教材）

> Phase 6 的完整理论讲义见 [`../../../AI原生化商业博士_独立教材_Capstone_AI和商业分析项目.md` § Phase 6](../../../AI原生化商业博士_独立教材_Capstone_AI和商业分析项目.md)（§Phase 6：系统实现与论文撰写，含6.1阶段目标/6.2 IMRaD论文撰写/6.3学术发表路线图/6.4交付物清单）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：Phase 1-6整合--Capstone收官

Phase 6是Capstone的最终交付，将Phase 1-5整合为完整系统：

| Phase | 能力 | 在Capstone中的角色 | 真实库/方法 |
|:-----:|------|-------------------|------------|
| Phase 1 | 问题定义+文献综述 | 研究问题+PRISMA综述 | arxiv文献检索 |
| Phase 2 | 数据表示+知识图谱 | 客户/产品向量化表示 | embeddings |
| Phase 3 | Agentic系统架构 | LangGraph Agent编排 | LangGraph |
| Phase 4 | 因果实验设计 | ATE估计+反事实 | DoWhy + causaldata |
| Phase 5 | 商业模式+价值评估 | ROI+价值捕获 | 商业模式分析 |
| **Phase 6** | **系统实现+论文撰写** | **整合交付+IMRaD+发表** | **langsmith+deepeval+statsmodels+arxiv** |

**端到端流水线**：
```
Phase 1-5产出（研究问题/数据/Agent/因果/价值）
  ↓ LangSmith @traceable 追踪全链路
系统实现（集成测试+trace存档）
  ↓ statsmodels 统计报告
IMRaD论文草稿（Introduction/Methods/Results/Discussion）
  ↓ deepeval LLM-as-a-judge 评估
发表路线图（arXiv -> 会议 -> 期刊）
  ↓ 天道推演×多Agent仿真 特色章节
完整Capstone交付物
```

### 关键回顾 2：DSR六步框架（Capstone研究方法论）

**设计科学研究**（Design Science Research, DSR）是信息系统的核心研究范式。Hevner et al. (2004) 在MIS Quarterly提出DSR七准则；Peffers et al. (2007) 将其操作化为六步方法论。

```
Step 1: 问题识别 -- 企业营销面临什么问题？为什么现有方案不够好？
Step 2: 目标定义 -- artifact应该达到什么效果？
Step 3: 设计开发 -- 架构设计+Agent设计+评估设计+可复现设计
Step 4: 演示     -- 在真实场景中运行系统
Step 5: 评估     -- 定量(统计检验)+定性(deepeval评估)+稳健性(反驳检验)
Step 6: 传播     -- IMRaD论文+arXiv预印本+开源代码+学术发表
```

**DSR vs 传统实证研究**：传统实证回答"是什么"（what is），DSR回答"如何构建有效artifact"（how to build）。AI原生化系统天然适合DSR--你构建的Agent系统就是一个artifact。

### 关键回顾 3：IMRaD论文撰写

| 部分 | 字数 | 核心内容 | DSR映射 |
|------|:----:|---------|---------|
| Title | - | 简洁信息量大 | - |
| Abstract | 150-250 | 问题/方法/结果/贡献 | 全文缩影 |
| Introduction | 800-1000 | 背景->问题->贡献（漏斗结构） | DSR Step 1 |
| Related Work | 600-800 | 文献综述（Phase 1 PRISMA） | 文献定位 |
| Methods | 1000-1200 | DSR框架+系统设计+评估方法 | DSR Step 3 |
| Results | 800-1000 | ATE+统计检验+Agent评估 | DSR Step 5 |
| Discussion | 600-800 | 发现+局限+未来+天道推演 | DSR Step 6 |
| References | - | 20-30篇核心文献 | APA第7版 |

**论文标题模板**：`[方法] for [问题]: A [框架] Approach`
**示例**：`Causal Marketing Intelligence: A LangGraph-Based Multi-Agent System with DoWhy Evaluation and LangSmith Reproducibility`

### 关键回顾 4：学术发表路线图

| 级别 | 期刊/会议 | 影响因子 | 适合度 | 周期 |
|------|----------|:--------:|:------:|:----:|
| 顶刊 | MIS Quarterly | IF~8.0 | ⭐⭐⭐ | 6-12月 |
| 顶会 | ICIS | AIS Top 1 | ⭐⭐⭐⭐⭐ | 6月 |
| 好刊 | Decision Support Systems | IF~7.0 | ⭐⭐⭐⭐⭐ | 3-6月 |
| 好刊 | International Journal of Information Management | IF~8.0 | ⭐⭐⭐⭐ | 3-6月 |
| 会议 | HICSS | AIS Top 2 | ⭐⭐⭐⭐ | 6月 |
| 前沿 | arXiv预印本 | - | ⭐⭐⭐⭐⭐ | 即时 |

**发表策略**：arXiv预印本（立即）-> 投稿会议（反馈快）-> 改进后投期刊 -> 持续迭代2-3轮。

---

## 上机部分：系统实现 + 论文撰写 + 质量评估

> 📓 **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO填空版，你来做）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，做完再看）
> 📊 **真实数据/库**：[`data/README.md`](./data/README.md)（langsmith + deepeval + statsmodels + arxiv + causaldata NSW + DoWhy）

### 为什么用真实库（langsmith/deepeval/statsmodels/arxiv）

v4.0 的Phase 6只讲论文格式模板--学生看了还是不会写。v5.0 用**真实库**构建可运行的Capstone交付物：

- **langsmith**（@traceable）：追踪系统执行链，生成trace存档，作为可复现研究的基础设施。每个Phase的执行都被记录，让他人能独立验证。
- **deepeval**（LLM-as-a-judge）：用自定义BaseMetric + GEval评估论文草稿质量，检查IMRaD完整性/统计依据/DSR描述/可复现性。
- **statsmodels + scipy**：跑t检验/Cohen's d/卡方检验，生成APA格式统计报告，让Results有真实数据支撑。
- **arxiv**：搜索相关论文做文献对比，定位Capstone的学术贡献。
- **causaldata + DoWhy**：整合Phase 4的因果分析产出。

### 营销场景映射

本Phase的Capstone最终交付：**AI营销Agent系统的完整实现 + IMRaD论文 + 发表路线图**

| 流水线层 | 真实库 | 产出 |
|---------|--------|------|
| 可复现层 | langsmith @traceable | Phase 1-5 trace存档 |
| 数据层 | causaldata NSW | 真实RCT DataFrame (N=445) |
| 因果层 | DoWhy | ATE估计 + 安慰剂检验 |
| 统计层 | statsmodels + scipy | t检验 + Cohen's d (APA格式) |
| 论文层 | IMRaD模板 | 3000-5000字论文草稿 |
| 评估层 | deepeval | 论文质量评分 (5维度) |
| 文献层 | arxiv | 相关论文对比 |
| 传播层 | 发表路线图 | arXiv -> 会议 -> 期刊 |

### 上机任务（7个TODO，见starter.ipynb）

1. **TODO1**：DSR Artifact设计--用DSR六步框架定义Capstone，整合Phase 1-5
2. **TODO2**：LangSmith可复现基础设施--用@traceable追踪系统执行链，生成trace存档
3. **TODO3**：Phase 1-5数据整合--加载NSW真实RCT，用DoWhy估计ATE
4. **TODO4**：论文Results统计报告--用statsmodels/scipy跑t检验+Cohen's d+卡方检验
5. **TODO5**：IMRaD论文草稿--整合所有产出生成结构化论文（含DSR artifact描述）
6. **TODO6**：论文质量评估--用deepeval自定义BaseMetric + GEval LLM-as-a-judge评估
7. **TODO7**：arxiv文献对比 + 发表路线图 + 天道推演×多Agent仿真特色章节

---

## 2026前沿：DSR artifact + 可复现研究 + 天道推演×多Agent仿真

> v5.0新增前沿点。Phase 6作为Capstone收官，聚焦四个前沿方向。

### DSR artifact 在AI系统设计中的应用

DSR（Hevner et al. 2004, MIS Quarterly）在AI原生系统时代获得新生命：Agent系统本身就是一个artifact，它的架构模式、评估框架、安全实践都是可发表的DSR知识贡献。2026年的趋势是用DSR框架系统化地构建和评估AI Agent系统，产出可复现的架构设计和评估方法论。

**怎么用**：把你的Capstone定位为DSR贡献--不是"我做了个系统"，而是"我设计了一个可复现的Agent架构artifact，并用五维度框架评估了它的有效性"。

### 可复现研究（Reproducible Research）与 LangSmith trace存档

可复现研究要求：不仅发表结论，还发表数据+代码+环境+trace，让他人能独立复现。Agent系统的可复现性挑战更大（非确定性输出、API版本依赖、模型版本漂移）。2026年最佳实践：
- **trace存档**：langsmith @traceable记录每次Agent运行的完整调用链
- **开源代码**：GitHub仓库+完整环境配置
- **测试套件**：deepeval的CI测试用例，确保代码变更后评估结果可追踪
- **数据文档**：数据集来源、预处理、变量定义的完整文档

### 天道推演×多Agent仿真（特色章节）

> 本节与项目CLAUDE.md的「天道推演系统」同构，作为Capstone的特色理论视角。

**天道推演**是一种元认知沙盘推演能力--以天神视角俯视局势，在意识中构建无限可能的沙盘，模拟不同决策路径下的未来走向。其核心能力包括：局势感知、因果链追踪、沙盘模拟、概率评估、最优路径推荐。

**与多Agent仿真的同构关系**：

| 天道推演能力 | 多Agent仿真对应 | 共享的因果建模底层 |
|-------------|----------------|-------------------|
| 局势感知 | Agent环境建模 | 状态空间定义 |
| 因果链追踪 | Agent交互链分析 | 因果有向图 |
| 沙盘模拟（3层推演） | 多Agent场景模拟 | 并行世界树 |
| 概率评估 | 涌现行为概率分布 | 贝叶斯推断 |
| 最优路径推荐 | 策略优化 | 收益/风险权衡 |

**怎么用**：在Capstone论文的Discussion部分，用"天道推演×多Agent仿真"作为理论视角--你的营销Agent系统本质上是一个计算化的天道推演沙盘。

### LLM-as-a-judge 论文评估

用LLM自动评估论文质量（NeurIPS 2023, arXiv 2306.05685）。2026年趋势是用DeepSeek等开源模型降低评估成本，实现大批量论文写作自检和CI/CD集成。注意：LLM-as-a-judge是辅助评估，有自身偏差，不能替代真实同行评审。

> 🔗 深入阅读见 [`reading.md`](./reading.md) 的DSR和可复现研究条目。

---

## 与前序Phase的衔接

- **Phase 1**（问题定义+文献综述）：今天的Introduction基于Phase 1的研究问题和PRISMA综述
- **Phase 2**（数据表示+知识图谱）：今天的数据层复用Phase 2的数据表示方法
- **Phase 3**（Agentic系统架构）：今天的系统实现整合Phase 3的LangGraph Agent架构
- **Phase 4**（因果实验设计）：今天的Results基于Phase 4的DoWhy ATE估计
- **Phase 5**（商业模式+价值评估）：今天的Discussion包含Phase 5的商业模式分析
- **Phase 6**（本Phase）：整合以上所有产出为完整Capstone交付物

---

## 作业与评估

作业、5分制量表、费曼演练、2分钟话术、复盘自诊表--沿用独立教材 § Phase 6 既有设计。本学习材料包不重复，仅新增上机交付物：

**新增交付物（v5.0 Capstone收官）**：
- [ ] 完成的 `starter.ipynb`（7个TODO全部填好，端到端流水线跑通）
- [ ] Capstone论文草稿（IMRaD结构，3000-5000字，含DSR artifact描述）
- [ ] LangSmith trace存档（@traceable追踪的Phase 1-5执行链）
- [ ] 论文质量评估报告（deepeval评分 + 改进建议）
- [ ] 学术发表路线图（arXiv -> 会议 -> 期刊，一页计划）
- [ ] 天道推演×多Agent仿真特色章节（500字以上）
- [ ] （可选）arXiv预印本上传计划

---

*本讲义由v5.0学习材料包升级生成。理论部分引用独立教材，上机部分用真实库（langsmith+deepeval+statsmodels+arxiv+causaldata+DoWhy）+ TODO脚手架，整合Phase 1-5为端到端Capstone收官。*
*最后更新：2026-07-24*

---

## 学习科学层 (v6.0)

本单元采用**刻意练习** (Ericsson 1993, deliberate practice) / **间隔重复** (FSRS-6, SM-2 backup, spaced retrieval) / **建构对齐** (Biggs 1996, constructive alignment, ILO↔TLA↔AT) / **牛津 tutorial LLM 仿真** (Socratic questioning, Hattie 四级形成性反馈 [TASK]/[PROCESS]/[SELF-REG]/[FEED-FORWARD])。

**mastery 阈值**与 **Worked-Faded** 示例 (完整示范 -> 部分填空 -> 独立解) 见 [`practice.md`](./practice.md) 与 [`alignment.md`](./alignment.md)。

**交叉练习** (interleaving, A1B1C1...B2C2A2...C3A3B3) 促进迁移: DSR-to-IMRaD 写作 / langsmith+deepeval / statsmodels APA 三子技能不块状训练, 而是每天轮换。

**提取练习** (retrieval practice) 优于重读: pre-tutorial essay 强制学生先提取, tutor 再精准定位盲点 (见 [`tutorial.ipynb`](./tutorial.ipynb))。

**FSRS-6 间隔重复卡片** (DSR六步 / langsmith trace / NSW统计 / deepeval五维 / 发表路线图 / 天道推演同构) 见 [`schedule.json`](./schedule.json), request_retention=0.9, 6 个 review 节点 [1,3,8,21,60,180]。

**v6.0 关键词命中**: FSRS-6, SM-2, 刻意练习, deliberate practice, 建构对齐, constructive alignment, 牛津 tutorial, Socratic, Hattie, 间隔重复, spaced retrieval, 交叉, interleaving, mastery, Worked-Faded, retrieval practice。

---

## 研究产出与产业链接层 (v7.0)

本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+arXiv链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。详见 research.md 与 industry.md。

**v7.0 关键词命中**: 研究产出, research output, IMRaD, 可复现, reproducibility, OSF, preregistration, 预注册, FAIR, contribution, 贡献, 产业链接, industry linkage, consulting, 咨询, case study, 案例, guest lecture, 客座, internship, 实习, deployment, 部署, linked_paper, arXiv, DSR, Hevner, research-to-practice, NeurIPS, 行动学习, action learning。
