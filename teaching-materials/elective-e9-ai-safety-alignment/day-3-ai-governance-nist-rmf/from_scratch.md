# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：选修E9 AI安全与对齐 · Day 3 AI治理与NIST RMF
> **scratch 哲学**：不调 pydantic/pandas/governance SDK，手写加权风险函数 + 风险矩阵聚合，从加权均值与 likelihood-impact 矩阵直译到 numpy。

## scratch_topic

本单元 from-scratch 主题：**手写 NIST RMF 风险评分聚合（加权风险函数 + 风险矩阵）**。对应 rohitg00 P18/24 Regulatory Frameworks + P18/18 Frontier Safety Frameworks。notes.md/starter.ipynb 用 pydantic 定义控制项 schema + pandas 构建治理台账，本层把"合规扫描器"的**评分聚合数学**拆开：从加权均值推导函数内控制项聚合、跨函数加权聚合，再到 likelihood-impact 风险矩阵的乘积模型与 composite 融合，让"治理分数 70 分"不再是 pydantic 黑箱，而是可逐层审计的加权计算。

## core_algorithm

NIST AI RMF 的合规评分本质是**两层加权均值 + 风险矩阵融合**。第一层：函数内控制项聚合。设函数 $f$（Govern/Map/Measure/Manage）含 $n_f$ 个控制项，每项有分数 $s_i \in [0,100]$ 与权重 $w_i$，函数级风险为加权均值：

$$R_f = \frac{\sum_{i \in f} w_i \cdot s_i}{\sum_{i \in f} w_i}$$

加权均值的性质：$R_f \in [\min_i s_i, \max_i s_i]$（有界性），且当某 $w_i \to \infty$ 时 $R_f \to s_i$（主导性）。这让"哪个控制项权重最大"成为可审计的治理决策，而非 pydantic schema 的隐藏默认值。

第二层：跨函数聚合。NIST RMF 四函数各有权重 $W_f$（Govern 0.30 / Map 0.20 / Measure 0.30 / Manage 0.20，反映 Govern 贯穿全过程且 Measure 度量核心）：

$$R_{\text{control}} = \frac{\sum_{f} W_f \cdot R_f}{\sum_{f} W_f}$$

风险矩阵用 likelihood $\times$ impact 乘积模型，$L, I \in \{1,2,3,4,5\}$：

$$R_{\text{matrix}} = L \times I \in [1, 25]$$

对应 5×5 矩阵，风险分级阈值：Low $[1,4]$ / Medium $[5,9]$ / High $[10,14]$ / Critical $[15,25]$。composite 融合控制分与矩阵分（归一化到 $[0,100]$）：

$$R_{\text{composite}} = \alpha \cdot R_{\text{control}} + (1 - \alpha) \cdot \frac{R_{\text{matrix}}}{25} \times 100$$

$\alpha$ 控制控制合规分与情境风险分的权重比：$\alpha \to 1$ 信任控制项评分，$\alpha \to 0$ 信任 likelihood-impact 情境评估。关键洞察：加权均值的"有界性"保证 $R_{\text{control}}$ 不会因单个高分控制项而虚高，而风险矩阵的"乘积性"使得 High likelihood + High impact 必然 Critical--两者融合避免"控制分高就安全"的虚假安全感。

## code_artifact

```python
import numpy as np

# NIST RMF 4-function weights: Govern(0.3) Map(0.2) Measure(0.3) Manage(0.2)
FUNC_W = np.array([0.30, 0.20, 0.30, 0.20])
# 5x5 risk matrix: rows=likelihood(1-5), cols=impact(1-5), values=L*I
RISK_MATRIX = np.array([
    [1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15],
    [4, 8, 12, 16, 20], [5, 10, 15, 20, 25],
])

def risk_level(score):
    if score <= 4: return "Low"
    elif score <= 9: return "Medium"
    elif score <= 14: return "High"
    else: return "Critical"

def weighted_control_score(scores, weights):
    # R_f = sum(w_i * s_i) / sum(w_i)
    s = np.asarray(scores, dtype=float)
    w = np.asarray(weights, dtype=float)
    return float(np.sum(w * s) / np.sum(w))

def nist_rmf_aggregate(func_scores, func_weights=None):
    # R_control = sum(W_f * R_f) / sum(W_f) across 4 functions
    fs = np.asarray(func_scores, dtype=float)
    fw = func_weights if func_weights is not None else FUNC_W
    return float(np.sum(fw * fs) / np.sum(fw))

def matrix_risk(likelihood, impact):
    return int(RISK_MATRIX[likelihood - 1, impact - 1])

def composite_risk(control_scores, weights, likelihood, impact, alpha=0.6):
    rc = weighted_control_score(control_scores, weights)
    rm = matrix_risk(likelihood, impact)
    rm_norm = rm / 25.0 * 100
    return alpha * rc + (1 - alpha) * rm_norm, risk_level(rm)

# verification_property:
#   weighted_control_score bounded in [min,max] of inputs;
#   matrix_risk(1,1)=1, matrix_risk(5,5)=25; risk_level monotonic;
#   nist_rmf_aggregate is weighted mean (within [min,max]);
#   composite blends control score with normalized matrix risk
if __name__ == "__main__":
    gov_scores = [80, 60, 90, 70, 50]
    gov_weights = [0.3, 0.2, 0.2, 0.2, 0.1]
    rc = weighted_control_score(gov_scores, gov_weights)
    assert 60 < rc < 80, f"weighted score {rc:.1f} must be in (60,80)"
    assert matrix_risk(1, 1) == 1 and matrix_risk(5, 5) == 25
    assert risk_level(3) == "Low" and risk_level(25) == "Critical"
    fscores = [70, 60, 80, 65]
    rt = nist_rmf_aggregate(fscores)
    assert 60 < rt < 80, f"aggregate {rt:.1f} must be weighted mean in (60,80)"
    comp, lvl = composite_risk(gov_scores, gov_weights, likelihood=4, impact=3)
    assert 0 <= comp <= 100
```

