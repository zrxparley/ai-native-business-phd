# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：Capstone AI和商业分析 · Phase 2 数据表示与知识图谱
> **scratch 哲学**：不调 networkx、不调 sentence-transformers，手写 KG 邻接矩阵 + 多跳检索 + 个性化 PageRank，从图论矩阵幂直译到 numpy。

## scratch_topic

本单元 from-scratch 主题：**手写知识图谱邻接矩阵 + 多跳检索（BFS 矩阵幂 + 个性化 PageRank）**。对应 rohitg00 P19/30 BPE Tokenizer from Scratch + P19/50 Hypothesis Generator。notes.md/starter.ipynb 用 `networkx.MultiDiGraph` 构建图谱 + `nx.shortest_path`/`nx.pagerank` 做图查询，本层把"图结构 -> 邻接矩阵 -> 多跳可达 -> 排序"拆开：从邻接矩阵幂运算 $A^k$ 与 PageRank 迭代公式出发，手写 numpy 实现 KG 三元组到邻接矩阵的构建 + K-hop 检索 + 个性化 PageRank，让"买了跑鞋的客户还买什么"这个多跳推理不再是 networkx 黑箱，而是可逐行审计的矩阵运算。

## core_algorithm

知识图谱的数学本质是有向图 $G = (V, E)$，其邻接矩阵 $A \in \{0,1\}^{n \times n}$ 满足 $A_{ij} = 1$ 当且仅当存在边 $i \to j$。多跳检索的核心是邻接矩阵的幂运算：$A^k$ 的元素 $(A^k)_{ij}$ 等于从节点 $i$ 到节点 $j$ 长度恰为 $k$ 的路径数。由矩阵乘法定义：

$$(A^k)_{ij} = \sum_{m_1=1}^{n} \sum_{m_2=1}^{n} \cdots \sum_{m_{k-1}=1}^{n} A_{im_1} A_{m_1 m_2} \cdots A_{m_{k-1} j}$$

K-hop 可达矩阵为 $R_K = \text{sign}\left(\sum_{k=1}^{K} A^k\right)$，标记所有 K 步内可达节点对。对于营销多跳推理"客户 -> 购买 -> 产品 -> 属于 -> 品类 -> 互补 -> 产品"，这正是 $A^3$ 的 reachable set。

**个性化 PageRank（PPR）** 给检索结果排序。设 $\mathbf{s} \in \mathbb{R}^n$ 为种子向量（查询节点 one-hot），$\alpha$ 为 teleport 概率（典型 0.15），转移矩阵 $P = D^{-1} A$（$D$ 为出度对角阵），PPR 迭代为：

$$\mathbf{r}^{(t+1)} = \alpha \mathbf{s} + (1-\alpha) P^T \mathbf{r}^{(t)}$$

收敛后 $\mathbf{r}$ 的非零分量即多跳相关节点的排序分数。PPR 相比纯 BFS 的优势：按路径数加权（多条路径到达的节点更相关），且 teleport 项保证收敛与非歧义性。手写时用 numpy 稀疏化邻接矩阵，$A^k$ 用 `np.linalg.matrix_power` 向量化，PPR 用不动点迭代（通常 20-50 步收敛）。

## code_artifact

```python
import numpy as np
from collections import defaultdict

def build_kg(triplets):
    # triplets: [(head, relation, tail), ...] -> adjacency matrix + index
    nodes = sorted({n for t in triplets for n in (t[0], t[2])})
    idx = {n: i for i, n in enumerate(nodes)}
    n = len(nodes)
    A = np.zeros((n, n))
    rels = defaultdict(list)
    for h, r, t in triplets:
        A[idx[h], idx[t]] = 1.0
        rels[r].append((idx[h], idx[t]))
    return idx, A, nodes, dict(rels)

def k_hop_reachable(A, seeds, K=3):
    # seeds: list of node indices; returns set of nodes reachable within K hops
    R = np.zeros_like(A)
    Ak = np.eye(A.shape[0])
    for k in range(1, K + 1):
        Ak = Ak @ A
        R = R + Ak
    reachable = set()
    for s in seeds:
        reachable.update(np.where(R[s] > 0)[0].tolist())
    return reachable

def personalized_pagerank(A, seeds, alpha=0.15, iters=50):
    n = A.shape[0]
    outdeg = A.sum(axis=1)
    outdeg[outdeg == 0] = 1.0
    P = A / outdeg[:, None]            # row-normalized transition
    s = np.zeros(n)
    for sd in seeds:
        s[sd] = 1.0 / len(seeds)
    r = s.copy()
    for _ in range(iters):
        r = alpha * s + (1 - alpha) * (P.T @ r)
    return r

# verification_property:
#   A^k counts k-length paths; PPR converges & seed nodes get highest scores;
#   multi-hop retrieval finds nodes unreachable by 1-hop (semantic similarity limit).
if __name__ == "__main__":
    triplets = [
        ("customer_1", "PURCHASED", "running_shoes"),
        ("running_shoes", "CATEGORIZED_AS", "sports_gear"),
        ("sports_gear", "COMPLEMENT", "knee_brace"),
        ("knee_brace", "CATEGORIZED_AS", "sports_gear"),
        ("customer_1", "PURCHASED", "water_bottle"),
    ]
    idx, A, nodes, rels = build_kg(triplets)
    seeds = [idx["customer_1"]]
    reach = k_hop_reachable(A, seeds, K=3)
    assert idx["knee_brace"] in reach, "3-hop must reach knee_brace via shoes->gear->brace"
    assert idx["water_bottle"] in reach, "1-hop direct purchase must be reachable"
    r = personalized_pagerank(A, seeds, alpha=0.15)
    top = np.argsort(-r)
    assert top[0] == idx["customer_1"], "seed must rank first in PPR"
    assert idx["knee_brace"] in top[:4], "PPR must surface multi-hop relevant node"
```

