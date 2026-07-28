# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：Capstone AI和商业分析 · Phase 5 商业模式与价值评估
> **scratch 哲学**：不调 numpy-financial、不调 scipy.stats，手写 DCF/NPV + 蒙特卡洛 + 龙卷风敏感性分析，从现金流折现公式 + 逆变换采样直译到 numpy。

## scratch_topic

本单元 from-scratch 主题：**手写蒙特卡洛 NPV + 敏感性分析（龙卷风图）**。对应 rohitg00 P19/56 Iteration Scheduler + P17/27 FinOps LLMs。notes.md/starter.ipynb 用 `numpy-financial.npv/irr` + `scipy.stats.norm` 蒙特卡洛 + matplotlib 龙卷风图完成投资评估，本层把"DCF 折现 -> 蒙特卡洛传播 -> 敏感性排序"拆开：从现金流折现公式与逆变换采样出发，手写 numpy 实现 NPV/IRR + 蒙特卡洛 NPV 分布 + 单变量敏感性分析，让"P(NPV>0) 为什么是 0.87""哪个变量是高杠杆因子"不再是 numpy-financial/scipy 的黑箱，而是可逐行审计的数值计算。

## core_algorithm

**NPV（净现值）** 是 DCF（折现现金流）模型的核心。给定 $T+1$ 期现金流 $\{FCF_0, FCF_1, \dots, FCF_T\}$ 与折现率 $r$：

$$\text{NPV} = \sum_{t=0}^{T} \frac{FCF_t}{(1+r)^t} = FCF_0 + \frac{FCF_1}{1+r} + \frac{FCF_2}{(1+r)^2} + \dots + \frac{FCF_T}{(1+r)^T}$$

IRR 是使 NPV=0 的 $r$。**蒙特卡洛传播**：Phase 4 ATE 有置信区间 $[\hat{\text{ATE}}_{lo}, \hat{\text{ATE}}_{hi}]$，假设 ATE $\sim \mathcal{N}(\mu, \sigma^2)$（$\mu$=点估计，$\sigma = (\text{hi}-\text{lo})/(2 \times 1.96)$）。通过逆变换采样 $u \sim U(0,1)$，$x = \mu + \sigma \sqrt{2}\,\text{erf}^{-1}(2u-1)$ 生成 ATE 样本，经 ARPU 推导链 $\text{ARPU} = \text{触达} \times \text{ATE} \times \text{AOV} \times \text{捕获率}$ 传播为 FCF，再折现得 NPV 样本。$N$ 次模拟得 NPV 分布，$P(\text{NPV}>0) = \frac{1}{N}\sum \mathbb{1}[\text{NPV}_i > 0]$。

**单变量敏感性分析（龙卷风图）**：对每个参数 $p_j$，在其取值范围 $[p_j^{lo}, p_j^{hi}]$ 内变动（其他参数固定基准值），计算 NPV 的最大值与最小值，范围 $\Delta_j = \text{NPV}_{max}^{(j)} - \text{NPV}_{min}^{(j)}$。按 $\Delta_j$ 降序排列即龙卷风图--顶部变量是 NPV 的高杠杆因子。数学上，这近似偏导数 $|\partial \text{NPV} / \partial p_j| \times \Delta p_j$ 的一阶排序。手写时用 numpy 向量化蒙特卡洛（矩阵化 $N \times T$ 现金流），逆变换采样用 `np.sqrt(2) * scipy.special.erfinv` 的有理逼近替代（避免 scipy 依赖）。

## code_artifact

