# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：技能3 因果推断 · Day 5 规模实验与营销应用
> **scratch 哲学**：不调 econml/scikit-uplift，手写 two-model CATE + Qini 曲线 + 贪心 MAB 预算分配，从 $\mu_1(x)-\mu_0(x)$ 与累计增量直译到 numpy。

## scratch_topic

本单元 from-scratch 主题：**手写 uplift modeling（two-model CATE + Qini 曲线）+ MAB 贪心预算分配**。对应 rohitg00 P2 ML Pipelines（CATE 模型作为 pipeline 一环）+ P9 Policy Gradients REINFORCE（决策优化的 RL 渊源）。notes.md/starter.ipynb TODO4 用 econml CausalForestDML 估 CATE、TODO6 用 scikit-uplift 画 Qini、TODO3 用 Thompson sampling 跑 MAB；本层把"哪类用户响应最大""按 CATE 排序的累计增量""有限预算如何分配"三步都拆成可逐行审计的 numpy：two-model OLS 估 CATE、累计增量算 Qini、贪心按 CATE 填预算，让"从估计效应到优化决策"的跃迁在白板级代码中显形。

## core_algorithm

**Uplift Modeling（two-model 法）**：对随机化数据，分别拟合 $\hat\mu_1(x)=E[Y\mid T=1,X=x]$ 与 $\hat\mu_0(x)=E[Y\mid T=0,X=x]$，预测个体条件平均处理效应

$$\hat\tau(x)=\hat\mu_1(x)-\hat\mu_0(x)$$

这是 CATE 的最简估计器--CausalForestDML 是其非参数推广（用森林/ML 替代 OLS、用 DML 正交化去偏）。two-model OLS 假设 CATE 在 $X$ 上线性，适合教学 baseline。

**Qini 曲线**：按预测 $\hat\tau(x)$ 降序排列用户，对前 $k$ 个计算累计增量

$$\text{Qini}(k)=\sum_{i\le k}T_iY_i - \sum_{i\le k}(1-T_i)Y_i\cdot\frac{\sum_{i\le k}T_i}{\sum_{i\le k}(1-T_i)}$$

第一项是前 $k$ 中处理组的累计响应，第二项是对照组响应率外推到处理组规模的预期响应--差值即"投放带来的增量转化"。好的 uplift 模型 Qini 在顶部 fraction 急升（高 CATE 用户驱动增量），随机排序的 Qini 近似直线。Qini 曲线下面积是 uplift 模型的总价值度量，类比 ROC-AUC。notes.md"关键回顾1 Uplift 四类用户"中 persuadables（可被说服）对应 Qini 顶部高增量区，sleeping dogs（反响应，$\hat\tau(x)<0$）需在排序中允许负 CATE 才能识别。

**MAB 贪心预算分配**：给定 $K$ 个用户群，各群估计 CATE $\hat\tau_k$、可达规模 $s_k$，预算 $B$，最大化总增量

$$\max_{a_k}\sum_k \hat\tau_k a_k\quad\text{s.t.}\quad 0\le a_k\le s_k,\ \sum_k a_k\le B$$

每用户成本为 1 时，价值密度即 $\hat\tau_k$，贪心按 $\hat\tau_k$ 降序填满各群直到预算耗尽即最优（线性可分背包）。这是 TODO3 Thompson sampling 的"已知 CATE、纯利用"对偶：Thompson 在 CATE 未知时探索，贪心在 CATE 已估时利用。

## code_artifact

```python
import numpy as np

def cate_two_model(X, T, Y):
    # two-model OLS: fit Y|X on T=1 and T=0 separately, CATE = mu1(x) - mu0(x)
    Xa = np.column_stack([np.ones(len(X)), X])
    m1 = np.linalg.lstsq(Xa[T == 1], Y[T == 1], rcond=None)[0]
    m0 = np.linalg.lstsq(Xa[T == 0], Y[T == 0], rcond=None)[0]
    return Xa @ (m1 - m0)

def qini_curve(cate_pred, T, Y):
    # sort by predicted CATE desc; cumulative incremental uplift per prefix
    order = np.argsort(-cate_pred)
    Ts, Ys = T[order], Y[order]
    cum_t = np.cumsum(Ts); cum_yt = np.cumsum(Ts * Ys)
    cum_c = np.cumsum(1 - Ts); cum_yc = np.cumsum((1 - Ts) * Ys)
    inc = cum_yt - cum_yc * cum_t / np.maximum(cum_c, 1)
    frac = np.arange(1, len(Y) + 1) / len(Y)
    return frac, inc

def mab_budget_alloc(cates, sizes, budget):
    # greedy: fill highest-CATE segments first, capped by segment size
    order = np.argsort(-cates)
    alloc = np.zeros(len(cates), dtype=int); remaining = budget
    for i in order:
        give = min(sizes[i], remaining); alloc[i] = give; remaining -= give
        if remaining <= 0: break
    return alloc, float((cates * alloc).sum())

# verification_property:
#   Qini of CATE-ranked population is positive at top fraction (uplift concentrated in high-CATE);
#   greedy MAB fills highest-CATE segment first.
if __name__ == "__main__":
    rng = np.random.default_rng(0); n = 1000
    X = rng.standard_normal((n, 1))
    T = rng.integers(0, 2, n).astype(float)  # randomized
    Y = 1.0 * T * X[:, 0] + 0.5 * rng.standard_normal(n)  # true CATE = x, varies with X
    cate = cate_two_model(X, T, Y)
    frac, inc = qini_curve(cate, T, Y)
    assert inc[int(0.3 * n)] > 0, "Qini at top 30% must be positive when CATE varies with X"
    alloc, total = mab_budget_alloc(np.array([0.1, 0.3, 0.05]), np.array([100, 50, 200]), budget=120)
    assert alloc[1] == 50 and alloc[0] == 70, "greedy must fill highest-CATE segment first"
```

