# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：技能0 AI商业分析基础 · Day 4 回归分析与概率分布
> **scratch 哲学**：不调 statsmodels.OLS / Logit，手写闭式解 + 梯度下降，从 $\hat\beta=(X^TX)^{-1}X^Ty$ 直译到 numpy 骨架。

## scratch_topic

本单元 from-scratch 主题：**手写线性回归 OLS + 梯度下降 + 逻辑回归**。对应 rohitg00 P2/02 Linear Regression + P2/03 Logistic Regression + P1/08 Optimization。notes.md/starter.ipynb 用 statsmodels.OLS / Logit 拟合 NSW 数据（treat 系数=1621, p=0.01），本层把"拟合"这一步拆开：从 OLS 闭式解 $(X^TX)^{-1}X^Ty$ 和梯度下降 $\beta \leftarrow \beta - \eta \nabla L$ 出发，手写 numpy 实现 OLS + SGD + Logit，让"treat 系数 1621"不再是 statsmodels 的黑箱输出，而是可逐行审计的矩阵运算。

## core_algorithm

OLS 线性回归最小化残差平方和 $\min_\beta \|y - X\beta\|^2$。对 $\beta$ 求导令其为零（正规方程）：

$$\nabla_\beta \|y - X\beta\|^2 = -2X^T(y - X\beta) = 0 \implies X^TX\beta = X^Ty \implies \hat\beta = (X^TX)^{-1}X^Ty$$

闭式解要求 $X^TX$ 可逆（无完美共线性，对应 notes.md VIF 检测）。残差方差 $\hat\sigma^2 = \|y - X\hat\beta\|^2 / (n - p)$，系数标准误 $\text{SE}(\hat\beta_j) = \sqrt{\hat\sigma^2 [(X^TX)^{-1}]_{jj}}$，$t = \hat\beta_j / \text{SE}(\hat\beta_j)$--这就是 statsmodels `.summary()` 的 p 值来源。

梯度下降迭代更新，学习率 $\eta$：

$$\beta_{t+1} = \beta_t - \eta \nabla L = \beta_t + \frac{2\eta}{n} X^T(y - X\beta_t)$$

当 $X^TX$ 病态（VIF 高，条件数大）时，梯度下降收敛极慢--这是 notes.md "VIF>10 严重共线性"的优化视角。from-scratch 版用 `np.linalg.solve` 替代显式求逆 $(X^TX)^{-1}$，数值更稳定（等价于 LU 分解）。

逻辑回归（Logit）用于二值因变量（如 treat 0/1），连接 notes.md TODO3 倾向性评分。预测 $\hat{p} = \sigma(X\beta)$，$\sigma(z) = 1/(1+e^{-z})$。梯度：

$$\nabla L = X^T(\sigma(X\beta) - y)$$

sigmoid 的数值稳定实现：当 $z \geq 0$ 用 $1/(1+e^{-z})$，当 $z < 0$ 用 $e^z/(1+e^z)$，避免大 $|z|$ 时溢出--这与 Day 3 的 log-sum-exp 同理，是 notes.md "数值稳定"的前置。

## code_artifact

```python
import numpy as np

def ols_closed_form(X, y):
    # beta_hat = (X^T X)^{-1} X^T y, via solve (more stable than inv)
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)
    return np.linalg.solve(X.T @ X, X.T @ y)

def ols_gradient_descent(X, y, lr=0.01, n_iter=5000):
    # beta_{t+1} = beta_t + (2*lr/n) X^T (y - X beta_t)
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)
    n, p = X.shape
    beta = np.zeros(p)
    for _ in range(n_iter):
        beta = beta + (2 * lr / n) * X.T @ (y - X @ beta)
    return beta

def sigmoid(z):
    # numerically stable: split z>=0 vs z<0 to avoid overflow
    z = np.asarray(z, dtype=float)
    return np.where(z >= 0, 1 / (1 + np.exp(-z)), np.exp(z) / (1 + np.exp(z)))

def logit_gradient_descent(X, y, lr=0.1, n_iter=5000):
    # gradient: X^T (sigmoid(X beta) - y)
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)
    n, p = X.shape
    beta = np.zeros(p)
    for _ in range(n_iter):
        beta = beta - (lr / n) * X.T @ (sigmoid(X @ beta) - y)
    return beta

# verification_property:
#   ols_closed_form == ols_gradient_descent (converged); X^T residual = 0 (normal equation);
#   logit beta shape correct; recover true beta on synthetic data
if __name__ == "__main__":
    rng = np.random.default_rng(0)
    n, p = 100, 3
    X = np.column_stack([np.ones(n), rng.standard_normal((n, p - 1))])
    true_beta = np.array([1.0, 2.0, -1.5])
    y = X @ true_beta + 0.1 * rng.standard_normal(n)
    b_cf = ols_closed_form(X, y)
    b_gd = ols_gradient_descent(X, y, lr=0.1, n_iter=10000)
    assert np.allclose(b_cf, b_gd, atol=0.05), f"cf {b_cf} vs gd {b_gd}"
    assert np.allclose(b_cf, true_beta, atol=0.1), "recover true beta"
    r = y - X @ b_cf
    assert np.allclose(X.T @ r, 0, atol=1e-9), "X^T r = 0 (normal equation)"
    # logit on binary outcome
    yl = (rng.random(n) < sigmoid(X @ true_beta)).astype(float)
    bl = logit_gradient_descent(X, yl, lr=0.1, n_iter=5000)
    assert bl.shape == true_beta.shape
    assert np.all(sigmoid(X @ bl) > 0) and np.all(sigmoid(X @ bl) < 1)
```

