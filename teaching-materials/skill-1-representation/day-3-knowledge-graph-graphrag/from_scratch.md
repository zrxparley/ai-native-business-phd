# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：技能1 表示工程 · Day 3 企业知识图谱 + GraphRAG
> **scratch 哲学**：不调 networkx / LLMGraphTransformer，手写三元组抽取 + 邻接矩阵幂运算多跳检索，从正则模式和矩阵代数直译到 numpy。

## scratch_topic

本单元 from-scratch 主题：**手写 KG 三元组抽取 + 多跳图检索**。对应 rohitg00 P5/26 Relation Extraction KG + P11/06 RAG + P5/23 Chunking Strategies RAG。notes.md/starter.ipynb 用 networkx 构建营销知识图谱（7 类实体 8 类关系），用 LLMGraphTransformer 从文本自动抽取实体关系，用 networkx 的 `shortest_path`/`louvain_communities` 做图查询--本层去库化：纯 numpy + re 手写正则模式三元组抽取，用邻接矩阵幂运算 $A^k$ 实现 k-hop 可达性检索，让"三元组如何从文本提取""多跳检索的矩阵代数本质""GraphRAG vs 向量 RAG 的检索差异"三个问题在白板级代码中显形。

## core_algorithm

**三元组抽取**是知识图谱构建的核心步骤。给定文本，抽取 $(h, r, t)$ 三元组--头实体 $h$、关系 $r$、尾实体 $t$。from-scratch 版用正则模式匹配（如 `X -> 关系 -> Y`），生产系统用 LLM（如 LLMGraphTransformer）或依存句法分析。形式化地，三元组抽取是一个映射函数：

$$\text{Extract}: \text{text} \rightarrow \{(h_i, r_i, t_i)\}_{i=1}^{m}$$

正则版依赖人工设计的模式模板，覆盖率高但泛化弱；LLM 版泛化强但需 API 调用且不可审计。理解正则版的局限（无法抽取隐式关系），才能理解 notes.md"为什么用 LLMGraphTransformer"。

**多跳图检索**的矩阵代数基础是邻接矩阵幂运算。给定有向图 $G=(V,E)$，邻接矩阵 $A \in \{0,1\}^{|V| \times |V|}$，$A_{ij}=1$ 当且仅当存在边 $i \to j$。矩阵幂的核心性质：

$$[A^k]_{ij} = \text{从 } i \text{ 到 } j \text{ 长度恰为 } k \text{ 的路径数}$$

因此 k-hop 可达矩阵为：

$$R_k = \left(\sum_{i=1}^{k} A^i\right) > 0$$

$[R_k]_{ij} = \text{True}$ 当且仅当存在从 $i$ 到 $j$ 长度 $\leq k$ 的路径。这是 GraphRAG 多跳检索的数学本质：沿图边做多步推理，而非向量相似度匹配。notes.md 关键回顾 3 的对比表"传统RAG 向量检索 vs GraphRAG 多跳推理"，在 from-scratch 版中体现为"TF-IDF 点积检索 vs $A^k$ 矩阵幂检索"--前者是连续空间的最近邻，后者是离散空间的路径可达性，两者在数学结构上完全不同，决定了它们能回答的问题类型不同。

## code_artifact

```python
import numpy as np
import re

def extract_triples(texts):
    # Pattern-based extraction: (subject, relation, object)
    pat = re.compile(r'(\S+)\s*->\s*(\S+)\s*->\s*(\S+)')
    triples = []
    for text in texts:
        m = pat.search(text.strip())
        if m:
            triples.append((m[1], m[2], m[3]))
    return triples

def multi_hop_matrix(triples, hops=2):
    # Build adjacency matrix; k-hop reachability via matrix power
    nodes = sorted({n for h,_,t in triples for n in (h,t)})
    idx = {nd:i for i,nd in enumerate(nodes)}
    A = np.zeros((len(nodes), len(nodes)))
    for h, _, t in triples:
        A[idx[h], idx[t]] = 1
    R = np.zeros_like(A); Ak = np.eye(len(nodes))
    for k in range(1, hops+1):
        Ak = Ak @ A; R += Ak
    return (R > 0), nodes, idx

# verification_property: k-hop reachability via matrix power; 2-hop node not in 1-hop
if __name__ == "__main__":
    texts = ["跑鞋 -> 属于 -> 运动装备", "运动装备 -> 互补 -> 运动护具", "护膝 -> 属于 -> 运动护具"]
    triples = extract_triples(texts)
    assert len(triples) == 3, f"expected 3 triples, got {len(triples)}"
    R, nodes, idx = multi_hop_matrix(triples, hops=2)
    i_run = idx["跑鞋"]
    assert R[i_run, idx["运动装备"]], "1-hop must be reachable"
    assert R[i_run, idx["运动护具"]], "2-hop must be reachable"
    R1, _, _ = multi_hop_matrix(triples, hops=1)
    assert not R1[i_run, idx["运动护具"]], "2-hop must not be reachable in 1-hop"
```

