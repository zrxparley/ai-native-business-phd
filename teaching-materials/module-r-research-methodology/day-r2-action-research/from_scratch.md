# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：模块R · R2 行动研究（Action Research）
> **scratch 哲学**：不调 pandas/scipy，手写行动研究 KPI 螺旋追踪 + Beta-Binomial 共轭贝叶斯更新，从 Susman 螺旋的"知识累积"本质直译到 numpy。

## scratch_topic

本单元 from-scratch 主题：**手写行动研究 KPI 时序追踪 + Beta-Binomial 干预有效性贝叶斯更新**。对应 rohitg00 P14 Anthropic Workflow Patterns（迭代工作流的 plan-act-observe-reflect 同构）+ P17 Load Testing LLM APIs（KPI 量化）。notes.md/starter.ipynb 用 pandas DataFrame 建 4 轮螺旋数据、用 matplotlib 画后验演化，本层把"每轮观察如何更新干预有效的后验信念"拆开：从 Beta-Binomial 共轭公式出发，手写 numpy 实现螺旋状态机 + 后验逐轮更新，让"行动研究的知识累积"不再是 pandas 表格里的累积行，而是可逐行审计的贝叶斯推断。

## core_algorithm

行动研究的 Lewin/Kemmis 四阶段螺旋（Plan->Act->Observe->Reflect）本质上是一个**序贯贝叶斯更新过程**：每轮观察产生新证据，更新对"干预有效"这一假设的后验信念。设干预有效概率 $\theta \in [0,1]$，先验取无信息 $\theta \sim \text{Beta}(\alpha_0, \beta_0)$（默认 $\alpha_0=\beta_0=1$ 即均匀分布）。每轮 $r$ 观察干预是否有效（≥2 个 KPI 改善达阈值视为成功），得伯努利似然 $X_r \mid \theta \sim \text{Bernoulli}(\theta)$。由 Beta 是 Bernoulli/Binomial 似然的共轭先验，累积 $S_r = \sum_{k=1}^r X_k$ 次成功后，后验为：

$$\theta \mid X_{1:r} \sim \text{Beta}(\alpha_0 + S_r,\; \beta_0 + r - S_r)$$

后验均值（$\theta$ 的后验期望估计）为：

$$\hat\theta_r = \mathbb{E}[\theta \mid X_{1:r}] = \frac{\alpha_0 + S_r}{\alpha_0 + \beta_0 + r}$$

后验方差随 $r$ 增大而收缩：$\text{Var}[\theta \mid X_{1:r}] = \frac{(\alpha_0+S_r)(\beta_0+r-S_r)}{(\alpha_0+\beta_0+r)^2(\alpha_0+\beta_0+r+1)}$，体现"观察越多、信念越确定"。关键洞察：朴素频率派估计 $\hat\theta_r = S_r/r$ 在 $r$ 小时极端（$r=1, S=0$ 直接归零），而贝叶斯后验受先验平滑、更稳健--这正是 notes.md "AR 从定性反思升级为定量+定性结合"的数学底座。KPI 改善幅度 $g_{r,k} = (x_{r,k} - x_{0,k})/x_{0,k}$ 决定 $X_r$：若 $\sum_k \mathbb{1}[|g_{r,k}| \geq \tau] \geq 2$ 则 $X_r=1$。高杠杆轮次识别：$\arg\max_r \sum_k g_{r,k}$。

## code_artifact

```python
import numpy as np

# AR spiral: round 0 baseline + rounds 1-4 (decision_time_min, decision_quality, ai_usage, satisfaction)
# KPIs from real AR literature improvement bands (time -30..-60%, quality +1..2.5)
SPIRAL = [
    {"r": 0, "kpi": [45.0, 2.50, 0.20, 2.50]},   # baseline
    {"r": 1, "kpi": [36.0, 3.20, 0.45, 3.10]},
    {"r": 2, "kpi": [24.0, 4.00, 0.65, 3.80]},
    {"r": 3, "kpi": [18.0, 4.60, 0.80, 4.40]},
    {"r": 4, "kpi": [18.0, 4.80, 0.85, 4.70]},
]
TAU = 0.20  # improvement threshold per KPI

def improvement_pct(spiral, k):
    base = spiral[0]["kpi"][k]
    return [(s["kpi"][k] - base) / base for s in spiral]

def is_effective(spiral, r, tau=TAU):
    cnt = 0
    for k in range(4):
        g = (spiral[r]["kpi"][k] - spiral[0]["kpi"][k]) / spiral[0]["kpi"][k]
        if k == 0:  # decision time: lower is better -> invert sign
            g = -g
        if abs(g) >= tau:
            cnt += 1
    return 1 if cnt >= 2 else 0

def beta_binomial_update(spiral, a0=1.0, b0=1.0):
    a, b = a0, b0
    trace = [(0, a, b, a / (a + b))]
    for r in range(1, len(spiral)):
        x = is_effective(spiral, r)
        a += x
        b += (1 - x)
        trace.append((r, a, b, a / (a + b)))
    return trace

if __name__ == "__main__":
    tr = beta_binomial_update(SPIRAL)
    posterior_r4 = tr[-1][3]
    assert 0.7 < posterior_r4 < 0.95, f"posterior {posterior_r4:.3f} must reflect 4 effective rounds"
    assert tr[-1][3] > tr[1][3], "posterior must grow with more successes"
    high_lev = max(range(1, 5), key=lambda r: sum(improvement_pct(SPIRAL, k)[r] for k in range(4)))
    assert high_lev in (2, 3), f"high-leverage round {high_lev}"
```