**verification_property**: Qini 曲线在 CATE 随 $X$ 变化的随机化数据上，top 30% 的累计增量 $>0$（uplift 集中在高 CATE 用户）；贪心 MAB 在 3 群（CATE 0.1/0.3/0.05、规模 100/50/200、预算 120）下先填满最高 CATE 群（idx=1，50），再填次高（idx=0，70），验证按价值密度贪心即最优。

## connection_to_unit

1. **econml CausalForestDML vs 手写 two-model OLS**：starter.ipynb TODO4 用 `CausalForestDML` 估 CATE（非参数 + DML 去偏），from-scratch `cate_two_model` 是其最简线性 baseline--让"two-model 是 CausalForestDML 的线性特例"显形：当 CATE 在 $X$ 上线性时两者一致，非线性时森林胜出。这是 notes.md"关键回顾4 CATE"从估计到异质性的入门台阶。
2. **TODO3 Thompson vs 手写贪心 MAB 的对偶**：TODO3 用 Thompson sampling 在未知响应率下探索-利用，from-scratch `mab_budget_alloc` 是"CATE 已估、纯利用"的贪心分配--两者是 MAB 的两个 regime：Thompson 解"未知时的探索"，贪心解"已知后的预算最优分配"。同一营销问题（有限流量如何分配）在 CATE 估计前用 Thompson、估计后用贪心，构成 notes.md"关键回顾1 MAB 自适应实验"到"关键回顾5 数据->因果->决策"的闭环。
3. **scikit-uplift Qini vs 手写 qini_curve**：TODO6（可选）用 scikit-uplift 画 Qini，from-scratch `qini_curve` 把"累计增量 = 处理组响应 - 对照组响应率 × 处理组规模"逐项写出--让 Qini 不再是黑箱指标，而是一个可审计的差值。随机排序的 Qini 近似直线，CATE 排序的 Qini 在顶部急升，两线之差即 uplift 模型价值（练习2）。
4. **Uplift 四类用户的代码定位**：notes.md"关键回顾1 Uplift 四类"中 persuadables 对应 Qini 顶部高增量区，sleeping dogs（反响应）对应 $\hat\tau(x)<0$；from-scratch `qini_curve` 默认按 CATE 降序，要识别 sleeping dogs 须允许负 CATE 排序（练习4）--这暴露了 two-model CATE 在"反响应用户"识别上的边界，是 practice.md D3 feedback"sleeping dogs 投了有害"的 from-scratch 验证点。

## deep_dive_links

- [P2/13 ML Pipelines - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/13-ml-pipelines/README.md) - ML pipeline：CATE 模型作为营销决策 pipeline 一环的工程定位
- [P9/06 Policy Gradients REINFORCE - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/09-reinforcement-learning/06-policy-gradients-reinforce/README.md) - 策略梯度：MAB/预算分配作为决策优化的 RL 渊源

## exercises

1. 在本单元 `starter.ipynb` TODO4（CausalForestDML）运行后，用 `cate_two_model` 在同一份 NSW 数据上估 CATE，对比两者的 per-user CATE 预测相关性。解释何时 two-model OLS 够用（CATE 在 $X$ 上线性）、何时 CausalForestDML 胜出（非线性异质性）--这是 notes.md"关键回顾4 CATE"的 from-scratch baseline 对照。
2. 在 `practice.md` D3（Uplift + Qini）阶段，用 `qini_curve` 替换 scikit-uplift：绘制 frac-inc 曲线，再画一条随机排序（`np.random.shuffle(cate_pred)`）的 Qini 对比线，两线之差即 uplift 模型价值。在曲线上标注"persuadables 区段"（顶部 Qini 急升的前 30%）。
3. 扩展 `mab_budget_alloc` 处理"每用户成本 $c_k$ 不等"（邮件便宜、Push 中等、SMS 贵）：贪心按 $\hat\tau_k/c_k$（价值密度）而非 $\hat\tau_k$ 排序。应用到 notes.md"关键回顾2 营销归因"的三渠道场景，对比等成本 vs 不等成本的分配差异。
4. TODO: 为 `qini_curve` 添加"sleeping dogs 检测"--允许负 CATE 进入排序，识别投放反而害了哪些用户（负增量）。在 NSW 上检查是否存在子群 CATE<0（培训反而降低其收入），这是 practice.md D3 feedback"sleeping dogs 投了有害"的 from-scratch 验证。
