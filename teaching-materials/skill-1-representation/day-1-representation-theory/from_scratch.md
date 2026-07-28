# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：技能1 表示工程 · Day 1 表示学习理论基础 + DSR框架
> **scratch 哲学**：不调 sentence-transformers，手写 word2vec SGNS + 截断 SVD，从负采样损失和矩阵分解直译到 numpy。

## scratch_topic

本单元 from-scratch 主题：**手写 word2vec Skip-gram Negative Sampling (SGNS) + SVD 降维**。对应 rohitg00 P5/03 Word Embeddings Word2Vec + P1/11 Singular Value Decomposition。notes.md/starter.ipynb 用 sentence-transformers（预训练 BERT）将营销文本编码为 384 维 embedding，用 scikit-learn 做 t-SNE/PCA 降维--本层去库化：纯 numpy 从随机初始化训练 word2vec 嵌入，用 `np.linalg.svd` 做截断 SVD 降维，让"为什么分布式假设成立""为什么 SVD 能降维""为什么负采样替代 softmax"三个问题在白板级代码中显形。

## core_algorithm

**Skip-gram Negative Sampling (SGNS)** 基于"分布假设"--一个词的含义由其上下文决定。给定中心词 $w$ 和上下文词 $c$，SGNS 用 sigmoid 近似 softmax，目标函数为：

$$\mathcal{L}_{\text{SGNS}} = -\log\sigma(\mathbf{v}'_c \cdot \mathbf{v}_w) - \sum_{n \in \mathcal{N}} \log\sigma(-\mathbf{v}'_n \cdot \mathbf{v}_w)$$

其中 $\mathbf{v}_w$ 是词 $w$ 的输入向量（center embedding），$\mathbf{v}'_c$ 是词 $c$ 的输出向量（context embedding），$\mathcal{N}$ 是从 unigram 分布 $P(w) \propto \text{freq}(w)^{3/4}$ 采样的负样本集，$\sigma(x) = 1/(1+e^{-x})$。第一项最大化正样本（共现对）的点积，第二项最小化负样本（随机对）的点积。SGNS 用负采样替代全词表 softmax 的动机是计算效率：$O(|V|)$ 降为 $O(|\mathcal{N}|)$，$|\mathcal{N}| \ll |V|$。

**截断 SVD** 将词-上下文共现矩阵 $X \in \mathbb{R}^{V \times V}$ 分解为低秩近似：

$$X = U\Sigma V^T, \quad X_k = U_k \Sigma_k V_k^T = \sum_{i=1}^{k} \sigma_i \mathbf{u}_i \mathbf{v}_i^T$$

$U_k$ 的行向量即为词的 $k$ 维 embedding。SVD 保证 $X_k$ 是 $X$ 的最优秩-$k$ 近似（Eckart-Young 定理），即 $\|X - X_k\|_F$ 最小。这与 word2vec 的梯度下降训练形成互补：SVD 是精确分解（全局最优但需完整矩阵），SGNS 是迭代优化（近似但可流式处理）。两者从不同路径到达"分布式表示"--理解这一点才能诊断"sentence-transformers 的 384 维 vs word2vec 的 100 维 vs SVD 的 2 维"各自的信息瓶颈。

## code_artifact

```python
import numpy as np
from collections import Counter

def sgns(corpus, dim=16, window=2, neg=3, epochs=50, lr=0.05, seed=0):
    rng = np.random.default_rng(seed)
    cnt = Counter(w for s in corpus for w in s)
    vocab = list(cnt); w2i = {w:i for i,w in enumerate(vocab)}
    V = len(vocab); freq = np.array([cnt[w] for w in vocab], float)
    neg_tbl = rng.choice(V, 10000, p=freq/freq.sum())
    Win = rng.standard_normal((V, dim))*0.1; Wout = np.zeros((V, dim))
    sig = lambda x: 1.0/(1.0+np.exp(-np.clip(x,-30,30)))
    for _ in range(epochs):
        for s in corpus:
            idx = [w2i[w] for w in s if w in w2i]
            for i,ci in enumerate(idx):
                for j in range(max(0,i-window), min(len(idx),i+window+1)):
                    if j==i: continue
                    pos = [(idx[j], 1)]
                    negs = [(int(neg_tbl[r]), 0) for r in rng.integers(0,len(neg_tbl),neg)]
                    for t,label in pos+negs:
                        v=Win[ci]; u=Wout[t]; g=lr*(label-sig(v@u))
                        Win[ci]+=g*u; Wout[t]+=g*v
    return Win, w2i

def svd_reduce(X, k=2):
    U,S,Vt = np.linalg.svd(X, full_matrices=False)
    return U[:,:k]*S[:k]

# verification_property:
#   sgns: co-occurring words have higher cosine sim than non-co-occurring;
#   svd_reduce: output shape (V, k), low-rank approximation
if __name__ == "__main__":
    corpus = [["run","shoe","sport"], ["run","fast","shoe"], ["lipstick","red","beauty"],
              ["lipstick","color","beauty"], ["shoe","run","sport"]]
    W, w2i = sgns(corpus, dim=8, epochs=30, seed=0)
    cos = lambda a,b: a@b/(np.linalg.norm(a)*np.linalg.norm(b)+1e-9)
    sim_run_shoe = cos(W[w2i["run"]], W[w2i["shoe"]])
    sim_run_lip = cos(W[w2i["run"]], W[w2i["lipstick"]])
    assert sim_run_shoe > sim_run_lip, f"co-occur must be closer: {sim_run_shoe:.3f} vs {sim_run_lip:.3f}"
    X2 = svd_reduce(W, k=2)
    assert X2.shape == (len(w2i), 2), "SVD output shape must be (V, k)"
```

