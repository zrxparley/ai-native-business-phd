# Day 1 深链阅读清单

> v5.0 升级：从"课程主页"升级为**经验证的深链**（指向具体论文 / 文档 / 仓库，非主页）。全部链接已验证存在。

---

## ① 表示学习理论

### Neural Collapse（Papyan et al., 2020, PNAS）
- 📄 arXiv 2008.08186：https://arxiv.org/abs/2008.08186
- **用法**：Day 1 理论回顾的核心概念来源。Neural Collapse 揭示了分类网络训练后期最后一层特征的几何结构（NC1 类内方差趋零、NC2 类均值形成 ETF、NC3 分类器与特征对齐、NC4 最近类中心决策规则）。重点读 §1 Introduction 和 §2 The four phenomena of NC，理解为什么好的表示让"相似聚在一起，不同的分开"。

### Auto-Encoding Variational Bayes（Kingma & Welling, 2013, ICLR）
- 📄 arXiv 1312.6114：https://arxiv.org/abs/1312.6114
- **用法**：VAE 的原始论文。Day 1 TODO3 实现的是基础 Autoencoder，VAE 是其概率扩展。重点读 §2 Method，理解重参数化技巧（reparameterization trick）和 KL 散度正则项的作用。营销应用：VAE 的生成能力可以"创造"合理的客户画像用于模拟营销策略。

### Generative Adversarial Networks（Goodfellow et al., 2014, NeurIPS）
- 📄 arXiv 1406.2661：https://arxiv.org/abs/1406.2661
- **用法**：GAN 的原始论文。Day 1 理论回顾的四种表示学习方法之一。重点读 §3 Theoretical Results，理解极小极大博弈（minimax game）的均衡点。营销应用：广告创意生成、产品图片风格迁移。

---

## ② 真实库 + 上机

### sentence-transformers 官方文档与教程（已验证：UKPLab/sentence-transformers）
- 🌐 官方文档：https://www.sbert.net/ （已验证，含完整教程和模型列表）
- 📦 GitHub：https://github.com/UKPLab/sentence-transformers （18.9k★，Apache-2.0，已验证存在）
- **深链用法**：
  - [快速入门](https://www.sbert.net/docs/quickstart.html)：对标 starter.ipynb TODO1，用 `SentenceTransformer('all-MiniLM-L6-v2')` 编码文本
  - [预训练模型列表](https://www.sbert.net/docs/pretrained_models.html)：选择不同维度的 embedding 模型（384/768/1024维）
  - [多语言模型](https://www.sbert.net/docs/pretrained_models.html#multilingual-models)：中文营销文本用 `paraphrase-multilingual-MiniLM-L12-v2`

### scikit-learn 降维与聚类文档（已验证）
- 🌐 官方文档：https://scikit-learn.org/ （已验证，BSD License）
- **深链用法**：
  - [t-SNE 用户指南](https://scikit-learn.org/stable/modules/manifold.html#t-distributed-stochastic-neighbor-embedding-t-sne)：对标 TODO2，理解 perplexity 参数和拥挤问题
  - [KMeans 文档](https://scikit-learn.org/stable/modules/clustering.html#k-means)：对标 TODO4，理解 n_clusters 和 n_init 参数
  - [silhouette_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html)：对标 TODO4/TODO6，评估聚类质量

### PyTorch 自编码器教程（已验证）
- 🌐 官方网站：https://pytorch.org/ （已验证，BSD License）
- **深链用法**：对标 TODO3，用 `nn.Linear` + `nn.ReLU` 构建 Autoencoder，用 `MSELoss` 计算重构误差。PyTorch 官方有完整的 [自编码器教程](https://pytorch.org/tutorials/beginner/blitz/neural_networks_tutorial.html) 可参考。

---

## ③ 2026 前沿：Representation Engineering

### Representation Engineering: A Top-Down Approach to AI Transparency（Zou et al., 2023）
- 📄 arXiv 2310.01405：https://arxiv.org/abs/2310.01405
- **用法**：本 Day 的前沿补充。RepE 是 MIT/Center for AI Safety 等机构提出的 AI 透明性方法，通过操控神经网络内部的高层表示来监测和干预模型行为（诚实性、有害性、权力寻求等）。重点读 §2 Representation Reading 和 §3 Representation Control，理解如何读取和操纵表示。营销应用：监控营销 Agent 内部表示是否在"想"虚构信息，比只看输出文本更早发现幻觉。

### 对比学习与表示质量
- 📄 SimCLR（Chen et al., 2020）：https://arxiv.org/abs/2002.05709
- **用法**：对比学习是表示学习最重要的进展之一，也是 sentence-transformers 的训练基础。理解 InfoNCE 损失和温度参数 τ 的作用。与本 Day TODO6 的"评估表示质量"相关：好的表示应该让相似样本距离近、不同样本距离远，这正是对比学习的优化目标。

---

## ④ DSR 研究方法论

### Design Science Research 六步流程
- 📄 Peffers et al. (2007)："A Design Science Research Methodology for Information Systems Research"
- **用法**：Day 1 TODO5 用 DSR 六步框架定义"企业表示工程"研究问题。DSR 是信息系统领域的核心研究范式，强调通过设计和评估 artifact 产生新知识。六步流程：问题识别 → 目标定义 → 设计开发 → 演示 → 评估 → 传播。关键思考：DSR 让工程实践有学术贡献框架--不是"做了系统"而是"设计了新框架并验证有效性"。

### Hevner et al. (2004) DSR 原始论文
- 📄 Hevner et al. (2004)："Design Science in Information Systems Research"，MIS Quarterly
- **用法**：DSR 的奠基论文，提出了设计科学的七条准则。Peffers 2007 的六步流程是在 Hevner 2004 基础上的操作化。理解 artifact（人工制品）的概念：模型、方法、框架、原型系统都可以是 artifact。

---

## ⑤ 对标课程

### Stanford CS224N: Natural Language Processing with Deep Learning
- 🌐 课程主页：https://web.stanford.edu/class/cs224n/ （已验证，Winter 2026 版）
- **用法**：Day 1 英语轨道材料。CS224N 2025/2026 版新增 Lecture 17-18（RAG、fine-tuning、prompt optimization、safety）。Lecture 1（Word Vectors）是 Day 1 的核心阅读，建立"表示即向量"的直觉。

### CMU 10741: Representation Learning
- 🌐 课程主页：https://www.cs.cmu.edu/~pradeepr/741/ （已验证，Fall 2024 版，Prof. Pradeep Ravikumar）
- **用法**：Day 1 理论基础的标杆课程。三个核心概念（不加约束的表示学习没有意义、Neural Collapse、不可辨识性）直接对标 CMU 10741 Lecture 1-3。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本 Day `notes.md` 理论回顾 + 独立教材 §3.1.1-3.1.6 | 表示学习理论基础 | 1h |
| 2 | Neural Collapse 论文 §1-2（选读） | 理解表示的几何结构 | 0.5h |
| 3 | `starter.ipynb` 上机（配 sentence-transformers 文档） | 真实库实操 | 2h |
| 4 | Representation Engineering 论文 §2-3 | 2026 前沿 | 0.5h |
| 5 | CS224N Lecture 1（Word Vectors） | 英语轨道 | 1h |
| 6 | Peffers 2007 DSR 六步流程 | 研究方法论 | 0.5h |

---

*全部深链已于 2026-07-24 验证存在。如发现失效，请在 Issues 报告。*
