# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：技能0 AI商业分析基础 · Day 6 研究方法论入门
> **scratch 哲学**：不调 scipy.special.logsumexp / hashlib，手写 log-sum-exp + 可复现实验指纹，从 $m+\log\sum e^{x_i-m}$ 直译到 numpy/math 骨架。

## scratch_topic

本单元 from-scratch 主题：**手写可复现实验 + 数值稳定技巧**。对应 rohitg00 P0/12 Debugging and Profiling + P1/13 Numerical Stability。notes.md/starter.ipynb 用 arxiv + pandas + networkx 做文献计量，用 OSF / FAIR / 环境锁定保障可复现性，本层把"可复现"和"数值稳定"这两个隐性工程前提拆开：手写 log-sum-exp 稳定版 + 可复现随机种子控制 + 实验指纹哈希，让"为什么 softmax 会溢出""为什么 random_state=42 能锁结果""FAIR 的 Reusable 如何技术实现"三个问题在白板级代码中显形。

## core_algorithm

**数值稳定性 -- log-sum-exp**。计算 $\log\sum_i e^{x_i}$ 时，若 $x_i$ 较大（如 $x_i = 1000$），$e^{1000}$ 溢出为 inf。稳定版先减去最大值 $m = \max_i x_i$：

$$\text{logsumexp}(x) = m + \log\sum_i e^{x_i - m}, \quad m = \max_i x_i$$

数学等价性证明：$\log\sum e^{x_i} = \log\sum e^{x_i - m + m} = \log(e^m \sum e^{x_i - m}) = m + \log\sum e^{x_i - m}$。减去 $m$ 后所有指数 $\leq 0$，$e^{x_i - m} \in (0, 1]$，不溢出。这是 softmax / 交叉熵 / 贝叶斯证据下界的通用技巧。

**稳定 softmax**：$\text{softmax}(x)_i = e^{x_i} / \sum_j e^{x_j}$，直接计算在 $x_i$ 大时溢出。稳定版：

$$\text{softmax}(x)_i = \frac{e^{x_i - m}}{\sum_j e^{x_j - m}}, \quad m = \max_i x_i$$

分子分母同减 $m$，结果不变（指数相消），但数值稳定。

**可复现实验的三大支柱**（对应 notes.md OSF / FAIR / 环境锁定）：

1. **随机种子控制**：`random.Random(seed)` 确保同 seed 产生同序列。PRNG（伪随机数生成器）是确定性算法：$x_{t+1} = f(x_t)$，种子 $x_0$ 锁定整条序列。
2. **实验指纹**：$\text{hash}(\text{seed} \| \text{data\_version} \| \text{code\_version})$ 唯一标识实验配置。from-scratch 版用 FNV-1a 哈希（无需 hashlib）：$h = (h \oplus \text{byte}) \times 16777619 \mod 2^{32}$，起始 $h = 2166136261$。
3. **环境锁定**：`requirements.txt` + `random_state=42` + Python 版本 = 可复现三件套。

## code_artifact

```python
import numpy as np
import math
import random

def naive_logsumexp(x):
    # unstable: e^1000 overflows to inf
    return math.log(sum(math.e ** xi for xi in x))

def stable_logsumexp(x):
    # m + log(sum(exp(x - m))), m = max(x) -- avoids overflow
    x = list(x)
    m = max(x)
    return m + math.log(sum(math.exp(xi - m) for xi in x))

def stable_softmax(x):
    # subtract max before exp to prevent overflow
    x = np.asarray(x, dtype=float)
    m = np.max(x)
    e = np.exp(x - m)
    return e / np.sum(e)

def reproducible_shuffle(items, seed=42):
    # same seed -> same order (PRNG determinism, reproducibility pillar)
    rng = random.Random(seed)
    items = list(items)
    rng.shuffle(items)
    return items

def fnv1a_hash(s):
    # FNV-1a hash using basic arithmetic (no hashlib) -- FAIR Reusable fingerprint
    h = 2166136261
    for ch in s:
        h = ((h ^ ord(ch)) * 16777619) % (2 ** 32)
    return format(h, '08x')

def experiment_fingerprint(seed, data_version, code_version):
    return fnv1a_hash(f"{seed}|{data_version}|{code_version}")

# verification_property:
#   stable == naive for small x; stable finite for large x; shuffle deterministic; fingerprint sensitive
if __name__ == "__main__":
    small = [1.0, 2.0, 3.0]
    assert abs(stable_logsumexp(small) - naive_logsumexp(small)) < 1e-9
    large = [1000.0, 1001.0, 1002.0]
    assert math.isfinite(stable_logsumexp(large)), "stable must not overflow"
    sm = stable_softmax(large)
    assert abs(sm.sum() - 1.0) < 1e-9 and np.all(sm > 0)
    a = reproducible_shuffle([1, 2, 3, 4, 5], seed=42)
    b = reproducible_shuffle([1, 2, 3, 4, 5], seed=42)
    assert a == b, "same seed -> same order"
    c = reproducible_shuffle([1, 2, 3, 4, 5], seed=43)
    assert a != c, "different seed differs"
    fp1 = experiment_fingerprint(42, "v1.0", "abc123")
    fp2 = experiment_fingerprint(42, "v1.0", "abc123")
    fp3 = experiment_fingerprint(42, "v1.1", "abc123")
    assert fp1 == fp2 and fp1 != fp3, "fingerprint sensitive to data version"
```

