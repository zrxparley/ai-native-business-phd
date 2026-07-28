# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：模块R · R1 设计科学研究（DSR）
> **scratch 哲学**：不调 pydantic/pandas，手写 DSR 三维评分矩阵（rigor/relevance/efficacy），从 Hevner 七准则的加权聚合公式直译到 numpy。

## scratch_topic

本单元 from-scratch 主题：**手写 DSR 三维评估框架（rigor/relevance/efficacy 加权评分矩阵 + 平衡惩罚）**。对应 rohitg00 P0 Debugging and Profiling（可复现调试驱动的评估）+ P14 Eval Driven Agent Development（评估驱动设计）。notes.md 用 pydantic 定义 artifact schema、用 pandas DataFrame 给 Hevner 七准则打分，本层把"七准则如何聚合成一个 DSR 质量分"拆开：从 Hevner 2004 的 rigor vs design 张力出发，手写 numpy 实现"三维加权均值 - 不平衡方差惩罚"的效用函数，让"DSR 评估"不再是 pandas 表格里的平均值，而是可逐行审计的、带平衡约束的优化目标。

## core_algorithm

Hevner et al. (2004) 的核心张力是 rigor（严谨性，理论依据）与 design（相关性，实际问题）的平衡。我们将七准则划分为三个维度：**rigor**（准则1 artifact贡献、准则4 研究贡献、准则5 研究严谨性）、**relevance**（准则2 问题相关性、准则6 设计即搜索）、**efficacy**（准则3 设计评估、准则7 研究交流）。设准则 $i$ 的得分为 $s_i \in [1,5]$、权重为 $w_i > 0$，维度 $D \in \{R, V, E\}$ 的加权均值为：

$$\mu_D(a) = \frac{\sum_{i \in D} w_i\, s_i}{\sum_{i \in D} w_i}$$

朴素做法是直接平均三个维度 $Q = \tfrac{1}{3}(\mu_R + \mu_V + \mu_E)$，但这会掩盖"某维度极弱"的情况——一个 rigor=5、relevance=1、efficacy=1 的 artifact 朴素均分 2.33，看似及格，实则违反 Hevner "两者兼顾"要求。故引入**不平衡方差惩罚**：

$$Q(a) = \frac{1}{3}\big(\mu_R(a) + \mu_V(a) + \mu_E(a)\big) - \lambda \cdot \text{Var}\big(\mu_R(a), \mu_V(a), \mu_E(a)\big)$$

其中 $\text{Var}(\cdot) = \tfrac{1}{3}\sum_D (\mu_D - \bar\mu)^2$，$\bar\mu = \tfrac{1}{3}\sum_D \mu_D$。$\lambda \geq 0$ 控制对不平衡的容忍度：$\lambda=0$ 退化为朴素均分（容忍偏科），$\lambda \to \infty$ 退化为 max-min 下界（强制均衡）。这把"rigor vs design 张力"从定性论述转成可计算的目标函数——DSR 设计搜索就是在这个效用面上找 $Q$ 最大的 artifact 配置。贝叶斯扩展：当 $s_i$ 带噪声时，用 $s_i \sim \mathcal{N}(\hat s_i, \sigma_i^2)$ 采样得 $Q$ 的后验分布，诚实表达评估不确定性。

## code_artifact

```python
import numpy as np

# Hevner 7 criteria -> 3 dimensions partition
RIGOR = (0, 3, 4)        # c1 artifact, c4 research contrib, c5 rigor
RELEV = (1, 5)           # c2 problem relevance, c6 design-as-search
EFFIC = (2, 6)           # c3 design evaluation, c7 communication
DIMS = (RIGOR, RELEV, EFFIC)
WEIGHTS = np.array([1.0, 1.2, 1.0, 0.8, 1.0, 0.8, 0.9])

def dim_mean(scores, idx, w):
    s = np.array(scores, dtype=float)[list(idx)]
    wi = w[list(idx)]
    return float((s * wi).sum() / wi.sum())

def dsr_quality(scores, lam=0.5, w=WEIGHTS):
    mu = np.array([dim_mean(scores, d, w) for d in DIMS])
    base = mu.mean()
    penalty = lam * float(mu.var())
    return {"rigor": mu[0], "relevance": mu[1], "efficacy": mu[2],
            "mean": float(base), "penalty": penalty,
            "Q": float(base) - penalty}

if __name__ == "__main__":
    # balanced strong artifact (NSW ATE=1794.34 as efficacy evidence)
    good = [5, 5, 5, 4, 5, 4, 4]
    # rigor-heavy but weak efficacy (academic-only, no eval/communication)
    skewed = [5, 3, 1, 5, 5, 3, 1]
    qg = dsr_quality(good)
    qk = dsr_quality(skewed)
    assert qg["Q"] > qk["Q"], "balanced must beat skewed under penalty"
    assert qk["penalty"] > qg["penalty"], "skewed penalized harder"
    assert 4.0 < qg["Q"] < 5.0
```

