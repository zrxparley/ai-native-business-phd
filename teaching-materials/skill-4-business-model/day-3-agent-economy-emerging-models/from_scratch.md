# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：技能4 AI驱动商业模式创新 · Day 3 Agent经济 + 新兴商业模式
> **scratch 哲学**：不调 mesa/pandas/matplotlib，手写 ABM 双边市场仿真 + Gini 系数，从 Agent 交易因果链直译到 numpy 数组。

## scratch_topic

本单元 from-scratch 主题：**手写多 Agent 双边市场仿真（ABM）+ Gini 系数涌现追踪**。对应 rohitg00 P16 Agent Economies（Agent 经济）+ P9 Actor-Critic（Agent 决策）。notes.md/starter.ipynb 用 `mesa.Model/Agent/DataCollector` 构建消费者/商家/AI中介三类 Agent 的 ABM 仿真，本层把 mesa 的 OOP 框架全部去库化：纯 numpy 数组表示 Agent 财富/价格状态，手写交易循环 + Gini 系数计算，让"Agent 经济如何涌现财富不平等""推理成本如何约束 AI 中介存活"两个问题在白板级代码中显形。

## core_algorithm

Agent 经济仿真的核心是**多主体交易 + 宏观指标涌现**。每个 step 中，消费者 $c$ 通过中介 $i$ 向商家 $m$ 购买，财富转移为：

$$\Delta W_c = -(P + f), \quad \Delta W_m = P(1 - \gamma), \quad \Delta W_i = f - c_{\text{reason}}$$

其中 $P$ 为商品价格，$f$ 为中介费，$\gamma$ 为平台抽成率（30%），$c_{\text{reason}} = \frac{\text{tokens}}{10^6} \times \text{price}_{\text{token}}$ 为每次匹配的推理成本。推理成本是 AI 中介与传统中介的本质区别--传统中介边际成本趋于零，AI 中介每次匹配都消耗 token。

Gini 系数量化财富不平等的涌现。给定排序后的财富 $x_{(1)} \le x_{(2)} \le \cdots \le x_{(n)}$：

$$G = \frac{2\sum_{i=1}^{n} i \cdot x_{(i)}}{n \sum_{i=1}^{n} x_{(i)}} - \frac{n+1}{n}$$

$G = 0$ 表示完全平等（所有 Agent 财富相同），$G \to 1$ 表示最大不平等（一个 Agent 持有全部财富）。在 $[0, 0, 0, 100]$ 上 $G = 0.75$，在 $[10, 10, 10, 10]$ 上 $G = 0$。

市场仿真的动态定价规则：商家库存高时降价（$P \leftarrow P \times 0.99$），库存低时涨价--这是 notes.md 商家 Agent `_adjust_price` 的 from-scratch 简化版。消费者预算 $< 1$ 时破产退出，模拟 notes.md 的破产机制。推理成本 $c_{\text{reason}}$ 作为 AI 中介的硬约束：若 $f < c_{\text{reason}}$，中介每笔交易亏损，最终破产--这是 Day 3 "推理成本是 Agent 经济核心约束"的数学表达。

## code_artifact

```python
import numpy as np

def gini(wealth):
    # G = 2*sum(i*x_i)/(n*sum(x)) - (n+1)/n, x sorted ascending
    n = len(wealth)
    if n == 0: return 0.0
    s = np.sort(wealth); total = s.sum()
    if total == 0: return 0.0
    return 2*np.sum(np.arange(1, n+1)*s)/(n*total) - (n+1)/n

def simulate_market(n_c=50, n_m=10, n_i=3, steps=100, comm=0.30, rcost=0.0025, seed=0):
    rng = np.random.default_rng(seed)
    cw = np.full(n_c, 1000.0); mw = np.full(n_m, 500.0)
    mp = np.full(n_m, 20.0); iw = np.full(n_i, 200.0); gh = []
    for _ in range(steps):
        for ci in np.where(cw >= 1.0)[0]:
            am = np.where(mw >= 1.0)[0]
            if len(am) == 0: break
            mi = rng.choice(am); price = mp[mi]
            ii = rng.integers(n_i) if n_i > 0 else -1
            fee = price * 0.05 if ii >= 0 else 0.0
            if cw[ci] >= price + fee:
                cw[ci] -= price + fee
                mw[mi] += price * (1 - comm)
                if ii >= 0: iw[ii] += fee - rcost
                mp[mi] = max(10.0, mp[mi] * 0.99)
        gh.append(gini(np.concatenate([cw, mw, iw])))
    return np.array(gh), cw, mw, iw

# verification_property:
#   gini(equal wealth)=0; gini([0,0,0,100])~0.75;
#   simulation gini increases (wealth concentration)
if __name__ == "__main__":
    assert abs(gini(np.array([10,10,10,10.]))) < 1e-6
    g = gini(np.array([0,0,0,100.])); assert 0.6 < g < 0.9
    gh, _, _, _ = simulate_market(steps=50, seed=0)
    assert len(gh) == 50 and gh[-1] >= gh[0]
```

