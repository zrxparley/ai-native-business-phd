# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：技能3 因果推断 · Day 4 因果发现与 ML 因果推断
> **scratch 哲学**：不调 causal-learn/gcastle 的 `pc()`，手写 PC 算法骨架（条件独立性检验 + v-结构定向），从精度矩阵与 Fisher Z 直译到 numpy。

## scratch_topic

本单元 from-scratch 主题：**手写 PC 算法骨架 + 条件独立性检验**。对应 rohitg00 P1 Graph Theory（DAG、d-分离）+ P2 Unsupervised Learning（结构学习）。notes.md/starter.ipynb TODO2 用 `causal-learn.pc()` 一行在糖尿病数据上发现因果图，本层把"从完全连接图逐步删边 + v-结构定向"拆成三步手写：精度矩阵求偏相关、Fisher Z 检验条件独立、unshielded triple 检测 collider，让"为什么某条边被删（哪个 sepset）""为什么某条边有向（哪个 v-结构）"在白板级代码中显形。

## core_algorithm

PC 算法（Spirtes-Glymour-Scheines 2000）从数据自动学因果图骨架与部分方向。**第一步骨架学习**：从完全连接无向图开始，对每对节点 $(i,j)$，寻找条件集 $S$ 使 $i\perp j\mid S$，找到则删除 $i$-$j$ 边并记录 $\text{sepset}(i,j)=S$。条件集大小从 $|S|=0$ 递增到 $|S|=k$，逐步收紧。

**条件独立性检验（高斯情形）**用偏相关 + Fisher Z 变换。偏相关由精度矩阵（逆协方差）给出：

$$\rho(i,j\mid S) = -\frac{P_{ij}}{\sqrt{P_{ii}\,P_{jj}}},\quad P=\left(\Sigma_{\{i,j\}\cup S,\{i,j\}\cup S}\right)^{-1}$$

Fisher Z 统计量在 $H_0$（条件独立）下近似标准正态：

$$z = \frac{1}{2}\ln\frac{1+r}{1-r}\sqrt{n-|S|-3} \sim \mathcal N(0,1),\quad r=\hat\rho(i,j\mid S)$$

$|z|<1.96$ 则接受独立、删边。

**第二步 v-结构定向**：对 unshielded triple $X\!-\!Z\!-\!Y$（$X,Y$ 不相邻），若 $Z\notin\text{sepset}(X,Y)$，则定向为 $X\to Z\leftarrow Y$（collider）。直觉：若 $Z$ 不在使 $X,Y$ 独立的条件集中，说明 $Z$ 不是 $X,Y$ 的共同原因，而是共同结果，故为 collider。链 $X\to Z\to Y$ 中 $Z\in\text{sepset}(X,Y)$（条件于 $Z$ 使 $X,Y$ 独立），不触发 v-结构，方向未定。PC 三大假设：因果马尔可夫、**因果充分性（无隐混杂）**、忠实性；FCI 放宽因果充分性，输出 PAG 用 $\leftrightarrow$ 标隐混杂--这是 from-scratch PC 的边界。

## code_artifact

```python
import numpy as np, math
from itertools import combinations

def partial_corr(C, i, j, S):
    idx = [i, j] + list(S)
    inv = np.linalg.pinv(C[np.ix_(idx, idx)])
    return -inv[0, 1] / math.sqrt(inv[0, 0] * inv[1, 1])

def ci_test(C, n, i, j, S):
    r = C[i, j] if not S else partial_corr(C, i, j, S)
    r = max(-0.9999, min(0.9999, r))
    z = 0.5 * math.log((1 + r) / (1 - r)) * math.sqrt(n - len(S) - 3)
    return abs(z) < 1.96  # Fisher Z, two-sided alpha=0.05

def pc_skeleton(C, n, nodes, max_k=2):
    adj = {frozenset({i, j}) for i in nodes for j in nodes if i < j}
    sepset = {}
    for k in range(max_k + 1):
        for pair in list(adj):
            i, j = sorted(pair); others = [x for x in nodes if x not in pair]
            if len(others) < k: continue
            for S in combinations(others, k):
                if ci_test(C, n, i, j, S):
                    adj.discard(pair); sepset[pair] = set(S); break
    return adj, sepset

def orient_v_structures(adj, sepset, nodes):
    arrows = set()
    nbr = {n: {m for p in adj if n in p for m in p if m != n} for n in nodes}
    for z in nodes:
        for x, y in combinations(list(nbr[z]), 2):
            if frozenset({x, y}) not in adj and z not in sepset.get(frozenset({x, y}), set()):
                arrows.add((x, z)); arrows.add((y, z))
    return arrows

# verification_property: chain X->Z->Y removes X-Y edge (Z d-sep); no v-structure on chain.
if __name__ == "__main__":
    rng = np.random.default_rng(0); n = 3000
    X = rng.standard_normal(n); Z = X + 0.5 * rng.standard_normal(n); Y = Z + 0.5 * rng.standard_normal(n)
    C = np.corrcoef(np.column_stack([X, Z, Y]).T); nodes = [0, 1, 2]
    adj, sepset = pc_skeleton(C, n, nodes, max_k=1)
    assert frozenset({0, 2}) not in adj, "chain: X-Y edge must be removed (Z d-separates)"
    assert frozenset({0, 1}) in adj and frozenset({1, 2}) in adj, "X-Z and Z-Y edges kept"
    arr = orient_v_structures(adj, sepset, nodes)
    assert (0, 1) not in arr and (2, 1) not in arr, "chain must NOT trigger v-structure"
```

