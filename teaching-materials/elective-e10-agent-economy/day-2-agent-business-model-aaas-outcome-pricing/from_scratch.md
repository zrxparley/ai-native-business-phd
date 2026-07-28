# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：选修E10 Agent经济 · Day 2 Agent商业模式+AaaS+outcome定价
> **scratch 哲学**：不调 numpy-financial 的 NPV 黑箱，手写 `price = E[loss] + risk_premium + margin`，从期望损失与风险溢价第一性原理直译到 numpy 蒙特卡洛。

## scratch_topic

本单元 from-scratch 主题：**手写 outcome-based pricing 的风险调整定价（期望损失 + 风险溢价 + 蒙特卡洛）**。对应 rohitg00 P17/02 Inference Platform Economics（推理平台经济学/定价）+ P17/27 FinOps LLMs（推理成本治理）。notes.md/starter.ipynb 用 pydantic schema 声明 `price_per_outcome` 为给定字段 + numpy-financial 算 12 月 NPV，本层把"outcome 的单价怎么定"这一步拆开：从 Agent 失败赔付的期望损失出发，手写 numpy 蒙特卡洛估计 $\mathbb{E}[\text{loss}]$ 与 $\sigma[\text{loss}]$，按均值-方差风险定价公式 `price = E[loss] + risk_premium + margin` 推出公平单价，让 outcome 定价从 NPV 黑箱变成可逐行审计的风险定价计算。

## core_algorithm

outcome-based pricing 的核心是风险调整定价。Agent 每次执行任务，成功收费 $p$，失败赔付 $L$（或免费重做消耗推理）。设单次成功概率 $\theta$、推理成本 $c$，则单次任务期望利润：

$$\mathbb{E}[\text{profit}] = \theta \cdot p + (1-\theta)\cdot(-L) - c$$

令期望利润为 0 得**盈亏平衡定价**（精算公平价）：

$$p^* = \frac{(1-\theta)\,L + c}{\theta}$$

但风险中性的 $p^*$ 不补偿波动性。在**均值-方差风险定价**框架下（Markowitz 1952），风险厌恶的 Agent 要求额外风险溢价：

$$p = \underbrace{(1-\theta)\,L}_{\mathbb{E}[\text{loss}]} + \underbrace{\lambda\,\sigma[\text{loss}]}_{\text{risk\_premium}} + \underbrace{m}_{\text{margin}} + c$$

其中损失标准差 $\sigma[\text{loss}] = \sqrt{\theta(1-\theta)}\,L$（伯努利损失方差 $\theta(1-\theta)L^2$），$\lambda$ 是风险厌恶系数（$\lambda=0$ 风险中性，$\lambda>0$ 风险厌恶，对应 CVaR/均值-方差定价族）。$\lambda$ 可由 Arrow-Pratt 风险厌恶系数 $\gamma$ 校准：$\lambda \approx \tfrac{1}{2}\gamma\,\sigma$。

**蒙特卡洛估计**：模拟 $N$ 次独立伯努利试验 $X_i \sim \text{Bernoulli}(1-\theta)$（$X_i=1$ 表失败），损失 $\ell_i = X_i \cdot L$：

$$\hat\mu = \frac{1}{N}\sum_{i=1}^N \ell_i \xrightarrow{a.s.} (1-\theta)L, \quad \hat\sigma = \sqrt{\frac{1}{N-1}\sum(\ell_i - \hat\mu)^2} \xrightarrow{a.s.} \sqrt{\theta(1-\theta)}\,L$$

由大数定律与中心极限定理，$\hat\mu$ 收敛速率 $O(1/\sqrt{N})$，95% 置信区间 $\hat\mu \pm 1.96\,\hat\sigma/\sqrt{N}$。当 $\theta$ 极端（接近 0 或 1）时方差小、风险溢价低；$\theta=0.5$ 时方差最大、风险溢价最高--这是 outcome 定价对"中等成功率 Agent 最贵"的数学解释。推理成本 $c$ 进入 break-even 公式的分子，$c \to 0$（DeepSeek V3）使 $p^* \to (1-\theta)L/\theta$，是 outcome-based pricing 在 2026 推理成本下降后可行的数学根源。

