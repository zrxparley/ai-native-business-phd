# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：技能4 AI驱动商业模式创新 · Day 2 价值创造机制 + 定价策略
> **scratch 哲学**：不调 statsmodels/numpy-financial/scipy.stats，手写 NPV 贴现 + OLS 正规方程 + 价格弹性 log-log 回归，从 DCF 公式 + 弹性定义直译到 numpy。

## scratch_topic

本单元 from-scratch 主题：**手写 NPV 贴现估值 + OLS 正规方程回归 + 价格弹性 log-log 估计 + outcome-based pricing 封顶模型**。对应 rohitg00 P17 Inference Platform Economics（推理经济学）+ P17 FinOps LLMs（LLM 成本）。notes.md/starter.ipynb 用 `statsmodels.OLS` 拟合"什么驱动 AI 定价"、`numpy_financial.npv` 算 NPV、`scipy.stats` 估弹性置信区间，本层把这三个金融/统计计算全部去库化：纯 numpy 手写 DCF 贴现 + 正规方程 $\hat\beta=(X^TX)^{-1}X^Ty$ + log-log 回归恢复弹性 $\epsilon$，让"NPV 为什么对折现率敏感""弹性为什么是 log-log 回归斜率"两个问题在白板级代码中显形。

## core_algorithm

AI 产品定价的核心是 NPV（净现值）与价格弹性（Price Elasticity）的联合分析。NPV 将未来现金流贴现到当前：

$$\text{NPV} = \sum_{t=0}^{T} \frac{CF_t}{(1+r)^t} = CF_0 + \frac{CF_1}{1+r} + \frac{CF_2}{(1+r)^2} + \cdots + \frac{CF_T}{(1+r)^T}$$

其中 $CF_t$ 为第 $t$ 期现金流（AI 产品中推理成本是持续负现金流），$r$ 为折现率（资本成本）。NPV 对 $r$ 的敏感度 $\frac{\partial \text{NPV}}{\partial r} = -\sum_t \frac{t \cdot CF_t}{(1+r)^{t+1}}$ --远期现金流权重更大，这是 AI 产品 J 曲线（前期亏损、后期盈利）对折现率高度敏感的数学根源。

价格弹性 $\epsilon$ 衡量需求量对价格变化的响应：

$$\epsilon = \frac{dQ/Q}{dP/P} = \frac{d\ln Q}{d\ln P}$$

在 log-log 回归模型 $\ln Q = \beta_0 + \beta_1 \ln P + u$ 中，$\hat\epsilon = \hat\beta_1$。$|\epsilon| > 1$ 为弹性需求（降价增收），$|\epsilon| < 1$ 为非弹性需求（提价增收）。OLS 估计通过正规方程求解：

$$\hat\beta = (X^TX)^{-1}X^Ty, \quad X = [\mathbf{1}, \ln P], \quad y = \ln Q$$

outcome-based pricing 模型引入价值捕获比例 $\alpha$（10%-30%）和风险封顶 Cap：

$$\text{Revenue} = \min(\alpha \cdot V \cdot R, \ \text{Cap})$$

其中 $V$ 为单位结果创造的价值，$R$ 为结果数。Cap 保护客户（成本可控），$\alpha$ 对齐供需利益--这是 Agent 经济中 outcome-based pricing 的数学骨架。

## code_artifact

```python
import numpy as np

def npv(rate, cashflows):
    # NPV = sum(CF_t / (1+r)^t), t=0 is initial investment
    t = np.arange(len(cashflows))
    return np.sum(np.array(cashflows, dtype=float) / (1 + rate) ** t)

def ols_fit(X, y):
    # beta = (X^T X)^-1 X^T y, X must include intercept column
    return np.linalg.solve(X.T @ X, X.T @ y)

def price_elasticity(prices, quantities):
    # log-log OLS: ln(Q) = b0 + b1*ln(P), elasticity = b1
    X = np.column_stack([np.ones(len(prices)), np.log(prices)])
    return ols_fit(X, np.log(quantities))[1]

def outcome_pricing(n_results, value_per_result, alpha=0.15, cap=None):
    rev = alpha * value_per_result * n_results
    return min(rev, cap) if cap is not None else rev

# verification_property:
#   NPV matches closed-form DCF; elasticity recovers true beta1 from log-log data;
#   outcome_pricing cap binds when alpha*V*R > cap
if __name__ == "__main__":
    cf = [-100, 50, 60, 70]
    val = npv(0.1, cf)
    expected = -100 + 50/1.1 + 60/1.21 + 70/1.331
    assert abs(val - expected) < 1e-6, f"NPV {val} != {expected}"
    P = np.array([1, 2, 3, 5, 8], dtype=float)
    Q = 100 * P ** (-1.5)  # true elasticity = -1.5
    eps = price_elasticity(P, Q)
    assert abs(eps - (-1.5)) < 1e-6, f"elasticity {eps} != -1.5"
    assert outcome_pricing(100, 200, alpha=0.15, cap=2500) == 2500, "cap binds"
    assert outcome_pricing(100, 200, alpha=0.15, cap=None) == 3000, "no cap"
```