**verification_property**: stable_logsumexp 与 naive 在小 $x$ 时数值一致（atol=1e-9）；大 $x$=1000 时 stable 有限、naive 溢出；stable_softmax 行和为 1 且全正；同 seed 产生同 shuffle 序列；指纹对 data_version 敏感（v1.0 ≠ v1.1）。

## connection_to_unit

1. **arxiv API 查询 vs experiment_fingerprint**：solution.ipynb TODO1 用 `arxiv.Search(query="marketing analytics")` 查询真实论文，from-scratch 版用 `experiment_fingerprint(seed, data_version, code_version)` 给文献检索过程生成唯一指纹--notes.md 教"环境锁定 = requirements.txt + random_state=42"，from-scratch 让"锁定"可验证：同指纹 = 同配置 = 可复现。
2. **networkx 度中心性 vs stable_softmax**：solution.ipynb TODO4 用 `networkx.degree_centrality(G)` 算作者合作网络的核心节点，from-scratch 版的 `stable_softmax` 是网络分析中数值稳定的基础--当节点权重大（如核心作者合作 100+ 次），朴素 softmax 溢出，stable_softmax 保证归一化不崩。notes.md "200 节点 3303 边"的合作网络在计算注意力权重时需要这个稳定技巧。
3. **OSF 预注册 vs fnv1a_hash 锁定**：notes.md 教"OSF 预注册 = 实验前公开声明假设/样本量/分析计划"，from-scratch 版的 `fnv1a_hash` 是预注册的技术实现--将 seed + 假设 + 分析计划哈希后公开，事后无法篡改（哈希敏感于任何改动）。这是"预注册对抗 p-hacking"的工程化落地。
4. **ASReview 主动学习 vs reproducible_shuffle**：notes.md 教 ASReview 用主动学习筛文献，from-scratch 的 `reproducible_shuffle` 确保 ASReview 的随机采样可复现--ASReview 的主动学习采样策略含随机性（选最不确定的论文），固定 seed 确保两次运行筛选顺序一致，这是 FAIR "可复现"支柱的底层。

## deep_dive_links

- [P0/12 Debugging and Profiling - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/00-setup-and-tooling/12-debugging-and-profiling/README.md) - 调试与性能分析，可复现实验的工程基础
- [P1/13 Numerical Stability - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/13-numerical-stability/README.md) - 数值稳定，log-sum-exp / softmax 稳定化的数学锚点

## exercises

1. 在本单元 `starter.ipynb` TODO1（arxiv 查询）运行后，用上面的 `experiment_fingerprint` 为你的文献检索配置（query + max_results + seed）生成指纹，验证"同 seed + 同 data_version = 同指纹"，并将指纹写入 notes.md 要求的"可复现研究包"。
2. 构造"数值溢出"实验：用 `naive_logsumexp([1000, 1001, 1002])` 观察 OverflowError，再用 `stable_logsumexp` 验证稳定性；对比 Day 3 from_scratch 的 `beta_pdf` 在大 $\alpha$ 时用 `math.lgamma` 的稳定技巧，讨论两者共同原理（减最大值 / 对数域计算）。
3. 对比 `stable_softmax` 与 Day 1 from_scratch 的广播运算：验证两者在数值稳定上的等价性（都减 max before exp），讨论 notes.md "networkx 200 节点合作网络"中若用 softmax 归一化度中心性，为何必须用 stable 版。
4. TODO: 在 `practice.md` D3 的可复现研究练习中，为本 from-scratch 实现添加"环境锁定"输出：将 `random_state=42` + Python 版本 + 依赖列表（用 `fnv1a_hash` 哈希）拼接为完整指纹，对应 notes.md "requirements.txt + Dockerfile + random_state=42"三件套。
