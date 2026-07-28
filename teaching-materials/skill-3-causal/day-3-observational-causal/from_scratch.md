# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：技能3 因果推断 · Day 3 观测数据的因果推断
> **scratch 哲学**：不调 DoWhy/econml，手写 IPW 估计器 + DML 双残差正交化，从倾向得分加权与 Frisch-Waugh-Lovell 直译到 numpy。

## scratch_topic

本单元 from-scratch 主题：**手写 IPW（逆概率加权）+ 双重机器学习（DML）估计器**。对应 rohitg00 P2 Statistics for ML（统计推断）+ P1 Convex Optimization（DML 正交化的凸优化根基）。notes.md/starter.ipynb 用 DoWhy+PSM（TODO4）与 econml/DoubleML（TODO6 选做）完成观测因果估计，本层把"倾向得分加权"与"双残差正交化"两条去偏路径都拆成可逐行审计的 numpy：手写 logistic 梯度下降估倾向得分、Hájek 稳定化 IPW、OLS 残差化 DML，让"PSM 匹配 vs IPW 加权 vs DML 正交化"三种去偏机制在同一份数据上同台对照。

## core_algorithm

**IPW（逆概率加权）**：给定倾向得分 $\hat e(X)=P(T=1|X)$，Horvitz-Thompson 估计器为

$$\hat\tau_{HT}=\frac{1}{n}\sum_i\frac{T_iY_i}{\hat e(X_i)}-\frac{1}{n}\sum_i\frac{(1-T_i)Y_i}{1-\hat e(X_i)}$$

其稳定化（Hájek）版本除以权重和，方差更小：

$$\hat\tau_{IPW}=\frac{\sum_i T_iY_i/\hat e(X_i)}{\sum_i T_i/\hat e(X_i)}-\frac{\sum_i(1-T_i)Y_i/(1-\hat e(X_i))}{\sum_i(1-T_i)/(1-\hat e(X_i))}$$

直觉：用 $1/\hat e(X)$ 把处理组重新加权为全总体分布、用 $1/(1-\hat e(X))$ 把对照组同样加权，两组共享同一 $P(X)$，从而消除可观测混杂偏差。倾向得分用手写 logistic 梯度下降估计（最小化交叉熵 $\ell=-\sum[T\log p+(1-T)\log(1-p)]$）。

**DML（双重机器学习，Chernozhukov 2018）**：先用 nuisance 模型分别拟合 $\hat\mu_Y(X)=E[Y|X]$ 与 $\hat\mu_T(X)=E[T|X]$，取残差 $\tilde Y=Y-\hat\mu_Y(X)$、$\tilde T=T-\hat\mu_T(X)$，再在残差上回归：

$$\hat\theta=\frac{\sum_i\tilde T_i\tilde Y_i}{\sum_i\tilde T_i^2}$$

由 Frisch-Waugh-Lovell 定理，$\hat\theta$ 即控制 $X$ 后 $T$ 对 $Y$ 的偏回归系数。"双重"指同时建模 $Y|X$ 与 $T|X$；"去偏"指正交化使 $\hat\theta$ 对 nuisance 估计误差不敏感（Neyman 正交性），即使 nuisance 用高维 ML 也能保持 $\sqrt{n}$ 一致性。本 from-scratch 用 OLS 作 nuisance（清晰），生产 DML 用交叉拟合（cross-fitting）消除过拟合偏差--这是 from-scratch 刻意省略、须在练习中补回的一步。关键边界：DML 放松函数形式假设，但**不放松可忽略性**，未观测混杂仍需 IV。

## code_artifact

```python
import numpy as np

def _sigmoid(z):
    return 1.0 / (1.0 + np.exp(-np.clip(z, -30, 30)))

def logistic_gd(X, T, lr=0.1, epochs=500):
    # hand-written logistic regression for propensity e(X) = P(T=1|X)
    n, d = X.shape
    w = np.zeros(d); b = 0.0
    for _ in range(epochs):
        p = _sigmoid(X @ w + b)
        w -= lr * X.T @ (p - T) / n
        b -= lr * (p - T).mean()
    return _sigmoid(X @ w + b)

def ipw_ate(T, Y, e):
    # stabilized (Hajek) IPW: reweight both groups to marginal P(X)
    w1 = T / e; w0 = (1 - T) / (1 - e)
    return (w1 * Y).sum() / w1.sum() - (w0 * Y).sum() / w0.sum()

def dml_ate(X, T, Y):
    # double ML: residualize Y and T via OLS on X, regress residuals (Frisch-Waugh-Lovell)
    Xa = np.column_stack([np.ones(len(X)), X])
    by = np.linalg.lstsq(Xa, Y, rcond=None)[0]
    bt = np.linalg.lstsq(Xa, T, rcond=None)[0]
    yr = Y - Xa @ by; tr = T - Xa @ bt
    return (tr * yr).sum() / (tr * tr).sum()

# verification_property:
#   IPW & DML recover true ATE on confounded data; naive E[Y|T=1]-E[Y|T=0] is biased.
if __name__ == "__main__":
    rng = np.random.default_rng(0)
    n = 2000
    X = rng.standard_normal((n, 1))
    T = (rng.random(n) < _sigmoid(0.5 + 1.0 * X[:, 0])).astype(float)  # X drives T (confounding)
    Y = 1.5 * T + 2.0 * X[:, 0] + 0.3 * rng.standard_normal(n)  # true ATE = 1.5
    e = logistic_gd(X, T)
    naive = Y[T == 1].mean() - Y[T == 0].mean()
    ipw = ipw_ate(T, Y, e)
    dml = dml_ate(X, T, Y)
    assert 1.2 < ipw < 1.8, f"IPW {ipw:.2f} must recover true ATE ~1.5"
    assert 1.2 < dml < 1.8, f"DML {dml:.2f} must recover true ATE ~1.5"
    assert abs(naive - 1.5) > 0.3, "naive must be biased under confounding"
```

