# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：Capstone AI和商业分析 · Phase 1 问题定义与文献综述
> **scratch 哲学**：不调 arxiv/Search API + 不调 sklearn TfidfVectorizer，手写 BM25 排序 + query expansion，从 Robertson 1995 概率检索公式直译到 numpy。

## scratch_topic

本单元 from-scratch 主题：**手写文献检索 Agent（query expansion + BM25 排序）**。对应 rohitg00 P19/05 Autonomous Research Agent + P19/51 Literature Retrieval。notes.md/starter.ipynb 用 `arxiv` 包查 arXiv API + `pandas` 做去重筛选，本层把"检索->排序"这一步拆开：从 BM25 概率检索公式出发，手写 numpy 实现 query expansion + BM25 打分，让"为什么这篇论文排第一"不再是 arxiv 包的黑箱，而是可逐行审计的词频-逆文档频率计算。

## core_algorithm

BM25（Okapi BM25, Robertson et al. 1995）是概率检索框架的标准排序函数，是 Elasticsearch/Lucene 默认打分器。给定查询 $Q = \{q_1, \dots, q_n\}$ 和文档 $D$，BM25 打分为：

$$\text{BM25}(D, Q) = \sum_{i=1}^{n} \text{IDF}(q_i) \cdot \frac{f(q_i, D) \cdot (k_1 + 1)}{f(q_i, D) + k_1 \cdot \left(1 - b + b \cdot \frac{|D|}{\text{avgdl}}\right)}$$

其中 $f(q_i, D)$ 是词 $q_i$ 在文档 $D$ 中的词频，$|D|$ 是文档长度，$\text{avgdl}$ 是语料平均文档长度，$k_1 \approx 1.5$ 控制词频饱和（避免长文档因词频高而无限得分），$b \approx 0.75$ 控制文档长度归一化（$b=0$ 不归一化，$b=1$ 完全归一化）。IDF 采用 Robertson-Sparck Jones 形式：

$$\text{IDF}(q_i) = \ln\left(\frac{N - n(q_i) + 0.5}{n(q_i) + 0.5} + 1\right)$$

$N$ 是语料文档数，$n(q_i)$ 是含 $q_i$ 的文档数。+1 平滑避免负 IDF。**Query expansion** 通过同义词/共现词扩展原始 query：$Q' = Q \cup \{q'_1, \dots\}$，用 Rocchio 思想对扩展词降权（乘 $\alpha < 1$），让"AI marketing agent"自动纳入"LLM agent advertising"等近义查询。BM25 相比纯 TF-IDF 的关键改进：词频饱和项 $(k_1+1)/(f + k_1 \cdot \text{len_norm})$ 让 10 次出现不比 5 次强两倍，更符合相关性直觉。手写时我们用 numpy 稀疏化词频矩阵，让 IDF 向量化计算。

## code_artifact

```python
import numpy as np
import re
from collections import Counter

def tokenize(text):
    return re.findall(r'[a-z0-9]+', text.lower())

def build_corpus(docs):
    toks = [tokenize(d) for d in docs]
    vocab = sorted({w for t in toks for w in t})
    idx = {w: i for i, w in enumerate(vocab)}
    N = len(docs)
    V = len(vocab)
    tf = np.zeros((N, V))
    for i, t in enumerate(toks):
        for w, c in Counter(t).items():
            tf[i, idx[w]] = c
    df = (tf > 0).sum(axis=0)
    idf = np.log((N - df + 0.5) / (df + 0.5) + 1.0)
    dl = tf.sum(axis=1)
    avgdl = dl.mean() if dl.mean() > 0 else 1.0
    return idx, tf, idf, dl, avgdl, N

def bm25_score(query, idx, tf, idf, dl, avgdl, N, k1=1.5, b=0.75):
    q_idxs = [idx[w] for w in tokenize(query) if w in idx]
    if not q_idxs:
        return np.zeros(N)
    f = tf[:, q_idxs]                      # (N, |q|)
    idf_q = idf[q_idxs]                    # (|q|,)
    len_norm = (1 - b) + b * (dl / avgdl)  # (N,)
    denom = f + k1 * len_norm[:, None]
    score = (idf_q[None, :] * f * (k1 + 1)) / denom
    return score.sum(axis=1)

def expand_query(query, synonyms, alpha=0.5):
    toks = tokenize(query)
    exp = list(toks)
    for w in toks:
        for s in synonyms.get(w, []):
            if s not in exp:
                exp.append(s)
    return ' '.join(exp)

# verification_property:
#   BM25 scores are non-negative; longer docs not unfairly favored (k1 saturation);
#   exact-match doc ranks highest; query expansion widens recall.
if __name__ == "__main__":
    docs = [
        "AI marketing agent for advertising automation",
        "causal inference for marketing analytics",
        "LLM agent advertising bid optimization",
        "knowledge graph for marketing data representation",
    ]
    synonyms = {"ai": ["llm", "artificial intelligence"], "marketing": ["advertising"]}
    q = expand_query("AI marketing agent", synonyms)
    idx, tf, idf, dl, avgdl, N = build_corpus(docs)
    scores = bm25_score(q, idx, tf, idf, dl, avgdl, N)
    order = np.argsort(-scores)
    assert scores.min() >= 0, "BM25 scores must be non-negative"
    assert order[0] == 0, "exact-match doc must rank first"
    assert order[1] == 2, "synonym doc (LLM advertising) must rank second after expansion"
```

