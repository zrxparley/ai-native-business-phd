# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：Capstone AI和商业分析 · Phase 6 系统实现与论文撰写
> **scratch 哲学**：不调 langsmith、不调 deepeval、不调 statsmodels，手写 IMRaD 结构校验 DFA + 引用图 HITS 影响力排序，从有限自动机 + 邻接矩阵幂迭代直译到 numpy。

## scratch_topic

本单元 from-scratch 主题：**手写 IMRaD 结构校验（DFA 状态机）+ 引用图影响力排序（HITS 算法）**。对应 rohitg00 P19/57 End to End Research Demo + P19/54 Paper Writer。notes.md/starter.ipynb 用 `langsmith @traceable` 追踪 + `deepeval GEval` 评估论文 + `statsmodels` 跑统计检验，本层把"论文结构合规性"与"引用影响力"两个可计算内核拆开：从 DFA 状态机校验 IMRaD 章节顺序 + HITS 超链接迭代算法出发，手写 numpy/python 实现论文结构校验器 + 引用图构建 + authority/hub 分数计算，让"论文是否符合 IMRaD""哪篇引用是核心 authority"不再是 deepeval 黑箱评分，而是可逐行审计的结构与图算法。

## core_algorithm

**IMRaD 结构校验** 用确定性有限自动机（DFA）建模。论文章节序列 $\sigma = (s_1, s_2, \dots, s_k)$，其中 $s_i \in \{\text{Intro}, \text{Methods}, \text{Results}, \text{Discussion}, \text{Other}\}$。合法 IMRaD 序列需满足偏序约束：Intro 必须在 Methods 前，Methods 在 Results 前，Results 在 Discussion 前。DFA 状态集 $Q = \{q_0, q_I, q_M, q_R, q_D, q_{acc}, q_{rej}\}$，转移函数：

$$\delta(q_0, \text{Intro}) = q_I, \quad \delta(q_I, \text{Methods}) = q_M, \quad \delta(q_M, \text{Results}) = q_R, \quad \delta(q_R, \text{Discussion}) = q_D \equiv q_{acc}$$

允许"Other"章节在任意态自环（$\delta(q, \text{Other}) = q$），允许 Methods/Results 重复出现（修订）。若任意章节缺失或乱序则进入 $q_{rej}$。

**引用图 HITS 算法**（Kleinberg 1999）：引用图 $G = (V, E)$，$e_{ij} = 1$ 表示论文 $i$ 引用论文 $j$。每篇论文同时是 authority（被引）和 hub（引用他人的好文章）。迭代更新：

$$\mathbf{a}^{(t+1)} = A^T \mathbf{h}^{(t)}, \quad \mathbf{h}^{(t+1)} = A \mathbf{a}^{(t+1)}$$

其中 $A \in \{0,1\}^{n \times n}$ 是引用邻接矩阵。每步归一化（$L_2$ 范数）防发散。收敛后 authority 分数 $\mathbf{a}^*$ 排序给出"被引最多/最重要"论文，hub 分数 $\mathbf{h}^*$ 给出"引用了最多好论文"的综述类文章。HITS 相比单纯 in-degree 的优势：一篇被多个高 hub 分数综述引用的论文获得更高 authority（间接引用证据聚合）。手写时用 `re` 解析类 BibTeX 引用，numpy 矩阵乘法迭代 HITS（通常 20-50 步收敛到主特征向量）。

## code_artifact

```python
import numpy as np
import re

IMRAD_ORDER = ["introduction", "methods", "results", "discussion"]

def validate_imrad(sections):
    # sections: list of (title, word_count); returns (is_valid, missing, order_ok)
    titles_lower = [t.lower() for t, _ in sections]
    found = {}
    for canonical in IMRAD_ORDER:
        match = [i for i, t in enumerate(titles_lower) if canonical in t]
        if match:
            found[canonical] = match[0]
    missing = [s for s in IMRAD_ORDER if s not in found]
    if missing:
        return False, missing, False
    order_ok = (found["introduction"] < found["methods"] < found["results"] < found["discussion"])
    return True, [], order_ok

def parse_citations(text):
    # parse \\cite{key1,key2} or [key1; key2] style citations -> list of keys
    cites = re.findall(r'\\cite\{([^}]+)\}|\[([a-z0-9]+(?:;\s*[a-z0-9]+)*)\]', text, re.IGNORECASE)
    keys = []
    for g1, g2 in cites:
        chunk = g1 if g1 else g2
        keys.extend([k.strip() for k in re.split(r'[;,]', chunk) if k.strip()])
    return keys

def build_citation_graph(papers):
    # papers: list of {id, citations: [key,...]} -> adjacency matrix (row i cites col j)
    ids = [p["id"] for p in papers]
    idx = {k: i for i, k in enumerate(ids)}
    n = len(ids)
    A = np.zeros((n, n))
    for p in papers:
        i = idx[p["id"]]
        for c in p.get("citations", []):
            if c in idx:
                A[i, idx[c]] = 1.0
    return A, ids

def hits(A, iters=50, tol=1e-6):
    # a = A^T h, h = A a ; normalize L2 each step
    n = A.shape[0]
    h = np.ones(n) / np.sqrt(n)
    a = np.ones(n) / np.sqrt(n)
    for _ in range(iters):
        a_new = A.T @ h
        h_new = A @ a_new
        na = np.linalg.norm(a_new) or 1.0
        nh = np.linalg.norm(h_new) or 1.0
        a_new, h_new = a_new / na, h_new / nh
        if np.linalg.norm(a_new - a) < tol and np.linalg.norm(h_new - h) < tol:
            a, h = a_new, h_new
            break
        a, h = a_new, h_new
    return a, h

# verification_property:
#   IMRaD validator rejects missing/out-of-order sections, accepts valid;
#   HITS converges; authority scores rank most-cited paper highest; hub scores rank survey highest.
if __name__ == "__main__":
    # IMRaD validation
    valid = [("Introduction", 900), ("Related Work", 700), ("Methods", 1100), ("Results", 950), ("Discussion", 650)]
    ok, miss, order = validate_imrad(valid)
    assert ok and order, "valid IMRaD must pass"
    bad_missing = [("Introduction", 900), ("Methods", 1100), ("Discussion", 650)]
    ok2, miss2, _ = validate_imrad(bad_missing)
    assert not ok2 and "results" in miss2, "missing Results must be flagged"
    bad_order = [("Methods", 1100), ("Introduction", 900), ("Results", 950), ("Discussion", 650)]
    ok3, _, order3 = validate_imrad(bad_order)
    assert ok3 and not order3, "out-of-order must flag order_ok=False"
    # citation graph + HITS
    papers = [
        {"id": "pearl1995", "citations": []},
        {"id": "he2008", "citations": ["pearl1995"]},
        {"id": "survey2020", "citations": ["pearl1995", "he2008"]},
        {"id": "novel2024", "citations": ["pearl1995", "he2008", "survey2020"]},
    ]
    A, ids = build_citation_graph(papers)
    a, h = hits(A)
    top_auth = ids[np.argmax(a)]
    top_hub = ids[np.argmax(h)]
    assert top_auth == "pearl1995", f"pearl1995 must be top authority (most cited), got {top_auth}"
    assert top_hub == "novel2024", f"novel2024 must be top hub (cites most), got {top_hub}"
```

