# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：Capstone AI和商业分析 · Phase 4 因果实验设计与验证
> **scratch 哲学**：不调 DoWhy、不调 econml、不调 sklearn，手写 IPW + DML 因果估计器，从倾向得分 + 双重正交直译到 numpy。

## scratch_topic

本单元 from-scratch 主题：**手写 ATE/IPW 估计器 + DML 双重机器学习**。对应 rohitg00 P19/52 Experiment Runner + P19/53 Result Evaluator。notes.md/starter.ipynb 用 `dowhy.CausalModel` + `econml.dml.LinearDML` 完成 DoWhy 四步 + DML 估计，本层把"估计"这一步拆开：从倾向得分加权（IPW）与双重正交（DML）公式出发，手写 numpy 实现逻辑回归（倾向得分）+ IPW 估计 + DML 残差正交估计，让"为什么 DML 比朴素均值差无偏""倾向得分如何消除选择偏差"不再是 DoWhy/econml 的黑箱，而是可逐行审计的数值计算。

## core_algorithm

**IPW（逆倾向得分加权）** 通过对样本重新加权消除选择偏差。设倾向得分 $e(X) = P(T=1 \mid X)$，则 ATE 的 IPW 估计为：

$$\hat{\text{ATE}}_{\text{IPW}} = \frac{1}{n}\sum_{i=1}^{n}\left[\frac{T_i Y_i}{\hat{e}(X_i)} - \frac{(1-T_i)Y_i}{1-\hat{e}(X_i)}\right]$$

直觉：处理组样本被欠采样（$e(X)$ 小时本该更多人被处理），用 $1/e(X)$ 上加权；对照组用 $1/(1-e(X))$ 上加权。加权后两组的 $X$ 分布趋同，消除混杂偏差。倾向得分用逻辑回归估计：$e(X) = \sigma(X^T\beta)$，其中 $\sigma(z) = 1/(1+e^{-z})$，用 IRLS（迭代加权最小二乘）求解 $\beta$。

**DML（双重/去偏机器学习，Chernozhukov et al. 2018）** 针对部分线性模型 $Y = \theta T + g(X) + \epsilon_Y$，$T = m(X) + \epsilon_T$。先用 ML 估计 nuisance functions $\hat{\mu}_Y(X) = \hat{g}(X)$ 和 $\hat{\mu}_T(X) = \hat{m}(X)$，计算残差 $\tilde{Y} = Y - \hat{\mu}_Y(X)$、$\tilde{T} = T - \hat{\mu}_T(X)$，再用残差回归估计 $\theta$：

$$\hat{\theta}_{\text{DML}} = \frac{\sum_i \tilde{T}_i \tilde{Y}_i}{\sum_i \tilde{T}_i^2}$$

DML 的"双重正交"保证：即使 $\hat{\mu}_Y, \hat{\mu}_T$ 有 $o(n^{-1/4})$ 收敛速度的估计误差（ML 典型），$\hat{\theta}_{\text{DML}}$ 仍达 $o(n^{-1/2})$ 根号 n 收敛且渐近无偏。这是 DML 相比朴素回归后门调整的关键优势--在高维/非线性 nuisance 下仍无偏。手写时 $\hat{\mu}_Y, \hat{\mu}_T$ 用 OLS（线性 nuisance），逻辑回归用 IRLS（Newton 步 $\beta \leftarrow \beta + (X^TWX)^{-1}X^T(T-\hat{T})$，$W=\text{diag}(\hat{e}(1-\hat{e}))$）。

## code_artifact

```python
import numpy as np

def sigmoid(z):
    z = np.clip(z, -30, 30)
    return 1.0 / (1.0 + np.exp(-z))

def logistic_irls(X, T, iters=20, ridge=1e-6):
    # propensity score e(X) = sigma(X @ beta) via IRLS
    n, d = X.shape
    beta = np.zeros(d)
    for _ in range(iters):
        e = sigmoid(X @ beta)
        W = e * (1 - e) + ridge
        grad = X.T @ (T - e)
        H = (X * W[:, None]).T @ X + ridge * np.eye(d)
        beta = beta + np.linalg.solve(H, grad)
    return beta

def ipw_ate(X, T, Y):
    Xa = np.column_stack([np.ones(len(T)), X])
    beta = logistic_irls(Xa, T)
    e = sigmoid(Xa @ beta)
    e = np.clip(e, 0.01, 0.99)  # truncate for stability
    w1 = T / e
    w0 = (1 - T) / (1 - e)
    return (w1 * Y).sum() / w1.sum() - (w0 * Y).sum() / w0.sum()

def ols(X, Y):
    # beta = (XtX)^-1 XtY, with ridge
    XtX = X.T @ X + 1e-6 * np.eye(X.shape[1])
    return np.linalg.solve(XtX, X.T @ Y)

def dml_ate(X, T, Y):
    Xa = np.column_stack([np.ones(len(T)), X])
    muY = Xa @ ols(Xa, Y)      # E[Y|X]
    muT = Xa @ ols(Xa, T)      # E[T|X]
    Yr = Y - muY               # residualized Y
    Tr = T - muT               # residualized T (orthogonalized)
    return (Tr @ Yr) / (Tr @ Tr)

def naive_ate(T, Y):
    return Y[T == 1].mean() - Y[T == 0].mean()

# verification_property:
#   IPW & DML recover true ATE on semi-synthetic data; naive is biased under confounding;
#   DML ~ IPW when nuisance is linear; |naive - true| > |dml - true|.
if __name__ == "__main__":
    rng = np.random.default_rng(42)
    n = 2000
    X = rng.standard_normal((n, 3))
    e_true = sigmoid(0.5 * X[:, 0] - 0.3 * X[:, 1] + 0.2)  # propensity depends on X
    T = (rng.random(n) < e_true).astype(float)
    true_ate = 2.0
    Y = true_ate * T + 1.5 * X[:, 0] + 0.8 * X[:, 1] + 0.5 * rng.standard_normal(n)
    naive = naive_ate(T, Y)
    ipw = ipw_ate(X, T, Y)
    dml = dml_ate(X, T, Y)
    assert abs(dml - true_ate) < 0.25, f"DML {dml:.2f} must recover true ATE ~{true_ate}"
    assert abs(ipw - true_ate) < 0.25, f"IPW {ipw:.2f} must recover true ATE ~{true_ate}"
    assert abs(naive - true_ate) > 0.2, "naive must be biased under confounding"
    assert abs(naive - true_ate) > abs(dml - true_ate), "DML must beat naive"
```

