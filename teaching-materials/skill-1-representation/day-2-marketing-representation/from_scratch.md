# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：技能1 表示工程 · Day 2 营销数据表示实战 + 多模态大模型演进
> **scratch 哲学**：不调 sentence-transformers / torch Two-Tower，手写 TF-IDF + 两塔余弦检索，从词频-逆文档频率和双塔点积直译到 numpy。

## scratch_topic

本单元 from-scratch 主题：**手写 TF-IDF 向量化 + 两塔检索模型**。对应 rohitg00 P5/02 Bag of Words TF-IDF + P5/22 Embedding Models Deep Dive。notes.md/starter.ipynb 用 sentence-transformers（预训练语义编码器）将客户行为/产品描述/营销文案编码为 384 维 embedding，用 torch 实现 Two-Tower 双塔 + InfoNCE 对比损失--本层去库化：纯 numpy 手写 TF-IDF 编码（无预训练），用 L2 归一化点积实现两塔检索，让"为什么 IDF 用 log""为什么余弦相似度要做归一化""两塔的查询塔和文档塔共享什么"三个问题在白板级代码中显形。

## core_algorithm

**TF-IDF** (Term Frequency - Inverse Document Frequency) 是词袋模型的经典加权方案。给定词 $t$、文档 $d$、语料库 $N$ 篇文档：

$$\text{tf-idf}(t, d) = \text{tf}(t, d) \times \text{idf}(t) = \text{tf}(t, d) \times \left[\log\frac{N+1}{\text{df}(t)+1} + 1\right]$$

其中 $\text{tf}(t,d)$ 是词 $t$ 在文档 $d$ 中的出现次数，$\text{df}(t)$ 是包含词 $t$ 的文档数。IDF 的 $\log$ 使权重随文档频率**反比**增长但增速放缓--出现在所有文档中的词 IDF 趋近 1（低区分度），仅出现在少数文档中的词 IDF 很大（高区分度）。加 1 平滑（$N+1$, $\text{df}+1$）避免零除和零 IDF。TF-IDF 的核心局限：无法理解语义（"跑步鞋"和"运动鞋"词不重叠则 TF-IDF 相似度为 0），这正是 sentence-transformers 用预训练 BERT 编码要解决的--理解这一局限才能理解"为什么需要语义嵌入"。

**两塔检索模型**用共享或独立编码器分别编码查询和文档，再用余弦相似度对齐：

$$\text{sim}(q, d) = \cos(\mathbf{z}_q, \mathbf{z}_d) = \frac{\mathbf{z}_q \cdot \mathbf{z}_d}{\|\mathbf{z}_q\| \|\mathbf{z}_d\|}$$

两塔的核心优势是**离线-在线分离**：文档塔预计算所有文档向量并存入 ANN 索引，在线只需查询塔编码一次 + 点积检索，复杂度 $O(1)$ per doc。TF-IDF 版两塔的 $\mathbf{z}$ 是词频加权向量，sentence-transformers 版的 $\mathbf{z}$ 是 BERT 语义向量，torch Two-Tower 版的 $\mathbf{z}$ 是 MLP 投影后的学习向量--三者的检索框架相同，差异仅在编码器的表达力。InfoNCE 损失（notes.md 关键回顾 2）训练 torch 版两塔使正样本相似度高、负样本低，而 TF-IDF 版无需训练--这恰好展示了"学习 vs 规则"的表示工程光谱。

## code_artifact

```python
import numpy as np
from collections import Counter

def tokenize(text):
    return text.lower().split()

def tfidf_encode(docs, w2i=None):
    tokens = [tokenize(d) for d in docs]
    if w2i is None:
        vocab = sorted(set(w for t in tokens for w in t))
        w2i = {w:i for i,w in enumerate(vocab)}
    V, N = len(w2i), len(docs)
    df = np.zeros(V); tf = np.zeros((N, V))
    for i, t in enumerate(tokens):
        for w, f in Counter(t).items():
            if w in w2i:
                tf[i, w2i[w]] = f; df[w2i[w]] += 1
    idf = np.log((N + 1) / (df + 1)) + 1
    return tf * idf, w2i

def two_tower_score(q_vec, d_vecs):
    # two-tower: query tower + doc tower, alignment = cosine sim
    qn = q_vec / (np.linalg.norm(q_vec) + 1e-9)
    dn = d_vecs / (np.linalg.norm(d_vecs, axis=1, keepdims=True) + 1e-9)
    return dn @ qn

# verification_property:
#   rare word idf > common word idf; cosine sim in [-1,1]; self-sim ~ 1
if __name__ == "__main__":
    queries = ["red lipstick beauty", "running shoe sport"]
    docs = ["red lipstick beauty", "lipstick color makeup", "sport shoe fast", "skincare cream"]
    _, w2i = tfidf_encode(queries + docs)
    Q, _ = tfidf_encode(queries, w2i)
    D, _ = tfidf_encode(docs, w2i)
    sims = two_tower_score(Q[0], D)
    assert sims[0] > 0.99, "identical query-doc must have sim ~1"
    assert np.all(sims <= 1.0 + 1e-6), "cosine sim <= 1"
    assert sims[1] > sims[3], "lipstick query must rank lipstick doc > skincare doc"
```

