# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：技能4 AI驱动商业模式创新 · Day 4 平台战略 + 生态设计
> **scratch 哲学**：不调 networkx/pandas/matplotlib，手写邻接矩阵 + 度中心性 + core-periphery 划分 + tipping point 蒙特卡洛，从图论公式直译到 numpy。

## scratch_topic

本单元 from-scratch 主题：**手写平台生态网络的邻接矩阵表示 + core-periphery 结构检测 + tipping point 蒙特卡洛仿真**。对应 rohitg00 P13 Skills and Agent SDKs（生态工具）+ P16 Supervisor Orchestrator（编排核心）。notes.md/starter.ipynb 用 `networkx.MultiDiGraph` 构建 26 节点 40 边的平台生态网络 + `nx.core_periphery` / `nx.clustering` 算图指标 + `numpy` 蒙特卡洛 tipping point，本层把 networkx 的图算法全部去库化：纯 numpy 邻接矩阵 + 度中心性 + 均值阈值 core-periphery 划分 + sigmoid tipping 模型，让"谁是生态核心""平台什么时候 tipping"两个问题在白板级代码中显形。

## core_algorithm

平台生态网络 $G = (V, E)$ 用邻接矩阵 $A \in \{0,1\}^{n \times n}$ 表示，$A_{ij} = 1$ 当且仅当节点 $i$ 与 $j$ 有边。节点的度中心性（degree centrality）为：

$$d_i = \sum_{j=1}^{n} A_{ij}$$

度中心性衡量节点连接数--在平台生态中，平台节点（如 Hugging Face）的度远高于普通开发者，因为大量开发者/消费者/互补者与之相连。

core-periphery 结构检测把节点分为核心（core，度高、互联密集）和边缘（periphery，度低、只连核心）。连续型 Borgatti-Everett 模型最大化 $\rho = \sum_{ij} A_{ij} \delta_{ij}$（$\delta_{ij}$ 在 core-core 和 core-periphery 对为 1）。from-scratch 版用度均值阈值的离散近似：

$$\text{core} = \{i \in V \mid d_i \geq \bar{d}\}, \quad \bar{d} = \frac{1}{n}\sum_{i=1}^{n} d_i$$

tipping point（临界点）模型预判平台走向赢者通吃的概率。用 sigmoid 模型：

$$P(\text{tip}) = \sigma(\beta \cdot \text{NE} - \alpha \cdot \text{MH} + \epsilon), \quad \sigma(x) = \frac{1}{1+e^{-x}}, \quad \epsilon \sim \mathcal{N}(0, \sigma^2)$$

其中 NE 为网络效应强度，MH 为多归属率（multi-homing rate，参与者同时使用多平台的比例）。$\beta > 0$：网络效应越强，tipping 概率越高；$\alpha > 0$：多归属率越高，tipping 概率越低（多归属阻止锁定，抑制赢者通吃）。蒙特卡洛仿真通过多次采样 $\epsilon$ 取平均，估计期望 tipping 概率--这是 notes.md TODO6 "天道推演平台临界点蒙特卡洛"的 from-scratch 数学骨架。

## code_artifact

```python
import numpy as np

def build_adj(n_nodes, edges, directed=False):
    A = np.zeros((n_nodes, n_nodes))
    for i, j in edges:
        A[i][j] = 1
        if not directed: A[j][i] = 1
    return A

def degree_centrality(A):
    return A.sum(axis=1)

def core_periphery(A, threshold=None):
    deg = degree_centrality(A)
    if threshold is None: threshold = np.mean(deg)
    core = deg >= threshold
    return core, ~core

def tipping_prob(n_effect, multi_homing, beta=3.0, alpha=2.0, n_sim=1000, seed=0):
    rng = np.random.default_rng(seed)
    logits = beta * n_effect - alpha * multi_homing + rng.normal(0, 0.5, n_sim)
    return (1.0 / (1.0 + np.exp(-logits))).mean()

# verification_property:
#   star graph: center degree=n-1, leaves degree=1;
#   core_periphery: center is core, leaves are periphery;
#   tipping_prob increases with network_effect, decreases with multi_homing
if __name__ == "__main__":
    A = build_adj(5, [(0,1),(0,2),(0,3),(0,4)])
    deg = degree_centrality(A)
    assert deg[0] == 4 and np.all(deg[1:] == 1), f"deg={deg}"
    core, peri = core_periphery(A)
    assert core[0] and not core[1:].any(), "center is core"
    p1 = tipping_prob(0.8, 0.2, n_sim=5000, seed=0)
    p2 = tipping_prob(0.3, 0.7, n_sim=5000, seed=0)
    assert p1 > p2, f"high NE should tip more: {p1} vs {p2}"
    assert 0 <= p1 <= 1 and 0 <= p2 <= 1
```