**verification_property**: IMRaD 校验器拒绝缺失/乱序章节、接受合法结构；HITS 收敛；authority 分数排序使"被引最多"论文（pearl1995）排第一；hub 分数使"引用最多"论文（novel2024）排第一。

## connection_to_unit

1. **库 vs 手写的论文评估**：notes.md 用 `deepeval GEval` + 自定义 `BaseMetric` 五维度评估论文质量（IMRaD 完整性/统计依据/DSR 描述/可复现性/写作质量），from-scratch 版用 `validate_imrad` DFA 校验结构合规性--deepeval 的"IMRaD 完整性"维度本质就是这样的结构校验，但 from-scratch 版让"为什么缺 Results 被扣分"可见为具体的缺失章节列表，而非 LLM 黑箱分数。
2. **引用图 vs arxiv 文献对比**：starter.ipynb TODO7 用 `arxiv` 包搜索相关论文做文献对比，from-scratch 版用 `build_citation_graph` + `hits` 构建引用图--arxiv 包返回论文列表（无引用关系），from-scratch 版用引用边计算 authority 分数，让"哪篇论文是领域的 authority"从"检索排序"变为"图论影响力排序"。这是 Related Work 章节定位核心文献的 from-scratch 方法。
3. **可复现研究的 trace 校验**：starter.ipynb TODO2 用 `langsmith @traceable` 记录执行链，from-scratch 版的 `parse_citations` 用正则解析引用--两者都是"可审计的执行链"，但 langsmith trace 是运行时调用链，引用图是论文间依赖链。from-scratch 版让"可复现性"的"引用可追溯"维度可计算化。
4. **统计报告的结构化输出**：starter.ipynb TODO4 用 `statsmodels` 跑 t 检验/Cohen's d 输出 APA 格式，from-scratch 版的 `validate_imrad` 确保 Results 章节存在--APA 格式报告必须出现在 Results 节内，from-scratch 校验器把"统计报告的位置合规"显式化，这是 deepeval"统计依据"维度的结构前提。

## deep_dive_links

- [P19/57 End to End Research Demo - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/19-capstone-projects/57-end-to-end-research-demo/README.md) - 端到端研究演示，本单元 from-scratch 的 pipeline 锚点（IMRaD 校验 + 引用图作为论文生成 pipeline 的质量门控）
- [P19/54 Paper Writer - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/19-capstone-projects/54-paper-writer/README.md) - 论文写作器，IMRaD 章节生成 + 引用管理的工程参考

## exercises

1. 在本单元 `starter.ipynb` TODO5（IMRaD 论文草稿）生成后，用上面的 `validate_imrad` 校验你的草稿结构，对比 deepeval `GEval` 的"IMRaD 完整性"维度评分。提示：deepeval 用 LLM 判断结构完整性，from-scratch 用 DFA 判断--两者对"Related Work 是否可选"可能判断不同，分析差异。
2. 扩展 `validate_imrad` 为"字数合规校验"：检查 Introduction $\in [800, 1000]$、Methods $\in [1000, 1200]$、Results $\in [800, 1000]$、Discussion $\in [600, 800]$（notes.md 关键回顾 3 的字数规范）。输出字数违规章节列表。这是 deepeval"写作质量"维度的 from-scratch 结构化校验。
3. 在 TODO7（arxiv 文献对比）的 arxiv 检索结果上，用 `parse_citations` 从论文全文/摘要中解析引用，构建引用图，跑 HITS 排序。对比 HITS authority 排序与 arXiv 服务端 relevance 排序的差异。这对应 notes.md"文献定位"的图论方法。
4. TODO: 在 `practice.md` 的 drill 中，用本 from-scratch 的 `validate_imrad` + `hits` 替代 deepeval 论文评估，把 feedback_rule 中的"deepeval 五维度评分 >= 0.7"升级为"IMRaD DFA 校验通过 + HITS authority Top-3 引用覆盖 >= 80%"。这是 starter.ipynb TODO6 论文质量评估的 from-scratch 版本。
