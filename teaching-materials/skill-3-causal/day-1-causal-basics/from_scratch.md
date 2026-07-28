# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：技能3 因果推断 · Day 1 因果基础
> **scratch 哲学**：不调 DoWhy，手写后门调整估计器，从 do-演算公式直译到 numpy。

## scratch_topic

本单元 from-scratch 主题：**手写后门调整（backdoor adjustment）估计器**。对应 rohitg00 P2 Model Evaluation（相关 vs 因果边界）+ P1 Graph Theory（DAG 与 d-分离）。notes.md 用 DoWhy 完成"建模->识别->估计->反驳"四步，本层把"估计"这一步拆开：从 Pearl 的 do-演算后门公式出发，手写 numpy 实现后门调整 ATE 估计，让"控制混杂因素"不再是 DoWhy 的黑箱，而是可逐行审计的数值计算。

## core_algorithm

后门调整是 Pearl 因果推断的核心识别公式。给定因果 DAG，处理变量 $T$、结果 $Y$、混杂因素集 $Z$，若 $Z$ 满足后门准则（阻断所有 $T$ 到 $Y$ 的后门路径且不含 $T$ 的后代），则干预分布可由观测分布识别：

$$P(Y=y \mid do(T=t)) = \sum_z P(Y=y \mid T=t, Z=z)\, P(Z=z)$$

由此平均处理效应 ATE 为：

$$\text{ATE} = \mathbb{E}[Y \mid do(T=1)] - \mathbb{E}[Y \mid do(T=0)] = \sum_z \big(\mathbb{E}[Y \mid T=1, Z=z] - \mathbb{E}[Y \mid T=0, Z=z]\big) P(Z=z)$$

关键洞察：朴素均值差 $\bar Y_1 - \bar Y_0$ 之所以有偏，是因为 $P(Z \mid T=1) \neq P(Z \mid T=0)$（混杂因素在两组分布不均）。后门调整用**公共的 $P(Z)$ 重新加权**，把"若处理组和对照组的 $Z$ 分布相同，效应会是多少"这个反事实量化出来。数值上，这是对 $\mathbb{E}[Y|T=t,Z=z]$ 在 $Z$ 的边缘分布上做加权平均。连续 $Z$ 需分箱或参数模型（如线性回归 $\mathbb{E}[Y|T,Z] = \beta_0 + \beta_T T + \beta_Z Z$，此时 $\hat\beta_T$ 即 ATE）；离散 $Z$ 可直接按层枚举。手写时我们用离散分箱版，让加权逻辑完全透明。

## code_artifact

```python
import numpy as np

def backdoor_adjust_ate(X, T, Y, z_cols):
    # P(y|do(t=1)) - P(y|do(t=0)) = sum_z [E[Y|T=1,z] - E[Y|T=0,z]] P(z)
    Z = X[:, z_cols]
    uniq = np.unique(Z, axis=0)
    n = len(Y)
    e1 = 0.0
    e0 = 0.0
    for z in uniq:
        mask_z = np.all(Z == z, axis=1)
        p_z = mask_z.sum() / n
        m1 = mask_z & (T == 1)
        m0 = mask_z & (T == 0)
        ey1 = Y[m1].mean() if m1.sum() > 0 else 0.0
        ey0 = Y[m0].mean() if m0.sum() > 0 else 0.0
        e1 += ey1 * p_z
        e0 += ey0 * p_z
    return e1 - e0

def naive_ate(T, Y):
    return Y[T == 1].mean() - Y[T == 0].mean()

# verification_property:
#   |backdoor_ate| <= |naive_ate| in presence of confounding (adjustment removes bias);
#   if Z is independent of T (no confounding), backdoor_ate ~= naive_ate
if __name__ == "__main__":
    rng = np.random.default_rng(0)
    n = 1000
    Z = rng.integers(0, 2, size=(n, 1))  # confounder
    T = ((rng.random(n) < (0.2 + 0.6 * Z[:, 0])).astype(int))  # Z affects T
    Y = 2.0 * T + 3.0 * Z[:, 0] + 0.5 * rng.standard_normal(n)  # true ATE = 2.0
    X = Z
    naive = naive_ate(T, Y)
    ate = backdoor_adjust_ate(X, T, Y, [0])
    assert 1.5 < ate < 2.5, f"backdoor ATE {ate:.2f} must recover true ATE ~2.0"
    assert abs(naive - ate) > 0.3, "naive must be biased vs adjusted under confounding"
```

**verification_property**: 后门调整 ATE 收敛到真实效应（构造数据 true ATE=2.0，估计应落在 [1.5, 2.5]）；在存在混杂时 `|backdoor_ate|` 与 `naive_ate` 有显著偏差（朴素估计有偏）。

## connection_to_unit

1. **库 vs 手写的颗粒度**：notes.md 用 `dowhy.CausalModel` 一行完成"识别+估计"，from-scratch 版把"估计"拆成"按 Z 分层 -> 算层内均值 -> 用 P(Z) 加权"三步，每步可单独审计；DoWhy 的 `identify_estimand` 对应这里的"选 Z"决策，`estimate_effect` 对应这里的加权求和。
2. **数据流对比**：DoWhy 要求用户声明 DAG（`graph=`），from-scratch 版直接接收 `z_cols` 索引--把"哪些是混杂"的知识外化为函数参数，迫使研究者显式回答"我控制了什么"。
3. **反事实可读性**：starter.ipynb TODO4 用 DoWhy 得到一个标量 ATE，from-scratch 版输出每层 $z$ 的贡献 `ey1-ey0` 与权重 `p_z`，能看到"哪个子人群驱动了效应"--这是 capstone day-phase-4 因果实验做异质性分析（HTE）的基础。
4. **数值稳定**：DoWhy 内部用 statsmodels/EconML，from-scratch 版用纯 numpy 均值，在层内样本为 0 时回退 0.0（生产中应报"支撑不足"而非静默），暴露了"共同支撑假设"这个常被库隐藏的前提。

## deep_dive_links

- [P2/09 Model Evaluation - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/09-model-evaluation/README.md) - 模型评估：相关 vs 因果的边界，本单元 from-scratch 的理论锚点
- [P1/21 Graph Theory - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/21-graph-theory/README.md) - 图论：DAG、d-分离、后门路径判定的数学基础

## exercises

1. 在本单元 `starter.ipynb` TODO4（DoWhy 后门调整）运行后，用上面的 `backdoor_adjust_ate` 在同一份 Lalonde/NSW 数据上手动估计 ATE，对比 DoWhy 输出，解释差异来源（提示：DoWhy 默认用线性回归估计器，本 from-scratch 用分层均值）。
2. 将 `z_cols` 从单变量扩展到多变量（如 `['age','education']`），实现连续变量的分箱后门调整：对连续 $Z$ 等宽分箱为 $k$ 个桶后套用同一公式。观察分箱数 $k$ 对估计方差的影响。
3. 构造一个"工具变量"场景：$Z$ 影响 $T$ 但不直接影响 $Y$（违反后门准则），验证此时后门调整会失效（ATE 偏离真值）。这与 TODO5 反驳检验的"安慰剂处理"思想一致--from-scratch 实现让你看到失效发生在哪一层。
4. TODO: 在 `practice.md` 的 DAG 练习中，为本 from-scratch 估计器添加"共同支撑诊断"输出（每层 $z$ 的处理组/对照组样本量），当某层样本量 < 10 时标记"支撑不足"。这是 DoWhy `refute` 之外的 from-scratch 稳健性检查。
