# AI原生化商业博士 v5.0 升级方案

> **编制**：Claude（基于 v4.0 + 13本独立教材现状的"学习材料包"升级规划）
> **日期**：2026-07-23
> **基于版本**：v4.0 全球对标与研究方法论版 + 本地 13 本独立教材（技能0-5 / 模块R / Capstone / 选修E1·E2·E3·E9·E10）
> **调研范围**：MIT / Stanford / Harvard / Oxford / Cambridge / Imperial 六校公开教学资源 + GitHub 教学型仓库生态 + 2026 前沿课题
> **升级方向**：从"独立教材（讲义+完整代码示例）"跃迁到"完整学习材料包（真实数据 × 练习脚手架 × Notebook化 × 2026前沿）"
> **v5.0 哲学增量**：表示即知识 → 规模揭示本质 → 目标即终点 → 做出来才算数 → 研究即贡献 → **真实即严谨 · 练习即掌握**

---

## 一、现状评估

### 1.1 v4.0 + 独立教材 已有的优势

v4.0 主教材之外，本地已建成 **13 本独立教材**（均未推送 GitHub），每本 39KB-135KB，已具备相当深度：

| 独立教材 | 体量 | 已有内容 |
|---------|------|---------|
| 技能0 AI商业分析基础 | 106KB | 6天讲义 + 电商RFM/多源数据整合完整Python脚本 |
| 技能1 表示工程与营销智能 | 89KB | 讲义 + embedding/知识图谱代码 |
| 技能2 AI原生企业架构 | 135KB | 讲义 + 治理框架 |
| 技能3 因果推断与规模实验 | 88KB | 讲义 + A/B测试/PSM/DiD/DoWhy完整代码 |
| 技能4 AI驱动商业模式创新 | 84KB | 讲义 + 商业模式画布 |
| 技能5 Agentic系统工程与落地 | 113KB | 讲义 + 完整LangGraph多Agent实现（分析/策略/内容/审核节点） |
| 模块R 博士研究方法论 | 66KB | R1-R6讲义 + 15题问答 + 综合作业 + 费曼演练 + 资源清单 |
| Capstone | 63KB | 双路径设计 |
| 选修E1/E2/E3/E9/E10 | 39-65KB | 5门选修教材 |

**已覆盖的四层（参见1.3）**：Delivery 交付层（讲义正文）✅、Practice 练习层（完整代码示例）✅、Assessment 评估层（问答/作业/费曼/量表）✅。

**已部分覆盖的 2026 前沿**：MCP（1处）、A2A（1处）、RAGAS（1处）、meridian/Robyn（1处）、HELM/promptfoo（1处）、garak/PyRIT/红队（4处）、EU AI Act（5处）、中国生成式AI/算法备案（3处）。

### 1.2 关键差距：从"独立教材"到"学习材料包"差三层

用顶级大学课程（Stanford CS224N / MIT 6.S191 / Harvard CS50 / HBS 案例法）的四层标准衡量，独立教材已填满三层，但**离"可交付的完整学习材料包"还有三个真实缺口**：

| 缺口 | 现状（量化） | 顶级课程标准 | 差距 |
|------|------------|------------|------|
| **① 真实数据集层** | 代码普遍用"模拟数据"（技能3出现15次、技能0出现12次）；Kaggle仅被提及14次，未作为起始数据集 | MIT 15.071 每个pset配真实数据集（Netflix/Twitter/医疗/选举）；CS50每pset配数据文件 | **模拟→真实**：Application层缺真实可复现案例 |
| **② 练习脚手架层** | 全部13本教材 **0个TODO/0个学生填空**；代码全是完整workout示例 | MIT 6.S191 lab是"起始代码+TODO填空"；CS224N作业是"骨架+你实现" | **示例→练习**：缺主动练习的脚手架（现在是"看懂"而非"做出"）|
| **③ Notebook化与文件分离** | 代码内嵌在.md里，无独立.ipynb、无独立数据文件、无参考答案分离 | 顶级课程讲义/笔记本/数据/答案分文件 | **单体→分包**：缺可运行、可分发、可gated答案的结构 |

**外加两个内容缺口**（详见第四、五章）：
- **④ 2026前沿仍有盲点**：LLM-as-a-judge（0处）、DeepSeek-R1/推理经济（薄）、deepeval（0处）、ASReview/cookiecutter（0处）
- **⑤ 资源仍是主页级**：多数链接指向课程主页，非深链到具体讲义PDF/pset/数据集

