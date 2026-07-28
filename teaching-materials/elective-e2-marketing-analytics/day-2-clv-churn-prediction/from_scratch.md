# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：选修E2 营销分析 · Day 2 CLV 与流失预测
> **scratch 哲学**：不调 sklearn.LogisticRegression、不调 lifetimes.BetaGeoFitter，手写 sigmoid 梯度下降 + BG/NBD 生存公式，从对数似然梯度直译到 numpy。

## scratch_topic

本单元 from-scratch 主题：**手写逻辑回归梯度下降 + BG/NBD 简化 CLV**。对应 rohitg00 P2/03 Logistic Regression（sigmoid + 梯度下降从零）+ P2/10 Bias Variance（正则化与泛化）。notes.md/solution.ipynb 用 `sklearn.LogisticRegression(class_weight='balanced')` 一行训练流失模型，用简化公式 `F × retention^12 × AOV × 12 × discount` 计算 BG/NBD CLV。本层把"训练"拆成梯度上升循环、把"生存概率"拆成几何分布存活函数--让"流失概率怎么算"和"CLV 怎么贴现"不再是 sklearn/lifetimes 的黑箱。

## core_algorithm

**逻辑回归**是流失预测的基线模型。给定特征 $x_i \in \mathbb{R}^k$ 和标签 $y_i \in \{0,1\}$，模型假设：

$$P(y_i=1 \mid x_i) = \sigma(w^Tx_i) = \frac{1}{1+e^{-w^Tx_i}}$$

对数似然为 $\ell(w) = \sum_i [y_i \log \sigma(w^Tx_i) + (1-y_i)\log(1-\sigma(w^Tx_i))]$。对 $w$ 求梯度：

$$\nabla_w \ell = \sum_i (y_i - \sigma(w^Tx_i))\,x_i = X^T(y - \sigma(Xw))$$

梯度上升更新 $w \leftarrow w + \eta \cdot \nabla_w \ell / n$。加入 L2 正则化（对应 sklearn 的 `C` 参数）后梯度变为 $\nabla_w \ell - \lambda w$，防止共线性下权重爆炸。`class_weight='balanced'` 在 from-scratch 版用损失加权实现：少数类（流失）乘以 $n/(2 n_{pos})$，多数类乘以 $n/(2 n_{neg})$。

**BG/NBD 生存**：BG/NBD（Fader & Hardie 2005）假设客户在活跃期以 Poisson 过程购买，每次购买后以概率 $p$ 流失（Beta 分布）。简化版用几何存活函数 $P(\text{alive after } t \text{ periods}) = r^t$（$r$ = 留存率），未来 $t$ 期期望购买次数为 $F \cdot r^t$。CLV 贴现：

$$\text{CLV} = \sum_{\tau=1}^{T} \frac{r^\tau \cdot \text{AOV} \cdot F_{\text{annual}}}{(1+d)^\tau} \approx F \cdot r^T \cdot \text{AOV} \cdot T \cdot \delta$$

其中 $\delta = 1/(1+d)$ 为月贴现因子。这是 solution.ipynb TODO3 的 `bg_nbd_clv = F * retention^12 * AOV * 12 * discount` 的数学根源--$r^{12}$ 是 12 个月存活概率，$\delta$ 是月贴现。完整 BG/NBD 的似然函数涉及 Beta-Geometric 与 Negative Binomial 的卷积，from-scratch 版保留生存+贴现的核心结构。

## code_artifact

```python
import numpy as np

def sigmoid(z):
    # numerically stable sigmoid
    return np.where(z >= 0, 1 / (1 + np.exp(-z)), np.exp(z) / (1 + np.exp(z)))

def logistic_gd(X, y, lr=0.1, n_iter=1000, l2=0.01):
    # gradient ascent on log-likelihood: w += lr * X^T (y - sigmoid(Xw)) / n
    n, k = X.shape
    w = np.zeros(k)
    for _ in range(n_iter):
        grad = X.T @ (y - sigmoid(X @ w)) - l2 * w
        w += lr * grad / n
    return w

def bg_nbd_clv(F, retention, aov, months=12, discount=0.99):
    # simplified BG/NBD: future_freq * survival^months * AOV * months * discount
    # P(alive after t periods) = retention^t (geometric survival)
    future_freq = np.asarray(F, dtype=float)
    survival = retention ** months
    return future_freq * survival * aov * months * discount

# verification_property:
#   logistic_gd recovers separable structure (accuracy > 0.9);
#   bg_nbd_clv monotone increasing in retention and F.
if __name__ == "__main__":
    rng = np.random.default_rng(0)
    n = 200
    X = np.column_stack([np.ones(n), rng.standard_normal((n, 2))])
    w_true = np.array([-1.0, 2.0, -1.5])
    p = sigmoid(X @ w_true)
    y = (rng.random(n) < p).astype(float)
    w_hat = logistic_gd(X, y, lr=0.5, n_iter=2000, l2=0.001)
    acc = ((sigmoid(X @ w_hat) > 0.5) == y).mean()
    assert acc > 0.9, f"logistic_gd accuracy {acc:.2f} must be > 0.9"
    clv_low = bg_nbd_clv(F=2, retention=0.5, aov=100, months=12, discount=0.99)
    clv_high = bg_nbd_clv(F=2, retention=0.9, aov=100, months=12, discount=0.99)
    assert clv_high > clv_low, "higher retention must yield higher CLV"
```

