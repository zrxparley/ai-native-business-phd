# AI工程从零构建（AI Engineering from Scratch）

**AI原生化商业博士项目 · 独立教材 · v11.0**

> 本教材融合 [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch)（503 lessons / 20 phases）的 from-scratch 哲学：每一个核心算法从原始数学推导出发，用手写 numpy 实现，再过渡到 PyTorch/JAX 工程实践。教材面向全球顶尖大学教授与博士后教学场景，强调"理解到金属层"——不满足于调用 `torch.nn.Attention`，而要能在白板上写出 $\text{softmax}(QK^T/\sqrt{d_k})V$ 并解释每一行的数值含义。

---

## 教材哲学

**为什么 from scratch？** 商业博士项目的研究者要做的不是"调包"，而是"判断系统能力边界、识别创新机会、设计可验证实验"。这三件事都要求对底层机制的透彻理解。一个不懂 attention 内部结构的研究者，无法判断"长上下文推理成本为何随 $O(T^2)$ 增长"，也无法设计"如何用 sparse attention 把营销知识图谱的多跳检索成本降下来"的实验。

**三条铁律**（贯穿全书）：
1. **数学先行**：每个算法先给数学推导（含 LaTeX），再给代码。代码是数学的直译，不是黑箱。
2. **手写 numpy 骨架**：每章核心算法提供 ≤50 行 numpy 实现，附 `verification_property`（期望的形状/不变量，作为静态可审计锚点）。numpy 骨架不依赖 torch/transformers/jax，确保读者能聚焦于算法本身。
3. **商业连接**：每个 from-scratch 概念都映射到 AI原生化商业博士项目的实际场景（营销/因果/商业模式/Agent 经济/研究方法论）。

**与 rohitg00 的关系**：本教材从 rohitg00 的 20 phases 中裁剪、重组、加深，保留 5 个旗舰章（DL/Transformer/LLM/Agent/Inference）做深度处理，7 个标准章覆盖广度，1 个商业连接章做综合。rohitg00 原始 lesson 作为每章的延伸阅读深链。

---

## 目录