### 1.3 调研方法

本轮调研由三个并行研究智能体完成，**全部链接经逐一验证存在**（非主页级深链）：
- 智能体A：六校公开教学资源（OER）深链检索 → 38 项已验证资源
- 智能体B：GitHub 教学型仓库检索 → 55 项已验证仓库（含star数）
- 智能体C：2026 前沿课题 + 顶级课程教材架构 → 30 项前沿 + 12组件教学单元模板

> 关键方法学结论：**"一个大纲条目不等于一个教学模块--只有当 Delivery / Practice / Application / Assessment 四层都存在时，它才成为一个真正的教学模块。"** 独立教材已完成 Delivery + Practice + Assessment，v5.0 的任务是把 Application 层做实（真实数据）+ 把 Practice 层从"示例"升级为"脚手架练习"。

---

## 二、v5.0 核心：从独立教材到完整学习材料包

### 2.1 学习材料包架构（v5.0 新增）

在每本独立教材旁，建立一个同名的**学习材料包目录**，包含四类可交付物：

```
teaching-materials/
├── skill-3-causal/
│   ├── day-1-causal-basics/
│   │   ├── notes.md              ← 从独立教材抽取/精炼的讲义（Delivery）
│   │   ├── starter.ipynb         ← 起始笔记本：TODO填空式（Practice-脚手架）⭐新增
│   │   ├── solution.ipynb        ← 参考答案（gated，不公开）⭐新增
│   │   ├── data/                 ← 真实数据集（Application）⭐新增
│   │   ├── reading.md            ← 深链阅读清单（指向具体PDF/pset）
│   │   ├── assignment.md         ← 作业（从独立教材迁移）
│   │   └── rubric.md             ← 量表（从独立教材迁移）
│   └── ...
├── _shared/
│   ├── glossary.md               ← 跨技能术语表
│   ├── datasets-index.md         ← 全部真实数据集索引与来源
│   └── reading-list.md           ← 全部深链阅读清单
└── cases/                        ← 真实案例库（替代虚构案例）
```

### 2.2 10 组件教学单元模板（从顶级课程提炼）

每个"技能-每天"作为一个标准教学单元，含 10 组件：

1. 学习目标（3-5条可衡量）— CS224N 每份handout开头都有
2. 讲义正文 .md（概念展开+图示+推导）— ✅独立教材已有，精炼抽取
3. 阅读清单（教材章+1-2篇论文**深链**）— ⭐升级：主页→深链
4. 起始 Notebook（TODO填空式）— ⭐新增
5. 真实数据集 — ⭐新增（替代模拟数据）
6. 习题+参考答案（笔试+编程）— ⭐新增
7. 案例（HBS式决策强制型，带真实数据）— ⭐升级：虚构→真实
8. 作业+5分制量表 — ✅独立教材已有，迁移
9. 费曼演练+2分钟话术 — ✅独立教材已有，迁移
10. 复盘自诊表+常见坑FAQ — ✅自诊已有，FAQ新增

### 2.3 v5.0 三大升级主线

| 主线 | 口号 | 动作 |
|------|------|------|
| **真实数据** | "真实即严谨" | 把模拟数据替换为真实数据集（MIT 15.071/Kaggle/HAI AI Index） |
| **脚手架练习** | "练习即掌握" | 把完整示例改写出 TODO 填空版起始笔记本 + gated 参考答案 |
| **Notebook化** | "可运行可分发" | 内嵌代码抽取为独立 .ipynb + 独立数据文件 + 答案分离 |

---

## 三、高校 × GitHub 资源深度融合地图

### 3.1 融合原则

1. **高校出理论与评测框架，GitHub 出可运行练习** — 二者配对嵌入每个教学单元
2. **深链替代主页** — 用经验证的 PDF/pset/数据集深链，不用课程主页
3. **诚实标注 gated 资源** — Cambridge/Imperial/HBS 教学材料不公开（见第五章），不硬凑
4. **融合进现有独立教材** — 不是另起炉灶，而是给每本独立教材补"真实数据+脚手架+深链"

### 3.2 技能 × 资源融合表（每技能选最强 2-4 项，全部已验证）

