# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：技能2 AI原生企业架构 · Day 4 企业级架构 + 行动研究（收官）
> **scratch 哲学**：不调 networkx DAG + pandas DataFrame，手写 TOGAF 四层依赖图拓扑排序 + 关键路径 + 行动研究 KPI 改善幅度，从 DAG 最长路径直译到 numpy。

## scratch_topic

本单元 from-scratch 主题：**手写 TOGAF 四层依赖图（拓扑排序 + 关键路径）+ 行动研究 KPI 改善幅度计算**。对应 rohitg00 P17/01 Managed LLM Platforms + P14/28 Orchestration Patterns。notes.md/starter.ipynb 用 networkx 建模 17 节点 27 边架构依赖图 + pandas 分析 4 轮行动研究 KPI，本层去框架化：纯 numpy + collections 实现 DAG 拓扑排序（Kahn 算法）+ 最长加权路径（关键路径）+ KPI 改善幅度百分比，让"层间依赖方向""架构瓶颈节点""KPI 改善趋势"三个概念在白板级代码中显形--不依赖 networkx 的 `topological_sort` / `longest_path`，不依赖 pandas 的 `groupby` 聚合，手写 BFS 队列让 DAG 拓扑序的生成过程可见。

## core_algorithm

TOGAF 四层架构的依赖关系建模为有向无环图 $G = (V, E, L)$，其中 $L: V \to \{1,2,3,4\}$ 是层映射（业务/应用/数据/技术）。拓扑序保证层间依赖方向一致：

$$\text{topo}(G) = [v_1, \dots, v_n], \quad \forall (u,v) \in E: \text{idx}(u) < \text{idx}(v)$$

Kahn 算法用入度队列 BFS 生成拓扑序：每次取出入度为 0 的节点，移除其出边，新入度为 0 的节点入队。关键路径（critical path）是 DAG 上的最长加权路径，标识架构瓶颈：

$$\text{dist}(v) = \max_{(u,v) \in E} [\text{dist}(u) + w(v)], \quad \text{dist}(v_0) = w(v_0) \text{ for sources}$$

$$\text{CP}(G) = \max_{v \in V} \text{dist}(v)$$

行动研究 KPI 追踪把 Susman 五步螺旋的每轮指标量化为改善幅度：

$$\Delta_k = \frac{\text{KPI}_k(R) - \text{KPI}_k(0)}{\text{KPI}_k(0)} \times 100\%$$

正值表示改善（如决策质量 +50%），负值表示数值下降但可能也是改善（如决策时间 -40% 意味着更快）。关键路径标识架构单点故障：若 $\text{dist}(v) = \text{CP}(G)$，则 $v$ 在最长路径上，移除会导致下游全链路断裂。这把 TOGAF 架构图从"PPT 图"升级为可计算依赖图，是 DSR artifact 的工程基础。from-scratch 版用 Kahn BFS + 动态规划最长路径，比 networkx 的 `nx.topological_sort` + `nx.dag_longest_path` 更直白地暴露"入度归零 -> 入队"和"dist[v] = max(dist[u] + w[v])"的算法结构。

## code_artifact

```python
import numpy as np
from collections import defaultdict, deque

def topo_sort(nodes, edges):
    indeg = {n: 0 for n in nodes}
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v); indeg[v] += 1
    q = deque([n for n in nodes if indeg[n] == 0])
    order = []
    while q:
        n = q.popleft(); order.append(n)
        for m in adj[n]:
            indeg[m] -= 1
            if indeg[m] == 0: q.append(m)
    return order

def critical_path(nodes, edges, weights):
    order = topo_sort(nodes, edges)
    indeg = {n: 0 for n in nodes}
    for u, v in edges: indeg[v] += 1
    dist = {n: (weights.get(n, 1.0) if indeg[n] == 0 else 0.0) for n in nodes}
    for n in order:
        for u, v in edges:
            if u == n:
                dist[v] = max(dist[v], dist[n] + weights.get(v, 1.0))
    return max(dist.values()), dist

def kpi_improvement(kpi_rounds):
    keys = list(kpi_rounds[0].keys())
    arr = np.array([[r[k] for k in keys] for r in kpi_rounds])
    first, last = arr[0], arr[-1]
    return (last - first) / np.maximum(first, 1e-9) * 100.0, keys

# verification_property: topo_sort respects DAG; critical_path = longest weighted path; KPI improvement in %
if __name__ == "__main__":
    nodes = ["CDP", "Agent", "RAG", "Report", "Gov"]
    edges = [("CDP","Agent"), ("CDP","RAG"), ("Agent","Report"), ("RAG","Report"), ("Gov","Agent")]
    w = {"CDP":2, "Agent":3, "RAG":1, "Report":2, "Gov":1}
    order = topo_sort(nodes, edges)
    assert order.index("CDP") < order.index("Agent") < order.index("Report")
    cp, dist = critical_path(nodes, edges, w)
    assert cp == 7.0
    rounds = [{"time": 100, "quality": 0.6}, {"time": 80, "quality": 0.8}, {"time": 60, "quality": 0.9}]
    imp, keys = kpi_improvement(rounds)
    assert abs(imp[0] - (-40.0)) < 1e-6
    assert abs(imp[1] - 50.0) < 1e-6
```