**verification_property**: OLS 闭式解 == 梯度下降解（收敛后 atol=0.05）；$X^T r = 0$（正规方程，残差正交于列空间）；闭式解恢复真实 $\beta$（atol=0.1）；Logit 输出 $\sigma(X\beta) \in (0,1)$。

## connection_to_unit

1. **statsmodels.OLS vs from-scratch ols_closed_form**：solution.ipynb TODO2 用 `sm.OLS(y, sm.add_constant(X)).fit()` 拟合 NSW 回归，from-scratch 版用 `np.linalg.solve(X.T @ X, X.T @ y)` 直接算闭式解--两者数学等价，但 statsmodels 额外提供 p 值 / CI / R² / VIF，from-scratch 版只有点估计 $\hat\beta$。notes.md 的 treat 系数 1621 在 from-scratch 版是 `b_cf[treat_col]`，可逐行验证。
2. **VIF 共线性 vs 条件数**：notes.md 用 `variance_inflation_factor` 检测 VIF>10 的多重共线性，from-scratch 版用 $X^TX$ 的条件数 $\kappa = \sigma_{\max}/\sigma_{\min}$（最大/最小奇异值比）检测同一问题--VIF 是"去掉某列后的共线性"，条件数是"整体共线性"，两者都是 $X^TX$ 接近奇异的表现，from-scratch 让"共线性 = 矩阵病态"这个几何事实可见。
3. **Logit 倾向性评分 vs from-scratch sigmoid**：solution.ipynb TODO3 用 `sm.Logit(y, X).fit()` 算倾向性评分 $P(\text{treat}=1|X)$，from-scratch 版用 `logit_gradient_descent` + `sigmoid` 手写--statsmodels 用 IRLS（迭代加权最小二乘）收敛，from-scratch 用 vanilla SGD，两者给出相近 $\beta$ 但收敛路径不同。
4. **QuantReg 分位数回归 vs OLS 均值回归**：notes.md 教分位数回归发现"treat 75 分位 2502 vs 25 分位 290"，from-scratch 版的 `ols_closed_form` 只算条件均值 $\mathbb{E}[Y|X]$--分位数回归最小化 $\rho_\tau(y - X\beta)$（check loss），需改用线性规划或梯度下降，from-scratch OLS 无法捕捉异质性效应，这正说明 notes.md 分位数回归的增量价值。

## deep_dive_links

- [P2/02 Linear Regression - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/02-linear-regression/README.md) - 线性回归 from scratch，OLS 闭式解与梯度下降的数学锚点
- [P2/03 Logistic Regression - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/03-logistic-regression/README.md) - 逻辑回归，sigmoid + MLE + 倾向性评分
- [P1/08 Optimization - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/08-optimization/README.md) - 梯度下降族，学习率/收敛/凸优化基础

## exercises

1. 在本单元 `starter.ipynb` TODO2（OLS 回归）运行后，用上面的 `ols_closed_form` 在同一份 NSW 数据上手动估计 treat 系数（需手动 `np.column_stack` 加截距列），对比 statsmodels 输出--应复现 treat $\approx 1621$，差异仅来自数值精度。
2. 用 `ols_gradient_descent` 替换闭式解，固定 $\eta=0.01$，测量不同迭代次数（100/1000/10000）下 $\hat\beta$ 与闭式解的差距；构造高 VIF 的 $X$（两列几乎共线），观察梯度下降收敛是否极慢（连接 notes.md VIF 检测）。
3. 为 `ols_closed_form` 添加 p 值计算：$\hat\sigma^2 = \|r\|^2/(n-p)$，$\text{Var}(\hat\beta) = \hat\sigma^2 (X^TX)^{-1}$，$t_j = \hat\beta_j / \sqrt{\text{diag}(\text{Var})_j}$，对比 statsmodels `.summary()` 的 p 值，验证 from-scratch 能复现 treat p≈0.01。
4. TODO: 在 `practice.md` D2 的 Logit 倾向性评分练习中，用 `logit_gradient_descent` + `sigmoid` 替换 `sm.Logit`，对比两者输出的倾向性评分直方图，讨论 SGD vs IRLS 的收敛差异（连接 Day 3 贝叶斯采样的随机性）。