**verification_property**: 稀有词（"skincare"仅出现在 1 篇文档）的 IDF > 常见词（"lipstick"出现在 2 篇）的 IDF；余弦相似度范围 $[-1, 1]$，查询与自身文档相似度 $\approx 1$；查询"red lipstick beauty"与含"lipstick"的文档相似度高于不含的文档。

## connection_to_unit

1. **语义 vs 词法编码**：starter.ipynb TODO1-3 用 `SentenceTransformer('all-MiniLM-L6-v2')` 编码客户行为/产品描述/营销文案为 384 维语义向量，"提亮精华"和"烟酰胺"虽词不重叠但语义相似度高（预训练 BERT 学到了语义关系）；from-scratch 版的 `tfidf_encode` 只做词法匹配--"red lipstick beauty"和"lipstick color makeup"的相似度来自共享词"lipstick"，而非语义理解。这直接对应 notes.md"为什么用真实库而非手写TF-IDF"的论述：TF-IDF 无法理解语义是升级到 sentence-transformers 的根本动机。
2. **两塔架构的编码器差异**：starter.ipynb TODO4 用 torch 实现 Two-Tower，查询塔和文档塔各是 `nn.Linear(384, 128)` MLP，用 InfoNCE 损失训练使正样本（客户购买的产品）相似度高；from-scratch 版的 `two_tower_score` 用 TF-IDF 向量直接做余弦相似度--编码器是规则（TF-IDF）而非学习（MLP），无需训练但表达力弱。torch 版的 InfoNCE 损失让两塔在共享空间对齐，from-scratch 版的两塔共享词表（`w2i`）但向量空间天然相同（都是 TF-IDF），不需要学习对齐。
3. **检索流程对比**：notes.md 关键回顾 2 的两塔架构图"客户特征 -> Tower A -> u, 产品特征 -> Tower B -> v, cos(u,v)"在 from-scratch 版中直接映射为 `Q = tfidf_encode(queries)`, `D = tfidf_encode(docs)`, `sims = two_tower_score(Q[0], D)`；torch 版需要训练 MLP 参数，from-scratch 版零训练直接检索。理解零训练基线（TF-IDF）和训练基线（torch Two-Tower）的检索质量差距，才能量化 sentence-transformers 语义编码的增量价值。

## deep_dive_links

- [P5/02 Bag of Words TF-IDF - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/05-nlp-foundations-to-advanced/02-bag-of-words-tfidf/README.md) - TF-IDF from scratch，本单元 from-scratch 的核心理论锚点，覆盖词袋模型/IDF 加权/稀疏表示
- [P5/22 Embedding Models Deep Dive - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/05-nlp-foundations-to-advanced/22-embedding-models-deep-dive/README.md) - 嵌入模型深挖，对比 TF-IDF 稀疏表示与 dense embedding 的检索质量差异

## exercises

1. 在本单元 `starter.ipynb` TODO2（产品 embedding + cosine 相似度检索）运行后，用上面的 `tfidf_encode` + `two_tower_score` 在同一份产品描述上做 TF-IDF 检索，对比 sentence-transformers 语义检索与 TF-IDF 词法检索的 top-3 结果差异。提示：找一对"语义相似但词不重叠"的产品描述（如"跑步鞋"和"运动鞋"），观察 TF-IDF 是否漏检。
2. 实现"IDF 权重实验"：在上面的 `tfidf_encode` 中，分别用 `idf = 1`（纯 TF）、`idf = log(N/df)`（无平滑）、`idf = log((N+1)/(df+1))+1`（平滑版）三种 IDF，对比检索结果的变化。对应 notes.md 关键回顾 1 的"四大表示类型"中产品嵌入的编码方法选择。
3. 构造"两塔 vs 单塔"实验：上面的 `two_tower_score` 是两塔架构（查询和文档各自编码后对齐），改为"单塔"（查询和文档拼接后过一个 MLP 分类器），对比两种架构在相同数据上的检索质量。这与 TODO4 的 torch Two-Tower + InfoNCE 实验形成"规则两塔 -> 学习两塔 -> 学习单塔"的三段对比。
4. TODO: 在 `practice.md` 的 D1 drill（客户 embedding + KMeans 分群）中，用 `tfidf_encode` 替代 sentence-transformers 编码客户行为文本，观察 KMeans 聚类结果的变化。这是 starter.ipynb TODO1 的 from-scratch 对照版，帮助你理解"语义 embedding vs 词法 TF-IDF 对聚类质量的影响"。
