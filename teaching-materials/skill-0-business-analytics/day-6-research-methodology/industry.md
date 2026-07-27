# Day 6 产业链接层 (v7.0)

> 本单元 (技能0 · Day 6 研究方法论入门) 的产业链接锚定: 用 arxiv + networkx + ASReview + OSF/FAIR 方法做"学术尽职调查"与企业研发情报. 产业链接遵循 Imperial MSc BA 咨询项目 (Burberry/Expedia/J&J) / HBS 案例法 / MIT Sloan 行动学习 (Action Learning) 模式.

---

## real_companies

**>=3 家真实企业锚点 (从公司库挑, 与本单元研究方法论 + 文献计量 + ASReview + 可复现研究主题匹配)**:

| 公司 | 与本单元关联 | 业务场景 |
|------|------------|---------|
| **Microsoft** | Microsoft Research 与 ExP (Experimentation Platform) 团队是全球 A/B 测试与可复现研究 (Reproducible Research) 的工业标杆. 本单元 OSF 预注册 / Registered Reports / random_state=42 环境锁定三大支柱, 正是 Microsoft ExP 在千亿级实验上落地的方法论. | Microsoft ExP 每年跑数十万次在线 A/B 实验, 用类似本单元的预注册+环境锁定机制保证实验可复现与可审计; Bing/Office/Azure 实验结果需可复现才能上线. |
| **McKinsey** | McKinsey Global Institute (MGI) 经常发布"行业学术全景"白皮书, 其方法论本质就是本单元的 arxiv 文献计量 + networkx 合作网络 + 关键词共现社区检测 -- "学术尽职调查"是咨询项目立项的标准前置步骤. | 面向 CPG/零售/金融客户的"技术全景扫描"项目: 用 Python 拉取 arXiv/Semantic Scholar 论文, 构建合作网络识别核心研究团队, 给客户出具"应合作/应招聘/应收购"建议. |
| **Hugging Face** | Hugging Face Papers (papers.huggingface.co) 是 AI 论文社交分发的标杆平台, 其数据治理 (模型/数据集/论文唯一 ID + 开放许可) 是本单元 FAIR 原则 (Findable/Accessible/Interoperable/Reusable) 的工业实现. | Hugging Face 平台让 arXiv 论文与代码/模型/数据集互相链接, 落地 FAIR 四原则; 企业用 HF Hub 做内部研究资产管理. |
| **Neo4j** | Neo4j 是图数据库标杆, 与本单元 networkx 200 节点 3303 边作者合作网络/关键词共现网络方法天然契合 -- networkx 是研究原型, Neo4j 是生产部署. | 企业用 Neo4j 把 networkx 研究原型 (学术合作网络/技术关键词共现) 部署为生产图数据库, 支持千亿级边实时查询, 用于研发情报/人才图谱/技术雷达. |

---

## deployment_example

**真实/合理部署场景: Microsoft Research 用 arxiv + networkx 做"AI 研发情报雷达"**

- **公司**: Microsoft Research (MSR) + Microsoft ExP
- **场景**: MSR 每季度扫描 arXiv "LLM marketing" / "causal inference marketing" / "agent" 等主题新论文, 用 arxiv.py 拉 API, pandas 做文献计量 (年度增长/高产作者/主题分类), networkx 构建作者合作网络 (度中心性识别核心团队, 社区检测发现新兴方向).
- **规模**: 单次扫描 ~200-500 篇论文, 合作网络 ~500-2000 节点 / 数千-数万边 (本单元 200 节点 3303 边为其训练样本).
- **约束**: arXiv API 速率限制 (3 秒/请求); 多语言论文过滤; LLM 幻觉引用对抗 (必须用 arxiv 包验证).
- **效果**: 识别"应关注/应合作/应收购"的研究团队与技术方向; 预注册机制保证内部实验可审计; FAIR 原则保证研究资产可发现可复用. 该流程每季度跑一次, 是 Microsoft 技术战略评审会的输入.

---

## consulting_project

**Imperial MSc Business Analytics 风格咨询项目 (8 周, 4-5 人团队)**:

- **Partner (赞助企业)**: McKinsey (或 BCG Gamma / Bain Advanced Analytics)
- **Problem (真实业务问题)**: 赞助企业需要为客户提供一份《2026 营销 AI 学术全景与人才战略》报告. 客户 (一家全球 CPG 巨头, 类 Unilever/P&G) 想知道: 在 "causal inference marketing" 与 "LLM marketing" 子领域, 全球 Top-20 学术团队是谁? 哪些团队适合战略合作/赞助/招聘? 哪些新兴关键词簇值得提前布局?
- **Data (企业提供数据)**: 企业客户提供的内部研发关键词清单 + 目标期刊/会议清单 + 历史合作记录; 公开数据: arXiv API + Semantic Scholar API + OpenAlex.
- **Scope (8 周, 4-5 人)**:
  - W1-2: arxiv.py 拉取 3 主题真实论文元数据, pandas 文献计量基线.
  - W3-4: networkx 构建 500-2000 节点作者合作网络, 度中心性 + 社区检测, 识别 Top-20 团队.
  - W5-6: 关键词共现网络 + LLM (DeepSeek) 辅助摘要提取 + ASReview 主动学习筛选.
  - W7: OSF 预注册分析计划 + FAIR 数据治理报告 + 可复现 requirements.txt/Dockerfile.
  - W8: 最终 deliverable 评审.