**verification_property**: 4 轮螺旋后后验 $\hat\theta_4 \in (0.7, 0.95)$（构造数据真值锚定 4 轮有效）；后验随成功轮数单调递增（`tr[-1][3] > tr[1][3]`）；高杠杆轮次落在 round 2 或 3（KPI 改善幅度最大）。当先验改为 Beta(10,10) 时后验会被拉向 0.5，证明先验对小学本的平滑作用。

## connection_to_unit

1. **库 vs 手写的更新逻辑**：starter.ipynb TODO7 用 pandas 建 `bayesian_df` 逐行算 `alpha/(alpha+beta)`，from-scratch 版把"观察 -> 共轭更新 -> 后验"拆成 `is_effective` + `beta_binomial_update` 两步，暴露了 pandas 隐藏的"成功判定阈值 τ 如何选"这一方法论决策。
2. **频率派 vs 贝叶斯**：practice.md D4 drill 强制"用贝叶斯后验而非频率派 p-hat"，from-scratch 版 `beta_binomial_update` 让两者可直接对比：频率派 `S_r/r` 在 $r=1,S=0$ 归零（过度自信），贝叶斯 `a/(a+b)` 受先验平滑--这是 notes.md "AR 不确定性量化"的可计算证明。
3. **KPI 方向处理**：solution.ipynb 的 KPI 改善对"决策时间"（越小越好）与"质量"（越大越好）混用同一公式，from-scratch 版 `is_effective` 显式对 `k==0` 取反号，迫使研究者回答"每个 KPI 的改善方向是什么"--这是 pandas 一行 `.pct_change()` 隐藏的语义。
4. **trace 可复现**：TODO6 要求 AR trace 结构化导出，from-scratch 版 `trace` 列表本身就是可序列化的后验演化记录（round, α, β, posterior），可直接喂入 notes.md 的"可复现 AR trace 存档"。

## deep_dive_links

- [P14/12 Anthropic Workflow Patterns - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/14-agent-engineering/12-anthropic-workflow-patterns/README.md) - 迭代工作流：plan-act-observe-reflect 螺旋与 agent workflow 的迭代循环同构
- [P17/22 Load Testing LLM APIs - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/17-infrastructure-and-production/22-load-testing-llm-apis/README.md) - 负载测试：KPI 量化与阈值判定，AR 干预有效性的工程化度量

## exercises

1. 在本单元 `starter.ipynb` TODO7（贝叶斯更新）完成后，用上面的 `beta_binomial_update` 在同一份 SPIRAL 数据上重算后验，对比 pandas `bayesian_df` 的 `alpha/(alpha+beta)` 列。若两者完全一致，说明 TODO7 的共轭更新正确；若有偏差，定位是 `is_effective` 的 τ 阈值还是 KPI 方向符号问题。
2. 实现先验敏感性分析：扫描先验 $\text{Beta}(\alpha_0,\beta_0) \in \{(1,1), (2,2), (5,5), (10,10), (1,5)\}$，绘制 5 条后验演化曲线。讨论"强先验（10,10）vs 无信息先验（1,1）"在仅 2 轮观察时的后验差异--这量化了 notes.md "小样本 AR 评估的贝叶斯优势"。
3. 将 `is_effective` 的阈值 τ 从 0.20 扫描到 0.50，观察后验 $\hat\theta_4$ 如何变化。定位"τ 过高导致所有轮次判失败（后验崩溃）"的拐点--这是 practice.md D2 drill "高杠杆轮次数=0 触发 weak_loop"的连续化版本。
4. TODO: 在 `practice.md` D4 drill 中，用 from-scratch `beta_binomial_update` 替换频率派 p-hat 计算，并添加"后验 95% 置信区间"输出（用 Beta 分布的 `a/(a+b) ± 1.96*sqrt(a*b/((a+b)^2*(a+b+1)))`）。验证 D4 的"后验 P(干预有效)=0.8333"在 from-scratch 版是否复现。
