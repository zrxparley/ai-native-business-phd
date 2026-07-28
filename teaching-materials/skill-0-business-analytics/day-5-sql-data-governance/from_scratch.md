# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：技能0 AI商业分析基础 · Day 5 数据治理与SQL
> **scratch 哲学**：不调 sqlite3 / pandas.read_sql，手写关系代数 select/project/join，从 $\sigma_{\theta}(R)$ 直译到 list-of-dicts 骨架。

## scratch_topic

本单元 from-scratch 主题：**手写关系代数 select/project/join + 数据质量度量**。对应 rohitg00 P0/09 Data Management + P1/14 Norms and Distances。notes.md/starter.ipynb 用 sqlite3 + pandas.read_sql 构建 6 表电商 Schema 并执行 SQL DQL，本层把 SQL 的关系代数本质拆开：手写 $\sigma$（选择）/ $\pi$（投影）/ $\bowtie$（连接）/ GROUP BY 聚合，用 list-of-dicts + defaultdict 实现，让"SQL = 关系代数 + 优化器"这个 Codd 1970 的命题在白板级代码中显形。

## core_algorithm

关系代数是 SQL 的数学基础（Codd 1970）。三个基本运算：

**选择** $\sigma_\theta(R)$：从关系 $R$ 中筛选满足谓词 $\theta$ 的元组。

$$\sigma_\theta(R) = \{ t \in R \mid \theta(t) \}$$

**投影** $\pi_L(R)$：保留指定属性集 $L$，集合语义自动去重。

$$\pi_L(R) = \{ t[L] \mid t \in R \}$$

**连接** $R \bowtie_{R.a = S.b} S$：合并满足匹配条件的元组。朴素嵌套循环 $O(|R| \cdot |S|)$，哈希连接 $O(|R| + |S|)$--用哈希表索引 $S$ 的 $b$ 列，对 $R$ 每行查表：

$$R \bowtie S = \{ (t_R, t_S) \mid t_R \in R, t_S \in S, t_R.a = t_S.b \}$$

数据质量度量对应 P1/14 范数与距离。完整性（completeness）= 非空比例 $1 - \frac{\text{nulls}}{n}$；唯一性（uniqueness）= 去重后计数 $\frac{|\text{distinct}|}{n}$。记录匹配用 Hamming 距离 $d_H(r_1, r_2) = \sum_i \mathbb{1}[r_1^{(i)} \neq r_2^{(i)}]$ 检测重复记录。这些是 notes.md DAMA-DMBOK 六维度中可数值化的两个。

## code_artifact

```python
from collections import defaultdict

def select(table, predicate):
    # sigma_predicate(R): filter rows where predicate(row) is True
    return [row for row in table if predicate(row)]

def project(table, columns):
    # pi_columns(R): keep only specified columns, set semantics (dedup)
    seen, out = set(), []
    for row in table:
        key = tuple(row[c] for c in columns)
        if key not in seen:
            seen.add(key)
            out.append({c: row[c] for c in columns})
    return out

def hash_join(left, right, left_key, right_key):
    # R join S on R.left_key = S.right_key, hash table O(n+m) not nested loop O(n*m)
    index = defaultdict(list)
    for r in right:
        index[r[right_key]].append(r)
    out = []
    for l in left:
        for r in index.get(l[left_key], []):
            out.append({**l, **r})
    return out

def group_aggregate(table, group_col, agg_col, agg_fn):
    # GROUP BY + aggregate: bucket by group_col, reduce agg_col
    groups = defaultdict(list)
    for row in table:
        groups[row[group_col]].append(row[agg_col])
    return {g: agg_fn(vals) for g, vals in groups.items()}

def data_quality_audit(table, cols):
    # DAMA-DMBOK: completeness (non-null) + uniqueness (distinct ratio)
    n = len(table)
    return {"completeness": {c: 1 - sum(1 for r in table if r.get(c) is None) / n for c in cols},
            "uniqueness": {c: len(set(r.get(c) for r in table)) / n for c in cols}}

# verification_property:
#   select cardinality <= input; project dedups; hash_join matches nested-loop; group sums correct
if __name__ == "__main__":
    orders = [{"oid": 1, "cid": "C1", "amt": 100}, {"oid": 2, "cid": "C1", "amt": 200},
              {"oid": 3, "cid": "C2", "amt": 50}]
    custs = [{"cid": "C1", "name": "Alice"}, {"cid": "C2", "name": "Bob"}]
    assert len(select(orders, lambda r: r["amt"] > 60)) == 2
    assert len(project(orders, ["cid"])) == 2  # dedup C1
    joined = hash_join(orders, custs, "cid", "cid")
    assert len(joined) == 3 and joined[0]["name"] == "Alice"
    g = group_aggregate(joined, "cid", "amt", sum)
    assert g["C1"] == 300 and g["C2"] == 50
    dq = data_quality_audit(orders, ["oid", "amt"])
    assert dq["completeness"]["amt"] == 1.0 and dq["uniqueness"]["oid"] == 1.0
```