**verification_property**: 三元组抽取从 3 条文本中提取 3 个 $(h,r,t)$ 三元组；2-hop 可达矩阵包含 1-hop（"跑鞋" -> "运动装备"）和 2-hop（"跑鞋" -> "运动装备" -> "运动护具"）节点；1-hop 可达矩阵不包含 2-hop 节点（"运动护具"不在 1-hop 结果中）。

## connection_to_unit

1. **图构建库 vs 手写**：starter.ipynb TODO1 用 `networkx.MultiDiGraph()` 构建知识图谱，`G.add_edge(h, t, relation=r)` 一行加边，自带 `successors()`/`predecessors()`/`shortest_path()` 等图算法；from-scratch 版用 `re` 正则抽取三元组 + numpy 邻接矩阵存图，`A[idx[h], idx[t]] = 1` 手动建边。networkx 封装了图数据结构（邻接表/多重边/属性），from-scratch 版用邻接矩阵让"图 = 矩阵"这个数学对等关系直接可见--这是 notes.md 关键回顾 2 中 TransE/RotatE/ComplEx KGE 方法的共同基础。
2. **多跳检索实现对比**：starter.ipynb TODO5 用 `nx.single_source_shortest_path(G, source, cutoff=3)` 做 3 跳检索（BFS），notes.md 前沿补充提到 GraphRAG 用 Leiden 社区检测 + 社区摘要做 Global/Local/DRIFT 三种搜索；from-scratch 版用 $R_k = \sum_{i=1}^{k} A^i > 0$ 矩阵幂做可达性判定。BFS 是 $O(|V|+|E|)$ 逐边遍历，矩阵幂是 $O(|V|^k)$ 逐层乘法--两者算法不同但数学等价。理解矩阵幂形式才能理解"为什么 KGE 把图嵌入到向量空间"：TransE 的 $h+r \approx t$ 本质是把 $A^k$ 的离散路径推理压缩为连续空间的向量运算。
3. **三元组抽取方式对比**：notes.md 提到 `langchain_experimental.LLMGraphTransformer` 用 LLM 从文本自动抽取实体关系（需 API Key），from-scratch 版用 `re.compile(r'(\S+)\s*->\s*(\S+)\s*->\s*(\S+)')` 正则匹配。LLM 版能抽取隐式关系（"苹果公司生产的iPhone" -> (苹果公司, 生产, iPhone)），正则版只能抽取显式模式（"X -> R -> Y" 格式）。这对应 notes.md 关键回顾 3"GraphRAG 构建成本高（需 LLM 抽取实体关系）"的根源：自动抽取的泛化能力直接决定图谱覆盖度。

## deep_dive_links

- [P5/26 Relation Extraction KG - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/05-nlp-foundations-to-advanced/26-relation-extraction-kg/README.md) - 关系抽取与 KG 构建，本单元 from-scratch 三元组抽取的理论锚点，覆盖正则/依存/LLM 三路抽取
- [P11/06 RAG - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/06-rag/README.md) - RAG 基础，对比向量 RAG 与 GraphRAG 的检索机制差异
- [P5/23 Chunking Strategies RAG - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/05-nlp-foundations-to-advanced/23-chunking-strategies-rag/README.md) - RAG 分块策略，GraphRAG 社区检测的分块替代方案

## exercises

1. 在本单元 `starter.ipynb` TODO1（networkx 构建营销知识图谱）运行后，用上面的 `extract_triples` 从同样的营销文本中抽取三元组，对比 networkx 的 `G.add_edge()` 手动建图与 from-scratch 正则抽取的覆盖率差异。提示：找一条不含 `->` 格式的营销文本（如"耐克是运动品牌"），观察正则版是否漏抽。
2. 实现"k-hop 路径计数"：上面的 `multi_hop_matrix` 返回可达性布尔矩阵 $R_k > 0$，修改为返回路径计数矩阵 $P_k = \sum_{i=1}^{k} A^i$（不做 `> 0`）。观察 $[P_k]_{ij}$ 的值表示什么（$i$ 到 $j$ 的长度 $\leq k$ 的路径总数）。对应 notes.md 关键回顾 2 的 TransE margin loss：路径数多的节点对在 KGE 中应有更高的链接预测概率。
3. 构造"GraphRAG vs 向量 RAG"对比实验：用上面的 `multi_hop_matrix` 回答多跳问题"买跑鞋的客户还买什么"（2-hop: 跑鞋 -> 运动装备 -> 运动护具），再用 Day 2 from_scratch 的 `tfidf_encode` + `two_tower_score` 做向量检索回答同样问题。对比两者能否找到"运动护具"这个 2-hop 答案--向量检索只能找语义相似项，无法沿关系链推理。这与 starter.ipynb TODO6 的 GraphRAG vs TF-IDF 对比实验直接对应。
4. TODO: 在 `practice.md` 的 D3 drill（GraphRAG 对比）中，为本 from-scratch `multi_hop_matrix` 实现添加"社区检测"简化版：用 numpy 计算度中心性 `A.sum(axis=1)` 和 PageRank 简化版 $PR = (1-d)/N + d \cdot A^T \cdot PR$（迭代 10 次），标注图中哪些节点是"流量枢纽"。这是 starter.ipynb TODO3 图查询（中心性分析）的 from-scratch 对照版。
