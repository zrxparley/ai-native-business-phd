# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：技能4 AI驱动商业模式创新 · Day 5 商业模式画布 + 投资评估（收官）
> **scratch 哲学**：不调 numpy-financial/scipy.stats/pandas，手写 NPV 贴现 + 蒙特卡洛仿真 + Bull/Base/Bear 三路径，从 DCF + 采样公式直译到 numpy。

## scratch_topic

本单元 from-scratch 主题：**手写蒙特卡洛 NPV 估值 + Bull/Base/Bear 三路径场景分析**。对应 rohitg00 P1 Sampling Methods（采样方法/蒙特卡洛）+ P17 FinOps LLMs（推理成本对估值的影响）。notes.md/starter.ipynb 用 `numpy_financial.npv/irr` 算 NPV/IRR + `scipy.stats` 做蒙特卡洛 10000 次抽样 + `matplotlib` 画龙卷风图，本层把金融计算和随机采样全部去库化：纯 numpy 手写 DCF 贴现 + 向量化蒙特卡洛 + 三场景概率对比，让"P(NPV>0) 怎么算的""Bull/Base/Bear 三路径如何排序"两个问题在白板级代码中显形。

## core_algorithm

蒙特卡洛估值的核心是**用随机采样把点估计变成概率分布**。AI 产品的 NPV 取决于收入增长率 $g$ 和毛利率 $m$，两者均有不确定性。对第 $i$ 次仿真：

$$\text{NPV}_i = -I + \sum_{t=1}^{T} \frac{R_0 (1+g_i)^t \cdot m_i}{(1+r)^t}$$

其中 $g_i \sim \mathcal{N}(\mu_g, \sigma_g^2)$（增长率加噪）、$m_i \sim \mathcal{N}(\mu_m, \sigma_m^2)$（毛利率加噪），$R_0$ 为初始收入，$I$ 为初始投资，$r$ 为折现率。向量化实现：对 $N$ 次仿真采样 $g, m$ 向量，用广播计算 $(N \times T)$ 的收入矩阵 $\text{revs}_{i,t} = R_0 (1+g_i)^t$，再贴现求和。

NPV 为正的概率（投资可行性指标）：

$$P(\text{NPV} > 0) = \frac{1}{N} \sum_{i=1}^{N} \mathbf{1}[\text{NPV}_i > 0]$$

Bull/Base/Bear 三路径场景分析对应天道推演的三沙盘分支：

$$\theta_{\text{bull}} = (1.3 R_0, \ \mu_g+0.1, \ \mu_m+0.05), \quad \theta_{\text{base}} = (R_0, \mu_g, \mu_m), \quad \theta_{\text{bear}} = (0.7 R_0, \ \mu_g-0.1, \ \mu_m-0.05)$$

Bull 场景的收入、增长率、毛利率均高于 Base，Bear 均低于 Base。由于 NPV 对 $g$ 和 $m$ 单调递增（更高的增长/毛利 $\to$ 更高的现金流 $\to$ 更高的 NPV），三路径的 $P(\text{NPV}>0)$ 满足 $P_{\text{bull}} \geq P_{\text{base}} \geq P_{\text{bear}}$。这是 notes.md "天道推演三路径推演" 的 from-scratch 数学骨架--蒙特卡洛评估"参数不确定性"，三路径评估"场景路径优不优"。

## code_artifact

```python
import numpy as np

def npv(rate, cashflows):
    t = np.arange(len(cashflows))
    return np.sum(np.array(cashflows, dtype=float) / (1 + rate) ** t)

def monte_carlo_npv(init_rev, growth, margin, invest, rate, n_years=5, n_sim=10000, seed=0):
    rng = np.random.default_rng(seed)
    g = np.clip(growth + rng.normal(0, 0.05, n_sim), -0.1, 0.5)
    m = np.clip(margin + rng.normal(0, 0.03, n_sim), 0.3, 0.9)
    t = np.arange(1, n_years + 1)
    revs = init_rev * (1 + g[:, None]) ** t[None, :]
    disc = revs * m[:, None] / (1 + rate) ** t[None, :]
    return -invest + disc.sum(axis=1)

def bull_base_bear(init_rev, growth, margin, invest, rate, n_years=5, n_sim=5000, seed=0):
    scenarios = {
        'bull': (init_rev*1.3, growth+0.1, margin+0.05),
        'base': (init_rev, growth, margin),
        'bear': (init_rev*0.7, growth-0.1, margin-0.05),
    }
    results = {}
    for name, (rev, grw, mar) in scenarios.items():
        npvs = monte_carlo_npv(rev, grw, mar, invest, rate, n_years, n_sim, seed)
        results[name] = (npvs.mean(), np.mean(npvs > 0))
    return results

# verification_property:
#   NPV matches closed-form DCF; P(NPV>0) in [0,1];
#   bull scenario P(NPV>0) >= base >= bear
if __name__ == "__main__":
    val = npv(0.1, [-100, 50, 60, 70])
    expected = -100 + 50/1.1 + 60/1.21 + 70/1.331
    assert abs(val - expected) < 1e-6
    npvs = monte_carlo_npv(600, 0.15, 0.5, 2000, 0.15, n_sim=10000, seed=0)
    p = np.mean(npvs > 0)
    assert 0 <= p <= 1, f"P(NPV>0)={p}"
    res = bull_base_bear(600, 0.15, 0.5, 2000, 0.15, seed=0)
    assert res['bull'][1] >= res['base'][1] >= res['bear'][1], f"bull>=base>=bear: {res}"
```