**verification_property**: SGNS 训练后，共现词对（"run"与"shoe"在 3 条句子中共现）的余弦相似度高于非共现词对（"run"与"lipstick"零共现）；SVD 降维输出形状为 $(V, k)$，保留低秩主成分。

## connection_to_unit

1. **预训练 vs 从零训练**：starter.ipynb TODO1 用 `SentenceTransformer('all-MiniLM-L6-v2')` 一行加载预训练 BERT 编码器，384 维 embedding 已在 10 亿句对上训练好；from-scratch 版的 `sgns` 从随机初始化开始在 5 条小语料上训练 30 epoch--前者是"站在巨人肩膀上"（迁移学习），后者是"从泥土烧砖"（理解训练本质）。sentence-transformers 能理解"跑步鞋"和"运动鞋"语义相关，而 from-scratch word2vec 只能学到"共现=相关"的统计信号--这正是 notes.md 关键回顾 1"范式转移"的底层逻辑。
2. **降维方法对比**：starter.ipynb TODO2 用 `sklearn.manifold.TSNE` 和 `sklearn.decomposition.PCA` 做降维可视化，t-SNE 用 t 分布解决拥挤问题（notes.md 关键回顾 4），PCA 本质就是 SVD；from-scratch 版的 `svd_reduce` 用 `np.linalg.svd` 直接做截断 SVD，让"Eckart-Young 定理保证最优低秩近似"这个数学保证在 3 行代码中显形。t-SNE 是非线性降维（保留局部结构），SVD/PCA 是线性降维（保留全局方差），理解差异才能选对工具。
3. **表示学习方法论对比**：notes.md 关键回顾 3 列出 Autoencoder/VAE/GAN/Flow 四种方法，starter.ipynb TODO3 用 torch 实现 Autoencoder（384->64 压缩）；from-scratch 版的 SGNS 是另一种表示学习方法--不是通过重建瓶颈（Autoencoder），而是通过预测上下文（分布式假设）。两种方法从不同约束出发到达"低维表示"，对应 CMU 10741 概念一"不加约束的表示学习没有意义"：Autoencoder 的约束是瓶颈维度，SGNS 的约束是负采样数量和嵌入维度。

## deep_dive_links

- [P5/03 Word Embeddings Word2Vec - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/05-nlp-foundations-to-advanced/03-word-embeddings-word2vec/README.md) - word2vec from scratch，本单元 from-scratch 的核心理论锚点，覆盖 SGNS/CBOW/层次 softmax
- [P1/11 Singular Value Decomposition - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/11-singular-value-decomposition/README.md) - SVD 降维的数学基础，Eckart-Young 定理与截断 SVD 的几何意义

## exercises

1. 在本单元 `starter.ipynb` TODO1（sentence-transformers 编码 20 条营销评论）运行后，用上面的 `sgns` 在同一份评论语料上训练 word2vec 嵌入（需先分词），对比 sentence-transformers 的 384 维语义 embedding 与 from-scratch word2vec 的低维统计 embedding 在"护肤正面评论"彼此相似度上的差异。提示：word2vec 需要更多语料才能学到稳定表示，观察小语料下的不稳定性。
2. 实现"共现矩阵 + SVD"路径：构建词-词共现矩阵 $X$（窗口内共现计数），用 `svd_reduce(X, k=2)` 降维，对比 SGNS 训练的 embedding 与 SVD 分解的 embedding 在 2D 散点图上的聚类结构。对应 notes.md 关键回顾 4 的降维方法对比。
3. 构造"负采样数量实验"：令 `neg=1, 3, 5, 10`，观察 SGNS 训练后共现词对的相似度变化。`neg` 越大，负样本越多，模型越能区分共现与随机--但训练更慢。这与 TODO4 中 KMeans 聚类的 K 选择类似：都是表示质量与计算成本的权衡。
4. TODO: 在 `practice.md` 的 D1 drill（文本编码）中，为本 from-scratch SGNS 实现添加"注意力可视化"：训练后将每个词的 embedding 用 `svd_reduce` 降到 2D，标注护肤/电子/健身三类颜色，观察 from-scratch word2vec 是否能分离三类产品。这是 starter.ipynb TODO2 的 from-scratch 对照版。
