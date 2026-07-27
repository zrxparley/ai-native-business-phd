# Day 2 真实数据与库说明

> v5.0 核心升级：用**真实预训练模型库**（sentence-transformers / transformers CLIP / torch）替代手写TF-IDF。手写TF-IDF无法理解语义（"跑步鞋"和"运动鞋"词不重叠则相似度为0），预训练模型能编码深层语义关系。

---

## 主库1：sentence-transformers（已验证，可运行）

**这是什么**：sentence-transformers 是 UKPLab 开源的句子/文本 embedding 框架（16k★），基于 BERT/RoBERTa 等预训练模型，将文本编码为固定维度的语义向量。它是表示工程中"文本表示"的工业标准，也是独立教材 §3.2.4 代码示例使用的库。

**为什么用它**：
- **语义理解**：TF-IDF 认为"跑步鞋"和"运动鞋"无关（词不重叠），sentence-transformers 能编码语义相似性
- **多语言支持**：`paraphrase-multilingual-MiniLM-L12-v2`（多语言含中文，384维）/ `BAAI/bge-small-zh`（中文优化，512维）
- **轻量高效**：`all-MiniLM-L6-v2` 仅约90MB，CPU即可推理
- **检索就绪**：编码后直接用 cosine 相似度检索，无需额外训练

**安装方式**：

```bash
pip install sentence-transformers scikit-learn
# 首次运行会自动下载预训练模型（约470MB for paraphrase-multilingual-MiniLM-L12-v2）
```

**核心 API 速查**：

| 组件 | 导入 | 用途 |
|------|------|------|
| SentenceTransformer | `from sentence_transformers import SentenceTransformer` | 加载预训练模型 |
| encode | `model.encode(texts, show_progress_bar=True)` | 文本->向量 |
| cosine_similarity | `from sklearn.metrics.pairwise import cosine_similarity` | 计算向量相似度 |
| KMeans | `from sklearn.cluster import KMeans` | 向量分群 |
| silhouette_score | `from sklearn.metrics import silhouette_score` | 评估分群质量 |

**来源与验证**：
- GitHub：https://github.com/UKPLab/sentence-transformers （16k★，Apache-2.0，已验证存在，2026-07 活跃维护）
- 官方文档：https://www.sbert.net/ （已验证，内容完整）
- PyPI：https://pypi.org/project/sentence-transformers/ （已验证，持续发布）

---

## 主库2：transformers CLIP（已验证，可运行）

**这是什么**：HuggingFace transformers 库提供 CLIP（Contrastive Language-Image Pre-training）的 Python 实现。CLIP 是 OpenAI 2021 年发布的图文对齐模型，用对比学习将图像和文本对齐到同一向量空间。它是多模态表示学习的里程碑。

**为什么用它**：
- **图文对齐**：给一张产品图片和几段描述，CLIP 能判断哪段描述最匹配--这是多模态搜索的基础
- **零样本分类**：无需训练即可做图像分类（给候选标签，CLIP 选最匹配的）
- **真实API**：`CLIPModel.get_text_features()` / `CLIPModel.get_image_features()` 是工业级接口

**安装方式**：

```bash
pip install transformers torch pillow
# 首次运行会自动下载 CLIP 模型（约600MB for openai/clip-vit-base-patch32）
```

**核心 API 速查**：

| 组件 | 导入 | 用途 |
|------|------|------|
| CLIPModel | `from transformers import CLIPModel` | 加载 CLIP 模型 |
| CLIPProcessor | `from transformers import CLIPProcessor` | 预处理图文输入 |
| get_text_features | `model.get_text_features(input_ids=..., attention_mask=...)` | 文本->向量 |
| get_image_features | `model.get_image_features(pixel_values=...)` | 图像->向量 |
| logits_per_image | `outputs.logits_per_image` | 图文相似度矩阵（含温度缩放） |

**来源与验证**：
- HuggingFace 模型页：https://huggingface.co/openai/clip-vit-base-patch32 （已验证，模型可下载）
- transformers CLIP文档：https://huggingface.co/docs/transformers/model_doc/clip （已验证，API文档完整）
- CLIP 原始论文：https://arxiv.org/abs/2103.00020 （已验证，Radford et al., 2021）

---

## 主库3：torch（Two-Tower实现）

**这是什么**：PyTorch 是 Meta 开源的深度学习框架，用于实现 Two-Tower 双塔模型和 InfoNCE 对比损失。Two-Tower 是 Google、Amazon 等公司推荐系统的核心架构。

**安装方式**：

```bash
pip install torch
# CPU版本即可运行本Day的Two-Tower示例
```

**核心 API 速查**：

| 组件 | 导入 | 用途 |
|------|------|------|
| nn.Module | `import torch.nn as nn` | 模型基类 |
| nn.Sequential | `nn.Sequential(nn.Linear(...), nn.ReLU(), nn.Linear(...))` | 构建MLP塔 |
| F.normalize | `torch.nn.functional as F; F.normalize(x, p=2, dim=1)` | L2归一化 |
| F.cross_entropy | `F.cross_entropy(logits, labels)` | InfoNCE损失核心 |

---

## 数据集：美妆电商营销数据（内嵌）

本 Day 使用内嵌的美妆电商营销数据（无需下载外部数据集），保持课程连贯性。数据模式基于独立教材 §3.2.4 的客户行为文本扩展：

| 数据类型 | 内容 | 数量 | 用途 |
|---------|------|:----:|------|
| 客户行为文本 | 浏览/搜索/购买行为描述 | 8条 | TODO1: 客户embedding+分群 |
| 产品描述 | 美妆产品标题+功效+成分+价格 | 8个 | TODO2: 产品embedding+检索 |
| 营销文案 | 小红书种草风格文案 | 6条 | TODO3: 内容embedding+推荐 |
| 客户-产品交互 | 正样本购买对（客户i购买产品i） | 8对 | TODO4: Two-Tower训练 |
| 产品图片 | PIL生成的合成色块图片 | 3张 | TODO5: CLIP图文对齐 |

> 💡 **数据说明**：行为文本和产品描述模拟真实美妆电商场景。在实际项目中，这些数据来自数据仓库（客户行为日志/产品PIM系统/内容管理系统）。如需真实大规模图文对数据集，推荐 HuggingFace `flickr30k`（3万+图文对，https://huggingface.co/datasets/nlphuji/flickr30k ）用于CLIP训练实验。

---

## 为什么不用手写TF-IDF（v4.0 做法）

| 维度 | 手写TF-IDF（v4.0） | sentence-transformers（v5.0） |
|------|---------------------|------------------------------|
| 语义理解 | ❌ 词不重叠=无关 | ✅ "提亮精华"≈"烟酰胺" |
| 多语言 | ❌ 需分语言处理 | ✅ 多语言模型统一编码 |
| 向量质量 | 词频统计，无上下文 | 上下文感知，深层语义 |
| 检索效果 | 关键词匹配 | 语义检索 |
| 工业可用 | ❌ 需大量调优 | ✅ 预训练即可用 |

**真实即严谨**--用预训练模型替代手写特征工程，是 v5.0 的哲学增量。
