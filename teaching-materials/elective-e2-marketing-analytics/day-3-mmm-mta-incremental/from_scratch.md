# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：选修E2 营销分析 · Day 3 MMM/MTA 与增量测量
> **scratch 哲学**：不调 sklearn.Ridge、不调 scipy.optimize，手写岭回归正规方程 + Markov 吸收链移除效应，从 $(X^TX+\alpha I)^{-1}X^Ty$ 和 $(I-Q)^{-1}R$ 直译到 numpy。

## scratch_topic

本单元 from-scratch 主题：**手写 MMM 岭回归 + Markov MTA 移除效应**。对应 rohitg00 P2/13 ML Pipelines（Ridge 回归从零）+ P9/04 Q Learning SARSA（MDP / Markov 链基础）。notes.md/solution.ipynb 用 `sklearn.Ridge(alpha=1.0)` 拟合 MMM 的 `Sales ~ Adstock(spend)`，用 pandas crosstab + `np.linalg.inv` 做 MTA 移除法。本层把"岭回归"拆成修正正规方程 $(X^TX+\alpha I)\hat\beta = X^Ty$，把"移除效应"拆成吸收马尔可夫链的基础矩阵 $N=(I-Q)^{-1}$ 与吸收概率 $B=NR$--让"为什么 Ridge 比 OLS 稳"和"移除渠道后转化率怎么算"不再是 sklearn/pandas 的黑箱。

## core_algorithm

**MMM 岭回归**。MMM 模型为 $\text{Sales}_t = \text{Base} + \sum_i \beta_i \cdot \text{Adstock}(\text{Spend}_{i,t}, \lambda_i) + \varepsilon_t$，其中 Adstock 递推 $\text{Adstock}_t = \text{Spend}_t + \lambda \cdot \text{Adstock}_{t-1}$（$\lambda$=衰减率，Search ~0.2，TV ~0.8）。OLS 估计 $\hat\beta = (X^TX)^{-1}X^Ty$ 在渠道共线下（搜索与社交同步投放）$X^TX$ 接近奇异，系数不稳定。Ridge 加入 L2 惩罚 $\alpha\|\beta\|^2$，目标变为：

$$\hat\beta_{\text{ridge}} = \arg\min_\beta \|y - X\beta\|^2 + \alpha\|\beta\|^2$$

对 $\beta$ 求梯度令其为零，得修正正规方程：

$$(X^TX + \alpha I)\hat\beta = X^Ty \implies \hat\beta = (X^TX + \alpha I)^{-1}X^Ty$$

$\alpha I$ 加到对角使矩阵恒可逆（正定），系数被拉向零--这是 notes.md "Ridge 比 OLS 稳"的数学根源。贡献分解 $C_i = |\hat\beta_i \cdot \bar X_i| / \sum_j |\hat\beta_j \cdot \bar X_j|$。

**Markov MTA 移除效应**。将用户触点路径建模为吸收马尔可夫链，状态集 = {Start, 各渠道, Conversion, Null}，转移矩阵 $P$ 行随机。将 $P$ 分块为瞬态 $Q$（渠道间转移）与吸收 $R$（到 Conv/Null）：

$$P = \begin{pmatrix} Q & R \\ 0 & I \end{pmatrix}$$

基础矩阵 $N = (I - Q)^{-1}$ 给出"从瞬态 $i$ 到瞬态 $j$ 的期望访问次数"，吸收概率 $B = NR$ 给出"从 $i$ 最终进入各吸收态的概率"。基线转化率 $= B[\text{Start}, \text{Conversion}]$。对每个渠道 $c$：将其所有出转移重定向到 Null（$P_{c,:} \to e_{\text{Null}}$），重算转化率 $r_c$，移除效应 $= (r_{\text{base}} - r_c) / r_{\text{base}}$，归一化得 MTA 功劳分配。这是 solution.ipynb TODO2 `compute_removal_effect` 的数学根源。

## code_artifact

```python
import numpy as np

def adstock(spend, decay):
    # Adstock_t = Spend_t + lambda * Adstock_{t-1}
    a = np.zeros_like(spend, dtype=float)
    a[0] = spend[0]
    for t in range(1, len(spend)):
        a[t] = spend[t] + decay * a[t-1]
    return a

def ridge_fit(X, y, alpha=1.0):
    # beta = (X^T X + alpha I)^{-1} X^T y  (alpha>0 handles multicollinearity)
    k = X.shape[1]
    return np.linalg.solve(X.T @ X + alpha * np.eye(k), X.T @ y)

def removal_effect(P, start, conv, null, channels):
    # P: row-stochastic transition matrix; returns normalized removal-effect attribution
    def cr(mat):
        tr = [s for s in range(mat.shape[0]) if s not in (conv, null)]
        Q, R = mat[np.ix_(tr, tr)], mat[np.ix_(tr, [conv, null])]
        B = np.linalg.inv(np.eye(len(tr)) - Q) @ R
        return B[tr.index(start), 0]
    base = cr(P)
    eff = {}
    for c in channels:
        Pr = P.copy(); Pr[c, :] = 0; Pr[c, null] = 1.0
        eff[c] = (base - cr(Pr)) / base
    tot = sum(eff.values())
    return {c: e / tot for c, e in eff.items()}

# verification_property:
#   ridge recovers beta at low alpha; adstock[0]=spend[0]; removal effects sum to 1.
if __name__ == "__main__":
    rng = np.random.default_rng(0)
    a = adstock(np.array([10, 20, 15, 5, 30], dtype=float), 0.5)
    assert a[0] == 10 and abs(a[1] - 25) < 0.01, "adstock recursion"
    X = rng.standard_normal((100, 3))
    bt = np.array([1.5, 1.0, 0.6])
    y = X @ bt + 0.01 * rng.standard_normal(100)
    assert np.allclose(ridge_fit(X, y, 0.01), bt, atol=0.05), "ridge recovers beta"
    P = np.array([[0,0.6,0.2,0.2],[0,0,0.5,0.5],[0,0,1,0],[0,0,0,1]])
    attr = removal_effect(P, 0, 2, 3, [1])
    assert abs(sum(attr.values()) - 1.0) < 1e-9, "removal effects normalize to 1"
```

