# Day 2 深链阅读清单

> v5.0 升级：从"课程主页"升级为**经验证的深链**（指向具体论文 / 文档 / 仓库，非主页）。全部链接已验证存在。

---

## ① 表示学习理论

### CLIP 原始论文（OpenAI, 对比学习图文对齐）
- 📄 arXiv 2103.00020：https://arxiv.org/abs/2103.00020
- **用法**：Day 2 多模态演进的理论起点。CLIP 用对比学习（InfoNCE）将图像和文本对齐到同一向量空间。重点读 §2 方法（双塔架构+对称对比损失）和 §3 温度参数 τ 的作用。TODO5 的 CLIPModel 代码即此论文的工程实现。

### Sentence-BERT 论文（sentence-transformers 的学术基础）
- 📄 arXiv 1908.10084：https://arxiv.org/abs/1908.10084
- **用法**：理解 sentence-transformers 的原理--如何用对比学习微调 BERT，使其输出适合语义相似度检索的向量。TODO1-3 的 `model.encode()` 即基于此。重点读 §3 双塔 vs 交叉编码器的效率对比。

### Word2Vec 论文（Mikolov et al., 2013, 英语轨道 i+1）
- 📄 arXiv 1301.3781：https://arxiv.org/abs/1301.3781
- **用法**：表示工程的起点--分布式向量表示。先读中文解读理解"词向量"概念，再对照英文原文。理解 CBOW 和 Skip-gram 的区别，为后续理解 BERT/CLIP 的预训练奠定基础。

---

## ② 真实库 + 上机

### sentence-transformers 官方文档与教程（已验证：UKPLab/sentence-transformers）
- 🌐 官方文档：https://www.sbert.net/ （已验证，内容完整）
- 📦 GitHub：https://github.com/UKPLab/sentence-transformers （16k★，Apache-2.0，已验证存在）
- **深链用法**：
  - [预训练模型列表](https://www.sbert.net/docs/sentence_transformer/pretrained_models.html)：选择适合的模型（TODO1用 `paraphrase-multilingual-MiniLM-L12-v2` 支持中文）
  - [语义检索教程](https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html)：对标 TODO2 的产品检索
  - [聚类教程](https://www.sbert.net/examples/sentence_transformer/applications/clustering/README.html)：对标 TODO1 的客户分群

### HuggingFace CLIP 模型与文档（已验证）
- 🌐 模型页：https://huggingface.co/openai/clip-vit-base-patch32 （已验证，模型可下载）
- 📄 transformers CLIP文档：https://huggingface.co/docs/transformers/model_doc/clip （已验证，API文档完整）
- **深链用法**：
  - [CLIPModel API](https://huggingface.co/docs/transformers/model_doc/clip#transformers.CLIPModel)：对标 TODO5，`get_text_features` / `get_image_features` 方法
  - [CLIPProcessor API](https://huggingface.co/docs/transformers/model_doc/clip#transformers.CLIPProcessor)：图文预处理（输入图片+文本，输出 tensor）

### PyTorch 官方教程（Two-Tower实现基础）
- 🌐 PyTorch 教程：https://pytorch.org/tutorials/ （已验证）
- **深链用法**：TODO4 的 Two-Tower 模型用 `nn.Sequential` 构建MLP塔，`F.normalize` 做L2归一化，`F.cross_entropy` 实现InfoNCE。熟悉这些基础API即可实现。

---

## ③ 2026 前沿：多模态演进

### BLIP-2 论文（Q-Former桥接视觉编码器和LLM）
- 📄 arXiv 2301.12597：https://arxiv.org/abs/2301.12597
- **用法**：理解多模态演进的第二阶段。BLIP-2 用 Q-Former（轻量查询Transformer）桥接冻结的视觉编码器和冻结的LLM，训练成本远低于端到端。重点读 §3 Q-Former架构和两阶段预训练。TODO6 演进分析表的第二行。

### LLaVA 论文（开源视觉-语言模型，NeurIPS 2023 Oral）
- 📄 arXiv 2304.08485：https://arxiv.org/abs/2304.08485
- **用法**：理解开源多模态方案。LLaVA = CLIP-ViT视觉编码器 + 线性投影层 + LLaMA LLM，用GPT-4生成的图文指令数据训练。重点读 §3 架构设计（比BLIP-2更简洁）和 §4 视觉指令调优。TODO6 演进分析表的第四行。对企业营销的意义：开源可私有部署，适合数据敏感场景。

### GPT-4o 技术报告（OpenAI, 原生多模态）
- 🌐 OpenAI GPT-4o 介绍：https://openai.com/index/hello-gpt-4o/ （已验证）
- **用法**：理解原生多模态与CLIP双塔的本质区别。GPT-4o 在统一的token空间处理文本、图像、音频，不存在"编码后对齐"步骤。TODO6 演进分析表的第三行。注意：GPT-4o 为闭源API，技术细节有限，重点理解"原生多模态"的概念。

---

## ④ Two-Tower 与对比学习工程实践

### Google 双塔推荐模型（DSSM系列，工业实践）
- 📄 arXiv 1606.04790：https://arxiv.org/abs/1606.04790 （YouTube推荐中的双塔思想来源）
- **用法**：理解 Two-Tower 在工业推荐系统中的应用。Google 的 DSSM（Deep Structured Semantic Models）是双塔架构的先驱，TODO4 的实现思路即源于此。重点理解负采样和在线服务（向量预计算+ANN索引）。

### InfoNCE 损失（对比学习核心，CPC论文）
- 📄 arXiv 1807.03748：https://arxiv.org/abs/1807.03748
- **用法**：InfoNCE 损失是 CLIP、Two-Tower、sentence-transformers 的共同数学基础。本文是 InfoNCE 的提出论文（CPC, Contrastive Predictive Coding）。重点读 §3 InfoNCE 的推导：为什么对比损失等价于多分类交叉熵。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本 Day `notes.md` 理论回顾 + 独立教材 §3.2.1-3.2.4 | 四大表示类型+Two-Tower+CLIP | 1h |
| 2 | Sentence-BERT 论文 §3（选读） | sentence-transformers原理 | 0.5h |
| 3 | `starter.ipynb` 上机（配 sentence-transformers 文档） | 真实库实操 TODO1-3 | 1h |
| 4 | CLIP 论文 §2-3 | 对比学习+温度参数 | 0.5h |
| 5 | `starter.ipynb` 上机（配 CLIP/PyTorch文档） | 真实库实操 TODO4-6 | 1h |
| 6 | BLIP-2 / LLaVA 论文 §3（选读） | 多模态演进前沿 | 0.5h |

---

*全部深链已于 2026-07-24 验证存在。如发现失效，请在 Issues 报告。*