**verification_property**: `npv` 与闭式 DCF 公式数值一致（`|npv(r,cf) - expected| < 1e-6`）；蒙特卡洛 $P(\text{NPV}>0) \in [0, 1]$；Bull 场景的 $P(\text{NPV}>0)$ $\geq$ Base $\geq$ Bear（NPV 对 $g, m$ 单调递增，高增长/高毛利场景的可行性概率更高）。

## connection_to_unit

1. **numpy-financial vs 手写 DCF**：starter.ipynb TODO2 用 `npf.npv(rate, fcf)` 一行算 NPV，from-scratch 版用 `np.sum(cf / (1+r)**t)` 手写贴现--让"NPV = 未来现金流按 $(1+r)^t$ 贴现求和"这个定义不被库函数遮蔽。notes.md 的 DCF 模型（初始投资 $2000K、5 年、折现率 15%）可直接用 `npv(0.15, fcf)` 计算。
2. **scipy.stats 蒙特卡洛 vs 手写向量化采样**：starter.ipynb TODO4 用 `scipy.stats` 分布做 10000 次蒙特卡洛抽样，from-scratch 版用 `rng.normal(0, 0.05, n_sim)` 采样 + numpy 广播一次性计算 $(10000 \times 5)$ 的收入矩阵--让"蒙特卡洛 = 采样参数 -> 算 NPV -> 统计分布"这个流程在向量化代码中可见，不被 scipy.stats 的分布对象抽象遮蔽。
3. **P(NPV>0) 的计算**：notes.md 的核心交付物是"P(NPV>0)=55.7%"，from-scratch 版用 `np.mean(npvs > 0)` 一行直译这个概率--让"P(NPV>0) = NPV 为正的仿真次数 / 总仿真次数"这个频率派定义在代码中显形。
4. **Bull/Base/Bear vs 天道推演三沙盘**：notes.md TODO6 用天道推演做 Bull/Base/Bear 三路径，from-scratch 版的 `bull_base_bear` 函数把三场景参数化（收入 $\times 1.3/1.0/0.7$、增长率 $\pm 0.1$、毛利率 $\pm 0.05$）--对应天道推演的"沙盘模拟（3 层推演）"能力，让三路径的参数差异在函数签名中显形，而非埋在天道推演框架的叙事中。

## deep_dive_links

- [P1/16 Sampling Methods - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/16-sampling-methods/README.md) - 采样方法：蒙特卡洛采样的数学基础（逆变换/重要性采样/方差缩减），本单元 from-scratch 蒙特卡洛 NPV 的理论锚点
- [P17/27 FinOps LLMs - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/17-infrastructure-and-production/27-finops-llms/README.md) - LLM FinOps：推理成本作为 AI 产品持续负现金流影响 NPV 估值，是 AI 估值与传统 SaaS 估值的本质差异

## exercises

1. 在本单元 `starter.ipynb` TODO4（scipy.stats 蒙特卡洛）运行后，用上面的 `monte_carlo_npv` 在 MarketingAgent Pro 的参数（初始投资 $2000K、ARPU $24K/年、毛利率 65%、折现率 15%）上跑 10000 次仿真，对比 scipy.stats 版与 from-scratch 版的 $P(\text{NPV}>0)$（应接近 notes.md 的 55.7%）。改变推理成本（通过调整毛利率从 65% 到 55%/75%），观察 $P(\text{NPV}>0)$ 的变化--对应 notes.md "推理成本每降低1个百分点，毛利率提升1个百分点，NPV显著上升"。
2. 将 `bull_base_bear` 的场景参数从固定倍数（1.3/0.7）改为分位数驱动：从历史数据中取 90/50/10 分位数作为 Bull/Base/Bear 参数。对应 notes.md "天道推演三路径" 的概率注入步骤--让场景参数不再是主观设定而是数据驱动。
3. 为 `monte_carlo_npv` 添加"敏感性分析"输出：对每个参数（$R_0, g, m, r$）分别 $\pm 10\%$，计算 NPV 均值的变化量 $\Delta\text{NPV}$，按 $|\Delta\text{NPV}|$ 排序输出龙卷风图数据（文本格式，不依赖 matplotlib）。对应 starter.ipynb TODO5 的龙卷风图。
4. TODO: 在 `practice.md` 的 D2 drill（DCF 财务计算）中，用 from-scratch `npv` 替代 `npf.npv`，并手写 IRR（二分法求 `npv(r, cf) = 0` 的根 $r^*$）。这是 starter.ipynb TODO2/TODO3 的 from-scratch 版本，让 IRR 不依赖 numpy-financial 也能求解。用 `bull_base_bear` 输出的三路径 $P(\text{NPV}>0)$ 代替 notes.md 的天道推演叙事，完成技能4收官。