**verification_property**: 在构造数据（X 同时驱动 T 与 Y，真实 ATE=1.5）上，IPW 与 DML 均落入 [1.2, 1.8] 恢复真值；朴素均值差因混杂偏离 1.5 超过 0.3（偏大），验证两种去偏机制有效。

## connection_to_unit

1. **DoWhy+PSM vs 手写 IPW 的去偏机制对照**：starter.ipynb TODO4 用 DoWhy+PSM（Logistic 倾向得分 + 最近邻匹配）估 ATT，from-scratch IPW 用同一 logistic 倾向得分但以 $1/\hat e(X)$ 加权而非配对--让"匹配是 IPW 的非参数版"这一定理在代码层显形：两者都把处理组与对照组的 $X$ 分布拉到同一目标，PSM 靠丢未匹配样本、IPW 靠加权保留全样本。
2. **TODO3 朴素 vs IPW/DML 的偏差数值化**：TODO3 算朴素均值差（观测对照下严重有偏），from-scratch 在同一份数据上同时输出 naive/IPW/DML 三个数，让 practice.md diagnostic Q3（PSM \$1600 / DML \$1200 / naive \$2500 哪个可信）从抽象判断变成可对照的数值实验--naive 偏大、IPW/DML 收敛到真值。
3. **TODO6 2SLS vs DML 的假设边界**：TODO6 用 statsmodels 2SLS 在 close_college 上估教育回报（IV 解决未观测混杂）；DML 是"无未观测混杂"前提下的另一条路，放松函数形式但不放松可忽略性。from-scratch DML 用 OLS nuisance 展示正交化骨架，练习里要求与 2SLS 同台对比--让 practice.md D3 feedback_rule"DML 不放松可忽略性"在代码上可证伪（构造未观测混杂看 DML 失效）。
4. **交叉拟合的刻意省略**：生产 DML（econml.LinearDML / DoubleML）用交叉拟合消除 nuisance 过拟合偏差，from-scratch 用全样本 OLS 换取清晰度--这是有意识的简化，须在练习中补回（拆 fold、hold-out 预测残差），让"库为你多做了什么"显形。

## deep_dive_links

- [P2/15 Statistics for ML - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/15-statistics-for-ml/README.md) - 统计推断：IPW 的倾向得分、Hájek 稳定化、假设检验的统计根基
- [P1/18 Convex Optimization - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/18-convex-optimization/README.md) - 凸优化：logistic 梯度下降收敛性与 DML Neyman 正交化的优化根基

## exercises

1. 在本单元 `starter.ipynb` TODO4（DoWhy+PSM）运行后，用上面的 `logistic_gd` + `ipw_ate` 在同一份 NSW+CPS 观测对照数据上估 ATT，对比 DoWhy PSM 输出。解释差异来源：PSM 丢弃未匹配样本（改变估计总体到 common support），IPW 保留全样本加权（估计 ATT 或 ATE 取决于权重归一化）。
2. 在 `practice.md` D3（DML）阶段，把 econml.LinearDML 替换为 `dml_ate`，再补一步交叉拟合：将数据分 5 折，在 4 折上拟合 OLS nuisance、在第 5 折预测残差，循环后拼回残差回归。对比交叉拟合 vs 全样本 DML 的估计差异--这就是 Chernozhukov 2018 警告的过拟合偏差。
3. 构造"违反可忽略性"场景：新增未观测变量 $U$ 同时影响 $T$ 和 $Y$（不进入 $X$），重跑 IPW/DML，观察两者都偏离真值 1.5。这是 practice.md D3 feedback_rule"DML 不放松可忽略性"的 from-scratch 反证--只有引入 IV（TODO6 的 nearc4）才能救。
4. TODO: 在 close_college（TODO6 IV 数据）上同时跑 OLS、`ipw_ate`、`dml_ate`、2SLS 四个估计，写 100 字：哪两个一致（可忽略性成立）、哪个偏离（未观测混杂）、为何 IV/2SLS 是唯一合法的。这是本单元"何时用哪个方法"决策框架的 from-scratch 验证。