**verification_property**: 加权控制分有界于 $[\min s_i, \max s_i]$；风险矩阵 `matrix_risk(1,1)=1` 且 `matrix_risk(5,5)=25`；`risk_level` 单调（Low<Medium<High<Critical）；`nist_rmf_aggregate` 为加权均值（落输入区间内）；composite 融合控制分与归一化矩阵分到 $[0,100]$。

## connection_to_unit

1. **pydantic schema vs 数学透明**：starter.ipynb TODO1 用 `ControlItem(BaseModel)` 定义控制项 schema（id/function/score），TODO3 的 `assess_control` 返回 score，from-scratch 版把"score 怎么聚合"拆开--`weighted_control_score` 让 $R_f = \sum w_i s_i / \sum w_i$ 的加权逻辑逐行可审计，而 pydantic 版把聚合藏在 `scan_nist_rmf` 的循环里。
2. **pandas 台账 vs 风险矩阵**：starter.ipynb TODO5 用 pandas 构建治理台账（用例清单/风险分级/控制措施），from-scratch 版的 `RISK_MATRIX` + `matrix_risk` 补上**情境风险评估**的数学底座--pandas 台账记录"风险等级"标签，from-scratch 版展示 likelihood×impact 乘积模型如何把标签算出来，让"High 风险"有数值依据。
3. **三框架分级 vs composite 融合**：notes.md 关键回顾 2 的 EU AI Act 4 级分级（禁止/高风险/有限/最小）是**法律标签**，from-scratch 版的 `composite_risk` 把控制合规分与情境风险分融合为连续分数--这让"高风险用例是否可降级为有限风险"有量化依据（$\alpha$ 调节控制分 vs 情境分的权重），而非 pydantic 的二值枚举判定。
4. **Govern 权重的治理含义**：notes.md 关键回顾 1 说"Govern 贯穿全过程而非第一步"，from-scratch 版的 `FUNC_W=[0.30,0.20,0.30,0.20]` 把这一论断编码为数值--Govern 权重 0.30 高于 Map/Manage 的 0.20，`nist_rmf_aggregate` 的加权均值让 Govern 的低分会拉低总分，数学上体现"治理失败拉低整体合规"的治理哲学。

## deep_dive_links

- [P18/24 Regulatory Frameworks EU US UK Korea - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/18-ethics-safety-alignment/24-regulatory-frameworks-eu-us-uk-korea/README.md) - 监管框架：NIST/EU/中国三框架的风险分级逻辑，本 from-scratch 加权聚合的框架锚点
- [P18/18 Frontier Safety Frameworks RSP PF FSF - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/18-ethics-safety-alignment/18-frontier-safety-frameworks-rsp-pf-fsf/README.md) - 前沿安全框架：RSP(preparedness)/PF(policy)/FSF(frontier)的风险评估方法论

## exercises

1. 在本单元 `starter.ipynb` TODO3（`scan_nist_rmf` 合规扫描器）运行后，用 `nist_rmf_aggregate` 对同一组 9 个营销 AI 用例的 4 函数分数做加权聚合，对比 pydantic 版 `scan_nist_rmf` 输出的总分。解释：两者聚合方式是否一致？若不一致，差异来自加权还是归一化？
2. 将 `composite_risk` 的 `alpha` 从 0.0 扫到 1.0，在 3 个营销用例（AI文案生成/AI动态定价/AI深度合成）上绘制 composite 分数随 alpha 的变化。解释：alpha 为何等价于"控制合规分 vs 情境风险分"的信任权重？哪个用例对 alpha 最敏感？与 notes.md 关键回顾 2 的 EU AI Act 分级对照。
3. 构造"Govern 失败"场景：令 Govern 函数的所有控制项 score=20（治理委员会未设立），其他函数保持 80。验证 `nist_rmf_aggregate` 因 Govern 权重 0.30 而显著下降。讨论：加权均值的"有界性"是否让单个函数失败的影响被稀释？这是否符合 notes.md "Govern 贯穿全过程"的治理哲学？
4. TODO: 在 `practice.md` 的 NIST 控制项评估练习基础上，为它添加 `composite_risk` 计算：给定用例的控制项分数与 likelihood/impact 评估，输出 composite 分数与 risk_level。把 TODO5 的 pandas 台账从"风险等级标签"升级为"composite 分数 + 标签"，让治理台账有量化深度。