**verification_property**: 链 $X\to Z\to Y$ 上，PC 骨架学习删除 $X$-$Y$ 边（条件于 $Z$ 后独立，sepset={Z}），保留 $X$-$Z$ 与 $Z$-$Y$；v-结构检测因 $Z\in\text{sepset}(X,Y)$ 不触发定向（链非 collider），输出无向边。

## connection_to_unit

1. **causal-learn `pc()` vs 手写 PC 的颗粒度**：starter.ipynb TODO2 用 `from causal-learn.causalDiscovery import pc; pc(data)` 一行返回 CPDAG，from-scratch 版拆成 `pc_skeleton`（逐对 CI 检验删边）+ `orient_v_structures`（collider 定向）--让 practice.md D1 feedback"无向边=方向未定（v-结构未触发），有向边=数据支持的方向"在代码层可逐行审计：每条删去的边都有 sepset 记录，每条有向边都来自一个 unshielded triple。
2. **Fisher Z 假设的显形**：causal-learn 默认 Fisher Z CI 检验假设高斯线性关系，from-scratch 版用 `np.corrcoef` + 精度矩阵显式假设高斯--这让 notes.md"关键回顾4 NOTEARS 放宽到非线性"的动机可见：PC 的 Fisher Z 在非线性关系（如 diabetes 的 age-glucose）上会漏边，NOTEARS-MLP 是 remedy。
3. **因果充分性边界**：notes.md"关键回顾2/3"对比 PC（假设无隐混杂）与 FCI（放宽，输出 PAG $\leftrightarrow$）；from-scratch PC 无 FCI 扩展，构造未观测混杂时（练习3）会产出伪边或错向--这是 from-scratch 刻意暴露的边界，让"为什么需要 FCI"从结论变成可复现的失败。
4. **PC（发现）vs CausalForestDML（估计）的分工**：TODO2 用 PC 发现结构（无处理/结果区分），TODO5 用 CausalForestDML 估 CATE（需已知 T/Y）；from-scratch PC + day-3 from-scratch DML 拼成"先发现结构、再估计效应"两步管线，对应 notes.md"关键回顾1 因果发现 vs 因果推断"的输入/输出/前提对比表。

## deep_dive_links

- [P1/21 Graph Theory - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/21-graph-theory/README.md) - 图论：DAG、d-分离、v-结构、骨架学习的数学基础
- [P2/07 Unsupervised Learning - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/07-unsupervised-learning/README.md) - 无监督学习：结构学习作为无监督因果发现的理论定位

## exercises

1. 在本单元 `starter.ipynb` TODO2（causal-learn `pc()` 糖尿病数据）运行后，用 `pc_skeleton` + `orient_v_structures` 在同一份 `np.corrcoef` 相关矩阵上跑（max_k=2），对比发现的骨架。列出一致边与不一致边，并用 sepset 解释每条删边的原因；alpha=0.05 硬编码为 1.96，尝试改为 2.58（α=0.01）观察边数变化。
2. 构造 collider $X\to Z\leftarrow Y$（$X,Y$ 独立，共同 cause $Z$）：`X=rag; Y=rng; Z=X+Y+noise`。跑 from-scratch PC：k=0 时 $X$-$Y$ 边因独立被删（sepset={}），`orient_v_structures` 检测 $Z\notin\text{sepset}(X,Y)$ 定向 $X\to Z\leftarrow Y$。验证并解释：为何链 $X\to Z\to Y$（$Z\in$ sepset）不定向、collider（$Z\notin$ sepset）定向。
3. 在 `practice.md` D1 feedback"糖尿病数据可能有隐混杂（age/genetics），PC 假设无隐混杂，FCI 放宽此假设"指导下，构造未观测混杂 $U\to X, U\to Y$（$U$ 不入数据），重跑 from-scratch PC，观察它产出伪 $X$-$Y$ 边或错向。这是因果充分性违反的 from-scratch 反证，解释 FCI 的 $\leftrightarrow$ 边如何标记此情形。
4. TODO: 为 `pc_skeleton` 添加可配置 CI 检验（把 Fisher Z 换成置换检验 partial corr p-value），在 NSW 前 5 变量子集上对比两种 CI 检验发现的边--这是 TODO3（notes.md"关键回顾2 PC on NSW"）的 from-scratch 版，理解 CI 检验选择如何影响发现结果。