**verification_property**: 星图的中心节点度 $= n-1$，叶节点度 $= 1$；core-periphery 划分把中心划入 core（$d_0 \geq \bar{d}$）、叶划入 periphery；tipping 概率随网络效应 NE 递增、随多归属率 MH 递减（`p1(NE=0.8,MH=0.2) > p2(NE=0.3,MH=0.7)`）。

## connection_to_unit

1. **networkx MultiDiGraph vs numpy 邻接矩阵**：starter.ipynb TODO1 用 `G = nx.MultiDiGraph()` + `G.add_node/add_edge` 构建生态网络，from-scratch 版用 `build_adj(n_nodes, edges)` 构建邻接矩阵--networkx 的节点属性/边属性（`node_type`/`relation`）在邻接矩阵中丢失，但图的拓扑结构（谁连谁）完整保留，让"图 = 邻接矩阵"这个数学定义可见。
2. **nx.degree vs 手写行求和**：starter.ipynb TODO2 用 `dict(G.in_degree())` / `nx.clustering` 算图指标，from-scratch 版用 `A.sum(axis=1)` 一行算度中心性--让"度 = 邻接矩阵行和"这个代数事实不被 networkx 的 API 遮蔽。聚类系数（triangles）需要三阶张量运算 $A^3$，from-scratch 暂未实现（练习 3 的内容）。
3. **nx.core_periphery vs 手写均值阈值**：notes.md 提到"核心-边缘结构分析"，from-scratch 版用 `deg >= np.mean(deg)` 的均值阈值划分--这是 Borgatti-Everett 连续模型的离散近似，让"core = 高度节点"这个直觉在代码中显形。
4. **tipping point 蒙特卡洛**：notes.md TODO6 用 `numpy` 做 tipping 蒙特卡洛 + 贝叶斯先验，from-scratch 版用 sigmoid 模型 $P(\text{tip}) = \sigma(\beta \cdot \text{NE} - \alpha \cdot \text{MH} + \epsilon)$ 手写--把"网络效应促进 tipping，多归属抑制 tipping"这个因果链编码进 sigmoid 的正负系数，比 networkx 的图指标更直接地回答"平台会不会赢者通吃"。

## deep_dive_links

- [P13/22 Skills and Agent SDKs - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/13-tools-and-protocols/22-skills-and-agent-sdks/README.md) - 技能与 SDK：平台生态中开发者/工具/SDK 的连接关系，本单元 from-scratch 生态网络图的工具层锚点
- [P16/05 Supervisor Orchestrator Pattern - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/16-multi-agent-and-swarms/05-supervisor-orchestrator-pattern/README.md) - supervisor 编排模式：平台生态中"核心节点编排边缘节点"的拓扑结构，core-periphery 划分的编排语义

## exercises

1. 在本单元 `starter.ipynb` TODO1（networkx 构建生态网络）运行后，用上面的 `build_adj` 把 notes.md 的 26 节点生态网络转为邻接矩阵，用 `degree_centrality` 算度，对比 networkx 的 `G.degree()` 输出（应一致）。识别度最高的 4 个节点（应为 4 个平台节点），验证它们被 `core_periphery` 划入 core。
2. 修改 `tipping_prob` 的参数 $\beta$ 和 $\alpha$，模拟 notes.md 的"MCP 生态零抽成 vs App Store 30% 抽成"场景：MCP 的多归属率更高（MH=0.7）但网络效应正在增长（NE=0.5），App Store 的多归属率低（MH=0.2）但网络效应强（NE=0.9）。对比两个平台的 tipping 概率，讨论开放生态能否阻止颠覆。
3. 为 `build_adj` 添加有向图支持（`directed=True`），计算入度/出度中心性，对应 notes.md 的 `G.in_degree()` / `G.out_degree()`。在平台生态中，平台的入度（被多少开发者/消费者连接）通常远高于出度--验证这一拓扑特征。
4. TODO: 在 `practice.md` 的 D3 drill（天道推演 tipping point）中，用 from-scratch `tipping_prob` 替代 numpy 蒙特卡洛 + 贝叶斯先验，输出不同参数组合下的 tipping 概率热力图（NE × MH 网格）。这是 starter.ipynb TODO6 的 from-scratch 版本。