**verification_property**: NPV 与闭式 DCF 公式数值一致（`|npv(r,cf) - expected| < 1e-6`）；从 $Q = 100 \cdot P^{-1.5}$ 生成的数据中 log-log 回归精确恢复弹性 $\epsilon = -1.5$；outcome-based pricing 的 Cap 在 $\alpha V R > \text{Cap}$ 时生效（返回 Cap），否则返回 $\alpha V R$。

## connection_to_unit

1. **numpy-financial vs 手写贴现**：starter.ipynb TODO3 用 `npf.npv(rate, cashflows)` 一行算 NPV，from-scratch 版用 `np.sum(cf / (1+r)**t)` 手写贴现--让"NPV = 未来现金流贴现求和"这个定义不被库函数遮蔽，能直接看到折现率 $r$ 如何通过 $(1+r)^t$ 指数衰减远期现金流。
2. **statsmodels vs 手写正规方程**：starter.ipynb TODO2 用 `sm.OLS(y, X).fit()` 拟合"什么驱动 AI 定价"，from-scratch 版用 `np.linalg.solve(X.T@X, X.T@y)` 手写正规方程--statsmodels 自动加截距项/算 R²/给 p 值，from-scratch 版只给 $\hat\beta$ 点估计，让"OLS 本质是解正规方程"这个代数事实可见。
3. **scipy.stats vs 手写 log-log 弹性**：notes.md 用 `scipy.stats` 估弹性的置信区间，from-scratch 版用 log-log OLS 只给点估计 $\hat\beta_1$--置信区间需要残差分布假设（t 分布），from-scratch 版暴露了"点估计容易、区间估计需要更多假设"这一统计推断的层次差异。
4. **outcome-based pricing 公式**：notes.md 关键回顾 3 给出 `Total Cost = min(P×R, Cap), P=α×V`，from-scratch 版的 `outcome_pricing` 直译这个公式--让 $\alpha$（价值捕获比例）和 Cap（风险封顶）两个参数的经济含义在函数签名中显形。

## deep_dive_links

- [P17/02 Inference Platform Economics - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/17-infrastructure-and-production/02-inference-platform-economics/README.md) - 推理平台经济学：NPV/ROI 计算中推理成本作为持续负现金流的建模基础，本单元 from-scratch DCF 估值的理论锚点
- [P17/27 FinOps LLMs - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/17-infrastructure-and-production/27-finops-llms/README.md) - LLM FinOps：AI 产品成本结构（推理成本占比）与定价策略的财务分析框架

## exercises

1. 在本单元 `starter.ipynb` TODO3（numpy-financial NPV）运行后，用上面的 `npv` 函数在 DeepSeek V3 训练成本 $5.576M + 5 年 API 收入流上手动计算 NPV，对比 `npf.npv` 输出（应数值一致）。改变折现率 $r = 0.08, 0.10, 0.12, 0.15$，观察 NPV 的敏感度--对应 notes.md "J 曲线效应对折现率高度敏感"。
2. 将 `price_elasticity` 应用于 starter.ipynb 的真实 AI API 定价数据（16 个模型的 input/output price），把每个模型视为一个"价格点"、假设需求量与价格成幂律关系，估计"AI API 市场的价格弹性"。讨论：真实数据点少（16 个）时点估计的可靠性问题--对应 notes.md "小样本下点估计不可靠"。
3. 为 `outcome_pricing` 添加"质量加权"版本：$\text{Revenue} = \min(\alpha \cdot V \cdot \sum_i q_i r_i, \text{Cap})$，其中 $q_i$ 为质量分数。对应 notes.md 关键回顾 3 的 `Total Cost = P × Σ(qi × ri)` 公式，观察质量权重如何改变收入分布。
4. TODO: 在 `practice.md` 的 D2 drill（NPV/IRR 计算）中，用 from-scratch `npv` 替代 `npf.npv`，并手写 IRR（二分法求 `npv(r, cf) = 0` 的根 $r$）。这是 starter.ipynb TODO3 的 from-scratch 版本，让 IRR 不依赖 numpy-financial 也能求解。
