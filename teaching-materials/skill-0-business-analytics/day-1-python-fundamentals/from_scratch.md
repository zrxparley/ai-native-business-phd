# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：技能0 AI商业分析基础 · Day 1 Python编程基础
> **scratch 哲学**：不调 pandas.DataFrame.apply，手写 numpy 张量广播，从 shape 对齐规则直译到 numpy 骨架。

## scratch_topic

本单元 from-scratch 主题：**手写 numpy 张量运算 + 广播机制**。对应 rohitg00 P0/01 Dev Environment + P1/12 Tensor Operations。notes.md/starter.ipynb 用 pandas DataFrame + `df.apply(classify_customer, axis=1)` 做 RFM 客户分类，本层下沉到 pandas 的底层--numpy 张量：手写广播规则（shape 对齐 + 维度扩展 + 逐元素运算），让 notes.md "apply 比 for 循环快 10-100 倍"的向量化原理在白板级代码中显形。

## core_algorithm

numpy 广播（broadcasting）是向量化计算的底层机制，也是 pandas DataFrame 操作的物理基础。给定两个数组形状 $s_A \in \mathbb{Z}_{>0}^{d_A}$ 和 $s_B \in \mathbb{Z}_{>0}^{d_B}$，广播从右向左对齐维度，较短的形状左侧补 1。对每个对齐维度 $i$，若 $s_A^{(i)} = s_B^{(i)}$ 或 $\min(s_A^{(i)}, s_B^{(i)}) = 1$，则兼容，结果维度取较大值；否则不兼容，抛出 ValueError。

$$\text{result\_shape} = \left(\max(\tilde{s}_A^{(1)}, \tilde{s}_B^{(1)}), \dots, \max(\tilde{s}_A^{(n)}, \tilde{s}_B^{(n)})\right), \quad \tilde{s}_A = (\underbrace{1,\dots,1}_{n-d_A}, s_A)$$

扩展操作的几何含义：形状 $(1, n)$ 广播到 $(m, n)$ 等价于沿 axis 0 重复 $m$ 次，即 $B[i, j] = A[0, j], \forall i \in \{0,\dots,m-1\}$。numpy 生产实现用 stride trick 零拷贝模拟重复（不真正分配 $m \times n$ 内存），from-scratch 版用 `np.repeat` 显式物化，让"广播 = 沿轴重复"这个几何操作可见。

向量化原理与 RFM 的连接：`df['recency'] <= 30` 是标量 30 广播到形状 $(n,)$ 的列，产生布尔掩码 $(n,)$。这等价于 for 循环逐行比较，但在 C 层一次完成--广播把"逐行 Python 解释器开销"消除，这就是 notes.md "apply 比 for 快 10-100 倍"的数学根源。当 $n=10^6$ 时，广播版本毫秒级，for 循环版本秒级，差距正比于 $n$。

## code_artifact

```python
import numpy as np

def broadcast_shapes(shape_a, shape_b):
    # right-align shapes, pad shorter with 1s
    la, lb = len(shape_a), len(shape_b)
    n = max(la, lb)
    a = (1,) * (n - la) + tuple(shape_a)
    b = (1,) * (n - lb) + tuple(shape_b)
    out = []
    for i in range(n):
        if a[i] == b[i] or a[i] == 1 or b[i] == 1:
            out.append(max(a[i], b[i]))
        else:
            raise ValueError("incompatible dims")
    return tuple(out)

def broadcast_to(arr, target_shape):
    # manually expand via repeat (numpy uses stride trick, we materialize)
    cur = np.asarray(arr)
    while cur.ndim < len(target_shape):
        cur = np.expand_dims(cur, axis=0)
    for axis in range(len(target_shape)):
        if cur.shape[axis] == 1 and target_shape[axis] > 1:
            cur = np.repeat(cur, target_shape[axis], axis=axis)
    return cur

def vec_add(a, b):
    # element-wise add via explicit broadcast (not relying on numpy +)
    sa, sb = np.asarray(a).shape, np.asarray(b).shape
    tgt = broadcast_shapes(sa, sb)
    return broadcast_to(a, tgt) + broadcast_to(b, tgt)

def vec_mask_le(col, threshold):
    # vectorized comparison: scalar broadcast to column (essence of apply)
    return np.asarray(col) <= threshold

# verification_property:
#   broadcast_shapes((3,1),(1,4))==(3,4); vec_add matches numpy native +; mask picks correct rows
if __name__ == "__main__":
    assert broadcast_shapes((3, 1), (1, 4)) == (3, 4)
    assert broadcast_shapes((5,), (1, 5)) == (5, 5)
    A = broadcast_to(np.ones((1, 4)), (3, 4))
    assert A.shape == (3, 4) and np.all(A == 1.0)
    r = vec_add(np.ones((3, 1)), np.ones((1, 4)) * 2)
    assert r.shape == (3, 4) and np.all(r == 3.0)
    recency = np.array([10, 35, 25, 60, 5])
    mask = vec_mask_le(recency, 30)
    assert mask.sum() == 3
    assert np.allclose(r, np.ones((3, 1)) + np.ones((1, 4)) * 2)
```