**verification_property**: Adstock 递推正确（`a[0]=spend[0]`，`a[1]=spend[1]+decay*spend[0]`）；Ridge 在低 $\alpha$（0.01）下恢复真实系数（atol=0.05）；Markov 移除效应归一化后和为 1（功劳分配守恒）--这是 TODO2 "归一化移除效应 -> MTA 功劳分配"的数学保证。

## connection_to_unit

1. **库 vs 手写的回归求解**：solution.ipynb TODO1 用 `sklearn.Ridge(alpha=1.0).fit(X_scaled, y)` 一行拟合 MMM，from-scratch 版把求解拆成 `np.linalg.solve(X.T@X + alpha*np.eye(k), X.T@y)` 一次修正正规方程--让"alpha=1.0 加到哪"等于"加到 $X^TX$ 的对角"，而非 sklearn 隐藏的 `alpha * I`（且 sklearn 默认不缩放截距，from-scratch 版需手动处理）。
2. **Adstock 变换对比**：solution.ipynb TODO1 的 `apply_adstock` 用 Python for 循环，from-scratch 版用同样的递推但显式标注 $\lambda$ 的渠道经验值映射（Search 0.2 / Social 0.4 / Display 0.6 / Email 0.15 / TV 0.8）--让"衰减率为什么不同"等于"广告遗留效应的物理半衰期"，对应 notes.md 关键回顾 2 的渠道衰减率表。
3. **MTA 转移矩阵构建**：solution.ipynb TODO2 用 `pd.crosstab(trans_df['from'], trans_df['to'], normalize='index')` 一行算转移矩阵，from-scratch 版直接接收 $P$ 矩阵--把"从路径到转移概率"的统计步骤外化，聚焦"移除效应怎么算"的核心：$N=(I-Q)^{-1}$，$B=NR$，这是 TODO2 `compute_conversion_rate` 的数学根源。
4. **共线性诊断**：starter.ipynb TODO1 用 `Ridge(alpha=1.0)` 但不展示为什么，from-scratch 版可计算 `np.linalg.cond(X.T@X)`（条件数）--当 Search 与 Social 共线时条件数 > 30，OLS 解会爆炸，Ridge 的 $\alpha I$ 把条件数压下来。这是 notes.md "为什么用 Ridge 不用 OLS"的 from-scratch 验证。

## deep_dive_links

- [P2/13 ML Pipelines - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/13-ml-pipelines/README.md) - ML pipeline，Ridge 回归与特征工程从零，本单元 MMM 的理论锚点
- [P9/04 Q Learning SARSA - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/09-reinforcement-learning/04-q-learning-sarsa/README.md) - MDP 与 Markov 链基础，MTA 移除效应的数学根源（吸收链基础矩阵 N=(I-Q)^{-1}）

## exercises

1. 在本单元 `starter.ipynb` TODO1（sklearn `Ridge(alpha=1.0)` 拟合 MMM）运行后，用上面的 `ridge_fit` 在同一份 Adstock 变换后的特征矩阵上手动估计系数，对比 sklearn 的 `ridge.coef_` 与手写 `beta_hat`。提示：sklearn 默认对截距不正则化，from-scratch 版需手动把 $\alpha I$ 的第一个对角元置零（或不加截距列）。
2. 在本单元 `starter.ipynb` TODO2（MTA 马尔可夫移除法）运行后，用上面的 `removal_effect` 在 solution.ipynb 构建的 4 渠道转移矩阵上手动计算移除效应，对比 pandas crosstab 版的 `mta_attribution` 与手写版的归一化功劳分配。两者应数值一致（差异 < 0.01）。
3. 构造"共线性实验"：生成两个高度相关的渠道投入（`social = 0.9 * search + noise`），用 `ridge_fit(X, y, alpha=0)`（退化为 OLS）与 `alpha=1.0` 分别拟合，观察 OLS 系数的符号翻转和量级爆炸。计算 `np.linalg.cond(X.T@X)`，验证 Ridge 的 $\alpha I$ 把条件数从 > 100 压到 < 30。这是 notes.md "渠道投入高度共线"的 from-scratch 诊断。
4. TODO: 在 `practice.md` 的 DRILL-01 drill（MMM-Adstock+Ridge）中，为本 from-scratch `adstock` 添加"饱和变换"输出：`saturated = np.sqrt(adstock)`（边际递减），用 `ridge_fit` 拟合 `Sales ~ sqrt(Adstock)`，对比无饱和 vs 有饱和的 R²。这是 TODO6 预算优化中 `sqrt` 饱和效应的 from-scratch 基础。