**verification_property**: IPW 与 DML 在半合成数据上收敛到真实 ATE（true ATE=2.0，估计落入 [1.75, 2.25]）；朴素均值差在存在混杂时有偏（$|naive - true| > 0.2$）；DML 优于朴素（$|naive - true| > |dml - true|$）。

## connection_to_unit

1. **库 vs 手写的因果估计颗粒度**：notes.md 用 `dowhy.CausalModel.estimate_effect(method_name="backdoor.linear_regression")` 一行完成估计，from-scratch 版把"倾向得分估计 -> 加权 -> ATE"（IPW）与"nuisance 估计 -> 残差正交 -> theta"（DML）拆成显式步骤；DoWhy 的 `identify_effect` 对应"选 IPW 还是 DML"的策略选择，`estimate_effect` 对应这里的数值计算。
2. **DML vs econml 的对比**：starter.ipynb TODO5 用 `econml.dml.LinearDML(model_y=RandomForestRegressor, model_t=RandomForestClassifier)` 估计 ATE/CATE，from-scratch 版用 OLS 做 nuisance--econml 的 RF nuisance 能捕捉非线性，from-scratch 版的 OLS 仅线性 nuisance，在 notes.md NSW 数据（协变量与结果关系近似线性）上两者接近，但 from-scratch 版暴露了"DML 无偏性依赖 nuisance 估计质量"这个前提。
3. **倾向得分显形**：starter.ipynb TODO3 DoWhy 后门调整不显式输出倾向得分，from-scratch 版的 `logistic_irls` 直接返回 $\beta$ 与 $e(X)$--让"哪些协变量驱动了处理分配"可见（$\beta$ 系数），这是 uplift 建模（notes.md 前沿）的工程基础：倾向得分高的用户是"本来就会被干预"的，uplift 关注"边际用户"（$e(X) \approx 0.5$）。
4. **CUPED 的从零实现**：starter.ipynb TODO4 用 pandas 手动算 CUPED $\theta = \text{Cov}(Y, X_{pre})/\text{Var}(X_{pre})$，from-scratch 版的 `ols` 函数直接复用--CUPED 本质是 $Y$ 对 $X_{pre}$ 的 OLS 回归取残差，与 DML 的 nuisance 估计同构。这让"CUPED 是 DML 的特例"（单协变量、无处理变量）这个关系显形。

## deep_dive_links

- [P19/52 Experiment Runner - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/19-capstone-projects/52-experiment-runner/README.md) - 实验运行器，本单元 from-scratch 的工程锚点（IPW/DML 估计器作为实验 pipeline 的估计模块）
- [P19/53 Result Evaluator - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/19-capstone-projects/53-result-evaluator/README.md) - 结果评估器，ATE/CATE 估计后的稳健性检验与效果评估参考

## exercises

1. 在本单元 `starter.ipynb` TODO3（DoWhy 四步因果分析）运行后，用上面的 `ipw_ate` 和 `dml_ate` 在同一份 NSW 数据上手动估计 ATE，对比 DoWhy 后门调整输出，解释差异来源（提示：DoWhy 默认线性回归估计器，IPW 用倾向得分加权，DML 用残差正交--三者在 NSW 上应有近似但非相同的 ATE）。
2. 扩展 `dml_ate` 为 CATE 估计：用协变量子群（如 `age > 30` vs `age <= 30`）分组估计 DML ATE，对比 econml 因果森林的 CATE 输出。这是 notes.md TODO5/TODO6 异质效应分析的 from-scratch 版本。
3. 实现安慰剂检验：随机打乱 $T$ 后重跑 `ipw_ate`，验证 ATE 趋近 0。这是 DoWhy `refute_estimate(method="placebo")` 的 from-scratch 实现，对应 notes.md TODO3 第四步"反驳"。
4. TODO: 在 `practice.md` 的 drill 中，用本 from-scratch 的 `dml_ate` 替代 econml 版本，把 feedback_rule 中的"DML ATE 与 DoWhy 后门 ATE 差异 < 0.3"升级为"from-scratch DML ATE + IRLS 倾向得分手动验证 + 安慰剂检验 ATE 趋近 0"。这是 starter.ipynb TODO5 DML 的 from-scratch 版本。