**verification_property**: `broadcast_shapes((3,1),(1,4)) == (3,4)`；`vec_add` 的结果与 numpy 原生 `+` 运算数值一致；`vec_mask_le` 对 RFM recency 列产生的布尔掩码正确筛选出 `<= 30` 的行（sum=3）；`broadcast_to` 物化后的 shape 等于目标 shape。

## connection_to_unit

1. **pandas DataFrame 底层 vs from-scratch 张量**：notes.md/starter.ipynb 用 `pd.DataFrame(dict)` 加载营销数据、`df.apply(classify_customer, axis=1)` 做 RFM 分类，from-scratch 版手写 `broadcast_shapes` + `broadcast_to`，让 DataFrame 的列运算底层（numpy 广播）显形--pandas 的 `df['col'] * 2` 本质就是标量 2 广播到 $(n,)$ 列。
2. **apply 向量化 vs vec_mask_le**：solution.ipynb TODO3 用 `rfm.apply(classify_customer, axis=1)` 逐行分类（Python 解释器逐行调用），from-scratch 版用 `vec_mask_le(recency, 30)` 做列级广播比较--前者是"伪向量化"（apply 仍逐行），后者是"真向量化"（C 层一次完成），差距在百万行时从秒级变毫秒级。
3. **dtype 治理 vs np.asarray 统一类型**：notes.md 强调 customer_id 必须存 str 防前导零丢失，solution.ipynb TODO2 用 `df.dtypes` 检查类型；from-scratch 版的 `np.asarray(arr)` 在创建数组时强制统一 dtype，让"类型一致性决定运算可行性"这个 numpy 铁律可见--若列内混合 int/str，`np.asarray` 会退化为 object dtype，广播运算失效。
4. **ROI 聚合 vs 逐元素 reduce**：solution.ipynb TODO6 用 `merged['revenue'].sum()` 计算 ROI，from-scratch 版的 `vec_add` + `np.sum` 展示了"逐元素广播 + 归约"两步走--`merged['revenue']` 是 $(n,)$，`total_revenue = np.sum(vec_add(revenue_col, cost_col_neg))` 就是 ROI 的 from-scratch 等价。

## deep_dive_links

- [P0/01 Dev Environment - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/00-setup-and-tooling/01-dev-environment/README.md) - 开发环境与工具链，numpy 张量运算的工程基础
- [P1/12 Tensor Operations - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/12-tensor-operations/README.md) - 张量运算直觉，广播规则与 shape 变换的数学锚点

## exercises

1. 在本单元 `starter.ipynb` TODO3（RFM apply 分类）运行后，用上面的 `vec_mask_le` 重写 RFM 的 R≤30 / F≥3 判断为纯 numpy 布尔掩码，对比 `df.apply(classify_customer, axis=1)` 的性能（用 `%timeit`），验证"apply 向量化 ≈ 广播"的等价性与性能差距。
2. 实现 `broadcast_matmul(A, B)`：用 `broadcast_shapes` 对齐 batch 维度，再做矩阵乘法，处理 `(batch, m, n) × (n, p) -> (batch, m, p)` 的批量营销指标计算（如多个产品类别的利润矩阵同时算）。
3. 构造"广播失败"实验：调用 `broadcast_shapes((3,4), (4,3))`，验证抛出 ValueError；解释为什么 pandas 两个不同形状的 DataFrame 列不能直接相加--这是 dtype/shape 治理的底层原因。
4. TODO: 在 `practice.md` D2 的 RFM 向量化练习中，用 `broadcast_to` 替代 `df.apply`，将 R/F/M 三个标量阈值广播到 $(n,)$ 列做布尔掩码交集，实现纯 numpy 的 RFM 分类（无 for 循环、无 apply），并与 solution.ipynb 的 apply 版本对比结果一致性。