**verification_property**: 逻辑回归梯度下降在可分数据上准确率 > 0.9（恢复真实决策边界）；BG/NBD CLV 对留存率单调递增（`clv_high( r=0.9 ) > clv_low( r=0.5 )`），对频率 F 单调递增--这是 CLV × 流失四象限行动矩阵（TODO6）的数学基础。

## connection_to_unit

1. **库 vs 手写的训练循环**：solution.ipynb TODO4 用 `LogisticRegression(class_weight='balanced', max_iter=2000).fit(X_train_scaled, y_train)` 一行训练，from-scratch 版把训练拆成 2000 次梯度上升循环 `w += lr * X^T(y - sigmoid(Xw)) / n`--让"max_iter=2000"和"lr"如何影响收敛可见，而非 sklearn 隐藏的 L-BFGS 求解器。
2. **正则化对比**：sklearn 的 `C` 参数是 L2 正则化的倒数（`C=1/λ`），from-scratch 版直接用 `l2` 系数乘以 `w` 加入梯度--让"正则化防过拟合"等于"每步把权重拉向零"，对应 notes.md 关键回顾 2 的 BG/NBD 假设违背讨论（高频客户单笔金额更低时需正则防系数爆炸）。
3. **BG/NBD 简化 vs 完整**：solution.ipynb TODO3 用 `F * retention^12 * AOV * 12 * discount` 一行算 CLV，from-scratch 版把 `retention^12` 显式标注为"几何存活函数 $P(\text{alive after 12 months}) = r^{12}$"--让 notes.md "Poisson 购买 + Beta 流失"两大假设的简化痕迹可见，完整 BG/NBD 的似然函数是 Beta-Geometric 与 NB 的卷积，from-scratch 版保留生存+贴现骨架。
4. **AUC 与不平衡评估**：starter.ipynb TODO4 用 `roc_auc_score(y_test, y_prob)` 一行算 AUC，from-scratch 版可直接用 `sigmoid(X @ w)` 的概率输出，手算 ROC 曲线（按概率排序，扫阈值算 TPR/FPR）--让"AUC > 0.80 是工业门槛"等于"ROC 曲线下面积"，而非 sklearn 的黑箱指标。

## deep_dive_links

- [P2/03 Logistic Regression - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/03-logistic-regression/README.md) - 逻辑回归 from scratch，sigmoid + 梯度下降 + 极大似然，本单元流失预测的理论锚点
- [P2/10 Bias Variance - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/10-bias-variance/README.md) - 偏差-方差分解，正则化与泛化的数学基础

## exercises

1. 在本单元 `starter.ipynb` TODO4（sklearn `LogisticRegression(class_weight='balanced')` 训练流失模型）运行后，用上面的 `logistic_gd` 在同一份 NSW 特征矩阵上手动训练，对比 sklearn 的 AUC-ROC 与手写版的准确率。提示：sklearn 用 L-BFGS（二阶），手写版用 vanilla 梯度上升（一阶），需调 `lr` 和 `n_iter` 才能收敛到相近 AUC ~0.54（RCT 数据下接近随机）。
2. 将 `bg_nbd_clv` 从简化版扩展到完整贴现和：实现 $\text{CLV} = \sum_{\tau=1}^{12} \frac{r^\tau \cdot \text{AOV} \cdot F/12}{(1+d)^\tau}$（月度贴现求和），对比 solution.ipynb TODO3 的 `F * retention^12 * AOV * 12 * discount` 一次性公式。观察两者在 `retention=0.5` vs `retention=0.9` 下的差异--简化版高估还是低估？
3. 实现手写 AUC-ROC：用 `logistic_gd` 输出的概率 `sigmoid(X @ w)`，按概率降序排列，扫阈值计算 TPR/FPR 对，用梯形法积分得 AUC。对比 `sklearn.metrics.roc_auc_score`，两者应数值一致（差异 < 0.01）。这是 TODO4 `roc_auc_score` 的 from-scratch 版本。
4. TODO: 在 `practice.md` 的 D5-SKLEARN drill 中，为本 from-scratch `logistic_gd` 添加 `class_weight='balanced'` 的损失加权实现：少数类（churn=1）梯度乘以 `n/(2*n_pos)`，多数类乘以 `n/(2*n_neg)`。观察加权前后 AUC 与 Precision/Recall 的变化，解释为什么 NSW 流失率 ~20% 下加权对 Recall 影响显著。