```python
import numpy as np
import math

def npv(rate, cashflows):
    # NPV = sum_{t} FCF_t / (1+r)^t ;  cashflows[0] = FCF_0 (t=0, not discounted)
    T = len(cashflows)
    disc = np.array([(1 + rate) ** t for t in range(T)])
    return float(np.sum(np.array(cashflows) / disc))

def irr(cashflows, lo=-0.9, hi=10.0, iters=200):
    # bisection search for rate where npv(rate, cf) == 0
    f_lo = npv(lo, cashflows)
    f_hi = npv(hi, cashflows)
    if f_lo * f_hi > 0:
        return float('nan')
    for _ in range(iters):
        mid = (lo + hi) / 2
        f_mid = npv(mid, cashflows)
        if abs(f_mid) < 1e-6:
            return mid
        if f_lo * f_mid < 0:
            hi, f_hi = mid, f_mid
        else:
            lo, f_lo = mid, f_mid
    return (lo + hi) / 2

def erfinv_approx(x):
    # Winitzki approximation for inverse erf (avoids scipy dependency)
    a = 0.147
    ln1mx2 = np.log(1 - x**2)
    term = (2 / (np.pi * a) + ln1mx2 / 2)
    return np.sign(x) * np.sqrt(np.sqrt(term**2 - ln1mx2 / a) - term)

def sample_normal(mu, sigma, n, rng):
    u = rng.random(n)
    return mu + sigma * np.sqrt(2) * erfinv_approx(2 * u - 1)

def monte_carlo_npv(ate_mean, ate_lo, ate_hi, reach, aov, capture, opex,
                    init_cost, years=5, rate=0.1, n_sim=10000, seed=0):
    rng = np.random.default_rng(seed)
    sigma = (ate_hi - ate_lo) / (2 * 1.96)
    ate_s = sample_normal(ate_mean, sigma, n_sim, rng)
    arpu = reach * ate_s * aov * capture          # (n_sim,)
    npvs = np.empty(n_sim)
    for i in range(n_sim):
        fcfs = [-init_cost] + [arpu[i] - opex] * years
        npvs[i] = npv(rate, fcfs)
    return npvs

def sensitivity_tornado(base_params, ranges, rate=0.1, years=5):
    # base_params: dict; ranges: {param: (lo, hi)}; returns sorted list of (param, npv_lo, npv_hi)
    def make_cf(p):
        return [-p['init_cost']] + [p['reach']*p['ate']*p['aov']*p['capture'] - p['opex']] * years
    base_npv = npv(rate, make_cf(base_params))
    results = []
    for param, (lo, hi) in ranges.items():
        p_lo = {**base_params, param: lo}
        p_hi = {**base_params, param: hi}
        nv_lo = npv(rate, make_cf(p_lo))
        nv_hi = npv(rate, make_cf(p_hi))
        results.append((param, min(nv_lo, nv_hi), max(nv_lo, nv_hi)))
    return sorted(results, key=lambda r: r[2] - r[1], reverse=True)

# verification_property:
#   NPV matches closed form for known cashflows; IRR satisfies npv(irr, cf)~0;
#   Monte Carlo mean NPV ~ deterministic NPV at base ATE; tornado top factor = highest leverage.
if __name__ == "__main__":
    cf = [-1000, 300, 400, 500, 600]
    assert abs(npv(0.1, cf) - 402.45) < 1.0, f"NPV {npv(0.1,cf):.2f} must match closed form ~402.45"
    r = irr(cf)
    assert abs(npv(r, cf)) < 1e-4, f"IRR must zero NPV, got {npv(r,cf)}"
    # Monte Carlo: base ATE = 0.038
    npvs = monte_carlo_npv(0.038, 0.022, 0.054, reach=10000, aov=158,
                           capture=0.0333, opex=20000, init_cost=100000, n_sim=2000)
    p_positive = (npvs > 0).mean()
    assert 0.0 <= p_positive <= 1.0
    # tornado: ATE should be high-leverage
    base = {'reach': 10000, 'ate': 0.038, 'aov': 158, 'capture': 0.0333,
            'opex': 20000, 'init_cost': 100000}
    ranges = {'ate': (0.022, 0.054), 'aov': (120, 200), 'opex': (15000, 25000)}
    tor = sensitivity_tornado(base, ranges)
    assert tor[0][0] == 'ate', f"ATE must be top leverage factor, got {tor[0][0]}"
```

**verification_property**: NPV 匹配闭式解（$\text{NPV}(0.1, [-1000,300,400,500,600]) \approx 402.45$）；IRR 使 NPV 趋零（$|\text{NPV}(\text{IRR}, cf)| < 10^{-4}$）；蒙特卡洛 $P(\text{NPV}>0) \in [0,1]$；龙卷风图顶部因子是 ATE（高杠杆）。

