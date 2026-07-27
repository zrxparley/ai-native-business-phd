# Day 4 真实数据与库说明

> v5.0 核心升级：用**真实多模态库**（transformers CLIP/BLIP）+ **PIL 生成模拟产品图片**替代手写 numpy 模拟。手写模拟无法处理真实图片，transformers 能加载预训练模型直接编码。

---

## 主库：transformers（HuggingFace，已验证，可运行）

**这是什么**：transformers 是 HuggingFace 维护的开源深度学习库（140k★），提供 CLIP、BLIP、BLIP-2、LLaVA 等多模态模型的预训练权重和统一 API。它是多模态表示学习的**工程标准实现**。

**为什么用它**：
- **CLIPModel/CLIPProcessor**：加载 OpenAI 预训练 CLIP，直接编码真实图片和文本，计算图文相似度
- **BlipProcessor/BlipForConditionalGeneration**：加载 Salesforce BLIP，自动生成图片描述
- **BlipForQuestionAnswering**：VQA 视觉问答，对产品图片提问
- **get_image_features/get_text_features**：获取归一化 embedding，用于检索和对齐

**安装方式**：

```bash
pip install transformers torch pillow numpy
# CLIP/BLIP模型首次运行需从HuggingFace下载：
#   openai/clip-vit-base-patch32 (~600MB)
#   Salesforce/blip-image-captioning-base (~250MB)
#   Salesforce/blip-vqa-base (~250MB)
# 如网络受限，可设置镜像：
# export HF_ENDPOINT=https://hf-mirror.com
```

**核心 API 速查**：

| 组件 | 导入 | 用途 |
|------|------|------|
| CLIPModel | `from transformers import CLIPModel` | CLIP 模型（图文编码+对齐） |
| CLIPProcessor | `from transformers import CLIPProcessor` | CLIP 输入预处理（图文统一） |
| get_image_features | `model.get_image_features(**inputs)` | 获取图像 embedding |
| get_text_features | `model.get_text_features(**inputs)` | 获取文本 embedding |
| BlipProcessor | `from transformers import BlipProcessor` | BLIP 输入预处理 |
| BlipForConditionalGeneration | `from transformers import BlipForConditionalGeneration` | BLIP 描述生成 |
| BlipForQuestionAnswering | `from transformers import BlipForQuestionAnswering` | BLIP VQA 问答 |

**来源与验证**：
- transformers GitHub：https://github.com/huggingface/transformers （140k★，Apache 2.0，已验证存在，2026-07 活跃维护）
- transformers 官方文档：https://huggingface.co/docs/transformers （已验证，内容完整）
- CLIP 模型页：https://huggingface.co/openai/clip-vit-base-patch32 （已验证，可下载）
- BLIP 模型页：https://huggingface.co/Salesforce/blip-image-captioning-base （已验证，可下载）

---

## 辅助库：torch（对比学习与融合策略实现）

**用途**：从零实现 InfoNCE 损失、CLIP 对称损失、多模态融合三策略（早/中/晚融合）。

| 组件 | 导入 | 用途 |
|------|------|------|
| nn.Module | `import torch.nn as nn` | 定义融合模型（EarlyFusion/CrossModalAttention/LateFusion） |
| F.normalize | `import torch.nn.functional as F` | embedding 归一化（L2） |
| F.cross_entropy | `F.cross_entropy(logits, labels)` | InfoNCE 损失核心 |
| nn.MultiheadAttention | `nn.MultiheadAttention(...)` | 中融合跨模态注意力 |

**安装**：`pip install torch`（通常已随 transformers 安装）

---

## 辅助库：sentence-transformers（文本侧 embedding）

**用途**：企业架构中文本编码器的推荐方案（独立教材 § 3.2.4 推荐）。

- 官方文档：https://www.sbert.net/ （已验证）
- GitHub：https://github.com/UKPLab/sentence-transformers （已验证）
- 推荐模型：`all-MiniLM-L6-v2`（384维，轻量快速）

**安装**：`pip install sentence-transformers`

---

## 数据说明：营销图文对

本 Day 不使用外部数据集，而是用 **PIL 生成模拟产品图片**（不同颜色+标签），确保代码无需下载图片即可运行：

| 图片 | 颜色 | 标签 | 营销文案 |
|------|------|------|---------|
| 产品1 | 红色 (180,30,30) | LIPSTICK | 红色哑光口红彩妆 |
| 产品2 | 绿色 (30,120,80) | SKINCARE | 绿色天然护肤面霜 |
| 产品3 | 蓝色 (30,50,150) | GADGET | 蓝色智能电子设备 |

> 💡 **实际项目中**：替换 `make_product_image()` 为 `Image.open("real_product.jpg")` 即可使用真实产品图片。CLIP/BLIP 的 API 完全不变。

**可选真实数据集**（进阶练习）：
- **Flickr30k**：https://huggingface.co/datasets/nlphuji/flickr30k （图文对数据集，3万张图+5个描述/图）
- **COCO Captions**：https://huggingface.co/datasets/yerevann/coco-karpathy （12万张图+5个描述/图）

---

## BLIP-2 vs BLIP（模型选择说明）

| 维度 | BLIP（本上机使用） | BLIP-2（生产推荐） |
|------|-------------------|-------------------|
| 模型大小 | ~250MB | 2.7B+（~5-15GB） |
| 类名 | BlipProcessor / BlipForConditionalGeneration | Blip2Processor / Blip2ForConditionalGeneration |
| 模型ID | Salesforce/blip-image-captioning-base | Salesforce/blip2-opt-2.7b |
| 功能 | 描述生成 + VQA | 描述生成 + VQA + 对话 |
| API | 几乎相同 | 几乎相同 |

> 本上机用 BLIP-base 确保代码可快速运行。BLIP-2 的 API 几乎相同，仅需替换类名和模型ID。

---

## 为什么不用手写 numpy（v4.0 做法）

| 维度 | 手写 numpy（v4.0） | transformers CLIP/BLIP（v5.0） |
|------|---------------------|-------------------------------|
| 图片处理 | ❌ 无法处理真实图片 | ✅ PIL图片直接输入 |
| 预训练能力 | ❌ 随机权重 | ✅ OpenAI/Salesforce预训练 |
| 图文对齐 | ❌ 手写cosine | ✅ CLIP对比学习对齐 |
| 图片描述 | ❌ 做不到 | ✅ BLIP自动生成 |
| VQA | ❌ 做不到 | ✅ BLIP VQA |
| 工程标准 | ❌ 教学演示 | ✅ 工业级API |

**真实即严谨**--用预训练模型替代手写模拟，是 v5.0 的哲学增量。
