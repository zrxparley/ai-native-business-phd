# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：选修E2 营销分析 · Day 1 框架与描述/诊断分析
> **scratch 哲学**：不调 statsmodels.OLS、不调 pandas.qcut，手写正规方程求解 OLS 系数 + 手写分位数分箱做 RFM，从 $(X^TX)^{-1}X^Ty$ 直译到 numpy。

## scratch_topic

本单元 from-scratch 主题：**手写 OLS 正规方程 + RFM 分位数分箱**。对应 rohitg00 P2/02 Linear Regression（OLS 从零推导）+ P1/15 Statistics for ML（描述统计从零）。notes.md/solution.ipynb 用 `statsmodels.OLS` 一行拟合 `re78 ~ treat + re75 + age + educ` 并输出 summary，用 `pd.qcut` 一行做 RFM 的 M 分桶。本层把"求解 beta"和"按分位数分箱"两步拆开：从最小化残差平方和的一阶条件推出正规方程，手写 numpy 解线性方程组；从排序索引推出分位数边界，手写 numpy 分箱--让"控制混杂后的净效应"和"自适应分群"不再是库的黑箱。

## core_algorithm

OLS（普通最小二乘）是诊断性分析的核心：给定设计矩阵 $X \in \mathbb{R}^{n \times k}$（含截距列）和结果向量 $y \in \mathbb{R}^n$，求 $\beta$ 最小化残差平方和：

$$\hat\beta = \arg\min_\beta \|y - X\beta\|^2 = \arg\min_\beta (y - X\beta)^T(y - X\beta)$$

展开目标函数 $L(\beta) = y^Ty - 2\beta^TX^Ty + \beta^TX^TX\beta$，对 $\beta$ 求梯度并令其为零（一阶必要条件）：

$$\frac{\partial L}{\partial \beta} = -2X^Ty + 2X^TX\beta = 0 \implies X^TX\hat\beta = X^Ty$$

这就是**正规方程**（normal equation）。当 $X^TX$ 可逆（$X$ 列满秩，无完美共线性），解为：

$$\hat\beta = (X^TX)^{-1}X^Ty$$

数值上不直接求逆，而用 `np.linalg.solve(XtX, Xty)` 解线性方程组（更稳定、$O(k^3)$ 而非求逆的 $O(k^3)$ 但常数更小）。拟合值 $\hat y = X\hat\beta$，残差 $e = y - \hat y$。决定系数 $R^2 = 1 - \frac{\sum e_i^2}{\sum(y_i - \bar y)^2}$ 衡量模型解释的方差比例。$\hat\beta_T$（treat 列对应系数）即"控制其他变量后的净效应"--这是 Day 1 TODO6 的核心产出，from-scratch 版让它等于一次矩阵分解，而非 statsmodels 的黑箱输出。

RFM 分位数分箱的从零实现：给定值数组 $v$，按排序秩次 $r_i$ 映射到桶 $b_i = \lfloor r_i \cdot k / n \rfloor$（截断到 $k-1$），等价于 `pd.qcut(v, k)` 但不依赖 pandas。这让"Champions = R 高分位 + F 高分位"的阈值自适应数据分布，而非硬编码固定金额。

## code_artifact

```python
import numpy as np

def ols_fit(X, y):
    # normal equation: beta = (X^T X)^{-1} X^T y  (solve, don't invert)
    return np.linalg.solve(X.T @ X, X.T @ y)

def r_squared(y, y_pred):
    ss_res = np.sum((y - y_pred) ** 2)
    ss_tot = np.sum((y - y.mean()) ** 2)
    return 1 - ss_res / ss_tot

def rfm_quantile_bin(values, n_bins=5):
    # manual quantile binning (no pandas qcut); 0=lowest, n_bins-1=highest
    order = np.argsort(values)
    n = len(values)
    bins = np.zeros(n, dtype=int)
    for rank, idx in enumerate(order):
        bins[idx] = min(int(rank * n_bins / n), n_bins - 1)
    return bins

def rfm_segment(r, f, m):
    if r == 1 and f >= 2 and m >= 3: return "Champions"
    if r == 1 and f >= 2: return "Loyal"
    if r == 1: return "Recent"
    if f >= 2: return "At Risk"
    return "Lost"

# verification_property:
#   OLS recovers true beta on near-linear data; R^2 > 0.95; RFM bin 0 = smallest.
if __name__ == "__main__":
    rng = np.random.default_rng(0)
    n = 100
    X = np.column_stack([np.ones(n), rng.standard_normal((n, 2))])
    beta_true = np.array([2.0, 3.0, -1.0])
    y = X @ beta_true + 0.1 * rng.standard_normal(n)
    beta_hat = ols_fit(X, y)
    y_pred = X @ beta_hat
    assert np.allclose(beta_hat, beta_true, atol=0.05), "OLS recovers true beta"
    assert r_squared(y, y_pred) > 0.95, "R^2 high on near-linear data"
    bins = rfm_quantile_bin(np.array([10,20,30,40,50,60,70,80,90,100]), 5)
    assert bins[0] == 0 and bins[-1] == 4, "smallest->bin0, largest->top"
```

