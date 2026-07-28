# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：技能0 AI商业分析基础 · Day 3 描述统计与推断统计
> **scratch 哲学**：不调 scipy.stats.beta，手写 Beta-Binomial 共轭后验更新，从 Bayes 定理直译到 numpy/math 骨架。

## scratch_topic

本单元 from-scratch 主题：**手写贝叶斯后验更新 + 概率分布采样**。对应 rohitg00 P1/06 Probability and Distributions + P1/07 Bayes Theorem + P1/15 Statistics for ML。notes.md/starter.ipynb 用 scipy.stats.ttest_ind / chi2_contingency / beta 做 A/B 测试统计推断，本层把贝叶斯推断这一步拆开：从 Beta-Binomial 共轭后验公式出发，手写 Beta PDF（用 `math.lgamma` 而非 scipy）+ 共轭更新 + 拒绝采样，让"先验 -> 似然 -> 后验"的更新机制不再是 scipy.stats.beta 的黑箱，而是可逐行审计的数值计算。

## core_algorithm

Beta-Binomial 共轭是贝叶斯统计最简单的入门模型，也是 notes.md TODO6 的核心。设转化率 $p$ 的先验为 $p \sim \text{Beta}(\alpha, \beta)$，观察到 $s$ 次成功 / $n$ 次试验（似然为 Binomial），则后验为：

$$P(p \mid s, n) = \frac{P(s \mid p) P(p)}{\int_0^1 P(s \mid p) P(p) dp} = \frac{p^{(\alpha+s)-1}(1-p)^{(\beta+n-s)-1}}{B(\alpha+s, \beta+n-s)}$$

其中 Beta 函数 $B(\alpha, \beta) = \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}$，$\Gamma$ 是 Gamma 函数。共轭性的威力在于：后验仍是 Beta 分布，参数简单更新为 $(\alpha+s, \beta+n-s)$，无需计算积分。

后验均值（点估计）为：

$$\mathbb{E}[p \mid s, n] = \frac{\alpha + s}{\alpha + \beta + n}$$

当 $n \to \infty$ 时后验均值趋近极大似然估计 $s/n$；当 $n$ 小时先验 $(\alpha, \beta)$ 起收缩（shrinkage）作用。先验 Beta(1,1) 是均匀分布（无信息先验），后验均值 $= (1+s)/(2+n) \approx s/n$（大样本）。Beta PDF 为：

$$f(p; \alpha, \beta) = \frac{p^{\alpha-1}(1-p)^{\beta-1}}{B(\alpha, \beta)}, \quad p \in (0,1)$$

from-scratch 版用 `math.lgamma`（对数 Gamma）计算 $\log B(\alpha,\beta) = \text{lgamma}(\alpha) + \text{lgamma}(\beta) - \text{lgamma}(\alpha+\beta)$，避免大 $\alpha$ 时的数值溢出。采样用拒绝采样（rejection sampling）：在 $[0,1]$ 均匀提议，以 Beta PDF 为接受概率，无需 scipy.stats.beta.rvs。共轭更新的"序列性"是关键：两批数据 $(s_1, n_1)$ 和 $(s_2, n_2)$ 分两步更新，等价于一批 $(s_1+s_2, n_1+n_2)$ 更新--这是 notes.md "贝叶斯后验可随新数据持续更新"的数学保证。

## code_artifact

```python
import numpy as np
import math

def beta_pdf(p, a, b):
    # Beta(a,b) PDF: p^(a-1)(1-p)^(b-1) / B(a,b), using lgamma for stability
    if p <= 0 or p >= 1:
        return 0.0
    log_B = math.lgamma(a) + math.lgamma(b) - math.lgamma(a + b)
    return math.exp((a - 1) * math.log(p) + (b - 1) * math.log(1 - p) - log_B)

def beta_binomial_posterior(prior_a, prior_b, successes, trials):
    # conjugate update: Beta(a,b) + s/n -> Beta(a+s, b+n-s)
    return prior_a + successes, prior_b + trials - successes

def posterior_mean(a, b):
    return a / (a + b)

def beta_sample(a, b, n=1000, seed=42):
    # rejection sampling (no scipy.stats.beta.rvs)
    rng = np.random.default_rng(seed)
    peak_p = (a - 1) / (a + b - 2) if a > 1 and b > 1 else 0.5
    max_pdf = beta_pdf(peak_p, a, b) if a > 1 and b > 1 else 1.0
    samples = []
    while len(samples) < n:
        p = rng.random()
        if rng.random() * max_pdf < beta_pdf(p, a, b):
            samples.append(p)
    return np.array(samples)

# verification_property:
#   posterior params (a+s, b+n-s); sequential update == batch update; samples within [0,1]
if __name__ == "__main__":
    # prior Beta(1,1) + 30 successes / 200 trials -> posterior Beta(31, 171)
    a, b = beta_binomial_posterior(1, 1, 30, 200)
    assert a == 31 and b == 171
    assert abs(posterior_mean(a, b) - 31/202) < 1e-9
    # sequential update == batch update (conjugacy)
    a1, b1 = beta_binomial_posterior(1, 1, 15, 100)
    a2, b2 = beta_binomial_posterior(a1, b1, 15, 100)
    assert a2 == 31 and b2 == 171, "sequential must equal batch"
    # samples within [0,1] and mean near posterior mean
    s = beta_sample(31, 171, n=2000)
    assert np.all(s > 0) and np.all(s < 1)
    assert abs(s.mean() - 31/202) < 0.02, f"sample mean {s.mean():.4f} ~= {31/202:.4f}"
```

