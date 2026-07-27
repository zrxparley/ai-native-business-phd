# 技能1 · Day 2：营销数据表示实战 + 多模态大模型演进 · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 技能1 表示工程与营销智能 · Day 2
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：营销对象（客户/产品/内容/行为）如何编码为向量？多模态大模型如何从CLIP演进到GPT-4o？
> **v5.0 升级点**：① 真实库上机（sentence-transformers / transformers CLIP / torch Two-Tower）② 新增 TODO 填空式起始笔记本 ③ Notebook 化 ④ 深链阅读 ⑤ 2026 前沿（CLIP对比学习 -> GPT-4o原生多模态 -> LLaVA开源）

---

## 学习目标（学完你能做到）

1. 能解释营销场景四大表示类型（客户嵌入/产品嵌入/内容嵌入/跨域对齐）的编码方法和核心挑战，并说明异构信息融合的"分通道编码+拼接+MLP映射"策略
2. 能用 **sentence-transformers** 将客户行为文本、产品描述、营销文案编码为语义向量，并用 cosine 相似度做检索、用 KMeans 做分群
3. 能用 **PyTorch** 实现 Two-Tower 双塔模型，理解 InfoNCE 对比损失如何让客户向量和产品向量在共享空间中对齐
4. 能用 **transformers CLIPModel** 做图文对齐（产品图片-描述匹配），理解对比学习双塔架构的数学原理与温度参数 τ 的作用
5. 能梳理从 CLIP（对比学习对齐）-> BLIP-2（Q-Former桥接）-> GPT-4o（原生多模态）-> LLaVA（开源）的演进路线，并指出每个阶段的营销应用与局限

---

## 理论部分：精炼索引（详见独立教材）

> Day 2 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_技能1_表示工程与营销智能.md` § Day 2](../../AI原生化商业博士_独立教材_技能1_表示工程与营销智能.md)（3.2.1–3.2.4 节，已包含四大表示类型/Two-Tower模型/CLIP到GPT-4o多模态演进/sentence-transformers代码示例）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：四大表示类型

| 表示类型 | 信息来源 | 编码方法 | 营销应用 |
|:--------:|---------|---------|---------|
| 客户嵌入 | 行为序列/交易/人口统计/文本反馈 | 序列模型+NLP+MLP融合 | 客户分群、个性化推荐 |
| 产品嵌入 | 属性/描述/图片/关系/评价 | NLP+CNN/ViT+图嵌入 | 相似产品检索、交叉推荐 |
| 内容嵌入 | 广告文案/文章/视频/图文 | sentence-transformers/CLIP | 相似文案推荐、内容检索 |
| 跨域对齐 | 客户-产品-内容跨空间 | Two-Tower对比学习/共享投影 | 客户-产品匹配（推荐核心） |

**核心挑战**：客户嵌入空间和产品嵌入空间分开训练时不"对齐"——直接计算余弦相似度没有意义。跨域对齐通过共享空间投影或对比学习，让客户和产品的 embedding 在同一空间可直接比较，这样"客户向量与产品向量的余弦相似度"就能直接预测购买概率。

### 关键回顾 2：Two-Tower 模型架构

```
客户特征 ──-> Tower A (MLP) ──-> 客户向量 u ─┐
                                            ├──-> cos(u,v) = u·v/(||u||·||v||)