**verification_property**: `select` 筛选后行数 $\leq$ 输入；`project` 去重后 C1 只出现一次；`hash_join` 结果行数 = 匹配行数（3 行，Alice 关联 2 单）；`group_aggregate` 按客户聚合金额正确（C1=300, C2=50）；`data_quality_audit` 完整性=1.0（无缺失），唯一性=1.0（oid 全唯一）。

## connection_to_unit

1. **sqlite3 CREATE TABLE vs list-of-dicts**：solution.ipynb TODO1 用 `CREATE TABLE customers(... PRIMARY KEY ... FOREIGN KEY ...)` 设计 6 表 Schema，from-scratch 版用 list-of-dicts 表示关系--SQL 表的本质就是"元组的集合"（Codd 关系模型），CHECK/NOT NULL 约束在 from-scratch 版是 `data_quality_audit` 的事后审计，而非数据库引擎的事前拦截。
2. **SELECT-WHERE vs select()**：solution.ipynb TODO2 用 `SELECT * FROM orders WHERE amt > 60`，from-scratch 版用 `select(orders, lambda r: r["amt"] > 60)`--谓词 $\theta$ 在 SQL 是声明式，在 Python 是 lambda 函数，数学等价（都是 $\sigma_\theta(R)$）。
3. **SQL JOIN vs hash_join**：solution.ipynb TODO3 用 `INNER JOIN orders ON customers.cid = orders.cid`，from-scratch 版用 `hash_join`（哈希表索引 $O(n+m)$）--sqlite 优化器在小表用嵌套循环 $O(nm)$，大表用哈希/索引连接，from-scratch 让"join 算法选择"可见，这是 notes.md "索引提升查询性能"的底层。
4. **GROUP BY-HAVING vs group_aggregate**：solution.ipynb TODO4 用 `GROUP BY category HAVING SUM(amt) > 100`，from-scratch 版用 `group_aggregate` + Python `filter`--GROUP BY 是 `defaultdict(list)` 分桶，HAVING 是后过滤，两者在 from-scratch 版显式分离，不被 SQL 声明式语法遮蔽。

## deep_dive_links

- [P0/09 Data Management - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/00-setup-and-tooling/09-data-management/README.md) - 数据管理，关系模型与数据治理的工程基础
- [P1/14 Norms and Distances - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/14-norms-and-distances/README.md) - 范数与距离，数据质量度量（Hamming/Euclidean）的数学锚点

## exercises

1. 在本单元 `starter.ipynb` TODO3（SQL JOIN）运行后，用上面的 `hash_join` 在同一份电商数据上手动 join orders × customers × products（两次 hash_join），对比 sqlite3 三表 JOIN 的结果行数与内容，验证 $O(n+m)$ 哈希连接比嵌套循环 $O(nm)$ 快。
2. 为 `hash_join` 添加"LEFT JOIN"语义（保留左表无匹配行，右表字段填 None），对比 SQL `LEFT JOIN`；再实现"集合差" $R - S$（在 orders 中但不在 customers 中的 cid），用于检测外键完整性违规（notes.md 数据治理）。
3. 用 `data_quality_audit` 扩展到 notes.md DAMA-DMBOK 六维度中的"及时性"：给每行加 `created_at` 字段，检测 `created_at` 距今天数 > 阈值的记录比例，讨论 from-scratch 版与 Great Expectations 声明式规则的表达力差异。
4. TODO: 在 `practice.md` D3 的数据治理审计练习中，为本 from-scratch 实现添加"一致性"维度检测（如 `orders.cid` 必须存在于 `customers.cid`，用 `set` 差集运算），输出不一致记录列表，连接 notes.md "主数据管理单一真相源"概念。