**verification_property**: 邻接矩阵幂 $A^k$ 计数 k 长路径（`A^3` 找到 customer->shoes->gear->brace 三跳）；PPR 收敛且种子节点得分最高；多跳检索找到 1-hop 语义相似度无法触达的节点（knee_brace 经三跳到达）。

## connection_to_unit

1. **库 vs 手写的图表示**：notes.md 用 `networkx.MultiDiGraph` 存节点+边+属性，from-scratch 版用邻接矩阵 $A \in \mathbb{R}^{n \times n}$--networkx 的 `G[u][v]` 查询对应 $A_{ij}$，`nx.shortest_path` 对应 $A^k$ 的非零位置，`nx.pagerank` 对应 PPR 不动点迭代。矩阵表示让"图结构"可被 numpy 向量化计算，是 GraphRAG 多跳检索的数值底座。
2. **多跳检索的显形**：starter.ipynb TODO4 用 `nx.shortest_path(G, customer, product)` 得到路径列表，from-scratch 版用 `k_hop_reachable(A, seeds, K=3)` 返回可达集--后者暴露了"K 跳"这个超参数（networkx 默认无 K 限制，但 PPR 实际衰减等价于软 K 截断），让"为什么 3 跳足够"可调参审计。
3. **PPR vs BFS 的排序差异**：starter.ipynb TODO5 的 GraphRAG 混合检索用 networkx 图查询返回节点集合（无排序），from-scratch 版的 `personalized_pagerank` 按路径数加权返回连续分数--多条路径到达的节点（如 sports_gear 被 shoes 和 brace 同时指向）PPR 分数更高，这是 networkx 默认 BFS 不提供的"多路径证据聚合"。
4. **三元组到矩阵的 ETL**：starter.ipynb TODO3 用 `G.add_edge(head, tail, relation=r)` 逐条加边，from-scratch 版用 `build_kg(triplets)` 一次性构建邻接矩阵+关系索引--让"三元组 -> 矩阵"的 ETL 显式化，这是 GraphRAG 实体关系抽取（LLM 抽三元组）之后的下一步工程。

## deep_dive_links

- [P19/30 BPE Tokenizer from Scratch - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/19-capstone-projects/30-bpe-tokenizer-from-scratch/README.md) - BPE 分词 from scratch，数据表示层的 token 化基础（本单元 KG 三元组抽取的文本预处理上游）
- [P19/50 Hypothesis Generator - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/19-capstone-projects/50-hypothesis-generator/README.md) - 假设生成器，KG 多跳检索支撑假设推理的下游应用

## exercises

1. 在本单元 `starter.ipynb` TODO4（networkx 图查询）运行后，用上面的 `k_hop_reachable` + `personalized_pagerank` 在同一份营销 KG（产品-品牌-品类-客户）上做多跳检索，对比 networkx `nx.shortest_path` 与 numpy 矩阵幂的可达集是否一致。提示：networkx 返回路径，from-scratch 返回可达集，需对齐语义。
2. 扩展 `build_kg` 支持加权边（关系权重）：把 PURCHASED 权重设为 1.0、COMPLEMENT 设为 0.5、CATEGORIZED_AS 设为 0.3，观察 PPR 排序的变化。这对应 notes.md 关键回顾 2 中八类关系的差异化重要性。
3. 实现"关系感知多跳检索"：用 `rels` 字典按关系类型过滤路径（如只走 PURCHASED->CATEGORIZED_AS->COMPLEMENT 三类边），而非全图 $A^k$。对比无过滤与有过滤的检索结果差异，分析"关系类型约束"对多跳推理精度的影响。
4. TODO: 在 `practice.md` 的 drill-3（GraphRAG 混合检索）中，用本 from-scratch 的 `personalized_pagerank` 替代 networkx 图查询部分，把 feedback_rule 中的"多跳召回率@5 > 传统向量RAG 至少20%"升级为"PPR Top-5 召回率 + 向量 Top-5 召回率的融合召回率"。这是 starter.ipynb TODO5 GraphRAG 混合检索的 from-scratch 版本。