**verification_property**: 平衡 artifact（good）的 $Q$ 严格高于偏科 artifact（skewed）；skewed 的不平衡方差惩罚 > good 的惩罚；good 的 $Q \in (4, 5)$（构造数据真值锚定）。当 $\lambda=0$ 时 $Q$ 退化为朴素均分，good 与 skewed 差距缩小——证明惩罚项捕获了 Hevner 平衡约束。

## connection_to_unit

1. **库 vs 手写的聚合逻辑**：notes.md/starter.ipynb TODO4 用 pandas DataFrame 存七准则评分后直接 `.mean()` 算平均分（朴素均分），from-scratch 版把"七准则 -> 三维 -> 带惩罚的 $Q$"拆成 `dim_mean` + `dsr_quality` 两步，暴露了"朴素均分掩盖偏科"这个被 pandas 一行代码隐藏的方法论缺陷。
2. **rigor/design 张力的可计算化**：notes.md 把 rigor vs design 描述为定性张力（"纯学术 rigor 高 design 低"），from-scratch 版用 `mu_R - mu_V` 的方差惩罚把它变成可优化目标——DSR Step 3 设计搜索等价于在 $Q$ 面上找最大值，连接了 notes.md 的"天道推演沙盘模拟"与具体优化。
3. **数据锚定对齐**：solution.ipynb 用 NSW ATE=1794.34 作为准则3（设计评估）证据给 5 分，from-scratch 版 `good` 实例的 efficacy 维度（准则3+准则7）正是这个锚点；TODO2 实例化的 artifact 评估结果可直接喂入 `dsr_quality` 做 $Q$ 重算。
4. **权重可审计**：pandas 版隐含等权（`mean`），from-scratch 版 `WEIGHTS` 数组显式给准则2（问题相关性）权重 1.2、准则4（研究贡献）权重 0.8，研究者必须为每个权重辩护——这是 pydantic schema 之外的"评估哲学"层。

## deep_dive_links

- [P0/12 Debugging and Profiling - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/00-setup-and-tooling/12-debugging-and-profiling/README.md) - 可复现调试：DSR Step 5 评估要求可复现，调试/profile 是评估可复现性的工程底座
- [P14/30 Eval Driven Agent Development - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/14-agent-engineering/30-eval-driven-agent-development/README.md) - 评估驱动开发：DSR 的"设计-评估"循环与 eval-driven agent 的"build-eval-iterate"同构

## exercises

1. 在本单元 `starter.ipynb` TODO4（七准则评分）完成后，把 TODO4 的 `evaluation_results` 评分向量喂入上面的 `dsr_quality`，对比 pandas `.mean()` 与 from-scratch $Q$（含 $\lambda=0.5$ 惩罚）。若两者排序不同，解释是哪个维度偏科导致的——这暴露了 TODO4 平均分掩盖的 rigor/design 失衡。
2. 实现贝叶斯扩展：当准则评分带噪声 $s_i \sim \mathcal{N}(\hat s_i, 0.3^2)$ 时，用 numpy 采样 1000 次得 $Q$ 的后验分布，输出 95% 置信区间。对比点估计 $Q$ 与区间估计，讨论 notes.md "贝叶斯评估替代点估计"前沿点在 DSR 中的具体形态。
3. 将 `WEIGHTS` 视为超参，扫描 $\lambda \in \{0, 0.25, 0.5, 1.0, 2.0\}$，观察 `good` 与 `skewed` 的 $Q$ 差距如何随 $\lambda$ 变化。画出 $\lambda$-$Q$ 曲线，定位"惩罚过强导致 good 也被压低"的拐点——这是 `practice.md` D2 drill "rigor/design 平衡分绝对值 < 1.5"判据的连续化版本。
4. TODO: 在 `practice.md` D3 drill（设计原则抽取）中，为每条设计原则添加一个 `dsr_quality` 维度标签（该原则主要提升 rigor/relevance/efficacy 哪一维），用 from-scratch 评分矩阵验证"4 条原则是否覆盖全部三维"——若某维无原则覆盖，触发 weak_loop。
