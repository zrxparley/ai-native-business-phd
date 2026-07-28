# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：技能1 表示工程 · Day 4 多模态融合与跨域对齐
> **scratch 哲学**：不调 transformers CLIPModel，手写 InfoNCE 对称对比损失 + 余弦相似度矩阵，从对比学习目标函数直译到 numpy。

## scratch_topic

本单元 from-scratch 主题：**手写 CLIP 对称对比损失（InfoNCE）+ 跨模态对齐**。对应 rohitg00 P12/02 CLIP Contrastive Pretraining + P12/03 BLIP2 QFormer Bridge。notes.md/starter.ipynb 用 `transformers.CLIPModel/CLIPProcessor` 加载 OpenAI 预训练 CLIP 做图文检索，用 torch 实现 InfoNCE + 融合策略--本层去库化：纯 numpy 手写 CLIP 的对称对比损失（图像-文本双塔对齐），用余弦相似度矩阵 + softmax 构造 InfoNCE，让"为什么对角线是正样本""为什么损失要对称（i2t + t2i）/2""温度参数 $\tau$ 如何控制分布尖锐度"三个问题在白板级代码中显形。

## core_algorithm

**InfoNCE 损失**（Noise Contrastive Estimation）是对比学习的核心目标函数。给定 $N$ 个图文对 $\{(I_i, T_i)\}_{i=1}^{N}$，图像编码器 $f_\theta$ 和文本编码器 $g_\phi$ 分别输出归一化向量 $\mathbf{z}_i^I = f_\theta(I_i)/\|f_\theta(I_i)\|$ 和 $\mathbf{z}_i^T = g_\phi(T_i)/\|g_\phi(T_i)\|$。相似度矩阵 $S \in \mathbb{R}^{N \times N}$，$S_{ij} = \mathbf{z}_i^I \cdot \mathbf{z}_j^T$（余弦相似度，已归一化故无需除以范数）。

**图像到文本方向**（每行 softmax，正样本在对角线 $S_{ii}$）：

$$\mathcal{L}_{\text{i2t}} = -\frac{1}{N}\sum_{i=1}^{N} \log\frac{\exp(S_{ii}/\tau)}{\sum_{j=1}^{N}\exp(S_{ij}/\tau)}$$

**文本到图像方向**（每列 softmax，正样本在对角线 $S_{ii}$）：

$$\mathcal{L}_{\text{t2i}} = -\frac{1}{N}\sum_{i=1}^{N} \log\frac{\exp(S_{ii}/\tau)}{\sum_{j=1}^{N}\exp(S_{ji}/\tau)}$$

**CLIP 对称损失**为两者均值：

$$\mathcal{L}_{\text{CLIP}} = \frac{1}{2}\left(\mathcal{L}_{\text{i2t}} + \mathcal{L}_{\text{t2i}}\right)$$

**温度参数 $\tau$ 的作用**：$\tau$ 控制 softmax 分布的尖锐度。$\tau$ 越小，$\exp(S/\tau)$ 越尖锐，模型对正确匹配的"信心"越强（正样本概率趋近 1，损失趋近 0）；$\tau$ 越大，分布越平坦，模型"犹豫"（正样本概率趋近 $1/N$，损失趋近 $\log N$）。CLIP 原始实现 $\tau = 0.07$（可学习，初始化值）。关键洞察：当 $S_{ii} = 1$（完美对齐）且 $S_{ij} \approx 0$（$i \neq j$，随机对不相关）时，$\tau \to 0$ 使损失 $\to 0$；但若 $S_{ii}$ 不显著大于 $S_{ij}$（编码器未学好），小 $\tau$ 反而放大错误匹配的惩罚。理解 $\tau$ 的双刃剑效应，才能诊断"CLIP 训练早期 loss 不收敛"的数值原因。

## code_artifact

```python
import numpy as np

def softmax(x, axis=-1):
    m = np.max(x, axis=axis, keepdims=True)
    e = np.exp(x - m)
    return e / np.sum(e, axis=axis, keepdims=True)

def cosine_sim(Z_img, Z_txt):
    # Normalize rows to unit length, then dot product -> (N, N) sim matrix
    img = Z_img / (np.linalg.norm(Z_img, axis=1, keepdims=True) + 1e-9)
    txt = Z_txt / (np.linalg.norm(Z_txt, axis=1, keepdims=True) + 1e-9)
    return img @ txt.T

def clip_contrastive_loss(Z_img, Z_txt, tau=0.07):
    # Symmetric InfoNCE: L = (L_i2t + L_t2i) / 2
    S = cosine_sim(Z_img, Z_txt) / tau  # (N, N) logits
    N = S.shape[0]; labels = np.arange(N)
    loss_i2t = -np.log(softmax(S, axis=1)[labels, labels] + 1e-9)
    loss_t2i = -np.log(softmax(S, axis=0)[labels, labels] + 1e-9)
    return (loss_i2t.mean() + loss_t2i.mean()) / 2

# verification_property:
#   aligned pairs (img=txt) -> low loss; random pairs -> higher loss;
#   smaller tau sharpens aligned loss downward
if __name__ == "__main__":
    rng = np.random.default_rng(0)
    N, D = 4, 8
    Z = rng.standard_normal((N, D))
    Z_img = rng.standard_normal((N, D)); Z_txt = rng.standard_normal((N, D))
    loss_aligned = clip_contrastive_loss(Z, Z, tau=0.07)
    loss_random = clip_contrastive_loss(Z_img, Z_txt, tau=0.07)
    assert loss_aligned < loss_random, "aligned pairs must have lower contrastive loss"
    assert loss_aligned < clip_contrastive_loss(Z, Z, tau=1.0), "smaller tau sharpens aligned loss"
```