#### 技能0 预科
| 概念 | 高校OER（理论/数据） | GitHub（练习） | 融合动作 |
|------|-------------------|--------------|---------|
| Python/数据思维 | **MIT OCW 6.0002**（15讲义PDF+代码+视频） | microsoft/Data-Science-For-Beginners（36k★） | 用6.0002讲义补Day1-2正文；DS-For-Beginners的notebook改写为TODO起始练习 |
| 概率统计 | **MIT OCW 18.05**（带答案pset+考试）+ **MIT OLL 18.06**（Strang线代，免费交互） | CamDavidsonPilon/Bayesian-Methods-Hackers（28k★） | 用18.05的pset+答案直接做练习层 |
| 数据库/SQL | **MIT OCW 6.830**（Stonebraker，20讲义） | — | 补SQL/数据治理深度 |

> **升级**：MIT OCW 是验证后最丰富的高校公开教学资源（PDF+代码+数据+答案齐全），应从"英语轨道材料"升格为预科主力教材。

#### 技能1 表示工程
| 概念 | 高校OER | GitHub | 融合动作 |
|------|--------|--------|---------|
| 表示学习/Embedding | **Stanford CS224N 2026**（17讲义+4作业+代码） | d2l-ai/d2l-en（29k★，500+大学采用） | CS224N升格为讲义正文来源；d2l对应章节做可运行笔记本 |
| 多模态 | **MIT 6.S191 2026**（9讲义+YouTube+3 lab） | BradyFU/Awesome-Multimodal-LLM（18k★） | 用6.S191的facial-detection bias lab当起始练习（含偏见检测） |
| 知识图谱/GraphRAG | **Stanford CS336**（8讲义+5作业，含数据管道） | husthuke/awesome-knowledge-graph（中文友好） | GraphRAG文档+awesome-kg索引做案例 |

#### 技能2 AI原生架构 + 治理
| 概念 | 高校OER | GitHub | 融合动作 |
|------|--------|--------|---------|
| NIST AI RMF | **NIST AI RMF 1.0 PDF** + **GenAI Profile** + **Playbook**（三深链） | finos/ai-governance-framework | 用Playbook做正文，finos框架当企业落地模板 |
| EU AI Act | **EUR-Lex官方全文PDF**（2024/1689） | ethanolivertroy/awesome-grc-ai | 用官方全文做分级练习（补2026.8 Article 50执行深度） |
| Agentic Org/伦理 | **Stanford HAI治理研究** + **Oxford OII出版物**（2026年14页） | nibzard/awesome-agentic-patterns（4.8k★） | OII研究做伦理视角，agentic-patterns当架构模式库 |

#### 技能3 因果推断（论文核心）
| 概念 | 高校OER | GitHub | 融合动作 |
|------|--------|--------|---------|
| 因果基础/DAG | **MIT OCW 15.071**（24+讲义+9带答案pset+**真实数据集**） | matteocourthoud/awesome-causal-inference（1.2k★） | **用15.071的Netflix/Twitter真实数据集替换技能3的模拟数据**（核心动作）|
| 营销归因/MMM | — | **google/meridian**（1.5k★）+ **facebookexperimental/Robyn**（1.5k★） | 用meridian/Robyn的vignette notebook当起始练习 |
| 因果发现/DoWhy | — | **Mixtape-Sessions/Causal-Inference**（课程代码）+ DoWhy tutorials | Mixtape课程代码做讲义配套练习 |

> ⚠️ **关键缺口**：六校无开放因果推断专门课。主力用 Brady Neal课程 + Mixtape Sessions + DoWhy tutorials；高校用 15.071 真实数据集补 Application 层。

#### 技能4 AI商业模式
| 概念 | 高校OER | GitHub | 融合动作 |
|------|--------|--------|---------|
| AI经济/行业数据 | **Stanford HAI AI Index 2026报告**（完整PDF+公开数据文件，9章） | — | **用AI Index 2026的经济/政策章当真实案例数据源**（替代虚构案例）|
| 平台经济学 | **Stanford HAI Global AI Vibrancy Tool**（可下载数据） | — | 用Vibrancy Tool做跨国AI竞争分析练习 |
| Agent经济 | — | 见技能5 agentic-patterns | a16z Agent Economy系列+HAI数据做商业模式画布 |