**verification_property**: OLS 在近线性数据上恢复真实系数（`beta_hat ≈ beta_true`，atol=0.05）；$R^2 > 0.95$（高信噪比下模型解释几乎全部方差）；RFM 分位数分箱的最小值落入 bin 0、最大值落入 top bin（分箱单调性）。

## connection_to_unit

1. **库 vs 手写的颗粒度**：notes.md TODO6 用 `sm.OLS(y, sm.add_constant(X)).fit().summary()` 一行输出系数/p 值/CI/R²，from-scratch 版把"求 beta"拆成 `np.linalg.solve(X.T @ X, X.T @ y)` 一次线性方程组求解--让"为什么 treat 系数是净效应"等于"它是正规方程解的一个分量"，而非 statsmodels 的黑箱输出。
2. **RFM 分箱对比**：solution.ipynb TODO3 用 `pd.qcut(df['M'].rank(method='first'), q=4)` 一行做 M 分桶，from-scratch 版用 `np.argsort` + 秩次映射 `int(rank * k / n)` 复现等频分箱--让"分位数分箱 = 按排序秩次切"这个操作在纯数组上可见，不被 pandas 的 `qcut` 抽象遮蔽。
3. **数值稳定**：statsmodels 内部用 QR 分解解 OLS（对共线性更稳），from-scratch 版用 `np.linalg.solve`（LU 分解）--在 TODO6 的 `re78 ~ treat + re75 + age + educ` 上若 `re74` 与 `re75` 高度共线（notes.md 提到 re74-re75 强相关），`X^TX` 接近奇异，手写版会暴露数值病态，这正是 statsmodels 默认隐藏的工程细节。
4. **残差诊断可读性**：starter.ipynb TODO6 只输出 `model.summary()` 的表格，from-scratch 版可直接拿到残差 `e = y - X @ beta`，让"残差正态性/同方差性"诊断（notes.md 诊断性分析核心）成为可逐行审计的数组操作--这是 capstone 做回归诊断的 from-scratch 基础。

## deep_dive_links

- [P2/02 Linear Regression - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/02-linear-regression/README.md) - 线性回归 from scratch，正规方程与梯度下降两种求解，本单元 OLS 的理论锚点
- [P1/15 Statistics for ML - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/15-statistics-for-ml/README.md) - ML 统计基础，描述统计与假设检验的数学推导

## exercises

1. 在本单元 `starter.ipynb` TODO6（statsmodels OLS 回归 `re78 ~ treat + re75 + age + educ`）运行后，用上面的 `ols_fit` 在同一份 NSW 数据上手动估计系数，对比 `sm.OLS` 的 `model.params['treat']` 与手写 `beta_hat[treat_idx]`，解释差异来源（提示：statsmodels 默认用 QR 分解，手写版用 solve，数值精度差异在共线性下放大）。
2. 将 `rfm_quantile_bin` 从 5 档扩展到连续值版：对 M 用分位数分箱后，再实现 R 和 F 的二值化（R = re78>0, F = 消费年份数），套用 `rfm_segment` 产出 Champions/Loyal/Recent/At Risk/Lost 五类。对比 solution.ipynb TODO3 的 pandas `apply` 版本，观察两者分群人数是否一致（应一致，因分箱逻辑等价）。
3. 构造"共线性诊断"实验：在 NSW 上加入 `re74` 列（与 `re75` 强相关），用 `ols_fit` 拟合 `re78 ~ treat + re74 + re75 + age + educ`，观察 `X^TX` 的条件数（`np.linalg.cond(X.T @ X)`）。当条件数 > 30 时，treat 系数是否变得不稳定？这与 notes.md "re74-re75 强相关"的描述如何对应？这是 statsmodels `summary()` 默认不暴露的 from-scratch 诊断。
4. TODO: 在 `practice.md` 的 D4 drill（OLS 回归）中，为本 from-scratch `ols_fit` 添加"残差正态性检验"输出（手算残差偏度/峰度，对比 scipy 的正态分布），当残差偏度绝对值 > 1 时标记"非正态，p 值不可信"。这是 TODO6 `model.summary()` 之外的 from-scratch 稳健性检查。
