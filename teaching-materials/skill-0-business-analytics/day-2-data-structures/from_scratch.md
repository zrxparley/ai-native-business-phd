# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：技能0 AI商业分析基础 · Day 2 数据结构与应用
> **scratch 哲学**：不调 numpy.linalg.solve，手写矩阵乘法 + 高斯消元，从 $C_{ij}=\sum_k A_{ik}B_{kj}$ 直译到 numpy 骨架。

## scratch_topic

本单元 from-scratch 主题：**手写向量/矩阵运算 + 线性系统求解**。对应 rohitg00 P1/02 Vectors Matrices Operations + P1/17 Linear Systems。notes.md/starter.ipynb 用 Python 内置 list/dict/set + collections + heapq 处理营销订单数据，本层下沉到线性代数层：手写矩阵乘法（三重循环）+ 高斯消元（部分主元法），让"dict O(1) 哈希查找 vs list O(n) 线性查找"的性能论证延伸到"矩阵乘法 O(n³) vs 高斯消元 O(n³)"的复杂度论证--数据结构选择决定性能，在矩阵层同样成立。

## core_algorithm

矩阵乘法是线性代数的基础操作，也是后续 Day 4 OLS 回归 $\hat\beta = (X^TX)^{-1}X^Ty$ 的计算单元。给定 $A \in \mathbb{R}^{m \times n}$, $B \in \mathbb{R}^{n \times p}$，矩阵乘积 $C = AB \in \mathbb{R}^{m \times p}$ 的每个元素为：

$$C_{ij} = \sum_{k=1}^{n} A_{ik} B_{kj}, \quad i \in \{1,\dots,m\}, \ j \in \{1,\dots,p\}$$

三重循环的复杂度为 $O(mnp)$，当 $m=n=p$ 时为 $O(n^3)$。numpy 的 `@` 运算符底层调 BLAS（Fortran/C 优化），比手写三重循环快 100-1000 倍，但数学等价--from-scratch 版让"矩阵乘法 = 行列内积"这个几何操作可见。

线性系统求解 $Ax = b$ 用高斯消元法。通过初等行变换将增广矩阵 $[A|b]$ 化为上三角 $[U|y]$，再回代求解。消元第 $k$ 步：对每行 $i > k$，乘数 $m_{ik} = A_{ik}/A_{kk}$，然后 $A_{i,:} \leftarrow A_{i,:} - m_{ik} A_{k,:}$, $b_i \leftarrow b_i - m_{ik} b_k$。部分主元法（partial pivoting）在第 $k$ 步选 $|A_{ik}|$ 最大的行交换到第 $k$ 行，避免 $A_{kk} \approx 0$ 导致的数值爆炸：

$$m_{ik} = \frac{A_{ik}}{A_{kk}}, \quad A_{ij} \leftarrow A_{ij} - m_{ik} A_{kj} \ (j \geq k), \quad b_i \leftarrow b_i - m_{ik} b_k$$

回代从最后一行开始：$x_n = b_n / A_{nn}$, $x_i = (b_i - \sum_{j>i} A_{ij} x_j) / A_{ii}$。高斯消元总复杂度 $O(n^3)$（消元 $O(n^3)$ + 回代 $O(n^2)$），与矩阵乘法同阶。这是 Day 4 OLS 闭式解 $(X^TX)^{-1}X^Ty$ 的底层计算路径--`np.linalg.solve` 内部就是 LU 分解（高斯消元的矩阵化）。

## code_artifact

```python
import numpy as np

def matmul(A, B):
    # C[i,j] = sum_k A[i,k] * B[k,j] -- explicit triple loop, no @ operator
    A = np.asarray(A, dtype=float)
    B = np.asarray(B, dtype=float)
    m, n = A.shape
    n2, p = B.shape
    assert n == n2, "inner dims mismatch"
    C = np.zeros((m, p))
    for i in range(m):
        for j in range(p):
            s = 0.0
            for k in range(n):
                s += A[i, k] * B[k, j]
            C[i, j] = s
    return C

def gauss_solve(A, b):
    # solve Ax = b via Gaussian elimination + partial pivoting + back substitution
    A = np.asarray(A, dtype=float).copy()
    b = np.asarray(b, dtype=float).copy()
    n = A.shape[0]
    for k in range(n):
        piv = k + int(np.argmax(np.abs(A[k:, k])))
        if piv != k:
            A[[k, piv]] = A[[piv, k]]
            b[[k, piv]] = b[[piv, k]]
        for i in range(k + 1, n):
            m = A[i, k] / A[k, k]
            A[i, k:] -= m * A[k, k:]
            b[i] -= m * b[k]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - A[i, i+1:] @ x[i+1:]) / A[i, i]
    return x

# verification_property:
#   matmul matches numpy @; gauss_solve recovers x for known Ax=b; pivoting avoids div-by-zero
if __name__ == "__main__":
    A = np.array([[2., 1., -1.], [-3., -1., 2.], [-2., 1., 2.]])
    b = np.array([8., -11., -3.])
    x = gauss_solve(A, b)
    assert np.allclose(A @ x, b), "Ax must equal b"
    assert np.allclose(matmul(np.eye(3), A), A), "matmul with identity"
    assert abs(x[0] - 2.0) < 1e-9 and abs(x[1] - 3.0) < 1e-9 and abs(x[2] + 1.0) < 1e-9
    rng = np.random.default_rng(0)
    M = rng.standard_normal((5, 5))
    assert np.allclose(matmul(M, np.eye(5)), M)
    y = rng.standard_normal(5)
    xs = gauss_solve(M, y)
    assert np.allclose(M @ xs, y), "random system solvable"
```