> ⚠️ 技能4是GitHub覆盖最弱领域。正确做法：从 HAI AI Index + HBR + a16z + 平台经济学论文取，不硬找代码仓库。

#### 技能5 Agentic系统（GitHub资源最丰富）
| 概念 | 高校OER | GitHub | 融合动作 |
|------|--------|--------|---------|
| Agent/LLM基础 | **Stanford CS329S**（Chip Huyen，讲义+作业+9份学生项目报告） | mlabonne/llm-course（81k★）；microsoft/generative-ai-for-beginners（113k★） | CS329S讲义补正文，学生项目报告当案例范本 |
| LangGraph实战 | — | **langchain-ai/langchain-academy**（2.8k★，官方课程）+ huggingface/agents-course（30k★） | **用langchain-academy课程当起始练习**（技能5现已有完整LangGraph实现，加TODO版）|
| Agent评测 | **Stanford CRFM HELM**（整体评测框架） | **confident-ai/deepeval**（17k★）⭐ + promptfoo（23k★） | **用deepeval做评测练习**（远超现在的AgentBench单点）⭐新增 |
| Agent安全 | — | **NVIDIA/garak**（8.6k★）+ Azure/PyRIT + liu00222/Open-Prompt-Injection | 用garak/PyRIT当红队实验起始代码（技能5已提及，需做成可运行lab）|
| 对齐/RLHF | **Stanford CS336 Assignment5**（SFT+RL推理+DPO，PDF+代码） | — | 用CS336 A5当对齐练习 |

#### 模块R 研究方法论（GitHub最薄）
| 概念 | 高校OER | GitHub | 融合动作 |
|------|--------|--------|---------|
| PRISMA系统综述 | **PRISMA 2020 Checklist**（PDF+Word，CC BY）+ **Expanded Checklist** + **Shiny App** | **asreview/asreview**（953★，主动学习做PRISMA筛选）⭐ | 用PRISMA Checklist做正文，**ASReview当可运行筛选工具**（模块R唯一能动手处）⭐新增 |
| 定性研究/访谈 | **MIT OLL 21A.819.1x/2x**（定性研究方法，免费）+ **EC.745X**（田野访谈） | — | R2行动研究的定性方法 |
| 研究伦理 | **MIT OLL 24.02x**（伦理学导论，免费） | — | R6伦理 |
| 可复现研究 | — | **drivendataorg/cookiecutter-data-science**（10k★）⭐ | **所有作业统一用此模板**，养成可复现习惯 ⭐新增 |
| DSR/IMRaD写作 | —（GitHub无高质量教学仓库） | — | 只能用原始论文（Hevner 2004/Peffers 2007）+大学写作中心 |

### 3.3 资源可信度分级

| 来源 | 开放状态 | 用法 |
|------|---------|------|
| MIT OCW / OLL | ✅ 完全开放（PDF+代码+数据+答案） | 主力教材内容来源 |
| Stanford CS224N/CS336/CS329S/CS25/HAI | ✅ 完全开放 | 主力教材内容来源 |
| NIST / EUR-Lex / PRISMA | ✅ 官方公开PDF | 治理/方法论权威原文 |
| Oxford OII | 🟡 仅出版物+研究手册PDF（无开放课程） | 研究视角对标 |
| Cambridge Judge / Imperial MSc | 🔴 不开放（403/Canvas） | 仅保留为对标，不作教材来源 |
| Harvard HBS 案例 | 🔴 付费 | 用 HBS Working Papers（免费）+ MIT Sloan 案例替代 |

---

## 四、2026 前沿课题补充

### 4.1 必须补（已是行业生产级，当前0处或薄）