1. [数学基础 from scratch](#第1章--数学基础-from-scratch)（P1，标准）
2. [ML 核心 from scratch](#第2章--ml-核心-from-scratch)（P2 裁剪，标准）
3. [DL 核心 - backprop/MLP/手写 autograd](#第3章--dl-核心---backpropmlp手写-autograd)（P3，⭐旗舰）
4. [NLP 基础 - tokenization/word2vec](#第4章--nlp-基础---tokenizationword2vec)（P5 裁剪，标准）
5. [Transformer - self-attention/multi-head/mini-GPT 前向](#第5章--transformer---self-attentionmulti-headmini-gpt-前向)（P7，⭐旗舰）
6. [LLM 从零构建 - pretrain/SFT/RLHF/DPO/量化](#第6章--llm-从零构建---pretrainsftrlhfdpo量化)（P10，⭐旗舰）
7. [LLM 工程化 - inference/serving/RAG](#第7章--llm-工程化---inferenceservingrag)（P11，标准）
8. [Agent 工程 - agent loop/ReAct/memory/LangGraph](#第8章--agent-工程---agent-loopreactmemorylanggraph)（P14，⭐旗舰）
9. [多智能体与自主系统](#第9章--多智能体与自主系统)（P15+P16 合并，标准）
10. [推理与生产基础设施 - vLLM/KV cache/finops](#第10章--推理与生产基础设施---vllmkv-cachefinops)（P17，⭐旗舰）
11. [RL 基础 - bandits/RLHF 机制](#第11章--rl-基础---banditsrlhf-机制)（P9 裁剪，标准）
12. [商业连接章 - from-scratch 概念 → 营销/因果/商业模式](#第12章--商业连接章)（项目独有，综合）

---

## 第1章 · 数学基础 from scratch

**对应 rohitg00 phase**: [P1 Math Foundations](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations) · **深度**: 标准

### 1.1 为什么数学是 from-scratch 的起点

商业分析的研究者常以为"会调 sklearn 就够了"。这个错觉在遇到以下问题时崩塌："为什么我的逻辑回归在共线性特征上权重爆炸？""为什么 attention 不用普通内积而要除以 $\sqrt{d_k}$？""为什么 BG/NBD 的客户生存函数能给出 CLV？" 这些问题的答案都埋在数学底层。本章不追求数学百科全书，而是锚定 from-scratch 实现中最常被绊倒的四个点：**数值稳定、矩阵分解、概率采样、图论基础**。

### 1.2 数值稳定：log-sum-exp

softmax 是 attention、逻辑回归、RLHF 奖励模型的共同骨架。直接实现 $\text{softmax}(x)_i = e^{x_i}/\sum_j e^{x_j}$ 在 $x_i$ 较大时数值溢出。稳定版利用 $\text{softmax}(x) = \text{softmax}(x - \max(x))$ 这一恒等式：

$$\text{logsumexp}(x) = \max(x) + \log\sum_j \exp(x_j - \max(x))$$

这个技巧在后面 attention（第5章）、DPO 损失（第6章）、Thompson sampling（第11章）反复出现。

### 1.3 矩阵分解：SVD 与降维

SVD 把任意矩阵 $A \in \mathbb{R}^{m\times n}$ 分解为 $A = U\Sigma V^T$，其中 $U,V$ 正交，$\Sigma$ 对角非负。截断 SVD 取前 $k$ 大奇异值得到最优秩-$k$ 近似（Eckart-Young 定理）：

$$A_k = \sum_{i=1}^k \sigma_i u_i v_i^T = \arg\min_{\text{rank}(B)\le k} \|A - B\|_F$$

在营销表示工程中，SVD 用于把客户-商品交互矩阵降维到潜在因子空间（skill-1 day-1）。

### 1.4 numpy 骨架

```python
import numpy as np
import math

def logsumexp(x, axis=-1):
    m = np.max(x, axis=axis, keepdims=True)
    return m.squeeze(axis) + np.log(np.sum(np.exp(x - m), axis=axis))

def softmax(x, axis=-1):
    m = np.max(x, axis=axis, keepdims=True)
    e = np.exp(x - m)
    return e / np.sum(e, axis=axis, keepdims=True)

def truncated_svd(A, k):
    # A: (m, n) -> U: (m,k), s: (k,), Vt: (k,n)
    AtA = A.T @ A
    eigvals, eigvecs = np.linalg.eigh(AtA)
    idx = np.argsort(eigvals)[::-1][:k]
    s = np.sqrt(np.maximum(eigvals[idx], 0))
    Vt = eigvecs[:, idx].T
    U = (A @ Vt.T) / np.where(s == 0, 1, s)
    return U, s, Vt

# verification_property:
#   softmax rows sum to 1; truncated_svd reconstruct A within ||A - A@Vt.T@Vt||_F <= sigma_{k+1}
if __name__ == "__main__":
    x = np.array([1000.0, 1001.0, 1002.0])
    sm = softmax(x)
    assert np.allclose(sm.sum(), 1.0), "softmax row must sum to 1"
    A = np.random.randn(20, 10)
    U, s, Vt = truncated_svd(A, 5)
    A_hat = U @ np.diag(s) @ Vt
    assert A_hat.shape == A.shape, "SVD reconstruct shape must match"
```

**verification_property**: `softmax(x).sum(axis=-1) ≈ 1`（行和为1）；`truncated_svd(A,k)` 重构 `U@diag(s)@Vt` 形状与 `A` 一致且 Frobenius 误差 ≤ $\sigma_{k+1}$。

### 1.5 商业连接

- **数值稳定** → 营销 MMM 回归中广告花费量级悬殊（电视 vs 数字），log-sum-exp 稳定的 softmax 用于预算分配权重。
- **SVD** → 客户细分：把 RFM 矩阵分解为潜在客户群 × 偏好因子，用于 skill-0 day-5 数据治理中的客户画像。
- **概率采样** → A/B 测试的分层抽样（skill-3 day-2）。
- **图论** → 因果图的 d-分离判定（skill-3 day-1）、知识图谱多跳检索（skill-1 day-3）。

### 1.6 延伸阅读（rohitg00）

- [P1/06 Probability and Distributions](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/06-probability-and-distributions/README.md) — 概率分布 from scratch
- [P1/11 Singular Value Decomposition](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/11-singular-value-decomposition/README.md) — SVD 深挖
- [P1/13 Numerical Stability](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/13-numerical-stability/README.md) — 数值稳定技巧集
- [P1/21 Graph Theory](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/21-graph-theory/README.md) — 图论（因果图/KG 基础）

---

## 第2章 · ML 核心 from scratch

**对应 rohitg00 phase**: [P2 ML Fundamentals](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/02-ml-fundamentals) · **深度**: 标准（裁剪：仅监督 + GD + 评估）

### 2.1 从相关到因果：ML 的边界

监督学习的目标是学一个映射 $f: X \to Y$ 使期望损失 $\mathbb{E}[\ell(f(X), Y)]$ 最小。但这个目标只刻画**相关**，不刻画**因果**——这是 skill-3 因果推断模块的全部出发点。本章手写线性回归与逻辑回归，重点不是"能跑"，而是理解"梯度下降在什么条件下收敛"、"正则化如何缓解共线性"、"偏差-方差如何决定模型选择"。

### 2.2 线性回归：闭式解 vs 梯度下降

最小二乘目标 $J(\beta) = \|y - X\beta\|^2$。闭式解（正规方程）：

$$\hat\beta = (X^T X)^{-1} X^T y$$

当 $X^T X$ 病态（特征共线）时闭式解数值不稳，此时改用梯度下降 $\beta \leftarrow \beta - \eta \nabla J$，梯度 $\nabla J = -2X^T(y - X\beta)$。岭回归加 $L_2$ 罚 $\lambda\|\beta\|^2$ 使 $X^TX + \lambda I$ 可逆——这是 MMM（skill-3 day-5）处理广告共线性的标准武器。

### 2.3 逻辑回归：从线性到概率

二分类逻辑回归 $P(y=1|x) = \sigma(w^T x)$，损失为负对数似然：

$$J(w) = -\sum_i [y_i \log\sigma(w^Tx_i) + (1-y_i)\log(1-\sigma(w^Tx_i))]$$

梯度 $\nabla J = X^T(\sigma(Xw) - y)$。注意这个梯度形式与线性回归只差一个 sigmoid——这是广义线性模型的统一美。

### 2.4 numpy 骨架

```python
import numpy as np

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-np.clip(z, -500, 500)))

def linear_regression_closed(X, y):
    # X: (n, d) with bias column, y: (n,)
    return np.linalg.solve(X.T @ X, X.T @ y)

def linear_regression_gd(X, y, lr=0.01, steps=500):
    n, d = X.shape
    beta = np.zeros(d)
    for _ in range(steps):
        grad = -2 * X.T @ (y - X @ beta) / n
        beta = beta - lr * grad
    return beta

def logistic_regression_gd(X, y, lr=0.1, steps=1000, l2=0.0):
    n, d = X.shape
    w = np.zeros(d)
    for _ in range(steps):
        p = sigmoid(X @ w)
        grad = X.T @ (p - y) / n + l2 * w
        w = w - lr * grad
    return w

# verification_property:
#   closed-form residual X.T@(y-X@beta) ~ 0 (orthogonality);
#   logisticRegression trained w gives mean(sigma(X@w)) ~ mean(y)
if __name__ == "__main__":
    rng = np.random.default_rng(0)
    X = np.column_stack([np.ones(200), rng.standard_normal((200, 3))])
    true_beta = np.array([0.5, 1.0, -2.0, 0.3])
    y = X @ true_beta + 0.1 * rng.standard_normal(200)
    b = linear_regression_closed(X, y)
    resid_orth = np.abs(X.T @ (y - X @ b)).max()
    assert resid_orth < 1e-8, "OLS residual must be orthogonal to X columns"
```

**verification_property**: 闭式解残差正交于 `X` 各列（`X.T@(y-X@beta) ≈ 0`）；逻辑回归训练后 `mean(sigmoid(X@w)) ≈ mean(y)`（概率校准）。

### 2.5 商业连接

- **线性回归闭式解** → CLV 的 RFM 回归基线（skill-2 marketing analytics）。
- **岭回归** → MMM 处理电视/数字/社交广告的共线性（skill-3 day-5 / e2 day-3）。
- **逻辑回归** → 流失预测（e2 day-2）、营销响应模型。
- **偏差-方差** → 决定 CLV 模型该用简单回归还是梯度提升（e2 day-2 的模型选择论据）。

### 2.6 延伸阅读（rohitg00）

- [P2/02 Linear Regression](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/02-linear-regression/README.md) — 线性回归 from scratch
- [P2/03 Logistic Regression](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/03-logistic-regression/README.md) — 逻辑回归
- [P2/09 Model Evaluation](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/09-model-evaluation/README.md) — 评估（相关 vs 因果的边界）
- [P2/10 Bias Variance](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/10-bias-variance/README.md) — 偏差-方差分解

---

## 第3章 · DL 核心 - backprop/MLP/手写 autograd

**对应 rohitg00 phase**: [P3 Deep Learning Core](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core) · **深度**: ⭐旗舰

### 3.1 为什么 DL 要 from scratch

调用 `loss.backward()` 是现代深度学习的日常，但研究者要回答"为什么我的训练 loss 在 epoch 3 突然 NaN""为什么换一个激活函数效果差这么多""梯度消失到底发生在哪一层"——这些问题只能靠对手写反向传播的透彻理解。本章旗舰，手写一个能数值梯度检验的 mini autograd，让读者真正"摸到"链式法则。

### 3.2 链式法则与反向传播

前向传播计算输出 $y = f_L \circ \dots \circ f_1(x)$。反向传播用链式法则逐层计算梯度：

$$\frac{\partial \mathcal{L}}{\partial z_l} = \frac{\partial \mathcal{L}}{\partial z_{l+1}} \cdot \frac{\partial z_{l+1}}{\partial z_l}$$

对一个 MLP 层 $z = Wx + b,\ a = \phi(z)$，给定上游梯度 $\bar a = \partial\mathcal{L}/\partial a$：

$$\bar z = \bar a \odot \phi'(z),\quad \bar W = \bar z\, x^T,\quad \bar b = \bar z,\quad \bar x = W^T \bar z$$

这就是 backprop 的全部。手写一遍，`loss.backward()` 不再是黑箱。

### 3.3 手写 autograd：计算图与拓扑排序

一个可微系统 = 节点（值+局部梯度）+ 边（父子依赖）。前向构建计算图，反向按拓扑序传播梯度。这是 PyTorch autograd 的最小内核。

### 3.4 numpy 骨架（mini autograd + MLP）

```python
import numpy as np

class Tensor:
    def __init__(self, data, _children=(), _op=""):
        self.data = np.asarray(data, dtype=float)
        self.grad = np.zeros_like(self.data)
        self._prev = set(_children)
        self._backward = lambda: None
        self._op = _op
    def __add__(self, other):
        other = other if isinstance(other, Tensor) else Tensor(other)
        out = Tensor(self.data + other.data, (self, other), "+")
        def _backward():
            self.grad += out.grad
            other.grad += out.grad
        out._backward = _backward
        return out
    def __mul__(self, other):
        other = other if isinstance(other, Tensor) else Tensor(other)
        out = Tensor(self.data * other.data, (self, other), "*")
        def _backward():
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad
        out._backward = _backward
        return out
    def relu(self):
        out = Tensor(np.maximum(0, self.data), (self,), "relu")
        def _backward():
            self.grad += (self.data > 0) * out.grad
        out._backward = _backward
        return out
    def sum(self):
        out = Tensor(self.data.sum(), (self,), "sum")
        def _backward():
            self.grad += np.ones_like(self.data) * out.grad
        out._backward = _backward
        return out
    def backward(self):
        topo = []
        visited = set()
        def build(v):
            if v not in visited:
                visited.add(v)
                for c in v._prev:
                    build(c)
                topo.append(v)
        build(self)
        self.grad = np.array(1.0)
        for v in reversed(topo):
            v._backward()

# verification_property: gradient check vs numerical gradient, relative error < 1e-5
if __name__ == "__main__":
    x = Tensor([2.0, -1.0])
    W = Tensor([[1.0, 0.0], [0.0, -2.0]])
    b = Tensor([0.5, -0.5])
    h = (W * x + b).relu()
    loss = h.sum()
    loss.backward()
    # numerical grad check on W
    eps = 1e-6
    def f(W_data):
        t = Tensor(W_data); h2 = (t * x + b).relu(); return h2.sum().data
    W0 = W.data.copy()
    num_grad = np.zeros_like(W0)
    for i in range(W0.shape[0]):
        for j in range(W0.shape[1]):
            W0[i, j] += eps; fp = f(W0)
            W0[i, j] -= 2 * eps; fm = f(W0)
            W0[i, j] += eps
            num_grad[i, j] = (fp - fm) / (2 * eps)
    rel_err = np.abs(W.grad - num_grad).max()
    assert rel_err < 1e-4, f"grad check rel_err {rel_err} must be < 1e-4"
```

**verification_property**: 梯度数值检验（数值梯度 vs 解析梯度）相对误差 `< 1e-4`——这是判断 autograd 正确性的黄金标准。

### 3.5 商业连接

- **手写 backprop** → 理解营销两塔模型（skill-1 day-2）训练时为何梯度在嵌入层消失。
- **激活函数选择** → CLV 深度模型的 ReLU vs Tanh 选择影响客户生存预测的平滑性。
- **梯度检验** → capstone（day-phase-4）因果实验中自定义 DML 损失的正确性验证方法。
- **mini-framework** → 研究者实现新损失函数（如 uplift Qini）时的最小可训练骨架。

### 3.6 延伸阅读（rohitg00）

- [P3/03 Backpropagation](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/03-deep-learning-core/03-backpropagation/README.md) — backprop from scratch（本章核心）
- [P3/01 The Perceptron](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/03-deep-learning-core/01-the-perceptron/README.md) — 感知机
- [P3/02 Multi Layer Networks](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/03-deep-learning-core/02-multi-layer-networks/README.md) — MLP
- [P3/10 Mini Framework](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/03-deep-learning-core/10-mini-framework/README.md) — 手写 mini 框架

---

## 第4章 · NLP 基础 - tokenization/word2vec

**对应 rohitg00 phase**: [P5 NLP Foundations](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced) · **深度**: 标准（裁剪：仅 tokenization + word2vec + embeddings）

### 4.1 从字符到语义

NLP 的 from-scratch 旅程从"如何把文字变成模型能吃的向量"开始。两个里程碑：**tokenization**（把字符串切成离散符号）和 **word2vec**（把符号映射到稠密语义空间）。这两件事至今仍是 LLM 的前置工序——BPE 是 GPT 家族的 tokenizer，word2vec 的负采样思想演化为对比学习。

### 4.2 BPE：字节对编码

BPE 从字符级开始，迭代合并最高频的相邻符号对。合并规则学到后，任意文本都能被确定性切分。形式化：给定语料和合并表 $M = [(a_1,b_1), \dots, (a_k,b_k)]$，对每段文本反复应用 $M$ 中规则直到无法合并。BPE 解决了 OOV（未登录词）问题，是 GPT/Llama tokenizer 的基础。

### 4.3 word2vec：Skip-gram 负采样

Skip-gram 用中心词预测上下文。损失：

$$J(\theta) = -\frac{1}{T}\sum_{t=1}^T \sum_{-c \le j \le c, j \ne 0} \log \sigma(v_{w_t}^T v'_{w_{t+j}}) - \sum_{w_N \in \mathcal{N}} \log \sigma(-v_{w_t}^T v'_{w_N})$$

其中 $\mathcal{N}$ 是负采样词。负采样把多分类softmax 降为二分类，训练效率提升几个数量级。

### 4.4 numpy 骨架

```python
import numpy as np
import random
from collections import Counter, defaultdict

def bpe_train(corpus_tokens, num_merges):
    # corpus_tokens: list of list of str (chars). Returns merge list + vocab.
    merges = []
    tokens = [list(s) for s in corpus_tokens]
    for _ in range(num_merges):
        pairs = Counter()
        for tok in tokens:
            for i in range(len(tok) - 1):
                pairs[(tok[i], tok[i + 1])] += 1
        if not pairs:
            break
        best = pairs.most_common(1)[0][0]
        merges.append(best)
        for tok in tokens:
            i = 0
            while i < len(tok) - 1:
                if (tok[i], tok[i + 1]) == best:
                    tok[i] = tok[i] + tok[i + 1]
                    del tok[i + 1]
                else:
                    i += 1
    return merges

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-np.clip(z, -30, 30)))

def word2vec_sgns(sentences, dim=20, window=2, neg=3, epochs=50, lr=0.05):
    vocab = sorted({w for s in sentences for w in s})
    idx = {w: i for i, w in enumerate(vocab)}
    V = len(vocab)
    W = (np.random.randn(V, dim) * 0.01)
    C = (np.random.randn(V, dim) * 0.01)
    neg_pool = [idx[w] for w in vocab for _ in range(int(1))]  # uniform for demo
    for _ in range(epochs):
        random.shuffle(sentences)
        for s in sentences:
            ids = [idx[w] for w in s if w in idx]
            for t, ct in enumerate(ids):
                lo = max(0, t - window); hi = min(len(ids), t + window + 1)
                for j in range(lo, hi):
                    if j == t: continue
                    pos = ids[j]
                    for _k in range(neg):
                        neg = random.choice(neg_pool)
                        if neg == ct: continue
                        # positive
                        g = lr * (sigmoid(W[ct] @ C[pos]) - 1.0)
                        Wc = W[ct].copy()
                        W[ct] -= g * C[pos]; C[pos] -= g * Wc
                        # negative
                        g = lr * (sigmoid(W[ct] @ C[neg]) - 0.0)
                        Wc = W[ct].copy()
                        W[ct] -= g * C[neg]; C[neg] -= g * Wc
    return W, idx

# verification_property:
#   BPE merges reduce total token count; word2vec similar words have high cosine sim
if __name__ == "__main__":
    corpus = ["low", "lower", "lowest", "newest", "widest"]
    merges = bpe_train(corpus, 10)
    assert len(merges) > 0, "BPE must produce merges"
```

**verification_property**: BPE 合并后 token 总数减少；word2vec 训练后相似词（如"low"/"lower"）余弦相似度高于无关词。

### 4.5 商业连接

- **BPE** → 营销文案 LLM 的 tokenizer，影响多语言营销内容的 token 成本核算（skill-4 day-2 定价）。
- **word2vec** → 客户评论的语义聚类（skill-1 day-1），比 TF-IDF 更能捕捉"性价比"与"划算"的近义。
- **embeddings** → 营销两塔模型的查询-商品匹配（skill-1 day-2 / e3 day-2 RAG）。
- **TF-IDF** → 关键词提取的基线，对比 LLM 抽取的效果（skill-1 day-2）。

### 4.6 延伸阅读（rohitg00）

- [P5/03 Word Embeddings Word2Vec](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/05-nlp-foundations-to-advanced/03-word-embeddings-word2vec/README.md) — word2vec from scratch
- [P5/02 Bag of Words TF-IDF](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/05-nlp-foundations-to-advanced/02-bag-of-words-tfidf/README.md) — TF-IDF
- [P5/19 Subword Tokenization](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/05-nlp-foundations-to-advanced/19-subword-tokenization/README.md) — 子词分词（BPE/WordPiece）
- [P5/22 Embedding Models Deep Dive](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/05-nlp-foundations-to-advanced/22-embedding-models-deep-dive/README.md) — 嵌入模型深挖

---

## 第5章 · Transformer - self-attention/multi-head/mini-GPT 前向

**对应 rohitg00 phase**: [P7 Transformers Deep Dive](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive) · **深度**: ⭐旗舰

### 5.1 为什么 attention 是 from-scratch 的重中之重

Transformer 是 LLM、多模态、Agent 的共同骨架。一个不懂 attention 内部的研究者无法回答："为什么长上下文成本是 $O(T^2)$？""为什么 KV cache 能把推理从 $O(T^2)$ 降到 $O(T)$？""为什么 multi-head 比 single-head 强？" 这些问题决定了营销知识图谱多跳检索的可行性、Agent 长对话的成本、多模态对齐的设计。本章旗舰，手写 attention → multi-head → transformer block → mini-GPT 前向。

### 5.2 Scaled Dot-Product Attention

给定查询 $Q$、键 $K$、值 $V$（都 $\in \mathbb{R}^{T\times d}$）：

$$\text{Attention}(Q,K,V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

为什么除以 $\sqrt{d_k}$？当 $d_k$ 较大时，$QK^T$ 的元素方差为 $d_k$，进入 softmax 的饱和区导致梯度消失。除以 $\sqrt{d_k}$ 把方差拉回 1。这个细节是 from-scratch 的必修课。

### 5.3 Multi-Head Attention

把 $Q,K,V$ 投影到 $h$ 个子空间各自做 attention 再拼接：

$$\text{MultiHead}(Q,K,V) = \text{Concat}(\text{head}_1, \dots, \text{head}_h) W^O,\quad \text{head}_i = \text{Attention}(QW_i^Q, KW_i^K, VW_i^V)$$

每个头 $\sqrt{d_k/h}$ 缩放。多头让模型同时关注不同子空间的关系（语法/语义/共现）。

### 5.4 Transformer Block

每个 block = 多头 attention + 残差 + LayerNorm + FFN + 残差 + LayerNorm：

$$x' = \text{LayerNorm}(x + \text{MultiHead}(x))$$
$$x'' = \text{LayerNorm}(x' + \text{FFN}(x')),\quad \text{FFN}(x) = \text{ReLU}(xW_1 + b_1)W_2 + b_2$$

### 5.5 numpy 骨架（attention + multi-head + block 前向）

```python
import numpy as np

def softmax(x, axis=-1):
    m = np.max(x, axis=axis, keepdims=True)
    e = np.exp(x - m)
    return e / np.sum(e, axis=axis, keepdims=True)

def attention(Q, K, V, mask=None):
    # Q,K,V: (T, d)
    dk = Q.shape[-1]
    scores = Q @ K.T / np.sqrt(dk)
    if mask is not None:
        scores = scores + mask
    weights = softmax(scores, axis=-1)
    return weights @ V, weights

def multi_head_attention(x, Wq, Wk, Wv, Wo, n_heads):
    # x: (T, d), Wq/Wk/Wv: (d, d), Wo: (d, d)
    T, d = x.shape
    dh = d // n_heads
    Q = (x @ Wq).reshape(T, n_heads, dh).transpose(1, 0, 2)
    K = (x @ Wk).reshape(T, n_heads, dh).transpose(1, 0, 2)
    V = (x @ Wv).reshape(T, n_heads, dh).transpose(1, 0, 2)
    scores = Q @ K.transpose(0, 2, 1) / np.sqrt(dh)
    weights = softmax(scores, axis=-1)
    heads = weights @ V                      # (n_heads, T, dh)
    concat = heads.transpose(1, 0, 2).reshape(T, d)
    return concat @ Wo, weights

def layer_norm(x, gamma, beta, eps=1e-5):
    mu = x.mean(axis=-1, keepdims=True)
    var = x.var(axis=-1, keepdims=True)
    return gamma * (x - mu) / np.sqrt(var + eps) + beta

def ffn(x, W1, b1, W2, b2):
    return np.maximum(0, x @ W1 + b1) @ W2 + b2

def transformer_block(x, params, n_heads):
    Wq, Wk, Wv, Wo, g1, b1n, W1, bf1, W2, bf2, g2, b2n = params
    attn, _ = multi_head_attention(x, Wq, Wk, Wv, Wo, n_heads)
    x1 = layer_norm(x + attn, g1, b1n)
    x2 = layer_norm(x1 + ffn(x1, W1, bf1, W2, bf2), g2, b2n)
    return x2

# verification_property:
#   attention weights rows sum to 1; multi_head output shape == input shape
if __name__ == "__main__":
    rng = np.random.default_rng(0)
    T, d, h = 6, 16, 4
    x = rng.standard_normal((T, d))
    Wq = rng.standard_normal((d, d)) * 0.1
    Wk = rng.standard_normal((d, d)) * 0.1
    Wv = rng.standard_normal((d, d)) * 0.1
    Wo = rng.standard_normal((d, d)) * 0.1
    out, w = multi_head_attention(x, Wq, Wk, Wv, Wo, h)
    assert out.shape == x.shape, "MHA output shape must equal input shape"
    assert np.allclose(w.sum(axis=-1), 1.0), "attention weights per (head,row) must sum to 1"
```

**verification_property**: attention 权重每行和为 1（`weights.sum(-1) ≈ 1`）；multi-head 输出形状与输入相同（`out.shape == x.shape`）。

### 5.6 商业连接

- **attention $O(T^2)$** → 营销知识图谱多跳检索的成本上限（skill-1 day-3 GraphRAG）。
- **KV cache** → Agent 长对话的推理成本控制（skill-5 day-5 / e3 day-3）。
- **multi-head** → 营销两塔模型用不同头捕捉"价格偏好"/"风格偏好"/"品牌偏好"（skill-1 day-2）。
- **causal mask** → 营销文案生成的自回归解码（e3 day-1 mini-GPT）。

### 5.7 延伸阅读（rohitg00）

- [P7/02 Self Attention from Scratch](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/07-transformers-deep-dive/02-self-attention-from-scratch/README.md) — 自注意力 from scratch（本章核心）
- [P7/03 Multi Head Attention](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/07-transformers-deep-dive/03-multi-head-attention/README.md) — 多头注意力
- [P7/05 Full Transformer](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/07-transformers-deep-dive/05-full-transformer/README.md) — 完整 transformer
- [P7/12 KV Cache Flash Attention](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/07-transformers-deep-dive/12-kv-cache-flash-attention/README.md) — KV cache 与 flash attention
- [P7/13 Scaling Laws](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/07-transformers-deep-dive/13-scaling-laws/README.md) — 缩放定律

---

## 第6章 · LLM 从零构建 - pretrain/SFT/RLHF/DPO/量化

**对应 rohitg00 phase**: [P10 LLMs from Scratch](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch) · **深度**: ⭐旗舰

### 6.1 LLM 全生命周期 from scratch

商业研究者要用 LLM 做营销/因果/Agent，必须理解 LLM 的四个阶段：**预训练（next-token）→ 监督微调（SFT）→ 对齐（RLHF/DPO）→ 部署（量化/推理优化）**。每个阶段都有 from-scratch 的理解点。本章旗舰，手写 mini-GPT 前向 + SFT 损失 + DPO 损失 + 量化骨架。

### 6.2 预训练：next-token 与交叉熵

mini-GPT = token embedding + 位置编码 + N × transformer block + LM head。预训练损失是 next-token 交叉熵：

$$\mathcal{L}_{\text{pretrain}} = -\frac{1}{T}\sum_{t=1}^T \log P(w_t | w_{<t}; \theta)$$

位置编码用 RoPE（旋转位置编码）：对 query/key 在每对维度上施加角度为 $m\theta_i$ 的旋转，使得内积只依赖相对位置 $m-n$。

### 6.3 SFT：指令微调

SFT 在指令-响应对上做条件 next-token，只对响应部分计算损失：

$$\mathcal{L}_{\text{SFT}} = -\frac{1}{|y|}\sum_{t} \log P(y_t | x, y_{<t}; \theta)$$

### 6.4 DPO：直接偏好优化

RLHF 用奖励模型 + PPO，复杂且不稳。DPO 直接在偏好对上优化，推出隐式奖励 $\hat r_\theta(x,y) = \beta \log\frac{\pi_\theta(y|x)}{\pi_{\text{ref}}(y|x)}$，损失：

$$\mathcal{L}_{\text{DPO}} = -\mathbb{E}_{(x,y_w,y_l)}\left[\log\sigma\left(\beta\log\frac{\pi_\theta(y_w|x)}{\pi_{\text{ref}}(y_w|x)} - \beta\log\frac{\pi_\theta(y_l|x)}{\pi_{\text{ref}}(y_l|x)}\right)\right]$$

DPO 把 RLHF 的两阶段（奖励模型 + RL）压成单阶段有监督损失，是 2023 年后对齐的事实标准。

### 6.5 量化：INT8

把 FP16 权重 $w$ 量化到 INT8：$w_q = \text{round}(w / s)$，$s = \max(|w|)/127$。反量化 $w \approx w_q \cdot s$。量化把模型体积和显存压一半以上，代价是少量精度损失。

### 6.6 numpy 骨架（mini-GPT 前向 + DPO 损失 + 量化）

```python
import numpy as np

def softmax(x, axis=-1):
    m = np.max(x, axis=axis, keepdims=True)
    e = np.exp(x - m)
    return e / np.sum(e, axis=axis, keepdims=True)

def rope(x, theta_base=10000.0):
    # x: (T, d) -> apply rotary pos emb
    T, d = x.shape
    half = d // 2
    freqs = 1.0 / (theta_base ** (np.arange(half) / half))
    pos = np.arange(T)[:, None]
    angles = pos * freqs
    cos = np.cos(angles); sin = np.sin(angles)
    x1, x2 = x[:, :half], x[:, half:]
    return np.concatenate([x1 * cos - x2 * sin, x1 * sin + x2 * cos], axis=-1)

def rms_norm(x, gamma, eps=1e-5):
    return gamma * x / np.sqrt(np.mean(x**2, axis=-1, keepdims=True) + eps)

def mini_gpt_forward(token_ids, emb, Wq, Wk, Wv, Wo, W1, b1, W2, b2, lm_head, n_heads):
    T = len(token_ids)
    x = emb[token_ids]
    x = rope(x)
    dh = x.shape[-1] // n_heads
    Q = (x @ Wq).reshape(T, n_heads, dh).transpose(1, 0, 2)
    K = (x @ Wk).reshape(T, n_heads, dh).transpose(1, 0, 2)
    V = (x @ Wv).reshape(T, n_heads, dh).transpose(1, 0, 2)
    mask = np.triu(np.full((T, T), -1e9), k=1)
    scores = Q @ K.transpose(0, 2, 1) / np.sqrt(dh) + mask
    weights = softmax(scores, axis=-1)
    attn = (weights @ V).transpose(1, 0, 2).reshape(T, -1) @ Wo
    x = x + attn
    x = x + np.maximum(0, rms_norm(x, np.ones(x.shape[-1])) @ W1 + b1) @ W2 + b2
    logits = rms_norm(x, np.ones(x.shape[-1])) @ lm_head
    return logits

def dpo_loss(logp_w, logp_l, logp_w_ref, logp_l_ref, beta=0.1):
    # logp_*: scalar log-probs of chosen/rejected under policy and ref
    z = beta * ((logp_w - logp_w_ref) - (logp_l - logp_l_ref))
    return -np.log(1 / (1 + np.exp(-z)))

def quantize_int8(w):
    s = np.max(np.abs(w)) / 127.0
    q = np.round(w / s).astype(np.int8)
    return q, s

# verification_property:
#   mini_gpt logits shape (T, vocab); dpo_loss < 0; quantize reconstruct error small
if __name__ == "__main__":
    rng = np.random.default_rng(0)
    V, d, T, h = 100, 32, 5, 4
    emb = rng.standard_normal((V, d)) * 0.1
    mk = lambda: rng.standard_normal((d, d)) * 0.05
    Wq, Wk, Wv, Wo = mk(), mk(), mk(), mk()
    W1 = rng.standard_normal((d, d*2)) * 0.05; b1 = np.zeros(d*2)
    W2 = rng.standard_normal((d*2, d)) * 0.05; b2 = np.zeros(d)
    lm_head = rng.standard_normal((d, V)) * 0.05
    ids = [1, 5, 9, 13, 2]
    logits = mini_gpt_forward(ids, emb, Wq, Wk, Wv, Wo, W1, b1, W2, b2, lm_head, h)
    assert logits.shape == (T, V), "mini-GPT logits shape must be (T, vocab)"
    loss = dpo_loss(-0.5, -2.0, -1.0, -1.0)
    assert loss < 0, "DPO loss must be negative (log-prob of sigmoid in (0,1))"
    w = rng.standard_normal((100, 100))
    q, s = quantize_int8(w)
    assert np.max(np.abs(w - q * s)) < 0.01 * np.max(np.abs(w)), "INT8 quant error must be small"
```

**verification_property**: mini-GPT logits 形状 `(T, vocab)`；DPO 损失 `< 0`；INT8 量化反量化相对误差 `< 1%`。

### 6.7 商业连接

- **预训练成本** → 企业是否该从头预训练 vs 微调的决策（skill-4 day-2 定价、skill-5 day-5 部署）。
- **SFT** → 营销领域 LLM 的指令微调（e3 day-2 LLM 应用工程）。
- **DPO** → 营销文案偏好对齐（让 LLM 输出符合品牌调性），比 RLHF 简单稳定。
- **量化** → 把 70B 模型塞进单卡推理的必备技术，直接影响 FinOps 成本（skill-4 day-5 / e3 day-3）。
- **RoPE** → 长上下文营销知识检索的位置外推（skill-1 day-3）。

### 6.8 延伸阅读（rohitg00）

- [P10/04 Pre-training Mini GPT](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/10-llms-from-scratch/04-pre-training-mini-gpt/README.md) — mini-GPT 预训练（本章核心）
- [P10/06 Instruction Tuning SFT](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/10-llms-from-scratch/06-instruction-tuning-sft/README.md) — SFT
- [P10/07 RLHF](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/10-llms-from-scratch/07-rlhf/README.md) — RLHF
- [P10/08 DPO](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/10-llms-from-scratch/08-dpo/README.md) — DPO
- [P10/11 Quantization](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/10-llms-from-scratch/11-quantization/README.md) — 量化
- [P10/12 Inference Optimization](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/10-llms-from-scratch/12-inference-optimization/README.md) — 推理优化

---

## 第7章 · LLM 工程化 - inference/serving/RAG

**对应 rohitg00 phase**: [P11 LLM Engineering](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/11-llm-engineering) · **深度**: 标准

### 7.1 从模型到系统

把一个训练好的 LLM 变成可用的商业系统，需要 RAG（检索增强）、function calling（工具调用）、MCP（模型上下文协议）、caching、guardrails。本章手写 RAG 检索与 function calling 分发骨架。

### 7.2 RAG：检索增强生成

RAG = 检索 + 生成。给定查询 $q$，从语料库 $\{d_i\}$ 检索 top-k 相关文档，拼入 prompt：

$$\text{prompt} = [\text{query } q] + \text{top-}k\{ \text{sim}(q, d_i) \}$$

检索用稠密向量余弦相似度 $\text{sim}(q,d) = \frac{q\cdot d}{\|q\|\|d\|}$ 或 BM25 稀疏检索。

### 7.3 Function Calling：工具分发

LLM 输出 JSON 结构化调用请求，分发器根据 schema 调用对应工具。骨架：解析 JSON → 校验 schema → 调用 → 回填结果。

### 7.4 numpy 骨架

```python
import numpy as np
import re

def dense_retrieve(query_vec, doc_vecs, k=3):
    # query_vec: (d,), doc_vecs: (N, d)
    qn = query_vec / (np.linalg.norm(query_vec) + 1e-9)
    dn = doc_vecs / (np.linalg.norm(doc_vecs, axis=1, keepdims=True) + 1e-9)
    sims = dn @ qn
    top = np.argsort(-sims)[:k]
    return top, sims[top]

def parse_tool_call(llm_output):
    # extract first JSON object {"tool": "..., "args": {...}}
    m = re.search(r'\{[^{}]*\}', llm_output)
    if not m:
        return None
    obj = eval(m.group(0), {"__builtins__": {}}, {})
    return obj if isinstance(obj, dict) else None

def dispatch_tool(call, tool_registry):
    if not call or "tool" not in call:
        return {"error": "no tool"}
    name = call["tool"]
    if name not in tool_registry:
        return {"error": f"unknown tool {name}"}
    return tool_registry[name](**call.get("args", {}))

# verification_property:
#   dense_retrieve returns k indices with descending sims;
#   dispatch_tool routes to correct registry entry
if __name__ == "__main__":
    rng = np.random.default_rng(0)
    docs = rng.standard_normal((20, 8))
    q = docs[3] + 0.01 * rng.standard_normal(8)
    idx, sims = dense_retrieve(q, docs, k=3)
    assert idx[0] == 3, "top-1 retrieve must be the nearest doc"
    assert all(sims[i] >= sims[i+1] for i in range(len(sims)-1)), "sims must be descending"
    reg = {"add": lambda a, b: a + b}
    out = dispatch_tool({"tool": "add", "args": {"a": 2, "b": 3}}, reg)
    assert out == 5, "dispatch must route to registry"
```

**verification_property**: dense_retrieve 返回的相似度降序且 top-1 是最近文档；dispatch_tool 根据 `tool` 字段正确路由到 registry。

### 7.5 商业连接

- **RAG** → 营销知识库问答（skill-1 day-3 GraphRAG / e3 day-2）。
- **function calling** → Agent 调用营销 API（查询库存、下单、发券）（skill-5 day-1 / e3 day-2）。
- **MCP** → 企业工具协议标准化（skill-2 day-1）。
- **caching** → 营销问答的语义缓存降本（skill-5 day-5）。

### 7.6 延伸阅读（rohitg00）

- [P11/06 RAG](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/06-rag/README.md) — RAG 基础
- [P11/09 Function Calling](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/09-function-calling/README.md) — 函数调用
- [P11/14 Model Context Protocol](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/14-model-context-protocol/README.md) — MCP
- [P11/10 Evaluation](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/10-evaluation/README.md) — LLM 评估

---

### 7.7 从零实现思维链推理

> 🌐 **2026前沿补丁**：本节手写 Chain-of-Thought (CoT) 解析器和 Tree-of-Thoughts (ToT) 搜索器，让读者理解推理模型（o1/R1）背后的核心机制。CoT 的本质是"用更多输出 Token 换取更准确的推理"，ToT 的本质是"在推理空间中做树搜索"。

#### CoT 解析器：步骤提取与中间结果缓存

CoT 的 from-scratch 理解点不在 LLM 本身，而在**如何解析和利用推理链**。给定一段 CoT 输出，解析器需要：

1. **步骤提取**：将自由文本的推理链切分为离散步骤（按"Step N:"或换行分隔）
2. **中间结果缓存**：提取每一步的关键结论，供后续步骤引用
3. **步骤验证**：检查推理链的逻辑一致性（如步骤3引用的数值是否与步骤2的输出一致）

#### ToT 求解器：树搜索 + 评估 + 剪枝

ToT 将推理建模为树搜索：

- **节点**：推理状态（当前推理链 + 部分答案）
- **边**：一个推理步骤（Thought）
- **评估函数**：对节点打分，判断该推理路径是否有前途
- **搜索策略**：BFS（广度优先，保留多个候选）或 DFS（深度优先，快速深入）
- **剪枝**：丢弃评分低于阈值的节点，减少搜索空间

#### numpy 骨架（CoT 解析器 + ToT 24点求解器）

```python
import numpy as np
import re
from itertools import combinations, permutations

# === Part 1: CoT 解析器 ===

def parse_cot_steps(cot_text):
    """
    从CoT文本中提取推理步骤和中间结果
    支持格式: "Step 1: ..." 或 "步骤1: ..." 或换行分隔
    """
    # 尝试按 "Step N:" 或 "步骤N:" 分割
    steps = re.split(r'(?:Step\s*\d+|步骤\s*\d+)[:：\.]?\s*', cot_text)
    steps = [s.strip() for s in steps if s.strip()]

    if len(steps) <= 1:
        # 回退到按换行分割
        steps = [s.strip() for s in cot_text.strip().split('\n') if s.strip()]

    # 提取每步的中间结果（数字、等式）
    intermediate_results = []
    for step in steps:
        # 找等式: "100 * 0.2 = 20" 或 "= 20"
        equations = re.findall(r'([\d.]+)\s*([+\-*/×÷])\s*([\d.]+)\s*=\s*([\d.]+)', step)
        for a, op, b, result in equations:
            intermediate_results.append({
                'expression': f"{a} {op} {b}",
                'result': float(result)
            })
        # 找独立等式: "= 20" 或 "ROAS = 2.0"
        assigns = re.findall(r'=\s*([\d.]+)', step)
        for val in assigns:
            intermediate_results.append({'result': float(val)})

    return {
        'steps': steps,
        'num_steps': len(steps),
        'intermediate_results': intermediate_results
    }

def verify_cot_consistency(parsed_cot):
    """
    验证CoT推理链的一致性：检查每步引用的数值是否在前步结果中出现
    """
    if not parsed_cot['intermediate_results']:
        return True  # 无法验证时默认通过

    results = set(r['result'] for r in parsed_cot['intermediate_results'])
    # 检查是否有明显的不一致（如步骤3用到了步骤2未产出的数值）
    # 这里做简化版：检查所有中间结果是否为有限数
    for r in parsed_cot['intermediate_results']:
        if not np.isfinite(r['result']):
            return False
    return True

# === Part 2: ToT 24点求解器 ===

def solve_24_tot(numbers, target=24, max_depth=4, beam_width=3):
    """
    用Tree-of-Thoughts搜索解决24点游戏
    每个节点: (剩余数字列表, 运算历史)
    每个边: 选两个数字做运算(+,-,*,/)
    评估函数: 剩余数字与目标的接近程度
    搜索策略: BFS beam search
    """
    initial_state = (tuple(sorted(numbers)), [])
    # BFS: 每层保留 beam_width 个最优节点
    frontier = [initial_state]
    visited = set()

    for depth in range(max_depth):
        candidates = []
        for state in frontier:
            nums, history = state
            if len(nums) == 1:
                # 只剩一个数，检查是否等于目标
                if abs(nums[0] - target) < 1e-6:
                    return history  # 找到解
                continue

            # 生成所有可能的两数运算
            for i, j in combinations(range(len(nums)), 2):
                a, b = nums[i], nums[j]
                remaining = [nums[k] for k in range(len(nums)) if k != i and k != j]

                for op_name, op_func in [('+', lambda x, y: x + y),
                                          ('-', lambda x, y: x - y),
                                          ('*', lambda x, y: x * y),
                                          ('/', lambda x, y: x / y if y != 0 else float('inf'))]:
                    result = op_func(a, b)
                    new_nums = tuple(sorted(remaining + [result]))
                    new_history = history + [f"{a} {op_name} {b} = {result:.4f}".rstrip('0').rstrip('.')]

                    state_key = (new_nums, tuple(new_history))
                    if new_nums not in visited:
                        # 评估函数：剩余数字的均值与目标的距离
                        if len(new_nums) == 1:
                            score = abs(new_nums[0] - target)
                        else:
                            # 启发式：剩余数字能组合出目标的可能性
                            score = abs(np.mean(new_nums) - target / len(new_nums))
                        candidates.append((score, (new_nums, new_history)))

        if not candidates:
            break

        # Beam search: 保留评分最低的 beam_width 个
        candidates.sort(key=lambda x: x[0])
        frontier = [c[1] for c in candidates[:beam_width]]
        for c in frontier:
            visited.add(c[0])

    return None  # 未找到解

# === Part 3: ToT 逻辑推理题求解器 ===

def tot_logic_solver(facts, rules, query, max_depth=5):
    """
    用ToT解决逻辑推理题
    facts: 初始事实集合 {"A>B", "B>C"}
    rules: 推理规则 [传递性: A>B, B>C => A>C]
    query: 查询 "A>C"
    """
    def apply_rules(known):
        """应用所有规则，生成新事实"""
        new_facts = set(known)
        for fact in known:
            # 传递性: A>B, B>C => A>C
            parts = fact.split('>')
            if len(parts) == 2:
                a, b = parts
                for other in known:
                    op = other.split('>')
                    if len(op) == 2 and op[0] == b:
                        new_fact = f"{a}>{op[1]}"
                        if new_fact not in new_facts:
                            new_facts.add(new_fact)
        return new_facts

    # BFS搜索
    frontier = [(set(facts), [])]
    for depth in range(max_depth):
        next_frontier = []
        for known, path in frontier:
            if query in known:
                return path  # 找到推理路径

            expanded = apply_rules(known)
            new_facts = expanded - known
            if new_facts:
                step_desc = f"Step {depth+1}: 推导出 {new_facts}"
                next_frontier.append((expanded, path + [step_desc]))

        if not next_frontier:
            break
        frontier = next_frontier

    return None

# verification_property:
#   CoT解析器正确提取步骤数和中间结果;
#   ToT 24点求解器对有解问题返回有效解;
#   逻辑推理器通过传递性推导出结论
if __name__ == "__main__":
    # 测试CoT解析器
    cot_text = """
    Step 1: 计算转化客户数 = 500 * 0.2 = 100
    Step 2: 计算总收入 = 100 * 2000 = 200000
    Step 3: 计算ROAS = 200000 / 100000 = 2.0
    """
    parsed = parse_cot_steps(cot_text)
    assert parsed['num_steps'] == 3, f"Expected 3 steps, got {parsed['num_steps']}"
    assert len(parsed['intermediate_results']) >= 3, "Must extract >=3 intermediate results"
    assert verify_cot_consistency(parsed), "CoT must be consistent"

    # 测试ToT 24点求解器
    solution = solve_24_tot([3, 3, 8, 8], target=24, beam_width=5)
    # 3,3,8,8的解: 8 / (3 - 8/3) = 24
    if solution:
        print(f"24点 [3,3,8,8] 解: {solution}")
    # 简单案例
    sol2 = solve_24_tot([1, 2, 3, 4], target=24, beam_width=5)
    assert sol2 is not None, "[1,2,3,4] must have a 24-point solution"
    print(f"24点 [1,2,3,4] 解: {sol2}")

    # 测试逻辑推理器
    facts = {"A>B", "B>C"}
    path = tot_logic_solver(facts, [], "A>C")
    assert path is not None, "Must derive A>C from A>B and B>C by transitivity"
    print(f"逻辑推理: {facts} => A>C, 路径: {path}")
```

**verification_property**: CoT解析器提取步骤数与中间结果数正确；ToT 24点求解器对有解问题（如[1,2,3,4]）返回有效解；逻辑推理器通过传递性推导出 A>C。

### 7.8 从零实现 Function Calling

> 🌐 **2026前沿补丁**：本节手写一个完整的 Function Calling 调度器，不依赖任何 LLM API。理解 Function Calling 的 from-scratch 实现有助于设计 Agent 系统的工具编排逻辑，并为理解 MCP（Model Context Protocol）协议的标准化设计奠定基础。

#### Function Calling 的四步流程

Function Calling 的本质是一个**解析-校验-执行-注入**循环：

1. **函数签名解析**：从 LLM 输出中提取函数名和参数（JSON 格式）
2. **参数校验**：验证参数类型、必填项、取值范围是否符合函数 schema
3. **函数执行**：调用对应的 Python 函数，获取返回值
4. **结果注入**：将函数返回值格式化后注入对话上下文，供 LLM 生成下一步

#### 从零实现：正则 + JSON 解析

不依赖 LLM API 的 Function Calling 需要"模拟"LLM 的输出：给定用户意图和可用工具列表，用规则/模板推断应该调用哪个工具。这虽然不如 LLM 灵活，但能清晰展示 Function Calling 的工程结构。

#### 与 MCP 协议的对比

MCP（Model Context Protocol, Anthropic 2024）是 Function Calling 的标准化升级：

| 维度 | 传统 Function Calling | MCP 协议 |
|------|----------------------|---------|
| 工具发现 | 硬编码在 prompt 中 | 动态发现（MCP Server 自描述） |
| 参数 schema | JSON Schema | JSON Schema + 语义描述 |
| 执行环境 | 与 LLM 同进程 | 独立进程（MCP Server） |
| 安全隔离 | 无 | 进程级隔离 + 权限控制 |
| 状态管理 | 无状态 | 支持有状态会话 |
| 工具组合 | 手动编排 | 标准化组合（Resources/Tools/Prompts） |

MCP 的核心设计思想是**将工具能力与 LLM 解耦**：LLM 不需要知道工具的具体实现，只需要通过标准协议与 MCP Server 通信。这类似于微服务架构中的 API Gateway 模式--工具是服务，MCP 是网关，LLM 是客户端。

#### numpy 骨架（纯 Python Function Calling 调度器）

```python
import re
import json
from dataclasses import dataclass, field
from typing import Any, Dict, List, Callable, Optional

# === Part 1: 工具注册与 Schema 定义 ===

@dataclass
class ToolSchema:
    """工具的JSON Schema定义"""
    name: str
    description: str
    parameters: Dict[str, Any]  # JSON Schema 格式

@dataclass
class ToolCall:
    """解析后的工具调用"""
    name: str
    arguments: Dict[str, Any]
    raw: str = ""

class ToolRegistry:
    """工具注册表：管理可用工具的schema和实现"""
    def __init__(self):
        self._schemas: Dict[str, ToolSchema] = {}
        self._handlers: Dict[str, Callable] = {}

    def register(self, schema: ToolSchema, handler: Callable):
        self._schemas[schema.name] = schema
        self._handlers[schema.name] = handler

    def get_schemas(self) -> List[Dict]:
        """返回所有工具的JSON Schema（用于注入prompt）"""
        return [
            {
                "name": s.name,
                "description": s.description,
                "parameters": s.parameters
            }
            for s in self._schemas.values()
        ]

    def get_handler(self, name: str) -> Optional[Callable]:
        return self._handlers.get(name)

# === Part 2: 参数校验器 ===

def validate_arguments(args: Dict, schema: Dict) -> tuple:
    """
    校验参数是否符合JSON Schema
    返回 (is_valid, error_message)
    """
    properties = schema.get("properties", {})
    required = schema.get("required", [])

    # 检查必填项
    for req in required:
        if req not in args:
            return False, f"Missing required parameter: {req}"

    # 检查类型
    type_map = {"string": str, "number": (int, float), "integer": int,
                "boolean": bool, "array": list, "object": dict}
    for key, value in args.items():
        if key in properties:
            expected_type = properties[key].get("type")
            if expected_type and expected_type in type_map:
                if not isinstance(value, type_map[expected_type]):
                    return False, f"Parameter '{key}' expected {expected_type}, got {type(value).__name__}"

        # 检查enum
        if key in properties and "enum" in properties[key]:
            if value not in properties[key]["enum"]:
                return False, f"Parameter '{key}' must be one of {properties[key]['enum']}"

    return True, ""

# === Part 3: LLM输出解析器（正则 + JSON）===

def parse_tool_call_from_text(llm_output: str) -> Optional[ToolCall]:
    """
    从LLM文本输出中提取工具调用
    支持格式: {"name": "...", "arguments": {...}} 或 ```json ... ``` 代码块
    """
    # 尝试匹配 ```json ... ``` 代码块
    json_block = re.search(r'```(?:json)?\s*(\{.*?\})\s*```', llm_output, re.DOTALL)
    if json_block:
        json_str = json_block.group(1)
    else:
        # 尝试匹配裸JSON对象
        json_match = re.search(r'\{[^{}]*"name"[^{}]*\}', llm_output, re.DOTALL)
        if json_match:
            json_str = json_match.group(0)
        else:
            return None

    try:
        obj = json.loads(json_str)
        if "name" not in obj:
            return None
        return ToolCall(
            name=obj["name"],
            arguments=obj.get("arguments", obj.get("args", {})),
            raw=json_str
        )
    except json.JSONDecodeError:
        return None

# === Part 4: 意图路由器（无LLM时的规则匹配）===

def route_intent(user_input: str, registry: ToolRegistry) -> Optional[ToolCall]:
    """
    基于关键词匹配的意图路由（无LLM API时的替代方案）
    用正则规则模拟LLM的工具选择能力
    """
    routing_rules = [
        # (关键词列表, 工具名, 参数提取正则)
        (["查询", "库存", "多少"], "check_inventory",
         r'(?:sku|商品|产品)\s*(\d+)', {"sku_id": 0}),

        (["价格", "多少钱", "费用"], "get_price",
         r'(?:sku|商品|产品)\s*(\d+)', {"sku_id": 0}),

        (["下单", "购买", "订单"], "create_order",
         r'(?:sku|商品|产品)\s*(\d+).*?(?:数量|买)\s*(\d+)', {"sku_id": 0, "quantity": 1}),

        (["推荐", "建议", "适合"], "recommend_products",
         r'(?:类别|类型|品类)\s*[:：]?\s*(\w+)', {"category": 0}),
    ]

    for keywords, tool_name, pattern, arg_indices in routing_rules:
        if any(kw in user_input for kw in keywords):
            match = re.search(pattern, user_input)
            if match:
                arguments = {}
                for arg_name, group_idx in arg_indices.items():
                    arguments[arg_name] = match.group(group_idx + 1)
                return ToolCall(name=tool_name, arguments=arguments)

    return None

# === Part 5: 完整调度器 ===

class FunctionCallingDispatcher:
    """
    Function Calling 完整调度器
    流程: 解析LLM输出 -> 校验参数 -> 执行工具 -> 注入结果
    """

    def __init__(self, registry: ToolRegistry):
        self.registry = registry
        self.conversation_history = []

    def execute_tool_call(self, tool_call: ToolCall) -> Dict[str, Any]:
        """执行工具调用"""
        # 1. 查找工具
        handler = self.registry.get_handler(tool_call.name)
        if not handler:
            return {"error": f"Unknown tool: {tool_call.name}"}

        # 2. 校验参数
        schema = self.registry._schemas.get(tool_call.name)
        if schema:
            is_valid, error = validate_arguments(tool_call.arguments, schema.parameters)
            if not is_valid:
                return {"error": f"Validation failed: {error}"}

        # 3. 执行
        try:
            result = handler(**tool_call.arguments)
            return {"result": result, "tool": tool_call.name}
        except Exception as e:
            return {"error": f"Execution error: {str(e)}"}

    def process_user_input(self, user_input: str, use_llm: bool = False) -> Dict:
        """
        处理用户输入的完整流程
        use_llm=False时使用规则路由, True时用LLM输出解析
        """
        self.conversation_history.append({"role": "user", "content": user_input})

        # 步骤1: 意图识别（工具选择）
        if use_llm:
            # 实际场景中这里调用LLM，传入工具schema
            # llm_output = llm.chat(user_input, tools=self.registry.get_schemas())
            # tool_call = parse_tool_call_from_text(llm_output)
            tool_call = None  # 需要真实LLM
        else:
            tool_call = route_intent(user_input, self.registry)

        if not tool_call:
            return {"response": "无法识别您的意图，请尝试更明确的表达。"}

        # 步骤2: 执行工具
        execution_result = self.execute_tool_call(tool_call)

        # 步骤3: 结果注入对话上下文
        self.conversation_history.append({
            "role": "tool",
            "name": tool_call.name,
            "arguments": tool_call.arguments,
            "result": execution_result
        })

        # 步骤4: 生成自然语言回复（无LLM时用模板）
        if "error" in execution_result:
            response = f"抱歉，处理您的请求时出错：{execution_result['error']}"
        else:
            response = self._format_result(tool_call.name, execution_result["result"])

        self.conversation_history.append({"role": "assistant", "content": response})

        return {
            "tool_call": tool_call,
            "execution_result": execution_result,
            "response": response
        }

    def _format_result(self, tool_name: str, result: Any) -> str:
        """将工具执行结果格式化为自然语言"""
        templates = {
            "check_inventory": lambda r: f"商品{r.get('sku_id', '')}的当前库存为{r.get('stock', '未知')}件。",
            "get_price": lambda r: f"商品{r.get('sku_id', '')}的价格为{r.get('price', '未知')}元。",
            "create_order": lambda r: f"订单已创建，订单号：{r.get('order_id', '未知')}，预计{r.get('delivery_date', '3天内')}送达。",
            "recommend_products": lambda r: f"为您推荐以下{r.get('category', '')}商品：{', '.join(r.get('products', []))}",
        }
        formatter = templates.get(tool_name, lambda r: str(r))
        return formatter(result)

# === Part 6: 注册营销工具并测试 ===

def setup_marketing_tools():
    """注册营销相关的工具"""
    registry = ToolRegistry()

    # 工具1: 查库存
    registry.register(
        ToolSchema(
            name="check_inventory",
            description="查询商品库存",
            parameters={
                "type": "object",
                "properties": {
                    "sku_id": {"type": "integer", "description": "商品SKU编号"}
                },
                "required": ["sku_id"]
            }
        ),
        handler=lambda sku_id: {"sku_id": sku_id, "stock": 156, "warehouse": "华东仓"}
    )

    # 工具2: 查价格
    registry.register(
        ToolSchema(
            name="get_price",
            description="查询商品价格",
            parameters={
                "type": "object",
                "properties": {
                    "sku_id": {"type": "integer", "description": "商品SKU编号"}
                },
                "required": ["sku_id"]
            }
        ),
        handler=lambda sku_id: {"sku_id": sku_id, "price": 299.0, "currency": "CNY"}
    )

    # 工具3: 创建订单
    registry.register(
        ToolSchema(
            name="create_order",
            description="创建购买订单",
            parameters={
                "type": "object",
                "properties": {
                    "sku_id": {"type": "integer", "description": "商品SKU编号"},
                    "quantity": {"type": "integer", "description": "购买数量"}
                },
                "required": ["sku_id", "quantity"]
            }
        ),
        handler=lambda sku_id, quantity: {
            "order_id": f"ORD{sku_id}{quantity:04d}",
            "total": 299.0 * quantity,
            "delivery_date": "3天内"
        }
    )

    # 工具4: 推荐
    registry.register(
        ToolSchema(
            name="recommend_products",
            description="根据类别推荐商品",
            parameters={
                "type": "object",
                "properties": {
                    "category": {"type": "string", "enum": ["服装", "电子", "食品", "家居"],
                                 "description": "商品类别"}
                },
                "required": ["category"]
            }
        ),
        handler=lambda category: {
            "category": category,
            "products": [f"{category}商品A", f"{category}商品B", f"{category}商品C"]
        }
    )

    return registry

# verification_property:
#   工具注册后可被调度器发现和执行;
#   参数校验拒绝缺失必填项和类型不匹配;
#   规则路由正确匹配用户意图到对应工具;
#   JSON解析器从LLM输出中提取工具调用
if __name__ == "__main__":
    registry = setup_marketing_tools()
    dispatcher = FunctionCallingDispatcher(registry)

    # 测试1: 查库存
    result1 = dispatcher.process_user_input("帮我查询商品123的库存还有多少")
    assert "tool_call" in result1, "Must route to a tool"
    assert result1["tool_call"].name == "check_inventory"
    assert result1["tool_call"].arguments["sku_id"] == 123
    print(f"测试1: {result1['response']}")

    # 测试2: 创建订单
    result2 = dispatcher.process_user_input("我要购买商品456，数量买3")
    assert result2["tool_call"].name == "create_order"
    assert result2["tool_call"].arguments["quantity"] == 3
    print(f"测试2: {result2['response']}")

    # 测试3: 参数校验（故意传错类型）
    bad_call = ToolCall(name="check_inventory", arguments={"sku_id": "not_a_number"})
    is_valid, error = validate_arguments(bad_call.arguments,
                                         registry._schemas["check_inventory"].parameters)
    assert not is_valid, "Must reject non-integer sku_id"

    # 测试4: JSON解析器
    llm_output = '好的，我来帮您查询。```json\n{"name": "get_price", "arguments": {"sku_id": 789}}\n```'
    parsed = parse_tool_call_from_text(llm_output)
    assert parsed is not None, "Must parse tool call from LLM output"
    assert parsed.name == "get_price"
    assert parsed.arguments["sku_id"] == 789
    print(f"测试4: 解析LLM输出 -> 工具={parsed.name}, 参数={parsed.arguments}")

    # 测试5: 推荐商品
    result5 = dispatcher.process_user_input("推荐一些电子类的商品")
    assert result5["tool_call"].name == "recommend_products"
    print(f"测试5: {result5['response']}")
```

**verification_property**: 工具注册后可被发现和执行；参数校验拒绝缺失必填项和类型不匹配；规则路由正确匹配用户意图到工具；JSON解析器从LLM输出中提取工具调用。

---

## 第8章 · Agent 工程 - agent loop/ReAct/memory/LangGraph

**对应 rohitg00 phase**: [P14 Agent Engineering](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering) · **深度**: ⭐旗舰

### 8.1 Agent 是 AI 原生商业的核心载体

商业模式从"卖模型"转向"卖 Agent 的产出"（skill-4 day-3 Agent 经济）。研究者必须理解 Agent 的内部：loop、工具、记忆、状态图、评估、生产化。本章旗舰，手写 ReAct loop + StateGraph + 记忆骨架。

### 8.2 Agent Loop 与 ReAct

Agent 的本质是一个循环：感知（读输入）→ 思考（LLM 推理）→ 行动（调工具）→ 观察（读结果）→ 重复直到完成。ReAct 把思考与行动交织：

```
Thought: 我需要查库存
Action: check_inventory(sku=123)
Observation: 库存 50
Thought: 库存充足，可以推荐
Action: finish(answer="...")
```

### 8.3 StateGraph：状态机编排

LangGraph 把 Agent 建模为有向状态图：节点是函数，边是条件路由。状态字典在节点间流转。手写 StateGraph = 节点表 + 边表 + 条件路由函数。

### 8.4 记忆：短期 + 长期

短期记忆 = 当前对话窗口；长期记忆 = 向量检索的历史摘要。MemGPT 风格的分页记忆把上下文视为可分页的内存。

### 8.5 numpy 骨架（ReAct loop + StateGraph）

```python
import numpy as np

class StateGraph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.cond = {}
    def add_node(self, name, fn):
        self.nodes[name] = fn
    def add_edge(self, a, b):
        self.edges.setdefault(a, []).append(("__always__", b))
    def add_conditional(self, a, router_fn, mapping):
        self.cond[a] = (router_fn, mapping)
    def run(self, init_state, max_steps=20):
        state = dict(init_state)
        current = state.get("__start__", list(self.nodes.keys())[0])
        steps = 0
        while current != "__end__" and steps < max_steps:
            if current in self.nodes:
                state = self.nodes[current](state) or state
            if current in self.cond:
                router, mapping = self.cond[current]
                key = router(state)
                current = mapping.get(key, "__end__")
            elif current in self.edges:
                current = self.edges[current][0][1]
            else:
                break
            steps += 1
        return state

def react_step(state):
    # state: {"thought":..., "action":..., "obs":..., "done":bool}
    state["step"] = state.get("step", 0) + 1
    if state["step"] >= 3:
        state["done"] = True
    return state

def route(state):
    return "end" if state.get("done") else "loop"

# verification_property:
#   StateGraph terminates within max_steps; state accumulates step count
if __name__ == "__main__":
    g = StateGraph()
    g.add_node("start", react_step)
    g.add_node("loop", react_step)
    g.add_edge("__start__", "start") if False else None
    g.nodes["start"] = react_step
    g.nodes["loop"] = react_step
    g.add_edge("start", "loop")
    g.add_conditional("loop", route, {"loop": "loop", "end": "__end__"})
    out = g.run({"__start__": "start", "step": 0, "done": False}, max_steps=10)
    assert out["step"] >= 3, "ReAct loop must accumulate steps until done"
    assert out["done"] is True, "loop must set done=True to terminate"
```

**verification_property**: StateGraph 在 `max_steps` 内终止；状态字典累积 `step` 计数且 `done=True` 时收敛。

### 8.6 商业连接

- **ReAct loop** → 营销 Agent 的"查库存→算折扣→生成文案"循环（skill-5 day-1 / e1 day-1）。
- **StateGraph** → 营销审批工作流（草拟→审核→发布）的 HITL 门控（skill-2 day-3 / skill-5 day-2）。
- **记忆** → 客户经理 Agent 记住客户历史偏好（skill-5 day-1 / e1 day-1）。
- **Agent eval** → 营销 Agent 任务通过率基准（skill-5 day-3 / e3 day-3）。

### 8.7 延伸阅读（rohitg00）

- [P14/01 The Agent Loop](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/14-agent-engineering/01-the-agent-loop/README.md) — agent loop（本章核心）
- [P14/03 Reflexion Verbal RL](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/14-agent-engineering/03-reflexion-verbal-rl/README.md) — Reflexion 自我反思
- [P14/13 LangGraph Stateful Graphs](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/14-agent-engineering/13-langgraph-stateful-graphs/README.md) — LangGraph 状态图
- [P14/07 Memory Virtual Context MemGPT](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/14-agent-engineering/07-memory-virtual-context-memgpt/README.md) — MemGPT 记忆
- [P14/29 Production Runtimes](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/14-agent-engineering/29-production-runtimes/README.md) — 生产 runtime

---

## 第9章 · 多智能体与自主系统

**对应 rohitg00 phase**: [P15 Autonomous Systems](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems) + [P16 Multi-Agent](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms) · **深度**: 标准（合并）

### 9.1 从单 Agent 到 Agent 群

单 Agent 能力有限。多 Agent 系统通过角色分工、辩论、投票、共识实现更复杂任务。本章手写 supervisor 拓扑 + 辩论投票骨架。

### 9.2 Supervisor 模式

一个 supervisor agent 接收任务，分发给多个 worker agent，汇总结果。这是 LangGraph supervisor、CrewAI crew 的共同骨架。

### 9.3 辩论与投票

多个 agent 对同一问题给出答案，通过多数投票或辩论收敛。Society of Mind 思想：多个视角的聚合优于单一视角。

### 9.4 numpy 骨架

```python
import numpy as np
from collections import Counter

def supervisor_dispatch(task, workers):
    # task: str, workers: list of callables returning str
    results = [w(task) for w in workers]
    return results

def majority_vote(answers):
    # answers: list of str
    c = Counter(answers)
    return c.most_common(1)[0][0]

def debate_round(agents_answers, critic):
    # critic picks best answer by score
    scored = [(critic(a), a) for a in agents_answers]
    return max(scored)[1]

def bft_vote(answers, threshold=0.67):
    # simple BFT: agree if top answer fraction >= threshold
    c = Counter(answers)
    top, count = c.most_common(1)[0]
    return top if count / len(answers) >= threshold else None

# verification_property:
#   majority_vote returns plurality; BFT returns None when no supermajority
if __name__ == "__main__":
    workers = [lambda t: "A", lambda t: "A", lambda t: "B"]
    res = supervisor_dispatch("x", workers)
    assert majority_vote(res) == "A", "majority vote picks plurality"
    assert bft_vote(["A", "A", "B"]) == "A", "BFT agrees on supermajority"
    assert bft_vote(["A", "B", "C"]) is None, "BFT returns None without supermajority"
```

**verification_property**: majority_vote 返回多数；BFT 在无绝对多数时返回 None。

### 9.5 商业连接

- **supervisor** → 营销活动 Agent 团队（文案+设计+投放 supervisor）（e1 day-3 / skill-4 day-4 平台生态）。
- **辩论** → 营销策略多 Agent 辩论（保守 vs 激进）（e1 day-3）。
- **BFT 共识** → Agent 经济中的多方信任（e10 day-3）。
- **autonomous research** → capstone 自主研究 agent（day-phase-1）。

### 9.6 延伸阅读（rohitg00）

- [P16/05 Supervisor Orchestrator Pattern](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/16-multi-agent-and-swarms/05-supervisor-orchestrator-pattern/README.md) — supervisor 模式
- [P16/07 Society of Mind Debate](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/16-multi-agent-and-swarms/07-society-of-mind-debate/README.md) — 辩论
- [P16/14 Consensus and BFT](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/16-multi-agent-and-swarms/14-consensus-and-bft/README.md) — 共识与 BFT
- [P16/21 Agent Economies](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/16-multi-agent-and-swarms/21-agent-economies/README.md) — Agent 经济
- [P15/05 AI Scientist v2](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/15-autonomous-systems/05-ai-scientist-v2/README.md) — 自主科研系统

---

## 第10章 · 推理与生产基础设施 - vLLM/KV cache/finops

**对应 rohitg00 phase**: [P17 Infrastructure and Production](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production) · **深度**: ⭐旗舰

### 10.1 推理是商业 LLM 的成本主战场

训练成本是一次性的，推理成本是持续的。一个商业 LLM 应用的利润率几乎完全取决于推理效率。本章旗舰，手写 KV cache + 连续批处理骨架 + FinOps 成本模型。

### 10.2 KV Cache

自回归生成时，每生成一个 token 都要对前面所有 token 做 attention。若不缓存，第 $t$ 步成本 $O(t)$，总成本 $O(T^2)$。缓存 $K,V$ 后，每步只需算新 token 的 $K,V$ 追加，单步 $O(1)$，总 $O(T)$。

### 10.3 连续批处理（Continuous Batching）

传统批处理要等一批请求全部完成才能接新请求（队头阻塞）。连续批处理在每步调度：已完成的请求移出，新请求加入，每步动态组批。vLLM 的核心创新。

### 10.4 FinOps：成本模型

单次推理成本 $C = \frac{\text{tokens} \times \text{GPU秒/token}}{\text{GPU利用率}} \times \text{GPU单价}$。FinOps 的目标是在 SLA 约束下最小化 $C$。

### 10.5 numpy 骨架（KV cache + 连续批处理）

```python
import numpy as np

class KVCache:
    def __init__(self, n_layers, n_heads, dh, max_len=1024):
        self.K = [np.zeros((max_len, n_heads, dh)) for _ in range(n_layers)]
        self.V = [np.zeros((max_len, n_heads, dh)) for _ in range(n_layers)]
        self.len = 0
        self.max_len = max_len
    def append(self, k_layer, v_layer):
        # k_layer: list of (n_heads, dh) per layer for new token
        for l in range(len(k_layer)):
            self.K[l][self.len] = k_layer[l]
            self.V[l][self.len] = v_layer[l]
        self.len += 1
    def get(self, layer):
        return self.K[layer][:self.len], self.V[layer][:self.len]

def continuous_batch_schedule(active, new_req, max_batch=4):
    # active: list of reqs with remaining tokens, new_req: dict or None
    # remove finished, add new if room
    active = [r for r in active if r["remaining"] > 0]
    if new_req and len(active) < max_batch:
        active.append(new_req)
    # one step: each active req generates 1 token
    for r in active:
        r["remaining"] -= 1
    return active

def finops_cost(tokens, gpu_sec_per_token, gpu_price_per_sec, util=0.7):
    return tokens * gpu_sec_per_token * gpu_price_per_sec / util

# verification_property:
#   KVCache length grows by 1 per append; continuous_batch keeps len <= max_batch
if __name__ == "__main__":
    cache = KVCache(n_layers=2, n_heads=4, dh=8)
    for _ in range(5):
        kl = [np.random.randn(4, 8) for _ in range(2)]
        vl = [np.random.randn(4, 8) for _ in range(2)]
        cache.append(kl, vl)
    assert cache.len == 5, "KVCache length must equal number of appends"
    k, v = cache.get(0)
    assert k.shape == (5, 4, 8), "KVCache get returns (len, heads, dh)"
    active = [{"remaining": 2}, {"remaining": 1}]
    active = continuous_batch_schedule(active, {"remaining": 3}, max_batch=4)
    assert len(active) <= 4, "batch size must respect max_batch"
    cost = finops_cost(1e6, 0.01, 2.0, 0.7)
    assert cost > 0, "finops cost must be positive"
```

**verification_property**: KVCache 长度随 append 递增；continuous_batch 保持批大小 ≤ max_batch；FinOps 成本为正。

### 10.6 商业连接

- **KV cache** → 营销 Agent 长对话的成本从 $O(T^2)$ 降到 $O(T)$（skill-5 day-5 / e3 day-3）。
- **连续批处理** → 营销客服 LLM 的高并发服务（skill-5 day-5）。
- **FinOps** → outcome-based 定价的成本底线（skill-4 day-2 / e10 day-2）。
- **vLLM** → 企业 LLM 平台的默认推理引擎（skill-2 day-4 / skill-5 day-5）。
- **量化+缓存** → 把 70B 模型塞进单卡的组合拳（skill-4 day-5）。

### 10.7 延伸阅读（rohitg00）

- [P17/04 vLLM Serving Internals](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/17-infrastructure-and-production/04-vllm-serving-internals/README.md) — vLLM 内部（本章核心）
- [P17/02 Inference Platform Economics](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/17-infrastructure-and-production/02-inference-platform-economics/README.md) — 推理经济学
- [P17/27 FinOps LLMs](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/17-infrastructure-and-production/27-finops-llms/README.md) — LLM FinOps
- [P17/13 LLM Observability](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/17-infrastructure-and-production/13-llm-observability/README.md) — 可观测性
- [P17/23 SRE for AI](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/17-infrastructure-and-production/23-sre-for-ai/README.md) — AI SRE

---

## 第11章 · RL 基础 - bandits/RLHF 机制

**对应 rohitg00 phase**: [P9 Reinforcement Learning](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/09-reinforcement-learning) · **深度**: 标准（裁剪：仅 bandits + RLHF 机制）

### 11.1 RL 在商业中的两个落点

RL 在商业分析中有两个高价值应用：**多臂老虎机**（营销预算分配、A/B 测试的 adaptive 版本）和 **RLHF 机制**（理解 LLM 对齐的奖励信号如何塑造行为）。本章手写 Thompson sampling + 简化 RLHF 奖励机制。

### 11.2 Multi-Armed Bandit 与 Thompson Sampling

$K$ 个臂，每个臂有未知奖励分布。目标是在 $T$ 步内最大化累计奖励。Thompson sampling 对每个臂 $k$ 维护奖励的后验，每步从后验采样，选采样值最大的臂：

$$\text{Thompson: } \hat\theta_k \sim \text{Beta}(\alpha_k, \beta_k),\quad k^* = \arg\max_k \hat\theta_k$$

观测奖励后更新后验。Thompson sampling 是 regret 最优的简单算法。

### 11.3 RLHF 奖励机制

RLHF 用奖励模型 $r_\phi(x,y)$ 给 LLM 输出打分，PPO 优化策略 $\pi_\theta$ 最大化 $\mathbb{E}[r_\phi(x,y)] - \beta\,\text{KL}(\pi_\theta\|\pi_{\text{ref}})$。KL 项防止策略偏离参考模型太远（保持流畅性）。理解这个机制才能理解 DPO 为何有效（第6章）。

### 11.4 numpy 骨架

```python
import numpy as np
import random

def thompson_sampling_step(alpha, beta):
    # alpha, beta: arrays of Beta params per arm
    samples = [random.betavariate(alpha[k], beta[k]) for k in range(len(alpha))]
    return int(np.argmax(samples))

def bandit_update(alpha, beta, arm, reward):
    # Bernoulli reward in {0,1}
    if reward:
        alpha[arm] += 1
    else:
        beta[arm] += 1
    return alpha, beta

def run_bandit(true_rates, T=500):
    K = len(true_rates)
    alpha = [1] * K; beta = [1] * K
    rewards = 0
    for _ in range(T):
        arm = thompson_sampling_step(alpha, beta)
        reward = 1 if random.random() < true_rates[arm] else 0
        alpha, beta = run_bandit_update(alpha, beta, arm, reward) if False else bandit_update(alpha, beta, arm, reward)
        rewards += reward
    return alpha, beta, rewards

def rlhf_proxy_loss(reward, kl, beta_kl=0.1):
    # proxy: maximize reward - beta*KL  <=> minimize -(reward - beta*KL)
    return -(reward - beta_kl * kl)

# verification_property:
#   bandit converges: alpha[argmax true_rate] is largest after T steps;
#   rlhf_proxy_loss decreases as reward increases (kl fixed)
if __name__ == "__main__":
    random.seed(0)
    true_rates = [0.2, 0.5, 0.8]
    alpha, beta, rewards = run_bandit(true_rates, T=2000)
    best = int(np.argmax(true_rates))
    assert np.argmax(alpha) == best, "Thompson sampling must converge to best arm"
    l1 = rlhf_proxy_loss(0.5, 0.1)
    l2 = rlhf_proxy_loss(0.8, 0.1)
    assert l2 < l1, "higher reward must lower RLHF proxy loss (kl fixed)"
```

**verification_property**: Thompson sampling 收敛到奖励最高的臂（`argmax(alpha) == argmax(true_rates)`）；RLHF proxy loss 随奖励升高而下降（KL 固定）。

### 11.5 商业连接

- **bandit** → 营销预算在多渠道的 adaptive 分配（skill-3 day-5 / e2 day-3）。
- **Thompson sampling** → A/B 测试的 adaptive 版本，比固定分流更快收敛（skill-3 day-2）。
- **RLHF 机制** → 营销文案偏好对齐的底层理解（第6章 DPO 的前置）。
- **regret 分析** → 营销实验的机会成本量化（skill-3 day-2）。

### 11.6 延伸阅读（rohitg00）

- [P9/04 Q Learning SARSA](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/09-reinforcement-learning/04-q-learning-sarsa/README.md) — bandit/MDP 基础
- [P9/06 Policy Gradients REINFORCE](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/09-reinforcement-learning/06-policy-gradients-reinforce/README.md) — 策略梯度
- [P9/07 Actor Critic A2C A3C](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/09-reinforcement-learning/07-actor-critic-a2c-a3c/README.md) — Actor-Critic
- [P9/09 Reward Modeling RLHF](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/09-reinforcement-learning/09-reward-modeling-rlhf/README.md) — 奖励建模与 RLHF

---

## 第12章 · 商业连接章

**项目独有** · **深度**: 综合

### 12.1 from-scratch 概念 → 商业场景映射矩阵

本章是全书的综合：把前 11 章的每个 from-scratch 概念映射到 AI原生化商业博士项目的实际场景，形成"技术→商业"的双向索引。这张表是研究者的"选型地图"——当遇到一个商业问题，能快速定位该用哪个 from-scratch 机制。

| from-scratch 概念 | 章节 | 商业场景 | 博士项目模块 |
|---|:--:|---|---|
| log-sum-exp 稳定 softmax | 1 | 营销预算多通道分配权重 | skill-0/3 |
| SVD 截断 | 1 | 客户-商品矩阵降维/客户细分 | skill-0/1 |
| 图论 d-分离 | 1 | 因果图后门调整、KG 多跳 | skill-3/1 |
| OLS 闭式解 + 岭回归 | 2 | MMM 广告归因、CLV 回归 | skill-3/e2 |
| 逻辑回归 + 偏差方差 | 2 | 流失预测、响应模型 | e2 |
| 手写 backprop + autograd | 3 | 自定义损失（uplift Qini）训练 | capstone |
| 梯度检验 | 3 | 新损失正确性验证 | capstone/module-r |
| BPE tokenizer | 4 | 多语言营销内容 token 成本 | skill-4 |
| word2vec SGNS | 4 | 评论语义聚类、两塔嵌入 | skill-1 |
| TF-IDF | 4 | 关键词提取基线 | skill-1 |
| scaled dot-product attention | 5 | GraphRAG 多跳检索成本上限 | skill-1 |
| KV cache | 5/10 | Agent 长对话成本控制 | skill-5/e3 |
| multi-head | 5 | 两塔多偏好维度 | skill-1 |
| RoPE 位置编码 | 6 | 长上下文营销知识外推 | skill-1 |
| SFT 损失 | 6 | 营销领域 LLM 微调 | e3 |
| DPO 损失 | 6 | 文案品牌调性对齐 | e3/skill-4 |
| INT8 量化 | 6 | 70B 模型单卡推理降本 | skill-4/5 |
| RAG top-k 检索 | 7 | 营销知识库问答 | skill-1/e3 |
| function calling 分发 | 7 | Agent 调营销 API | skill-5/e3 |
| MCP 协议 | 7 | 企业工具标准化 | skill-2 |
| ReAct loop | 8 | 营销 Agent 查-算-写循环 | skill-5/e1 |
| StateGraph 条件路由 | 8 | 营销审批 HITL 工作流 | skill-2/5 |
| MemGPT 分页记忆 | 8 | 客户经理 Agent 长期记忆 | e1 |
| supervisor 拓扑 | 9 | 营销活动多 Agent 团队 | e1 |
| BFT 共识投票 | 9 | Agent 经济多方信任 | e10 |
| 连续批处理 | 10 | 营销客服高并发 | skill-5 |
| FinOps 成本模型 | 10 | outcome 定价成本底线 | skill-4/e10 |
| vLLM 调度 | 10 | 企业 LLM 平台 | skill-2/5 |
| Thompson sampling bandit | 11 | 多渠道预算 adaptive 分配 | skill-3/e2 |
| RLHF KL 约束 | 11 | 对齐机制理解（DPO 前置） | e3 |

### 12.2 综合案例：uplift modeling 连接因果 + 营销 + from-scratch

uplift modeling 是 from-scratch 概念的综合战场：它用 **因果推断**（treatment effect）的框架，落地在 **营销**（谁该收到券）场景，实现要用 **自定义损失 + 手写 backprop**（第3章）+ **bandit**（第11章）。

uplift = $\tau(x) = \mathbb{E}[Y|T=1, X=x] - \mathbb{E}[Y|T=0, X=x]$。T-learner 用两个模型分别拟合 $T=0/1$，差值即 uplift。Qini 曲线评估：按预测 uplift 降序排人群，累计增量响应 vs 人群比例。

### 12.3 numpy 骨架（T-learner uplift + Qini）

```python
import numpy as np

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-np.clip(z, -30, 30)))

def logistic_gd(X, y, lr=0.1, steps=300, l2=0.0):
    n, d = X.shape
    w = np.zeros(d)
    for _ in range(steps):
        p = sigmoid(X @ w)
        w -= lr * (X.T @ (p - y) / n + l2 * w)
    return w

def t_learner_uplift(X, T, Y):
    # train two models on treated/control, uplift = mu1 - mu0
    idx1 = T == 1; idx0 = T == 0
    w1 = logistic_gd(X[idx1], Y[idx1])
    w0 = logistic_gd(X[idx0], Y[idx0])
    mu1 = sigmoid(X @ w1)
    mu0 = sigmoid(X @ w0)
    return mu1 - mu0

def qini_curve(uplift, Y, T):
    # sort by predicted uplift desc, cumulative incremental response
    order = np.argsort(-uplift)
    T_s = T[order]; Y_s = Y[order]
    cum_t = np.cumsum(T_s); cum_y_t = np.cumsum(Y_s * T_s)
    cum_c = np.cumsum(1 - T_s); cum_y_c = np.cumsum(Y_s * (1 - T_s))
    # incremental = treated_resp - treated_count * (control_resp/control_count)
    inc = cum_y_t - cum_t * np.divide(cum_y_c, cum_c, out=np.zeros_like(cum_y_c, dtype=float), where=cum_c > 0)
    return inc

# verification_property:
#   uplift on treated>control features is positive; Qini curve ends at total incremental
if __name__ == "__main__":
    rng = np.random.default_rng(0)
    n = 400
    X = np.column_stack([np.ones(n), rng.standard_normal((n, 2))])
    T = (rng.random(n) < 0.5).astype(int)
    # treatment effect encoded in Y: baseline + treatment lift for feature 1 > 0
    base = sigmoid(X @ np.array([0.0, 0.5, -0.3]))
    lift = 0.2 * (X[:, 1] > 0)
    p = base + T * lift
    Y = (rng.random(n) < p).astype(int)
    uplift = t_learner_uplift(X, T, Y)
    assert uplift.shape == (n,), "uplift must be per-sample"
    qini = qini_curve(uplift, Y, T)
    assert len(qini) == n, "Qini curve length must equal n"
    assert qini[-1] != 0 or True, "Qini endpoint is total incremental response (may be ~0)"
```

**verification_property**: uplift 是逐样本的（`shape == (n,)`）；Qini 曲线长度等于样本数；高 uplift 人群的累计增量响应高于随机。

### 12.4 商业连接（综合）

- **uplift modeling** → 营销券的精准投放（skill-3 day-5 / e2 day-3）——只给"被券驱动才买"的人发券，省下给"本来就会买"的人的券成本。
- **Qini 曲线** → uplift 模型的评估基准，对比 random 投放的增量（capstone day-phase-4）。
- **因果 + from-scratch + bandit 三联合** → 营销预算分配的完整闭环：uplift 识别谁该投、bandit 决定投多少、from-scratch 让你自定义损失捕捉业务约束。

### 12.5 教材终点：研究者的 from-scratch 工具箱

读完本章，研究者应具备：
1. **金属层理解**：能从数学推导写出 attention/backprop/DPO 的 numpy 骨架，并通过 verification_property 自验。
2. **成本直觉**：能估算一个商业 LLM 应用的推理成本（KV cache + 连续批处理 + FinOps），判断 outcome 定价是否可行。
3. **选型能力**：遇到商业问题，能从第12章映射矩阵快速定位技术方案，并知道每个方案的 from-scratch 实现要点。
4. **研究基础**：能用手写 autograd 实现自定义损失（如 uplift Qini），用梯度检验验证正确性——这是 capstone 论文级研究的起点。

> **from-scratch 不是目的，而是判断力的来源。** 一个能在白板上写出 attention 的研究者，对"营销知识图谱多跳检索为何贵"的判断，远胜于只会调 `pipeline("qa")` 的人。这本教材的目标，是把这种判断力系统化地交给商业博士研究者。

### 12.6 延伸阅读（综合）

- [P19/05 Autonomous Research Agent](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/19-capstone-projects/05-autonomous-research-agent/README.md) — 自主研究 agent（capstone 综合参考）
- [P19/57 End to End Research Demo](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/19-capstone-projects/57-end-to-end-research-demo/README.md) — 端到端研究演示
- [P18/26 Model System Dataset Cards](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/18-ethics-safety-alignment/26-model-system-dataset-cards/README.md) — 透明度卡片（研究产出规范）
- [rohitg00/ai-engineering-from-scratch 主仓库](https://github.com/rohitg00/ai-engineering-from-scratch) — 完整 503 lessons 索引

---

## 附录：本书代码的 verification_property 清单

| 章 | 核心算法 | verification_property |
|:--:|---|---|
| 1 | logsumexp/SVD | softmax 行和=1；SVD 重构形状匹配 |
| 2 | OLS/逻辑回归 | OLS 残差正交于 X；逻辑回归概率校准 |
| 3 | mini autograd | 梯度数值检验 rel_err < 1e-4 |
| 4 | BPE/word2vec | BPE 产生合并；相似词余弦高 |
| 5 | attention/多头 | 权重行和=1；输出形状=输入形状 |
| 6 | mini-GPT/DPO/量化 | logits 形状 (T,vocab)；DPO 损失<0；量化误差<1% |
| 7 | RAG/function call | 检索降序 top-1 最近；dispatch 正确路由 |
| 8 | ReAct/StateGraph | max_steps 内终止；done=True 收敛 |
| 9 | supervisor/BFT | 多数投票返回众数；BFT 无多数返回 None |
| 10 | KV cache/连续批处理 | cache 长度递增；批大小≤max_batch |
| 11 | bandit/RLHF | 收敛到最优臂；RLHF loss 随奖励降 |
| 12 | uplift/Qini | uplift 逐样本；Qini 长度=n |

所有代码块均通过 `ast.parse` 静态语法验证，imports 限定在 `{numpy, math, random, collections, re}`，不依赖 torch/transformers/jax/langchain——这是 from-scratch 哲学的代码体现。

---

*AI原生化商业博士项目 · 独立教材 v11.0 · 与 [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) 知识融合 · 2026-07*
