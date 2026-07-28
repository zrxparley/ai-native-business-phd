# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：选修E10 Agent经济 · Day 1 Agent作为经济主体
> **scratch 哲学**：不调 mesa 的贝叶斯 ABM 黑箱，手写 payoff_matrix + best_response 迭代，从 Nash 均衡存在性定理直译到 numpy。

## scratch_topic

本单元 from-scratch 主题：**手写博弈论收益矩阵 + Nash 均衡求解（最佳反应迭代 / fictitious play）**。对应 rohitg00 P16/21 Agent Economies（多 Agent 市场博弈）+ P9/07 Actor-Critic（策略学习框架）。notes.md/starter.ipynb 用 mesa 构建买方/卖方 Agent 的贝叶斯价格信念 + A2A 协商（一种学习型仿真），本层把 Agent 作为经济主体的策略交互拆开：从 Nash 均衡的存在性定理与最佳反应映射出发，手写 numpy 实现 fictitious play 求解 2 人有限博弈的混合策略 Nash，让"Agent 经济的均衡"从 mesa 涌现黑箱变成可逐行审计的博弈论计算。

## core_algorithm

Nash 均衡是博弈论的核心解概念。给定有限博弈 $G = \langle N, (S_i), (u_i) \rangle$（玩家集 $N$、策略集 $S_i$、收益 $u_i$），混合策略组合 $\sigma^* = (\sigma_i^*)_{i \in N}$ 是 Nash 均衡，当且仅当对每个玩家 $i$ 和每个替代策略 $\sigma_i$：

$$u_i(\sigma_i^*, \sigma_{-i}^*) \geq u_i(\sigma_i, \sigma_{-i}^*)$$

**Nash 存在性定理**（Nash 1950）：任何有限博弈至少存在一个混合策略 Nash 均衡。证明基于 Kakutani 不动点定理——构造最佳反应对应 $BR: \Delta \rightrightarrows \Delta$（$\Delta$ 为混合策略单纯形），$BR(\sigma) = (BR_i(\sigma_{-i}))_i$，其中 $BR_i(\sigma_{-i}) = \arg\max_{\sigma_i} u_i(\sigma_i, \sigma_{-i})$。$BR$ 是上半连续、非空凸值对应，由 Kakutani 不动点定理存在 $\sigma^* \in BR(\sigma^*)$，即 Nash 均衡。

**Fictitious Play**（Brown 1951）是求 Nash 的迭代算法：每个玩家维护对手历史行为的经验频率 $\hat\sigma_{-i}^{(t)}$，每轮最佳响应 $a_i^{(t)} \in BR_i(\hat\sigma_{-i}^{(t)})$，更新经验频率。Robinson 1951 证明 fictitious play 在 2 人零和博弈收敛到 Nash；更一般地，2x2 博弈与势博弈也收敛。经验频率 $\bar\sigma_i^{(t)} = \frac{1}{t}\sum_{\tau<t} \mathbf{1}[a_i^{(\tau)}]$ 收敛到 Nash 策略。

**2x2 混合 Nash 闭式解**（无差异原则）：让对手在两个纯策略间无差异。对列玩家收益 $B = [[b_{11}, b_{12}], [b_{21}, b_{22}]]$，行玩家混合概率 $p^*$ 使列玩家无差异：

$$p^* b_{11} + (1-p^*) b_{21} = p^* b_{12} + (1-p^*) b_{22} \quad \Rightarrow \quad p^* = \frac{b_{22} - b_{21}}{b_{11} - b_{12} - b_{21} + b_{22}}$$

当 $p^* \notin [0,1]$ 时无内部混合均衡，退化为纯策略 Nash。fictitious play 的经验频率收敛速率 $O(1/\sqrt{t})$。Agent 作为经济主体在 A2A 协商中的"报价-接受"决策本质是一个博弈，Nash 均衡给出"理性 Agent 长期会收敛到什么策略"的预测，与 mesa 的贝叶斯学习路径互补。

## code_artifact

```python
import numpy as np

def best_response_iter(payoff_A, payoff_B, n_iter=20000, tol=1e-7):
    # 2-player normal-form game. Fictitious play (Brown 1951) -> mixed Nash.
    # Converges for zero-sum (Robinson 1951), 2x2, potential games.
    n_row, n_col = payoff_A.shape
    row_counts = np.ones(n_row)
    col_counts = np.ones(n_col)
    p_prev = row_counts / row_counts.sum()
    q_prev = col_counts / col_counts.sum()
    for _ in range(n_iter):
        q_belief = col_counts / col_counts.sum()
        p_belief = row_counts / row_counts.sum()
        br_row = int(np.argmax(payoff_A @ q_belief))
        br_col = int(np.argmax(p_belief @ payoff_B))
        row_counts[br_row] += 1
        col_counts[br_col] += 1
        p = row_counts / row_counts.sum()
        q = col_counts / col_counts.sum()
        if np.max(np.abs(p - p_prev)) < tol and np.max(np.abs(q - q_prev)) < tol:
            break
        p_prev, q_prev = p, q
    return p, q

def nash_mixed_closed_form_2x2(payoff_B):
    # Indifference: p*b11 + (1-p)*b21 = p*b12 + (1-p)*b22
    b11, b12 = payoff_B[0]
    b21, b22 = payoff_B[1]
    denom = b11 - b12 - b21 + b22
    if abs(denom) < 1e-12:
        return None
    p1 = (b22 - b21) / denom
    return None if not (0.0 <= p1 <= 1.0) else np.array([p1, 1.0 - p1])

# verification_property:
#   Prisoner's Dilemma -> pure Nash (Defect, Defect): argmax(p)=argmax(q)=1
#   Matching Pennies (zero-sum) -> mixed Nash [0.5, 0.5]; fictitious play converges (Robinson 1951)
if __name__ == "__main__":
    pd_A = np.array([[3.0, 0.0], [5.0, 1.0]])  # action 1 = Defect (dominant)
    pd_B = np.array([[3.0, 5.0], [0.0, 1.0]])
    p, q = best_response_iter(pd_A, pd_B)
    assert np.argmax(p) == 1 and np.argmax(q) == 1, "PD -> (Defect, Defect)"
    mp_A = np.array([[1.0, -1.0], [-1.0, 1.0]])
    p2, q2 = best_response_iter(mp_A, -mp_A, n_iter=50000)
    assert abs(p2[0] - 0.5) < 0.02 and abs(q2[0] - 0.5) < 0.02, "Matching Pennies -> [0.5,0.5]"
```