| 前沿课题 | 现状 | 映射到 | 验证链接 | 补充动作 |
|---------|------|--------|---------|---------|
| **LLM-as-a-judge** | 0处 | 技能5评测 | arxiv 2306.05685 | 新增Day：开放式任务评测工业标准，补AgentBench之外的评测方法 |
| **DeepSeek-R1 / 推理经济** | 薄（1处泛提） | 技能4定价+技能5 | DeepSeek-R1发Nature 2025；arxiv 2501.12948 | 新增"推理模型改变单位经济"（o1-pro $150/$600每百万token）章节 |
| **deepeval 评测框架** | 0处 | 技能5评测 | github confident-ai/deepeval（17k★） | 用deepeval做可运行评测练习 |
| **ASReview（PRISMA工具）** | 0处 | 模块R4 | github asreview/asreview（953★） | 模块R唯一可动手工具，补PRISMA实操 |
| **cookiecutter-data-science** | 0处 | 模块R/全技能 | github drivendataorg/cookiecutter-data-science（10k★） | 所有作业统一可复现模板 |
| **EU AI Act 2026执行深度** | 5处提及但无执行细节 | 技能2+R6 | artificialintelligenceact.eu | 补2026.8 Article 50透明度义务、GPAI义务、Code of Practice |
| **中国生成式AI规则** | 3处提及 | 技能2+R6 | CAC 2023.8临时办法 | 已部分覆盖，需补算法备案/AIGC备案实操 |

### 4.2 建议补（真实但早期/有特色价值）

| 课题 | 映射到 | 价值 |
|------|--------|------|
| **MCP / A2A 协议深化** | 技能2+5 | 已各提及1处，需从"提及"升级为"可运行示例"（MCP是Agent互操作事实标准）|
| **小语言模型/端侧AI（Phi-3）** | 技能2 | 企业隐私+零API成本推理 |
| **推理成本工程（vLLM/投机解码/MoE）** | 技能5 | 影响部署经济，arxiv 2309.06180等 |
| **计算机使用/浏览器Agent** | 技能5 | Claude computer use 2024.10，新自动化范式 |
| **Feature Store（Feast）/合成数据** | 技能0+1 | AI数据基础设施，未覆盖 |
| **SWE-bench / AI编码Agent** | 技能4+5 | 影响软件商业模式与开发效率研究 |
| **⭐多Agent仿真 × 天道推演** | 技能4 | **与CLAUDE.md「天道推演系统」高度同构**，可把天道推演从"思维框架"升级为"可计算多Agent沙盘"，成为教材独有特色 |

### 4.3 前沿 × 技能映射总表

```
技能0 预科    ← Feature Store/合成数据（数据基础设施）
技能1 表示    ← MCP深化（表示→工具协议）
技能2 架构    ← MCP/A2A深化 + SLM端侧 + EU AI Act 2026执行 + 中国AI规则实操
技能3 因果    ← （因果前沿已较全，重点补真实数据）
技能4 商业    ← DeepSeek-R1推理经济 + 多Agent仿真×天道推演（特色）+ SWE-bench
技能5 系统    ← LLM-as-a-judge + deepeval + 推理成本工程 + 计算机使用Agent + MCP/A2A
模块R         ← ASReview + cookiecutter + EU AI Act 2026执行 + 中国AI伦理
```

---

## 五、诚实标注的缺口（不粉饰）

1. **Cambridge / Imperial / Harvard HBS 教学材料不公开** — 经验证分别为 403 / Canvas / 付费。建议保留为"研究视角对标"，教材内容主力用 MIT OCW + Stanford（验证后最丰富）。
2. **六校无开放因果推断专门课** — 用 Brady Neal + Mixtape Sessions + DoWhy tutorials 主导，高校用 15.071 真实数据集补应用层。
3. **技能4 GitHub覆盖弱** — 不硬找代码仓库，从 HAI AI Index 2026 + HBR + a16z + 平台经济学论文取内容。
4. **模块R 的 DSR/IMRaD 在 GitHub 无高质量教学仓库** — 只能用原始论文 + 大学写作中心 + PRISMA工具(ASReview)。
5. **Harvard HBS 案例付费** — 用 HBS Working Papers（免费）+ MIT Sloan 案例替代。
6. **独立教材未推送 GitHub** — 13本本地教材与GitHub仓库不同步，v5.0应一并推送。

---

## 六、实施计划

### 6.1 三阶段实施

**第一阶段：样本单元验证（1周）**
- 选 **技能3 Day1（因果推断基础）** 做完整样本学习材料包（因它是论文核心，又能同时演示三大升级主线）
- 产出：notes.md（精炼讲义）+ starter.ipynb（TODO填空版）+ solution.ipynb（gated答案）+ data/（MIT 15.071真实数据集）+ reading.md（深链）+ 迁移作业/量表/费曼
- 验证模板可行后批量铺开

