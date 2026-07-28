# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：技能3 因果推断 · Day 2 实验设计与 A/B 测试统计
> **scratch 哲学**：不调 scipy.stats，手写 Welch t 检验 + Thompson sampling bandit，从 t 统计量与 Beta 后验直译到 numpy。

## scratch_topic

本单元 from-scratch 主题：**手写 Welch t 检验 + Thompson sampling 多臂老虎机**。对应 rohitg00 P2 Model Evaluation（假设检验与评估）+ P9 Q Learning SARSA（bandit 探索-利用）。notes.md/starter.ipynb 用 `scipy.stats.ttest_ind(..., equal_var=False)` 一行完成 A/B 显著性检验，用 `statsmodels` 算样本量/功效；本层把"不假定等方差的两样本检验"拆成均值差、合并方差、Welch-Satterthwaite 自由度三步手写，再把 TODO3 概念里的自适应实验写成 Beta 后验采样循环，让"p<0.05"和"探索-利用权衡"在白板级代码中显形。

## core_algorithm

Welch t 检验是 A/B 测试默认的显著性检验引擎，它放宽了 Student t 的等方差假设。给定两组独立样本，容量 $n_1, n_0$，样本均值 $\bar Y_1, \bar Y_0$，样本方差 $s_1^2, s_0^2$，检验统计量为

$$t = \frac{\bar Y_1 - \bar Y_0}{\sqrt{s_1^2/n_1 + s_0^2/n_0}}$$

其自由度由 Welch-Satterthwaite 近似给出

$$\nu = \frac{\left(s_1^2/n_1 + s_0^2/n_0\right)^2}{\left(s_1^2/n_1\right)^2/(n_1-1) + \left(s_0^2/n_0\right)^2/(n_0-1)}$$

当 $|t|$ 超过临界值（大样本下 $\approx 1.96$，双侧 $\alpha=0.05$）则拒绝 $H_0$，组间存在差异。这正是 starter.ipynb TODO4 `scipy.stats.ttest_ind(equal_var=False)` 的内核：朴素均值差除以"不等方差版"标准误。大样本下 $t$ 近似标准正态，p 值可由 $\text{erf}$ 闭式给出。

Thompson Sampling 解决 A/B 的"实验成本"痛点：固定 A/B 在实验期把一半流量分给较差版本，而 bandit 自适应地把流量倾向更优版本。对 $K$ 个 Bernoulli 臂，每臂维护共轭先验 $\text{Beta}(\alpha_k, \beta_k)$（初始 $\alpha=\beta=1$）。每轮采样 $\theta_k \sim \text{Beta}(\alpha_k, \beta_k)$，拉 $\arg\max_k \theta_k$，观察奖励 $r\in\{0,1\}$，更新 $\alpha_k \mathrel{+}= r,\ \beta_k \mathrel{+}= 1-r$。后验均值 $\alpha_k/(\alpha_k+\beta_k)$ 收敛到真实转化率，而后验方差驱动探索——不确定的臂偶尔采到高值而被再探。Thompson sampling 的累计遗憾为 $O(\sqrt{KT\log T})$，近最优，是 TODO3 自适应实验与 Day 5 MAB 的数学根基。

## code_artifact

```python
import numpy as np
import math

def welch_t_test(y1, y0):
    # Welch t (unequal var): t=(m1-m0)/sqrt(v1/n1+v0/n0), Welch-Satterthwaite df
    n1, n0 = len(y1), len(y0)
    m1, m0 = float(y1.mean()), float(y0.mean())
    v1, v0 = float(y1.var(ddof=1)), float(y0.var(ddof=1))
    se = math.sqrt(v1 / n1 + v0 / n0)
    t = (m1 - m0) / se
    df = (v1 / n1 + v0 / n0) ** 2 / ((v1 / n1) ** 2 / (n1 - 1) + (v0 / n0) ** 2 / (n0 - 1))
    p = 2 * (1 - 0.5 * (1 + math.erf(abs(t) / math.sqrt(2))))  # normal approx, large n
    return t, df, p

def thompson_bandit(true_rates, n_steps=2000, seed=0):
    # Beta(1,1) prior per arm; sample theta, pull argmax, observe Bernoulli, update
    rng = np.random.default_rng(seed)
    k = len(true_rates)
    a = np.ones(k); b = np.ones(k)
    counts = np.zeros(k, dtype=int)
    for _ in range(n_steps):
        theta = rng.beta(a, b)
        arm = int(np.argmax(theta))
        r = 1 if rng.random() < true_rates[arm] else 0
        a[arm] += r; b[arm] += 1 - r
        counts[arm] += 1
    return counts, a, b

# verification_property:
#   |t|>1.96 recovers significance for a true effect; Thompson allocates most pulls to best arm.
if __name__ == "__main__":
    rng = np.random.default_rng(0)
    y1 = 0.5 + rng.standard_normal(500)
    y0 = rng.standard_normal(500)
    t, df, p = welch_t_test(y1, y0)
    assert t > 1.96, f"t={t:.2f} must be significant for effect=0.5, n=500"
    counts, a, b = thompson_bandit([0.2, 0.5, 0.4])
    assert counts.argmax() == 1, "Thompson must converge to best arm (idx 1, rate 0.5)"
    assert counts[1] > 1000, "best arm should attract most of 2000 pulls"
```