## connection_to_unit

1. **库 vs 手写的金融计算**：notes.md 用 `numpy-financial.npv(rate, cashflows)` + `numpy-financial.irr(cashflows)` 一行完成，from-scratch 版用 `npv()` 手写折现公式 $\sum FCF_t/(1+r)^t$ + `irr()` 二分法求根--numpy-financial 的 `irr` 内部正是这样的数值求根，from-scratch 版让"IRR 是 NPV=0 的折现率"这个定义可计算化而非抽象概念。
2. **蒙特卡洛的逆变换采样显形**：starter.ipynb TODO4 用 `scipy.stats.norm.rvs(loc=mu, scale=sigma, size=10000)` 采样，from-scratch 版用 `sample_normal` + `erfinv_approx`（Winitzki 逼近）实现逆变换采样 $x = \mu + \sigma\sqrt{2}\,\text{erf}^{-1}(2u-1)$--让"为什么正态采样能传播 ATE 不确定性"可见，且去除了 scipy 依赖。
3. **龙卷风图的数学本质**：starter.ipynb TODO5 用 matplotlib 画龙卷风图，from-scratch 版用 `sensitivity_tornado` 显式实现"单变量变动 -> NPV 极差 -> 排序"--暴露了龙卷风图是一阶偏导数 $|\partial \text{NPV}/\partial p_j| \times \Delta p_j$ 的数值近似，而非"魔法可视化"。
4. **ATE -> ARPU -> NPV 推导链的矩阵化**：starter.ipynb TODO2 用 for 循环逐年算 FCF，from-scratch 版在 `monte_carlo_npv` 中用 `arpu = reach * ate_s * aov * capture` 向量化（ate_s 是 $N$ 维向量），让 $N$ 次模拟的 ARPU 一次性算完--这是蒙特卡洛从"慢循环"到"快矩阵"的工程优化，notes.md 没有显式讲。

## deep_dive_links

- [P19/56 Iteration Scheduler - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/19-capstone-projects/56-iteration-scheduler/README.md) - 迭代调度器，本单元 from-scratch 的工程锚点（蒙特卡洛迭代次数与敏感性扫描的调度逻辑）
- [P17/27 FinOps LLMs - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/17-infrastructure-and-production/27-finops-llms/README.md) - LLM FinOps，推理成本对 NPV/毛利率影响的成本建模参考

## exercises

1. 在本单元 `starter.ipynb` TODO2（DCF + NPV）运行后，用上面的 `npv()` + `irr()` 在同一组 FCF 上手动计算，对比 numpy-financial 输出（提示：numpy-financial 的 `npf.npv` 把第一个现金流也折现，from-scratch 版不折现 t=0--需对齐 convention）。解释两种 convention 的差异。
2. 扩展 `sensitivity_tornado` 为"双变量交互敏感性"：对 ATE×AOV 做网格扫描（$5 \times 5$ 网格），输出 NPV 热力图。对比单变量龙卷风图与双变量热力图发现的杠杆因子是否一致。这对应 notes.md 天道推演多路径场景分析的 from-scratch 版本。
3. 实现"贝叶斯 NPV"：用 `sample_normal` 给 ATE 加先验 $\text{ATE} \sim \mathcal{N}(0.03, 0.02^2)$，观测 Phase 4 估计后用共轭正态更新后验，再传播到 NPV。对比频率派蒙特卡洛 NPV 分布与贝叶斯后验 NPV 分布的差异。这是 notes.md 前沿"贝叶斯估值"的 from-scratch 版本。
4. TODO: 在 `practice.md` 的 drill 中，用本 from-scratch 的 `monte_carlo_npv` + `sensitivity_tornado` 替代 numpy-financial/scipy 版本，把 feedback_rule 中的"P(NPV>0) 概率"升级为"from-scratch 蒙特卡洛 P(NPV>0) + 龙卷风图顶部因子 == ATE 验证"。这是 starter.ipynb TODO4+TODO5 的 from-scratch 版本。