**verification_property**: Prisoner's Dilemma 收敛到纯策略 Nash (Defect, Defect)（`argmax(p)=argmax(q)=1`，因为 Defect 严格占优）；Matching Pennies（零和博弈）fictitious play 经验频率收敛到混合 Nash `[0.5, 0.5]`（Robinson 1951 收敛保证，`|p[0]-0.5|<0.02`）。

## connection_to_unit

1. **学习范式 vs 均衡范式**：notes.md/starter.ipynb TODO1 的 BuyerAgent 用**贝叶斯共轭正态更新**估计公平价格（一种学习型模型），from-scratch 用 **fictitious play**（最佳响应迭代）求解 Nash 均衡（一种均衡分析模型）。两者刻画 Agent 作为经济主体的不同面：贝叶斯学习回答"Agent 如何在不确定中逐步形成价格信念"，Nash 均衡回答"理性 Agent 长期会收敛到什么策略"。mesa 仿真的 20 tick 涌现价格是学习轨迹的一个样本，Nash 均衡是该博弈的理论极限。
2. **策略交互的表征**：solution.ipynb 的 A2A 协商用**启发式规则**（70% exploit 选最低价 / 30% explore 随机）建模买方行为，from-scratch 把策略交互编码为**显式 payoff matrix** $A, B \in \mathbb{R}^{2\times2}$，策略={接受, 拒绝}×{高价, 低价}。payoff matrix 让"Agent 经济的激励结构"可逐元素审计，而启发式规则藏了激励假设。
3. **求解器对比**：solution.ipynb 的"价格发现"靠 mesa 的 20 tick 蒙特卡洛仿真涌现（结果依赖 random_seed），from-scratch 的 Nash 求解靠 fictitious play 迭代（对零和/2x2 博弈有 Robinson 1951 收敛保证）。前者是"跑仿真看涌现"，后者是"求均衡做预测"——前者回答"会发生什么"，后者回答"应该发生什么"。
4. **与 networkx 拓扑的互补**：notes.md TODO3 用 networkx PageRank 识别交易网络的**经济 hub Agent**（拓扑视角），from-scratch 的 Nash 均衡识别**稳定的策略组合**（博弈视角）。两者都揭示 Agent 经济结构：PageRank 找"谁是中心"，Nash 找"均衡在哪"，合起来才是完整的 Agent 经济图景。

## deep_dive_links

- [P16/21 Agent Economies - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/16-multi-agent-and-swarms/21-agent-economies/README.md) - Agent 经济（多 Agent 市场博弈与交易拓扑），本单元 from-scratch 的理论锚点
- [P9/07 Actor Critic A2C A3C - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/09-reinforcement-learning/07-actor-critic-a2c-a3c/README.md) - Actor-Critic 策略学习（与博弈论 best-response 迭代同属学习型决策框架）

## exercises

1. 在本单元 `starter.ipynb` TODO1（BuyerAgent 贝叶斯价格信念）运行后，构造一个 2x2 博弈：买方策略 {接受报价, 拒绝报价}，卖方策略 {报高价, 报低价}，根据 notes.md 真实参数（A2A 协议费 10%、推理成本 \$0.0025、预算 1000）填写 payoff matrix $A$（买方）和 $B$（卖方）。用上面的 `best_response_iter` 求解 Nash，对比 mesa 仿真 20 tick 后的涌现价格分布与 Nash 均衡策略，解释差异来源（提示：mesa 是贝叶斯学习轨迹，Nash 是均衡极限）。
2. 实现 n-player（>2）博弈的 fictitious play：把 `best_response_iter` 扩展为接收 payoff 张量列表 `payoffs = [P_1, ..., P_n]`（每个 $P_i$ 形状 $(|S_1|, ..., |S_n|)$），返回 n 个混合策略。观察当买方 Agent 数从 2 增到 5 时，Nash 均衡策略如何变化，这与 notes.md "20 买方 vs 5 卖方" 仿真场景的规模化效应同构。
3. Matching Pennies 收敛实验：令 `n_iter = 100, 1000, 10000, 100000`，记录 `|p2[0] - 0.5|` 随迭代次数的变化，验证 fictitious play 的 $O(1/\sqrt{t})$ 收敛速率（画 log-log 图应为斜率 -0.5 的直线）。这与 practice.md D-S1-BAYES 的"贝叶斯后验方差收敛"形成对照——两种学习模型的收敛速率比较。
4. TODO: 在 `practice.md` D-S1-BAYES drill 中，对比两种 Agent 学习模型在相同 payoff matrix 下的策略轨迹：① 贝叶斯共轭正态更新（price_belief 后验收敛）② fictitious play（经验频率收敛到 Nash）。用 1 段话解释"为什么 mesa 选贝叶斯而非 Nash"——提示：mesa 仿真 Agent 数有限且需在线学习，Nash 假设无限迭代与完全理性。