**verification_property**: 后验参数 $(a+s, b+n-s) = (31, 171)$；序列更新（15/100 两批）== 批量更新（30/200）；后验均值 $= 31/202 \approx 0.153$；拒绝采样样本全在 $(0,1)$ 内且样本均值收敛到后验均值。

## connection_to_unit

1. **scipy.stats.beta vs from-scratch beta_pdf**：notes.md TODO6 用 `scipy.stats.beta(a, b).pdf(p)` / `.rvs()` 做贝叶斯推断，from-scratch 版用 `math.lgamma` + `math.exp` 手写 Beta PDF + 拒绝采样--scipy 的 `beta.pdf` 内部就是 $p^{\alpha-1}(1-p)^{\beta-1}/B(\alpha,\beta)$，from-scratch 让 Beta 函数 $B(\alpha,\beta) = \Gamma(\alpha)\Gamma(\beta)/\Gamma(\alpha+\beta)$ 的对数计算显形，理解大 $\alpha$ 时为何用 lgamma 而非直接算 Gamma。
2. **ttest_ind vs 后验更新**：solution.ipynb TODO3 用 `scipy.stats.ttest_ind` 做 A/B 转化率 t 检验（频率派），from-scratch 版做 Beta-Binomial 后验更新（贝叶斯派）--两者回答不同问题：t 检验答"H0 成立时观察到当前差异的概率"，后验答"给定数据，转化率 $p$ 的分布是什么"，notes.md 的"频率派 vs 贝叶斯派"表格在这里变成可运行的代码对照。
3. **ASA p 值六原则 vs 后验分布**：notes.md 教 ASA 2016 p 值六原则（p ≠ P(H0 真)），from-scratch 版的后验分布直接给出 $P(p > \text{阈值} \mid \text{data})$--这个"直接回答业务问题"的能力是贝叶斯相对于频率派的核心优势，notes.md 称"贝叶斯后验直接回答方案有效的概率"，from-scratch 让这个概率可计算。
4. **共轭序列更新 vs A/B 测试持续优化**：notes.md 称"贝叶斯后验可随新数据持续更新，每次实验结果都是下一次实验的先验"，from-scratch 版的 `beta_binomial_posterior(a1, b1, s2, n2)` 验证了"两批更新 = 一批更新"的共轭性--这是营销 A/B 测试"持续优化节奏"的数学基础，频率派 t 检验无此性质。

## deep_dive_links

- [P1/06 Probability and Distributions - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/06-probability-and-distributions/README.md) - 概率分布 from scratch，Beta/Binomial/Normal 的数学推导锚点
- [P1/07 Bayes Theorem - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/07-bayes-theorem/README.md) - 贝叶斯定理，先验/似然/后验的更新机制
- [P1/15 Statistics for ML - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/15-statistics-for-ml/README.md) - ML 统计，假设检验与贝叶斯推断的工程对照

## exercises

1. 在本单元 `starter.ipynb` TODO6（Beta-Binomial 贝叶斯估计）运行后，用上面的 `beta_binomial_posterior` + `beta_sample` 在同一份 A/B 测试数据上手动估计后验，对比 `scipy.stats.beta` 输出的后验均值与可信区间，解释差异来源（提示：from-scratch 拒绝采样的随机性 vs scipy 的精确分位数）。
2. 将先验从 Beta(1,1)（均匀/无信息）改为 Beta(10,10)（强先验，峰值在 0.5），在相同观察 $s=30, n=200$ 下对比后验均值的变化，验证"小样本时先验起收缩作用"（shrinkage），观察 $n=20$ vs $n=2000$ 时先验影响的衰减。
3. 构造"先验冲突"场景：先验 Beta(100,1)（强偏 $p \approx 1$）+ 观察到 $s=10, n=100$（数据说 $p \approx 0.1$），用 `beta_sample` 画后验分布直方图，验证后验被先验主导还是数据主导，讨论 notes.md "先验信息显式融入"的利弊。
4. TODO: 在 `practice.md` D3 的贝叶斯练习中，为本 from-scratch 实现添加"95% 可信区间"输出（用 `beta_sample` 采样的 2.5% / 97.5% 分位），对比频率派 95% CI 的语义差异（"95% 概率包含真值" vs "重复实验 95% 次包含真值"）。
