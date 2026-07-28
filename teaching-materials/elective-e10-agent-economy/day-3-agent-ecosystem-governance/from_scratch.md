# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：选修E10 Agent经济 · Day 3 Agent生态治理
> **scratch 哲学**：不调 pydantic schema 声明 + mesa 涌现仿真，手写声誉衰减更新 + Shapley 值排列枚举，从合作博弈论四公理直译到 numpy。

## scratch_topic

本单元 from-scratch 主题：**手写生态治理的声誉评分衰减更新 + Shapley 值收益分配（排列枚举）**。对应 rohitg00 P16/14 Consensus and BFT（治理共识门限）+ P18/24 Regulatory Frameworks（监管框架）。notes.md/starter.ipynb 用 pydantic 声明 ReputationScoring/RevenueShare schema（字段配置）+ mesa 仿真涌现 Gini（治理效果），本层把治理的两个核心机制拆开：从 Shapley 值四公理与声誉衰减模型出发，手写 numpy 实现声誉更新 $R_{t+1}=\alpha R_t + (1-\alpha)\bar b$ + Shapley 值排列枚举分润，让"治理规则如何决定生态公平"从 mesa 仿真黑箱变成可逐行审计的机制设计计算。

## core_algorithm

**Shapley 值**（Shapley 1953）是合作博弈论的唯一公平分配方案，满足四条公理（对称性、载体性、可加性、效率）。给定联盟博弈 $(N, v)$（玩家集 $N$、联盟价值函数 $v: 2^N \to \mathbb{R}$），玩家 $i$ 的 Shapley 值：

$$\phi_i(v) = \sum_{S \subseteq N \setminus \{i\}} \frac{|S|!\,(|N|-|S|-1)!}{|N|!}\big[v(S \cup \{i\}) - v(S)\big]$$

直觉：玩家 $i$ 的公平份额 = 它加入所有可能联盟 $S$ 时的边际贡献 $v(S \cup \{i\}) - v(S)$ 的加权平均，权重 $\frac{|S|!(n-|S|-1)!}{n!}$ 是 $i$ 在随机排列中位于位置 $|S|+1$ 的概率。等价的**排列枚举形式**：

$$\phi_i(v) = \frac{1}{|N|!}\sum_{\pi \in \Pi(N)} \big[v(S_\pi(i) \cup \{i\}) - v(S_\pi(i))\big]$$

其中 $\Pi(N)$ 是所有 $n!$ 个排列，$S_\pi(i)$ 是排列 $\pi$ 中 $i$ 之前的玩家集。四公理唯一确定 $\phi$：对称性（同等边际贡献同等分配）、载体性（无贡献玩家 $\phi_i=0$）、可加性（$\phi_i(v+w)=\phi_i(v)+\phi_i(w)$）、效率（$\sum_i \phi_i = v(N)$）。Shapley 值用于 A2A 协作链分润--洞察->创意->投放->分析四 Agent 协作产出 $v(N)$，按 $\phi_i$ 分配比固定比例更公平，自动奖励"不可替代的 Agent"。

**声誉评分衰减模型**：Agent 信誉 $R_i^{(t)}$ 随时间衰减并按行为更新：

$$R_i^{(t+1)} = \alpha \cdot R_i^{(t)} + (1-\alpha)\cdot \bar{b}_i^{(t)}$$

其中 $\alpha \in [0,1]$ 是衰减/记忆率（$\alpha$ 大=长记忆，$\alpha$ 小=快遗忘），$\bar{b}_i^{(t)}$ 是 $t$ 期多维加权行为评分 $\bar{b} = w_1\cdot\text{成交率} + w_2\cdot(1-\text{欺诈率}) + w_3\cdot\text{用户评分}$，$\sum w_k=1$。行为恒定时稳态 $R^* = \bar{b}$（解 $R=\alpha R+(1-\alpha)\bar b$）。声誉低于准入门槛 $\tau$ 的 Agent 被驱逐--这是 BFT 门限思想在生态治理的落地：超过 $f$ 个低声誉节点触发治理干预（类比 BFT 共识的 $n \geq 3f+1$ 容错门限）。$\alpha$ 是治理哲学旋钮：高 $\alpha$（长记忆）让欺诈者长期被拒，低 $\alpha$（快遗忘）允许改过自新。