**verification_property**: Gini 系数在完全平等时为 0（`gini([10,10,10,10]) ≈ 0`）；在 $[0,0,0,100]$ 上为 0.75（`0.6 < g < 0.9`）；市场仿真中 Gini 随时间递增（`gh[-1] >= gh[0]`，财富向商家/中介集中，消费者破产导致不平等加剧）。

## connection_to_unit

1. **mesa OOP vs numpy 数组**：starter.ipynb TODO1-3 用 `class ConsumerAgent(mesa.Agent)` / `class MerchantAgent` / `class AIIntermediaryAgent` 三个 OOP 类，from-scratch 版用三个 numpy 数组 `cw/mw/iw` 表示财富 + `mp` 表示价格--把"Agent = 有状态的对象"简化为"Agent = 数组中的一个元素"，让仿真的数据流在数组操作中完全可见，不被 mesa 的 Agent 抽象遮蔽。
2. **DataCollector vs 手写 Gini 追踪**：starter.ipynb TODO4 用 `DataCollector(model_reporters={'gini': compute_gini})` 自动收集指标，from-scratch 版在每个 step 末尾手动 `gini(np.concatenate([cw, mw, iw]))` 追加到 `gh` 列表--让"Gini 系数怎么算的"不被 mesa 的 collector 抽象隐藏，能逐行审计公式。
3. **推理成本约束的显形**：notes.md 关键回顾 4 讲"推理成本是 Agent 经济的核心约束"，from-scratch 版在 `iw[ii] += fee - rcost` 这一行直接体现--若 `rcost > fee`，中介财富递减最终破产。mesa 版的 `AIIntermediaryAgent.process_transaction` 把这个逻辑封装在方法内，from-scratch 版让"fee - reasoning_cost"这个净值在代码中裸露。
4. **A2A 交易的简化**：notes.md 提到"AI 中介间以 15% 概率进行 A2A 信息交换"，from-scratch 版暂未实现 A2A（聚焦双边市场核心），但 `simulate_market` 的数组结构天然支持扩展--增加 `a2a_matrix` 参数即可在中介间转移信息/财富，这是练习 3 的内容。

## deep_dive_links

- [P16/21 Agent Economies - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/16-multi-agent-and-swarms/21-agent-economies/README.md) - Agent 经济：多 Agent 市场交易、涌现行为、经济指标追踪，本单元 from-scratch ABM 仿真的理论锚点
- [P9/07 Actor Critic A2C A3C - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/09-reinforcement-learning/07-actor-critic-a2c-a3c/README.md) - Actor-Critic：Agent 决策的强化学习基础，Agent 经济中 Agent 定价/购买策略可建模为 RL 策略

## exercises

1. 在本单元 `starter.ipynb` TODO1-4（mesa 三类 Agent + Model）运行后，用上面的 `simulate_market` 在相同参数（50 消费者/10 商家/3 中介/100 步）下运行，对比 mesa 版与 from-scratch 版的 Gini 系数时间序列（应趋势一致：均递增），解释差异来源（提示：mesa 版有动态定价/补货/库存逻辑，from-scratch 版简化了定价）。
2. 修改 `rcost` 参数从 GPT-4o 的 $0.0025（500 tokens × $5/1M）改为 DeepSeek V3 的 $0.000135（500 tokens × $0.27/1M），重新运行 `simulate_market`，观察 AI 中介存活率和 Gini 系数的变化--对应 notes.md "推理成本下降5-10倍时 Agent 经济可行性发生质变"。
3. 为 `simulate_market` 添加 A2A 交易逻辑：每 step 以 15% 概率在中介间转移 `a2a_amount` 财富（信息交换付费），对应 notes.md "AI中介间以15%概率进行A2A信息交换"。观察 A2A 交易对中介财富分布和 Gini 的影响。
4. TODO: 在 `practice.md` 的 D1 drill（Agent 经济建模）中，用 from-scratch `simulate_market` 替代 mesa 仿真，输出 Gini 时间序列 + 存活 Agent 数曲线。这是 starter.ipynb TODO5/TODO6 的 from-scratch 版本，让仿真不依赖 mesa 也能运行。
