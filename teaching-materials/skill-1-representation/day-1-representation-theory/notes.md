# 技能1 · Day 1：表示学习理论基础 + DSR框架 · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 技能1 表示工程与营销智能 · Day 1
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：AI如何"理解"企业的客户、产品与内容？--从"标签"到"向量"的范式转移
> **v5.0 升级点**：① 新增真实库上机（sentence-transformers + scikit-learn + torch）② 新增 TODO 填空式起始笔记本 ③ Notebook 化 ④ 深链阅读 ⑤ 2026 前沿（Representation Engineering + Neural Collapse）

---

## 学习目标（学完你能做到）

1. 能解释从 `f(x)=wᵀφ(x)` 到 `f(x)=wᵀφ_θ(x)` 的范式转移核心：表示函数 `φ` 从人工设计变为数据驱动学习，并说明这对营销场景意味着什么（从手工特征到自动发现行为模式）
2. 能阐述 CMU 10741 的三个核心概念--不加约束的表示学习没有意义、Neural Collapse、不可辨识性--并指出各自对客户分群和 embedding 工程的实践启示
3. 能区分 Autoencoder / VAE / GAN / Normalizing Flow 四种表示学习方法的设计哲学、核心公式和营销应用场景
4. 能用 **sentence-transformers** 将营销文本（产品评论/用户反馈）编码为 384 维 embedding，用 **scikit-learn** 做 t-SNE/PCA 降维可视化和 KMeans 聚类，用 **torch** 实现自编码器压缩表示
5. 能用 **DSR 六步框架**（Hevner 2004 / Peffers 2007）定义"企业表示工程"的研究问题，把工程实践转化为有学术贡献的研究设计

---

## 理论部分：精炼索引（详见独立教材）