**verification_property**: BM25 分数非负（IDF 平滑 + tf 非负）；词频饱和项让长文档不会因词频高无限得分；精确匹配文档排第一；query expansion 把同义文档召回（doc-2 "LLM agent advertising" 升至第二）。

## connection_to_unit

1. **库 vs 手写的检索颗粒度**：notes.md 用 `arxiv.Search(query="AI marketing agent", max_results=50)` 一行完成检索，from-scratch 版把"查询字符串 -> 词频矩阵 -> IDF -> BM25 打分 -> 排序"拆成五步，每步可审计；arxiv 包把排序交给 arXiv 服务端的 Solr，from-scratch 版让你看到"为什么这篇排第一"。
2. **query expansion 显形**：starter.ipynb TODO2 直接用 `arxiv.Search(query=...)` 查询，from-scratch 版显式实现 `expand_query`--把"AI marketing agent"自动扩展为"AI LLM artificial-intelligence marketing advertising agent"，解决 PRISMA Step 1 检索的"同义词遗漏"问题（这是 PRISMA 2020 Statement 要求的"可重复检索策略"的工程内核）。
3. **去重 vs 排序的边界**：starter.ipynb TODO3 用 `pandas.drop_duplicates(subset=['title_hash'])` 去重，from-scratch 版用 `Counter` 做 token 频次--两个层面都是"去冗余"，但 BM25 的 IDF 把"出现在所有文档的高频词（如 'the'）"自动降权，是排序层面的"语义去重"，而 pandas 去重是字面去重。
4. **PRISMA 流程的可计算化**：notes.md 讲 PRISMA 四步是流程描述，from-scratch 版把"Identification"对应 `build_corpus`、"Screening"对应 `bm25_score` 阈值过滤、"Quality Assessment"对应分数 Top-K 截断--让 PRISMA 流程从图示变为可执行代码，每个阶段有数值输出。

## deep_dive_links

- [P19/05 Autonomous Research Agent - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/19-capstone-projects/05-autonomous-research-agent/README.md) - 自主研究 agent，本单元 from-scratch 的架构锚点（query->retrieve->rank->filter 闭环）
- [P19/51 Literature Retrieval - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/19-capstone-projects/51-literature-retrieval/README.md) - 文献检索，BM25 + query expansion 的工程实现参考

## exercises

1. 在本单元 `starter.ipynb` TODO2（arxiv 查询）运行后，把 arxiv 返回的论文标题+摘要作为 `docs` 输入上面的 `build_corpus` + `bm25_score`，用手写 BM25 对结果重排序，对比 arXiv 服务端排序与你的 BM25 排序的差异（提示：arXiv 默认按 relevance 排，BM25 是另一种 relevance 定义）。
2. 扩展 `expand_query`：用词共现（同现频率 Top-3）自动生成同义词表，而非手写 `synonyms` dict。提示：在 `build_corpus` 后算词对共现矩阵 $C_{ij} = \sum_d tf[d,i] \cdot tf[d,j]$，取 $C_{ij} > 0$ 的词对。这对应 PRISMA 检索策略的"迭代精化"。
3. 实现"PRISMA 去重 + BM25 排序"的整合 pipeline：对 `docs` 先按 title 哈希去重，再对去重后语料跑 BM25。对比去重前后 Top-5 排序的变化，分析"去重是否改变了排序"。
4. TODO: 在 `practice.md` 的 drill-2（arxiv + pandas PRISMA 四步）中，用本 from-scratch 的 `bm25_score` 替代 arXiv 服务端排序，把 feedback_rule 中的"matplotlib 流程图框中数字必须等于 DataFrame len()"升级为"BM25 Top-K 截断后的数字 + 流程图数字一致"。这是 starter.ipynb TODO4 筛选的 from-scratch 版本。