## code_artifact

```python
import numpy as np
import math
from itertools import permutations

def reputation_update(R_prev, behavior_scores, weights, alpha=0.7):
    # R_{t+1} = alpha*R_t + (1-alpha)*weighted_behavior ; weights sum to 1
    b_bar = float(np.dot(np.array(weights), np.array(behavior_scores)))
    return alpha * R_prev + (1 - alpha) * b_bar

def shapley_value(value_func, players):
    # phi_i = (1/n!) * sum over permutations of marginal contribution
    n = len(players)
    phi = {p: 0.0 for p in players}
    for perm in permutations(players):
        S = ()
        for p in perm:
            v_with = value_func(frozenset(S + (p,)))
            v_without = value_func(frozenset(S))
            phi[p] += (v_with - v_without)
            S = S + (p,)
    for p in players:
        phi[p] /= math.factorial(n)
    return phi

# verification_property:
#   Shapley symmetry: equal-contribution players get equal share
#   Shapley efficiency: sum(phi) = v(N) = 12
#   reputation decay: steady state R* = b_bar when behavior constant
if __name__ == "__main__":
    def v(S):
        table = {frozenset(): 0.0, frozenset({"A"}): 0.0, frozenset({"B"}): 0.0,
                 frozenset({"C"}): 0.0, frozenset({"A", "B"}): 10.0,
                 frozenset({"A", "C"}): 10.0, frozenset({"B", "C"}): 10.0,
                 frozenset({"A", "B", "C"}): 12.0}
        return table[S]
    phi = shapley_value(v, ["A", "B", "C"])
    assert abs(phi["A"] - phi["B"]) < 1e-9 and abs(phi["B"] - phi["C"]) < 1e-9, "symmetry: A=B=C"
    assert abs(sum(phi.values()) - 12.0) < 1e-9, "efficiency: sum(phi)=v(N)=12"
    R = 50.0
    for _ in range(200):
        R = reputation_update(R, [0.8, 0.95, 0.9], [0.4, 0.3, 0.3], alpha=0.7)
    b_bar = 0.4 * 0.8 + 0.3 * 0.95 + 0.3 * 0.9
    assert abs(R - b_bar) < 1e-6, f"steady state R*=b_bar={b_bar}, got {R}"
```

**verification_property**: Shapley 对称性（同等贡献玩家同等份额：对称 3 人博弈 $\phi_A=\phi_B=\phi_C=4.0$）；Shapley 效率（$\sum\phi_i = v(N) = 12.0$）；声誉衰减稳态（行为恒定时 $R \xrightarrow{a.s.} \bar{b}$，$\alpha=0.7$ 下 200 步收敛到 $\bar{b}=0.875$）。

## connection_to_unit