## code_artifact

```python
import numpy as np

def outcome_price_risk_adjusted(theta, loss_per_fail, reasoning_cost, lam=1.5, margin=0.5, n_mc=100000, rng=None):
    # price = E[loss] + risk_premium + margin + reasoning_cost
    # E[loss] = (1-theta)*L ; sigma[loss] = sqrt(theta*(1-theta))*L ; risk_premium = lam*sigma
    if rng is None:
        rng = np.random.default_rng(0)
    fails = rng.binomial(1, 1 - theta, size=n_mc)  # 1 = failure event
    losses = fails * loss_per_fail
    e_loss = losses.mean()
    sigma_loss = losses.std(ddof=1)
    risk_premium = lam * sigma_loss
    price = e_loss + risk_premium + margin + reasoning_cost
    return {"price": price, "e_loss": e_loss, "sigma_loss": sigma_loss,
            "risk_premium": risk_premium,
            "break_even_price": ((1 - theta) * loss_per_fail + reasoning_cost) / theta}

# verification_property:
#   risk-neutral (lam=0): price -> E[loss] + margin + cost ; MC e_loss -> (1-theta)*L (Law of Large Numbers)
#   higher theta -> lower price ; higher lam -> higher risk_premium ; break_even closed form matches
if __name__ == "__main__":
    r = outcome_price_risk_adjusted(theta=0.85, loss_per_fail=10.0, reasoning_cost=0.005, lam=0.0, margin=0.5)
    assert abs(r["e_loss"] - 1.5) < 0.05, f"E[loss]~(1-0.85)*10=1.5, got {r['e_loss']:.3f}"
    assert abs(r["price"] - (1.5 + 0.0 + 0.5 + 0.005)) < 0.06, "risk-neutral price = E[loss]+margin+cost"
    r2 = outcome_price_risk_adjusted(theta=0.85, loss_per_fail=10.0, reasoning_cost=0.005, lam=2.0, margin=0.5)
    assert r2["price"] > r["price"], "risk-averse (lam>0) price > risk-neutral"
    assert r2["risk_premium"] > 0, "risk_premium positive for lam>0"
    assert abs(r["break_even_price"] - 1.7706) < 0.01, "break-even: ((1-0.85)*10+0.005)/0.85=1.7706"
```

**verification_property**: 风险中性（$\lambda=0$）时 `price = E[loss] + margin + cost` 且蒙特卡洛 $\hat\mu \to (1-\theta)L$（大数定律，$\theta=0.85, L=10 \Rightarrow \mathbb{E}[\text{loss}]=1.5$，误差 <0.05）；风险厌恶（$\lambda=2.0$）时 `price > risk-neutral price` 且 `risk_premium > 0`；break-even 闭式 $p^* = ((1-\theta)L+c)/\theta = 1.7706$ 与公式一致。

## connection_to_unit