产品特征 ──-> Tower B (MLP) ──-> 产品向量 v ─┘
```

**InfoNCE 损失**（对比学习核心）：
```
L = -log[ exp(sim(u, v⁺)) / Σ exp(sim(u, vᵢ)) ]
```
- v⁺ 是正样本（客户实际购买的产品），vᵢ 包括正样本和所有负样本产品
- 让正样本相似度高、负样本相似度低——本质是一个多分类问题
- **负采样**：从全量产品中随机采样作为负样本，无需全部产品参与计算
- **在线服务**：产品向量预计算并建立ANN索引，实时只需计算用户向量并检索

### 关键回顾 3：从 CLIP 到 GPT-4o 的多模态演进

| 阶段 | 代表方法 | 核心思想 | 营销应用 |
|:----:|---------|---------|---------|
| 对比学习对齐 | CLIP (2021) | 双塔架构，对比损失对齐图文 | 商品图文匹配、多模态搜索 |
| 视觉-语言预训练 | BLIP-2 (2023) | Q-Former桥接冻结视觉编码器和LLM | 图片理解+文案生成 |
| 原生多模态 | GPT-4o/Gemini (2024-2025) | 端到端统一token空间，非拼接 | 自动广告创意生成、视频理解 |
| 开源多模态 | LLaVA (2024) | CLIP-ViT+投影层+LLM | 低成本多模态方案 |

**CLIP 核心创新**：用对比学习将图像和文本对齐到同一向量空间。训练N个图文对，计算 N×N 相似度矩阵，最大化对角线（匹配对）、最小化非对角线（不匹配对）。对称 InfoNCE 损失中温度参数 τ 控制区分敏感度——τ 越小，模型对正确匹配的"信心"越强。

**本质转变**：CLIP 是"双塔"（编码后对齐），GPT-4o 是"原生多模态"（统一token空间，无对齐步骤）。GPT-4o 能理解跨模态细微关联（如图中红色文字与描述语气是否一致），这对企业营销意义重大——可以直接"看"广告图片、"读"文案、"听"配乐，给出整体评价。

---

## 上机部分：用真实库构建营销表示

> 📓 **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO 填空版，你来做）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，gated，做完再看）
> 📊 **真实数据/库**：[`data/README.md`](./data/README.md)（sentence-transformers / transformers CLIP / torch + 美妆电商营销数据）

### 为什么用真实库而非手写TF-IDF

v4.0 的代码用"手写TF-IDF+numpy"做文本表示——TF-IDF 无法理解语义（"跑步鞋"和"运动鞋"的词不重叠，TF-IDF 相似度为0，但语义高度相关）。v5.0 改用真实预训练模型：

- **sentence-transformers**：基于 BERT/RoBERTa 预训练，将文本编码为384维语义向量，"提亮精华"和"烟酰胺"的余弦相似度自然很高
- **transformers CLIPModel**：OpenAI CLIP 的 HuggingFace 实现，图文对齐的真实可运行代码
- **torch**：Two-Tower模型的工业级实现，InfoNCE损失+负采样

> **推理成本提示**：CLIP 模型（`openai/clip-vit-base-patch32`）约600MB，首次运行需下载。sentence-transformers 的 `paraphrase-multilingual-MiniLM-L12-v2` 仅约470MB，CPU即可推理。生产部署可用 ONNX 量化降低推理成本。

### 营销映射（关键桥接）

本 Day 为一个"美妆电商"构建四大表示，所有数据围绕真实营销场景：

| 表示类型 | 营销场景 | 真实库实现 |
|---------|---------|-----------|
| 客户嵌入 | 客户行为文本->向量->KMeans分群 | sentence-transformers + sklearn |
| 产品嵌入 | 产品描述->向量->cosine相似度检索 | sentence-transformers + sklearn |
| 内容嵌入 | 营销文案->向量->相似文案推荐 | sentence-transformers |
| 跨域对齐 | 客户-产品匹配检索 | torch Two-Tower + InfoNCE |
| 图文对齐 | 产品图片-描述匹配 | transformers CLIPModel |

### 上机任务（6 个 TODO，见 starter.ipynb）

1. **TODO1**：客户 embedding（行为文本->向量+KMeans分群+Silhouette选K）
2. **TODO2**：产品 embedding（产品描述->向量+cosine相似度检索）
3. **TODO3**：内容 embedding（营销文案->向量+相似文案推荐）
4. **TODO4**：Two-Tower 双塔模型（torch实现，客户-产品匹配检索+InfoNCE损失）
5. **TODO5**：CLIP 图文对齐（transformers CLIPModel，产品图-文相似度矩阵）
6. **TODO6**：多模态演进分析表（CLIP->BLIP-2->GPT-4o->LLaVA，对比架构/能力/营销应用）

---

## 2026 前沿补充：从 CLIP 对比学习到 GPT-4o 原生多模态

> v5.0 新增前沿点。多模态AI在2021-2025年经历了四阶段快速演进。理解这条路线对于设计企业级多模态营销系统至关重要。

**CLIP（2021）**：对比学习双塔架构。图像编码器和文本编码器各自编码后，用对称InfoNCE对比损失对齐到同一空间。优点：训练高效、检索方便（预计算向量+ANN索引）。缺点：只能做匹配，不能生成；细粒度视觉理解受限。

**BLIP-2（2023）**：Q-Former桥接冻结的视觉编码器和冻结的LLM。Q-Former学习一组"查询token"提取视觉特征，再输入LLM做生成。优点：复用预训练LLM，训练成本低。缺点：Q-Former是信息瓶颈，细粒度视觉理解受限。

**GPT-4o/Gemini（2024-2025）**：原生多模态——文本、图像、音频在统一的token空间中处理，不存在"编码后对齐"步骤。能理解跨模态细微关联（如图中文字与描述语气是否一致）。对企业营销的意义：可以直接"看"广告图片、"读"文案、"听"配乐，给出整体评价——这比分别分析图文再拼接的传统方案强大得多。

**LLaVA（2024）**：开源视觉-语言模型。架构 = CLIP-ViT视觉编码器 + 线性投影层 + Vicuna/LLaMA LLM。用GPT-4生成的图文指令数据训练。优点：开源可私有化部署，适合数据敏感的营销场景。缺点：能力不及GPT-4o，但差距在缩小。

**对比学习是贯穿全程的底层技术**：CLIP用对比学习对齐图文，Two-Tower用对比学习对齐客户-产品，sentence-transformers用对比学习微调文本编码器。理解InfoNCE损失，就理解了现代表示学习的核心。

> 🔗 深入阅读见 [`reading.md`](./reading.md) 的 CLIP / BLIP-2 / LLaVA 条目。

---

## 与后续 Day 的衔接

- **Day 3**：企业知识图谱 + GraphRAG——今天的向量表示是知识图谱的"软"表示，Day 3 补充"硬"关系表示
- **Day 4**：RAG与检索增强——今天的 embedding 检索是 RAG 的基础组件
- **Day 5**：表示工程评估——今天的 cosine 相似度检索质量需要系统化评估

---

## 作业与评估

作业、5 分制量表、费曼演练、2 分钟话术、复盘自诊表——沿用独立教材 § Day 2 既有设计。本学习材料包不重复，仅新增上机交付物：

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6 个 TODO 全部填好，能跑通）
- [ ] 一段 300 字分析：你的营销场景中，四大表示类型哪个最难构建？瓶颈在数据、模型还是融合策略？
- [ ] （可选）用 CLIP 对一张真实产品图片做图文匹配实验，分析匹配错误的原因（背景干扰/角度/风格偏差）

---

*本讲义由 v5.0 学习材料包升级生成。理论部分引用独立教材，上机部分用真实库（sentence-transformers/transformers CLIP/torch）+ TODO 脚手架。*
*最后更新：2026-07-24*

---

## 学习科学层 (v6.0)

> v6.0 增量: 用学习科学把"练习"升级为"刻意练习 + 间隔重复 + 建构对齐 + 牛津 tutorial 仿真"。
> 研究依据: Ericsson 刻意练习 / FSRS-6 + SM-2 间隔重复 / Biggs 建构对齐 / Hattie 四级 formative feedback / Oxford tutorial Socratic / MIT 6.5940 渐退示例 (Worked-Faded) + 交叉 (interleaving A1B1C1) / Butler 2010 检索练习 (spaced retrieval)。

### 刻意练习 (deliberate practice)
本单元的 6 个 TODO 不再是"做完即过", 而是分解为 3 subskill × 3 drill (D1/D2/D3), 每 drill 有 difficulty / reps_required / feedback_rule, feedback_rule 直接引用本单元真实库因果链 (sentence-transformers 语义嵌入 / torch Two-Tower + InfoNCE 对比学习 / transformers CLIP 对称损失 / 温度参数 τ)。详见 [`practice.md`](./practice.md)。

### 间隔重复 (spaced retrieval, FSRS-6 / SM-2)
本单元核心概念 (四大表示类型 / sentence-transformers / Two-Tower InfoNCE / CLIP 对比学习 / CLIP->GPT-4o 演进 / 对比学习贯穿性) 进入 FSRS-6 调度, 间隔日 [1,3,8,21,60,180], request_retention=0.9, EF₀=2.5 (SM-2 备份)。详见 [`schedule.json`](./schedule.json)。

### 建构对齐 (constructive alignment, Biggs)
5 ILO ↔ TLA (starter.ipynb TODO + drill + tutorial Socratic) ↔ AT (progressive_project P1-P4 gate + solution.ipynb) 矩阵对齐, 每 ILO 有 mastery_threshold, 过 Biggs 三自检 (Feed Up / Feed Back / Feed Forward)。详见 [`alignment.md`](./alignment.md)。

### 牛津 tutorial 仿真 (Oxford tutorial, Socratic, Hattie)
[`tutorial.ipynb`](./tutorial.ipynb) 用 Oxford fellow persona + Socratic 追问 (5 轮, 永不直接给答案) + devil's advocate + student_model.json 跨单元画像 + Hattie 四级反馈 [TASK]/[PROCESS]/[SELF-REG]/[FEED-FORWARD] (省略 Self 级表扬, 因 Hattie 研究表明其近 0 效应) + 限频 1 次/天防依赖。

### mastery 与弱项循环 (weak loop)
每 drill 连续 2 次失败触发 weak_loop: 回退到上一 difficulty + 补充 worked example + 触发 tutorial Socratic 追问。学生画像写入 student_model.json, 跨单元连续追踪。

### 与 v5.0 的衔接
v5.0 的 7 条验收 (notes.md / data/README.md / starter.ipynb / solution.ipynb / reading.md / 前沿点) 全部保持不变, v6.0 只在 notes.md 末尾追加本节, 并新增 4 个文件 (practice.md / schedule.json / alignment.md / tutorial.ipynb)。v5.0 基线 + v6.0 学习科学层 = 12/12 收敛。

---

## 研究产出与产业链接层 (v7.0)

本单元产出可发表研究工件 (research.md: 研究问题 + 贡献声明 + arXiv 链接 + IMRaD 大纲 + NeurIPS 可复现清单 + research-to-practice 翻译) 与产业链接 (industry.md: >=3 真实企业 + 部署场景 + Imperial 咨询项目 + HBS 教学案例 + 客座讲座 + 实习指针)。研究产出遵循 IMRaD / DSR (Hevner) / OSF 预注册 (preregistration) / FAIR / 可复现研究 (reproducibility) 标准; 产业链接遵循 Imperial MSc BA 咨询项目 (consulting, Burberry/Expedia/J&J) / HBS 案例法 (case study) / MIT Sloan 行动学习 (action learning) 模式。linked_paper 锚定 CLIP (arXiv 2103.00020) + Sentence-BERT (1908.10084) + InfoNCE/CPC (1807.03748) + BLIP-2 (2301.12597) + LLaVA (2304.08485)。deployment 锚定 Stitch Fix / Sephora / Adobe Sensei / Meta Ads / Unilever。详见 research.md 与 industry.md。