**verification_property**: 拓扑序满足 `CDP` 在 `Agent` 前、`Agent` 在 `Report` 前（DAG 依赖方向一致）；关键路径 `CP = 7.0`（CDP->Agent->Report = 2+3+2）；KPI 改善幅度 time=-40%（下降即改善）、quality=+50%（上升即改善）。

## connection_to_unit

1. **DAG 建模对比**：starter.ipynb 用 `nx.DiGraph()` + `add_nodes_from` + `add_edges_from` + `nx.topological_sort()` 建模 17 节点 27 边架构图，from-scratch 版的 `topo_sort(nodes, edges)` 用 Kahn BFS（入度队列）手写拓扑排序--networkx 的 `topological_sort` 隐藏了"入度归零 -> 入队"的 BFS 过程，from-scratch 版让 `indeg[m] -= 1; if indeg[m] == 0: q.append(m)` 这个核心操作可见，研究者能直接看到拓扑序是如何"逐层剥离"生成的。
2. **关键路径的动态规划**：starter.ipynb 用 `nx.dag_longest_path(G)` 一行得到关键路径，from-scratch 版的 `critical_path` 用 `dist[v] = max(dist[v], dist[n] + weights.get(v, 1.0))` 按拓扑序动态规划--让"最长路径 = 拓扑序遍历 + dist 松弛"这个 DP 结构不被 networkx 的 C 实现遮蔽，是 notes.md "天道推演×企业架构"中"因果链追踪"的数值化形态。
3. **KPI 改善幅度从 pandas 到 numpy**：starter.ipynb TODO6 用 `df.groupby('phase')['kpi'].agg(['mean','std'])` + `(last-first)/first*100%` 计算改善幅度，from-scratch 版的 `kpi_improvement` 用 `np.array` + 向量运算 `(last - first) / np.maximum(first, 1e-9) * 100.0` --pandas 的 groupby 隐藏了"按阶段分片"操作，from-scratch 版把"构造矩阵 -> 首末行差分 -> 归一化"暴露为三步向量运算，`np.maximum(first, 1e-9)` 的除零保护是 pandas 自动处理的细节。
4. **层映射的外化**：notes.md 关键回顾 1 的"TOGAF 四层（业务/应用/数据/技术）"在 starter.ipynb 中用 networkx 的 `partition` dict 标注节点层级，from-scratch 版不显式建模层映射但通过 `edges` 的方向隐含层间依赖（`CDP->Agent` 表示数据层->应用层）--让"层 = 节点集合的划分 + 跨层边方向"这个 TOGAF 核心概念在裸 DAG 中可推理。

## deep_dive_links

- [P17/01 Managed LLM Platforms - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/17-infrastructure-and-production/01-managed-llm-platforms/README.md) - 托管 LLM 平台（企业级架构的技术层基础设施），本 from-scratch 单元 TOGAF 四层依赖图的技术层锚点
- [P14/28 Orchestration Patterns - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/14-agent-engineering/28-orchestration-patterns/README.md) - 编排模式（企业 Agent 编排拓扑），本单元架构依赖图中应用层节点间编排关系的参考

## exercises

1. 在本单元 `starter.ipynb` TODO4（networkx 架构依赖图 17 节点 27 边）运行后，用上面的 `topo_sort` + `critical_path` 在同一份节点/边列表上手动计算拓扑序与关键路径，对比 networkx 的 `nx.topological_sort` 与 `nx.dag_longest_path` 输出（应一致），解释差异来源（提示：networkx 的 longest_path 返回节点序列，from-scratch 版返回路径长度标量）。
2. 构造"单点故障实验"：从 5 节点 DAG 中移除 `Agent` 节点（关键路径上的节点），重新计算 `critical_path`，观察 CP 值下降幅度。再移除非关键路径上的 `Gov` 节点，观察 CP 不变。这与 notes.md "天道推演×企业架构"中"高杠杆点 = 小投入改变大局"直接相关--关键路径上的节点就是高杠杆点。
3. 为 `kpi_improvement` 添加"霍桑效应排除"功能：构造对照组 KPI 数据（无 AI 干预），计算处理组 vs 对照组的改善幅度差值 $\Delta_{\text{net}} = \Delta_{\text{treatment}} - \Delta_{\text{control}}$，当 $\Delta_{\text{net}} < 5\%$ 时标记"改善不显著"。对应 practice.md D3 drill 的"霍桑效应排除论证"。
4. TODO: 在 `practice.md` 的 D2 drill（TOGAF 四层依赖图）中，用 from-scratch 版的 `topo_sort` 替代 networkx 完成 Worked 阶段示范，为 17 节点图添加 `layer_map` 参数（节点->层号），验证拓扑序中层间依赖方向一致（业务层节点在应用层前，应用层在数据层前）。这是本单元既有 TODO4 的 from-scratch 补充。