1. **NPV 折现 vs 单价推导**：solution.ipynb TODO3 用 `npf.npv(rate, cashflows)` 把给定的 `price_per_outcome=$10` 折现成 12 月 NPV--这是**财务折现工具**，不是定价模型。from-scratch 在 NPV 之前先推导 `price_per_outcome` 应该是多少（从 $\theta, L, \lambda$ 出发），两者是串联关系：from-scratch 定单价，NPV 折现现金流。solution 把"单价"当输入，from-scratch 把"单价"当输出。
2. **pydantic schema 的字段来源**：notes.md 的 `OutcomeBasedPricing` pydantic schema 把 `price_per_outcome` 声明为 `Field(gt=0)` 的给定字段（验证非负即可），from-scratch 显示这个字段应该由 $\theta$（成功率）、$L$（失败赔付）、$\lambda$（风险厌恶）**推导**而来。schema 验证契约的合法性，from-scratch 推导契约的公平性--API Economy 2.0 的 Agent 可发现能力声明应包含风险参数，不只是价格。
3. **弹性定价 vs 成本加风险定价**：TODO4 的 statsmodels log-log OLS 从**需求侧**找最优定价（弹性 $\epsilon$，Lerner 公式 $p_{opt} = \epsilon \cdot MC/(\epsilon-1)$），from-scratch 从**成本+风险侧**找公平定价。两者是定价的两面：需求侧回答"市场愿付多少"，成本+风险侧回答"Agent 不亏的底线"。合并两者（取 max 或加权）才是完整定价决策。
4. **推理成本敏感度的闭式解**：notes.md TODO5 把推理成本当滑块（GPT-4o \$5/1M vs DeepSeek V3 \$0.27/1M）做数值对比，from-scratch 给出闭式敏感度 $dp^*/dc = 1/\theta$。在 $\theta=0.85$ 时，推理成本从 \$0.005 降到 \$0.00027，break-even price 下降 $\Delta c/\theta = 0.00473/0.85 = \$0.00556$--这是 outcome-based pricing 在 DeepSeek V3 后利润率改善的数学根源，比数值滑块更可解释。

## deep_dive_links

- [P17/02 Inference Platform Economics - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/17-infrastructure-and-production/02-inference-platform-economics/README.md) - 推理平台经济学（定价/成本结构/盈亏平衡），本单元 from-scratch 的理论锚点
- [P17/27 FinOps LLMs - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/17-infrastructure-and-production/27-finops-llms/README.md) - LLM FinOps（推理成本治理与定价策略）

## exercises

1. 在本单元 `starter.ipynb` TODO3（三模式 12 月 NPV/IRR）运行后，用 `outcome_price_risk_adjusted` 重新推导 outcome-based 的 `price_per_outcome`：代入 notes.md 营销场景的 $\theta=0.85$（成功转化率）、$L=\$10$（失败重做成本）、推理成本 GPT-4o \$0.005/次、$\lambda=1.5$。用推出的价格重算 12 月 NPV，对比 solution.ipynb 直接用 \$10/转化 的 NPV，判断 \$10 是否高于风险调整公平价（提示：若 \$10 > 公平价，Agent 有超额利润，竞争会压价）。
2. $\theta$ 敏感性实验：令 $\theta = 0.7, 0.8, 0.9, 0.95, 0.99$，画 `price` 与 `break_even_price` 随 $\theta$ 的曲线，验证 $\theta \to 1$ 时 `price → margin + cost`（风险消失，只剩边际）。找出 outcome-based 定价可行的最低 $\theta$ 阈值（即 price < 客户愿付价格的最大失败率），这与 notes.md "outcome-based 五实施条件"的"风险可控"条件量化对接。
3. 蒙特卡洛收敛实验：令 `n_mc = 1000, 10000, 100000, 1000000`，记录 $|\hat\mu - 1.5|$（真实 $\mathbb{E}[\text{loss}]=1.5$），画 log-log 图验证 $O(1/\sqrt{N})$ 收敛速率（斜率应为 -0.5）。这与 practice.md D2-npv-irr 的"NPV 误差 <5%" mastery 阈值呼应--蒙特卡洛样本量决定定价误差。
4. TODO: 在 `practice.md` D2-npv-irr drill 的阶段C（Devin + DeepSeek V3 重算）中，用 from-scratch 的闭式 break-even $p^* = ((1-\theta)L+c)/\theta$ 计算推理成本从 GPT-4o（\$0.005/次）降到 DeepSeek V3（\$0.00027/次）时 break-even price 的下降幅度 $\Delta p^* = \Delta c / \theta$，写出利润率变化百分比。对比蒙特卡洛验证（用 `outcome_price_risk_adjusted` 跑两次取差），验证闭式解与 MC 估计一致。
