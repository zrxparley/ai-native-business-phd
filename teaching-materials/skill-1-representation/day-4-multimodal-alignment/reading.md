# Day 4 深链阅读清单

> v5.0 升级：从"课程主页"升级为**经验证的深链**（指向具体论文 / 文档 / 仓库，非主页）。全部链接已验证存在。

---

## ① 多模态对齐理论

### CLIP 原始论文（OpenAI, 2021，对比学习对齐图文）
- 📄 arXiv 2103.00020：https://arxiv.org/abs/2103.00020
- **用法**：Day 4 对比学习理论回顾的核心来源。CLIP 用4亿图文对训练，双塔架构+对比损失对齐图文。重点读 §2 方法（对比学习训练过程）和 §3 实验（零样本分类结果）。理解 InfoNCE 损失和温度参数 τ 的设计。

### SimCLR 原始论文（Google, 2020，对比学习视觉表示）
- 📄 arXiv 2002.05709：https://arxiv.org/abs/2002.05709
- **用法**：对比学习的视觉基础工作。SimCLR 提出了视觉对比学习的框架（正样本=同一图片的不同增强），CLIP 将其扩展到跨模态。重点读 §3 框架和温度参数分析。

### BLIP-2 原始论文（Salesforce, 2023，Q-Former桥接ViT和LLM）
- 📄 arXiv 2301.12597：https://arxiv.org/abs/2301.12597
- **用法**：Day 4 BLIP 图文理解的理论来源。BLIP-2 用 Q-Former 桥接冻结视觉编码器和冻结LLM，实现图文理解。重点读 §3 Q-Former 架构和 §4 两阶段预训练。

---

## ② 真实库 + 上机

### HuggingFace Transformers CLIP 文档（已验证）
- 🌐 官方文档：https://huggingface.co/docs/transformers/model_doc/clip （已验证，内容完整）
- **深链用法**：
  - [CLIPModel API](https://huggingface.co/docs/transformers/model_doc/clip#transformers.CLIPModel)：对标 TODO3，get_image_features/get_text_features 方法
  - [CLIPProcessor](https://huggingface.co/docs/transformers/model_doc/clip#transformers.CLIPProcessor)：对标 TODO3，图文统一预处理
  - [零样本图片分类示例](https://huggingface.co/docs/transformers/model_doc/clip#transformers.CLIPModel.forward)：对标 TODO5，zero-shot-image-classification pipeline
- 📦 GitHub：https://github.com/huggingface/transformers （140k★，Apache 2.0，已验证）

### HuggingFace Transformers BLIP-2 文档（已验证）
- 🌐 官方文档：https://huggingface.co/docs/transformers/model_doc/blip-2 （已验证）
- **深链用法**：
  - [Blip2ForConditionalGeneration](https://huggingface.co/docs/transformers/model_doc/blip-2#transformers.Blip2ForConditionalGeneration)：对标 TODO4，图片描述生成
  - [Blip2Processor](https://huggingface.co/docs/transformers/model_doc/blip-2#transformers.Blip2Processor)：图文预处理
  - [BLIP-2 教程笔记本](https://github.com/NielsRogge/Transformers-Tutorials/tree/master/BLIP-2)：官方推荐的 BLIP-2 实操教程（captioning + VQA + chat）

### CLIP 模型页（OpenAI 预训练权重）
- 🌐 模型页：https://huggingface.co/openai/clip-vit-base-patch32 （已验证，可直接下载）
- **用法**：TODO3 和 TODO5 使用的模型权重。base-patch32 是最轻量的 CLIP 模型（~600MB），适合教学。

### BLIP 模型页（Salesforce 预训练权重）
- 🌐 描述生成模型：https://huggingface.co/Salesforce/blip-image-captioning-base （已验证，~250MB）
- 🌐 VQA 模型：https://huggingface.co/Salesforce/blip-vqa-base （已验证，~250MB）
- **用法**：TODO4 使用的模型权重。BLIP-base 是 BLIP-2 的轻量替代。

---

## ③ 2026 前沿：原生多模态与开源多模态

### LLaVA（开源视觉-语言模型，2024）
- 🌐 项目主页：https://llava-vl.github.io/ （已验证）
- 📦 GitHub：https://github.com/haotian-liu/LLaVA （已验证，开源多模态模型）
- **用法**：LLaVA = CLIP-ViT + 投影层 + LLM，是企业级低成本多模态方案的代表。理解其架构有助于设计企业多模态系统（TODO6）。重点看其如何用投影层对齐视觉和语言特征。

### GPT-4o 多模态能力（OpenAI, 2024）
- 🌐 OpenAI 官方介绍：https://openai.com/index/hello-gpt-4o/ （已验证）
- **用法**：理解"原生多模态"的含义--端到端训练，统一 token 空间处理文本/图像/音频。与 CLIP 的"双塔"架构对比，理解为什么原生多模态能理解跨模态细微关联。

### BLIP-3 / Salesforce 多模态演进
- 🌐 Salesforce BLIP 系列：https://huggingface.co/Salesforce （已验证，包含 blip2/blip3 模型）
- **用法**：跟踪 BLIP 系列的最新演进。BLIP-3（2024-2025）在 Q-Former 基础上进一步优化，是开源多模态的重要力量。

---

## ④ 企业级多模态架构实践

### FAISS 向量检索（Meta，已验证）
- 📦 GitHub：https://github.com/facebookresearch/faiss （已验证，30k★）
- **用法**：TODO6 架构设计的存储与检索层。FAISS 是工业标准向量检索库，支持 CLIP embedding 的大规模近邻搜索。

### Sentence-Transformers（文本 embedding，已验证）
- 🌐 官方文档：https://www.sbert.net/ （已验证）
- 📦 GitHub：https://github.com/UKPLab/sentence-transformers （已验证）
- **用法**：TODO6 架构设计的文本编码器。推荐 all-MiniLM-L6-v2（384维，轻量快速）。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本 Day `notes.md` 理论回顾 + 独立教材 §3.4.1-3.4.3 | 融合策略/对比学习/架构 | 1h |
| 2 | CLIP 论文 §2-3（选读） | 对比学习原理 | 0.5h |
| 3 | `starter.ipynb` 上机（配 transformers CLIP 文档） | 真实库实操 | 2h |
| 4 | BLIP-2 论文 §3（选读） | Q-Former 架构 | 0.5h |
| 5 | LLaVA 项目主页 + GitHub | 开源多模态方案 | 0.5h |
| 6 | transformers CLIP/BLIP 文档（API巩固） | 工程实现 | 0.5h |

---

*全部深链已于 2026-07-24 验证存在。如发现失效，请在 Issues 报告。*
