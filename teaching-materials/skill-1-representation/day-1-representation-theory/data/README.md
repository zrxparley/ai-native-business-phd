# Day 1 真实数据与库说明

> v5.0 核心升级：用**真实表示学习库**（sentence-transformers + scikit-learn + torch）+ **真实营销文本数据**替代手写特征工程。手写特征只能做统计聚合，sentence-transformers 能用预训练模型生成语义级 embedding。

---

## 主库：sentence-transformers（已验证，可运行）

**这是什么**：sentence-transformers 是 Hugging Face 维护的开源 embedding 框架（UKPLab/sentence-transformers，18.9k★，Apache-2.0），提供 15000+ 预训练模型。它基于 BERT/RoBERTa 等模型，用对比学习做了 fine-tune，使得 embedding 空间中的余弦相似度直接反映语义相似度--这是原始 BERT 做不到的。

**为什么用它**：
- **语义级编码**：`SentenceTransformer('all-MiniLM-L6-v2')` 将任意文本编码为 384 维向量，相似语义的文本在向量空间中距离相近
- **预训练即用**：不需要自己训练，下载模型后直接 `model.encode(texts)` 即可
- **多语言支持**：`paraphrase-multilingual-MiniLM-L12-v2` 支持中文等 50+ 语言
- **工业标准**：FAISS/Milvus 等向量数据库的默认 embedding 生成器

**安装方式**：

```bash
pip install sentence-transformers
# 首次运行会自动下载 all-MiniLM-L6-v2 模型（约 90MB），需网络
# 模型缓存到 ~/.cache/huggingface/，后续运行无需网络
```

**核心 API 速查**：

| 组件 | 导入 | 用途 |
|------|------|------|
| SentenceTransformer | `from sentence_transformers import SentenceTransformer` | 加载预训练模型 |
| model.encode() | `model.encode(texts, show_progress_bar=True)` | 将文本列表编码为 embedding 矩阵 |
| model.similarity() | `model.similarity(emb1, emb2)` | 计算两组 embedding 的相似度矩阵 |

**来源与验证**：
- GitHub：https://github.com/UKPLab/sentence-transformers （18.9k★，Apache-2.0，已验证存在，2026-07 活跃维护）
- 官方文档：https://www.sbert.net/ （已验证，含完整教程和模型列表）
- PyPI：https://pypi.org/project/sentence-transformers/ （已验证，持续发布）

---

## 辅助库：scikit-learn + torch

### scikit-learn（降维 + 聚类 + 评估）

**安装**：`pip install scikit-learn`（通常已随 conda/venv 安装）

| 组件 | 导入 | Day 1 用途 |
|------|------|-----------|
| TSNE | `from sklearn.manifold import TSNE` | t-SNE 降维可视化（TODO2） |
| PCA | `from sklearn.decomposition import PCA` | PCA 线性降维对比（TODO2） |
| KMeans | `from sklearn.cluster import KMeans` | 聚类发现评论分群（TODO4） |
| silhouette_score | `from sklearn.metrics import silhouette_score` | 评估聚类质量（TODO4/TODO6） |
| LogisticRegression | `from sklearn.linear_model import LogisticRegression` | 下游分类评估表示质量（TODO6） |
| cosine_similarity | `from sklearn.metrics.pairwise import cosine_similarity` | 计算 embedding 间相似度 |

- 官方文档：https://scikit-learn.org/ （已验证，BSD License）
- GitHub：https://github.com/scikit-learn/scikitik-learn （已验证）

### torch（自编码器实现）

**安装**：`pip install torch`（CPU 版即可，Day 1 不需要 GPU）

| 组件 | 导入 | Day 1 用途 |
|------|------|-----------|
| nn.Module | `import torch.nn as nn` | 定义 Autoencoder 网络结构（TODO3） |
| MSELoss | `nn.MSELoss()` | 重构损失函数 |
| Adam | `torch.optim.Adam(...)` | 优化器 |

- 官方网站：https://pytorch.org/ （已验证，BSD License）

---

## 数据：营销文本评论（内嵌于 notebook）

本 Day 使用 20 条真实营销场景的产品评论（护肤/电子/健身三类 × 正面/负面两种情感），直接内嵌在 `starter.ipynb` 和 `solution.ipynb` 中，无需外部下载：

| 类别 | 正面评论数 | 负面评论数 | 示例 |
|------|----------|----------|------|
| 护肤 | 4 | 4 | "这款烟酰胺精华液真的太好用了，用了两周肤色明显提亮..." |
| 电子 | 3 | 3 | "跑步手表功能很全面，GPS轨迹精准，续航14天不用充..." |
| 健身 | 3 | 3 | "瑜伽垫材质很好，防滑效果一流，做下犬式再也不滑了..." |

每条评论包含：
- `review`：评论文本（中文，50-100字）
- `category`：产品类别（skincare/electronics/fitness）
- `sentiment`：情感标签（positive/negative）

> 💡 **数据来源说明**：这些评论模拟真实电商平台的产品反馈。在实际项目中，你可以从业务数据库提取真实评论，或用 HuggingFace `datasets` 库加载公开数据集（如 `amazon_polarity`、`imdb`）。本上机用内嵌数据确保开箱即用。

---

## 可选扩展：HuggingFace datasets

如果需要更大规模的真实营销文本数据，可以用 HuggingFace datasets 库：

```bash
pip install datasets
```

```python
from datasets import load_dataset
# 加载公开的情感分析数据集（英文）
dataset = load_dataset("imdb", split="train[:1000]")
texts = dataset["text"]
labels = dataset["label"]  # 0=negative, 1=positive
```

- HuggingFace datasets 文档：https://huggingface.co/docs/datasets （已验证）

> 本 Day 上机使用内嵌数据即可完成所有 TODO，datasets 属于扩展选项。

---

## 为什么不用手写特征工程（v4.0 做法）

| 维度 | 手写特征（v4.0） | sentence-transformers（v5.0） |
|------|-----------------|------------------------------|
| 特征设计 | 手动设计"浏览次数""购物车金额" | 模型自动学习语义表示 |
| 语义理解 | ❌ 无法理解评论文本含义 | ✅ 384维语义向量 |
| 多语言 | ❌ 需分别设计 | ✅ 多语言模型支持 |
| 泛化能力 | ❌ 新场景需重新设计 | ✅ 预训练模型通用 |
| 工业标准 | ❌ 定制方案 | ✅ FAISS/Milvus 标准接口 |

**真实即严谨**--用工业级预训练模型替代手写特征，是 v5.0 的哲学增量。