> Day 1 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_技能1_表示工程与营销智能.md` § Day 1](../../AI原生化商业博士_独立教材_技能1_表示工程与营销智能.md)（3.1.1–3.1.6 节，已包含范式转移/CMU概念/Autoencoder-VAE-GAN-Flow/非线性降维/CS224N对标/DSR六步框架）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：范式转移 -- 从手工特征到端到端学习

| 维度 | 传统范式 `f(x)=wᵀφ(x)` | 端到端范式 `f(x)=wᵀφ_θ(x)` |
|------|----------------------|--------------------------|
| 表示函数 φ | 人工设计、固定 | 数据驱动学习（θ 是可训练参数） |
| 营销特征 | "过去30天浏览次数""购物车金额" | 从原始行为序列自动学习行为模式 |
| 粒度 | 粗（几十维） | 细（数百维） |
| 更新 | 静态 | 动态（每次行为微调） |

**核心洞察**：端到端学习能捕捉手工特征难以表达的"比较后收藏但未购买 = 等待降价意图"这类序列模式。

### 关键回顾 2：CMU 10741 三个核心概念

**概念一：不加约束的表示学习没有意义**

如果不施加维度限制等约束，模型可以把每个样本映射为独立的"记忆"（lookup table），退化成记忆而非学习。真正的表示学习必须用约束（如限制为 128 维）迫使模型发现数据的**潜在结构**。

营销含义：把每个客户映射为 10000 维向量只记录行为，不是表示学习；用 128 维捕捉行为模式的结构性规律，才是。

**概念二：Neural Collapse**（Papyan et al., 2020, arXiv 2008.08186）

分类网络训练后期，最后一层特征呈现特殊几何结构：类别内方差趋零、类别间距离最大化、特征与分类器对齐。这说明好的表示让"相似的聚在一起，不同的分开"--分类模型的倒数第二层特征天然适合做客户分群。

**概念三：不可辨识性（Non-identifiability）**

不同随机种子训练的 embedding 数值不同但语义等价。实践含义：不能解释单个维度（"第47维=购买力"无意义），应关注几何关系（余弦相似度、点积）。

### 关键回顾 3：四种表示学习方法

| 方法 | 核心公式 | 设计哲学 | 营销应用 |
|------|---------|---------|---------|
| Autoencoder | `z=f_enc(x), x'=f_dec(z), L=‖x-x'‖²` | 压缩-重建瓶颈 | 客户行为日志压缩 |
| VAE | `z~N(μ,σ²), L=E[‖x-x'‖²]+KL(q‖p)` | 概率框架+KL正则 | 客户画像生成 |
| GAN | `min_G max_D E[log D(x)]+E[log(1-D(G(z)))]` | 对抗训练 | 广告创意生成 |
| Normalizing Flow | `log p(x)=log p(z₀)+Σ log|det J|` | 可逆变换精确密度 | 欺诈检测（精确概率） |

### 关键回顾 4：非线性降维方法

| 方法 | 核心思想 | 营销应用 |
|------|---------|---------|
| MDS | 保持点对距离 | 品牌感知图 |
| Isomap | 测地线距离替代欧氏距离 | 非线性客户结构 |
| LLE | 局部线性关系保持 | 客户子群体发现 |
| t-SNE | t分布解决拥挤问题 | 客户分群可视化 |

**t-SNE 为什么用 t 分布**：t 分布有更重的尾巴，低维空间中远距离的点不会过度排斥，解决了"中等距离的点降维后全挤一起"的拥挤问题。

### 关键回顾 5：DSR 六步框架

设计科学研究（Design Science Research）是信息系统领域的核心研究范式，通过设计和评估 artifact 产生新知识。Peffers 等人（2007）提出六步流程：

| 步骤 | DSR 框架 | 在企业表示工程中的内容 |
|:----:|---------|---------------------|
| 1 | 问题识别与动机 | 从"标签"到"向量"的 gap |
| 2 | 定义解决方案目标 | 统一表示框架（客户/产品/内容） |
| 3 | 设计与开发 | embedding系统 + Two-Tower + 对比学习 |
| 4 | 演示 | 在真实营销场景中验证 |
| 5 | 评估 | Recall@K / Silhouette / 跨域匹配准确率 |
| 6 | 传播 | IMRaD 论文投稿 |

**关键思考**：DSR 让工程实践有了学术贡献框架--不是"我做了一个系统"，而是"我设计了一个新的表示工程框架，通过系统化评估验证了有效性"。

---

## 上机部分：用真实库构建营销文本表示学习

> 📓 **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO 填空版，你来做）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，gated，做完再看）
> 📊 **真实数据/库**：[`data/README.md`](./data/README.md)（sentence-transformers + scikit-learn + torch + 营销评论数据）

### 为什么用真实库而非手写脚本

v4.0 的代码用"手写特征工程"演示概念。v5.0 改用工业级真实库：

- **sentence-transformers**（UKPLab/sentence-transformers，18.9k★，Apache-2.0）：`SentenceTransformer('all-MiniLM-L6-v2')` 将营销文本编码为 384 维 embedding，模型已用对比学习 fine-tune，embedding 空间的余弦相似度直接反映语义相似度
- **scikit-learn**：t-SNE/PCA 降维、KMeans 聚类、silhouette_score 评估--工业标准工具链
- **torch**：实现 Autoencoder，理解"压缩-重建"瓶颈如何迫使网络丢弃冗余信息

### 营销映射（关键桥接）

本 Day 处理一个"营销文本表示学习"场景：20 条产品评论（护肤/电子/健身三类 × 正面/负面两种情感），用 embedding 编码后做降维可视化、自编码器压缩、聚类分群、下游分类评估：

| 上机任务 | 营销场景 | 真实库实现 |
|---------|---------|-----------|
| 文本编码 | 将产品评论编码为向量 | sentence-transformers |
| 降维可视化 | 观察正负面评论的聚类结构 | scikit-learn t-SNE/PCA |
| 自编码器 | 压缩 embedding 理解重构损失 | torch Autoencoder |
| 聚类分群 | 发现客户/产品分群 | scikit-learn KMeans + silhouette |
| DSR 框架 | 定义"企业表示工程"研究问题 | 六步结构化定义 |
| 表示评估 | 下游分类准确率对比不同 embedding | scikit-learn LogisticRegression |

### 上机任务（6 个 TODO，见 starter.ipynb）

1. **TODO1**：用 sentence-transformers 编码 20 条营销评论为 384 维 embedding，查看维度
2. **TODO2**：用 t-SNE/PCA 降维可视化，观察正负面评论聚类结构
3. **TODO3**：用 torch 实现 Autoencoder 压缩 embedding（384→64），理解重构损失
4. **TODO4**：用 KMeans 聚类发现评论分群，silhouette 评估最优 K
5. **TODO5**：用 DSR 六步框架定义"企业表示工程"研究问题
6. **TODO6**：评估表示质量（下游情感分类准确率 + silhouette 对比不同维度表示）

---

## 2026 前沿补充：Representation Engineering + 多模态表示演进

> v5.0 新增前沿点。本 Day 覆盖两个前沿方向：① 表示工程（RepE）--自上而下的 AI 透明性 ② 多模态表示演进--从 CLIP 到 GPT-4o 的表示对齐路径。

### Representation Engineering（RepE）

表示工程（Representation Engineering, RepE）是 MIT/Center for AI Safety 等机构提出的一种**自上而下的 AI 透明性方法**（Zou et al., 2023, arXiv 2310.01405），通过操控神经网络内部的高层表示来实现对模型行为的监测和干预。

**核心思想**：传统的可解释性研究是"自下而上"的（研究单个神经元或电路），RepE 是"自上而下"的--直接研究**群体级表示**（population-level representations），通过读取和操纵这些表示来监测模型的"认知状态"（诚实性、有害性、权力寻求等）。

**对营销 AI 的启示**：
- **表示监测**：可以监控营销 Agent 的内部表示是否"诚实"（生成文案时是否在"想"虚构信息），比只看输出文本更早发现幻觉
- **表示操控**：可以通过调整内部表示来引导模型行为（如增强"品牌调性"方向的表示，抑制"夸大宣传"方向的表示）
- **与 Day 1 理论的连接**：RepE 的理论基础正是本 Day 学习的"表示学习"--只有理解了 embedding 空间的几何结构，才能理解如何读取和操纵表示

> ⚠️ RepE 对应因果阶梯的 L1（对表示的关联分析），不能替代真实业务指标（L2 A/B 测试）。定位为"开发期透明性工具"。
> 🔗 深入阅读见 [`reading.md`](./reading.md) 的 Representation Engineering 条目。

### 多模态表示演进：从 CLIP 到 GPT-4o

表示学习不仅限于文本。多模态表示学习的核心是**跨模态对齐**--让不同模态（文本、图像、音频）的表示在同一个向量空间中可比较。这条演进路径对营销场景至关重要（产品图片 + 文案 + 用户行为的统一表示）：

| 阶段 | 代表方法 | 核心思想 | 与 Day 1 的理论连接 |
|------|---------|---------|-------------------|
| 对比学习对齐 | **CLIP**（OpenAI, 2021） | 双塔架构 + 对比损失对齐图文 | InfoNCE 损失 = 本 Day 的对比学习原理 |
| 视觉-语言预训练 | **BLIP-2**（Salesforce, 2023） | Q-Former 桥接视觉编码器和 LLM | 表示的瓶颈设计 = 本 Day 的 Autoencoder |
| 开源多模态 | **LLaVA**（2024） | CLIP-ViT + 投影层 + LLM | 表示投影 = 本 Day 的降维思想 |
| 原生多模态 | GPT-4o/Gemini（2024-2025） | 端到端多模态训练 | 统一表示空间 = Day 1 范式转移的终态 |

**关键洞察**：CLIP 用对比学习（contrastive learning）将图像和文本对齐到同一向量空间--这正是 Day 1 TODO4 中 KMeans 聚类所依赖的"相似样本距离近、不同样本距离远"原则的工业级应用。BLIP-2 的 Q-Former 本质上是一个学习到的"表示瓶颈"，与本 Day TODO3 的 Autoencoder 设计哲学一脉相承。LLaVA 用投影层将视觉表示映射到语言模型空间，这是降维投影思想的扩展。

---

## 与后续 Day 的衔接

- **Day 2**：营销数据表示实战 + 多模态演进--今天的 embedding 基础将扩展到客户/产品/内容三大对象的向量化表示 + Two-Tower 跨域对齐
- **Day 3**：企业知识图谱 + GraphRAG--今天的"向量表示"将与"图表示"互补，向量擅长相似度匹配，图擅长关系推理
- **Day 4**：多模态融合与跨域对齐--今天的单模态文本表示将扩展到图文多模态融合

---

## 作业与评估

作业、5 分制量表、费曼演练、2 分钟话术、复盘自诊表--沿用独立教材 § Day 1 既有设计。本学习材料包不重复，仅新增上机交付物：

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6 个 TODO 全部填好，能跑通）
- [ ] 一段 300 字分析：你的营销评论 embedding 在 t-SNE 降维后呈现什么聚类结构？正负面评论是否清晰分离？Autoencoder 压缩后信息损失多大？
- [ ] （可选）用 DSR 六步框架为你自己的业务场景写一份一页纸研究计划（800-1000 字）

---

*本讲义由 v5.0 学习材料包升级生成。理论部分引用独立教材，上机部分用真实库（sentence-transformers + scikit-learn + torch）+ TODO 脚手架。*
*最后更新：2026-07-24*

---

## 学习科学层 (v6.0)

> 本节为 v6.0 学习科学升级追加, 不改 v5.0 原文一字。基于 4 agent 调研合成 (NUS + MIT + Oxford + Harvard/Stanford)。

### 设计哲学增量
- v5.0: 真实即严谨 · 练习即掌握
- v6.0: **科学即高效 · 反馈即成长** -- 用学习科学把"练习"升级为"刻意练习 (deliberate practice) + 间隔重复 (spaced retrieval) + 建构对齐 (constructive alignment) + 牛津 tutorial (Socratic)"

### 4 个新文件
1. `practice.md` -- Ericsson 刻意练习 (deliberate practice) 5 要素 + MIT 6.5940 Worked-Faded 渐退示例 + CS229 pset0 诊断性先测 + CS230 渐进项目脚手架 + 交叉 (interleaving) A1B1C1...B2C2A2...C3A3B3 明文排布 + retry_policy + weak_loop
2. `schedule.json` -- FSRS-6 间隔重复 (request_retention=0.9, SM-2 备份 EF₀=2.5, I(1)=1, I(2)=6), 6 张卡片覆盖范式转移 / Neural Collapse / sentence-transformers / 四方法 / RepE / DSR
3. `alignment.md` -- Biggs 建构对齐 (constructive alignment) ILO↔TLA↔AT 矩阵 3 行 + mastery 阈值 + 3 自检 (Feed Up / Feed Back / Feed Forward)
4. `tutorial.ipynb` -- 牛津 tutorial (Oxford tutorial) LLM 仿真: Socratic 追问 (禁直接答案) + Hattie 四级 formative feedback ([TASK]/[PROCESS]/[SELF-REG]/[FEED-FORWARD]) + student_model.json 跨单元复用 + 限频 1 次/天

### 研究依据
- **Ericsson**: 刻意练习 5 要素 (specific goal + feedback + repetition + challenge + scaffold)
- **FSRS-6**: 开源间隔重复算法, request_retention=0.9, 21 weights; SM-2 备份 (EF₀=2.5)
- **Biggs**: 建构对齐 -- ILO ↔ TLA ↔ AT 三者必须对齐, 不经 TLA 能过 AT = 对齐失败
- **Hattie (2007, Educational Researcher 77(1):81-112)**: formative feedback 3 问 (Feed Up/Back/Forward) × 4 级 (Task/Process/Self-Reg/Feed-Forward), 避免 Self 级表扬 (d=0.14 最弱)
- **MIT 6.5940**: mastery 阈值 "至少 4/5 实验提交方可及格" + 间隔与交叉练习 + Worked-Faded 渐退示例
- **Oxford tutorial / Cambridge supervision**: 1 对 1-3 + 每周 + 强制 + 口头辩护, LLM 仿真用 Socratic 追问 (arXiv 2024-2025: 2409.05511 / 2507.05795 / 2508.21204 / 2508.06583 / 2502.12633 / 2505.21582)
- **Harvard CS230**: 渐进项目脚手架 (proposal->milestone->final->poster) + retry 政策 (10 late days, 失败不罚)
- **Butler 2010**: 检索练习 (retrieval practice) 证据 -- 推断题 68% > 重学 44%

### 收敛条件
- v5.0 基线 (1-7): `verify_unit.py` 全通过 (7/7)
- v6.0 新层 (8-12): `verify_v6_unit.py` 全通过 (5/5)
- 整单元: 12/12 收敛

---
*v6.0 学习科学层追加完成 · 2026-07-25 · 不改 v5.0 原文一字*

---

## 研究产出与产业链接层 (v7.0)

本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+arXiv链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。详见 research.md 与 industry.md。

- **研究产出 (research output)**：linked_paper 锚定 Zou 2023 (RepE, arXiv 2310.01405) + Papyan 2020 (Neural Collapse, arXiv 2008.08186)；IMRaD 大纲基于 20 条营销评论 + sentence-transformers 384 维 + torch Autoencoder 64 维压缩；可复现 (reproducibility) 清单 8 项 (code/data/seed/environment/preregistration/FAIR/weights/evaluation)。
- **产业链接 (industry linkage)**：>=3 真实企业 (Stitch Fix/Sephora/Hugging Face/Salesforce/Spotify)；咨询 (consulting) 项目 partner 为 Sephora (8 周 4-5 人, DSR 六步)；HBS 案例 (case study) protagonist 为 Stitch Fix Head of AI；客座讲座 (guest lecture) 主讲人为 Hugging Face ML Engineer；实习 (internship) 指针指向 Hugging Face/OpenAI Residency/Google AI Resident/Stitch Fix Capstone。

---
*v7.0 研究产出与产业链接层追加完成 · 2026-07-26 · 不改 v5.0/v6.0 原文一字*

---

## 学术前沿层 (v9.0)

本单元新增 `frontier.md`：注入 2025-2026 最新学术前沿（N 篇真实 arXiv 论文 + 批判性综述 + delta_to_unit + ≥3 开放研究问题 + 方法论批评）。论文来自 `_frontier_corpus/skill-1-representation.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证），覆盖前沿课题：表示工程 × 多模态对齐 × 检索蒸馏。面向博后/教授级读者：批判性综述非罗列，delta_to_unit 显式指出前沿如何更新本单元所教，开放问题为可发表研究方向。详见 `frontier.md`。

---

## AI工程从零构建层 (v11.0)

> v11.0 新增 [`from_scratch.md`](./from_scratch.md)：AI工程从零构建，与本单元 sentence-transformers + scikit-learn + torch 形成对照。
> - **从零构建主题**：手写 word2vec SGNS + SVD 降维
> - **核心算法**：Skip-gram 负采样损失 $\mathcal{L}_{\text{SGNS}} = -\log\sigma(\mathbf{v}'_c \cdot \mathbf{v}_w) - \sum_{n} \log\sigma(-\mathbf{v}'_n \cdot \mathbf{v}_w)$ + 截断 SVD $X_k = U_k \Sigma_k V_k^T$（含数学推导 + LaTeX）
> - **code_artifact**：手写 numpy 骨架，imports ⊆ {numpy, collections}，附 verification_property
> - **延伸阅读**：rohitg00 AI工程 from scratch P5/03 Word Embeddings Word2Vec + P1/11 SVD
> - **手写实现要点**：用 from-scratch numpy SGNS + SVD 而非 sentence-transformers + sklearn PCA，理解到金属层
> - **verification_property**：共现词对余弦相似度 > 非共现词对；SVD 降维输出 (V, k)