**第二阶段：批量铺开（4-6周）**
- 按融合地图，给每本独立教材补"真实数据+脚手架+深链"
- 优先级：技能3 > 技能5 > 技能1 > 技能0 > 技能2/4/模块R > 选修
- 同步推送13本独立教材到GitHub

**第三阶段：v5.0 主教材正式版（1-2周）**
- 写 v5.0 主教材，纳入"四层学习材料包架构 + 2026前沿 + 多Agent天道推演特色章节"
- 更新README版本说明与导航

### 6.2 学时与工作量变化

| 项目 | v4.0 | v5.0 | 变化 |
|------|------|------|------|
| 预科 | 22h | 22h | 不变（补真实数据，不加时）|
| 技能1-5 | 50-64h | 50-64h | 不变（脚手架练习替换部分示例，不加时）|
| 模块R | 10h | 10h | 不变 |
| 选修 | 18h | 18h | 不变 |
| 英语轨道 | 32h | 32h | 不变 |
| **总计** | **122-136h** | **122-136h** | **学时不变，材料完整度跃升** |
| 制作工作量 | — | 样本1周+批量4-6周+正式版1-2周 | 约6-9周 |

> v5.0 是**材料完整度升级**，不是学时扩张--把"看懂"升级为"做出"，把"模拟"升级为"真实"。

### 6.3 版本命名

- 主教材文件：`AI原生化商业博士_主教材_v5.0_学习材料包版.md`
- 版本特色标签：四层学习材料包 + 真实数据集 + 练习脚手架 + Notebook化 + 2026前沿补全 + 多Agent天道推演特色
- 保留 v4.0 作为历史版本

### 6.4 风险与对策

| 风险 | 概率 | 对策 |
|------|:----:|------|
| 真实数据集获取/授权复杂 | 中 | 优先用MIT 15.071/Kaggle/HAI等已开放数据集；商业敏感数据用脱敏 |
| 脚手架练习制作工作量大 | 高 | 先做样本验证模板，批量时用脚本从完整代码自动生成TODO版 |
| 2026前沿更新过快 | 低 | 每季度审查前沿，标注[ADOPTED]/[EMERGING]/[HYPE]状态 |
| 深链失效 | 中 | 每月检查，保留备选；_shared/reading-list.md集中维护 |
| 独立教材与GitHub不同步 | 高 | v5.0第一阶段就推送13本独立教材 |

---

## 七、决策点

请审阅以下决策点，确认后开始执行：

**决策1：样本单元选择**
- 方案A（推荐）：技能3 Day1（因果推断基础）— 论文核心 + 同时演示三大主线
- 方案B：技能5 Day2（LangGraph实战）— GitHub资源最丰富 + 已有完整实现
- 方案C：技能0 Day1（Python基础）— 最简单，快速验证模板

**决策2：脚手架练习的制作方式**
- 方案A（推荐）：完整代码 + 自动生成的TODO版起始笔记本 + gated参考答案
- 方案B：只提供起始笔记本+TODO，不提供参考答案
- 方案C：保留完整示例，另加独立习题（不做TODO改写）

**决策3：真实数据集策略**
- 方案A（推荐）：优先MIT 15.071/Kaggle/HAI AI Index等已开放数据集
- 方案B：用宿主企业脱敏数据（更贴近业务，但有合规风险）
- 方案C：混合—开放数据集为主，企业脱敏数据为Capstone专用

**决策4：2026前沿纳入范围**
- 方案A（推荐）：4.1必须补全部纳入 + 4.2建议补选3项（MCP/A2A深化、推理成本工程、多Agent天道推演特色）
- 方案B：仅纳入4.1必须补
- 方案C：4.1+4.2全部纳入

**决策5：多Agent天道推演特色章节**
- 方案A（推荐）：作为技能4特色章节，把天道推演从思维框架升级为可计算多Agent沙盘
- 方案B：作为独立选修E11
- 方案C：暂不纳入，留待v6.0

**决策6：执行范围**
- 方案A（推荐）：先做样本单元（第一阶段），验证后再批量
- 方案B：一次性完成全部v5.0升级
- 方案C：分批—先技能3+5+模块R，再技能0/1/2/4

---

*本方案由Claude基于 v4.0 + 13本独立教材现状 + 六校OER/GitHub教学仓库/2026前沿三轮调研编制，等待用户审阅确认后执行。*
*最后更新：2026-07-23*
