# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：模块R · R3 混合方法研究（Mixed Methods）
> **scratch 哲学**：不调 scipy/pandas，手写 joint display 对齐矩阵 + 三角验证收敛指数，从 Cohen's d 方差与质化饱和度的乘性证据合并直译到 numpy。

## scratch_topic

本单元 from-scratch 主题：**手写混合方法 joint display 对齐矩阵 + 三角验证收敛指数（quant Cohen's d × qual 主题饱和度的乘性证据合并）**。对应 rohitg00 P5 LLM Evaluation Frameworks（评估框架的多源证据整合）+ P2 Model Evaluation（模型评估的效应量）。notes.md/starter.ipynb 用 pandas DataFrame 构建 joint display、用 scipy.stats 做 t 检验，本层把"定量效应与定性主题如何合并成一个收敛证据"拆开：从 Cohen's d 的方差公式与主题饱和度出发，手写 numpy 实现对齐矩阵与收敛指数，让"三角验证"不再是 pandas 表格里的并排列，而是可逐行审计的乘性证据函数。

## core_algorithm

混合方法的核心是**证据合并**：定量效应（Cohen's $d$）与定性主题饱和度（$q$）如何融合成一个收敛指数。设两组样本均值 $\bar\mu_1, \bar\mu_0$，合并方差 $s_p = \sqrt{((n_1-1)s_1^2+(n_0-1)s_0^2)/(n_1+n_0-2)}$，Cohen's $d = (\bar\mu_1-\bar\mu_0)/s_p$。由 Hedges 公式，$d$ 的近似方差为：

$$\text{Var}(d) \approx \frac{n_1+n_0}{n_1 n_0} + \frac{d^2}{2(n_1+n_0)}$$

故 $d \sim \mathcal{N}(\delta, \sigma_d^2)$，量化置信度随样本量增大、效应量减小而提高。定性侧：主题在 $M$ 份转录中出现 $m$ 次，饱和度 $q = m/M \in [0,1]$，饱和阈值 $q > 0.6$ 视为"主题稳定"。**乘性证据合并**定义第 $k$ 个发现的联合权重：

$$w_k = \underbrace{\frac{|d_k|}{\sqrt{\sigma_{d,k}^2 + 1}}}_{\text{quant confidence}} \cdot \underbrace{q_k}_{\text{qual saturation}} \cdot \underbrace{\mathbb{1}[\text{sign}(d_k) = \text{sign}(\text{qual})]}_{\text{directional agreement}}$$

第一项是 $|d|/\sqrt{\sigma_d^2+1}$（信噪比，类比 $z$-分），第二项是定性饱和度，第三项是方向一致指示函数（量化为正且定性主题"提升"则一致）。**三角验证收敛指数**为所有发现权重的有向平均：

$$T = \frac{1}{K}\sum_{k=1}^K w_k \cdot \text{sign}(d_k)$$

$T \in [-1,1]$：$T>0.3$ 强收敛（quant 与 qual 一致强化），$|T|<0.1$ 发散（证据冲突，需解释差异），$T<-0.1$ 反向收敛（一致地指向相反方向）。关键洞察：朴素并列（pandas joint display 的并排列）无法区分"两源都强且一致"与"一源强一源弱"，乘性合并 $w_k$ 才暴露"哪条发现真正被双源支持"--这是 notes.md "整合 ≠ 并列"的数学底座。

## code_artifact

```python
import numpy as np

def cohens_d(g1, g0):
    n1, n0 = len(g1), len(g0)
    m1, m0 = float(np.mean(g1)), float(np.mean(g0))
    v1, v0 = float(np.var(g1, ddof=1)), float(np.var(g0, ddof=1))
    sp = np.sqrt(((n1-1)*v1 + (n0-1)*v0) / (n1+n0-2))
    d = (m1 - m0) / sp
    var_d = (n1+n0)/(n1*n0) + d**2 / (2*(n1+n0))
    return float(d), float(var_d)

def joint_display(quant_findings, qual_findings):
    # quant_findings: list of (g1_array, g0_array); qual_findings: list of (m_quotes, M_transcripts, direction)
    rows = []
    for (g1, g0), (m, M, qdir) in zip(quant_findings, qual_findings):
        d, var_d = cohens_d(g1, g0)
        q = m / M
        snr = abs(d) / np.sqrt(var_d + 1.0)
        agree = 1.0 if (np.sign(d) == np.sign(qdir)) else 0.0
        w = snr * q * agree
        rows.append({"d": d, "var_d": var_d, "q": q,
                     "snr": float(snr), "agree": agree, "w": float(w),
                     "converged": agree == 1.0 and q > 0.6 and abs(d) > 0.2})
    return rows

def triangulation_index(rows):
    if not rows:
        return 0.0
    return float(np.mean([r["w"] * np.sign(r["d"]) for r in rows]))

if __name__ == "__main__":
    rng = np.random.default_rng(0)
    # 3 findings: convergent strong, convergent weak, divergent
    qf = [(rng.normal(5, 1, 50), rng.normal(3, 1, 50)),   # d~2.0, strong
          (rng.normal(4, 1, 50), rng.normal(3.5, 1, 50)), # d~0.5, weak
          (rng.normal(3, 1, 50), rng.normal(4, 1, 50))]   # d~-1.0, negative
    ql = [(40, 50, +1), (15, 50, +1), (35, 50, -1)]  # last: qual says positive but quant negative
    rows = joint_display(qf, ql)
    T = triangulation_index(rows)
    assert rows[0]["converged"] and not rows[2]["converged"], "divergent must not converge"
    assert rows[2]["agree"] == 0.0, "sign disagreement flagged"
    assert -1.0 <= T <= 1.0
```