- **Deliverable (交付物)**: (1) 交互式合作网络可视化原型 (networkx + matplotlib + pyvis); (2) Top-20 学术团队人才战略矩阵模型; (3) 60 页咨询报告 + 30 分钟高管演讲; (4) 可复现研究包 (代码 + 数据 + 预注册 DOI).

---

## case_study

**HBS 风格教学案例钩子**:

- **Protagonist (主角)**: Dr. Lin Wei, Head of Marketing AI at a global CPG company (类 Unilever/P&G), 前学术圈出身 (PhD in Marketing Science).
- **Decision (关键决策点)**: 公司董事会要求 Lin Wei 在 6 个月内决定: 是 (A) 与某 arXiv 合作网络度中心性 Top-1 学术团队签订 5 年战略合作 (高沉没成本, 高知识锁定), 还是 (B) 同时赞助 5 个度中心性 Top-20 团队做分布式布局 (低成本, 但知识碎片化), 还是 (C) 自建内部研究团队 (最高控制权, 但招聘周期长).
- **Tension (核心张力/两难)**:
  - 学术vs商业: Top-1 学术团队的研究方向 (因果推断理论) 与公司短期 KPI (LLM 营销转化率) 不完全对齐.
  - 锁定vs分散: 5 年战略合作带来深度知识壁垒, 但锁定风险高; 分布式赞助灵活但难以形成护城河.
  - 可复现vs速度: 严格 OSF 预注册 + FAIR 治理会拖慢迭代, 但跳过会面临"幻觉引用"与"不可复现实验"风险.
  - LLM辅助vs人工验证: 用 DeepSeek/ASReview 加速文献综述, 但必须用 arxiv 包对抗幻觉, 增加 QA 成本.

---

## guest_lecture

**客座讲座**:

- **Topic (主题)**: 《From arXiv to Boardroom: How Bibliometric Networks Inform AI Strategy at Microsoft Research》-- 从 arXiv 论文合作网络到董事会 AI 战略决策.
- **Speaker Profile (主讲人画像)**: Dr. Jamie Tan, Principal Research Manager at Microsoft Research, ExP (Experimentation Platform) 负责人. 背景: PhD in Statistics (Causal Inference), 10 年工业界 A/B 测试经验, 维护 lukasschwab/arxiv.py 的内部 fork, 在 OSF 预注册过 50+ 在线实验. 个人研究方向: LLM 辅助研究 Trajectory 评估 (RAGAS).
- **衔接本单元**: 主讲人会展示 MSR 内部如何用本单元的 arxiv + pandas + networkx 流水线 (本单元 200 节点 3303 边为其训练样本) 做季度研发情报扫描, 并讨论 OSF 预注册/FAIR/ASReview 在工业界的真实落地 vs 学术理想.

---

## internship_pointer

**实习/驻留指针**:

- **机构 (Institution)**: Microsoft Research (MSR) AI Resident / OpenAI Residency / Google AI Resident / Hugging Face Intern (Research) / McKinsey Data Science Intern
- **角色 (Role)**: AI Resident (Research) -- 研究 LLM 辅助研究轨迹 (Trajectory) 与可复现实验方法.
- **衔接 (Bridge)**: 本单元为该角色做准备的具体路径:
  1. **方法论基础**: 本单元的 IMRaD / positivism-interpretivism-pragmatism / Creswell 研究设计 -- Resident 需快速阅读论文并写文献综述.
  2. **工具链熟练**: arxiv.py / pandas / networkx / matplotlib -- Resident 日常拉论文做综述的标准工具.
  3. **可复现研究素养**: OSF 预注册 / FAIR / requirements.txt / Dockerfile / random_state=42 -- Resident 提交论文到 NeurIPS/ICML 必须满足的可复现标准.
  4. **前沿衔接**: ASReview (主动学习文献综述) / DeepSeek + Trajectory (LLM 辅助研究) / RAGAS (轨迹评估) -- Resident 进入 LLM 辅助研究方向的入口.
  5. **作品集**: 本单元的 solution.ipynb (200 节点 3303 边合作网络) + research.md (IMRaD 大纲 + 可复现清单) 可作为 Resident 申请的作品集材料.
