# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：选修E3 LLM导论 · Day 1 Transformer架构与训练流程（⭐旗舰单元）
> **scratch 哲学**：不调 torch.nn.MultiheadAttention，手写 scaled dot-product attention + multi-head，从 softmax(QK^T/√d_k)V 直译到 numpy。

## scratch_topic

本单元 from-scratch 主题：**手写 scaled dot-product attention + multi-head attention**（旗舰）。对应 rohitg00 P7/02 Self Attention from Scratch + P7/05 Full Transformer + P10/04 Pre-training Mini GPT。notes.md/starter.ipynb 用 torch 张量手写 Self-Attention（W_q/W_k/W_v + softmax），本层进一步去 torch 化：纯 numpy 实现 attention + multi-head + causal mask，让"为什么除以 √d_k""为什么多头""因果掩码如何防泄漏"三个问题在白板级代码中显形。

## core_algorithm

Scaled Dot-Product Attention 是 Transformer 的灵魂。给定查询 $Q$、键 $K$、值 $V$（均 $\in \mathbb{R}^{T\times d_k}$）：

$$\text{Attention}(Q,K,V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

**为什么除以 $\sqrt{d_k}$**：当 $d_k$ 较大时，$QK^T$ 的元素是 $d_k$ 个独立项之和，方差正比于 $d_k$。若不缩放，大方差把 softmax 推向饱和区（最大值梯度趋于 0），训练停滞。除以 $\sqrt{d_k}$ 把方差拉回 1，保持梯度健康。这是 from-scratch 必须理解数值细节，否则无法诊断"训练 loss 早期 NaN"。

**Multi-Head** 把 $Q,K,V$ 投影到 $h$ 个子空间各自做 attention 再拼接：

$$\text{MultiHead}(Q,K,V) = \text{Concat}(\text{head}_1,\dots,\text{head}_h)W^O,\quad \text{head}_i = \text{Attention}(QW_i^Q, KW_i^K, VW_i^V)$$

每个头用 $d_k/h$ 维，缩放因子为 $\sqrt{d_k/h}$。多头让模型同时关注不同关系子空间（语法/语义/共现），GPT-2 small 用 12 头。

**因果掩码**（causal mask）用于自回归生成：位置 $i$ 只能看位置 $\le i$。实现上把上三角（$j>i$）的 attention score 设为 $-\infty$，softmax 后归零，防止"看到未来 token"。

attention 的计算复杂度 $O(T^2 d_k)$--这是长上下文成本随序列长度平方增长的数学根源，直接决定营销知识图谱多跳检索的可行性上限。

## code_artifact

```python
import numpy as np

def softmax(x, axis=-1):
    m = np.max(x, axis=axis, keepdims=True)
    e = np.exp(x - m)
    return e / np.sum(e, axis=axis, keepdims=True)

def attention(Q, K, V, causal=False):
    # Q,K,V: (T, dk)
    dk = Q.shape[-1]
    scores = Q @ K.T / np.sqrt(dk)
    if causal:
        mask = np.triu(np.full(scores.shape, -1e9), k=1)
        scores = scores + mask
    weights = softmax(scores, axis=-1)
    return weights @ V, weights

def multi_head_attention(x, Wq, Wk, Wv, Wo, n_heads, causal=False):
    # x: (T, d), W*: (d, d)
    T, d = x.shape
    dh = d // n_heads
    Q = (x @ Wq).reshape(T, n_heads, dh).transpose(1, 0, 2)
    K = (x @ Wk).reshape(T, n_heads, dh).transpose(1, 0, 2)
    V = (x @ Wv).reshape(T, n_heads, dh).transpose(1, 0, 2)
    scores = Q @ K.transpose(0, 2, 1) / np.sqrt(dh)
    if causal:
        mask = np.triu(np.full((T, T), -1e9), k=1)
        scores = scores + mask
    weights = softmax(scores, axis=-1)
    heads = weights @ V
    concat = heads.transpose(1, 0, 2).reshape(T, d)
    return concat @ Wo, weights

# verification_property:
#   attention weights rows sum to 1; causal mask makes upper-triangle weights ~0;
#   multi_head output shape == input shape
if __name__ == "__main__":
    rng = np.random.default_rng(0)
    T, d, h = 6, 16, 4
    x = rng.standard_normal((T, d))
    Wq = rng.standard_normal((d, d)) * 0.1
    Wk = rng.standard_normal((d, d)) * 0.1
    Wv = rng.standard_normal((d, d)) * 0.1
    Wo = rng.standard_normal((d, d)) * 0.1
    out, w = multi_head_attention(x, Wq, Wk, Wv, Wo, h, causal=True)
    assert out.shape == x.shape, "MHA output shape must equal input shape"
    assert np.allclose(w.sum(axis=-1), 1.0), "attention weights per (head,row) must sum to 1"
    # causal: upper triangle ~ 0
    for head in range(h):
        for i in range(T):
            assert w[head, i, i+1:].sum() < 1e-6, "causal mask must zero future positions"
    # single-head sanity: attention without causal
    Q = x @ Wq; K = x @ Wk; V = x @ Wv
    _, w2 = attention(Q, K, V, causal=False)
    assert np.allclose(w2.sum(axis=-1), 1.0), "single-head weights rows sum to 1"
```

**verification_property**: attention 权重每行和为 1（`weights.sum(-1) ≈ 1`）；因果掩码使上三角权重 ≈ 0（防未来泄漏）；multi-head 输出形状与输入相同（`out.shape == x.shape`）。

## connection_to_unit

1. **框架对比**：starter.ipynb 用 `torch.nn.Linear` 做 W_q/W_k/W_v 投影 + `torch.softmax`，from-scratch 版用 `x @ Wq` + 手写 softmax（log-sum-exp 稳定版）；torch 的反向传播自动算梯度，from-scratch 版若要训练需接第3章的 mini autograd--但本 Day 只做前向，聚焦"注意力机制本身"。
2. **缩放因子的显形**：starter.ipynb 用 `Q @ K.T / np.sqrt(dk)` 一行带过，from-scratch 版在 `verification_property` 里通过"权重行和=1"间接验证缩放正确--更关键的是，去掉 `/np.sqrt(dk)` 后大 d_k 下 softmax 会饱和（可构造实验观察），这是 torch 版默认隐藏的数值陷阱。
3. **多头拆分对比**：starter.ipynb 的 torch 版用 `view(T, n_heads, dh).transpose` 操作张量，from-scratch 版用 numpy 的 `reshape + transpose` 完成同样的事--让"多头=把 d 维切成 h 份各自 attention"这个几何操作在纯数组上可见，不被 torch 的 einsum 抽象遮蔽。
4. **因果掩码的数值实现**：notes.md 讲"自回归生成不能看未来"，from-scratch 版用 `np.triu(-1e9)` 把上三角设为大负数，softmax 后归零--这是 GPT 家族因果掩码的最简实现，研究者能直接看到"防泄漏"是加法掩码而非乘法（乘 0 会破坏 softmax 归一化）。

## deep_dive_links

- [P7/02 Self Attention from Scratch - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/07-transformers-deep-dive/02-self-attention-from-scratch/README.md) - 自注意力 from scratch，本旗舰单元的核心理论锚点
- [P7/05 Full Transformer - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/07-transformers-deep-dive/05-full-transformer/README.md) - 完整 transformer（残差/LayerNorm/FFN 块组装）
- [P10/04 Pre-training Mini GPT - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/10-llms-from-scratch/04-pre-training-mini-gpt/README.md) - mini-GPT 预训练（本单元 attention 的下一步：堆叠成 GPT 前向）

## exercises

1. 在本单元 `starter.ipynb` TODO（torch 手写 Self-Attention）运行后，用上面的 `multi_head_attention` 在同一份营销文案的 token embedding 上跑前向，对比 torch 版与 numpy 版的 attention 权重矩阵（应数值一致，差异仅来自初始化随机性）。提示：固定 `np.random.default_rng(0)` 与 torch 同种子。
2. 实现"位置编码注入"：在 `multi_head_attention` 的输入 `x` 上加正弦位置编码 $PE_{(pos,2i)} = \sin(pos/10000^{2i/d})$，对应 notes.md 关键回顾 3。观察加 PE 前后 attention 权重的变化（同样 token 在不同位置的权重差异）。
3. 构造"长上下文成本实验"：令 $T = 64, 128, 256, 512$，测量 `multi_head_attention` 的运行时间，验证 $O(T^2)$ 增长。这与 notes.md "128K context window" 的成本讨论直接相关--from-scratch 让你摸到成本曲线。
4. TODO: 在 `practice.md` 的注意力可视化练习中，为本 from-scratch 实现添加"注意力热力图"输出（matplotlib 可视化 `weights[head]` 矩阵），标注营销文案中哪些 token 相互关联。这是 starter.ipynb TODO 的 from-scratch 版本。