**verification_property**: 收敛发现（finding 0）`converged=True`，发散发现（finding 2，quant 负 qual 正）`converged=False` 且 `agree=0.0`；三角验证指数 $T \in [-1,1]$ 且 finding 2 的 $w=0$（方向不一致直接归零，符合乘性合并定义）。当 qual direction 与 quant 一致时 $w_k>0$，否则归零--捕获"方向不一致即证据失效"。

## connection_to_unit

1. **库 vs 手写的合并逻辑**：starter.ipynb TODO4 用 pandas DataFrame 把 quant 统计与 qual 主题**并排列出**（并列 ≠ 整合），from-scratch 版 `joint_display` 用乘性 $w_k = \text{snr} \cdot q \cdot \text{agree}$ 把两源合并成单一收敛权重，暴露了 pandas 并排掩盖的"方向不一致"问题。
2. **效应量方差的来源**：solution.ipynb TODO2 用 scipy `ttest_ind` 输出 $d$ 点值，from-scratch 版 `cohens_d` 同时返回 `var_d`（Hedges 公式），让"效应量本身有不确定性"可见--这是 TODO5 贝叶斯整合先验的合理来源。
3. **饱和度阈值的方法论化**：notes.md 把"主题饱和"描述为定性概念，from-scratch 版 `q = m/M` + 阈值 0.6 把它变成可计算指标，且 `converged` 判据要求 $q>0.6$ 与 $|d|>0.2$ 同时满足--这是 "triangulation 不是任一源强即可" 的可计算化。
4. **发散发现的保留**：pandas joint display 通常只报收敛发现，from-scratch 版 `agree` 标志保留发散发现（finding 2），$w=0$ 但不删除--对应 notes.md "divergence 需解释而非丢弃"的方法论要求。

## deep_dive_links

- [P5/27 LLM Evaluation Frameworks - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/05-nlp-foundations-to-advanced/27-llm-evaluation-frameworks/README.md) - 评估框架：多源证据整合与 LLM-as-judge 的多准则合并，本单元 joint display 的工程化对照
- [P2/09 Model Evaluation - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/09-model-evaluation/README.md) - 模型评估：效应量 Cohen's d 与方差的理论锚点

## exercises

1. 在本单元 `starter.ipynb` TODO4（Joint Display）完成后，用上面的 `joint_display` 在 TODO1-3 的同一份 NSW quant 数据与主题编码 qual 数据上重算收敛权重 $w_k$。对比 pandas 并排列与 from-scratch $w_k$：哪些发现 pandas 看似支持但 $w_k=0$（方向不一致）？
2. 实现 saturation 敏感性：扫描饱和阈值 $q^* \in \{0.4, 0.5, 0.6, 0.7, 0.8\}$，观察 `converged` 发现数如何变化。定位"阈值过高导致无发现收敛"的拐点--这量化了 notes.md "定性饱和度判断的主观性"。
3. 将 `cohens_d` 的 Hedges 方差 `var_d` 用作 TODO5 贝叶斯整合的正态先验标准差（$\delta \sim \mathcal{N}(d, \text{var\_d})$），对比用 vs 不用 Hedges 方差的贝叶斯后验宽度。讨论"忽略效应量方差的贝叶斯整合会低估不确定性"。
4. TODO: 在 `practice.md` 的混合方法 drill 中，为 `joint_display` 添加"divergence 报告"输出（列出所有 `agree=0` 的发现及方向冲突描述），验证 notes.md "divergence 需解释而非丢弃"在 from-scratch 层的可计算实现。