**verification_property**: 完美对齐对（$\mathbf{z}_i^I = \mathbf{z}_i^T$，对角线 $S_{ii}=1$）的对比损失低于随机对（$S_{ij}$ 无对角线优势）；温度参数 $\tau=0.07$ 时对齐对的损失低于 $\tau=1.0$ 时（小 $\tau$ 使分布更尖锐，对角线概率更高，损失更低）。

## connection_to_unit

1. **预训练 CLIP vs 从零损失**：starter.ipynb TODO3 用 `CLIPModel.from_pretrained("openai/clip-vit-base-patch32")` 加载预训练 CLIP，图像和文本编码器已在 4 亿图文对上训练好，直接编码 + 计算相似度即可做图文检索；from-scratch 版的 `clip_contrastive_loss` 只实现损失函数（前向计算），不训练编码器--预训练 CLIP 的编码器输出已对齐，from-scratch 版假设 $\mathbf{z}^I$ 和 $\mathbf{z}^T$ 给定，聚焦"损失函数本身如何衡量对齐质量"。理解损失函数才能理解 CLIP 训练时在优化什么。
2. **温度参数 $\tau$ 的实验对比**：notes.md 关键回顾 2 和 starter.ipynb TODO2 都提到"$\tau$ 小->分布尖锐，$\tau$ 大->分布平坦，CLIP 原始 $\tau=0.07$"；from-scratch 版的 verification_property 直接构造实验：`clip_contrastive_loss(Z, Z, tau=0.07) < clip_contrastive_loss(Z, Z, tau=1.0)`，让"$\tau$ 越小对齐损失越低"这个数学关系在 assert 中验证。torch 版 TODO2 的 $\tau$ 实验需要训练模型观察 loss 曲线，from-scratch 版在给定编码器输出上直接计算--更快地暴露 $\tau$ 的数值效应。
3. **对称损失的方向性**：starter.ipynb TODO2 用 torch 实现 InfoNCE + CLIP 对称损失，`L = (L_img2text + L_text2img) / 2`；from-scratch 版的 `loss_i2t` 用 `softmax(S, axis=1)`（行方向，每个图像选正确文本），`loss_t2i` 用 `softmax(S, axis=0)`（列方向，每个文本选正确图像）。理解"对称"不是简单的两次计算，而是**两个方向的分类任务**：i2t 是"给定图像，从 N 个文本中选对的"，t2i 是"给定文本，从 N 个图像中选对的"--两个方向的负样本集合不同，故损失不同，取均值保证双向对齐。

## deep_dive_links

- [P12/02 CLIP Contrastive Pretraining - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/12-multimodal-ai/02-clip-contrastive-pretraining/README.md) - CLIP 对比预训练，本单元 from-scratch 的核心理论锚点，覆盖双塔架构/InfoNCE/温度参数
- [P12/03 BLIP2 QFormer Bridge - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/12-multimodal-ai/03-blip2-qformer-bridge/README.md) - BLIP-2 Q-Former 桥接，从对比对齐（CLIP）到生成式理解（BLIP-2）的范式跃迁

## exercises

1. 在本单元 `starter.ipynb` TODO2（torch 实现 InfoNCE + CLIP 对称损失 + 温度参数实验）运行后，用上面的 `clip_contrastive_loss` 在相同的随机向量上计算损失，对比 torch 版与 numpy 版的数值是否一致（固定 `rng = np.random.default_rng(0)` 与 torch 同种子）。提示：torch 的 `F.cross_entropy` 与 from-scratch 的 `softmax + -log` 在数学上等价，差异仅来自浮点精度。
2. 实现"$\tau$ 扫描实验"：令 $\tau = 0.01, 0.07, 0.1, 0.5, 1.0$，对每个 $\tau$ 计算对齐对和随机对的 `clip_contrastive_loss`，绘制 $\tau$ vs loss 曲线。观察"$\tau$ 越小对齐损失越低但随机损失越高"的双刃剑效应。对应 notes.md 关键回顾 2"$\tau$ 小->分布尖锐（模型'信心强'）"的量化验证。
3. 构造"负样本数量实验"：令 $N = 4, 8, 16, 32$（batch size = 负样本数 + 1），观察对齐对的 `clip_contrastive_loss` 随 $N$ 增大的变化。$N$ 越大，负样本越多，对齐任务越难（需要在更多候选中选对），损失越高。这与 CLIP 论文"batch size = 32768"的设计动机直接相关--大规模 batch 提供更多负样本是对比学习有效的关键。
4. TODO: 在 `practice.md` 的 D1 drill（融合策略）中，为本 from-scratch `clip_contrastive_loss` 添加"梯度计算"：对 $\mathbf{z}^I$ 和 $\mathbf{z}^T$ 求损失梯度 $\partial\mathcal{L}/\partial\mathbf{z}^I$（手写 softmax 反向传播），用 `Win += g*u` 风格的 SGD 更新验证"对比学习拉正样本推负样本"的几何效应。这是 starter.ipynb TODO2 torch 版（自动微分）的 from-scratch 对照版，帮助你理解 InfoNCE 的梯度如何实现对齐。