1. **schema 字段 vs 动力学实现**：notes.md TODO1 的 pydantic `ReputationScoring` schema 把 `initial_score/decay_rate/weight` 当配置字段声明并验证类型，from-scratch 的 `reputation_update` 实现了这些字段的**实际动力学**：衰减+加权更新公式 $R_{t+1}=\alpha R_t + (1-\alpha)\bar b$。schema 验证字段合法性，from-scratch 实现字段演化语义--`decay_rate` 不是标签，而是 $\alpha$ 进入递推的参数。
2. **固定比例分润 vs 边际贡献分润**：notes.md TODO1 的 `RevenueShare` schema 用固定 `platform_share/developer_share` 比例分润（如 GPT Store 30% vs MCP 0%），from-scratch 的 Shapley 值按**边际贡献** $v(S\cup\{i\})-v(S)$ 分润。固定比例是粗糙的（不区分 Agent 实际贡献），Shapley 是公平的（满足对称性/载体性/效率公理，自动奖励不可替代者）。mesa 仿真涌现的 Gini 差异部分来自分润规则的选择。
3. **mesa 涌现仿真 vs 机制设计**：notes.md TODO4 的 mesa 仿真用 `PlatformAgent` 执行治理规则（准入/惩罚/信誉更新），观察 30 agents/15 ticks 的 Gini 涌现，from-scratch 把"信誉更新"和"分润"两个机制单独拆出用 numpy 实现并验证公理。mesa 是"跑仿真看涌现"（依赖 random_seed），from-scratch 是"求公理解做预测"（Shapley 满足公理、声誉有稳态闭式）。
4. **networkx 拓扑重要性 vs Shapley 博弈重要性**：notes.md TODO3 的 networkx 中心性（degree/betweenness/closeness）从**拓扑结构**识别生态 hub，from-scratch 的 Shapley 值从**合作博弈**识别"边际贡献最大"的 Agent。两者都找"谁重要"但角度不同：networkx 找结构 hub，Shapley 找不可替代者。一个 Agent 可能 betweenness 低但 Shapley 高（若它是某协作链的关键补足者），合起来才是完整的生态重要性图景。

## deep_dive_links

- [P16/14 Consensus and BFT - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/16-multi-agent-and-swarms/14-consensus-and-bft/README.md) - 共识与 BFT（治理门限/投票容错），声誉准入门限 $\tau$ 与 BFT $3f+1$ 门限同构
- [P18/24 Regulatory Frameworks EU US UK Korea - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/18-ethics-safety-alignment/24-regulatory-frameworks-eu-us-uk-korea/README.md) - 监管框架（责任归属/反垄断/消费者保护），生态治理的合规视角

## exercises

1. 在本单元 `starter.ipynb` TODO1（pydantic 四种治理规则 schema）运行后，用 `reputation_update` 替代 TODO4 mesa 仿真中 `PlatformAgent` 的信誉更新逻辑。对比 from-scratch 衰减模型与 solution.ipynb 默认信誉更新在 15 ticks 下的 Gini 演化差异。提示：notes.md `ReputationScoring.decay_rate` 对应 from-scratch 的 $\alpha$，`weight` 对应多维行为权重 $w_k$。
2. Shapley 分润实验：构造 A2A 营销协作链（洞察 Agent A / 创意 Agent B / 投放 Agent C / 分析 Agent D），定义 value_func（如 $v(\{A,B,C,D\})=100$、$v(\{A,B,C\})=70$、$v(\{A,C,D\})=65$、单 Agent $v=0$），用 `shapley_value` 计算每个 Agent 的公平份额 $\phi_i$，对比 notes.md 的固定比例分润（`platform_share=0.25` 剩余按等分）。找出"Shapley 分润 $\neq$ 固定分润"的 Agent（边际贡献与固定比例不匹配者），这就是 notes.md 激励设计"激励兼容"原则要解决的错配。
3. Shapley 公理验证：在 exercise 2 的博弈中加入一个"零玩家" Agent E（对所有 $S$，$v(S\cup\{E\})=v(S)$），验证 `phi["E"]=0`（载体性公理）。再验证 $\sum_i \phi_i = v(N)$（效率公理）。最后验证对称性：若 Agent B 和 C 在所有联盟中边际贡献相同，则 $\phi_B=\phi_C$。这三条公理是 Shapley 值作为"唯一公平分配"的数学根基。
4. TODO: 在 `practice.md` D4（天道推演×生态治理）的天道推演沙盘中，用 from-scratch 的声誉衰减模型推演"宽准入"生态的信誉分布演化：低 $\alpha=0.3$（快遗忘）vs 高 $\alpha=0.9$（长记忆）下，一个欺诈 Agent（行为评分 0.2）的信誉恢复到准入门槛 $\tau=0.6$ 所需 tick 数差异。标注推演假设（行为恒定）与盲点（Agent 可能策略性调整行为），这是治理哲学选择--长记忆惩戒 vs 快遗忘容错。