**verification_property**: `matmul` 与 numpy 原生 `@` 数值一致（含单位阵）；`gauss_solve` 对已知 $Ax=b$（解 $x=[2,3,-1]$）精确恢复解向量；部分主元法避免 $A_{kk}\approx 0$ 时的除零；残差 $A\hat{x}-b \approx 0$。

## connection_to_unit

1. **复杂度论证的延续**：notes.md 教"list O(n) vs dict O(1) 差 10 万倍"，from-scratch 版的 `matmul` 三重循环 $O(n^3)$ 与 numpy `@`（BLAS 优化）对比，复杂度论证从"数据结构层"延伸到"矩阵层"--`matmul` 手写版在 $n=1000$ 时约秒级，numpy `@` 毫秒级，差距来自 BLAS 的分块/向量化，与 dict vs list 的"算法复杂度差距"同构。
2. **namedtuple schema vs numpy 矩阵**：solution.ipynb TODO6 用 `namedtuple` 设计 Product/Order 不可变 schema，from-scratch 版用 numpy 2D 数组表示矩阵--两者都是"结构化数据容器"，但 namedtuple 是行式（每条记录一个 tuple），numpy 矩阵是列式（数值运算优化），这正是 notes.md "Apache Arrow 列式 vs list-of-dicts 行式"的底层映射。
3. **BFS 树遍历 vs 高斯消元主元选择**：solution.ipynb TODO6 用 `deque` 做 BFS 遍历产品分类树，from-scratch 版的 `gauss_solve` 在每步选 $|A_{ik}|$ 最大的行做主元--两者都是"遍历 + 选择"算法，BFS 选的是树节点访问顺序，主元法选的是数值稳定性最大的行，数据结构选择（deque vs argmax）服务于不同的目标。
4. **heapq Top-K vs 矩阵乘法复杂度**：notes.md 教 `heapq.nlargest` 是 $O(n \log k)$，from-scratch 版的 `matmul` 是 $O(n^3)$--两者都是"用数据结构降低复杂度"的范例：heap 用最小堆避免全排序，矩阵乘法用三重循环（理论下界 $O(n^{2.37})$ Strassen），复杂度论证是 Day 2 的核心能力。

## deep_dive_links

- [P1/02 Vectors Matrices Operations - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/02-vectors-matrices-operations/README.md) - 向量矩阵运算 from scratch，矩阵乘法与线性变换的数学锚点
- [P1/17 Linear Systems - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/17-linear-systems/README.md) - 线性系统求解，高斯消元与 LU 分解的工程实现

## exercises

1. 在本单元 `starter.ipynb` TODO1（list 排序/筛选）运行后，用上面的 `matmul` 实现"订单-产品矩阵乘法"：构造订单矩阵 $O \in \mathbb{R}^{m \times n}$（m 订单 × n 产品）与价格向量 $p \in \mathbb{R}^{n}$，验证 $Op$ 给出每订单金额，对比 `df.groupby().sum()` 的结果。
2. 将 `gauss_solve` 扩展为支持非方阵的最小二乘解：解 normal equation $X^TX\beta = X^Ty$（先 `matmul(X.T, X)` 再 `gauss_solve`），连接 Day 4 OLS 闭式解 $(X^TX)^{-1}X^Ty$，验证两者给出相同 $\hat\beta$。
3. 构造病态矩阵（Hilbert matrix $H_{ij} = 1/(i+j-1)$）测试 `gauss_solve` 的数值稳定性：$n=5,10,15$ 时观察残差 $\|A\hat{x}-b\|$ 的增长，讨论部分主元法是否足够（连接 Day 6 数值稳定）。
4. TODO: 在 `practice.md` D3 的 heapq Top-K 练习中，为本 from-scratch `matmul` 添加 $O(n^3)$ 复杂度验证：测量 $n=50,100,200,400$ 的运行时间，验证 $t(n)/t(n/2) \approx 8$（立方增长），与 `heapq.nlargest` 的 $O(n \log k)$ 对比。