**verification_property**: Welch t 在真实效应 0.5、n=500 下 $|t|>1.96$（显著）；Thompson bandit 在 3 臂（0.2/0.5/0.4）2000 步后把绝大多数拉臂分配给真实率最高的臂 idx=1，验证后验采样收敛。

## connection_to_unit

1. **库 vs 手写的颗粒度**：starter.ipynb TODO4 用 `scipy.stats.ttest_ind(equal_var=False)` 一行返回 t/p/df，from-scratch 版把"不等方差"这步拆成 $s_1^2/n_1 + s_0^2/n_0$ 的逐项加权与 Welch-Satterthwaite 自由度修正——让"为什么 A/B 不该用等方差 t 检验"在数值上可见，而非被 scipy 的 `equal_var` 参数遮蔽。
2. **TODO2 均衡性 vs TODO4 效应检验共享同一引擎**：TODO2 对每个协变量（age/education/re75）做 t 检验验证随机化均衡，TODO4 对结果 re78 做 t 检验验证处理效应——from-scratch 版是同一个 `welch_t_test` 函数，只是喂入不同的 Y，让"均衡检验与效应检验是同一数学对象、不同因果问题"这一洞察显形。
3. **TODO6 CUPED vs bandit 的对偶**：TODO6 用 CUPED 缩减方差（固定 A/B，缩小标准误分母），Thompson bandit 用自适应分配缩减实验成本（动态重分配流量）；from-scratch 同时给出两条路，让 notes.md"关键回顾4 CUPED"与 Day 5"关键回顾1 MAB"在代码层对账——两者都降低 A/B 成本，但一个改方差、一个改分配。
4. **p 值的数值透明**：scipy 返回的 p 是 t 分布 CDF 数值积分，from-scratch 版用 $\text{erf}$ 给出大样本正态近似 p——在 n=500 时与 scipy 差异 <0.01，但让"p 值是 tail probability 的积分"这层从黑箱变成可读公式，呼应 notes.md"关键回顾3 不被 p<0.05 绑架"的警示。

## deep_dive_links

- [P2/09 Model Evaluation - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/09-model-evaluation/README.md) - 模型评估与假设检验：A/B 测试显著性检验的理论锚点，相关 vs 因果边界
- [P9/04 Q Learning SARSA - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/09-reinforcement-learning/04-q-learning-sarsa/README.md) - 强化学习 bandit 基础：Thompson sampling 探索-利用权衡的 RL 渊源

## exercises

1. 在本单元 `starter.ipynb` TODO4 运行 scipy t 检验后，用上面的 `welch_t_test` 在同一份 NSW `re78` 数据上手动算 t/df/p，验证 t 与 scipy 差异 <0.01，并解释为什么 df 是非整数（Welch-Satterthwaite 加权）。提示：scipy 默认 `equal_var=True` 是 Student t，需传 `equal_var=False` 才对应本实现。
2. 在 `practice.md` D2（样本量与功效）的"事后功效"阶段，用 `welch_t_test` 反向构造：给定 n=5000、真实效应 1%，模拟 1000 次数据集算"拒绝 H0"的比例（即经验功效），对比 statsmodels `TTestIndPower.power` 的解析值，理解功效 = $P(\text{拒绝}|\text{H1为真})$。
3. 把 TODO6（CUPED）与 `thompson_bandit` 接到同一份 NSW 响应率上：先用 re75 手写 CUPED 调整 re78（`beta=Cov(Y,X)/Var(X)`，`theta=Y-beta*(X-Xbar)`），再用 `welch_t_test` 对 theta 检验；然后用 NSW 按子群的 `re78>0` 比例作 3 臂真实率跑 bandit，量化"自适应 vs 固定 A/B"的累计转化增益。两条 from-scratch 路径都指向"降低实验成本"。
4. TODO: 为 `thompson_bandit` 添加"regret 曲线"输出（每步累计奖励与最优臂累计奖励之差），在 3 臂场景下绘制 regret 随步数增长（应近似 $\sqrt{T}$），这是 Day 5 TODO3 MAB 的 from-scratch 预备。
